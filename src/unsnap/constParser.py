import struct, opcode

TC_NONE = 0
TC_INT = 1
TC_STRING = 2
TC_FUNC = 3
TC_CFUNC = 4
TC_BOOL = 5
TC_TUPLE = 6
TC_ITER = 7
TC_BYTE_LIST = 8
TC_UNBOUND = 255
TCM_BLOBOFS = 64
TCM_DYNAMIC = 128

def parseConst(const, dblobsDict):
    (header,) = struct.unpack('B', const[0:1])
    if header == TC_NONE:
        return "None"

    if header == TC_INT:
        (intValue,) = struct.unpack('<H', const[1:3])
        if intValue == 0xffff:
            return -1
        return intValue

    if header == TC_BOOL:
        (intValue,) = struct.unpack('<H', const[1:3])
        if intValue == 0:
            return "False"
        if intValue == 1:
            return "True"

    if header == TC_BYTE_LIST:
        return "TC_BYTE_LIST"

    if header == TC_STRING | TCM_BLOBOFS:
        (dBlobOffset,) = struct.unpack('<H', const[1:3])
        try:
            return '\'{0}\''.format(dblobsDict[dBlobOffset])
        except:
            return "nope {0}".format(const.encode("hex"))
    return header

def parseGlobal(globalValue, dblobsDict):
    (header,) = struct.unpack('B', globalValue[0:1])

    if header == TC_NONE:
        return "None"

    if header == TC_INT:
        (intValue,) = struct.unpack('<H', globalValue[1:3])
        return "INT {0}".format(intValue)

    if header == TC_BOOL:
        (intValue,) = struct.unpack('<H', globalValue[1:3])
        if intValue == 0:
            return "BOOL False"
        if intValue == 1:
            return "BOOL True"

    if header == TC_STRING | TCM_BLOBOFS:
        (dBlobOffset,) = struct.unpack('<H', globalValue[1:3])
        try:
            return 'STRING \'{0}\''.format(dblobsDict[dBlobOffset])
        except:
            return "error"

    return header


def dumpBytecode(bytes, consts, funcs):
    rtnVal = ''
    n = len(bytes)
    i = 0
    while i < n-1:
        op = ord(bytes[i])

        try:
            funcs[i]
            rtnVal += "\n-----\n"
            rtnVal += funcs[i]
            rtnVal += '\nblob @ 0x%04x ' % i
            rtnVal += 'Func locals={0}\n'.format(op)
            i += 1
            continue
        except:
            pass
        i += 1
        opName = opcode.opname[op]
        rtnVal += '%3d (0x%02X) %s ' % (i, op, opName)

        if op >= opcode.HAVE_ARG16:
            oparg = ord(bytes[i]) * 256 + ord(bytes[(i + 1)])
            if op == opcode.opmap['JUMP_IF_FALSE'] or op == opcode.opmap['JUMP_IF_TRUE'] or op == opcode.opmap['JUMP_FORWARD']:
                oparg += i + 2
            rtnVal += str(oparg)
            if op == opcode.opmap['LOAD_CONST']:
                rtnVal += ' (%s)' % consts[oparg]
            i += 2
        elif op >= opcode.HAVE_ARGUMENT:
            rtnVal += '%i' % ord(bytes[i])
            i += 1
        rtnVal += '\n'

    return rtnVal