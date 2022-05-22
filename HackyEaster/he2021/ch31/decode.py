map = { '0': '0', '1': '1', '2': '2', '3': '3',
        '4': '4', '5': '5', '6': '6', '7': '7',
        '8': '8', '9': '9', 'a': 'd', 'b': 'e',
        'c': 'f', 'd': 'a', 'e': 'b', 'f': 'c'}

input = ['4ab56415e91e6d5172ee79d9810e30be5da8af18',
         'c19a3ca5251db76b221048ca0a445fc39ba576a0',
         'fdb2c9cd51459c2cc38c92af472f3275f8a6b393',
         '6d586747083fb6b20e099ba962a3f5f457cbaddb',
         '5587adf42a547b141071cedc7f0347955516ae13']


def mapping(s):
    ret = ''
    for c in s:
        ret += map[c]
    return ret


for i in input:
    print(mapping(i))
