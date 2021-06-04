import sys
from snaplib import SnappyGen
from unsnap import decryptor
from unsnap import unpacker

SnappyGen.fixupOpcodeModule()

args = sys.argv[1:]
filename = args[0]
decryptedFileName = decryptor.decryptSnapSpy(filename)

unpackedSnap = unpacker.UnpackedSnap()
unpackedSnap.unpackFromFile(decryptedFileName)

unpackedSnap.printMap()
