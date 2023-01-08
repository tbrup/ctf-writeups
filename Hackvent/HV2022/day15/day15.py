import base64

import contextlib
import numpy as np


def filter(dta, window, apply=True):
    for i in range(len(dta) - window):
        tmp = np.sum(dta[i:i + window], dtype=np.int32) // window
        if apply:
            if tmp > 32:
                dta[i] = 127
            elif tmp < -32:
                dta[i] = -128
            else:
                dta[i] = 0
        else:
            dta[i] = tmp
    return dta


def amplPhase(raw):
    z = raw[::2] + 1j * raw[1::2]
    z -= 128.0 + 1j * 128.0

    ampl = np.absolute(z)
    phase = np.angle(z)
    # n = 3946500
    # for i in range(n, n+3000):
    #     print(f'{i}: raw {raw[2*i]}, {raw[2*i+1]}: {z[i]},  ampl: {ampl[i]:6.2f}, phase: {phase[i]:6.2f}')
    maxA = max(ampl)
    ampl = np.uint8(ampl / maxA * 250)
    phase = np.uint8(phase / np.pi * 120)
    print(f'max ampl: {maxA}')
    print(f'max ampl new: {max(ampl)}')
    ampl.tofile('ampl.cu8')
    phase.tofile('phase.cu8')
    return ampl, phase


def quantize(dta):
    res = np.zeros(len(dta), dtype=np.bool_)
    thresh = (max(dta) - min(dta)) // 2
    for i in range(len(dta)):
        res[i] = dta[i] >= thresh
    return res


def rllEncode(dta):
    res = []
    last, lastIndex = False, 0
    for i in range(1, len(dta)):
        if dta[i] != last:
            l = i - lastIndex
            res.append((last, l))
            last, lastIndex = dta[i], i
    print(res)
    return res


def scaleByPreamble(dta):
    nPre = 8 * 2
    preamble = dta[1:nPre]
    local_sum = sum(n for _, n in preamble)
    print(preamble)
    avg = local_sum / (nPre - 1)
    print(avg)
    return [(t, int(round(n / avg))) for t, n in dta[1:]]


def nrtzi(dta):
    res = '0'
    for (_, n) in dta[1:]:
        res += '1' + '0' * (n - 1)
    print(res)
    return res


def skipToFrame(dta):
    frame = '01111110'
    frame = '10000001'
    if frame in dta:
        return dta[dta.find(frame) + len(frame):]


def removeStuffBits(dta):
    res = ''
    n_ones = 0
    for i in range(len(dta)):
        val = dta[i]
        if n_ones == 5:
            if val == '0':  # we have a frame marker
                n_ones += 1
                res += val
            else:
                n_ones = 0
                print(f'dropping a 0: {dta[i - 6:i]}')
        else:
            if val == '0':
                n_ones += 1
            else:
                n_ones = 0
            res += val
    return res


def searchNbitNew(dta, n):
    ints = [int(dta[i:i + n], 2) & 0x7f for i in range(len(dta) - n)]
    chars = [chr(c) if c>=0x20 else ' ' for c in ints]   
    for i in range(stop=len(chars), step=40):
        print(chars[i:i+40]) 
    twos = [i for i,v in enumerate(ints) if v == 0x32]
    ss = [i for i,v in enumerate(ints) if v == 0x53]
    fs = [i for i,v in enumerate(ints) if v == 0x46]
    print(ss)
    print(fs)
    twos = []
    ss = []
    fs = []
    for i in range(len(dta) - n):
        c = int(dta[i:i + n][::-1], 2) & 0x7f
        if c >= 0x20:
            print(chr(c), end=' ')
        else:
            print(' ', end=' ')
        # print(f'{c:02x} ', end='')
        if c == 0x32:
            twos.append(i)
        elif c == 0x53:
            ss.append(i)
        elif c == 0x46:
            fs.append(i)
        if (i + 1) % 20 == 0:
            print()
    print()
    print(ss)
    print(fs)


def searchNbit(dta, n):
    twos = []
    ss = []
    fs = []
    for i in range(len(dta) - n):
        c = int(dta[i:i + n], 2) & 0x7f
        # print(f'{c:02x} ', end='')
        if c >= 0x20:
            print(chr(c), end=' ')
        else:
            print(' ', end=' ')
        if c == 0x32:
            twos.append(i)
        elif c == 0x53:
            ss.append(i)
        elif c == 0x46:
            fs.append(i)
        if (i + 1) % 20 == 0:
            print()
    print()
    print(ss)
    print(fs)
    twos = []
    ss = []
    fs = []
    for i in range(len(dta) - n):
        c = int(dta[i:i + n][::-1], 2) & 0x7f
        if c >= 0x20:
            print(chr(c), end=' ')
        else:
            print(' ', end=' ')
        # print(f'{c:02x} ', end='')
        if c == 0x32:
            twos.append(i)
        elif c == 0x53:
            ss.append(i)
        elif c == 0x46:
            fs.append(i)
        if (i + 1) % 20 == 0:
            print()
    print()
    print(ss)
    print(fs)


def pr(dta, offset, bits, rev=False):
    res = ''
    for i in range(offset, len(dta), bits):
        tmp = dta[i:i + bits]
        if rev:
            tmp = tmp[::-1]
        c = int(tmp, 2) & 0x7f
        res += chr(c) if c >= 0x20 and c <= ord('}') else ' '
    print(res)
    with contextlib.suppress(Exception):
        print(base64.b64decode(res))


def search7bit(dta):
    searchNbit(dta, 7)


def search6bit(dta):
    searchNbit(dta, 6)


if __name__ == '__main__':
    # raw = np.fromfile('cropped.cu8', dtype=np.uint8)
    raw = np.fromfile('message_1msps.cu8', dtype=np.uint8)

    a, ph = amplPhase(raw)

    a = np.reshape(a, (-1, 64))
    smooth = np.uint8(np.average(a, axis=1))

    quantized = quantize(smooth)
    rll = rllEncode(quantized)
    # print(rll)
    sc = scaleByPreamble(rll)
    print(sc)
    bits = nrtzi(sc)
    print(f'bits: {len(bits)} bit, {len(bits) // 8} bytes')
    # search7bit(bits[-512:])
    stuffed_msg = skipToFrame(bits)
    msg = removeStuffBits(bits)

    print(msg)
    # search7bit(msg)
    searchNbitNew(msg, 8)
    searchNbit(msg, 8)
    for i in range(8):
        pr(bits, i, 8, rev=False)
    for i in range(7):
        pr(bits, i, 8, rev=True)
    # searchNbit(msg, 8)
