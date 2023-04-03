from micropython import const

LPS33HW_CTRL_REG_1 = const(0x10)
LPS33HW_P_OUT_XL = const(0x28)
LPS33HW_P_OUT_L = const(0x29)
LPS33HW_P_OUT_H = const(0x2a)
LPS33HW_T_OUT_L = const(0x2b)
LPS33HW_T_OUT_H = const(0x2c)

class LPS33HB:
    def __init__(self, i2c, i2cAddress=0x5d):
        self._i2c = i2c
        self._address = i2cAddress
        self.ID = int.from_bytes(self._i2c.readfrom_mem(self._address, 0x0F, 1), "big")

    def get_temp_pressure(self):
        p_out_xl = self._i2c.readfrom_mem(self._address, LPS33HW_P_OUT_XL, 1)
        pre_xl = int.from_bytes(p_out_xl, 'big')
        p_out_l  = self._i2c.readfrom_mem(self._address, LPS33HW_P_OUT_L, 1)
        pre_l = int.from_bytes(p_out_l, 'big')
        p_out_h  = self._i2c.readfrom_mem(self._address, LPS33HW_P_OUT_H, 1)
        pre_h = int.from_bytes(p_out_h, 'big')
        p = [pre_h, pre_l, pre_xl]
        p_data = p[0] << 16 | p[1] << 8 | p[2]
        print("pressure: {}".format(p_data))
        pre = ((pre_h<<16)|(pre_l<<8)|pre_xl)
        if pre & 0x00800000:
            pre |= 0xFF000000
        pre = pre/4096.0
        t_out_l  = self._i2c.readfrom_mem(self._address, LPS33HW_T_OUT_L, 1)
        t_l = int.from_bytes(t_out_l, 'big')
        t_out_h  = self._i2c.readfrom_mem(self._address, LPS33HW_T_OUT_H, 1)
        t_h = int.from_bytes(t_out_h, 'big')
        temp = (t_l<<8)|t_h
        return temp, pre

