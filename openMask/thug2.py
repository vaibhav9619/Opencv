import cv2
from PIL import Image
cap=cv2.VideoCapture(cv2.CAP_ANY)
while True:
    ret,img=cap.read()
    if ret:
        cv2.imshow("Live",img)
        if cv2.waitKey(1)==27:
            break
cap.release()
cv2.destroyAllWindows()
