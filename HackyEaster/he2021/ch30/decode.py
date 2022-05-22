import re
import sys
import requests


decryptionErrorRe = re.compile('Decryption Error.')
imageFoundRe = re.compile('src=\"data:image/png')
spanRe = re.compile('<span>(.+)</span>')
base_url = "http://46.101.107.117:2110/"
code_url = base_url+'picture?code='
cat = '05C9AF9CF1A450081E5775ED22E384D375CC5AAD7DE30BB2419F5F7D5D9973B310D5098C4189DFD0D80D0184781C0B590EBE65DF10D35DCCA62A746D60523D7E'
egg = '41E5D00E5CECC3019834C99B403DE4B24933AF3087BCE219699D7E3EB178A06F7B4717A36C617760EC0AD8BFD5DF05B2'
rab = '4DA28E65F0EDA286FAF7D6E886D2EB45D919F98AF2CA9F603CF581D83E9517CE9FD4DCE6DCC320715ED45844EA76274D1B4B1E381415A92CF29DC5E9FF7159A7'
ind = ' 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7'
myc = ' { " i m a g e " :   " e g g " , " e f f e c t " :   2 } X X X X 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5'
myr = ' { " i m a g e " :   " w i s e r a b b i t " , " e f f e c t " :   2 } X X X X X X X X X X X X X 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5'
# padding = 32
# iv = 'A'*(padding - 2)

def bitReverse(x):
    retVal = 0
    for i in range(8):
        retVal <<= 1
        retVal += x & 0x01
        x >>= 1
    return retVal


crib = '{"image": "wiserabbit", "effect": 2 }'
codes = []
for i in range(len(rab)//2):
    n = int(rab[2*i:2*i+2], 16)
    codes.append(n)

temp = []
for i in range(8):
    tmp = codes[i] ^  ord(crib[i+16])
    print(i+16, crib[i+16], '{:02x}'.format(tmp), '{:02x}'.format(codes[i+16]))
    print(i+16, crib[i+16], '{:08b}'.format(tmp), '{:08b}'.format(codes[i+16]))
    print(i+16, crib[i+16], '{:08b}'.format(tmp ^ codes[i+16]),
            '{:02x}'.format(tmp^codes[i+16]))
    print(i+16, crib[i+16], '{:02x}'.format(~tmp & 0xFF), '{:02x}'.format(codes[i+16]))


# for i in range(len(codes)-20,len(codes)):
#     print(hex(codes[i]))
#     tmp = []
#     for j in range(16):
#         tmp.append(codes[i] ^ codes[j])
#     print(tmp)
#     for x in tmp:
#         if x >32 and x<128:
#             print(chr(x), end='')
#         else:
#             print(' ', end='')
#     print()

# for j in range(1): #len(codes)):
#     print(' '*j, end='')
#     test = bitReverse(codes[j])
#     for i in range(j+1,len(codes)):
#         x = test ^ codes[i]
#         if x > 32 and x <128:
#             print(chr(x),end='')
#         else:
#             print(' ', end='')
#     print()


# for i in range(len(codes)):
#     print(hex(codes[i]), hex(bitReverse(codes[i])))
