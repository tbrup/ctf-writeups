def maschadar(code, invert = False):
    input = 'abcdefghijklmnopqrstuvwxyz01'
    outpt = 'ghbcanopqrstuvwxyz01defijklm'

    map = {}
    for c in input:
        i = input.index(c)
        j = outpt.index(c)
        if invert:
            map[j] = i
        else:
            map[i] = j

    res = list(' ' * len(input))
    for i in range(len(code)):
        res[map[i]] = code[i]
    return ''.join(res)


def remplazzar(code, invert=False):
    s = list(code)
    for rdx in range(len(s)):
        rdx_1 = (-0x3333333333333333 * rdx) >>0x40
        r9 = ((((rdx >> 0x3f) + rdx) >> 1) << 1)
        r8 = ((rdx - r9) + (rdx - (((rdx + rdx_1) >> 2) * 5)))
        # print(rdx, r9, r8)
        if invert:
            s[rdx] = chr(ord(s[rdx]) - r8)
        else:
            s[rdx] = chr(ord(s[rdx]) + r8)
    return ''.join(s)


def verifitgar(code, scrambled):
    var_48 = "aug{"
    var_38 = "mepdpeuv"
    var_28 = "isvohxhqjx"
    var_18 = "fhr"

    rax_1 = var_48 + 'l' + var_38 + 'l' + var_28 + 'l' + var_18
    if scrambled != rax_1:
        print("Sorry, no.")
    else:
        print("Congrats, the flag is: he2022{" + code + '}')

def remplazzar2(code, invert = False):
    input  = 'ghbcanopqrstuvwxyz01defijklm'
    output = 'gjdgeopstwsvwz{yz}36dghmnlmp'

    diff = []
    for i in range(len(input)):
        diff.append(ord(input[i]) - ord(output[i]))

    res = ''
    for i in range(len(code)):
        if invert:
            res += chr(ord(code[i]) + diff[i])
        else:
            res += chr(ord(code[i]) - diff[i])
    
    return res

if __name__ == '__main__':
    target = 'aug{lmepdpeuvlisvohxhqjxlfhr'
    tmp = remplazzar2(target, True)
    print(tmp)
    code = maschadar(tmp, True)
    print(code)
    verifitgar(code, remplazzar2(maschadar(code)))
