#!/usr/bin/env python3
# vim: tw=78

import itertools
import statistics
import math
import pwn

pwn.pwnlib.context.context.defaults['encoding'] = 'utf-8'

KEYSIZE = 768
HB_COUNT = (KEYSIZE // 64) // 4 * 3
NBITS = 384
NBITS = 400
R = 2 ** 512


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def calc_block(us):
    s1, s2 = 0, 0
    for v in us:
        s1 = (s1 + v) & 0xffff_ffff
        s2 = (s2 + s1) & 0xffff_ffff
    return ((s2 << 32) | s1) & 0xffff_ffff_ffff_ffff


def calc_vs(u):
    s1 = u % 0x1_0000_0000
    s2 = u // 0x1_0000_0000
    v1 = (s2 - s1) & 0xffff_ffff
    v2 = (s1 - v1) & 0xffff_ffff
    # print(f's1 : {s1:08x}, s2: {s2:08x}')
    # print(f'v1 : {v1:08x}, v2: {v2:08x}')
    tmp = (v1 + v2) & 0xffff_ffff
    tmp1 = (v1 + v1 + v2) & 0xffff_ffff
    # print(f'v1+v2 : {tmp:09x}, {tmp1:08x}')
    return [v1, v2]


def bin_msg_to_txt(msg):
    return ''.join(f'{b:02x}' for b in msg)


def txt_msg_to_bin(msg):
    res = b''
    for t in chunker(msg, 2):
        res += int(t, 16).to_bytes(1, byteorder='little')
    return res


def msg_to_bseg(msg):
    segs = [[] for _ in range(HB_COUNT)]
    for (i, b) in enumerate(msg):
        segs[i % HB_COUNT].append(b)
    return segs


def bseg_to_vseg(b_segs):
    v_segs = []
    for seg in b_segs:
        m = len(seg) % 4
        if m != 0:
            for _ in range(4 - m):
                seg.append(0)
        newSeg = [int.from_bytes(t, 'little') for t in chunker(seg, 4)]
        v_segs.append(newSeg)
    return v_segs


# re-creation of the rust function, given a msg matches the
# implemntation on-line
def hash(msg):
    b_segs = msg_to_bseg(msg)
    v_segs = []
    s_segs = []
    digest = b''
    for seg in b_segs:
        m = len(seg) % 4
        for _ in range(m):
            seg.append(b'\x00')

        newSeg = [int.from_bytes(t, 'little') for t in chunker(seg, 4)]
        v_segs.append(newSeg)
        s = calc_block(newSeg)
        s_segs.append(s)
        # print(f'0x{s:016x}')
        digest += s.to_bytes(8, byteorder='little')
    # for s in s_segs:
    #     print(f'{s:016x}')
    return digest[::-1]


def hash2(msg):
    b_segs = msg_to_bseg(msg)
    v_segs = bseg_to_vseg(b_segs)
    s_segs = vseg_to_seg(v_segs)
    return sseg_to_bits(s_segs)


def bytes_to_seg(byt):
    return [int.from_bytes(t, 'little') for t in chunker(byt, 8)]


def seg_to_u(segs):
    window = (1 << 64)
    u = 0
    for s in segs[::-1]:
        u *= window
        u += s
    return u


def sseg_to_bits(segs):
    digest = b''
    for s in segs:
        digest += s.to_bytes(8, byteorder='little')
    return digest[::-1]


def seg_to_vseg(seg):
    return [calc_vs(s) for s in seg]


def vseg_to_seg(v_seg):
    return [calc_block(vs) for vs in v_seg]


def vseg_to_bseg(v_seg):
    b_seg = []
    for s in v_seg:
        # print(f'v1: {s[0]:08x}, v2: {s[1]:08x}')
        # print(f'u:  {calc_block(s):08x}, v2: {s[1]:08x}')
        tmp = []
        for v in s:
            tmp.extend(v.to_bytes(4, byteorder='little'))
        b_seg.append(tmp)

    return b_seg


def bseg_to_msg(b_seg):
    res = b''
    for i in range(HB_COUNT * 8):
        tmp = b_seg[i % HB_COUNT]
        tmp2 = tmp[i // HB_COUNT]
        res += tmp2.to_bytes(1, byteorder='little')
    return res


def reverse_hash(u):
    byt = u.to_bytes(HB_COUNT * 8, 'little')
    seg = bytes_to_seg(byt)
    v_seg = seg_to_vseg(seg)
    b_seg = vseg_to_bseg(v_seg)
    bin_msg = bseg_to_msg(b_seg)
    return bin_msg[::-1]


def reverse_hash2(u):
    byt = u.to_bytes(HB_COUNT * 8, 'big')
    s_segs = bytes_to_seg(byt)
    v_segs = seg_to_vseg(s_segs)
    b_segs = vseg_to_bseg(v_segs)
    return bseg_to_msg(b_segs)


def getNFlag(p):
    p.recvuntil(b'modulus: n = ')
    n = p.recvline().decode('ascii').strip()
    # print(n)
    p.recvuntil(b' [yN]')
    p.sendline(b'n')
    p.recvuntil(b': ')
    flag = p.recvline().decode('ascii').strip()
    # print(flag)
    return n, flag


def getNEP(p):
    print(p.recvuntil(b'modulus: n = '))
    n = p.recvline().decode('ascii').strip()
    print(n)
    print(p.recvuntil(b'exponent: e = '))
    e = p.recvline().decode('ascii').strip()
    print(e)
    print(p.recvuntil(b'prime: p = '))
    prime = p.recvline().decode('ascii').strip()
    print(hex(int(prime[:-3], 16)))
    energy = p.recvline().decode('ascii').strip()
    energy = int(energy.split(' ')[2])
    print(energy)
    return int(n, 16), int(e, 16), int(prime[:-3], 16), energy


def decode_sig(sig, n, e):
    return pow(sig, e, n)


def getSigTxt(p, t, nrg: int):
    p.recvuntil(b' [yN]')
    p.sendline(b'y')
    p.recvuntil(b'?')
    p.sendline(t)
    p.recvuntil(b': ')
    sig = p.recvline().decode('ascii').strip()
    energy = p.recvline().decode('ascii').strip().split(' ')
    energy = int(energy[2])
    return nrg - energy, sig, energy


def getSig(p, u: int, nrg: int):
    msg = reverse_hash2(u)
    t = bin_msg_to_txt(msg)
    return getSigTxt(p, t, nrg)


def findBisect(u1, u2):
    return (u1 + u2) // 2


def confirmInterval(p, u2, u1, thresh, factor, energy):
    NTRIES = 16
    # NTRIES = 8
    NSTEP = 2 ** 96
    NSTEP = 1
    tu1s, tu2s = [], []
    for i in range(NTRIES * factor):
        tu1, _, energy = getSig(p, u1 * 2 + i * NSTEP, energy)
        tu2, _, energy = getSig(p, u2 * 2 - i * NSTEP, energy)
        tu1s.append(tu1)
        tu2s.append(tu2)

    ds = [tu2s[i] - tu1s[j] for i, j in itertools.product(range(NTRIES * factor), range(NTRIES * factor))]

    cnt = sum(1 if d < thresh else -1 for d in ds)
    cnt_thresh = len(ds) // 2  # NTRIES*NTRIES*factor*factor
    return (True, energy) if cnt > 0 else (False, energy)


TIMINGS = {}


def getMeasurements(p, u, energy):
    ntries = 75
    tus = []
    for i in range(ntries):
        utmp = u * 2 + i
        if utmp not in TIMINGS:
            tu, _, energy = getSig(p, utmp, energy)
            TIMINGS[utmp] = tu
        tus.append(TIMINGS[utmp])
    return tus, energy


def counterInterval(p, u2, u1, thresh, energy):
    tu1s, energy = getMeasurements(p, u1, energy)
    tu2s, energy = getMeasurements(p, u2, energy)

    ds = [tu2s[i] - tu1s[j] for i, j in itertools.product(range(len(tu2s)), range(len(tu1s)))]

    cnt = sum(1 if d < thresh else -1 for d in ds)
    return cnt, energy


def confirmIntervalLow(p, u3, u2, u1, thresh, factor, energy):
    NTRIES = 16
    # NTRIES = 8
    NSTEP = 2 ** 96
    NSTEP = 1
    while factor < 4:
        tu1s, tu2s, tu3s = [], [], []
        for i in range(NTRIES * factor):
            tu1, _, energy = getSig(p, u1 * 2 + i * NSTEP, energy)
            tu2, _, energy = getSig(p, u2 * 2 - i * NSTEP, energy)
            tu3, _, energy = getSig(p, u3 * 2 + (NTRIES // 2) - i * NSTEP, energy)
            tu1s.append(tu1)
            tu2s.append(tu2)
            tu3s.append(tu3)

        dsHi = [tu2s[i] - tu3s[j] for i, j in itertools.product(range(NTRIES * factor), range(NTRIES * factor))]
        dsLo = [tu3s[i] - tu1s[j] for i, j in itertools.product(range(NTRIES * factor), range(NTRIES * factor))]

        cntHi = sum(1 if d < thresh else -1 for d in dsHi)
        cntLo = sum(1 if d < thresh else -1 for d in dsLo)
        print(f'cntLo = {cntLo}, cntHi = {cntHi} --> {cntLo > cntHi}')
        if cntLo < 0 and cntHi < 0:
            factor += 1
        else:
            break
    tmp = []
    tmp.extend(dsLo)
    tmp.extend(dsHi)
    thresh = statistics.median(tmp)
    cntHi = sum(1 if d < thresh else -1 for d in dsHi)
    cntLo = sum(1 if d < thresh else -1 for d in dsLo)
    print(f'cntLo = {cntLo}, cntHi = {cntHi} --> {cntLo > cntHi}')
    print(f'{thresh}')
    return (True, energy) if cntLo > cntHi else (False, energy)


def part2(p, u2, u1, thresh, energy):
    # confirmed, tu2, tu1, energy = confirmInterval(p, u2, u1, thresh, energy)
    while energy >= 1_000_000_000 or (u2 - u1) < 2 ** 32:
        u3 = findBisect(u1, u2)
        print(f'energy = {energy:12d}, u1 = {u1:100x}')
        print(f'                       u3 = {u3:100x}')
        print(f'                       u2 = {u2:100x}')

        counter, energy = counterInterval(p, u2, u1, thresh, energy)
        counter_low, energy = counterInterval(p, u3, u1, thresh, energy)
        counter_hi, energy = counterInterval(p, u2, u3, thresh, energy)
        print(f'counter = {counter}, cntLo = {counter_low}, cntHi = {counter_hi} --> {counter_low > counter_hi}')
        print(f'{thresh}')
        if counter_hi < 0 and counter_low < 0:
            u23 = findBisect(u2, u3)
            u13 = findBisect(u3, u1)
            counter_mid, energy = counterInterval(p, u23, u13, thresh, energy)
            print(f'counter_mid = {counter_mid}')
            if counter_mid > 0:
                u2 = u23
                u1 = u13
            else:
                print('took a wrong turn...')
                return -1, -1, energy
        elif counter_low > counter_hi:
            u2 = u3
        else:
            u1 = u3

    return u2, u1, energy


def part2b(p, prime, thresh, energy):
    res = prime
    while energy >= 600_000_000 and prime < 2 ** NBITS:
        u1 = prime << 8
        u2 = u1 + 0xff
        u3 = findBisect(u1, u2)
        print(f'energy = {energy:12d}, u1 = {u1:100x}')
        print(f'                       u3 = {u3:100x}')
        print(f'                       u2 = {u2:100x}')
        confirmed_lo, energy = confirmIntervalLow(p, u3, u2, u1, thresh, 1, energy)
        if confirmed_lo:
            energy, u1_new = part2b(p, prime << 1, thresh, energy)
            if u1_new < 0:
                return part2b(p, (prime << 1) + 1, thresh, energy)
        else:
            energy, u1_new = part2b(p, (prime << 1) + 1, thresh, energy)
            if u1_new < 0:
                return part2b(p, prime << 1, thresh, energy)
        res = u1_new
    return energy, res


def getStats(p, u1, u2, energy):
    NTRIES = 16
    tu1s, tu2s = [], []
    for i in range(NTRIES):
        tu1p, _, energy = getSig(p, u1 + i, energy)
        tu2p, _, energy = getSig(p, u2 - i, energy)
        tu1s.append(tu1p)
        tu2s.append(tu2p)
    ds = [tu2s[i] - tu1s[j] for i, j in itertools.product(range(NTRIES), range(NTRIES))]

    ds = sorted(ds)
    print(f'delta range for {NTRIES}: {min(ds)}..{max(ds)}')
    print(f'mean                    : {statistics.mean(ds)}')
    print(f'variance                : {statistics.variance(ds)}')
    print(f'limits                  : {ds[-16]}, {ds[16]}')

    return ds[-64], energy


def findPrime(u, n, prime):
    for i in range(1000):
        p = math.gcd(u + i, n)
        if p > 2 ** 10:
            pstr = hex(p)
            prstr = hex(prime)
            ok = all(pstr[i] == prstr[i] for i in range(len(prstr)))
            if ok:
                print(pstr)
                return p


def getU1U2(prime):
    bits = NBITS
    pl = f'{prime - 1:x}'
    ph = f'{prime + 1:x}'
    pb = len(ph) * 4
    print(f'prime: {prime:x}')
    print(f'pb: {pb}, bits: {bits}')
    print(f'missing bits: {bits - pb}')
    lo = 'f' * ((bits - pb) // 4)
    hi = '0' * ((bits - pb) // 4)
    u1 = int(pl + lo, 16)
    u2 = int(ph + hi, 16)
    # step = (int(hi,16)+1) // 256
    # u2 = int(f'{prime+1:x}'+lo, 16)
    print(f'u1 = {u1:x}')
    print(f'u2 = {u2:x}')
    return u1, u2


def getBaseline(p, energy):
    baseline, sig, energy = getSig(p, 0, energy)
    return baseline, energy


def decode(ip, port):
    p = pwn.remote(ip, port)
    n, e, prime, energy = getNEP(p)
    R_inv = pow(R, -1, n)
    print(R * R_inv % n)
    # import binascii
    # determine the baseline for energy needed: call for u=0
    baseline, energy = getBaseline(p, energy)
    baseline, energy = getBaseline(p, energy)
    print(f'baseline is {baseline}, new energy {energy}')
    # u1, tu1, u2, tu2, energy = part1a(p, prime, energy, baseline)
    # if False:
    #     u21, u11, tu2, tu1, energy = part1(p, 2**560, 2**7, energy, baseline) #n, e)
    # u1, u2 = getU1U2(prime // 256)
    u1, u2 = getU1U2(prime)
    thresh, energy = getStats(p, u1, u2, energy)
    # energy, u1 = part2a(p, prime // 256, n, 0, R_inv, energy, baseline)
    thresh = -1600
    u2, u1, energy = part2(p, u2, u1, thresh, energy)
    # energy, u1 = part2b(p, prime, thresh, energy)
    # findPrime(u1, n, prime)
    print(f'n: {n:x}')
    print(f'e: {e:x}')
    print(f'prime: {prime:072x}')
    print(f'u1: {u1:x}')

    # u2, u1, tu2, tu1 = part2(p, u2, u1, energy, baseline)
    p.recvuntil(b' [yN]')
    p.sendline(b'n')
    print(p.recvuntil(b':'))
    flag = p.recvline().decode('ascii').strip()
    print(f'flag = {flag}')
    p.close()
    with open('input_1.sage', 'w') as outF:
        outF.write(f'n = 0x{n:x}\n')
        outF.write(f'u1 = 0x{u1:x}\n')
        outF.write(f'flag = 0x{flag}\n')
    # if isPeak or tu1 >0.040:


if __name__ == '__main__':
    decode('152.96.7.9', '5825')
    # print(f'here is your flag: {flag}')
