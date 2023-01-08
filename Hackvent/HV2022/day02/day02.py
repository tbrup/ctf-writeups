
key = ["bae", "faced", "a", "bad", "deed"]
res = ''
for w in key:
    print(f'{w}: {int(w,16)}')
    res += f'{int(w, 16)} '

print(res)

res = int(''.join(key), 16)
print(res)
