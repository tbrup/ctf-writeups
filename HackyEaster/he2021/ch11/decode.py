with open('text.txt', 'r') as inF:
    data = inF.read()
    charW = 16
    charH = 5
    off = charW * charH
    for i in range(len(data)//charW):
        print(i, data[i*charW:(i+1)*charW])

    for j in range(charH):
        for i in range(len(data)//(charW*charH)):
            print(data[j*off + i*charW:j*off + (i+1)*charW], end='')
        print()

    print(data[:16],   data[80:96],   data[160:176], data[240:256])
    print(data[16:32], data[96:112],  data[176:192], data[256:272])
    print(data[32:48], data[112:128], data[192:208], data[272:288])
    print(data[48:64], data[128:144], data[208:224], data[288:304])
    print(data[64:80], data[144:160], data[224:240], data[304:320])


print('he2021{☐☐0☐☐☐☐☐☐☐☐☐☐☐0☐☐☐3☐☐☐☐☐5☐}')
print('he2021{Wh0_is_scared_0f_h3xdump5?}')
