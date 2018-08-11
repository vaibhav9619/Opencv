import cv2
import numpy as np
lower_cascade=cv2.CascadeClassifier("haarcascade_smile.xml")
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    #frame=cv2.imread("images.jpg")
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    body=lower_cascade.detectMultiScale(gray,4.1,4)
    for  (x,y,w,h) in body:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("img",frame)
    k=cv2.waitKey(1)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()

