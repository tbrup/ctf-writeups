from PIL import Image
import re

def stipple(r, g, b, shiftr = 0, shiftg = 0):
    res = ''
    for i in range(len(r)):
        res += str(r[(i+shiftr)%len(r)] % 2)
        res += str(g[(i+shiftg)%len(r)] % 2)
        res += str(b[(i)%len(r)] % 2)
    resBin = []
    for i in range(0,len(res),8):
        resBin.append(int(res[i:i+8],2))
    return resBin

def bands(fn):
    with Image.open(fn) as im:
        (sx,sy) = im.size
        r, g, b = [], [], []

        for y in range(sy):
            for x in range(sx):
                (rp, gp, bp, ap) = im.getpixel((x,y))
                r.append(rp%2)
                g.append(gp%2)
                b.append(bp%2)
    return (r,g,b)


# (r,g,b) = bands('jupiter-one.png')
(r,g,b) = bands('jupiter-two.png')
print(r[80:160])
print(g[80:160])
print(b[80:160])

print(bin(0x68))

# res = stipple(r, g, b, 0)
        
        
    
def shiftImage(fn):
    with Image.open(fn) as im:
        (sx,sy) = im.size
        for shift in range(1,40):
            newFn = 'shift%d.png' % shift
            imNew = Image.new('RGBA', im.size)
            for y in range(sy):
                for x in range(sx):
                    (r1, g1, b1, a1) = im.getpixel((x,y))
                    (r2, g2, b2, a2) = im.getpixel(((x+shift)%sx,y))
                    imNew.putpixel((x,y),(r2,g1,b1,a1))
            imNew.save(newFn)

# shiftImage('jupiter-two.png')

# for shiftr in range(-30,31):
#     for shiftg in range(-30,31):
#         res = stipple(r, g, b, shiftr, shiftg)
#         tmp = ''
#         for x in res:
#             tmp += chr(x)

#         if 'he2022' in tmp:
#             print('found flag for shift = ', shiftr, shiftg)
#             for x in res[:10]:
#                 print(hex(x),end='')
#             print()
#             for x in res[:10]:
#                 print(chr(x),end='')
#             print()

def extract_binary(fn):
    res = ''
    with open(fn, 'r') as inF:
        for l in inF.readlines():
            tmp = int(l[:-1], 16)
            res +=  format(tmp, '0128b')

    return res

def find_crib(s):
    crib = ''.join(format(ord(i), '08b') for i in 'he2022{')
    print(crib)
    print(len(crib), len('he2022{')*8)
    bits = []
    for c in range(2):
        crib2 = ''
        for i in range(len(crib)):
            if i % 2 == c:
                if c == 0:
                    if crib[i] == '1':
                        crib2 += '1'
                    else:
                        crib2 += '0'
                else:    
                    crib2 += crib[i]
            else:
                crib2 += '.'
        crib2 += 20*8*'.'
        print(crib2)
        cribRe = re.compile(crib2)
        g = cribRe.findall(s)
        if len(g)>0:
            print(g)
            bits.append(g)
        else:
            bits.append(['0'*len(crib2)])
    return bits

def stipple(s1, s2):
    res = ''
    for i in range(len(s1)):
        res += s1[i] + s2[i]
    # print(res)
    for b in range(0,len(res),8):
        tmp = res[b:b+8]
        print(chr(int(tmp,2)), end='')
    print()


# bin = extract_binary('hex_dump_lsb_row.txt')
# bits = find_crib(bin)
# print(bits)

# r = bits[0][0]
# bin = extract_binary('hex_dump_lsb.txt')
# bits = find_crib(bin)
# g = bits[1][0]
# b = bits[2][0]
# stipple([r,g,b])

def single_colour(fn):
    bits = []
    with open(fn, 'rb') as inB:
        bBin = inB.read()
        blue=''
        for b in bBin:
            blue += format(b, f'08b')
        
        # print(blue)   
        crib = ''.join(format(ord(i), '08b') for i in 'he2022{')
        for i in range(2):
            crib2 = ''
            for j in range(len(crib)):
                if j%2 == i:
                    crib2 += crib[j]

            crib2 += 20*8*'.'
            cribRe = re.compile(crib2)
            g = cribRe.findall(blue)
            if len(g)>0:
                print(g)
                bits.append(g)
    return bits


r = single_colour('lsb_r_by_row.bin')
g = single_colour('lsb_g_by_row.bin')
b = single_colour('lsb_b_by_row.bin')
print('r', r)
print('g', g)
print('b', b)

stipple(r[0][0], b[0][0])
