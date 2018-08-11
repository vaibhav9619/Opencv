from PIL import Image
import sys
import cv2
cam=cv2.VideoCapture("http://www.juude.info/user/user-images/group.png")
cam1=cv2.VideoCapture("https://banner2.kisspng.com/20180402/dlw/kisspng-t-shirt-sunglasses-clip-art-thug-life-5ac1b26dbc5755.3735686315226435657715.jpg")
# detect=cv2.CascadeClassifier("haarcascade_eye.xml")
detect=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
ret,cap=cam.read()
grey=cv2.cvtColor(cap,cv2.COLOR_RGB2GRAY)
face=detect.detectMultiScale(grey,2,5)
for (x,y,w,h) in face:
    cv2.rectangle(cap,(x,y),(x+w,y+h),(255,0,0),2)
# face=cv2.cvtColor(face,cv2.COLOR_RGB2GRAY)
# specs=cv2.resize(cam1,(w,h))
# w,h,c=specs.shape
# face[y:y+w,x:x+h]


cv2.imshow("face",cap)
cv2.waitKey(0)
cam.release()
cv2.destroyAllWindows()
