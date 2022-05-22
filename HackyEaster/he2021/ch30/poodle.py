import re
import sys
import requests


BLOCKLEN = 16
decryptionErrorRe = re.compile('Decryption Error.')
imageFoundRe = re.compile('src=\"data:image/png')
spanRe = re.compile('<span>(.+)</span>')
base_url = "http://46.101.107.117:2110/"
code_url = base_url+'picture?code='
cat = '05C9AF9CF1A450081E5775ED22E384D375CC5AAD7DE30BB2419F5F7D5D9973B310D5098C4189DFD0D80D0184781C0B590EBE65DF10D35DCCA62A746D60523D7E'
egg = '41E5D00E5CECC3019834C99B403DE4B24933AF3087BCE219699D7E3EB178A06F7B4717A36C617760EC0AD8BFD5DF05B2'
ind = ' 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7'
myc = ' { " i m a g e " :   " e g g " ,   " e f f e c t " :   4 } X X X 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5'
pony ='6395BF0DE317C98B7C01823798291736D46D6A1A6C7A9C5D7F8DBFC942C86961D0E174797972AE30C4BEF5840238E5E8'
myp = ' { " i m a g e " :   " p o n y " ,   " e f f e c t " :   4 } X X X 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5'
# padding = 32
# iv = 'A'*(padding - 2)

def decodeStatus(r):
    if r.status_code == 200:
        if decryptionErrorRe.search(r.text):
            return 'DecryptionError'
        elif imageFoundRe.search(r.text):
            return 'ImageFound'
        elif spanRe.search(r.text):
            g = spanRe.search(r.text)
            return g.group(1)
        else:
            'Unhandled'
    else:
        return 'HTTPError'


def buildPrePostFix(code, block, offset):
    prefix = code[:2*(block*BLOCKLEN + offset)]
    postfix = code[2*(block*BLOCKLEN + offset+1):]
    return (prefix,postfix)


def buildCode(code, block, offset, byte):
    (pre,post) = buildPrePostFix(code, block, offset)
    return pre + '{:02X}'.format(byte) + post

# Assume that the code is PKCS padded and that we can use a padding oracle to
# figure out the padding length.  The function returns the number of padding
# bytes.

# It is assumed, that the padding is done in any case, the padded bytes are
# filled with the number of padded bytes: if there is one byte padding, this byte
# has the value 0x01, if there are two bytes, both are set to 0x02.

# The validity of the code is tested first, padding errors are detected using "Decryption Error."

def findPadding(code, url):
    session = requests.session()
    r = session.get(url + code)
    if decodeStatus(r) == 'ImageFound': # code is OK
        block = len(code) // (2*BLOCKLEN) - 2
        print('Block: ', block)
        for offset in range(BLOCKLEN):
            for byte in range(256): # try every possible value for byte at offset
                newCode = buildCode(code, block, offset, byte)
                r = session.get(url + newCode)
                if decodeStatus(r) == 'DecryptionError':
                    print(code)
                    print(newCode)
                    print(r.text)
                    print(byte)
                    return (len(code) // 2 - BLOCKLEN) - (block * BLOCKLEN + offset)
    else:
        raise 'IncorrectCodeAtStart'


# To decode the last byte, we assume that the padded bytes are filled as
# described above.  Now we try to construct a code with one more byte of padding
# by setting the known padding bytes to the new value (= old value + 1): this can
# be done by xoring the known plaintext.  If we find a code without padding
# error, we can calculate the original value of the at this position.
def incPadding(oldPad):
    oldVal = len(oldPad) // 2
    newVal = oldVal + 1
    newPad = ''
    for i in range(len(oldPad)//2):
        x = int(oldPad[2*i:2*i+2], 16)
        newPad += '{:02X}'.format(x ^ oldVal ^ newVal)
    return newPad

def decodeLastByte(code, url, padding):
    lastBlock = code[-2*BLOCKLEN:]
    pads      = incPadding(code[-2*(BLOCKLEN+padding):-2*BLOCKLEN])
    prefix    = code[:-2*(BLOCKLEN+padding+1)]
    crypt     = int(code[-2*(BLOCKLEN+padding+1):-2*(BLOCKLEN+padding)],16)
    session = requests.session()
    for run in range(2):
        if run == 1:
            prefix = code[:-2*(BLOCKLEN+padding+2)]
            crypt2 = int(code[-2*(BLOCKLEN+padding+2):
                -2*(BLOCKLEN+padding+1)],16)
            prefix = prefix + '{:02X}'.format(crypt2 ^ run)
        for byte in range(256):
            newCode = prefix + '{:02X}'.format(byte) + pads + lastBlock
            r = session.get(url + newCode)
            if decodeStatus(r) != 'DecryptionError':
                plain = crypt ^ byte ^ (padding+1)
                # print(padding, byte, chr(plain))
                return  (newCode,chr(plain))
    print(newCode)
    print(code)
    print(pads)
    print(prefix)
    raise BaseException('NoByteFound')


def setEffectByte(code, index, now, should, url):
    indexVariable = index + BLOCKLEN
    prefix    = code[:2*index]
    crypt     = int(code[2*index:2*index+2],16)
    middle    = code[2*index+2:2*indexVariable]
    tail      = code[2*indexVariable+2:]
    newCrypt  = '{:02X}'.format(crypt ^ now ^ should)
    print(hex(crypt), newCrypt)
    session = requests.session()
    for byte in range(256):
        newCode = prefix + newCrypt + middle + '{:02X}'.format(byte) +  tail
        # print(code)
        # print(newCode)
        r = session.get(url + newCode)
        if decodeStatus(r) == 'ImageFound':
            # print(code)
            print(newCode)
            # print(r.text)
            # print(byte)
            return  newCode
        else:
            print(decodeStatus(r))


def setSubject(code, index, now, should, url):
    codes = []
    for i in range(2*BLOCKLEN):
        codes.append(int(code[2*i:2*i+2], 16))

    prefix    = code[:2*index]
    tail      = code[2*index+2*len(now):]
    newCrypt = ''
    for i in range(len(now)):
        tmp = codes[i+index] ^ ord(now[i]) ^ ord(should[i])
        newCrypt  += '{:02X}'.format(tmp)
    print(newCrypt)
    session = requests.session()
    newCode = prefix + newCrypt + tail
    print(code)
    print(newCode)
    r = session.get(url + newCode)
    if decodeStatus(r) == 'ImageFound':
        # print(code)
        print(newCode)
        # print(r.text)
        # print(byte)
        return  newCode
    else:
        print(decodeStatus(r))


#print('padding: ', findPadding(egg, code_url))
# padding = findPadding(egg, code_url)
# code = egg
# padding = 3
# plaintext = ''
# for i in range(padding, BLOCKLEN):
#     (newCode, c) = decodeLastByte(code, code_url, i)
#     plaintext += c
#     code = newCode
#     print(plaintext[::-1])

# setEffectByte(egg, 27, ord('4'), ord('3'), code_url)
setSubject(pony, 11, 'pony"', 'egg" ', code_url)
