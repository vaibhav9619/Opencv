import cv2
from PIL import Image
import numpy as np
maskPath="mask.png"
mask=Image.open(maskPath)
detect=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
def Thug_mask(image):
    grey=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    faces=detect.detectMultiScale(grey,2,5)
    back=Image.fromarray(image)
    for (x,y,w,h) in faces:
        resixe=mask.resize((w,h),Image.ANTIALIAS)
        offset=(x,y)
        back.paste(resixe,offset,mask=resixe)
    return np.asarray(back)
cap=cv2.VideoCapture(cv2.CAP_ANY)
while True:
    ret,img=cap.read()
    if ret:
        cv2.imshow("Live",Thug_mask(img))
        if cv2.waitKey(1)==27:
            break
cap.release()
cv2.destroyAllWindows()
