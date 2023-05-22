#                      flag_leds.8
# mem:0216 22 18 0b        undefine
#          03 0b 0a 
#          10 1f 18 
#    mem:0216 22  undefined1  22h [0]
#    mem:0217 18  undefined1  18h [1]
#    mem:0218 0b  undefined1  0Bh [2]
#    mem:0219 03  undefined1  03h [3]
#    mem:021a 0b  undefined1  0Bh [4]
#    mem:021b 0a  undefined1  0Ah [5]
#    mem:021c 10  undefined1  10h [6]
#    mem:021d 1f  undefined1  1Fh [7]
#    mem:021e 18  undefined1  18h [8]
#    mem:021f 25  undefined1  25h [9]
#    mem:0220 26  undefined1  26h [10]
#    mem:0221 02  undefined1  02h [11]
#    mem:0222 1f  undefined1  1Fh [12]
#    mem:0223 13  undefined1  13h [13]
#    mem:0224 23  undefined1  23h [14]
#    mem:0225 22  undefined1  22h [15]
#    mem:0226 16  undefined1  16h [16]
#    mem:0227 02  undefined1  02h [17]
#    mem:0228 16  undefined1  16h [18]
#    mem:0229 22  undefined1  22h [19]
#    mem:022a 18  undefined1  18h [20]
#    mem:022b 02  undefined1  02h [21]
#    mem:022c 19  undefined1  19h [22]
#    mem:022d 27  undefined1  27h [23]
#    mem:022e 15  undefined1  15h [24]
#    mem:022f 0f  undefined1  0Fh [25]
#


msg = [0x22, 0x18, 0x0b, 0x03, 0x0b, 0x0a, 0x10, 0x1f,
0x18, 0x25, 0x26, 0x02, 0x1f, 0x13, 0x23, 0x22,
0x16, 0x02, 0x16, 0x22, 0x18, 0x02, 0x19, 0x27,
0x15, 0x0f]

mapping = { 0x22: 'h', 0x18: 'e', 0xb: '2', 0x03: '0',
           0x0a: '3', 0x10: '{', 0x0f: '}', 0x02: '_',
           0x16: 't', 0x1f: 'l', 0x25: 'd', 0x26: 's'}

for i in msg:
    if i in mapping:
        print(f"{mapping[i]}, {ord(mapping[i]):08b} ", end ='')
    else:
        print(" ,          ", end ='')
    print(f"{i:3d} 0x{i:02x}, {i:08b}b")


for i in msg:
    if i in mapping:
        print(f"{mapping[i]}", end ='')
    else:
        print(" ", end ='')

print()
