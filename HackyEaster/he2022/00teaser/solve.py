msg = 'a4a9fefcfefeb7b8fff8bfa9bee1a8fca2ffedb1'
res = ''
for i in range(len(msg)//2):
    s = int(msg[2*i:2*i+2],16)
    c = s ^ 0xcc
    res += chr(c)
    print(f'{s} -> {c} %s'%chr(c)) 
print(res)
