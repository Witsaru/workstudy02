import cv2
import numpy as np
import utils as u

parameters = cv2.aruco.DetectorParameters_create()
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000)


cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("Video/2023-10-24-155544.webm")
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
while True:
    success, img = cap.read()

    corners, _, _ = cv2.aruco.detectMarkers(img, aruco_dict, parameters=parameters)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if corners:
        aruco_perimeter = cv2.arcLength(corners[0], True)
        pixel_cm_ratio = aruco_perimeter / 66
        corners, ids, _ = cv2.aruco.detectMarkers(gray, aruco_dict)
        list_posAruco = u.aruco_display(corners,ids, 0,img)
        # image_with_markers = cv2.aruco.drawDetectedMarkers(img.copy(), corners, ids)

        # print(corners)
        print(list_posAruco)
    cv2.imshow('img',img)
    cv2.imshow('gray',gray)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()