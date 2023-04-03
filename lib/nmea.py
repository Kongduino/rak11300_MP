import gc


class NMEAParser():
    def __init__(self, uart):
        self._uart = uart
        self.UTCTime = "??:??:??"
        self.TXT = []
        self.hasTXT = False
        self.hasFix = False
        self.hasSIV = False
        self.SIV = -1
        self.fixMode = ''
        self.fixType = ''
        self.latitude = None
        self.longitude = None
        self.fixQuality = -1
        self.hasFixQuality = False
        self.textFixQuality = []
        self.textFixQuality.append("GPS fix")
        self.textFixQuality.append("Diff. GPS Fix")
        self.TTMG = False
        self.MTMG = False
        self.knots = False
        self.kpm = False
        buf = uart.read() # flush
        self.remainder = b''

    def parseDegrees(self, term):
        value = float(term) / 100.0
        left = int(value)
        value = (value - left) * 1.66666666666666
        value += left
        return value

    def setGPS(self, result, start):
        self.hasFix = True
        signLat = 1
        signLong = 1
        if result[start+1] == b'W':
            signLat = -1
        if result[start+3] == b'S':
            signLong = -1
        newLatitude = signLat * self.parseDegrees(result[start])
        newLongitude = signLong * self.parseDegrees(result[start+2])
        if self.longitude != newLongitude or self.latitude != newLatitude:
            self.latitude = newLatitude
            self.longitude = newLongitude

    def feed(self, buffer):
        self.hasTXT = (len(self.TXT) > 0)
        buf = (self.remainder+buffer).split(b'\r\n')
        self.remainder = buf.pop()
        for line in buf:
            if line.startswith(b'$'):
                if line.find(b'*') > -1:
                    [line, crc] = line.split(b'*')
                    chunks=line.split(b',')
                    verb = chunks[0][3:]
                    if verb == b'TXT':
                        self.parseGPTXT(chunks)
                    elif verb == b'RMC':
                        self.parseGPRMC(chunks)
                    elif verb == b'GSV':
                        self.parseGPGSV(chunks)
                    elif verb == b'GGA':
                        self.parseGPGGA(chunks)
                    elif verb == b'GSA':
                        self.parseGPGSA(chunks)
                    elif verb == b'GLL':
                        self.parseGPGLL(chunks)
                    elif verb == b'VTG':
                        self.parseGPVTG(chunks)
                    elif verb!=b'':
                        print(line)
    gc.collect()

    def setTime(self, result):
        hh = result[0:2].decode()
        mm = result[2:4].decode()
        ss = result[4:6].decode()
        self.UTCTime = "{}:{}:{} UTC".format(hh, mm, ss)

    def parseGPVTG(self, result):
        if result[1] != b'':
            self.TTMG = float(result[1])
        else:
            self.TTMG = False
        if result[3] != b'':
            self.MTMG = float(result[3])
        else:
            self.MTMG = False
        if result[5] != b'':
            self.knots = float(result[5])
        else:
            self.knots = False
        if result[7] != b'':
            self.kpm = float(result[7])
        else:
            self.kpm = False

    def parseGPRMC(self, result):
        if result[1] != b'':
            #print("RMC set time to {}".format(result[1]))
            self.setTime(result[1])
        if result[2] != b'A' or result[3] == b'':
            self.hasFix = False
            return
        self.setGPS(result, 3)

    def parseGPGLL(self, result):
        if result[1] != b'':
            self.setGPS(result, 1)
            if len(result) > 5:
                if result[5] != b'':
                    #print("GLL set time to {}".format(result[5][0:6]))
                    self.setTime(result[5][0:6])

    def displayFixQuality(self):
        if self.hasFixQuality == False:
            return
        self.hasFixQuality = False
        #print("Fix quality: {}".format(self.textFixQuality[self.fixQuality]))


    def parseGPGGA(self, result):
        if result[1] != b'':
            #print("GGA set time to {}".format(result[1]))
            self.setTime(result[1])
        quality = int(result[6])
        if quality == 0:
            self.hasFix == False
            return
        self.hasFix = True
        self.fixQuality = quality
        self.hasFixQuality = True
        self.setGPS(result, 2)

    def parseGPGSA(self, result):
        if result[1] != b'':
            if result[1] == b'A':
                self.fixType = "Automatic"
            elif result[1] == b'M':
                self.fixType = "Manual"
            if result[2] == b'1':
                self.fixMode = "Fix not available."
                self.hasFix = False
            else:
                self.fixMode = result[2].decode() + "D fix."
                self.hasFix = True

    def parseGPGSV(self, result):
        if result[1] != b'':
            newSIV = int(result[3])
            if self.SIV != newSIV:
                self.SIV = newSIV
                self.hasSIV = True
            else:
                self.hasSIV = False

    def parseGPTXT(result):
        if result[1] != b'':
            self.TXT.append(result[4])
            self.hasTXT = True
    
    def showTexts(self):
        if self.hasTXT == False:
            return
        ln = len(self.TXT)
        for i in range(0, ln):
            print("Message {} of {}: {}".format(i+1, ln, self.TXT[i]))
        self.TXT = []
        self.hasTXT = False
