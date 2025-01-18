# import cv2
# import numpy as np

# image = cv2.imread("../Images/shapes.png")


# # Step 1: Convert the Image into Gray Scale

# image_grayscale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# # Step 2: Apply Canny Edge Detector to Detect the Edges

# lower_threshold=100
# upper_threshold=150
# canny_edge=cv2.Canny(image_grayscale, lower_threshold, upper_threshold)

# # Step 3: Find the Contours

# contours, hirearchy = cv2.findContours(canny_edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# # Step 4: Find the Length of the Contours

# print(f"Length of the Contours = {str(len(contours))}")

# # Step 5: Draw the Contours
# image_copy=image.copy()

# cv2.drawContours(image_copy, contours, -1, (0,255,0), 3)


# cv2.imshow("Original Image", image)

# cv2.imshow("Gray Scale Image", image_grayscale)

# cv2.imshow("Edge Detector", canny_edge)

# cv2.imshow("Draw Contours", image_copy)
# cv2.waitKey(0)


import cv2
import numpy as np

image = cv2.imread('./Images/shapes.png')
upper_threshold = 150
lower_threshold = 150
canny = cv2.Canny(image, lower_threshold, upper_threshold)
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
contours, hirearchy = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print(f"Length of the Contours ={str(len(contours))}")

image_copy = image.copy()

cv2.drawContours(image_copy, contours, -1,(0,255,0),3)

cv2.imshow('Original Image', image)


cv2.imshow('grayscale Image', image_grayscale)
cv2.imshow('Canny Image', canny)


cv2.imshow("output", image_copy)
cv2.waitKey(0)
