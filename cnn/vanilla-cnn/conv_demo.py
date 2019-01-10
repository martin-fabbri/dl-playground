from PIL import Image
import numpy
from scipy.signal import convolve2d
import cv2

print(f"OpenCV version: {cv2.__version__}")

kernel = [[0.1,0.1,0.1],
          [0.1,0.1,0.1],
          [0.1,0.1,0.1]]

backgroundColor = (0,)*3
pixelSize = 10
imgFile = 'puppy.jpg'
color = True

def drawImage(channel):
    image = Image.open(imgFile)
    red, green, blue = image.split()
    if channel == 'grey':
        image = Image.open(imgFile).convert('LA')
    elif channel == 'r':
        image = red
    elif channel == 'g':
        image = green
    elif channel == 'b':
        image = blue

    image = image.resize((image.size[0]//pixelSize, image.size[1]//pixelSize), Image.NEAREST)
    image = image.resize((image.size[0]*pixelSize, image.size[1]*pixelSize), Image.NEAREST)
    image = image.convert('RGB')
    pixel = image.load()

    for i in range(0, image.size[0], pixelSize):
        for j in range(0, image.size[1], pixelSize):
            for r in range(pixelSize):
                pixel[i+r, j] = backgroundColor
                pixel[i, j+r] = backgroundColor

    return image


