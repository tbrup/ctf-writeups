# try a timing based attack on the path finder

import urllib.request
import urllib.parse
import numpy as np
import time
import string
import sys
import io
import hashlib
import base64
from PIL import Image


def mse(im1_arr, im2_arr):
    #diff = im1_arr - im2_arr
    err = np.sum((im1_arr - im2_arr) ** 2)
    err /= float(im1_arr.shape[0])
    return 3.0*err

def match(im1_arr, im2_arrs):
    rms = np.empty(4, dtype=np.float)
    for i in range(4):
        rms[i] = mse(im1_arr, im2_arrs[i])
    avg = np.sum(rms) / 4.0
    rms2 = np.true_divide(rms, avg)
    return (np.max(rms2) - np.min(rms2))

def match_with(im, im2, thresh):
    (sX,sY) = im.size
    arrlen = sX*sY*3
    (sX2,sY2) = im2.size

    if sX == sX2 and sX == sY2 and sX == sY:
        # build an array with all rotated images as arrays
        im_arrs = []
        for i in range(4):
            im_arrs.append(np.array(im, dtype=np.float).reshape((arrlen)))
            if i < 3:
                im = im.rotate(90)
        im_arr2 = np.array(im2, dtype=np.float).reshape((arrlen))
        m = match(im_arr2,im_arrs)
        if m > thresh:
            return True
    else:
        if sX == sX2 and sY == sY2:
            return True
        elif sX == sY2 and sY == sX2:
            return True
        else:
            return False
    return False

#def md5(b):
#    h = hashlib.md5()
#    h.update(b)
#    d = h.hexdigest()
#    return d


#def rotateAndMD5(img):
#    retVal = []
#    index = 0
#    while True:
#        b = io.BytesIO()
#        img.save(fp=b, format='jpeg')
#        #img.show()
#        # retVal.append(md5(raw))
#        retVal.append(md5(img.tobytes()))
#        if index == 3:
#            return retVal
#        index += 1
#        img = img.rotate(90)


base_url = "http://46.101.107.117:2107/"
def getPics(s):
    pics = {}
    for i in range(1,99):
        u = base_url+'pic/%d'%i
        r = s.get(u)
        # try:
        with io.BytesIO(r.content) as imgF:
            img = Image.open(imgF)
            img.load()
            pics[i] = img
    return(pics)


def runMatch(session, pics, found, thresh):
    solve_url = base_url+'solve'
    post_data = {'first': '1', 'second': '2'}
    for i in range(1,99):
        if not found[i]:
            for j in range(i+1, 99):
                if not found[j]:
                    try:
                        if match_with(pics[i], pics[j], thresh):
                            post_data['first'] = i
                            post_data['second'] = j
                            r = session.post(solve_url, post_data)
                            if r.text[:2] != 'ok' and r.text != 'nextRound':
                                raise ValueError
                            # print('pics %d and %d match!' %(i,j))
                            found[i] = True
                            found[j] = True
                            break
                    except ValueError:
                        print(i,j)
                        print(pics[i].size, pics[j].size)
                        print(r.text)
                        # pics[i].show()
                        # pics[j].show()
                        pass

    nNotFound = 0
    for v in found:
        if not v:
            nNotFound += 1
    return r.text, session, found, nNotFound

def solveRound(session):
    r = session.get(base_url)
    pics = getPics(session)
    found = [False for i in range(99)]
    found[0] = True
    nNotFound = 98
    thresh = 0.9

    while nNotFound > 0:
        result, session, found, nNotFound = \
            runMatch(session, pics, found, thresh)
        print(result, nNotFound, thresh)
        thresh -= 0.1
    return result


def solve():
    count = 0
    ok = 'nextRound'
    res = ok
    import requests
    session = requests.session()
    while res == ok:
        count += 1
        print('round: ', count)
        res = solveRound(session)
        print(res)


# solve()

with Image.open('Memeory 3.0 - The Final Game_files/34.jpg') as img1:
    with Image.open('Memeory 3.0 - The Final Game_files/55.jpg') as img2:
    #img.show()
        m = match_with(img1, img2, 0.8)
        print(m)

solve()
"""
{'Secret': 'https://hackyeaster.hacking-lab.com/hackyeaster/images/challenge/egg16_UYgXzJqpfc.png', 'Answer': 'Thanks PathFinder you saved my life by giving me the solution to this sudoku!', 'your_solution': [[1, 5, 7, 2, 9, 4, 6, 8, 3], [2, 6, 9, 3, 5, 8, 1, 7, 4], [8, 4, 3, 7, 1, 6, 5, 2, 9], [4, 9, 6, 5, 8, 3, 7, 1, 2], [5, 2, 8, 9, 7, 1, 3, 4, 6], [7, 3, 1, 6, 4, 2, 8, 9, 5], [9, 7, 2, 1, 3, 5, 4, 6, 8], [6, 8, 5, 4, 2, 7, 9, 3, 1], [3, 1, 4, 8, 6, 9, 2, 5, 7]], 'sudoku': [[0, 0, 0, 2, 0, 4, 6, 0, 0], [2, 0, 9, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 6, 5, 0, 0], [0, 0, 6, 5, 0, 0, 7, 1, 0], [0, 0, 0, 9, 0, 0, 0, 4, 0], [7, 3, 1, 0, 0, 0, 0, 0, 0], [0, 7, 0, 0, 3, 0, 0, 0, 8], [0, 8, 0, 0, 2, 7, 0, 3, 1], [0, 1, 4, 0, 6, 0, 0, 0, 0]]}
here is your flag: he2021{0k-1-5u44end3r-y0u-w1n!}
"""
