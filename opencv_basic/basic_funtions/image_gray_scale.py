"""img to gray
"""
import cv2

image = cv2.imread('./Section_01_R/Images/car.jpg')
imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow('output gray', image)
cv2.imshow('output gray', imagegray)

cv2.waitKey(0)