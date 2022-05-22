from Crypto.Util.number import getPrime, long_to_bytes
import math
# from secrets import FLAG

# assert FLAG.startswith("he2022")

# p = getPrime(512)
# q = getPrime(512)
e = 65537
crib = 'he2022'
# n = p * q

with open('output','r') as inF:
    s = inF.read()[1:-2]
    crypt = [int(x) for x in s.split(', ')]

print(crypt[0])    

def multi_n(c, cr):
    tmp = pow(ord(c), e)
    return (tmp - cr)

   
n = math.gcd(multi_n(crib[0], crypt[0]),
            multi_n(crib[1], crypt[1]))

print(n)

rainbow = {}
for i in range(32,128):
    rainbow[pow(i,e,n)] = chr(i)

res = ''
for i in crypt:
    res += rainbow[i]

print(res)
# def encrypt(content):
#     ct = []
#     for c in content:
#         ct.append(pow(ord(c), e, n))
#     return ct

# print(encrypt(FLAG))
