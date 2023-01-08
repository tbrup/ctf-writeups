# import coppersmith
# import sympy
# import gmpy2
# from gmpy2 import mpz
import math


def solve(n, qprime):
    print(math.log(qprime)/math.log(2))

    qbar = qprime
    print(f'qbar = 0x{qbar:x}')

    F.< x > = PolynomialRing(Zmod(n), implementation='NTL')
    pol = x - qbar
    dd = pol.degree()

    # PLAY WITH THOSE:
    beta = 0.5  # we should have q >= N^beta
    epsilon = beta / 7  # <= beta/7
    mm = math.ceil(beta ** 2 / (dd * epsilon))  # optimized
    tt = math.floor(dd * mm * ((1 / beta) - 1))  # optimized
    XX = math.ceil(n ** ((beta ** 2 / dd) - epsilon))  # we should have |diff| < X

    roots = coppersmith_howgrave_univariate(pol, n, beta, mm, tt, XX)
    res = []
    print("\n# Solutions")
    print("we found:", roots)
    ok = False
    for r in roots:
        print(f'{"X" * 80}')
        print(f'root:  {r:x}')
        print(f'qbar:  {qbar:x}')
        if r == qbar or r == -qbar:
            print('root is the same as qbar')
            break
        for f in [-1,1]:
            rbar = r
            q = qbar - f*rbar
            res.append(q)
            p = n // q

            if p * q == n:
                print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                print(f'q = {q:x}')
                print(f'p = {p:x}')
                ok = True
                break
    if ok:
        print(hex(q))
        print(hex(p))
        print(hex(p * q))
        return p, q
    return -1, -1


if __name__ == '__main__':
    n = 0xbd07eca878c684ec1b00456b9ece383843d402c0e4b4625b64bc2e966137ab416771dbe556337175159087a7498ce0f7994b56355d5dcb108d4a02e2e388a7da018ef8941df25d20def4f50536f4a87815e0bd9ba3d96529eb58202a5f90a10b
    e = 0x10001
    u1 = 0xf880547bf47e5bd5441dd97e49ef95e5d4adbfb7229936bf209166fbdb7f25dbae7fffffffffffffffffffffffffffffffff
    flag = 0x7e362852f3d84f250f0ff156739463b4fc0490c87e4e1ed5927f4e074202dbc8d7f09b0cae5dddca6c26e10c9e0bd74a7d0dd5cdf42b08a14d28c6d95dffaca7e9aaef29dcca85e5599f4ef6244e24e752e052c14d893c6ee90fc40b3ce71c0e
    # while math.log(u1)/math.log(2) < 400:
    #     u1 *= 2
    tmp = -1
    while tmp == -1 and math.log(u1)/math.log(2) > 382:
        print(f'{u1:x}')
        tmp, tmq = solve(n, u1)
        u1 //= 2
    if tmp > 0:
        phi = (tmp-1)*(tmq-1)
        d = inverse_mod(0x10001, phi)
        print(f'd * e mod phi = {d*e % phi}')
        msg = int(pow(flag, d, n))
        print(f'msg = {msg}')
        print(f'msg = {msg:x}')
        print(msg % 0x100)
        flg = ''
        while msg>0:
            c = msg % 0x100
            flg += chr(c)
            print(flg)
            msg //= 0x100
        print(flg)
        print(flg[::-1])
