# import c2utils
from hashlib import sha256
from Crypto.Cipher import AES
from base64 import standard_b64decode
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Random.random import randint
from Crypto.Util.Padding import pad, unpad
import subprocess

# def long_to_base64(n):
#     return standard_b64encode(long_to_bytes(n)).decode()

# def encrypt(cipher, msg):
#     return standard_b64encode(cipher.encrypt(pad(msg, 16))).decode()

def base64_to_long(e):
    return bytes_to_long(standard_b64decode(e))

def decrypt(cipher, e):
    return unpad(cipher.decrypt(standard_b64decode(e)), 16)




cipher = None

p = base64_to_long("h3rl/Q==")
g = base64_to_long("Ag==")
A = base64_to_long("QpFOyA==")
B = base64_to_long("Ph6IeA==")

print('p:', p)
print('g:', g)
print('A:', A)
print('B:', B)

for b in range(620620105,p):
    test = pow(g, b, p)
    if b % 10000000 == 0:
        print(b)
    if test == B:
        print('found b: ', b)
        # b = randint(1, p)
        shared = pow(A, b, p)
        shared = sha256(long_to_bytes(shared)).digest()
        cipher = AES.new(shared, AES.MODE_ECB)
        # return {
        #     'B': long_to_base64(pow(g, b, p))
        # }
    
        cmd = decrypt(cipher, "6+lX9noxcSrRAnTbQMYdPg==")
        print(cmd)
        cmd1 = decrypt(cipher, "15AsYtxN//27mQ/lDUAJOjApyeXQx65dFso1oP7w8Qw=")
        print(cmd1)

        ret = decrypt(cipher,"GkSU2VwQyFe5Jt0Vd0cfxw==" )
        print(ret)
        ret1 = decrypt(cipher, "3eWXhpQagWGMlfc71Qxd2QMvy4EVIyLfP54Jm6lpyHot6Qz+U7t3q2DdKnOxZBQf")
 
        print(ret1)
    # return {
        # 'return': encrypt(cipher, subprocess.check_output(cmd))
    # }

# c2utils.start_listener(handle)
