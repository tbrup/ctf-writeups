import cv2
import itertools
import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode


# first split the image into the small boxes
# since the image is 24800 x 24800 pixels, PIL bombs
# so use OpenCV

def isAllWhite(dta):
    return not any((line[:, :] != 255).any() for line in dta)


def getTiles():
    image = cv2.imread('haystack.png')
    x, y = 24800, 24800
    h = x // 31
    imgs = []
    for ix, iy in itertools.product(range(0, x, h), range(0, y, h)):
        cropped = image[ix:ix + h, iy:iy + h]
        if not isAllWhite(cropped):
            imgs.append(cropped)

    print(f'{len(imgs)} tiles that are not white')
    return imgs


def tileWithBorder(tile):
    size = len(tile)
    newSize = (len(tile) // 25) * 35
    border = 5 * len(tile) // 25
    img = np.zeros((newSize, newSize, 3), np.uint8)
    img[:, :] = (255, 255, 255)
    for row in range(size):
        img[border:border + size, border + row] = tile[:, row]
    return img


def handleTile(tile):
    allTiles = [tile]
    allTiles.extend(
        cv2.rotate(tile, op)
        for op in [
            cv2.ROTATE_90_CLOCKWISE,
            cv2.ROTATE_180,
            cv2.ROTATE_90_COUNTERCLOCKWISE,
        ]
    )
    for t in allTiles:
        data = decode(Image.fromarray(t))
        if len(data) > 0:
            foundText = data[0].data.decode()
            if foundText != 'Sorry, no flag here!':
                print(f'tile with code {foundText}')
            return


def analyseTile(tile):
    # my_tile = tileWithBorder(tile)

    # handleTile(my_tile)
    handleTile(tile)
    size = len(tile)
    if size > 25:
        new_size = size // 2
        for x, y in itertools.product(range(0, size, new_size), range(0, size, new_size)):
            new_tile = tile[x:x + new_size, y:y + new_size]
            if not isAllWhite(new_tile):
                analyseTile(new_tile)


def testTile():
    image = cv2.imread('crop_2400_3200.png')
    analyseTile(image)


if __name__ == '__main__':
    imgs = getTiles()
    for img in imgs:
        analyseTile(img)
    # testTile()
