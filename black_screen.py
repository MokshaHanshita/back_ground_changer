import cv2
import numpy as np
import time
fourcc= cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output1.avi',fourcc,20.0,(640,480))
cap=cv2.VideoCapture(1)
time.sleep(2)
bg=cv2.imread("background.jpg")
bg = cv2.resize(bg,(640,480))



while cap.isOpened():
    ret,img=cap.read()
    img=np.flip(img,axis=1)
    
    img = cv2.resize(img, (640,480))
    u_black = np.array([90,140,60])
    l_black = np.array([10,10,0])

    mask = cv2.inRange(img, l_black, u_black)
    res = cv2.bitwise_and(img,img, mask =mask)
    f = img - res
    f = np.where(f == 0,bg, f)
    cv2.imshow("mask",f)
    cv2.waitKey(1)
cap.release()
output_file.release()
cv2.destroyAllWindows()
