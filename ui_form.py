# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDoubleSpinBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStatusBar,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_WakaControlPanel(object):
    def setupUi(self, WakaControlPanel):
        if not WakaControlPanel.objectName():
            WakaControlPanel.setObjectName(u"WakaControlPanel")
        WakaControlPanel.resize(655, 695)
        self.centralwidget = QWidget(WakaControlPanel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.Shape.WinPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Label_PCANStatus_3 = QLabel(self.frame_4)
        self.Label_PCANStatus_3.setObjectName(u"Label_PCANStatus_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Label_PCANStatus_3.sizePolicy().hasHeightForWidth())
        self.Label_PCANStatus_3.setSizePolicy(sizePolicy1)
        self.Label_PCANStatus_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.Label_PCANStatus_3)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.spin_CapacitorTempLimit = QDoubleSpinBox(self.frame)
        self.spin_CapacitorTempLimit.setObjectName(u"spin_CapacitorTempLimit")
        self.spin_CapacitorTempLimit.setMaximum(1000.000000000000000)
        self.spin_CapacitorTempLimit.setValue(120.000000000000000)

        self.gridLayout_2.addWidget(self.spin_CapacitorTempLimit, 5, 2, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 6, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 5, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 4, 1, 1, 1)

        self.spin_MotorTempLimit = QDoubleSpinBox(self.frame)
        self.spin_MotorTempLimit.setObjectName(u"spin_MotorTempLimit")
        self.spin_MotorTempLimit.setMaximum(1000.000000000000000)
        self.spin_MotorTempLimit.setValue(59.000000000000000)

        self.gridLayout_2.addWidget(self.spin_MotorTempLimit, 4, 2, 1, 1)

        self.spin_RPMLimit_5s = QDoubleSpinBox(self.frame)
        self.spin_RPMLimit_5s.setObjectName(u"spin_RPMLimit_5s")
        self.spin_RPMLimit_5s.setMaximum(10000.000000000000000)
        self.spin_RPMLimit_5s.setValue(3400.000000000000000)

        self.gridLayout_2.addWidget(self.spin_RPMLimit_5s, 6, 2, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 7, 1, 1, 1)

        self.spin_LogTimeLimit = QSpinBox(self.frame)
        self.spin_LogTimeLimit.setObjectName(u"spin_LogTimeLimit")

        self.gridLayout_2.addWidget(self.spin_LogTimeLimit, 7, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.Label_PCANStatus_4 = QLabel(self.frame_4)
        self.Label_PCANStatus_4.setObjectName(u"Label_PCANStatus_4")
        sizePolicy1.setHeightForWidth(self.Label_PCANStatus_4.sizePolicy().hasHeightForWidth())
        self.Label_PCANStatus_4.setSizePolicy(sizePolicy1)
        self.Label_PCANStatus_4.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.Label_PCANStatus_4)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.text_TestName = QLineEdit(self.frame_5)
        self.text_TestName.setObjectName(u"text_TestName")

        self.gridLayout_4.addWidget(self.text_TestName, 1, 1, 1, 1)

        self.text_LogFolder = QLineEdit(self.frame_5)
        self.text_LogFolder.setObjectName(u"text_LogFolder")

        self.gridLayout_4.addWidget(self.text_LogFolder, 0, 1, 1, 1)

        self.label_name = QLabel(self.frame_5)
        self.label_name.setObjectName(u"label_name")

        self.gridLayout_4.addWidget(self.label_name, 1, 0, 1, 1)

        self.label_folder = QLabel(self.frame_5)
        self.label_folder.setObjectName(u"label_folder")

        self.gridLayout_4.addWidget(self.label_folder, 0, 0, 1, 1)

        self.tool_LogBrowse = QToolButton(self.frame_5)
        self.tool_LogBrowse.setObjectName(u"tool_LogBrowse")

        self.gridLayout_4.addWidget(self.tool_LogBrowse, 0, 2, 1, 1)

        self.button_StartLog = QPushButton(self.frame_5)
        self.button_StartLog.setObjectName(u"button_StartLog")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.button_StartLog.sizePolicy().hasHeightForWidth())
        self.button_StartLog.setSizePolicy(sizePolicy3)

        self.gridLayout_4.addWidget(self.button_StartLog, 1, 2, 1, 1)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)

        self.spin_LogTime = QDoubleSpinBox(self.frame_5)
        self.spin_LogTime.setObjectName(u"spin_LogTime")
        self.spin_LogTime.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.spin_LogTime.sizePolicy().hasHeightForWidth())
        self.spin_LogTime.setSizePolicy(sizePolicy4)

        self.gridLayout_4.addWidget(self.spin_LogTime, 2, 1, 1, 2)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.gridLayout_3.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy5)
        self.frame_2.setFrameShape(QFrame.Shape.WinPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.label)

        self.table_LiveData = QTableWidget(self.frame_2)
        self.table_LiveData.setObjectName(u"table_LiveData")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.table_LiveData.sizePolicy().hasHeightForWidth())
        self.table_LiveData.setSizePolicy(sizePolicy6)

        self.verticalLayout_5.addWidget(self.table_LiveData)


        self.gridLayout_3.addWidget(self.frame_2, 2, 0, 1, 2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.Shape.WinPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Label_PCANStatus = QLabel(self.frame_3)
        self.Label_PCANStatus.setObjectName(u"Label_PCANStatus")
        sizePolicy1.setHeightForWidth(self.Label_PCANStatus.sizePolicy().hasHeightForWidth())
        self.Label_PCANStatus.setSizePolicy(sizePolicy1)
        self.Label_PCANStatus.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.Label_PCANStatus)

        self.Frame_PCAN_Status = QFrame(self.frame_3)
        self.Frame_PCAN_Status.setObjectName(u"Frame_PCAN_Status")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.Frame_PCAN_Status.sizePolicy().hasHeightForWidth())
        self.Frame_PCAN_Status.setSizePolicy(sizePolicy7)
        self.Frame_PCAN_Status.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_PCAN_Status.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.Frame_PCAN_Status)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Button_Connect = QPushButton(self.Frame_PCAN_Status)
        self.Button_Connect.setObjectName(u"Button_Connect")
        sizePolicy3.setHeightForWidth(self.Button_Connect.sizePolicy().hasHeightForWidth())
        self.Button_Connect.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.Button_Connect)

        self.Check_Transmitting = QCheckBox(self.Frame_PCAN_Status)
        self.Check_Transmitting.setObjectName(u"Check_Transmitting")
        self.Check_Transmitting.setEnabled(True)
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.Check_Transmitting.sizePolicy().hasHeightForWidth())
        self.Check_Transmitting.setSizePolicy(sizePolicy8)
        self.Check_Transmitting.setChecked(False)

        self.horizontalLayout.addWidget(self.Check_Transmitting)


        self.verticalLayout.addWidget(self.Frame_PCAN_Status)

        self.Label_PCANStatus_2 = QLabel(self.frame_3)
        self.Label_PCANStatus_2.setObjectName(u"Label_PCANStatus_2")
        sizePolicy1.setHeightForWidth(self.Label_PCANStatus_2.sizePolicy().hasHeightForWidth())
        self.Label_PCANStatus_2.setSizePolicy(sizePolicy1)
        self.Label_PCANStatus_2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.Label_PCANStatus_2)

        self.Frame_Motor_Controls = QFrame(self.frame_3)
        self.Frame_Motor_Controls.setObjectName(u"Frame_Motor_Controls")
        self.Frame_Motor_Controls.setFrameShape(QFrame.Shape.StyledPanel)
        self.Frame_Motor_Controls.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.Frame_Motor_Controls)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Button_Reset = QPushButton(self.Frame_Motor_Controls)
        self.Button_Reset.setObjectName(u"Button_Reset")

        self.gridLayout.addWidget(self.Button_Reset, 1, 0, 1, 1)

        self.DoubleSpin_MaxTorque = QDoubleSpinBox(self.Frame_Motor_Controls)
        self.DoubleSpin_MaxTorque.setObjectName(u"DoubleSpin_MaxTorque")
        sizePolicy4.setHeightForWidth(self.DoubleSpin_MaxTorque.sizePolicy().hasHeightForWidth())
        self.DoubleSpin_MaxTorque.setSizePolicy(sizePolicy4)
        self.DoubleSpin_MaxTorque.setMaximum(1000.000000000000000)
        self.DoubleSpin_MaxTorque.setValue(50.000000000000000)

        self.gridLayout.addWidget(self.DoubleSpin_MaxTorque, 5, 1, 1, 1)

        self.Button_Off = QPushButton(self.Frame_Motor_Controls)
        self.Button_Off.setObjectName(u"Button_Off")

        self.gridLayout.addWidget(self.Button_Off, 1, 1, 1, 1)

        self.label_8 = QLabel(self.Frame_Motor_Controls)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 2)

        self.label_2 = QLabel(self.Frame_Motor_Controls)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.DoubleSpin_CurrentTorque = QDoubleSpinBox(self.Frame_Motor_Controls)
        self.DoubleSpin_CurrentTorque.setObjectName(u"DoubleSpin_CurrentTorque")
        self.DoubleSpin_CurrentTorque.setReadOnly(True)
        self.DoubleSpin_CurrentTorque.setMaximum(1000.000000000000000)
        self.DoubleSpin_CurrentTorque.setSingleStep(0.100000000000000)
        self.DoubleSpin_CurrentTorque.setValue(0.000000000000000)

        self.gridLayout.addWidget(self.DoubleSpin_CurrentTorque, 4, 1, 1, 1)

        self.Button_On = QPushButton(self.Frame_Motor_Controls)
        self.Button_On.setObjectName(u"Button_On")

        self.gridLayout.addWidget(self.Button_On, 0, 1, 1, 1)

        self.Slider_TorqueRequest = QSlider(self.Frame_Motor_Controls)
        self.Slider_TorqueRequest.setObjectName(u"Slider_TorqueRequest")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.Slider_TorqueRequest.sizePolicy().hasHeightForWidth())
        self.Slider_TorqueRequest.setSizePolicy(sizePolicy9)
        self.Slider_TorqueRequest.setMaximum(50000)
        self.Slider_TorqueRequest.setSingleStep(100)
        self.Slider_TorqueRequest.setPageStep(1000)
        self.Slider_TorqueRequest.setValue(0)
        self.Slider_TorqueRequest.setTracking(True)
        self.Slider_TorqueRequest.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.Slider_TorqueRequest, 3, 0, 2, 1)

        self.Button_Operational = QPushButton(self.Frame_Motor_Controls)
        self.Button_Operational.setObjectName(u"Button_Operational")

        self.gridLayout.addWidget(self.Button_Operational, 0, 0, 1, 1)

        self.label_3 = QLabel(self.Frame_Motor_Controls)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.DoubleSpin_MinTorque = QDoubleSpinBox(self.Frame_Motor_Controls)
        self.DoubleSpin_MinTorque.setObjectName(u"DoubleSpin_MinTorque")
        sizePolicy4.setHeightForWidth(self.DoubleSpin_MinTorque.sizePolicy().hasHeightForWidth())
        self.DoubleSpin_MinTorque.setSizePolicy(sizePolicy4)
        self.DoubleSpin_MinTorque.setMinimum(-1000.000000000000000)
        self.DoubleSpin_MinTorque.setMaximum(1000.000000000000000)

        self.gridLayout.addWidget(self.DoubleSpin_MinTorque, 6, 1, 1, 1)


        self.verticalLayout.addWidget(self.Frame_Motor_Controls)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 2, 1)

        WakaControlPanel.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(WakaControlPanel)
        self.statusbar.setObjectName(u"statusbar")
        WakaControlPanel.setStatusBar(self.statusbar)

        self.retranslateUi(WakaControlPanel)

        QMetaObject.connectSlotsByName(WakaControlPanel)
    # setupUi

    def retranslateUi(self, WakaControlPanel):
        WakaControlPanel.setWindowTitle(QCoreApplication.translate("WakaControlPanel", u"WakaControlPanel", None))
        self.Label_PCANStatus_3.setText(QCoreApplication.translate("WakaControlPanel", u"Limits", None))
        self.label_6.setText(QCoreApplication.translate("WakaControlPanel", u"RPM limit (5s)", None))
        self.label_5.setText(QCoreApplication.translate("WakaControlPanel", u"Capacitor temp limit", None))
        self.label_4.setText(QCoreApplication.translate("WakaControlPanel", u"Motor temp limit", None))
        self.label_9.setText(QCoreApplication.translate("WakaControlPanel", u"Log timer (minutes) ", None))
        self.Label_PCANStatus_4.setText(QCoreApplication.translate("WakaControlPanel", u"Log file folder", None))
        self.label_name.setText(QCoreApplication.translate("WakaControlPanel", u"Name", None))
        self.label_folder.setText(QCoreApplication.translate("WakaControlPanel", u"Folder", None))
        self.tool_LogBrowse.setText(QCoreApplication.translate("WakaControlPanel", u"...", None))
        self.button_StartLog.setText(QCoreApplication.translate("WakaControlPanel", u"Start", None))
        self.label_7.setText(QCoreApplication.translate("WakaControlPanel", u"Current log time", None))
        self.spin_LogTime.setPrefix("")
        self.spin_LogTime.setSuffix(QCoreApplication.translate("WakaControlPanel", u" min", None))
        self.label.setText(QCoreApplication.translate("WakaControlPanel", u"Status variables", None))
        self.Label_PCANStatus.setText(QCoreApplication.translate("WakaControlPanel", u"PCAN Status (Press this button to connect)", None))
        self.Button_Connect.setText(QCoreApplication.translate("WakaControlPanel", u"Disconnected", None))
        self.Check_Transmitting.setText(QCoreApplication.translate("WakaControlPanel", u"Transmitting", None))
        self.Label_PCANStatus_2.setText(QCoreApplication.translate("WakaControlPanel", u"Motor control", None))
        self.Button_Reset.setText(QCoreApplication.translate("WakaControlPanel", u"Reset", None))
        self.Button_Off.setText(QCoreApplication.translate("WakaControlPanel", u"Off", None))
        self.label_8.setText(QCoreApplication.translate("WakaControlPanel", u"Torque", None))
        self.label_2.setText(QCoreApplication.translate("WakaControlPanel", u"Max torque", None))
        self.Button_On.setText(QCoreApplication.translate("WakaControlPanel", u"On", None))
        self.Button_Operational.setText(QCoreApplication.translate("WakaControlPanel", u"Operational", None))
        self.label_3.setText(QCoreApplication.translate("WakaControlPanel", u"Min torque", None))
    # retranslateUi

