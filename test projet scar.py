import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
from skimage.color import rgb2gray, rgb2hsv, hsv2rgb
from skimage.io import imread, imshow
from sklearn.cluster import KMeans
from keras.models import load_model
from PIL import Image, ImageOps
import os

import cv2 as cv

img= cv.imread('peclerey1600__2020-09-27__09-00-00(1).jpg')
img2 = Image.open('peclerey1600__2020-07-08__09-00-00(1).jpg')
implot=plt.imshow(img2)
plt.show()

#seuillage

res = cv.resize(img, dsize=(54, 140), interpolation=cv.INTER_CUBIC)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret1,th1 = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)
implot= plt.imshow(th1)

plt.show()

#trouver le blanc

#mask blanc
mask1 = cv.inRange(img, (190, 150, 190), (255, 255,255))

implot2= plt.imshow(mask1)
plt.show()

#mask vert
mask2 = cv.inRange(img, (0, 120, 0), (128, 245,128))

implot3= plt.imshow(mask2)
plt.show()