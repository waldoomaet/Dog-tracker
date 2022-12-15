from services.savers.saver_factory import SaverType
from services.savers.saver_manager import SaverManager
from services.serial_service import SerialWrapper
from services.config_service import ConfigService
from services.parser_service import parse_output
from serial import Serial

config = ConfigService()

port = config["serial"]["port"]
baudrate = config["serial"]["baudrate"]
timeout = config["serial"]["timeout"]

serial = SerialWrapper(Serial(port, baudrate=baudrate, timeout=timeout))
saver = SaverManager()
saver.add(SaverType.TINY_DB_SAVER)

while True:
    output = serial.readline_until()
    parsed_output = parse_output(output)
    print(parsed_output)
    saver.insert({"output": parsed_output})
