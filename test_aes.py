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
plaintext = randomBuff[48:80]
print("Key")
hexDump(pKey)
print("IV")
hexDump(pIV)
print("Plaintext")
hexDump(plaintext)

encrypt = cbc_encryptor(pKey, pIV)
decrypt = aes(pKey, 2, pIV)

startTime = time.ticks_us()
ciphertext = encrypt.encrypt(plaintext[0:16]) + encrypt.encrypt(plaintext[16:32])
endTime = time.ticks_us()
print("Encryption: {} µs".format(endTime-startTime))

startTime = time.ticks_us()
deciphered = decrypt.decrypt(ciphertext[0:16]) + decrypt.decrypt(ciphertext[16:32])
endTime = time.ticks_us()
print("Decryption: {} µs".format(endTime-startTime))

print("ciphertext")
hexDump(ciphertext)
print("deciphered")
hexDump(deciphered)
print(deciphered == plaintext)

