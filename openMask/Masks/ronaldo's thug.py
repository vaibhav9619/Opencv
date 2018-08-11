import cv2
import numpy as np
from PIL import Image

thug_mask="mask.png"
p1="ronaldo.jpg"
img=cv2.imread("ronaldo.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces=face_cascade.detectMultiScale(gray,1.3,0)
background=Image.open(p1)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.waitKey(0)
    mask=Image.open(thug_mask)
    r_mask=mask.resize((w,h),Image.ANTIALIAS)
    offset=(x,y)
    background.paste(mask,offset,mask=r_mask)
background.save("OKIT.jpg")
