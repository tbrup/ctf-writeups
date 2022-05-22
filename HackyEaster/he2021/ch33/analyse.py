from mnemonic import Mnemonic

challenge = {
    'adapt':    0x3555,
    'bind':     0x824e,
    'bless':    0x8fcf,
    'blind':    0x81db,
    'civil':    0x03ec,
    'craft':    0xed05,
    'garage':   0x9db4,
    'good':     0xd2ba,
    'half':     0x1272,
    'hip':      0x8d53,
    'home':     0x21b7,
    'hotel':    0x1cb0,
    'lonely':   0xe5b8,
    'magnet':   0x16b9,
    'metal':    0x770e,
    'mushroom': 0xdd80,
    'napkin':   0x0829,
    'reason':   0xecd3,
    'rescue':   0x5ef2,
    'ring':     0xe3b0,
    'shift':    0x4ea1,
    'small':    0xf1f6,
    'sunset':   0xb271,
    'tongue':   0xf08d
}


def getWordList():
    with open('english.txt', 'r') as inF:
        retVal = {}
        index = 0
        for w in inF.readlines():
            retVal[w[:-1]] = index
            index += 1
        return retVal


def toBin(v):
    return '{:011b}'.format(v)


def makeHeader(l,wl):
    retVal = ''
    for k in l:
        tmp = toBin(wl[k])
        retVal += tmp
    return retVal


def toByteArray(s):
    bound = len(s)//8
    if len(s) % 8 == 0:
        bound -= 1
    retVal = b''
    for i in range(0, bound):
        tmp = int(s[i*8:(i+1)*8],2) & 0xFF
        retVal += tmp.to_bytes(1,'little')
    return retVal



def isAscii(s):
    bound = len(s)//8
    if len(s) % 8 == 0:
        bound -= 1
    for i in range(0, bound):
        tmp = int(s[i*8:(i+1)*8],2) & 0xFF
        if tmp<0x20 or tmp>127:
            return False
    return True

wl = getWordList()

# print(wl['adapt'])
# print(challenge['adapt'])

# invCh = {}
# for k in challenge.keys():
#     invCh[challenge[k]] = k

# for k in sorted(invCh.keys()):
#     print(k, invCh[k])

# for k in challenge.keys():
#     print('{:10s}'.format(k), '{:016b}'.format(challenge[k]), '{:016b}'.format(wl[k]))

# print()

# sl = {}
# for k in challenge.keys():
#     c = challenge[k]
#     w = wl[k]
#     tmp = (c ^ w) & 2047
#     print('{:10s}'.format(k), '{:#4d}'.format(tmp), '{:04x}'.format(tmp))
#     sl[c] = k

# for k in sorted(sl.keys()):
#     print(sl[k])

# input = []
# for k in sorted(sl.keys()):
#     input.append(sl[k])

# mnemo = Mnemonic("english")

# seed = mnemo.to_seed(' '.join(input), passphrase="")
# print(seed)
# entropy = mnemo.to_entropy(' '.join(input))
# print(entropy)

# for k in sorted(challenge.keys()):
#     ror = lambda val, r_bits, max_bits: \
#         ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
#         (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))
#     print(k, end='')
#     for i in range(16):
#         x = challenge[k] ^ ror(wl[k], i, 16)
#         print(' {:04X}'.format(x), end='')
#     print()

mnemo = Mnemonic("english")
trial = b'he2021{123456789012345678901234}'
words = mnemo.to_mnemonic(trial)
print(words)
trial = b'he2021{f1sh_@r3_012345678901234}'

words = mnemo.to_mnemonic(trial)
print(words)
# entropy = mnemo.to_entropy(' '.join(input))

part = ['half','civil','metal','good','bless', 'reason',
        'shift','home', 'garage', 'rescue']
part = ['half','civil','metal','good','bless', 'reason', 'shift', 'home',
        'garage', 'napkin', 'sunset', 'tongue', 'bind', 'rescue', 'mushroom',
        'hip', 'hotel', 'lonely', 'blind', 'small', 'adapt', 'craft', 'magnet']
        # 'ring']

for k in part:
    v = challenge[k]
    w = wl[k]
    print('{:10s}'.format(k),
          '{:04x}'.format(v),'{:016b}'.format(w),'{:016b}'.format(w^v))

vorrat = set()
for k in challenge.keys():
    if k not in part:
        vorrat.add(k)


# for k in part:
#     vorrat.remove(k)

header = makeHeader(part, wl)
print(len(header)//11, header)

for k in vorrat:
    tmp = header + toBin(int(wl[k]))
    if isAscii(tmp):
        print(k, '-->', toByteArray(tmp))

    # v = challenge[k]
    # w = wl[k]
    # print('{:10s}'.format(k),
    #       '{:016b}'.format(v),'{:016b}'.format(w),'{:016b}'.format(w^v))
# for
