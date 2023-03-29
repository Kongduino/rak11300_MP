from sx1262 import SX1262
from pinout import *
from aes_lib import *
from hexdump import hexDump
import time, sys

sx = SX1262()
sx.begin(freq=868, bw=125.0, sf=12, cr=5, syncWord=0x12,
         power=22, currentLimit=100.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=False, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=True, blocking=True)
randomBuff = sx.fillRandom(80)

pKey = randomBuff[0:32]
pIV = randomBuff[32:48]
plaintext = b"tagada pouet pouet\x00"
print("Key")
hexDump(pKey)
print("Plaintext")
hexDump(plaintext)

enc = cbc_encryptor(pKey, pIV, plaintext)
if enc.inited == False:
    print("Failed to init cbc_encryptor!")
    sys.exit()
print("Ciphertext with IV")
hexDump(enc.ciphertext)

dec = cbc_decryptor(pKey, enc.ciphertext)
if dec.inited == False:
    print("Failed to init cbc_decryptor!")
    sys.exit()
print("Deciphered")
hexDump(dec.plaintext)

ln = len(plaintext)
print(dec.plaintext.decode())
print(dec.plaintext[0:ln] == bytearray(plaintext))
