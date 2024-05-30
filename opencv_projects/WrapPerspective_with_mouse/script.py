import cv2
import numpy as np


image = cv2.imread('./Images/cards.jpg')

# gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# canny = cv2.Canny(gray_scale,100,300)
# kernel = np.ones((5,5), np.int8)
# dilate = cv2.dilate(gray_scale, kernel, iterations=1)
# erode = cv2.erode(dilate, kernel, iterations=1)

circles = np.zeros((4,2),int)

count = 0

def mousepoints(event, x, y, flags, params):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[count] = x,y
        print(f"mouse click no: {count}", circles)
        count+=1
        print(max(circles.any()))


while True:
    if count == 4:
        # width = (circles[::, 0].max())- (circles[::, 0].min())
        # height = (circles[::, 1].max()) - (circles[::, 1].min())
        width = 300
        height = 600
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imageOutput = cv2.warpPerspective(image, matrix,(width,height))
        cv2.imshow('Final Output Image', imageOutput)
        
    cv2.imshow("Input Image", image)
    cv2.setMouseCallback('Input Image', mousepoints )

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cv2.destroyAllWindows()