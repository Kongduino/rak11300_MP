import time
from machine import I2C
from pinout import *
from lps33hb import LPS33HB

#i2c obj
i2c = I2C(id = 1, scl = machine.Pin(PIN_WIRE_SCL), sda = machine.Pin(PIN_WIRE_SDA))
lps = LPS33HB(i2c)

print("Device ID: {}".format(hex(lps.ID)))
temp, pressure = lps.get_temp_pressure()
print("Temperature: {:.2f}°C".format(temp))
print("Pressure: {:.2f} HPa".format(pressure))
