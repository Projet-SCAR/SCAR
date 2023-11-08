import pandas as pd
import numpy as np

import glob


images=glob.glob("**/*.JPG")
images.sort()
import cv2 as cv

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


def graph_vert(): 

    d={'date':[],'taux_vert':[]}
    for image in images:
        img=cv.imread(image)
        img=cv.medianBlur(img, 5)
        img=resize(img,50) 
        d['taux_vert'].append(detectvert(img))
        i=image.find("_")
        d['date'].append(image[i+2:i+12])
        
    
        
    return(d)


def graph_neige(): 
    d={'date':[],'taux_neige':[]}
    for image in images:
        img=cv.imread(image)
        img=cv.medianBlur(img, 5)
        img=resize(img,50) 
        d['taux_neige'].append(seuillage(img))
        i=image.find("_")
        d['date'].append(image[i+2:i+12])
        # taux_neige=seuillage(img)
        # N.append(taux_neige)
    return(d)
        

dico_r=graph_vert()   
dico_n=graph_neige()

df_r=pd.DataFrame.from_dict(dico_r)
df_n=pd.DataFrame.from_dict(dico_n)
df_r['date']=pd.to_datetime(df_r['date'].astype(str), format='%Y-%m-%d')
df_r.set_index('date',inplace=True)
df_r.plot()
df_n['date']=pd.to_datetime(df_n['date'].astype(str), format='%Y-%m-%d')
df_n.set_index('date',inplace=True)
df_n.plot()
