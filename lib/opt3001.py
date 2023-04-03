# Constants
I2C_LS_REG_RESULT = 0x00
I2C_LS_REG_CONFIG = 0x01
I2C_LS_REG_LOWLIMIT = 0x02
I2C_LS_REG_HIGHLIMIT = 0x03
I2C_LS_REG_MANUFACTURERID = 0x7E
I2C_LS_REG_DEVICEID = 0x7F

# Configdata for Register "Configuration"
I2C_LS_CONFIG_DEFAULT = 0xc810
# Bit 15..12 Automatic Full-Scale Setting Mode
# Bit 11 Conversion time field: 800ms
# Bit 10..9 Mode of conversion: Shutdown
# Bit 4 Latch field

# Configdata for Register "Configuration"
I2C_LS_CONFIG_CONT_FULL_800MS = 0xcc10
# Bit 15..12 Automatic Full-Scale Setting Mode
# Bit 11 Conversion timefield: 800ms
# 10..9 Mode of conversion: Continuous conversions
# Bit 4 Latch field

class OPT3001:
    def __init__(self, i2c, i2cAddress=0x44):
        self._i2c = i2c
        self._address = i2cAddress
        self.manufacturerID = self.read_manufacturer_id()
        self.deviceID = self.read_device_id()

    def read_register_16bit(self, addr):
        values = self._i2c.readfrom_mem(self._address, addr, 2)
        data = (values[0] << 8) | values[1]
        return data

    def write_register_16bit(self, addr, data):
        d1 = (data >> 8) & 0xFF
        d0 = data & 0xFF
        return self._i2c.writeto_mem(self._address, addr, bytearray([d1, d0]))

    def write_config_reg(self, data):
        return self.write_register_16bit(I2C_LS_REG_CONFIG, data)

    def read_manufacturer_id(self):
        return self.read_register_16bit(I2C_LS_REG_MANUFACTURERID)

    def read_device_id(self):
        return self.read_register_16bit(I2C_LS_REG_DEVICEID)

    def read_lux_fixpoint(self):
        # Register Value
        req_value = self.read_register_16bit(I2C_LS_REG_RESULT)
        # Convert to LUX
        mantissa = req_value & 0x0fff
        exponent = (req_value & 0xf000) >> 12
        return 2**exponent * mantissa  # mantissa << exponent;

    def read_lux_float(self):
        # Register Value
        req_value = self.read_register_16bit(I2C_LS_REG_RESULT)
        # Convert to LUX
        mantissa = req_value & 0x0fff
        exponent = (req_value & 0xf000) >> 12
        return 2**exponent * mantissa * 0.01  # mantisse << exponent * 0.01;
