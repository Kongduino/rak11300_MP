from sys import implementation

if implementation.name == 'micropython':
  from utime import sleep_ms

if implementation.name == 'circuitpython':
    from time import sleep
    def sleep_ms(ms):
        sleep(ms/1000)

def ASSERT(state):
    assert state == ERR_NONE, ERROR[state]

def yield_():
    sleep_ms(1)

SX126X_ANA_LNA = const(0x08E2)
SX126X_ANA_MIXER = const(0x08E5)

SX126X_FREQUENCY_STEP_SIZE = 0.9536743164
SX126X_MAX_PACKET_LENGTH = const(255)
SX126X_CRYSTAL_FREQ = 32.0
SX126X_DIV_EXPONENT = const(25)
SX126X_CMD_NOP = const(0x00)
SX126X_CMD_SET_SLEEP = const(0x84)
SX126X_CMD_SET_STANDBY = const(0x80)
SX126X_CMD_SET_FS = const(0xC1)
SX126X_CMD_SET_TX = const(0x83)
SX126X_CMD_SET_RX = const(0x82)
SX126X_CMD_STOP_TIMER_ON_PREAMBLE = const(0x9F)
SX126X_CMD_SET_RX_DUTY_CYCLE = const(0x94)
SX126X_CMD_SET_CAD = const(0xC5)
SX126X_CMD_SET_TX_CONTINUOUS_WAVE = const(0xD1)
SX126X_CMD_SET_TX_INFINITE_PREAMBLE = const(0xD2)
SX126X_CMD_SET_REGULATOR_MODE = const(0x96)
SX126X_CMD_CALIBRATE = const(0x89)
SX126X_CMD_CALIBRATE_IMAGE = const(0x98)
SX126X_CMD_SET_PA_CONFIG = const(0x95)
SX126X_CMD_SET_RX_TX_FALLBACK_MODE = const(0x93)
SX126X_CMD_WRITE_REGISTER = const(0x0D)
SX126X_CMD_READ_REGISTER = const(0x1D)
SX126X_CMD_WRITE_BUFFER = const(0x0E)
SX126X_CMD_READ_BUFFER = const(0x1E)
SX126X_CMD_SET_DIO_IRQ_PARAMS = const(0x08)
SX126X_CMD_GET_IRQ_STATUS = const(0x12)
SX126X_CMD_CLEAR_IRQ_STATUS = const(0x02)
SX126X_CMD_SET_DIO2_AS_RF_SWITCH_CTRL = const(0x9D)
SX126X_CMD_SET_DIO3_AS_TCXO_CTRL = const(0x97)
SX126X_CMD_SET_RF_FREQUENCY = const(0x86)
SX126X_CMD_SET_PACKET_TYPE = const(0x8A)
SX126X_CMD_GET_PACKET_TYPE = const(0x11)
SX126X_CMD_SET_TX_PARAMS = const(0x8E)
SX126X_CMD_SET_MODULATION_PARAMS = const(0x8B)
SX126X_CMD_SET_PACKET_PARAMS = const(0x8C)
SX126X_CMD_SET_CAD_PARAMS = const(0x88)
SX126X_CMD_SET_BUFFER_BASE_ADDRESS = const(0x8F)
SX126X_CMD_SET_LORA_SYMB_NUM_TIMEOUT = const(0x0A)
SX126X_CMD_GET_STATUS = const(0xC0)
SX126X_CMD_GET_RSSI_INST = const(0x15)
SX126X_CMD_GET_RX_BUFFER_STATUS = const(0x13)
SX126X_CMD_GET_PACKET_STATUS = const(0x14)
SX126X_CMD_GET_DEVICE_ERRORS = const(0x17)
SX126X_CMD_CLEAR_DEVICE_ERRORS = const(0x07)
SX126X_CMD_GET_STATS = const(0x10)
SX126X_CMD_RESET_STATS = const(0x00)
SX126X_REG_WHITENING_INITIAL_MSB = const(0x06B8)
SX126X_REG_WHITENING_INITIAL_LSB = const(0x06B9)
SX126X_REG_CRC_INITIAL_MSB = const(0x06BC)
SX126X_REG_CRC_INITIAL_LSB = const(0x06BD)
SX126X_REG_CRC_POLYNOMIAL_MSB = const(0x06BE)
SX126X_REG_CRC_POLYNOMIAL_LSB = const(0x06BF)
SX126X_REG_SYNC_WORD_0 = const(0x06C0)
SX126X_REG_SYNC_WORD_1 = const(0x06C1)
SX126X_REG_SYNC_WORD_2 = const(0x06C2)
SX126X_REG_SYNC_WORD_3 = const(0x06C3)
SX126X_REG_SYNC_WORD_4 = const(0x06C4)
SX126X_REG_SYNC_WORD_5 = const(0x06C5)
SX126X_REG_SYNC_WORD_6 = const(0x06C6)
SX126X_REG_SYNC_WORD_7 = const(0x06C7)
SX126X_REG_NODE_ADDRESS = const(0x06CD)
SX126X_REG_BROADCAST_ADDRESS = const(0x06CE)
SX126X_REG_LORA_SYNC_WORD_MSB = const(0x0740)
SX126X_REG_LORA_SYNC_WORD_LSB = const(0x0741)
SX126X_REG_RANDOM_NUMBER_0 = const(0x0819)
SX126X_REG_RANDOM_NUMBER_1 = const(0x081A)
SX126X_REG_RANDOM_NUMBER_2 = const(0x081B)
SX126X_REG_RANDOM_NUMBER_3 = const(0x081C)
SX126X_REG_RX_GAIN = const(0x08AC)
SX126X_REG_OCP_CONFIGURATION = const(0x08E7)
SX126X_REG_XTA_TRIM = const(0x0911)
SX126X_REG_XTB_TRIM = const(0x0912)
SX126X_REG_SENSITIVITY_CONFIG = const(0x0889)
SX126X_REG_TX_CLAMP_CONFIG = const(0x08D8)
SX126X_REG_RTC_STOP = const(0x0920)
SX126X_REG_RTC_EVENT = const(0x0944)
SX126X_REG_IQ_CONFIG = const(0x0736)
SX126X_REG_RX_GAIN_RETENTION_0 = const(0x029F)
SX126X_REG_RX_GAIN_RETENTION_1 = const(0x02A0)
SX126X_REG_RX_GAIN_RETENTION_2 = const(0x02A1)
SX126X_SLEEP_START_COLD = const(0b00000000)
SX126X_SLEEP_START_WARM = const(0b00000100)
SX126X_SLEEP_RTC_OFF = const(0b00000000)
SX126X_SLEEP_RTC_ON = const(0b00000001)
SX126X_STANDBY_RC = const(0x00)
SX126X_STANDBY_XOSC = const(0x01)
SX126X_RX_TIMEOUT_NONE = const(0x000000)
SX126X_RX_TIMEOUT_INF = const(0xFFFFFF)
SX126X_TX_TIMEOUT_NONE = const(0x000000)
SX126X_STOP_ON_PREAMBLE_OFF = const(0x00)
SX126X_STOP_ON_PREAMBLE_ON = const(0x01)
SX126X_REGULATOR_LDO = const(0x00)
SX126X_REGULATOR_DC_DC = const(0x01)
SX126X_CALIBRATE_IMAGE_OFF = const(0b00000000)
SX126X_CALIBRATE_IMAGE_ON = const(0b01000000)
SX126X_CALIBRATE_ADC_BULK_P_OFF = const(0b00000000)
SX126X_CALIBRATE_ADC_BULK_P_ON = const(0b00100000)
SX126X_CALIBRATE_ADC_BULK_N_OFF = const(0b00000000)
SX126X_CALIBRATE_ADC_BULK_N_ON = const(0b00010000)
SX126X_CALIBRATE_ADC_PULSE_OFF = const(0b00000000)
SX126X_CALIBRATE_ADC_PULSE_ON = const(0b00001000)
SX126X_CALIBRATE_PLL_OFF = const(0b00000000)
SX126X_CALIBRATE_PLL_ON = const(0b00000100)
SX126X_CALIBRATE_RC13M_OFF = const(0b00000000)
SX126X_CALIBRATE_RC13M_ON = const(0b00000010)
SX126X_CALIBRATE_RC64K_OFF = const(0b00000000)
SX126X_CALIBRATE_RC64K_ON = const(0b00000001)
SX126X_CALIBRATE_ALL = const(0b01111111)
SX126X_CAL_IMG_430_MHZ_1 = const(0x6B)
SX126X_CAL_IMG_430_MHZ_2 = const(0x6F)
SX126X_CAL_IMG_470_MHZ_1 = const(0x75)
SX126X_CAL_IMG_470_MHZ_2 = const(0x81)
SX126X_CAL_IMG_779_MHZ_1 = const(0xC1)
SX126X_CAL_IMG_779_MHZ_2 = const(0xC5)
SX126X_CAL_IMG_863_MHZ_1 = const(0xD7)
SX126X_CAL_IMG_863_MHZ_2 = const(0xDB)
SX126X_CAL_IMG_902_MHZ_1 = const(0xE1)
SX126X_CAL_IMG_902_MHZ_2 = const(0xE9)
SX126X_PA_CONFIG_HP_MAX = const(0x07)
SX126X_PA_CONFIG_PA_LUT = const(0x01)
SX126X_PA_CONFIG_SX1262_8 = const(0x00)
SX126X_RX_TX_FALLBACK_MODE_FS = const(0x40)
SX126X_RX_TX_FALLBACK_MODE_STDBY_XOSC = const(0x30)
SX126X_RX_TX_FALLBACK_MODE_STDBY_RC = const(0x20)
SX126X_IRQ_TIMEOUT = const(0b1000000000)
SX126X_IRQ_CAD_DETECTED = const(0b0100000000)
SX126X_IRQ_CAD_DONE = const(0b0010000000)
SX126X_IRQ_CRC_ERR = const(0b0001000000)
SX126X_IRQ_HEADER_ERR = const(0b0000100000)
SX126X_IRQ_HEADER_VALID = const(0b0000010000)
SX126X_IRQ_SYNC_WORD_VALID = const(0b0000001000)
SX126X_IRQ_PREAMBLE_DETECTED = const(0b0000000100)
SX126X_IRQ_RX_DONE = const(0b0000000010)
SX126X_IRQ_TX_DONE = const(0b0000000001)
SX126X_IRQ_ALL = const(0b1111111111)
SX126X_IRQ_NONE = const(0b0000000000)
SX126X_DIO2_AS_IRQ = const(0x00)
SX126X_DIO2_AS_RF_SWITCH = const(0x01)
SX126X_DIO3_OUTPUT_1_6 = const(0x00)
SX126X_DIO3_OUTPUT_1_7 = const(0x01)
SX126X_DIO3_OUTPUT_1_8 = const(0x02)
SX126X_DIO3_OUTPUT_2_2 = const(0x03)
SX126X_DIO3_OUTPUT_2_4 = const(0x04)
SX126X_DIO3_OUTPUT_2_7 = const(0x05)
SX126X_DIO3_OUTPUT_3_0 = const(0x06)
SX126X_DIO3_OUTPUT_3_3 = const(0x07)
SX126X_PACKET_TYPE_GFSK = const(0x00)
SX126X_PACKET_TYPE_LORA = const(0x01)
SX126X_PA_RAMP_10U = const(0x00)
SX126X_PA_RAMP_20U = const(0x01)
SX126X_PA_RAMP_40U = const(0x02)
SX126X_PA_RAMP_80U = const(0x03)
SX126X_PA_RAMP_200U = const(0x04)
SX126X_PA_RAMP_800U = const(0x05)
SX126X_PA_RAMP_1700U = const(0x06)
SX126X_PA_RAMP_3400U = const(0x07)
SX126X_GFSK_FILTER_NONE = const(0x00)
SX126X_GFSK_FILTER_GAUSS_0_3 = const(0x08)
SX126X_GFSK_FILTER_GAUSS_0_5 = const(0x09)
SX126X_GFSK_FILTER_GAUSS_0_7 = const(0x0A)
SX126X_GFSK_FILTER_GAUSS_1 = const(0x0B)
SX126X_GFSK_RX_BW_4_8 = const(0x1F)
SX126X_GFSK_RX_BW_5_8 = const(0x17)
SX126X_GFSK_RX_BW_7_3 = const(0x0F)
SX126X_GFSK_RX_BW_9_7 = const(0x1E)
SX126X_GFSK_RX_BW_11_7 = const(0x16)
SX126X_GFSK_RX_BW_14_6 = const(0x0E)
SX126X_GFSK_RX_BW_19_5 = const(0x1D)
SX126X_GFSK_RX_BW_23_4 = const(0x15)
SX126X_GFSK_RX_BW_29_3 = const(0x0D)
SX126X_GFSK_RX_BW_39_0 = const(0x1C)
SX126X_GFSK_RX_BW_46_9 = const(0x14)
SX126X_GFSK_RX_BW_58_6 = const(0x0C)
SX126X_GFSK_RX_BW_78_2 = const(0x1B)
SX126X_GFSK_RX_BW_93_8 = const(0x13)
SX126X_GFSK_RX_BW_117_3 = const(0x0B)
SX126X_GFSK_RX_BW_156_2 = const(0x1A)
SX126X_GFSK_RX_BW_187_2 = const(0x12)
SX126X_GFSK_RX_BW_234_3 = const(0x0A)
SX126X_GFSK_RX_BW_312_0 = const(0x19)
SX126X_GFSK_RX_BW_373_6 = const(0x11)
SX126X_GFSK_RX_BW_467_0 = const(0x09)
SX126X_LORA_BW_7_8 = const(0x00)
SX126X_LORA_BW_10_4 = const(0x08)
SX126X_LORA_BW_15_6 = const(0x01)
SX126X_LORA_BW_20_8 = const(0x09)
SX126X_LORA_BW_31_25 = const(0x02)
SX126X_LORA_BW_41_7 = const(0x0A)
SX126X_LORA_BW_62_5 = const(0x03)
SX126X_LORA_BW_125_0 = const(0x04)
SX126X_LORA_BW_250_0 = const(0x05)
SX126X_LORA_BW_500_0 = const(0x06)
SX126X_LORA_CR_4_5 = const(0x01)
SX126X_LORA_CR_4_6 = const(0x02)
SX126X_LORA_CR_4_7 = const(0x03)
SX126X_LORA_CR_4_8 = const(0x04)
SX126X_LORA_LOW_DATA_RATE_OPTIMIZE_OFF = const(0x00)
SX126X_LORA_LOW_DATA_RATE_OPTIMIZE_ON = const(0x01)
SX126X_GFSK_PREAMBLE_DETECT_OFF = const(0x00)
SX126X_GFSK_PREAMBLE_DETECT_8 = const(0x04)
SX126X_GFSK_PREAMBLE_DETECT_16 = const(0x05)
SX126X_GFSK_PREAMBLE_DETECT_24 = const(0x06)
SX126X_GFSK_PREAMBLE_DETECT_32 = const(0x07)
SX126X_GFSK_ADDRESS_FILT_OFF = const(0x00)
SX126X_GFSK_ADDRESS_FILT_NODE = const(0x01)
SX126X_GFSK_ADDRESS_FILT_NODE_BROADCAST = const(0x02)
SX126X_GFSK_PACKET_FIXED = const(0x00)
SX126X_GFSK_PACKET_VARIABLE = const(0x01)
SX126X_GFSK_CRC_OFF = const(0x01)
SX126X_GFSK_CRC_1_BYTE = const(0x00)
SX126X_GFSK_CRC_2_BYTE = const(0x02)
SX126X_GFSK_CRC_1_BYTE_INV = const(0x04)
SX126X_GFSK_CRC_2_BYTE_INV = const(0x06)
SX126X_GFSK_WHITENING_OFF = const(0x00)
SX126X_GFSK_WHITENING_ON = const(0x01)
SX126X_LORA_HEADER_EXPLICIT = const(0x00)
SX126X_LORA_HEADER_IMPLICIT = const(0x01)
SX126X_LORA_CRC_OFF = const(0x00)
SX126X_LORA_CRC_ON = const(0x01)
SX126X_LORA_IQ_STANDARD = const(0x00)
SX126X_LORA_IQ_INVERTED = const(0x01)
SX126X_CAD_ON_1_SYMB = const(0x00)
SX126X_CAD_ON_2_SYMB = const(0x01)
SX126X_CAD_ON_4_SYMB = const(0x02)
SX126X_CAD_ON_8_SYMB = const(0x03)
SX126X_CAD_ON_16_SYMB = const(0x04)
SX126X_CAD_GOTO_STDBY = const(0x00)
SX126X_CAD_GOTO_RX = const(0x01)
SX126X_STATUS_MODE_STDBY_RC = const(0b00100000)
SX126X_STATUS_MODE_STDBY_XOSC = const(0b00110000)
SX126X_STATUS_MODE_FS = const(0b01000000)
SX126X_STATUS_MODE_RX = const(0b01010000)
SX126X_STATUS_MODE_TX = const(0b01100000)
SX126X_STATUS_DATA_AVAILABLE = const(0b00000100)
SX126X_STATUS_CMD_TIMEOUT = const(0b00000110)
SX126X_STATUS_CMD_INVALID = const(0b00001000)
SX126X_STATUS_CMD_FAILED = const(0b00001010)
SX126X_STATUS_TX_DONE = const(0b00001100)
SX126X_STATUS_SPI_FAILED = const(0b11111111)
SX126X_GFSK_RX_STATUS_PREAMBLE_ERR = const(0b10000000)
SX126X_GFSK_RX_STATUS_SYNC_ERR = const(0b01000000)
SX126X_GFSK_RX_STATUS_ADRS_ERR = const(0b00100000)
SX126X_GFSK_RX_STATUS_CRC_ERR = const(0b00010000)
SX126X_GFSK_RX_STATUS_LENGTH_ERR = const(0b00001000)
SX126X_GFSK_RX_STATUS_ABORT_ERR = const(0b00000100)
SX126X_GFSK_RX_STATUS_PACKET_RECEIVED = const(0b00000010)
SX126X_GFSK_RX_STATUS_PACKET_SENT = const(0b00000001)
SX126X_PA_RAMP_ERR = const(0b100000000)
SX126X_PLL_LOCK_ERR = const(0b001000000)
SX126X_XOSC_START_ERR = const(0b000100000)
SX126X_IMG_CALIB_ERR = const(0b000010000)
SX126X_ADC_CALIB_ERR = const(0b000001000)
SX126X_PLL_CALIB_ERR = const(0b000000100)
SX126X_RC13M_CALIB_ERR = const(0b000000010)
SX126X_RC64K_CALIB_ERR = const(0b000000001)
SX126X_SYNC_WORD_PUBLIC = const(0x34)
SX126X_SYNC_WORD_PRIVATE = const(0x12)

ERR_NONE = const(0)
ERR_UNKNOWN = const(-1)
ERR_CHIP_NOT_FOUND = const(-2)
ERR_MEMORY_ALLOCATION_FAILED = const(-3)
ERR_PACKET_TOO_LONG = const(-4)
ERR_TX_TIMEOUT = const(-5)
ERR_RX_TIMEOUT = const(-6)
ERR_CRC_MISMATCH = const(-7)
ERR_INVALID_BANDWIDTH = const(-8)
ERR_INVALID_SPREADING_FACTOR = const(-9)
ERR_INVALID_CODING_RATE = const(-10)
ERR_INVALID_BIT_RANGE = const(-11)
ERR_INVALID_FREQUENCY = const(-12)
ERR_INVALID_OUTPUT_POWER = const(-13)
PREAMBLE_DETECTED = const(-14)
CHANNEL_FREE = const(-15)
ERR_SPI_WRITE_FAILED = const(-16)
ERR_INVALID_CURRENT_LIMIT = const(-17)
ERR_INVALID_PREAMBLE_LENGTH = const(-18)
ERR_INVALID_GAIN = const(-19)
ERR_WRONG_MODEM = const(-20)
ERR_INVALID_NUM_SAMPLES = const(-21)
ERR_INVALID_RSSI_OFFSET = const(-22)
ERR_INVALID_ENCODING = const(-23)
ERR_INVALID_BIT_RATE = const(-101)
ERR_INVALID_FREQUENCY_DEVIATION = const(-102)
ERR_INVALID_BIT_RATE_BW_RATIO = const(-103)
ERR_INVALID_RX_BANDWIDTH = const(-104)
ERR_INVALID_SYNC_WORD = const(-105)
ERR_INVALID_DATA_SHAPING = const(-106)
ERR_INVALID_MODULATION = const(-107)
ERR_AT_FAILED = const(-201)
ERR_URL_MALFORMED = const(-202)
ERR_RESPONSE_MALFORMED_AT = const(-203)
ERR_RESPONSE_MALFORMED = const(-204)
ERR_MQTT_CONN_VERSION_REJECTED = const(-205)
ERR_MQTT_CONN_ID_REJECTED = const(-206)
ERR_MQTT_CONN_SERVER_UNAVAILABLE = const(-207)
ERR_MQTT_CONN_BAD_USERNAME_PASSWORD = const(-208)
ERR_MQTT_CONN_NOT_AUTHORIZED = const(-208)
ERR_MQTT_UNEXPECTED_PACKET_ID = const(-209)
ERR_MQTT_NO_NEW_PACKET_AVAILABLE = const(-210)
ERR_CMD_MODE_FAILED = const(-301)
ERR_FRAME_MALFORMED = const(-302)
ERR_FRAME_INCORRECT_CHECKSUM = const(-303)
ERR_FRAME_UNEXPECTED_ID = const(-304)
ERR_FRAME_NO_RESPONSE = const(-305)
ERR_INVALID_RTTY_SHIFT = const(-401)
ERR_UNSUPPORTED_ENCODING = const(-402)
ERR_INVALID_DATA_RATE = const(-501)
ERR_INVALID_ADDRESS_WIDTH = const(-502)
ERR_INVALID_PIPE_NUMBER = const(-503)
ERR_ACK_NOT_RECEIVED = const(-504)
ERR_INVALID_NUM_BROAD_ADDRS = const(-601)
ERR_INVALID_CRC_CONFIGURATION = const(-701)
LORA_DETECTED = const(-702)
ERR_INVALID_TCXO_VOLTAGE = const(-703)
ERR_INVALID_MODULATION_PARAMETERS = const(-704)
ERR_SPI_CMD_TIMEOUT = const(-705)
ERR_SPI_CMD_INVALID = const(-706)
ERR_SPI_CMD_FAILED = const(-707)
ERR_INVALID_SLEEP_PERIOD = const(-708)
ERR_INVALID_RX_PERIOD = const(-709)
ERR_INVALID_CALLSIGN = const(-801)
ERR_INVALID_NUM_REPEATERS = const(-802)
ERR_INVALID_REPEATER_CALLSIGN = const(-803)
ERR_INVALID_PACKET_TYPE = const(-804)
ERR_INVALID_PACKET_LENGTH = const(-805)

ERROR = {
    0: 'ERR_NONE',
    -1: 'ERR_UNKNOWN',
    -2: 'ERR_CHIP_NOT_FOUND',
    -3: 'ERR_MEMORY_ALLOCATION_FAILED',
    -4: 'ERR_PACKET_TOO_LONG',
    -5: 'ERR_TX_TIMEOUT',
    -6: 'ERR_RX_TIMEOUT',
    -7: 'ERR_CRC_MISMATCH',
    -8: 'ERR_INVALID_BANDWIDTH',
    -9: 'ERR_INVALID_SPREADING_FACTOR',
    -10: 'ERR_INVALID_CODING_RATE',
    -11: 'ERR_INVALID_BIT_RANGE',
    -12: 'ERR_INVALID_FREQUENCY',
    -13: 'ERR_INVALID_OUTPUT_POWER',
    -14: 'PREAMBLE_DETECTED',
    -15: 'CHANNEL_FREE',
    -16: 'ERR_SPI_WRITE_FAILED',
    -17: 'ERR_INVALID_CURRENT_LIMIT',
    -18: 'ERR_INVALID_PREAMBLE_LENGTH',
    -19: 'ERR_INVALID_GAIN',
    -20: 'ERR_WRONG_MODEM',
    -21: 'ERR_INVALID_NUM_SAMPLES',
    -22: 'ERR_INVALID_RSSI_OFFSET',
    -23: 'ERR_INVALID_ENCODING',
    -101: 'ERR_INVALID_BIT_RATE',
    -102: 'ERR_INVALID_FREQUENCY_DEVIATION',
    -103: 'ERR_INVALID_BIT_RATE_BW_RATIO',
    -104: 'ERR_INVALID_RX_BANDWIDTH',
    -105: 'ERR_INVALID_SYNC_WORD',
    -106: 'ERR_INVALID_DATA_SHAPING',
    -107: 'ERR_INVALID_MODULATION',
    -201: 'ERR_AT_FAILED',
    -202: 'ERR_URL_MALFORMED',
    -203: 'ERR_RESPONSE_MALFORMED_AT',
    -204: 'ERR_RESPONSE_MALFORMED',
    -205: 'ERR_MQTT_CONN_VERSION_REJECTED',
    -206: 'ERR_MQTT_CONN_ID_REJECTED',
    -207: 'ERR_MQTT_CONN_SERVER_UNAVAILABLE',
    -208: 'ERR_MQTT_CONN_BAD_USERNAME_PASSWORD',
    -208: 'ERR_MQTT_CONN_NOT_AUTHORIZED',
    -209: 'ERR_MQTT_UNEXPECTED_PACKET_ID',
    -210: 'ERR_MQTT_NO_NEW_PACKET_AVAILABLE',
    -301: 'ERR_CMD_MODE_FAILED',
    -302: 'ERR_FRAME_MALFORMED',
    -303: 'ERR_FRAME_INCORRECT_CHECKSUM',
    -304: 'ERR_FRAME_UNEXPECTED_ID',
    -305: 'ERR_FRAME_NO_RESPONSE',
    -401: 'ERR_INVALID_RTTY_SHIFT',
    -402: 'ERR_UNSUPPORTED_ENCODING',
    -501: 'ERR_INVALID_DATA_RATE',
    -502: 'ERR_INVALID_ADDRESS_WIDTH',
    -503: 'ERR_INVALID_PIPE_NUMBER',
    -504: 'ERR_ACK_NOT_RECEIVED',
    -601: 'ERR_INVALID_NUM_BROAD_ADDRS',
    -701: 'ERR_INVALID_CRC_CONFIGURATION',
    -702: 'LORA_DETECTED',
    -703: 'ERR_INVALID_TCXO_VOLTAGE',
    -704: 'ERR_INVALID_MODULATION_PARAMETERS',
    -705: 'ERR_SPI_CMD_TIMEOUT',
    -706: 'ERR_SPI_CMD_INVALID',
    -707: 'ERR_SPI_CMD_FAILED',
    -708: 'ERR_INVALID_SLEEP_PERIOD',
    -709: 'ERR_INVALID_RX_PERIOD',
    -801: 'ERR_INVALID_CALLSIGN',
    -802: 'ERR_INVALID_NUM_REPEATERS',
    -803: 'ERR_INVALID_REPEATER_CALLSIGN',
    -804: 'ERR_INVALID_PACKET_TYPE',
    -805: 'ERR_INVALID_PACKET_LENGTH'
    }
