# SnappyDecompiler
Decompile Synapse Wireless SNAPpy SPY files back to python bytecode

## Prerequisite
- Python 2.7
pip install --extra-index-url https://update.synapse-wireless.com/pypi snaplib -t .
    
## Usage
python snappyDecompiler.py sample.spy

## Sample output
Output from sample.spy, a simple led toggling script.

```
Length: 1199
ImageNamePstr(6): sample
Hook: Startup (68)
Hook: GPIN (1)
HooksPstr(14): D☺            
constOfs16: 30
namesOfs16: 284
globOfs16: 1142
constCount: 84
namesCount: 80
160: bist
165: buttonEvent
177: call
182: callback
191: callout
199: cbusRd
206: cbusWr
213: chr
217: crossConnect
230: dmCallout
240: dmcastRpc
250: eraseImage
261: errno
267: flowControl
279: getChannel
290: getDmxBuf
300: getEnergy
310: getI2cResult
323: getInfo
331: getLq
337: getMs
343: getNetId
352: getStat
360: i2cInit
368: i2cRead
376: i2cWrite
385: imageName
395: initUart
404: initVm
411: int
415: later
421: lcdPlot
429: len
433: loadNvParam
445: localAddr
455: mcastRpc
464: mcastSerial
476: monitorPin
487: nodeConfig
498: ord
502: peek
507: peekRadio
517: poke
522: pokeRadio
532: pulsePin
541: random
548: readAdc
556: readPin
564: reboot
571: resetVm
579: rpc
583: rpcSourceAddr
597: rx
600: saveNvParam
612: scanEnergy
623: setChannel
634: setNetId
643: setPinDir
653: setPinPullup
666: setPinSlew
677: setRadioRate
690: setRate
698: setSegments
710: sleep
716: spiInit
724: spiRead
732: spiWrite
741: spiXfer
749: startupEvent
762: stdinMode
772: str
776: txPwr
782: type
787: ucastSerial
799: uniConnect
810: updateDmxBuf
823: vmStat
830: writeChunk
841: writePin
850: xrange
globalsCount: 1
blobLength: 53
blobStart: 0x47a
SNAPpy Image Map:  sample  (0x9f7b)

Consts:
0x0000 (  0) : 'bist' = 042600
0x0001 (  1) : 'buttonEvent' = 030000
0x0002 (  2) : 'call' = 042900
0x0003 (  3) : 'callback' = 043e00
0x0004 (  4) : 'callout' = 044200
0x0005 (  5) : 'cbusRd' = 043000
0x0006 (  6) : 'cbusWr' = 043100
0x0007 (  7) : 'chr' = 042f00
0x0008 (  8) : 'crossConnect' = 041000
0x0009 (  9) : 'dmCallout' = 044b00
0x000a ( 10) : 'dmcastRpc' = 044a00
0x000b ( 11) : 'eraseImage' = 041c00
0x000c ( 12) : 'errno' = 042800
0x000d ( 13) : 'flowControl' = 040f00
0x000e ( 14) : 'getChannel' = 041800
0x000f ( 15) : 'getDmxBuf' = 044700
0x0010 ( 16) : 'getEnergy' = 043200
0x0011 ( 17) : 'getI2cResult' = 043800
0x0012 ( 18) : 'getInfo' = 043d00
0x0013 ( 19) : 'getLq' = 041400
0x0014 ( 20) : 'getMs' = 040400
0x0015 ( 21) : 'getNetId' = 042500
0x0016 ( 22) : 'getStat' = 043f00
0x0017 ( 23) : 'i2cInit' = 043500
0x0018 ( 24) : 'i2cRead' = 043700
0x0019 ( 25) : 'i2cWrite' = 043600
0x001a ( 26) : 'imageName' = 042700
0x001b ( 27) : 'initUart' = 040e00
0x001c ( 28) : 'initVm' = 041e00
0x001d ( 29) : 'int' = 042d00
0x001e ( 30) : 'later' = 044d00
0x001f ( 31) : 'lcdPlot' = 044100
0x0020 ( 32) : 'len' = 042300
0x0021 ( 33) : 'loadNvParam' = 041500
0x0022 ( 34) : 'localAddr' = 040d00
0x0023 ( 35) : 'mcastRpc' = 040300
0x0024 ( 36) : 'mcastSerial' = 041300
0x0025 ( 37) : 'monitorPin' = 040a00
0x0026 ( 38) : 'nodeConfig' = 044c00
0x0027 ( 39) : 'ord' = 041a00
0x0028 ( 40) : 'peek' = 040000
0x0029 ( 41) : 'peekRadio' = 044300
0x002a ( 42) : 'poke' = 040100
0x002b ( 43) : 'pokeRadio' = 044400
0x002c ( 44) : 'pulsePin' = 040b00
0x002d ( 45) : 'random' = 042b00
0x002e ( 46) : 'readAdc' = 040c00
0x002f ( 47) : 'readPin' = 040700
0x0030 ( 48) : 'reboot' = 041900
0x0031 ( 49) : 'resetVm' = 041b00
0x0032 ( 50) : 'rpc' = 040200
0x0033 ( 51) : 'rpcSourceAddr' = 042000
0x0034 ( 52) : 'rx' = 042200
0x0035 ( 53) : 'saveNvParam' = 041600
0x0036 ( 54) : 'scanEnergy' = 043300
0x0037 ( 55) : 'setChannel' = 041700
0x0038 ( 56) : 'setNetId' = 042400
0x0039 ( 57) : 'setPinDir' = 040500
0x003a ( 58) : 'setPinPullup' = 040600
0x003b ( 59) : 'setPinSlew' = 040800
0x003c ( 60) : 'setRadioRate' = 044500
0x003d ( 61) : 'setRate' = 042e00
0x003e ( 62) : 'setSegments' = 041f00
0x003f ( 63) : 'sleep' = 042100
0x0040 ( 64) : 'spiInit' = 043900
0x0041 ( 65) : 'spiRead' = 043b00
0x0042 ( 66) : 'spiWrite' = 043a00
0x0043 ( 67) : 'spiXfer' = 043c00
0x0044 ( 68) : 'startupEvent' = 032300
0x0045 ( 69) : 'stdinMode' = 042c00
0x0046 ( 70) : 'str' = 044000
0x0047 ( 71) : 'txPwr' = 043400
0x0048 ( 72) : 'type' = 044800
0x0049 ( 73) : 'ucastSerial' = 041200
0x004a ( 74) : 'uniConnect' = 041100
0x004b ( 75) : 'updateDmxBuf' = 044600
0x004c ( 76) : 'vmStat' = 042a00
0x004d ( 77) : 'writeChunk' = 041d00
0x004e ( 78) : 'writePin' = 040900
0x004f ( 79) : 'xrange' = 044900
0x0050 ( 80) : None = 000000
0x0051 ( 81) : True = 050100
0x0052 ( 82) : 1 = 010100
0x0053 ( 83) : 2 = 010200

Globals:
  0 : BOOL False


-----
buttonEvent
blob @ 0x0000 Func locals=2
  2 (0x6E) LOAD_FAST 1
  4 (0x7D) JUMP_IF_TRUE 30
  7 (0x01) POP_TOP
  8 (0x74) LOAD_GLOBAL 0
 11 (0x0C) UNARY_NOT
 12 (0x7E) STORE_GLOBAL 0
 15 (0x7C) LOAD_CONST 78 ('writePin')
 18 (0x7C) LOAD_CONST 83 (2)
 21 (0x74) LOAD_GLOBAL 0
 24 (0x83) CALL_FUNCTION 2
 27 (0x01) POP_TOP
 28 (0x72) JUMP_FORWARD 31
 31 (0x01) POP_TOP
 32 (0x7C) LOAD_CONST 80 (None)
 35 (0x53) RETURN_VALUE

-----
startupEvent
blob @ 0x0023 Func locals=0
 37 (0x7C) LOAD_CONST 37 ('monitorPin')
 40 (0x7C) LOAD_CONST 82 (1)
 43 (0x7C) LOAD_CONST 81 (True)
 46 (0x83) CALL_FUNCTION 2
 49 (0x01) POP_TOP
 50 (0x7C) LOAD_CONST 80 (None)
```

## Documentation
[https://developer.synapse-wireless.com/](https://developer.synapse-wireless.com/)

## License
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](LICENSE)