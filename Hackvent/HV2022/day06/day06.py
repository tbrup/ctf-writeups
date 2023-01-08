msg = 0x485632327b436834316e535f6172335f5075626c31437d00000000000000002e          
res = ''
while msg > 0:
    c = msg & 0xFF 
    msg >>= 8
    if c >= 0x20:
        res += chr(c)
        print(chr(c))


print(res[::-1])        
