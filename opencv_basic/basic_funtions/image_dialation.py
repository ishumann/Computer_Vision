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


# #cv2.imshow("Original Image", image)

# cv2.imshow("Canny Image", imgCanny)

# cv2.imshow("Image Dilation", imageDialation)


# cv2.waitKey(0)

import cv2
import numpy as np
img = cv2.imread('./Section_01_R/Images/d.jpg')
# Applying Canny Edge Detector

img_canny = cv2.Canny(img, threshold1=400, threshold2=500)

# Applying Dilation 
kernel = np.ones( (5,5), np.uint8)
img_dil = cv2.dilate(img_canny, kernel, iterations=1) 

cv2.imshow('original', img)
cv2.imshow('Canny', img_canny)
cv2.imshow('dilated', img_dil)

cv2.waitKey()