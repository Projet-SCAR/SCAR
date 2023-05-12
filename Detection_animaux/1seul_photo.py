# -*- coding: utf-8 -*-
"""
Created on Tue May  2 15:30:49 2023

@author: barbi
"""

# Import opencv and initialize the HOG person detector
import cv2
from ultralytics import YOLO
import time
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()

#importation du model YOLO utilisé
model = YOLO("yolov8l.pt")

time.sleep(10)
    #on fait le traitement uniquement si on arrive à trouver une image
try:
    # ouverture de l'image prise en direct (Polytech Annecy-Chambéry ipcam video stream)
    cap = cv2.VideoCapture("http://view:app@192.168.119.194/mjpg/video.mjpg")
    print("Stream found.")
    success, img = cap.read()
    
    #Application du modèle YOLO sur l'image
    res = model(img, conf=0.3, classes=[0,1,2,3,14,15,16,17,18,19,24,26,28], line_thickness=2)
    
    #affichage résultat
    res_plotted = res[0].plot()
    cv2.imshow("result", res_plotted)
    cv2.waitKey(1) 
            
except:
    # si on ne trouve pas d'image
    print("Stream not found.")
