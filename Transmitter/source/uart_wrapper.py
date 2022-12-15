from machine import UART

class UartWrapper:
    _uart = None
    def __init__(self, uart: UART) -> None:
        self._uart = uart

    def _readline_until(self, until: str=None) -> str:
        # TODO: I need some sort of timeout here
        while True:
            output: bytes = self._uart.readline()
            if output:
                try:
                    output_str = output.rstrip().decode("ASCII")
                    if until == None or (output_str == until or until in output_str):
                        return output_str
                except Exception as err:
                    print(f"Error: {err}")
                    print(f"Error: {str(err)}")
                    return "Error..."

    def _writeline(self, to_write: str, eol: str='\r\n', return_immediate_response: bool = False) -> str:
        self._uart.write(f"{to_write}{eol}".encode("ASCII"))
        if return_immediate_response:
            return self._readline_until()
        return None