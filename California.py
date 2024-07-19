import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
_,img = cap.read()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

def calibrate():

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    objp = np.zeros((6*7,3),np.float32)
    objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

    objpoints = []
    imgpoints = []

    ret, corners = cv.findChessboardCorners(gray,(7,6),None)
    if ret:
        corners2 = cv.cornerSubPix(gray, corners, (11,11),(-1,-1),criteria)
        imgpoints.append(objp)

        cv.drawChessboardCorners(img,(7,6),corners2, ret)
    cv.imshow("img", img)
    cv.waitKey(50000)


calibrate()

