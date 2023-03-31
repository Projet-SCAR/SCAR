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
# while 1 :
#     ret,image = cam.read()
#     cv2.imshow('ImageTest2',image)
#     k = cv2.waitKey(1)
#     if k != -1:
#         break
path = '/home/scar/Documents/Programme/img_a_traiter/'+ str(datetime.now()) +'.jpg'
cv2.imwrite(path,image)
cam.release()
cv2.destroyAllWindows()

