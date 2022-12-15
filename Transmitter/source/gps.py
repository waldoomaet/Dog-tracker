from machine import UART
from uart_wrapper import UartWrapper

class RmcOutput:
    latitude: float = None
    # North/South
    ns_indicator: str = None
    longitude: float = None
    # East/West
    ew_indicator: str = None
    date: str = None
    time: str = None
    def __init__(self, latitude: str, longitude: str, ns: str, ew:str, date: str, time: str) -> None:
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.ns_indicator = ns
        self.ew_indicator = ew
        self.date = date
        self.time = time

# TODO: Would be usefull to have some function or method to handle gps configuration (if possible, need to keep reading the docs)
# TODO: Need to see the power saving options for gps (at the end of the day simply cutting off power could be an option)
class Gps(UartWrapper):
    def __init__(self, uart: UART) -> None:
        super().__init__(uart)
    
    def get_any(self) -> str:
        return self._readline_until()

    def get_rmc(self) -> RmcOutput:
        data_list = self._readline_until("RMC").split(',')
        # Status check
        if data_list[2] == 'A':
            return RmcOutput(data_list[3], data_list[5], data_list[4], data_list[6], data_list[9], data_list[1])
        else:
            return None