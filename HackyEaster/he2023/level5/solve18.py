SHIFT1 = 8
SHIFT2 = 4

msg = 'ip0232j{1t_x_v0z4b3bm__v4xvq}a'

def rotate(c, r):
    tmp = ord(c) + r
    if tmp > ord('z'):
        return chr(tmp-26)
    elif tmp < ord('a'):
        return chr(tmp+26)
    else:
        return chr(tmp)

def encode(s):
    res = ''
    for i in range(0,len(s),2):
        p = s[i:i+2]
        print(p)
        res += rotate(p[1], SHIFT2) if p[1].islower() else p[1]
        res += rotate(p[0], SHIFT1) if p[0].islower() else p[0]
    return res

def decode(s):
    res = ''
    for i in range(0,len(s),2):
        p = s[i:i+2]
        print(p)
        res += rotate(p[1], -SHIFT1) if p[1].islower() else p[1]
        res += rotate(p[0], -SHIFT2) if p[0].islower() else p[0]
    return res


if __name__ == "__main__":
    inp = "he2023{a"
    tmp = encode(inp)
    tmp2 = decode(tmp)

    print(inp)
    print(tmp)
    print(tmp2)
    print(decode(msg))

