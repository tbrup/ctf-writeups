import json
import base64


def expand(level, jwt, sig):
    if len(jwt.split('.')) < 3:
        if jwt != 'he' and jwt != 'no{flag}':
            print(jwt)
        return

    header_enc, payload_enc, sig_enc = jwt.split('.')
    payload_enc += '=' * (-len(payload_enc) % 4)  # add padding
    payload = json.loads(base64.b64decode(payload_enc).decode("utf-8"))
    #print('level: ', level, payload.keys())
    #print('length of jwt:', len(jwt))
    #print('length of payload:', len(payload))
    keys = payload.keys()
    for k in sorted(keys):
        expand(level+1, payload[k])


with open('jwts.txt', 'r') as inF:
    jwt_data = inF.read()
    header_enc, payload_enc, sig_enc = jwt_data.split('.')
    payload_enc += '=' * (-len(payload_enc) % 4)  # add padding
    payload = json.loads(base64.b64decode(payload_enc).decode("utf-8"))
    header = base64.b64decode(header_enc).decode("utf-8")
    print(sig_enc)
    sig = base64.b64decode(sig_enc).decode("utf-8")

    print(sorted(payload.keys()))
    print(header)
    print(sig)
    with open('payload.txt', 'w') as outF:
        outF.write(base64.b64decode(payload_enc).decode("utf-8"))

    for k in sorted(payload.keys()):
        #print(k, len(payload[k]), payload[k][:80])
        expand(0, payload[k], sig)
