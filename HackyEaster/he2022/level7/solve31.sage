from random import randint
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad
from socket import *
from telnetlib import Telnet
import base64

class RNG:
    def __init__(self, r = None):
        p = 115792089210356248762697446949407573530086143415290314195533631308867097853951
        p = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
        b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
        self.curve = EllipticCurve(GF(p), [-3,b])

        self.P = self.curve.lift_x(15957832354939571418537618117378383777560216674381177964707415375932803624163)
		# 2347D02339CE6B6F40EBADF8D7968F7685F0E8A74E7AA53586393D157FADACE3
        self.Q = self.curve.lift_x(66579344068745538488594410918533596972988648549966873409328261501470196728491)
		# 933292C549062B6CD9F2682336B60C4A74286AEAF9B627BF2211661B7E1182AB
        if r == None:    
            self.state = randint(1, 2**256)
        else:
            self.state = r
        
    def next(self):
        r = (self.state * self.P)[0].lift()
        self.state = (r * self.P)[0].lift()
        return (r * self.Q)[0].lift() >> 8

class Casino:
    def __init__(self, rng):
        self.rng = rng
        self.balance = 10

    def play(self):
        print("Your bet: ", end='')
        bet = input()
        if (bet in ["0", "1"]):
            bet = Integer(bet)
            if (self.rng.next() % 2 == bet):
                self.balance += 1
            else:
                self.balance -= 1
                if (self.balance == 0):
                    print("You are broke... play again")
                    exit()
            print(f"Your current balance: {self.balance}")
        else:
            print("Invalid bet option, use either 0 or 1")
            
    def buy_flag(self):
        if (self.balance >= 1337):
            print('you can buy the flag')
        else:
            print("No flag for the poor. Gamble more")

def build_candidates(r):
    rng = RNG()
    e = 1337
    candidates = []
    for i in range(256):
        try:
            qr = rng.curve.lift_x(r + i)
            pr = (qr*e)[0].lift()
            candidates.append(RNG(pr))
        except ValueError:
            pass
            # print(f'no point for {i}')

    return candidates

def purge(rngs, bit):
    retVal = []
    for r in rngs:
        if r.next() % 2 == bit:
            retVal.append(r)
    return retVal

def play(io, bit, money):
    io.read_until(b'> ')
    io.write(b'p\n')
    io.write(str(bit).encode('ascii')+b'\n')
    
    io.read_until(b'balance: ')
    m = int(io.read_until(b'\n'))
    if m > money:
        return bit, m
    else:
        if bit == 1:
            return 0, m
        else:
            return 1, m

def buy_flag(io, rng):
    io.read_until(b'> ')
    io.write(b'b\n')
    flag_enc = io.read_until(b'\n')[:-1].decode('ascii')
    print(flag_enc)
    key = SHA256.new(str(rng.next()).encode('ascii')).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    flag = cipher.decrypt(bytes.fromhex(flag_enc))
    print("here is your flag!")
    if ord(flag[-1:]) < 16:
        flag = flag[:-ord(flag[-1:])]
    print(f'{flag}')


def main():
    rng = RNG()
    
    for i in range(1336,100000):
        Q1 = i * rng.P
        if Q1 == rng.Q:
            print(i, ' solves Q = n*P')
            break
        if rng.P == i*rng.Q:
            print(i, ' solves P = n*Q')
            e = i
            # d = inverse_mod(i, rng.curve.order())
            # if rng.Q == d*rng.P:
            #     print(d, ' solves Q = n*P')
            # tmp = rng.curve.lift_x(rng.next())
            # print(tmp)
            # print((e*tmp)[0].lift())
            # print(rng.state)
            break

    # casino = Casino(rng)
    r = rng.next() * 256
    candidates = build_candidates(r)

    while len(candidates) > 1:
        print(len(candidates))
        bit = rng.next() % 2
        candidates = purge(candidates, bit)

    print('now the state is known')
    print(rng.state)
    print(candidates[0].state)
    # print("Welcome to the Casino")
    # print(f"Your id is {rng.next()}")
    # print("What would you like to do?")
    # print("(p)lay and win some money")
    # print("(b)uy the flag")

    # while (True):
    #     print("> ", end='')
    #     option = input()

    #     if (not option in ["b", "p"]):
    #         print("Unknown option, use 'b' or 'p'")
    #     elif (option == "b"):
    #         casino.buy_flag()
    #     elif (option == "p"):
    #         casino.play()

def solve():
    # io = Telnet()
    with Telnet("46.101.107.117","2212") as io:
        io.read_until(b'Your id is')
        r = Integer(io.read_until(b'\n')) * 256
        candidates = build_candidates(r)

        money = 10
        while len(candidates) > 1:
            print(len(candidates))
            bit, money = play(io, 1, money)
            candidates = purge(candidates, bit)

        print('now the state is known')

        rng = candidates[0]
        while money < 1337:
            bit = rng.next() % 2
            bit2, money = play(io, bit, money)
            assert(bit == bit2)
            if money % 100 == 0:
                print(money)
        print(money)
        buy_flag(io, rng)


def test_decrypt():
    rng = RNG()
    flag_enc = 'c245b43c1e7bbec5de4a56802a79818139e6ea794e660959dd457ea7630dd7fc'
    flag = 'he2022{test}'
    key = SHA256.new(str(rng.next()).encode('ascii')).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    flag_enc = cipher.encrypt(pad(flag.encode('ascii'), 16)).hex()
    print(flag_enc)
    flag = cipher.decrypt(bytes.fromhex(flag_enc))
    if ord(flag[-1:]) < 16:
        flag = flag[:-ord(flag[-1:])]
    print(flag)

    

if __name__ == '__main__':
    # test_decrypt()
    # main()
    solve()
