import cv2

image=cv2.imread("../Images/lambo.png")
hsv_image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_range=(0, 13, 75)

upper_range=(18, 255, 255)

mask=cv2.inRange(hsv_image, lower_range, upper_range)

color_image=cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Color Detected", color_image)

cv2.waitKey(0)