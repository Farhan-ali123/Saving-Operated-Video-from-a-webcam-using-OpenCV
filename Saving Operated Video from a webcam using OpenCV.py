import cv2 as cv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi' , fourcc , 20.0 , (640,480))
while (True):
    ret, frame = cap.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    out.write(hsv)
    cv.imshow('original', frame)
    cv.imshow('frame',hsv)
    if cv.waitKey(1)& 0xFF == ord('a'):
        break
cap.release()
out.release()
cv.destroyAllWindows()


