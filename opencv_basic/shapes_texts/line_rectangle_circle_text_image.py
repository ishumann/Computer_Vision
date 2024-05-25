# import cv2
# import numpy as np
# # This is a gray scale image because we have only 512 x 512 pixels or boxes
# #image=np.zeros((512,512))

# #If we want to add the color functionality we have to give it the channels
# image=np.zeros((512,512, 3))

# # Add color

# image[:] = 255, 0, 0

# # Drawing a Line

# cv2.line(image, (0,0), (image.shape[1], image.shape[0]), (0,255,0), 3)

# # Draw a rectnagle
# cv2.rectangle(image, (0,0), (250, 350), (0,0,255), 3)

# #Draw a Circle


# cv2.circle(image, (400,50), 30, (0,255,255), -1)

# # Write Text on an Image

# cv2.putText(image, "OpenCV", (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,150,0), 2)

# cv2.imshow("Output Image", image)

# cv2.waitKey(0)


import cv2
import numpy as np


image = np.zeros((512,512,3))

# add color

image[:] = 255,0,0

cv2.line(image, (0,0),(250,350), (0,0,255), 3)

cv2.rectangle(image,(0,0), (250,350),(0,0,255),3)

# draw a circle

cv2.circle(image,(400,50),30, (0,255,255), 2)

# write words

cv2.putText(image, 'opencv',(100,260), cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2 )

cv2.imshow('output', image )
 
 
cv2.waitKey()
