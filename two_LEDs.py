import time
from machine import Pin
LEDG = Pin(23, Pin.OUT)
LEDB = Pin(24, Pin.OUT)

while True:
    LEDG.high()
    LEDB.low()
    time.sleep(0.8)
    LEDB.high()
    LEDG.low()
    time.sleep(0.8)
