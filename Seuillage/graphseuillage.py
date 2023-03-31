
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib import colors
# from skimage.color import rgb2gray, rgb2hsv, hsv2rgb
# from skimage.io import imread, imshow
# from sklearn.cluster import KMeans
# from keras.models import load_model
# from PIL import Image, ImageOps
import os
import glob
from PIL import Image
import cv2 as cv
images=glob.glob("*.JPG")
images.sort()


def resize(img, scale_percent):
    img=img[0:img.shape[0]-80,0:img.shape[1]]
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    res = cv.resize(img, dim, interpolation=cv.INTER_CUBIC)
    return(res)
#seuillage
def seuillage(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret1,th1 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    th1=th1/255
    return(np.sum(th1)*100/np.size(th1))

#dectection de vert
def detectvert(img):
    mask2 = cv.inRange(img, (0, 50, 0), (100,255,90))
    mask2=mask2/255
    return(np.sum(mask2)*100/np.size(mask2))


def run_vert(): 
    D=[]
    V=[]
    for image in images:
        img=cv.imread(image)
        img=resize(img,50) 
        taux_vert=detectvert(img)
        i=image.find("_")
        date=image[i:i+11]
        D.append(date)
        V.append(taux_vert)
    return(D,V)


def run_neige(): 
    N=[]
    for image in images:
        img=cv.imread(image)
        img=resize(img,50) 
        taux_neige=seuillage(img)
        N.append(taux_neige)
    return(N)
        
def run_mi_saison():
    
    V=[]
    N=[]
    for image in images:
        img=cv.imread(image)
        img=resize(img,50) 
        taux_vert=detectvert(img)
        taux_neige=seuillage(img)
        V.append(taux_vert)
        N.append(taux_neige)
    return(V,N)


D,V=run_vert() 
print(D,V)  
plt.plot(D,V)
plt.show()
