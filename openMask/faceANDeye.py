import numpy as np
import cv2
import time
face_detector=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
eye_detector=cv2.CascadeClassifier("haarcascade_eye.xml")
cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faces=face_detector.detectMultiScale(gray,2,5)
    # print(faces)
    for (x,y,w,h) in faces:
        # cv2.circle(img, (x, y), 5, (0, 0, 255), 2)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4)
        # cv2.line(img, (x+110, y+110), (x+w, y+h), (0, 0, 0), 20)
        gray_face = gray[y:y + h, x:x + w]
        # gray_face=cv2.cvtColor(faces,cv2.COLOR_RGB2GRAY)
        eyes=eye_detector.detectMultiScale(gray_face,2,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(img, (x+ex,y+ey), (x+ex + ew, y+ey + eh), (0, 0, 0), 10)



    cv2.imshow("image",img)


    cv2.waitKey(1)