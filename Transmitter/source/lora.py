from machine import UART
from uart_wrapper import UartWrapper

class AtCommand:
    AT = "AT"
    SEND = "AT+SEND"
    ADDRESS = "AT+ADDRESS"
    NETWORKID = "AT+NETWORKID"
    BAND = "AT+BAND"
    PARAMETER="AT+PARAMETER"

# TODO: would be cool to also implement the errors with Python Exceptions
class AtResponse:
    OK = "+OK"
    RESET = "+RESET"
    READY = "+READY"

# TODO: The data transmission is really slow. Some config on lora modules is necessary, and some data compression too.
# TODO: Need to see the power saving options for lora (at the end of the day simply cutting off power could be an option)
# TODO: Would be usefull to have some function or method to handle lora module configuration. I think best 
# for that would be to have some classes for setted configurations and a method to load them, but I'll do that
# when the time for testing efficiency and range comes
class Lora(UartWrapper):
    def __init__(self, uart: UART) -> None:
        super().__init__(uart)

    def get(self, command: str) -> str:
        output = self._writeline(f"{command}?", return_immediate_response=True)
        output_start = output.find("=") + 1
        return output[output_start:]

    def at(self) -> str:
        return self._writeline(AtCommand.AT, return_immediate_response=True)

    def set_address(self, address: int) -> str:
        return self._writeline(f"{AtCommand.ADDRESS}={address}", return_immediate_response=True)

    def set_network_id(self, id: int) -> str:
        return self._writeline(f"{AtCommand.NETWORKID}={id}", return_immediate_response=True)
    
    def set_band(self, band: int) -> str:
        return self._writeline(f"{AtCommand.BAND}={band}", return_immediate_response=True)
    
    def set_parameter(self, spreading_factor: int, bandwith: int, coding_rate: int, programmed_preamble: int) -> str:
        return self._writeline(f"{AtCommand.PARAMETER}={spreading_factor},{bandwith},{coding_rate},{programmed_preamble}", return_immediate_response=True)

    def send(self, address: int, message: str) -> str:
        return self._writeline(f"{AtCommand.SEND}={address},{len(message)},{message}", return_immediate_response=True)
    
