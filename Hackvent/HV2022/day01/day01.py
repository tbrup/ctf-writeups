import cv2
from pyzbar.pyzbar import decode
from PIL import Image, ImageSequence
import numpy


res = b''
im = Image.open('hackvent2022_01.gif')
for frame in ImageSequence.Iterator(im):
    data = decode(frame)[0]
    res += data.data
print(res)


res = ''
det = cv2.QRCodeDetector()
for frame in ImageSequence.Iterator(im):
    im_cv = cv2.cvtColor(numpy.array(frame), cv2.COLOR_RGB2BGR)
    data = det.detectAndDecode(im_cv)[0]
    res += data

print(res)

