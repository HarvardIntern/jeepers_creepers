import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

def calibrate():
    _, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    objp = np.zeros((6*9,3),np.float32)
    objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

    objpoints = []
    imgpoints = []

    ret, corners = cv.findChessboardCorners(gray,(9,6),None)

    if ret:
        objpoints.append(objp)

        corners2 = cv.cornerSubPix(gray, corners, (11,11),(-1,-1),criteria)
        imgpoints.append(corners2)
        cv.drawChessboardCorners(img,(9,6),corners, ret)
        ret, mtx, dist, rvecs, tvecs, = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
        return img, ret, mtx, dist, rvecs, tvecs

    return img, 0

    cv.waitKey(100)


while True:
    a = calibrate()[0]
    cv.imshow("sigma", a)
    cv.waitKey(200)

