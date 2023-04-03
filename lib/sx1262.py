from _sx126x import *
from sx126x import SX126X
from time import sleep

_SX126X_PA_CONFIG_SX1262 = const(0x00)

class SX1262(SX126X):
    TX_DONE = SX126X_IRQ_TX_DONE
    RX_DONE = SX126X_IRQ_RX_DONE
    ADDR_FILT_OFF = SX126X_GFSK_ADDRESS_FILT_OFF
    ADDR_FILT_NODE = SX126X_GFSK_ADDRESS_FILT_NODE
    ADDR_FILT_NODE_BROAD = SX126X_GFSK_ADDRESS_FILT_NODE_BROADCAST
    PREAMBLE_DETECT_OFF = SX126X_GFSK_PREAMBLE_DETECT_OFF
    PREAMBLE_DETECT_8 = SX126X_GFSK_PREAMBLE_DETECT_8
    PREAMBLE_DETECT_16 = SX126X_GFSK_PREAMBLE_DETECT_16
    PREAMBLE_DETECT_24 = SX126X_GFSK_PREAMBLE_DETECT_24
    PREAMBLE_DETECT_32 = SX126X_GFSK_PREAMBLE_DETECT_32
    STATUS = ERROR

    def setReceiveLED(self, led):
        self.LED_RECV = led

    def __init__(self, clk=10, mosi=11, miso=12, cs=13, irq=29, rst=14, gpio=15, ledrcv=None):
        super().__init__(clk, mosi, miso, cs, irq, rst, gpio)
        self._callbackFunction = self._dummyFunction
        self.LED_RECV = ledrcv

    def begin(self, freq=868.125, bw=125.0, sf=12, cr=5, syncWord=SX126X_SYNC_WORD_PRIVATE,
              power=22, currentLimit=100.0, preambleLength=8, implicit=False, implicitLen=0xFF,
              crcOn=False, txIq=False, rxIq=False, tcxoVoltage=1.6, useRegulatorLDO=False,
              blocking=True):
        state = super().begin(bw, sf, cr, syncWord, currentLimit, preambleLength, tcxoVoltage, useRegulatorLDO, txIq, rxIq)
        ASSERT(state)
        if not implicit:
            state = super().explicitHeader()
        else:
            state = super().implicitHeader(implicitLen)
        ASSERT(state)
        state = super().setCRC(crcOn)
        ASSERT(state)
        state = self.setFrequency(freq)
        ASSERT(state)
        state = self.setOutputPower(power)
        ASSERT(state)
        state = super().fixPaClamping()
        ASSERT(state)
        state = self.setBlockingCallback(blocking)
        return state

    def beginFSK(self, freq=434.0, br=48.0, freqDev=50.0, rxBw=156.2, power=14, currentLimit=60.0,
                 preambleLength=16, dataShaping=0.5, syncWord=[0x2D, 0x01], syncBitsLength=16,
                 addrFilter=SX126X_GFSK_ADDRESS_FILT_OFF, addr=0x00, crcLength=2, crcInitial=0x1D0F, crcPolynomial=0x1021,
                 crcInverted=True, whiteningOn=True, whiteningInitial=0x0100,
                 fixedPacketLength=False, packetLength=0xFF, preambleDetectorLength=SX126X_GFSK_PREAMBLE_DETECT_16,
                 tcxoVoltage=1.6, useRegulatorLDO=False,
                 blocking=True):
        state = super().beginFSK(br, freqDev, rxBw, currentLimit, preambleLength, dataShaping, preambleDetectorLength, tcxoVoltage, useRegulatorLDO)
        ASSERT(state)
        state = super().setSyncBits(syncWord, syncBitsLength)
        ASSERT(state)
        if addrFilter == SX126X_GFSK_ADDRESS_FILT_OFF:
            state = super().disableAddressFiltering()
        elif addrFilter == SX126X_GFSK_ADDRESS_FILT_NODE:
            state = super().setNodeAddress(addr)
        elif addrFilter == SX126X_GFSK_ADDRESS_FILT_NODE_BROADCAST:
            state = super().setBroadcastAddress(addr)
        else:
            state = ERR_UNKNOWN
        ASSERT(state)
        state = super().setCRC(crcLength, crcInitial, crcPolynomial, crcInverted)
        ASSERT(state)
        state = super().setWhitening(whiteningOn, whiteningInitial)
        ASSERT(state)
        if fixedPacketLength:
            state = super().fixedPacketLengthMode(packetLength)
        else:
            state = super().variablePacketLengthMode(packetLength)
        ASSERT(state)
        state = self.setFrequency(freq)
        ASSERT(state)
        state = self.setOutputPower(power)
        ASSERT(state)
        state = super().fixPaClamping()
        ASSERT(state)
        state = self.setBlockingCallback(blocking)
        return state

    def setFrequency(self, freq, calibrate=True):
        if freq < 150.0 or freq > 960.0:
            return ERR_INVALID_FREQUENCY
        state = ERR_NONE
        if calibrate:
            data = bytearray(2)
            if freq > 900.0:
                data[0] = SX126X_CAL_IMG_902_MHZ_1
                data[1] = SX126X_CAL_IMG_902_MHZ_2
            elif freq > 850.0:
                data[0] = SX126X_CAL_IMG_863_MHZ_1
                data[1] = SX126X_CAL_IMG_863_MHZ_2
            elif freq > 770.0:
                data[0] = SX126X_CAL_IMG_779_MHZ_1
                data[1] = SX126X_CAL_IMG_779_MHZ_2
            elif freq > 460.0:
                data[0] = SX126X_CAL_IMG_470_MHZ_1
                data[1] = SX126X_CAL_IMG_470_MHZ_2
            else:
                data[0] = SX126X_CAL_IMG_430_MHZ_1
                data[1] = SX126X_CAL_IMG_430_MHZ_2
            state = super().calibrateImage(data)
            ASSERT(state)
        return super().setFrequencyRaw(freq)

    def setOutputPower(self, power):
        if not ((power >= -9) and (power <= 22)):
            return ERR_INVALID_OUTPUT_POWER
        ocp = bytearray(1)
        ocp_mv = memoryview(ocp)
        state = super().readRegister(SX126X_REG_OCP_CONFIGURATION, ocp_mv, 1)
        ASSERT(state)
        state = super().setPaConfig(0x04, _SX126X_PA_CONFIG_SX1262)
        ASSERT(state)
        state = super().setTxParams(power)
        ASSERT(state)
        return super().writeRegister(SX126X_REG_OCP_CONFIGURATION, ocp, 1)

    def setTxIq(self, txIq):
        self._txIq = txIq

    def setRxIq(self, rxIq):
        self._rxIq = rxIq
        if not self.blocking:
            ASSERT(super().startReceive())

    def setPreambleDetectorLength(self, preambleDetectorLength):
        self._preambleDetectorLength = preambleDetectorLength
        if not self.blocking:
            ASSERT(super().startReceive())

    def setBlockingCallback(self, blocking, callback=None):
        self.blocking = blocking
        if not self.blocking:
            state = super().startReceive()
            ASSERT(state)
            if callback != None:
                self._callbackFunction = callback
                super().setDio1Action(self._onIRQ)
            else:
                self._callbackFunction = self._dummyFunction
                super().clearDio1Action()
            return state
        else:
            state = super().standby()
            ASSERT(state)
            self._callbackFunction = self._dummyFunction
            super().clearDio1Action()
            return state

    def recv(self, len=0, timeout_en=False, timeout_ms=0):
        if not self.blocking:
            return self._readData(len)
        else:
            return self._receive(len, timeout_en, timeout_ms)

    def send(self, data):
        if not self.blocking:
            return self._startTransmit(data)
        else:
            return self._transmit(data)

    def _events(self):
        return super().getIrqStatus()

    def _receive(self, len_=0, timeout_en=False, timeout_ms=0):
        state = ERR_NONE
        length = len_
        if len_ == 0:
            length = SX126X_MAX_PACKET_LENGTH
        data = bytearray(length)
        data_mv = memoryview(data)
        try:
            state = super().receive(data_mv, length, timeout_en, timeout_ms)
        except AssertionError as e:
            state = list(ERROR.keys())[list(ERROR.values()).index(str(e))]
        if state == ERR_NONE or state == ERR_CRC_MISMATCH:
            if len_ == 0:
                length = super().getPacketLength(False)
                data = data[:length]
        else:
            return b'', state
        return  bytes(data), state

    def _transmit(self, data):
        if isinstance(data, bytes) or isinstance(data, bytearray):
            pass
        else:
            return 0, ERR_INVALID_PACKET_TYPE
        state = super().transmit(data, len(data))
        return len(data), state

    def _readData(self, len_=0):
        state = ERR_NONE
        length = super().getPacketLength()
        if len_ < length and len_ != 0:
            length = len_
        data = bytearray(length)
        data_mv = memoryview(data)
        if self.LED_RECV != None:
            self.LED_RECV.low()
            for i in range(0, 6):
                self.LED_RECV.toggle()
                sleep(0.2)
        try:
            state = super().readData(data_mv, length)
        except AssertionError as e:
            state = list(ERROR.keys())[list(ERROR.values()).index(str(e))]
        ASSERT(super().startReceive())
        if state == ERR_NONE or state == ERR_CRC_MISMATCH:
            return bytes(data), state
        else:
            return b'', state

    def _startTransmit(self, data):
        if isinstance(data, bytes) or isinstance(data, bytearray):
            pass
        else:
            return 0, ERR_INVALID_PACKET_TYPE
        state = super().startTransmit(data, len(data))
        return len(data), state

    def _dummyFunction(self, *args):
        pass

    def _onIRQ(self, callback):
        events = self._events()
        if events & SX126X_IRQ_TX_DONE:
            super().startReceive()
        self._callbackFunction(events)

    def fillRandom(self, numBytes):
        self.regAnaLna = [0]
        self.regAnaMixer = [0]
        if numBytes % 4 != 0:
            numBytes = (int(numBytes / 4) + 1) * 4
        print("Requesting {} random bytes".format(numBytes))
        data = bytearray(numBytes)
        super().standby()
        state = super().readRegister(SX126X_ANA_LNA, self.regAnaLna, 1)
        self.regAnaLna[0] = self.regAnaLna[0] & ~(1 << 0)
        super().writeRegister(SX126X_ANA_LNA, self.regAnaLna, 1)
        state = super().readRegister(SX126X_ANA_MIXER, self.regAnaMixer, 1)
        self.regAnaMixer[0] = self.regAnaMixer[0] & ~(1 << 7)
        super().writeRegister(SX126X_ANA_MIXER, self.regAnaMixer, 1)
        # Set radio in continuous reception
        super().startReceive()
        fourBytes = [0, 0, 0, 0]
        for i in range(0, numBytes, 4):
            super().readRegister(SX126X_REG_RANDOM_NUMBER_0, fourBytes, 4)
            data[i] = fourBytes[0]
            data[i+1] = fourBytes[1]
            data[i+2] = fourBytes[2]
            data[i+3] = fourBytes[3]
        super().standby()
        super().writeRegister(SX126X_ANA_LNA, self.regAnaLna, 1)
        super().writeRegister(SX126X_ANA_MIXER, self.regAnaMixer, 1)
        return data
