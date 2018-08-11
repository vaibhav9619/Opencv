import cv2
import numpy as np
img=cv2.VideoCapture(0)
four=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',four,20.0,(640,480))
while True:
    ret,cap=img.read()
    grey=cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
    cv2.imshow("dfd",cap)
    cv2.imshow("asa",grey)
    cv2.waitKey(1)
out.release()
img.release()