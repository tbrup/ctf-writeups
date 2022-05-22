msg= '68 65 32 30 32 32 7b 74 68 31 73 5f 30 6e 33 5f 31 73 5f 72 33 33 33 33 6c 79 5f 73 31 6d 70 6c 33 7d'

res = ''
for n in msg.split(' '):
    res += chr(int(n,16))

print(res)
