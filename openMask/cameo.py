import numpy as np
import cv2
import time
# count=0
cap=cv2.VideoCapture(0)
while True:
    # time.sleep(1)

    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2LUV)
    # cv2.imshow(str(time.time()),img)
    cv2.imshow("image",gray)
    # cv2.imwrite("images/"+ str(count)+ "image.jpg",img)# stores final location idirectoryn some
    # count += 1
    cv2.waitKey(1)
# for new capture we have to  destroy the previous 1
# cv2.destroyAllWindows()