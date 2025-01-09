from os import path
from time import sleep
import canopen
import canopen.objectdictionary
import canopen.pdo
import canopen.pdo.base
import canopen.sdo
import can.interfaces.pcan
import uptime
import logging



# Logging setup, naming all logging in this file as Power Unit
logger = logging.getLogger('Power Unit')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class power_unit:
    eds_files = {}
    network: canopen.Network
    motor_node: canopen.RemoteNode
    
    def __init__(self):
        self.eds_files['emdrive'] = path.abspath(path.join(path.dirname(__file__), 'EmDrive.eds'))
        self.network = canopen.Network()
    
    def connect(self):
        self.network.connect(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)
    
    def disconnect(self):
        self.network.disconnect()

    def pdo_received(self, event):
        print("PDO received: ", event)

    def init_emdrive(self, node_id=1):
        # Create the motor slave node
        with open(self.eds_files['emdrive'], 'r', encoding="utf-8") as file:
            self.motor_node = canopen.RemoteNode(node_id, file)
        self.network.add_node(self.motor_node)
        
        for tpdo_number, tpdo in self.motor_node.tpdo.items():
            tpdo: canopen.pdo.base.PdoMap
            tpdo.add_callback(self.pdo_received)
            pass
        
        for rpdo_number, rpdo in self.motor_node.rpdo.items():
            rpdo: canopen.pdo.base.PdoMap
            rpdo.add_callback(self.pdo_received)
            pass
        
        # Set the motor node to operational state
        logging.info("Setting NMT reset to the motor")
        self.motor_node.nmt.state = 'RESET'
        sleep(1)
        logging.info("Sending NMT pre-operational to the motor")
        self.motor_node.nmt.state = 'PRE-OPERATIONAL'
        sleep(1)
        logging.info("Sending NMT operational to the motor")
        self.motor_node.nmt.state = 'OPERATIONAL'
        sleep(1)

    def get_sdo(self, index: int, subindex: int):
        try:
            return self.motor_node.sdo[index][subindex].raw
        except RuntimeError:
            return None
        except TypeError:
            return None
        except canopen.sdo.SdoCommunicationError:
            return None
    
    def send_sdo(self, index: int, subindex: int, value):
        if not self.network.bus:
            return False
        try:
            self.motor_node.sdo[index][subindex].raw = value
            return True
        except RuntimeError:
            return False
        except TypeError:
            return False
        except AttributeError:
            return False
        except canopen.sdo.SdoCommunicationError:
            return False

    def send_emdrive_nmt_operational(self):
        try:
            self.motor_node.nmt.state = 'OPERATIONAL'
            return True
        except RuntimeError:
            return False

    def send_emdrive_nmt_reset(self):
        try:
            self.motor_node.nmt.state = 'RESET'
            return True
        except RuntimeError:
            return False

    def send_emdrive_torque_request(self, torque: int):
        return self.send_sdo(0x3010, 0x04, torque)

    def send_emdrive_on(self):
        # 0x3010 sub 0x01, set to a value of 1 to turn on the motor
        return self.send_sdo(0x3010, 0x01, 1)

    def send_emdrive_off(self):
        # 0x3010 sub 0x01, set to a value of 0 to turn off the motor
        return self.send_sdo(0x3010, 0x01, 0)

    def send_emdrive_clear_errors(self):
        # 0x3000 sub 0x01, set to a value of 0 to clear errors
        return self.send_sdo(0x3010, 0x01, 2)

    def get_key_statuses(self) -> dict:
        data_dict = {
            'state': self.get_sdo(0x3010, 0x02),
            'motor_temp': self.get_sdo(0x3053, 0x01),
            'capacitor_temp': self.get_sdo(0x3074, 0x01),
            'bridge1_temp': self.get_sdo(0x3074, 0x02),
            'rpm': self.get_sdo(0x3101, 0x01),
            'logic_voltage': self.get_sdo(0x3070, 0x03),
            'stud_voltage': self.get_sdo(0x3071, 0x00),
            'phase_current': self.get_sdo(0x31F0, 0x01),
            'load_power': self.get_sdo(0x31F0, 0x06),
            'calculated_dc_current': self.get_sdo(0x31F0, 0x07),
            'calculated_bridge_loss': self.get_sdo(0x31F0, 0x0A),
            'torque_request': self.get_sdo(0x3010, 0x04),
        }
        return data_dict

# Example usage
if __name__ == "__main__":
    master = power_unit()
    master.connect()
    master.init_emdrive()
    
    input("Press Enter to reset...")
    
    master.send_emdrive_nmt_reset()
    
    input("Press Enter to operational...")
    
    master.send_emdrive_nmt_operational()
    
    input("Press Enter to set on...")
    
    master.send_emdrive_on()
    
    try:
        while True:
            master.network.update()
            uptime_seconds = uptime.uptime()
            print(uptime_seconds)
            for i in master.get_key_statuses():
                print(i, master.get_key_statuses()[i])
            sleep(1)
    except KeyboardInterrupt:
        master.send_emdrive_off()
        print("EmDrive off signal sent")