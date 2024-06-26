# import cv2
# import numpy as np

# def empty(a):
#     pass

# cv2.namedWindow("Trackbars")
# cv2.resizeWindow("Trackbars", 640, 240)

# cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
# cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
# cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
# cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
# cv2.createTrackbar("Val Min", "Trackbars", 0, 255, empty)
# cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

# while True:
#     image=cv2.imread("../Images/lambo.png")

#     imgHSV=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#     h_min=cv2.getTrackbarPos("Hue Min", "Trackbars")
#     h_max=cv2.getTrackbarPos("Hue Max", "Trackbars")
#     s_min=cv2.getTrackbarPos("Sat Min", "Trackbars")
#     s_max=cv2.getTrackbarPos("Sat Max", "Trackbars")
#     v_min=cv2.getTrackbarPos("Val Min", "Trackbars")
#     v_max=cv2.getTrackbarPos("Val Max", "Trackbars")

#     print(h_min, h_max, s_min, s_max, v_min, v_max)
#     lower=np.array([h_min, s_min, v_min])
#     upper=np.array([h_max, s_max, v_max])

#     mask=cv2.inRange(imgHSV, lower, upper)

#     cv2.imshow("Original Image", image)

#     cv2.imshow("HSV Image", imgHSV)

#     cv2.imshow("Mask Image", mask)
#     cv2.waitKey(1)

import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 640,240)

cv2.createTrackbar('Hue Min', "Trackbars",0,179, empty)
cv2.createTrackbar('Hue Max', "Trackbars",179,255, empty)
cv2.createTrackbar('Sat Min', "Trackbars",0,255, empty)
cv2.createTrackbar('Sat Max', "Trackbars",255,255, empty)
cv2.createTrackbar('Val Min', "Trackbars",0,255, empty)
cv2.createTrackbar('Val Max', "Trackbars",255,255, empty)

while True:
    img1 = cv2.imread('./Images/car.jpg')       
    imgHSV =cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    
    h_min = cv2.getTrackbarPos('Hue Min', 'Trackbars')
    h_max = cv2.getTrackbarPos('Hue Max', 'Trackbars')
    s_min = cv2.getTrackbarPos('Sat Min', 'Trackbars')
    s_max = cv2.getTrackbarPos('Sat Max', 'Trackbars')
    v_min = cv2.getTrackbarPos('Val Min', 'Trackbars')
    v_max = cv2.getTrackbarPos('Val Max', 'Trackbars')
    

    lower= np.array([h_min,s_min,v_min])
    upper= np.array([h_max,s_max,v_max])
    
    mask = cv2.inRange(imgHSV, lower, upper)
    
    color_img = cv2.bitwise_and(img1,img1, mask=mask)
    
    
    cv2.imshow('Original',img1)
    cv2.imshow('HSV Image',imgHSV)
    cv2.imshow('Mask Image',mask)
    cv2.imshow('final_output',color_img)
    cv2.waitKey(1)






































