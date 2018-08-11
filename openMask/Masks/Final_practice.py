import cv2
import numpy as np
from PIL import Image

path="modi.png"
mask=Image.open(path)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def thug(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3)
    background=Image.fromarray(image)
    for (x,y,w,h) in faces:
        mask_r=mask.resize((w,h),Image.ANTIALIAS)

        of=(x,y)
        background.paste(mask_r,of,mask=mask_r)
    return np.asarray(background)
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if ret:
        cv2.imshow("THUG LIFE",thug(frame))
        if cv2.waitKey(1)==27:
                break
cap.release()
cv2.destroyAllWindows()
