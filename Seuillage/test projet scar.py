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

img1= cv.imread('peclerey1600__2020-09-27__09-00-00(1).jpg')
img2 = cv.imread('peclerey1600__2020-07-08__09-00-00(1).jpg')
img3= cv.imread('para1900__2019-11-22__13-00-00(1).jpg')
img4= cv.imread('para1900__2020-06-01__13-00-00(1).jpg')
img5= cv.imread('para2100__2020-07-20__16-00-00(1).jpg')
img6= cv.imread('Para2100__2020-11-21__09-00-00(1).jpg')
img7= cv.imread('peclerey1400Planet__2021-04-14__09-00-00(1).jpg')
img8= cv.imread('peclerey1400Planet__2021-07-03__09-00-00(1).jpg')
img9= cv.imread('peclerey2200Nord__2020-12-21__09-00-00(1).jpg')

plt.show()
def resize(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    res = cv.resize(img, dim, interpolation=cv.INTER_CUBIC)
    return(res)
#seuillage
def seuillage(img):
    res=resize(img,50)
    gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
    ret1,th1 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    plt.imshow(th1)
    plt.title('image avec seuillage')
    plt.show()

def run(img): 
    
    plt.imshow(img)
    plt.show()
    seuillage(img)


def detectvert(img):
    plt.imshow(img)
    plt.show()
    mask2 = cv.inRange(img, (0, 80, 0), (110, 255,110))
    mask2=mask2/255
    plt.imshow(mask2)
    plt.title('detection de vert')
    plt.show()
    print(np.sum(mask2)*100/np.size(mask2))



detectvert(img9)

#trouver le blanc

#mask blanc
    
#mask1 = cv.inRange(img, (190, 150, 190), (255, 255,255))
#
#implot2= plt.imshow(mask1)
#plt.title('detection de blanc')
#plt.show()
#
##mask vert
