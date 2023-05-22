import cv2
import itertools
import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode


def getTiles():
    imgs = []
    with Image.open('quilt.png') as img:
        x, y = img.size 
        h = 69
        for iy, ix in itertools.product(range(0, y, h), range(0, x, h)):
            # cropped = image[ix:ix + h, iy:iy + h]
            cropped = img.crop((ix,iy,ix+h, iy+h))
            imgs.append(cropped)

    print(f'{len(imgs)} tiles')
    return imgs


if __name__ == '__main__':
    imgs = getTiles()
    for img in imgs:
        # data = decode(Image.fromarray(img))
        data = decode(img)
        if len(data) > 0:
            foundText = data[0].data.decode()
            print(f'{foundText}', end='')
