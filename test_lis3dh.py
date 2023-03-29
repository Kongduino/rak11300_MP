import time
from machine import I2C
from pinout import *
from lis3dh import LIS3DH

#i2c obj
i2c = I2C(id = 1, scl = machine.Pin(PIN_WIRE_SCL), sda = machine.Pin(PIN_WIRE_SDA))
lis = LIS3DH(i2c, 0x18)

print("Device ID: {}".format(hex(lis.ID)))

while True:
    accel = lis.get_acceleration()
    print(accel['x'], accel['y'], accel['z'])
    time.sleep(0.1)