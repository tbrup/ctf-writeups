#!/usr/bin/env python3

from Crypto.Cipher import AES
from os import urandom
import binascii
import sys
from pwn import *

context.defaults['encoding'] = 'utf-8'

# Remote
IP = '152.96.7.8'
PORT = 1337
CHARS = ['', '0', 'ö', '⓫', '𝄞'] # 0, 1, 2, 3, 4 byte wide characters


def buildHeader(targetLen: int):
    res = ''
    for i in range(4, 0, -1):
        res += (targetLen // i) * CHARS[i]
        targetLen = targetLen % i
    return res


def buildCentre(nChars: int):
    def lenCentre(p):
        res = 0
        for i in range(len(p)):
            res += p[i] * (i + 1)
        return res

    assert (nChars >= 4)
    p = [nChars, 0, 0, 0]
    while lenCentre(p) != 16:
        # print(p)
        if p[2] > 0:
            p[3] += 1;
            p[2] -= 1
        elif p[1] > 0:
            p[2] += 1;
            p[1] -= 1
        else:
            p[1] += 1;
            p[0] -= 1
    return p[1] * CHARS[1] + p[2] * CHARS[2] + p[3] * CHARS[3] + p[0] * CHARS[0]


# build a payload in UTF-8 that when expanded into bytes gives a payload of 47
# bytes.  The first 15 bytes and the last 15 bytes must be the same.

def buildPayload(s):
    headerLen = 32 - len(s)
    header = buildHeader(headerLen)
    nCharsAssigned = 2 * len(header) + len(s)
    # print(f'number of character for header and tail: {nCharsAssigned}')
    # print('find number of padding blocks')
    # sys.exit(-1)
    found = False
    index = (nCharsAssigned // 16) + 1
    centre = ''
    nCentrePackets = 0
    while not found:
        goal = index * 16  # + 15
        if goal - 4 < nCharsAssigned:
            print('not enough character to fill, increase index')
            index += 1
        else:
            toFill = goal - nCharsAssigned
            found = True
            if toFill % 16 < 4:
                centre += buildCentre(4)
                toFill -= 4
            while toFill > 0:
                nCentrePackets += 1
                if toFill > 16:
                    centre += buildCentre(16)
                    toFill -= 16
                else:
                    centre += buildCentre(toFill)
                    toFill = 0

    payload = header + s + centre + header
    # print((header+s).encode(), len(header+s))
    # print(centre.encode(),len(centre))
    # print((header).encode(),len(header))
    assert (len(payload) % 16 == 0)
    return payload, nCentrePackets


def printPackets(s):
    for i in range(0, len(s), 16):
        print(s[i:i + 16])


# pad block size to 16, zfill() fills on left. Invert the string to fill on right, then invert back.
def pad(msg):
    if len(msg) % 16 != 0:
        msg = msg[::-1].zfill(len(msg) - len(msg) % 16 + 16)[::-1]
    # print(msg)
    return msg


flag = open('flag.txt').read().strip()


def encode(msg):
    aes = AES.new(urandom(16), AES.MODE_ECB)
    enc = pad(msg) + pad(flag)
    enc = aes.encrypt(pad(enc.encode()))
    return enc.hex()


def testChar(s, p):
    msg, index = buildPayload(s)
    pkt = encode(msg)
    p.recvline(b'Enter access code:')
    p.sendline(msg)
    pkt = p.recvline()
    # print(pkt)
    return (
        pkt[(16 + (index + 2) * 16) * 2 : (32 + (index + 2) * 16) * 2]
        == pkt[32:64]
    )


def decode(ip, port):
    myFlag = ''
    while True:
        p = remote(ip, port)
        for i in range(33, 127):
            tst = myFlag + chr(i)
            if testChar(tst, p):
                myFlag += chr(i)
                print(f'myFlag = {myFlag}, lastChr = {myFlag[-1]}')
                break
            p.recvline()
            # print(p.recvline())
            p.sendline(b'y')
        p.close()
        if myFlag[-1] == '}':
            return myFlag


if __name__ == '__main__':
    flag = decode('152.96.7.11', '1337')
    print(f'here is your flag: {flag}')
