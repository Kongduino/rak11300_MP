from sx1262 import SX1262
from pinout import *
from aes_lib import *
from hexdump import hexDump
import time

sx = SX1262()
sx.begin(freq=868, bw=125.0, sf=12, cr=5, syncWord=0x12,
         power=22, currentLimit=100.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=False, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=True, blocking=True)

randomBuff = sx.fillRandom(80)

pKey = randomBuff[0:32]
pIV = randomBuff[32:48]
plaintext = "this is a random sentence..."
print("Key")
hexDump(pKey)
print("IV")
hexDump(pIV)
print("Plaintext")
hexDump(plaintext)

encrypt = cbc_encryptor(pKey, pIV, plaintext)
decrypt = cbc_decryptor(pKey, encrypt.ciphertext)

print("ciphertext")
hexDump(encrypt.ciphertext)
print("deciphered")
hexDump(decrypt.plaintext)
print(decrypt.plaintext[0:len(plaintext)].decode() == plaintext)

