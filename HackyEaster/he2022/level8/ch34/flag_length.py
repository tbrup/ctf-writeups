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

p = remote(IP, PORT)

bun = b'1'*16
crypt = {}
for i in range(24):
    p.recvuntil(b'How many patties: ')
    p.sendline(str(i+1))

    p.recvuntil(b'Which bun? ')
    p.sendline(bun)
    p.recvuntil(b"Heres your order, enjoy!\n")
    burger = p.recvuntil(b'\n')
    crypt[i] = (len(burger) - 1) // 2

p.close()
print(crypt)

for flag_len in range(9, 36):
    ok = True
    for n in range(24):
        if crypt[n] != packet(n+1, flag_len):
            ok = False
            break

    if ok:
        print('[+] flag length: ', flag_len)
        break

