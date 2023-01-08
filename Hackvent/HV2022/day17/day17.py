import math

# first create the binary file
with open('SantasSleigh.raw', 'r') as inF:
    binStr = ''
    res = b''
    resStr = ''
    bit0 = ''
    bit1 = ''
    for c in inF.read():
        tmp = f'{int(c):02b}'
        binStr += tmp
        bit0 += tmp[0]
        bit1 += tmp[1]
        if len(binStr) == 8:
            res += int(binStr, 2).to_bytes(1)
            resStr += binStr  # f'{int(binStr,2):x}'
            binStr = ''

    with open('ss.bin', 'wb') as outF:
        outF.write(res)

    # print(resStr)
    # with open('ss.can', 'wb') as outF:
    #     outF.write(resStr.encode(encoding='ASCII'))

    with open('bit0.txt', 'w') as outF:
        outF.write(bit0)
    with open('bit1.txt', 'w') as outF:
        outF.write(bit1)

count = {}
for i in range(0, len(bit0), 4):
    tmp = bit0[i:i + 4]
    if tmp in count:
        count[tmp] += 1
    else:
        count[tmp] = 1

print(count)
count = {}
for i in range(0, len(bit1), 4):
    tmp = bit1[i:i + 4]
    if tmp in count:
        count[tmp] += 1
    else:
        count[tmp] = 1

print(count)


def rllStatistics(dta):
    res = ''
    count = {}
    last, lastIndex = dta[0], 2
    for i in range(3, len(dta)):
        if dta[i] != last:
            l = i - lastIndex
            n_char = int(round(l / 4))
            res += last * n_char
            if l in count:
                count[l] += 1
            else:
                count[l] = 1
            last = dta[i]
            lastIndex = i
    print(count)
    print(res)
    return res


def searchPrintables(dta):
    for i in range(8):
        res = ''
        resRev = ''
        for j in range(i, len(dta), 8):
            c = int(dta[j:j + 8], 2)
            res += chr(c & 0x7f)
            c = int(dta[j:j + 8][::-1], 2)
            resRev += chr(c & 0x7f)
        print(res)
        print(resRev)


def search7bit(dta):
    res = ''
    for j in range(1202, len(dta), 9):
        c = int(dta[j:j + 7][::-1], 2) & 0x7f
        c2 = chr(c) if c > 32 else ' '
        # print(f'  {j:4d}: {c1} {c2} : {ord(c1)} {ord(c2)}')
        res += c2
    print(res)


def searchCrib(dta, rev=False):
    occurrences1 = {'H': [], 'V': [], '2': []}
    res = ''
    for j in range(len(dta)):
        tmp = dta[j:j + 7]
        if rev:
            tmp = tmp[::-1]
        c1 = chr(int(tmp, 2) & 0x7f)
        if c1 in occurrences1:
            occurrences1[c1].append(j)

        # print(f'  {j:4d}: {c1} {c2} : {ord(c1)} {ord(c2)}')
    if rev:
        print('reversed bit order')
    print(occurrences1)


b0 = rllStatistics(bit0)
b1 = rllStatistics(bit1)

# searchPrintables(b0)
# searchPrintables(b1)
searchCrib(b0, rev=False)
searchCrib(b0, rev=True)
searchCrib(b1, rev=False)
searchCrib(b1, rev=True)

search7bit(b0)
search7bit(b1)
