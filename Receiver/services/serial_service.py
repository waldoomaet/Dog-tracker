import time
from serial import Serial

class SerialWrapper:
    _serial:Serial = None
    def __init__(self, serial: Serial) -> None:
        self._serial = serial

    def readline_until(self, until: str=None) -> str:
        while True:
            output = self._serial.readline()
            if output:
                output_str = output.rstrip().decode("ASCII")
                if until == None or (output_str == until or until in output_str):
                    return output_str

    def writeline(self, to_write: str, eol: str='\r\n', return_immediate_response: bool = False) -> str:
        self._serial.write(f"{to_write}{eol}".encode("ASCII"))
        if return_immediate_response:
            return self.readline_until()
        return None