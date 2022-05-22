import png
from PIL import Image

def hist(anArr):
    pal = {}
    for i in range(1025*1024):
        c = anArr[i]
        if c in pal:
            pal[c] += 1
        else:
            pal[c] = 1

    return pal


def saveAscii(fn, arr):
    with open(fn, 'w') as outF:
        for rows in range(1024):
            row = ''
            for cols in range(1, 1025):
                row += chr(arr[rows*1025+cols] + 32)
            outF.write(row + '\n')

with open('pic1', 'rb') as firstF:
    arr1 = firstF.read()
    pal1 = hist(arr1)

    # print(pal1)

with open('pic2', 'rb') as firstF:
    arr2 = firstF.read()
    pal2 = hist(arr2)
    # print(pal2)
    saveAscii('pic2.txt', arr2)

with open('twoyolks.png', 'rb') as pngF:
    r = png.Reader(pngF)
    (width, height, rows, info) = r.read()
    print(info)

print('number of colours in palette:', len(info['palette']))
print('colours used in picture 1:')
for k in sorted(pal1.keys()):
    print('key %d: %d' % (k, pal1[k]))
print('colours used in picture 2:')
for k in sorted(pal2.keys()):
    print('key %d: %d' % (k, pal2[k]))


qr = Image.new('1', (1024,1024))
for rows in range(1024):
    for cols in range(1, 1025):
        p = arr2[rows*1025+cols]
        if p == 15:
            qr.putpixel((cols-1, rows), 0)
        else:
            qr.putpixel((cols-1, rows), 1)
qr.save('qr.png')
