#importation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import cv2 as cv
#création d'un tableau avec 9 images
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

#fonction pour recadrer l'image
def resize(img, scale_percent):
    img=img[0:img.shape[0]-80,0:img.shape[1]]
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    res = cv.resize(img, dim, interpolation=cv.INTER_CUBIC)
    return(res)

#fonction de seuillage
def seuillage(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret1,th1 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    th1=th1/255
    return(np.sum(th1)*100/np.size(th1))

#fonction de dectection de vert
def detectvert(img):
    mask2 = cv.inRange(img, (0, 50, 0), (100,255,90))
    mask2=mask2/255
    return(np.sum(mask2)*100/np.size(mask2))

#main
def run(img): 
    #on affiche le tableau d'image
    for i in range(len(img)):
        img=img[i]
        img=resize(img,50) 
        plt.imshow(img)
        plt.show()
        #algorithme de l'arbre de proba
        taux_vert=detectvert(img)
        print(taux_vert)
        if taux_vert>20:
            print('il y a de la verdure')
        else:
                taux_neige=seuillage(img)
                if taux_neige<40:
                    print("C'est la mi-saison")
                else:
                    print('Il y a de la neige')
        

run(imgs)
