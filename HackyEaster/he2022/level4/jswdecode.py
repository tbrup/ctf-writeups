# from Python < 3
# see LICENSE file for licensing information

MAXLETTER = 'R'

# data at $9e00 dumped from emulator
DATA = '''
00000000  2b 4b 0d 78 ca 60 1d cd  5b 1e fe 2c c0 18 f3 11  |+K.x.`..[..,....|
00000010  f2 40 1a b7 ca a0 19 3c  32 9a 40 12 7e fe 87 28  |.@.....<2.@.~..(|
00000020  0c cd 5a 1e c0 7a b3 c2  c5 1e 3c 18 02 d7 c0 2a  |..Z..z....<....*|
00000030  ee 40 eb 2a ea 40 22 a2  40 eb c0 7e b7 20 04 23  |.@.*.@".@..~. .#|
00000040  23 23 23 23 7a a3 3c c2  05 1f 3a dd 40 3d ca be  |####z.<...:.@=..|
00000050  1d c3 05 1f cd 1c 2b c0  b7 ca 4a 1e 3d 87 5f fe  |......+...J.=._.|
00000060  2d 38 02 1e 26 c3 a2 19  11 0a 00 d5 28 17 cd 4f  |-8..&.......(..O|
00000070  1e eb e3 28 11 eb cf 2c  eb 2a e4 40 eb 28 06 cd  |...(...,.*.@.(..|
00000080  5a 1e c2 97 19 eb 7c b5  ca 4a 1e 22 e4 40 32 e1  |Z.....|..J.".@2.|
00000090  40 e1 22 e2 40 c1 c3 33  1a cd 37 23 7e fe 2c cc  |@.".@..3..7#~.,.|
000000a0  78 1d fe ca cc 78 1d 2b  e5 cd 94 09 e1 28 07 d7  |x....x.+.....(..|
000000b0  da c2 1e c3 5f 1d 16 01  cd 05 1f b7 c8 d7 fe 95  |...._...........|
000000c0  20 f6 15 20 f3 18 e8 3e  01 32 9c 40 c3 7c 20 cd  | .. ...>.2.@.| .|
000000d0  ca 41 fe 23 20 06 cd 84  02 32 9c 40 2b d7 cc fe  |.A.# ....2.@+...|
000000e0  20 ca 69 21 f6 20 fe 60  20 1b cd 01 2b fe 04 d2  | .i!. .` ...+...|
000000f0  4a 1e e5 21 00 3c 19 22  20 40 7b e6 3f 32 a6 40  |J..!.<." @{.?2.@|
'''

# handy-dandy utility function for mapping two bits into the
# corresponding numeric values; can change this to
#       return ( 'B', 'R', 'P', 'G' )[n]
# to print the results in terms of (B)lue/(R)ed/(P)ink/(G)reen

def bin2digit(n):
        return ( '1', '2', '3', '4' )[n]

# return the code at a given set of coordinates

def codeat(letter, digit):
        l = ord(letter) - ord('A')
        rowlen = ord(MAXLETTER) - ord('A') + 1
        index = (digit * rowlen) + l
        code = LUT[index] + index               # add index to duplicate "obfuscation"

        # decode to human-readable form
        L = []
        for i in range(4):
                L = [bin2digit(code & 0x3)] + L
                code >>= 2
        return ' '.join(L)

LUT = []                                        # LUT == look-up table

# break apart data in DATA and convert it into a useable form

for line in DATA.split('\n'):
        if len(line) == 0:                      # skip blank lines
                continue
        fields = line.split(' ')
        for hexbyte in fields[2:2+16+1]:
                if hexbyte == '':               # skip double space in middle
                        continue
                LUT.append(int(hexbyte, 16))

# print out the copy protection card's contents

for ordletter in range(ord('A'), ord(MAXLETTER)+1):
        letter = chr(ordletter)
        for digit in range(10):
                print(letter, digit, '=', codeat(letter, digit))
