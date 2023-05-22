msg = """
🥦🥝🍋🍊🥭🍌🫑🧅 🧅🥝🥖 🍉🍠🥬🫐 🍉🫐🥔🥥🍈 🥔🍌🥝🥖
🍏 🥐🍍🥦🍉🍇🥥🍋 🥑🍉🍍🥐🍉 🍅🍠🥦 🍋🥭🍓🍐🌶🍇 🥕
🌶🥔🥭🍓🍏🍒🍆🍏 🌶🫐🍎🍏🍒🥥🍊 🍎🥝 🍅🥝🥥🍇 🍎🍉🥔
🍓 🥝🍓🍇 🥐🥭🥦🍉🍇🥥🍏🫐🍆🍎 🌶🫐🍎🍏🍇🥥🍋 🍎🍉🍇
🍊🫐 🍠🥥🍒 🥐🍠🌶🫑🫐🍈 🍉🥝🍅🥝🥦🍉🥝🍓🍍🥐 🥐🍍🥕
🍉🫐🥥🍋 🍏🍉🍇 🍋🥝🫑🥖🍏🍍🥝🍓 🥭🍋 🍉🧅🥦🍒🥥🥬🥭
🍏🍠🍅🥭🍓🥝🍋🥭🍊
"""

msg = msg.replace('\n','').replace('🍏','🍎')
d = set(msg)
print(len(d))
print(d)

hist = {}
for c in msg:
    if c in hist:
        hist[c] += 1
    else:
        hist[c] = 1

print(hist)

ch = 0x41
subst = {}
for key in hist:
    if key == ' ':
        subst[key] = key
    else:
        subst[key] = chr(ch)
        ch += 1
        if ch >= 0x41 + 26:
            ch = 0x31

print(subst)

msg2 = ''.join(subst[c] for c in msg)
print(msg2)

hist = {}
for c in msg2:
    if c in hist:
        hist[c] += 1
    else:
        hist[c] = 1

print(hist)

subst2 = {'Q': 't', 'B': 'o',   # to
          'E': 'i', 'C': 's',
          'J': 'h', 'T': 'e',
          'V': 'm', 'O': 'r',
          'K': 'a', 'A': 'p',
          'W': 'n', 'N': 'a',
          'D': 's', 'M': 'e',
          'S': 'i', 'G': 'l', 'I': 'u',
          'H': 'y', 'F': 'b', 'L': 'v', 'P': 'd', 'R': 'c', 'U': 'w',
          'Y': 'l', '1': 'e', 
          'Z': 'p', 'X': 'g', '2': 'x'
          }

count = 0
for c in msg2:
    if c in subst2:
        c = subst2[c]
    print(f"{c}", end = '')
    count += 1
    if count>70 and c == ' ':
        count = 0
        print()

print()


