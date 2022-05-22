
a = set({7, 3, 2})
b =   [7, 8, a, 4, 5, 3, 5, 1, 3, 0, 3, 4, 5, 5]

tmp = [1, 6, a, 9, 4, 5, 3, 4, 8, 9, 1, a, 3, 3]

s = [1, 6, 7, 3, 2, 9, 4, 5, 3, 4, 8, 9, 1, 7, 3, 2, 3, 3, 7, 8, 7, 3, 2, 4, 5, 3, 5, 1, 3, 0, 3, 4, 5, 5]
cipher = "ik934:\u007fnvr|h2>biu37~\u0080bdeg|D~"
sol = ''

for i in range(len(cipher)):
    t = ord(cipher[i]) - s[i]
    print(ord(cipher[i]), s[i], t) 
    sol += chr(t)
    print(sol)

