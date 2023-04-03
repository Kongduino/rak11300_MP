from sx1262 import SX1262
import time, json, lzw, gc
from hexdump import hexDump
from machine import I2C, Pin
from pinout import *
from bme680i import *
from bme280_float import *
from sgp40 import SGP40
from voc_algorithm import VOCAlgorithm
from STC3x import *
from opt3001 import *

print("\n=============================")
print(" Starting...")
LEDG = Pin(23, Pin.OUT) # Green LED
LEDB = Pin(24, Pin.OUT) # Green LED
switch = Pin(WB_IO3, Pin.IN) # Button / switch to force sending a packet.

print(" I2C...")
i2c = I2C(id = 1, scl = machine.Pin(PIN_WIRE_SCL), sda = machine.Pin(PIN_WIRE_SDA))

# Variables for the sensors, installed or not
hasBME680 = False
hasBME280 = False
bme = None
hasSGP40 = False
sgp40 = None
hasSTC3x = False
stc31 = None
hasOPT3001 = False
opt = None

# Let's see what's connected
rslt = i2c.scan()
print(rslt)
if rslt.count(0x76) == 1: # RAK1906
    ID = hex(i2c.readfrom_mem(0x76, 0xD0, 1))
    print("ID = {}".format(ID))
    if ID == b'61':
        hasBME680 = True
        print(" [√] BME680")
        bme = BME680_I2C(i2c, address=0x76)
        bme.sea_level_pressure = 1016.8
        # You can change this via LoRa
        # Send a JSON packet with 'cmd':'MSL:1006.3' inside, the rest will be ignored
    elif ID == 0x60:
        hasBME280 = True
        print(" [√] BME280")
        bme = BME280(i2c, address = 0x76)
        bme.sea_level_pressure = 1013.25
        # You can change this via LoRa
        # Send a JSON packet with 'cmd':'MSL:1006.3' inside, the rest will be ignored

if rslt.count(0x59) == 1: # RAK12047
    hasSGP40 = True
    print(" [√] SGP40")
    sgp40 = SGP40(i2c, 0x59)
    voc_algorithm = VOCAlgorithm()
    voc_algorithm.vocalgorithm_init()

if rslt.count(0x59) == 1: # RAK12047
    print(" [√] STC31")
    stc31 = STC3xSensor(i2c)
    if stc31 == None:
        print(" . stc31 init failed!")
        sys.exit()
    hasSTC3x = True
    print(" - Serial Number: {}".format(stc31.serialNumber))
    print(" - Product Number: {}".format(stc31.productNumber))
    print(" - Set Binary Gas")
    success = stc31.setBinaryGas(STC3X_BINARY_GAS_CO2_AIR_25)
    if success != True:
        print(" . Set Binary Gas failed!")
        sys.exit()

if rslt.count(0x44) == 1: # RAK1903
    print(" [√] OPT3001")
    opt = OPT3001(i2c)
    hasOPT3001 = True
    print(" - Manufacturer ID: {}".format("0x%0.2X" % opt.manufacturerID))
    print(" - Device ID: {}".format("0x%0.2X" % opt.deviceID))
    opt.write_config_reg(I2C_LS_CONFIG_CONT_FULL_800MS)

# variables for the loop
INTERVAL = const(180000) # 180 seconds
lastReading = 0
randomBuffer = None # we will stock up 256 random bytes
randomIndex = -1
randomMax = const(256)

print(" [√] SX1262")
sx = SX1262(ledrcv = LEDG) # green LED will blink on receive
print("=============================")

def lora_cb(events):
    global sx
    if events & SX1262.TX_DONE:
        # Tx done successfully
        print(' TX done.')
        sx.startReceive() # put sx1262 back in receive mode.
        LEDB.low()
    elif events & SX1262.RX_DONE:
        # incoming!
        msg, err = sx.recv()
        error = SX1262.STATUS[err]
        print(msg)
        print(error)
        try:
            # is this JSON?
            payload=json.loads(msg)
            sender = payload.get('from')
            if sender == None:
                # no from, no love.
                return
            if sender != "BastMobile":
                # no BastMobile, no love.
                return
            cmd = payload.get('cmd')
            if cmd == None:
                # no command, no love.
                return
            if cmd.startswith("MSL:") and hasBME680 == True:
                # change MSL air pressure.
                MSL = float(cmd[4:])
                if MSL >= 652.5 and MSL <= 1083.8:
                    bme.sea_level_pressure = MSL
                    print("Set new MSL to {} HPa".format(MSL))
            # on this model we could change other parameters like frequency,
            # BW, SF etc
        except:
            pass
    gc.collect()
    print("Free memory: {}".format(gc.mem_free()))

sx.begin(freq=868, bw=125.0, sf=12, cr=5, syncWord=0x12,
         power=22, currentLimit=100.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=False, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=True, blocking=True)
sx.setBlockingCallback(False, lora_cb)

# fill up a buffer with random bytes
randomBuffer = sx.fillRandom(randomMax)
randomIndex = -1
hexDump(randomBuffer)

def getRNDBytes(numBytes):
    # get numBytes bytes from the random buffer
    global randomBuffer, randomMax, randomIndex
    randomIndex += 1
    if randomIndex+numBytes >= randomMax:
        randomBuffer = sx.fillRandom(randomMax)
        randomIndex = 0
    data = bytearray(numBytes)
    for i in range(0, numBytes):
        data[i] = randomBuffer[randomIndex+i]
    randomIndex += (numBytes - 1)
    return data

def getRNDByte():
    # get one byte from the random buffer
    global randomBuffer, randomMax, randomIndex
    randomIndex += 1
    if randomIndex == randomMax:
        randomBuffer = sx.fillRandom(randomMax)
        randomIndex = 0
    return randomBuffer[randomIndex].to_bytes(1, 'big')

def getRNDHexaByte():
    # get one byte from the random buffer as hexadecimal
    b = getRNDByte()
    return hex(b).decode()

while True:
    if switch.value() == 1:
        while switch.value() == 1:
            # debounce
            pass
        lastReading = 0 # reset lastReading ==> send packet
    if (time.ticks_ms() - lastReading) > INTERVAL:
        print("\n+------------------------+")
        print("| Time for a new packet! |")
        print("+------------------------+")
        LEDB.high()
        msg = {}
        msg['UUID'] = getRNDHexaByte() + getRNDHexaByte() + getRNDHexaByte() + getRNDHexaByte()
        if hasBME680 == True:
            T = bme.temperature
            H = int(bme.humidity*100)/100.0
            P = int(bme.pressure*100)/100.0
            A = int(bme.altitude*100)/100.0
            G = bme.gas
            msg['T'] = T
            msg['H'] = H
            msg['P'] = P
            msg['A'] = A
            msg['G'] = G
            print(" - Temperature: {:.2f} °C".format(T))
            print(" - Humidity: {:.2f}%".format(H))
            print(" - Pressure: {:.2f} HPa".format(P))
            print(" - MSL: {:.2f} HPa".format(bme.sea_level_pressure))
            print(" - Altitude: {:d} m".format(int(A)))
            print(" - Gas: {:d}".format(int(G)))
        else:
            print("No BME680")
        if hasSGP40 == True:
            R = sgp40.measure_raw()
            print(" - VOC raw: {:d}".format(int(R)))
            index = voc_algorithm.vocalgorithm_process(R)
            print(" - VOC Index: {:d}".format(index))
            msg['R'] = R
            msg['I'] = index
        if hasSTC3x == True:
            if hasBME680 == True:
                print("   . setTemperature")
                success = stc31.setTemperature(T)
                print("   . setHumidity")
                success = stc31.setHumidity(H)
                print("   . setPressure")
                success = stc31.setPressure(P)
            rawCO2, calcCO2, _ = stc31.measureGasConcentration()
            print(" - raw CO2: {}".format(rawCO2))
            print(" - CO2 concentration: {:.2f}%".format(calcCO2))
            msg['C'] = float("{:.2f}".format(calcCO2))
        if hasSTC3x == True:
            LUX = opt.read_lux_float()
            msg['L'] = int(LUX*100)/100.0
            print("Lux: {}".format(msg['L']))
        msg = json.dumps(msg)
        len0 = len(msg)
        msg0 = bytearray(lzw.compress(msg))
        len1 = len(msg0)
        savings = (1 - (len1/len0))*100
        print("Sending:\n  `{}`\n  {} vs {} bytes --> {:.2f}% savings".format(msg, len1,len0, savings))
        sx.standby()
        sx.send(msg0)
        lastReading = time.ticks_ms()
