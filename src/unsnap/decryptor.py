import math, bz2, os

from snaplib.ppcrypto import ARC4

# _SNAPPY_EXPORT_KEY
encoder = ARC4("SynapseExport" + str(math.pi))

def decryptSnapSpy(file):
    (filename_and_path, extension) = os.path.splitext(file)
    with open(file, "rb") as binary_file:
        data = binary_file.read()
        exportString = encoder.decrypt(data)
        decomp_data = bz2.decompress(exportString)
        newFileName = "{0}.unspy".format(filename_and_path)
        with open(newFileName, "wb") as unspy:
            unspy.write(decomp_data)
            return newFileName