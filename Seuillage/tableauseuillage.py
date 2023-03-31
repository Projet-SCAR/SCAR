import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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

imgs = []
imgs.append(img1)
imgs.append(img2)
imgs.append(img3)
imgs.append(img4)
imgs.append(img5)
imgs.append(img6)
imgs.append(img7)
imgs.append(img8)
imgs.append(img9)

seuils = [ 75, 100, 125, 150, 175, 200, 225, 250]

def resize(img, scale_percent):
    img=img[0:img.shape[0]-80,0:img.shape[1]]
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    res = cv.resize(img, dim, interpolation=cv.INTER_CUBIC)
    return(res)

#seuillage
def seuillage(img, seuil):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret1,th1 = cv.threshold(gray, seuil, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    th1=th1/255
    return(th1)


def run(imgs,seuils): 
    fig, axs = plt.subplots(9, 9, figsize = (40, 25))
    for i in range(len(imgs)):
        for j in range (len(seuils)):
        
        
            img=resize(imgs[i],50) 
            img=cv.medianBlur(img, 5)
            img=seuillage(img, seuils[j])
            axs[i][j].set_title(seuils[j])
            axs[i][j].imshow(img)  
            
      
    
        
run(imgs,seuils)
plt.show()
