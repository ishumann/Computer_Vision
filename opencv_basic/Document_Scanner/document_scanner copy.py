import cv2
import numpy as np

width = 940
height = 680

def preprocess_image(image):
    image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image_canny = cv2.Canny(image_gray, 450, 600)
    kernel = np.ones((5,5), np.uint8)
    image_dilation = cv2.dilate(image_canny, kernel, iterations=2)
    return cv2.erode(image_dilation, kernel ,iterations=1)
    

def draw_contours(image):
    contours, hirearchy = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    maxarea = 0
    biggest = np.array([])
    for cnt in contours:
        area = cv2.contourArea(cnt)  
        print("Area: ", area)
        if area>5000:
            peri= cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            if area>maxarea and len(approx)==4:
                biggest = approx
        
    print("Biggest", biggest)        
    print("Biggest Shape", biggest.shape)
    cv2.drawContours(contour_img, biggest, -1, (255, 255, 0), 3)
    
    return biggest
        
        

def reorder(mypoints):
    mypoints = mypoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2), np.int32)
    
    add = mypoints.sum(1)
    print('add',add)
    
    myPointsNew[0] = mypoints[np.argmin(add)]
    myPointsNew[3] = mypoints[np.argmax(add)]
    diff = np.diff(mypoints, axis=1)
    myPointsNew[1] = mypoints[np.argmin(diff)]
    myPointsNew[2] = mypoints[np.argmax(diff)]
    print('new Points', myPointsNew)
    
    return myPointsNew





def wrap(image, biggest):
    biggest = reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv2.warpPerspective(image, matrix, (width, height))
    imgCropped = imgOutput[0:imgOutput.shape[0]-10,20:imgOutput.shape[1]-10]
    imgCropped = cv2.resize(imgCropped, (width,height))
    return imgCropped
    



image = cv2.imread('./Images/documentscanner2.jpg')
contour_img = image.copy()

preprocess_image = preprocess_image(image)

biggest = draw_contours(preprocess_image)

wrap = wrap(image, biggest)

print('output img shape:', wrap.shape)
cv2.imshow("original", image)
cv2.imshow("Preprocessed", preprocess_image)
cv2.imshow("Final Output", wrap)


cv2.waitKey(0)

cv1.destroyAllWindows()