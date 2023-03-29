from pinout import *
from bme680i import *
from machine import I2C, Pin
from sx1262 import SX1262
import time

LEDG = Pin(23, Pin.OUT)
LEDB = Pin(24, Pin.OUT)
i2c = I2C(id = 1, scl = machine.Pin(PIN_WIRE_SCL), sda = machine.Pin(PIN_WIRE_SDA))
bme = BME680_I2C(i2c, address=0x76)
bme.sea_level_pressure= 1008.5
sx = SX1262()

def cb(events):
    global sx
    if events & SX1262.RX_DONE:
        msg, err = sx.recv()
        error = SX1262.STATUS[err]
        print(msg)
        print(error)

sx.begin(freq=868, bw=125.0, sf=12, cr=5, syncWord=0x12,
         power=22, currentLimit=100.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=False, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=True, blocking=True)

sx.setBlockingCallback(False, cb)
interval = 20000
start = time.ticks_ms() - interval - 1

while True:
    if time.ticks_ms() - start >= interval:
        LEDB.high()
        T = bme.temperature
        H = bme.humidity
        P = bme.pressure
        A = bme.altitude
        G = bme.gas
        msg = '"T":{:.2f}, "H":{:.2f}, "P":{:.2f}, "A":{:.2f}, "G":{:d}'.format(T, H, P, A, int(G))
        msg = '{' + msg + '}'
        print("\nTemperature: {:.2f} °C".format(T))
        print("Humidity: {:.2f}%".format(H))
        print("Pressure: {:.2f} HPa".format(P))
        print("MSL: {:.2f} HPa".format(bme.sea_level_pressure))
        print("Altitude: {:d} m".format(int(A)))
        print("Gas: {:d}".format(int(G)))
        print("Sending: {}".format(msg))
        sx.send(bytearray(msg))
        start = time.ticks_ms()
        LEDB.low()



