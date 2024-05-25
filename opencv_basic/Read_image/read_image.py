
'''
Import the Required Library
'''
import cv2

# TO read the image i will use imread function

image = cv2.imread("./Section_01_R/Images/face.png")

# Display the Output Image

cv2.imshow("Output", image)

cv2.waitKey(0)

