from pinout import *
from cryptolib import aes

class cbc_encryptor():
    def __init__(self, pKey, pIV, plaintext):
        self.inited = False
        self.ciphertext = b''
        if len(pIV) != 16:
            return
        self._IV = bytearray(pIV)
        if len(pKey) == 16 or len(pKey) == 24 or len(pKey) == 32:
            self._aes = aes(bytearray(pKey), 2, self._IV)
            self.inited = True
        else:
            return
        pt = bytearray(plaintext)
        rmn = 16 - len(pt)%16
        if rmn > 0:
            pt = pt + bytes([rmn])*rmn # Padding
        ln = len(pt)
        cip = self._IV
        for i in range(0, ln, 16):
            cip = cip + self._aes.encrypt(pt[i:i+16])
        self.ciphertext = cip

class cbc_decryptor():
    def __init__(self, pKey, ciphertext):
        # ciphertext = IV[0-15] + ciphertext
        self.inited = False
        if len(pKey) == 16 or len(pKey) == 24 or len(pKey) == 32:
            pIV = ciphertext[0:16]
            cip = ciphertext[16:]
            self._aes = aes(bytearray(pKey), 2, bytearray(pIV))
            self.inited = True
        else:
            return
        rmn = len(cip)%16
        if rmn > 0:
            print("Error: ciphertext length must be a multiple of 16! [{}]".format(len(ciphertext)))
            return None
        ln = len(cip)
        pt = b''
        for i in range(0, ln, 16):
            pt = pt + self._aes.decrypt(cip[i:i+16])
        self.plaintext = pt
