import time
from machine import SoftI2C, I2C

STC3X_COMMAND_SET_RELATIVE_HUMIDITY = const(0x3624)
STC3X_COMMAND_SET_TEMPERATURE = const(0x361E)
STC3X_COMMAND_SET_PRESSURE = const(0x362F)
STC3X_COMMAND_MEASURE_GAS_CONCENTRATION = const(0x3639)
STC3X_COMMAND_FORCED_RECALIBRATION = const(0x3661)
STC3X_COMMAND_AUTOMATIC_CALIBRATION_ENABLE = const(0x3FEF)
STC3X_COMMAND_AUTOMATIC_CALIBRATION_DISABLE = const(0x3F6E)
STC3X_COMMAND_PREPARE_READ_STATE = const(0x3752)
STC3X_COMMAND_READ_WRITE_STATE = const(0xE133)
STC3X_COMMAND_APPLY_STATE = const(0x3650)
STC3X_COMMAND_SELF_TEST = const(0x365B)
STC3X_COMMAND_ENTER_SLEEP_MODE = const(0x3677)
STC3X_COMMAND_READ_PRODUCT_IDENTIFIER_1 = const(0x367C)
STC3X_COMMAND_READ_PRODUCT_IDENTIFIER_2 = const(0xE102)

STC3X_BINARY_GAS_CO2_N2_100 = const(0)
STC3X_BINARY_GAS_CO2_AIR_100 = const(1)
STC3X_BINARY_GAS_CO2_N2_25 = const(2)
STC3X_BINARY_GAS_CO2_AIR_25 = const(3)

STC3x_COMMAND_SET_BINARY_GAS = const(0x3615)
STC3x_COMMAND_DISABLE_CRC = const(0x3768)

class STC3xSensor:
    def __init__(self, wirePort, i2cAddress=0x2c):
        self._i2cAddress = i2cAddress
        self._wirePort = wirePort
        self._lastReadTimeMillis = 0
        success = self.disableCRC()
        self.serialNumber, self.productNumber = self.getProductIdentifier()
        if self.serialNumber == '':
            print("Error! Couldn't get the serial number!")
            return
        return

    def getProductIdentifier(self):
        success = self.sendCommandOnly(STC3X_COMMAND_READ_PRODUCT_IDENTIFIER_1)
        success &= self.sendCommandOnly(STC3X_COMMAND_READ_PRODUCT_IDENTIFIER_2)
        if success == False:
            print("STC3x did not acknowledge STC3X_COMMAND_READ_PRODUCT_IDENTIFIER")
            return ['', '']
        receivedBytes = self._wirePort.readfrom(self._i2cAddress, 12)
        #print(receivedBytes)
        PN = b''
        SN = b''
        PN = self.convertHexToASCII(receivedBytes[0] >> 4)
        PN = PN + self.convertHexToASCII(receivedBytes[0] & 0x0F)
        PN = PN + self.convertHexToASCII(receivedBytes[1] >> 4)
        PN = PN + self.convertHexToASCII(receivedBytes[1] & 0x0F)
        PN = PN + self.convertHexToASCII(receivedBytes[2] >> 4)
        PN = PN + self.convertHexToASCII(receivedBytes[2] & 0x0F)
        PN = PN + self.convertHexToASCII(receivedBytes[3] >> 4)
        PN = PN + self.convertHexToASCII(receivedBytes[3] & 0x0F)
        SN = self.convertHexToASCII(receivedBytes[4] >> 4)
        SN = SN + self.convertHexToASCII(receivedBytes[4] & 0x0F)
        SN = SN + self.convertHexToASCII(receivedBytes[5] >> 4)
        SN = SN + self.convertHexToASCII(receivedBytes[5] & 0x0F)
        SN = SN + self.convertHexToASCII(receivedBytes[6] >> 4)
        SN = SN + self.convertHexToASCII(receivedBytes[6] & 0x0F)
        SN = SN + self.convertHexToASCII(receivedBytes[7] >> 4)
        SN = SN + self.convertHexToASCII(receivedBytes[7] & 0x0F)
        SN = SN + self.convertHexToASCII(receivedBytes[8] >> 4)
        SN = SN + self.convertHexToASCII(receivedBytes[8] & 0x0F)
        SN = SN + self.convertHexToASCII(receivedBytes[9] >> 4)
        SN = SN + self.convertHexToASCII(receivedBytes[9] & 0x0F)
        SN = SN + self.convertHexToASCII(receivedBytes[10] >> 4)
        SN = SN + self.convertHexToASCII(receivedBytes[10] & 0x0F)
        SN = SN + self.convertHexToASCII(receivedBytes[11] >> 4)
        SN = SN + self.convertHexToASCII(receivedBytes[11] & 0x0F)
        return [SN.decode(), PN.decode()]

    def sendCommandOnly(self, command):
        packet = []
        if command>255:
            packet.append((command>>8) & 0xFF)
        packet.append(command & 0xFF)
        if type(self._wirePort) == SoftI2C:
            self._wirePort.start()
        success = self._wirePort.writeto(self._i2cAddress, bytearray(packet))
        if type(self._wirePort) == SoftI2C:
            self._wirePort.stop()
        return success == len(packet)

    def sendCommandParam16(self, command, param16):
        packet = []
        packet.append((command>>8) & 0xFF)
        packet.append(command & 0xFF)
        packet.append((param16>>8) & 0xFF)
        packet.append(param16 & 0xFF)
        success = self._wirePort.writeto(self._i2cAddress, bytearray(packet))
        return success == len(packet)

    def convertHexToASCII(self, digit):
        if (digit <= 9):
            digit += 0x30
            return digit.to_bytes(1, 'big')
        else:
            digit += 55
            return digit.to_bytes(1, 'big')

    def disableCRC(self):
        return self.sendCommandOnly(STC3x_COMMAND_DISABLE_CRC)

    def setBinaryGas(self, binaryGas):
        return (self.sendCommandParam16(STC3x_COMMAND_SET_BINARY_GAS, binaryGas))
    
    def setPressure(self, hpa):
        return (self.sendCommandParam16(STC3X_COMMAND_SET_PRESSURE, int(hpa)))

    def setHumidity(self, humidity):
        rh = int(humidity * 655.35)
        return (self.sendCommandParam16(STC3X_COMMAND_SET_RELATIVE_HUMIDITY, rh))

    def setTemperature(self, temp):
        T = int(temp*200)
        return (self.sendCommandParam16(STC3X_COMMAND_SET_TEMPERATURE, T))

    def measureGasConcentration(self):
        if (time.ticks_ms() - self._lastReadTimeMillis) < 1000:
            return [None, None] # too early
        success = self.sendCommandOnly(STC3X_COMMAND_MEASURE_GAS_CONCENTRATION)
        time.sleep(0.1)
        receivedBytes = bytearray(6)
        if type(self._wirePort) == SoftI2C:
            #self._wirePort.start()
            self._wirePort.readinto(receivedBytes)
            #self._wirePort.stop()
        else:
            #self._wirePort.readfrom_into(self._i2cAddress, receivedBytes)
            receivedBytes = self._wirePort.readfrom(self._i2cAddress, 6)
        #print(receivedBytes)
        #print("tempCO2 = {}, tempTemperature = {}".format((receivedBytes[0] * 256 + receivedBytes[1]), (receivedBytes[3] * 256 + receivedBytes[4])))
        rawCO2 = (receivedBytes[0] * 256 + receivedBytes[1])
        if rawCO2 < 16384:
            rawCO2 = 16384
        calcCO2 = ((rawCO2  - 16384)  / 327.68)
        temp = (receivedBytes[2] * 256 + receivedBytes[3]) / 200.0
        return [rawCO2, calcCO2, temp]

    def forcedRecalibration(self, concentration, delayMillis):
        if (concentration < 0.0): # Ignore negative concentrations
            concentration = 0.0
        if (concentration > 100.0): # Ignore concentrations above 100%
            concentration = 100.0
        conc_16 = int(((concentration * 32768) / 100) + 16384)
        success = self.sendCommandParam16(STC3X_COMMAND_FORCED_RECALIBRATION, conc_16)
        if (delayMillis > 0):
            time.sleep(delayMillis/1000.0) # Allow time for the measurement to complete
        return success

    def enableAutomaticSelfCalibration(self):
        return self.sendCommandOnly(STC3X_COMMAND_AUTOMATIC_CALIBRATION_ENABLE)

    def performSelfTest(self):
        response = self.readRegister(STC3X_COMMAND_SELF_TEST)
        if response == None:
            print("response == None")
            return False
        print("response == {}".format(response))
        return (response == 0x0000)

    def readRegister(self, registerAddress, delayMillis=70):
        success = self.sendCommandOnly(registerAddress)
        if success == False:
            return None
        time.sleep(delayMillis / 1000.0)
        data = self._wirePort.readfrom(self._i2cAddress, 2) # Request data sans CRC
        response = int(data[0]) << 8 | int(data[1])
        return response
