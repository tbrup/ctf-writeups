# import argparse
from pwn import *
# context.terminal = ['tmux', 'splitw', '-h']
context.defaults['encoding'] = 'utf-8'
# cmdline argument - how to connect to binary
# parser = argparse.ArgumentParser()
# parser.add_argument("--local", help="Run exploit locally", action="store_true")
# parser.add_argument("--attach", help="Run exploit locally and attach debugger", action="store_true")
# parser.add_argument("--remote", help="Run exploit on remote service", action="store_true")
# parser.add_argument("--ssh", help="Run exploit on SSH server", action="store_true")
# args = parser.parse_args()

# Remote
IP = '46.101.107.117'
PORT = 2207


def packet(n, flag_len):
    raw = 2*16 + n * flag_len
    padded = raw + (16 - (raw % 16)) % 16
    return padded

def patties(flag_len, offset):
    for n in range(1,25):
        if (n*flag_len)%16 == offset%16:
            return n
    print(f'[x] cannot find number of patties')
    exit(-1)


p = remote(IP, PORT)

bun = b'1'*16
flag_len = 35
flag = ''

for j in range(1,flag_len+1):
    n = patties(flag_len, j)
    print(f'[ ] need {n} patties for char {j}')

    for i in range(33,127):
        bun = chr(i) + flag
        if len(bun) < 16:
            bun += (16-j)*'a'
        else:
            bun = bun[:16]
        bun = bun[::-1]
        if i == 33:
            print(i, (chr(i) + flag + bun)[:16], flag, bun[:16])
        assert(len(bun) == 16)
        assert(bun[::-1] == (chr(i) + flag + bun)[:16])
        bun = bun.encode()
        p.recvuntil(b'How many patties: ')
        p.sendline(bytes(str(n), encoding='ASCII'))

        p.recvuntil(b'Which bun? ')
        p.sendline(bun)
        p.recvuntil(b"Heres your order, enjoy!\n")
        burger = p.recvuntil(b'\n')
        cnub = burger[:32]
        shift = ((j-1)//16)*32
        cbunf = burger[-65-shift:-33-shift]
        # if chr(i) == '}':
        #     print(burger)
        #     print(cnub)
        #     print(cbunf)
        assert(len(cnub) == len(cbunf))
        if cnub == cbunf:
            flag = chr(i) + flag
            print(f'[+] found {j}th character ', chr(i), ' flag: ', flag)
            break
p.close()

