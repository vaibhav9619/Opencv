import cv2
img=cv2.VideoCapture(0)
while True:
    ret,cap=img.read()
    cv2.imshow("dfd",cap)
    cv2.waitKey(1)
