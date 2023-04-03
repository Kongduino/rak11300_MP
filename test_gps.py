from micropython import const
from machine import UART
import time, gc, sys
from pinout import *
from machine import Pin
from machine import Timer
from nmea import *

WISBLOCK_EN = Pin(WB_IO2, Pin.OUT)
WISBLOCK_EN.off()
time.sleep(0.1)
WISBLOCK_EN.on()
gps = UART(0, baudrate=9600)
print(gps)
nmea = NMEAParser(gps)

DELAY = const(10000)
lastCheck = time.ticks_ms() - DELAY + 1000
while True:
    buf = gps.read()
    if buf != None:
        nmea.feed(buf)
    if time.ticks_ms() - lastCheck > DELAY:
        print("-----------------------------------------")
        if nmea.hasTXT:
            nmea.showTexts()
        lastCheck = time.ticks_ms()
        if nmea.hasSIV == True:
            print("SIV: {}".format(nmea.SIV))
        if nmea.fixMode != "":
            print("Fix type: {}".format(nmea.fixType))
            print("Fix mode: {}".format(nmea.fixMode))
        print(nmea.UTCTime)
        if nmea.hasFix == True:
            print("Location: {}, {}".format(nmea.latitude, nmea.longitude))
        if nmea.hasFixQuality:
            nmea.displayFixQuality()
        if nmea.knots != False:
            print("Speed: {} knots".format(nmea.knots))
        if nmea.kpm != False:
            print("Speed: {} km/h".format(nmea.kpm))
        lastCheck = time.ticks_ms()

        

