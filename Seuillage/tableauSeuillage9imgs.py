import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import cv2 as cv
from PIL import Image


seuils = [75, 100, 125, 150, 175, 200, 225, 250]
print("niveaux de seuils", seuils)
imgs = []
dir  = os.getcwd()
dir,__ = os.path.split(dir)
imgs_path = os.listdir(dir + '/IMGS_9')
imgs_path.sort()

for i in imgs_path:
    imgs +=[cv.imread(f"{dir}/IMGS_9/{i}")]

fig, axs = plt.subplots(1, 9, figsize = (40, 10))
for i in range(len(imgs)):
    img=imgs[i]
    plt.imshow(imgs[i])
    img=img[0:img.shape[0]-80,0:img.shape[1]]
    img=cv.medianBlur(img, 5)
    axs[i].imshow(imgs[i])
    #axs[i].set_title(imgs_path[i][:-29])
plt.show()

plt.rcParams.update({'font.size': 40})
fig, axs = plt.subplots(9, 9, figsize = (40, 25))
for i in range (len(imgs)):
    img=imgs[i]
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    axs[i][0].imshow(img)
    axs[i][0].set_axis_off()
    axs[i][0].set_title(imgs_path[i][:-29])
    for j in range (len(seuils)):
        seuil=seuils[j]
        ret1,th1 = cv.threshold(gray, seuil, 255, cv.THRESH_BINARY)
        axs[i][j+1].imshow(th1)
        axs[i][j+1].set_axis_off()
        axs[i][j+1].set_title(f'seuil={seuil}')
plt.tight_layout()
plt.show()

