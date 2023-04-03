from sx1262 import SX1262
import time
#import radio_cfg as radio

print("sx")
sx = SX1262(cs=13, irq=29, rst=14, gpio=15, clk=10, mosi=11, miso=12)
print("begin")
sx.begin(blocking=False, syncWord=0x1444)

print("ready to go")
start = time.ticks_ms()
interval = 10000
counter = 0

while True:
    msg, err = sx.recv()
    if len(msg) > 0:
        print("len(msg) = {}".format(len(msg)))
        error = SX1262.STATUS[err]
        print(msg)
        print(error)
    if time.ticks_ms() - start >= interval:
        msg = ("PING #{} ".format(counter))*10
        counter += 1
        print("Sending `{}`".format(msg))
        sx.send(bytearray(msg))
        start = time.ticks_ms()