import urllib.request
import urllib.parse
import time
import string
import hashlib
import base64
import requests
from requests.auth import HTTPBasicAuth

def getPics(s):
    md = {}
    for i in range(2,99):
        u = base_url+'pic/%d'%i
        print(i, end='')
        r = s.get(u)
        try:
            h = hashlib.md5()
            h.update(base64.b64encode(r.text.encode('utf-8')))
            d = h.hexdigest()
            if d in md:
                md[d].append(i)
            else:
                md[d] = [i]
        except ValueError:
            pass
    print()
    return(md)

base_url = 'https://21.hackyeaster.com/'
payload = '{flag: "dsfasdfasdfasdf"}'
response = '{"solveStatus":"WRONG","challengeLevel":null,"challengeDifficulty":null,"challengePoints":null,"levelUp":null}'

def login(session):
    https_proxy = "https://localhost:8081"

    proxyDict = {
              "https" : https_proxy
            }
    # import requests

    # url = "https://hackyeaster.com/auth/login"

    # payload={'username': 'thomas.brupbacher@protonmail.ch',
    # 'password': 'jafpyw-wyvgy2-hyhFyk'}
    # files=[

    # ]
    # headers = {}

    # response = requests.request("POST", url, headers=headers, data=payload, files=files)

    # print(response.text)
    # r = session.get(base_url+'auth/login')
    # print(r.headers)
    headers = {
        'Origin': 'https://21.hackyeaster.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json,text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        'Referer': 'https://21.hackyeaster.com/auth/login',
        'Accept-Language': 'en-GB,en-US',
        'Host': '21.hackyeaster.com'
            }
    post_data = {'username': 'thomas.brupbacher@protonmail.ch',
                 'password': 'jafpyw-wyvgy2-hyhFyk'}
    # raw_data = 'username=thomas.brupbacher%40protonmail.ch&password=jafpyw-wyvgy2-hyhFyk'
    r = session.post(base_url+'auth/login', data=post_data,
                     headers=headers)
    print(r.headers)
    print(r.status_code)
    for k in r.headers:
        print(k, r.headers[k])
    print('\n\n')
    print(r.content)

    headers['Content-Type'] = 'application/json'
    check_url = 'rest/user/challenge/26/checkflag'
    print(base_url + check_url)
    print('https://21.hackyeaster.com/rest/user/challenge/26/checkflag')
    r = session.post(base_url + check_url,
                data= b"{'flag': 'sdfasdfa'}",
                headers=headers)
    print(r.headers)
    print(r.status_code)
    for k in r.headers:
        print(k, r.headers[k])
    print('\n\n')
    print(r.content)
    # r = requests.get('https://21.hackyeaster.com/auth/login',
    #         auth = HTTPBasicAuth('thomas.brupbacher@protonmail.ch',
    #                              'jafpyw-wyvgy2-hyhFyk'  ))
    # print(r.headers)
    # print(r.status_code)
    # print('\n\n')
    # print(r.content)
    # r = session.get('https://21.hackyeaster.com/#/challengedetails/26')
    # print(r.headers)
    # print(r.status_code)
    # print(r.content)


def submit(session, flag):
    check_url = 'rest/user/challenge/26/checkflag'
    print('Submitting flag:', flag, ' to ', check_url)
    post_data = {'flag': flag}
    headers = {
  'Cookie': 'JSESSIONID=61583B72EE151A8F2370DEA3C62D82A9',
    'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
    r = session.post(base_url + check_url, post_data, headers=headers)
    print(r.headers)
    print(r.status_code)
    print(r.text)
    return(r.text)



import requests
session = requests.session()
login(session)
#submit(session,'sadfasdfasdf')
# with open('flags.txt', 'r') as inF:
#     for f in inF.readlines():
#         print(f[:-1])



