from __future__ import division
from PIL import Image
import colorsys 
import sys

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

if len(sys.argv) != 2:
    print "1 filename argument"
    exit()

filename = sys.argv[1]
img = Image.open(filename)
hsvAcc = [0, 0, 0]
rgbAcc = [0, 0, 0]
for x in range(img.size[0]):
    for y in range(img.size[1]):
        rgb = img.getpixel((x, y))
        hsv = colorsys.rgb_to_hsv(*rgb)
        hsvAcc[0] += hsv[0]
        hsvAcc[1] += hsv[1]
        hsvAcc[2] += hsv[2]
        rgbAcc[0] += rgb[0]
        rgbAcc[1] += rgb[1]
        rgbAcc[2] += rgb[2]

size = img.size[0] * img.size[1]
hsvAverage = tuple([hsv / size for hsv in hsvAcc])
rgbAverage = tuple([rgb / size for rgb in rgbAcc])
print "hsv: ", hsvAverage
print rgb_to_hex(colorsys.hsv_to_rgb(*hsvAverage))
print "rgb average: ", rgbAverage
print rgb_to_hex(rgbAverage)