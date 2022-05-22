# Fetch a number of pictures for challenge 30 to find out if the codes will
# repeat.

import re
import requests


base_url = "http://46.101.107.117:2110/"
code_url = base_url+'code'


valueRe = re.compile('value=\"([0-9A-F]+)\"')
unknownEffectRe = re.compile('Unknown effect.')

def ok(reg, text):
    return not reg.search(text)


def findImage(reg, text):
    g = reg.search(text)
    return g.group(1)

session = requests.session()


res = set()
post_data = {'image': 'thecat', 'effect': 2 }
for i in range(1000):
    # post_data['effect'] = i
    r = session.post(code_url, post_data)
    if r.status_code == 200:
        g = valueRe.search(r.text)
        if g:
            res.add(g.group(1))
        # g = unknownEffectRe.search(r.text)
        # if not g:
        #     res.add(i)


print(res)
print(len(res))
with open('thecat_2', 'w') as outF:
    outF.write(str(res))
