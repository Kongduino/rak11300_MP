import time
from machine import I2C
from pinout import *
from opt3001 import *

#i2c obj
i2c = I2C(id = 1, scl = machine.Pin(PIN_WIRE_SCL), sda = machine.Pin(PIN_WIRE_SDA))
opt = OPT3001(i2c)

print("Manufacturer ID: {}".format(hex(opt.manufacturerID)))
print("Device ID: {}".format(hex(opt.deviceID)))

opt.write_config_reg(I2C_LS_CONFIG_CONT_FULL_800MS)
while(True):
  print(opt.read_lux_float())
  time.sleep(1)
