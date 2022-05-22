import re
pattern = re.compile('^he2021\\{([dlsz134]){9}\\}$')

def hizzle(s):
    s1 = 13
    s2 = 37
    for n in range(len(s)):
        s1 = (s1 + ord(s[n])) % 65521
        s2 = (s1 * s2) % 65521
    return (s2 << 16) | s1

def smizzle (a,b):
    return format(a, 'x') + format(b, 'x')

# print('-------------------------------------')
# print('      o                  o           ')
# print('      | o      o         |           ')
# print('    o-O   o--o   o-o o-o | o-o o-o   ')
# print("   |  | | |  | |  /   /  | |-' |     ")
# print('    o-o | o--O | o-o o-o o o-o o     ')
# print('             |                       ')
# print('         o--o                        ')
# print('-------------------------------------')
# s = input('enter flag:')
# res = pattern.match(s)
# if res:
#     print('digizzling...')
#     a = hizzle(s)
#     b = hizzle(s[::-1])

#     print(smizzle(a,b))

# else:
#     print('wrong format!')

alph = 'dlsz134'

for c1 in alph:
    for c2 in alph:
        print(c2)
        for c3 in alph:
            for c4 in alph:
                for c5 in alph:
                    for c6 in alph:
                        for c7 in alph:
                            for c8 in alph:
                                for c9 in alph:
                                    s = 'he2021{' + c1 + c2 + c3+ c4 + c5 + c6+ c7 + c8 + c9 + '}'
                                    a = hizzle(s)
                                    if a == 0xc5ab05ca:
                                        b = hizzle(s[::-1])
                                        if b == 0x73f205ca:
                                            print(s)
                                            print(smizzle(a,b))
                                            sys.exit(0)
                                    
