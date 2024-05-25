# import cv2
# import numpy as np

# image = cv2.imread("../Images/documentscanner2.jpg")

# kernel = np.ones((5,5), np.uint8)

# #Setting the Threshold Values
# t_lower=400
# t_higher=500

# # Apply Canny Edge Detector

# imgCanny =cv2.Canny(image, t_lower, t_higher)

# # Dialation of Image

# imageDialation = cv2.dilate(imgCanny, kernel, iterations=1)

# # Erosion of Image

# image_erosion = cv2.erode(imageDialation, kernel, iterations=1)
# #cv2.imshow("Original Image", image)

# #cv2.imshow("Canny Image", imgCanny)

# cv2.imshow("Image Dilation", imageDialation)

# cv2.imshow("Image Erosion", image_erosion)

# cv2.waitKey(0)


import cv2
import numpy as np


img = cv2.imread('./opencv_basic/Images/car.jpg')

kernel = np.ones((1,1), np.int8)
low_thresh = 50
high_thresh = 100

edge = cv2.Canny(img, low_thresh, high_thresh)


erode = cv2.erode(edge, kernel=kernel,iterations=1)

cv2.imshow('output',edge)
cv2.imshow('erode', erode)
cv2.waitKey()
