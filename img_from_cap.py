import numpy as np
import cv2 as cv


cap=cv.VideoCapture(0)
if not cap.isOpened():
    print('Cannot open camera')
    exit()
while True:
    ret,frame=cap.read()
    if not ret:
        print('Cannot receive frame . Exiting...')
        break
    # gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    # new_gray=cv.flip(gray, 1)
    # cv.imshow("frame",new_gray)
    new_frame=cv.flip(frame, 1)
    cv.imshow("frame", new_frame)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
