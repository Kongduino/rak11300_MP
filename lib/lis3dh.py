class LIS3DH:
    def __init__(self, i2c, i2cAddress=0x19):
        self._i2c = i2c
        self._address = i2cAddress
        buf = bytearray([0x57])
        self._i2c.writeto_mem(self._address, 0x20, buf)
        buf = bytearray([0x08])
        self._i2c.writeto_mem(self._address, 0x23, buf)
        self.ID = int.from_bytes(self._i2c.readfrom_mem(self._address, 0x0F, 1), "big")

    def get_acceleration(self):
        x_l=self._i2c.readfrom_mem(self._address, 0x28, 1)
        x_h=self._i2c.readfrom_mem(self._address, 0x29, 1)
        y_l=self._i2c.readfrom_mem(self._address, 0x2a, 1)
        y_h=self._i2c.readfrom_mem(self._address, 0x2b, 1)
        z_l=self._i2c.readfrom_mem(self._address, 0x2c, 1)
        z_h=self._i2c.readfrom_mem(self._address, 0x2d, 1)
        x= (x_h[0]<<8) | x_l[0]
        y= (y_h[0]<<8) | y_l[0]
        z= (z_h[0]<<8) | z_l[0]
        if x < 0x8000:
            x=x
        else:
            x=x-0x10000
        if y < 0x8000:
            y=y
        else:
            y=y-0x10000
        if z < 0x8000:
            z=z
        else:
            z=z-0x10000
        acc_x = (x*4000)/65536.0
        acc_y = (y*4000)/65536.0
        acc_z = (z*4000)/65536.0
        ret_Arg = {
            'x':acc_x,
            'y':acc_y,
            'z':acc_z
        }
        return ret_Arg