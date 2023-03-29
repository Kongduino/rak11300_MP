from pinout import *
from machine import SoftI2C, Pin, I2C
from STC3x import *
from bme680i import *
import sys

#i2c = SoftI2C(scl = machine.Pin(PIN_WIRE_SCL), sda = machine.Pin(PIN_WIRE_SDA), freq=400000)
i2c = I2C(id = 1, scl = machine.Pin(PIN_WIRE_SCL), sda = machine.Pin(PIN_WIRE_SDA), freq=400000)

bme = BME680_I2C(i2c, address=0x76)

mySensor = STC3xSensor(i2c)
if mySensor == True:
    print(" . mySensor init failed!")
    sys.exit()
print("STC3xSensor init ok.")

success = mySensor.setBinaryGas(STC3X_BINARY_GAS_CO2_AIR_25)
if success != True:
    print(" . Set Binary Gas failed!")
    sys.exit()
print(" - Set Binary Gas ok.")

success = mySensor.forcedRecalibration(0.0, 100)
if success != True:
    print(" . Forced recalibration failed!")
    sys.exit()
print(" - Forced recalibration ok.")

success = mySensor.enableAutomaticSelfCalibration()
if success != True:
    print(" . Automatic self-calibration failed!")
    sys.exit()
print(" - Automatic self-calibration ok.")

while True:
    # Arduino's good old loop()
    print("\nBME")
    T = bme.temperature
    H = int(bme.humidity*100)/100.0
    P = bme.pressure
    print(" - Temperature: {:.2f} °C".format(T))
    print(" - Humidity: {:.2f}%".format(H))
    print(" - Pressure: {:.2f} HPa".format(P))
    print(" . setHumidity...")
    success = mySensor.setHumidity(H)
    print(" . setTemperature...")
    success = mySensor.setTemperature(T)
    print(" . setPressure...")
    success = mySensor.setPressure(P)

    print("Gas Concentration")
    rawCO2, calcCO2, _ = mySensor.measureGasConcentration()
    print("Raw CO2 index: {}".format(rawCO2))
    print("CO2 concentration: {:.2f}%".format(calcCO2))
    
    # Temperature is what we passed.
    time.sleep(10)