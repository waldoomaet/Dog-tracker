from machine import UART, Timer, Pin
from time import sleep
from lora import Lora, AtCommand
from gps import Gps

def toggle_led(t):
    global count
    if count >= max:
        led.value(not led.value())
        count = 0
    else:
        count+=1

lora = Lora(UART(1, baudrate=115200, tx=23, rx=22))
gps = Gps(UART(2, baudrate=9600))

led = Pin(2, Pin.OUT)
count = 0
max = 10
led.on()

tim = Timer(-1)
tim.init(period=100, mode=Timer.PERIODIC, callback=toggle_led)
# TODO: Right now this code is really unefficient threadwise, so this needs some optimization
# TODO: Would be cool to keep track of wich files have changed so we only put those, thus saving some time
# TODO: Need a way to measure RAM and ROM consumption
while True:
    try:
        output = gps.get_rmc()
        if output:
            max = 10
            print(str(output.__dict__))
            lora.send(30, str(output.__dict__))
            sleep(6)
        else:
            max = 1
            print("No complete data...", output)
    except Exception as err:
        max = 1
        print(f"Error: {err}")
        print(f"Error: {str(err)}")
