# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:19:02 2023

@author: barbi
"""

# Import opencv and initialize the HOG person detector
import cv2
from ultralytics import YOLO
from PIL import Image
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()

#importation du model YOLO utilisé
model = YOLO("yolov8l.pt")
img = Image.open("animal.JPG")
        
#Application du modèle YOLO sur l'image
res = model(img, conf=0.3, classes=[0,1,2,3,14,15,16,17,18,19,24,25,26,28], save=True)
#conf = seuil de confiance pour détecter une classe
#classes = choix des éléments à détecter parmis la liste de YOLO

#affichage résultat
res_plotted = res[0].plot()
cv2.imshow("result", res_plotted)
cv2.waitKey(1)