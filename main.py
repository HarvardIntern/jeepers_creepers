import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)


while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.imshow("window_name",hsv)
    cv.waitKey(1)

