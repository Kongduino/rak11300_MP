from pinout import *
from bme680i import *
from machine import I2C, Pin
import time

i2c = I2C(id = 1, scl = machine.Pin(PIN_WIRE_SCL), sda = machine.Pin(PIN_WIRE_SDA))
bme = BME680_I2C(i2c, address=0x76)
INTERVAL = const(10)
lastReading = 0
bme.sea_level_pressure= 1008.5

while True:
    if (time.ticks_ms() - lastReading) / 1000 > INTERVAL:
        print("\nTemperature: {:.2f} °C".format(bme.temperature))
        print("Humidity: {:.2f}%".format(bme.humidity))
        print("Pressure: {:.2f} HPa".format(bme.pressure))
        print("MSL: {:.2f} HPa".format(bme.sea_level_pressure))
        print("Altitude: {:d} m".format(int(bme.altitude)))
        print("Gas: {:d}".format(int(bme.gas)))
        lastReading = time.ticks_ms()