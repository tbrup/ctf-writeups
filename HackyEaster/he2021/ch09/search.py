import hashlib
import re


base_url = "http://46.101.107.117:2104/"
solve_url = base_url+'order'

cafeRe = re.compile('cafe')
colaRe = re.compile('c01a')
decafRe = re.compile('decaf')
colaDecafRe = re.compile(r'^.*(c01a)*(decaf).*$')

post_data = {'id': '11865456 Vanilla Cafe'}
test_data = {'id': '11865457 Vanilla Cafe'}


def hash(text):
    m = hashlib.sha256()
    m.update(text)
    return m.hexdigest()


# h = hash(b'11865457 Vanilla Cafe')
# print(h)

res = {}
for i in range(10000000, 100000000):
    if i % 1000000 == 0:
        print(i)
    s = b'%d Cola Decaf' % i
    h = hashlib.sha256(s).hexdigest()
    if h.find("c01a") != -1:
        if h.find("decaf") != -1:
            print('found match for s: %s' % s)
            print(h)
            res[s] = h

print(res)
