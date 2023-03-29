import time
from machine import I2C
from pinout import *
from lps22hb import LPS22HB

#i2c obj
i2c = I2C(id = 1, scl = machine.Pin(PIN_WIRE_SCL), sda = machine.Pin(PIN_WIRE_SDA))
lps = LPS22HB(i2c)

print("Device ID: {}".format(hex(lps.ID)))
pre = lps.get_pressure()
print("Pressure: {:.2f} HPa".format(pre))