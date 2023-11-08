#Code utilisé par le bash pour prendre les photos
import cv2
import numpy
from datetime import datetime

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_AUTO_EXPOSURE,0.25)
cam.set(cv2.CAP_PROP_AUTOFOCUS,0.25)
cam.set(cv2.CAP_PROP_AUTO_WB,0.25)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
ret,image = cam.read()
path = '/home/scar/Documents/Programme/img_a_traiter/'+ str(datetime.now()) +'.jpg'
cv2.imwrite(path,image)
cam.release()
cv2.destroyAllWindows()

