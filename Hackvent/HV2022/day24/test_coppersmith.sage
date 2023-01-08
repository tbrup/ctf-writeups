# import coppersmith
# import sympy
# import gmpy2
# from gmpy2 import mpz
import time
import math

def test_example1():
    ############################################
    # Test on Stereotyped Messages
    ##########################################

    print("//////////////////////////////////")
    print("// TEST 1")
    print("////////////////////////////////")

    # RSA gen options (for the demo)
    length_N = 1024  # size of the modulus
    Kbits = 200      # size of the root
    e = 3

    # RSA gen (for the demo)
    p = next_prime(2^int(round(length_N/2)))
    q = next_prime(p)
    N = p*q
    ZmodN = Zmod(N);

    # Create problem (for the demo)
    K = ZZ.random_element(0, 2^Kbits)
    Kdigits = K.digits(2)
    M = [0]*Kbits + [1]*(length_N-Kbits);
    for i in range(len(Kdigits)):
        M[i] = Kdigits[i]
    M = ZZ(M, 2)
    C = ZmodN(M)^e

    # Problem to equation (default)
    P.<x> = PolynomialRing(ZmodN) #, implementation='NTL')
    pol = (2^length_N - 2^Kbits + x)^e - C
    dd = pol.degree()

    # Tweak those
    beta = 1                                # b = N
    epsilon = beta / 7                      # <= beta / 7
    mm = ceil(beta**2 / (dd * epsilon))     # optimized value
    tt = floor(dd * mm * ((1/beta) - 1))    # optimized value
    XX = ceil(N**((beta**2/dd) - epsilon))  # optimized value

    # Coppersmith
    start_time = time.time()
    roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)

    # output
    print("\n# Solutions")
    print("we want to find:",str(K))
    print("we found:", str(roots))
    print(("in: %s seconds " % (time.time() - start_time)))
    print("\n")


def test_example2():
    print("//////////////////////////////////")
    print("// TEST 2")
    print("////////////////////////////////")
    #
    # RSA gen
    length_N = 1024
    length_N = 768
    p = next_prime(2^int(round(length_N/2)))
    q = next_prime(round(pi.n()*p) )
    N = p*q

    # qbar is q + [hidden_size_random]
    hidden = 120
    diff = ZZ.random_element(0, 2^hidden-1)
    diff = -(q % (2^hidden))
    qbar = q*4 + diff
    print(f'qbar = {qbar:x}')
    print(f'q    = {q:x}')
    print(f'p    = {p:x}')

    F.<x> = PolynomialRing(Zmod(N), implementation='NTL')
    pol = x - qbar
    dd = pol.degree()

    # PLAY WITH THOSE:
    beta = 0.5                             # we should have q >= N^beta
    epsilon = beta / 7                     # <= beta/7
    mm = math.ceil(beta**2 / (dd * epsilon))    # optimized
    tt = math.floor(dd * mm * ((1/beta) - 1))   # optimized
    XX = math.ceil(N**((beta**2/dd) - epsilon)) # we should have |diff| < X

    # Coppersmith
    start_time = time.time()
    roots = coppersmith_howgrave_univariate(pol, N, beta, mm, tt, XX)

    # output
    print("\n# Solutions")
    print("we want to find:", qbar - q)
    print("we found:", roots)
    found = False
    for r in roots:
        print(f'r            = {r:x}')
        print(f'r / (qbar-q) = {1.0*(r / (qbar-q))}')
        print(f'r       = {r:x}')
        for f in [-1, 1]:
            print(f'difference between q and qbar+{f}*root: {q - qbar - f*r}')
            found = found or ((q - qbar - f*r) == 0)
            qNeu = qbar + f * r
            if qNeu != 0:
                p = N // qNeu
                if p*q == N:
                    print(f'qbar + {f} * r is a factor of n')
    assert found
    print(("in: %s seconds " % (time.time() - start_time)))

if __name__ == '__main__':
    test_example1()
    test_example2()
