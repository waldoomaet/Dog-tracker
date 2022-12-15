from services.serial_service import SerialWrapper
from services.config_service import ConfigService
from serial import Serial

config = ConfigService()

port = config["serial"]["port"]
baudrate = config["serial"]["baudrate"]
timeout = config["serial"]["timeout"]

serial = SerialWrapper(Serial(port, baudrate=baudrate, timeout=timeout))

while True:
    print(serial.writeline(input(">"), return_immediate_response=True))
