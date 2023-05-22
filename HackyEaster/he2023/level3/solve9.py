import codecs

msg="he23{gulliver's_travels_affect_2023}"

msg='he23{u7f_b0m5s_8r3_n07_8lway5_1gn0r3d}'

trans = {
        # '2': '☡',
        '2': '②',
        '3': 'ᗱ',
        'e': 'ε',
        'l': 'ㅣ',
        'f': 'ƒ',
        'm': '𝕞',
        't': '𝙩',
        }
encodings=['utf-16-le', 'utf-16-be']
boms = [codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE]

with open('message.txt', 'rb') as inF:
    msg = inF.read()
    chars = msg.split(b'\xff\xfe')
    for c in chars:
        cs = c.split(b'\xfe\xff')
        if len(cs) > 1:
            print(f"{cs[0].decode(encodings[0])}{cs[1].decode(encodings[1])}",end='')
    print()
