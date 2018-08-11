import cv2
import numpy as np
from PIL import Image

m="bunny.png"
mask=Image.open(m)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def dog(image):

    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3)
    background = Image.fromarray(image)
    for(x,y,w,h)in faces:
        r_mask=mask.resize((w,h),Image.ANTIALIAS)
        offset=(x,y)
        background.paste(r_mask,offset,mask=r_mask)
    return np.asarray(background)
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if ret:
        cv2.imshow("Thug",dog(frame))
        if cv2.waitKey(1)==27:
            break
cap.release()
cv2.destroyAllWindows()