from PIL import Image
import cv2
import numpy as np

maskPath="mask.png"
cascPath="haarcascade_frontalface_default.xml"
mask=Image.open(maskPath)

face_cascade=cv2.CascadeClassifier(cascPath)

def thug(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3)
    background=Image.fromarray(image)
    for(x,y,w,h)in faces:
        r_mask=mask.resize((w,h),Image.ANTIALIAS)
        offset=(x,y)
        background.paste(r_mask,offset,mask=r_mask) #just pasted the mask not the trANspiracy

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