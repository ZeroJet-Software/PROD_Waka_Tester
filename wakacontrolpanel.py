# This Python file uses the following encoding: utf-8
import sys
from datetime import datetime
import os
import ctypes
from ctypes import wintypes

# pylint: disable=no-name-in-module
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QHeaderView, QFileDialog
from PySide6.QtCore import QRunnable, QThreadPool, QTimer, QEventLoop
from PySide6.QtCore import Slot, QObject, Signal
import nptdms

from modules.power_unit import power_unit
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_WakaControlPanel

class connect_worker(QRunnable):
    class Signals(QObject):
        update_button_text = Signal(str)
    
    def __init__(self, pu:power_unit, button:QPushButton, status:bool):
        super().__init__()
        self.power_unit = pu
        self.button = button
        self.status = status
        self.signals = self.Signals()
        self.signals.update_button_text.connect(self.button.setText)
    
    def run(self):
        print("Connect button clicked")
        if self.status:
            print("Disconnecting")
            self.power_unit.disconnect()
            self.signals.update_button_text.emit("Disconnected")
        else:
            print("Connecting")
            self.signals.update_button_text.emit("Connecting")
            self.power_unit.connect()
            self.signals.update_button_text.emit("Connected")
            self.power_unit.init_emdrive()

class TorqueWorker(QRunnable):
    class Signals(QObject):
        update_transmitting_status = Signal(bool)
        start_timer = Signal(int)

    def __init__(self, pu: power_unit, get_torque_func):
        super().__init__()
        self.power_unit = pu
        self.get_torque_func = get_torque_func
        self.timer = QTimer()
        self.timer.timeout.connect(self.send_torque)
        self.signals = self.Signals()
        self.signals.start_timer.connect(self.timer.start)

    def send_torque(self):
        torque = self.get_torque_func()
        result = self.power_unit.send_emdrive_torque_request(torque)
        self.signals.update_transmitting_status.emit(result)
        # print(f"Torque sent: {torque}, result: {result}")

    def run(self):
        loop = QEventLoop()
        self.signals.start_timer.emit(100)  # 0.1 seconds
        loop.exec()

class StatusWorker(QRunnable):
    class Signals(QObject):
        update_status = Signal(dict)
        start_timer = Signal(int)

    def __init__(self, pu: power_unit):
        super().__init__()
        self.power_unit = pu
        self.timer = QTimer()
        self.timer.timeout.connect(self.get_status)
        self.signals = self.Signals()
        self.signals.start_timer.connect(self.timer.start)

    def get_status(self):
        statuses = self.power_unit.get_key_statuses()
        self.signals.update_status.emit(statuses)

    def run(self):
        loop = QEventLoop()
        self.signals.start_timer.emit(500)  # 0.5 seconds
        loop.exec()

class WakaControlPanel(QMainWindow):
    connected = False
    power_unit = power_unit()
    torque_worker = None
    status_worker = None
    status_dict = {}
    is_logging = False
    tdms_writer = None
    logfilepath: str
    log_start_time: datetime
    rpm_limit_triggers = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_WakaControlPanel()
        self.ui.setupUi(self)
        # Set default log folder and name
        default_log_folder = self.get_desktop_path() + "\\WakaLogs"
        
        if not os.path.exists(default_log_folder):
            os.makedirs(default_log_folder)
        self.ui.text_LogFolder.setText(default_log_folder)
        self.ui.text_TestName.setText("Test")
        self.ui.Button_Operational.clicked.connect(self.operational_clicked)
        self.ui.Button_Reset.clicked.connect(self.reset_clicked)
        self.ui.Button_On.clicked.connect(self.on_clicked)
        self.ui.Button_Off.clicked.connect(self.off_clicked)
        self.ui.Button_Connect.clicked.connect(self.connect_button_clicked)
        
        self.ui.DoubleSpin_MaxTorque.valueChanged.connect(self.update_slider_bounds)
        self.ui.DoubleSpin_MinTorque.valueChanged.connect(self.update_slider_bounds)
        
        self.ui.Slider_TorqueRequest.valueChanged.connect(self.update_torque_request)
        self.ui.DoubleSpin_CurrentTorque.valueChanged.connect(self.update_slider_from_spinbox)
        
        self.torque_worker = TorqueWorker(self.power_unit, self.get_torque_value)
        self.torque_worker.signals.update_transmitting_status.connect(self.update_transmitting_status)
        self.torque_worker_thread = QThreadPool.globalInstance()
        
        self.status_worker = StatusWorker(self.power_unit)
        self.status_worker.signals.update_status.connect(self.update_live_data)
        self.status_worker_thread = QThreadPool.globalInstance()
        
        self.setup_live_data_table()
        self.ui.tool_LogBrowse.clicked.connect(self.open_log_folder_dialog)
        self.ui.button_StartLog.clicked.connect(self.handle_start_log)

    def get_desktop_path(self):
        CSIDL_DESKTOP = 0x0000
        SHGFP_TYPE_CURRENT = 0
        buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_DESKTOP, None, SHGFP_TYPE_CURRENT, buf)
        return buf.value

    def update_slider_bounds(self):
        max_bounds = self.ui.DoubleSpin_MaxTorque.value()
        min_bounds = self.ui.DoubleSpin_MinTorque.value()
        self.ui.Slider_TorqueRequest.setMinimum(min_bounds * 1000)
        self.ui.Slider_TorqueRequest.setMaximum(max_bounds * 1000)
        self.update_torque_request()
        print(f"Slider bounds updated: {min_bounds * 1000} - {max_bounds * 1000}")
    
    def update_torque_request(self):
        torque = self.get_torque_value()
        self.ui.DoubleSpin_CurrentTorque.blockSignals(True)
        self.ui.DoubleSpin_CurrentTorque.setValue(torque)
        self.ui.DoubleSpin_CurrentTorque.blockSignals(False)
        self.power_unit.send_emdrive_torque_request(torque)
    
    def get_torque_value(self) -> float:
        return self.ui.Slider_TorqueRequest.value() / 1000
    
    def update_slider_from_spinbox(self):
        torque = self.ui.DoubleSpin_CurrentTorque.value()
        self.ui.Slider_TorqueRequest.setValue(torque * 1000)
        self.power_unit.send_emdrive_torque_request(torque)
    
    @Slot()
    def operational_clicked(self):
        print("Operate button clicked")
        self.power_unit.send_emdrive_nmt_operational()
    
    @Slot()
    def reset_clicked(self):
        print("Reset button clicked")
        self.power_unit.send_emdrive_nmt_reset()
    
    @Slot()
    def on_clicked(self):
        print("On button clicked")
        self.power_unit.send_emdrive_on()
    
    @Slot()
    def off_clicked(self):
        print("Off button clicked")
        self.power_unit.send_emdrive_off()
    
    @Slot()
    def connect_button_clicked(self):
        pool = QThreadPool.globalInstance()
        worker = connect_worker(self.power_unit, self.ui.Button_Connect, self.connected)
        self.connected = not self.connected
        pool.start(worker)
        
        if self.connected:
            self.torque_worker_thread.start(self.torque_worker)
            self.status_worker_thread.start(self.status_worker)
        else:
            self.torque_worker.timer.stop()
            self.status_worker.timer.stop()
            self.ui.Check_Transmitting.setChecked(False)

    @Slot(bool)
    def update_transmitting_status(self, status: bool):
        self.ui.Check_Transmitting.setChecked(status)

    @Slot(dict)
    def update_live_data(self, statuses: dict):
        self.status_dict = statuses
        self.populate_live_data_table()
        if self.is_logging:
            self.log_data("Key Data", statuses)

    def log_data(self, group_name: str, data: dict):
        with nptdms.TdmsWriter(self.logfilepath, mode='a', index_file=True) as tdms_writer:
            timestamp = datetime.now()
            group = nptdms.GroupObject(group_name)
            channel_ts = nptdms.ChannelObject(group_name, "Timestamp", [timestamp])
            tdms_writer.write_segment([nptdms.RootObject(), group, channel_ts])

            test_time = (timestamp - self.log_start_time).total_seconds()
            channel_dt = nptdms.ChannelObject(group_name, "Test Time (s)", [test_time])
            self.ui.spin_LogTime.setValue(test_time/60)
            
            tdms_writer.write_segment([nptdms.RootObject(), group, channel_dt])
            for key, value in data.items():
                if value is not None:
                    channel = nptdms.ChannelObject(group_name, key, [value])
                    tdms_writer.write_segment([nptdms.RootObject(), group, channel])

    def setup_live_data_table(self):
        self.ui.table_LiveData.setColumnCount(2)
        self.ui.table_LiveData.setRowCount(20)
        self.ui.table_LiveData.setHorizontalHeaderLabels(['Key', 'Value'])
        self.ui.table_LiveData.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_LiveData.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.table_LiveData.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

    def populate_live_data_table(self):
        self.ui.table_LiveData.setRowCount(0)
        for row, (key, value) in enumerate(self.status_dict.items()):
            self.ui.table_LiveData.insertRow(row)
            self.ui.table_LiveData.setItem(row, 0, QTableWidgetItem(key))
            self.ui.table_LiveData.setItem(row, 1, QTableWidgetItem(str(value)))
        self.apply_safety_limits()
    
    def apply_safety_limits(self):
        capacitor_temp_limit = self.ui.spin_CapacitorTempLimit.value()
        motor_temp_limit = self.ui.spin_MotorTempLimit.value()
        rpm_limit_5s = self.ui.spin_RPMLimit_5s.value()
        
        if 'capacitor_temp' in self.status_dict and self.status_dict['capacitor_temp'] > capacitor_temp_limit:
            self.power_unit.send_emdrive_off()
            print("Capacitor temperature exceeded limit, motor turned off")
        if 'motor_temp' in self.status_dict and self.status_dict['motor_temp'] > motor_temp_limit:
            self.power_unit.send_emdrive_off()
            print("Motor temperature exceeded limit, motor turned off")
        if 'rpm' in self.status_dict and self.status_dict['rpm'] > rpm_limit_5s:
            self.rpm_limit_triggers += 1
            if self.rpm_limit_triggers > 10:  # Data comes in every 0.5 seconds
                self.power_unit.send_emdrive_off()
                print("RPM exceeded limit for 5 seconds, motor turned off")
        else:
            self.rpm_limit_triggers = 0

    def closeEvent(self, event):
        self.set_torque_to_zero()
        self.power_unit.send_emdrive_off()
        self.power_unit.send_emdrive_nmt_reset()
        self.power_unit.disconnect()
        self.stop_logging()
        
        try:
            del self.power_unit
        except AttributeError:
            pass
        event.accept()
        super().closeEvent(event)

    def set_torque_to_zero(self):
        self.ui.Slider_TorqueRequest.setValue(0)
        self.ui.DoubleSpin_CurrentTorque.setValue(0)
        self.power_unit.send_emdrive_torque_request(0)
        print("Torque set to 0")

    def open_log_folder_dialog(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Log Folder")
        if folder:
            self.ui.text_LogFolder.setText(folder)
        print(f"Log folder selected: {folder}")

    def handle_start_log(self):
        if not self.is_logging:
            try:
                folder = self.ui.text_LogFolder.text()
                test_name = self.ui.text_TestName.text()
                self.logfilepath = f"{folder}/{test_name}.tdms"
                with nptdms.TdmsWriter(self.logfilepath, mode='a', index_file=True):
                    pass
                self.log_start_time = datetime.now()
                self.is_logging = True
                self.ui.button_StartLog.setText("Stop")
                self.ui.spin_LogTime.setValue(0)
            except:
                self.ui.button_StartLog.setText("error")
        else:
            self.stop_logging()
    

    def stop_logging(self):
        if self.tdms_writer:
            self.tdms_writer.close()
        self.is_logging = False
        self.ui.button_StartLog.setText("Start Log")

if __name__ == "__main__":
    
    print("Please ensure you have installed the PEAK PCAN drivers")
    print("https://www.peak-system.com/quick/DrvSetup")
    app = QApplication(sys.argv)
    widget = WakaControlPanel()
    widget.show()
    sys.exit(app.exec())