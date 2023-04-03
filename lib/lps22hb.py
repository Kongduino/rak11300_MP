from micropython import const

LPS33HW_CTRL_REG_1 = const(0x10)
LPS33HW_P_OUT_XL = const(0x28)
LPS33HW_P_OUT_L = const(0x29)
LPS33HW_P_OUT_H = const(0x2a)

class LPS22HB:
    def __init__(self, i2c, i2cAddress=0x5c):
        self._i2c = i2c
        self._address = i2cAddress
        buf = bytearray([0x50])
        self._i2c.writeto_mem(self._address, LPS33HW_CTRL_REG_1, buf)
        self.ID = int.from_bytes(self._i2c.readfrom_mem(self._address, 0x0F, 1), "big")

    def get_pressure(self):
        pre_xl = self._i2c.readfrom_mem(self._address, LPS33HW_P_OUT_XL, 1)
        pre_xl = int.from_bytes(pre_xl, 'big')
        pre_l = self._i2c.readfrom_mem(self._address, LPS33HW_P_OUT_L, 1)
        pre_l = int.from_bytes(pre_l, 'big')
        pre_h = self._i2c.readfrom_mem(self._address, LPS33HW_P_OUT_H, 1)
        pre_h = int.from_bytes(pre_h, 'big')
        pre = (pre_h<<16)|(pre_l<<8)|pre_xl
        if pre & 0x00800000:
            pre |= 0xFF000000
        return (pre/4096.0)
        
