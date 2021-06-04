import struct,binascii

from snappy.SnapConstants import HOOK_DESCRIPTIONS
from unsnap import constParser

"""
 len16      (over everything but len16 itself)
 imageNamePstr
 hooksPstr
 constOfs16
 namesOfs16
 globOfs16
 dBlob
 consts
 names
 globals
 blob
 crc16     (covers everything but crc16 itself)

* offsets are from base of image (before len16)
* names, globals begin with U8 num field
* consts begins with U16 num field
"""

class UnpackedSnap:

    def __init__(self):
        self.length = 0
        self.imageNamePstr = ''
        self.hooksPstr = ''
        self.hooks = {}
        self.hooksConsts = {}
        self.constOfs16 = 0
        self.namesOfs16 = 0
        self.globOfs16 = 0
        self.dBlobs = []
        self.dBlobsDict = {}
        self.consts = []
        self.namesOfs = []
        self.names = []
        self.globals = []
        self.blob = ''
        self.crc = 0

    def unpackFromFile(self, filename):

        with open(filename, "rb") as binary_file:

            (self.length,) = struct.unpack('H', binary_file.read(2))
            print 'Length: {0}'.format(self.length)
            pointer = 2

            (imageNamePstrLength,) = struct.unpack('B', binary_file.read(1))
            pointer += 1

            self.imageNamePstr = binary_file.read(imageNamePstrLength)
            print 'ImageNamePstr({0}): {1}'.format(imageNamePstrLength, self.imageNamePstr)

            pointer += imageNamePstrLength

            (hooksPstrLength,) = struct.unpack('B', binary_file.read(1))
            pointer += 1

            self.hooksPstr = binary_file.read(hooksPstrLength)
            for i in range(hooksPstrLength):
                (hooksPstrTmp,) = struct.unpack('B', self.hooksPstr[i])
                if hooksPstrTmp != 255:
                    self.hooks[i] = HOOK_DESCRIPTIONS[i]
                    self.hooksConsts[i] = hooksPstrTmp

            for hook in self.hooks:
                print 'Hook: {0} ({1})'.format(self.hooks[hook], self.hooksConsts[hook])

            print 'HooksPstr({0}): {1}'.format(hooksPstrLength, self.hooksPstr)
            pointer += hooksPstrLength

            (self.constOfs16,) = struct.unpack('H', binary_file.read(2))
            print 'constOfs16: {0}'.format(self.constOfs16)
            pointer += 2

            (self.namesOfs16,) = struct.unpack('H', binary_file.read(2))
            print 'namesOfs16: {0}'.format(self.namesOfs16)
            pointer += 2

            (self.globOfs16,) = struct.unpack('H', binary_file.read(2))
            print 'globOfs16: {0}'.format(self.globOfs16)
            pointer += 2

            blobPointer = pointer
            while pointer < self.constOfs16:
                (dBlobLength,) = struct.unpack('B', binary_file.read(1))
                pointer += 1
                print dBlobLength
                if dBlobLength == 0:
                    (dBlobLength,) = struct.unpack('B', binary_file.read(1))
                    pointer += 1
                if dBlobLength == 0:
                    dBlob = '0'
                    self. dBlobsDict[pointer - blobPointer - 2] = dBlob
                else:
                    dBlob = binary_file.read(dBlobLength)
                    self.dBlobsDict[pointer - blobPointer - 1] = dBlob
                self.dBlobs.append(dBlob)
                pointer += dBlobLength

            binary_file.seek(self.constOfs16)
            (constCount,) = struct.unpack('H', binary_file.read(2))
            print 'constCount: {0}'.format(constCount)
            pointer += 2


            for i in range(constCount):
                self.consts.append(binary_file.read(3))
                pointer += 3

            (namesCount,) = struct.unpack('B', binary_file.read(1))
            pointer += 1

            if namesCount == 2:
                (namesCount,) = struct.unpack('H', binary_file.read(2))
                pointer += 2

            print 'namesCount: {0}'.format(namesCount)

            for i in range(namesCount):
                (nameOf,) = struct.unpack('H', binary_file.read(2))
                self.namesOfs.append(nameOf)
                pointer += 2

            for i in range(namesCount):
                (nameCount,) = struct.unpack('B', binary_file.read(1))
                pointer += 1
                self.names.append(binary_file.read(nameCount))
                pointer += nameCount

            for i in range(namesCount):
                print '{0}: {1}'.format(self.namesOfs[i], self.names[i])

            (globalsCount,) = struct.unpack('B', binary_file.read(1))
            pointer += 1
            print 'globalsCount: {0}'.format(globalsCount)

            for i in range(globalsCount):
                self.globals.append(binary_file.read(3))
                pointer += 3

            blobLength = self.length - pointer
            print 'blobLength: {0}'.format(blobLength)
            print 'blobStart: 0x{0:x}'.format(pointer)

            self.blob = binary_file.read(blobLength)
            pointer += blobLength

            (self.crc,) = struct.unpack('<H', binary_file.read(2))

    def printMap(self):
        mapText = 'SNAPpy Image Map:  %s  (0x%04x)\n' % (self.imageNamePstr, self.crc)
        mapText += '\nConsts:\n'

        constArray = ''.join(self.consts)
        parsedConsts = {}
        parsedConstsNames = {}

        for i in range(len(self.consts)):
            constOfs = 3 * i
            if i < len(self.names):
                constString = '\'{0}\''.format(self.names[i])
                parsedConsts[i] = constString
                parsedConstsNames[binascii.hexlify(constArray[constOfs:constOfs + 3])] = constString
                mapText += '0x%04x (%3d) : %s = %s\n' % \
                (i, i, constString, binascii.hexlify(constArray[constOfs:constOfs + 3]))
            else:
                parsedConst = constParser.parseConst(self.consts[i], self.dBlobsDict)
                parsedConsts[i] = parsedConst
                mapText += '0x%04x (%3d) : %s = %s\n' % (
                i, i, parsedConst, binascii.hexlify(constArray[constOfs:constOfs + 3]))

        mapText += '\nGlobals:\n'
        i = 0
        for nm in self.globals:
            mapText += '%3d : %s\n' % (i, constParser.parseGlobal(nm, self.dBlobsDict))
            i += 1

        print mapText

        funcs = {}
        constNum = 0
        for const in self.consts:
            (header,) = struct.unpack('B', const[0:1])
            if header == 3:
                (value, ) = struct.unpack('H', const[1:3])
                funcs[value] = self.names[constNum]
            constNum += 1

        print constParser.dumpBytecode(self.blob, parsedConsts, funcs)
