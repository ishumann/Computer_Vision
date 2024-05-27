import cv2
import numpy as np

width=940
height=680
def preprocess_image(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imageCanny = cv2.Canny(image_gray, 450, 600)
    kernel = np.ones((5,5), np.uint8)
    image_dilation = cv2.dilate(imageCanny, kernel, iterations=2)
    image_erosion = cv2.erode(image_dilation, kernel, iterations=1)
    return image_erosion

def draw_contours(image):
    contours, hirearchy = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    maxarea=0
    biggest=np.array([])
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print("Area", area)
        if area> 5000:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            if area>maxarea and len(approx)==4:
                biggest=approx
    print("Biggest", biggest)
    print("Biggest Shape", biggest.shape)
    cv2.drawContours(image_contours, biggest, -1, (255,0,0), 3)

    return biggest

def reorder(myPoints):
    myPoints=myPoints.reshape((4,2))
    myPointsNew=np.zeros((4,1,2), np.int32)

    add=myPoints.sum(1)
    print("add", add)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    print("New Points", myPointsNew)

    return myPointsNew




def warp_perscpective(img, biggest):
    biggest=reorder(biggest)
    pts1=np.float32(biggest)
    pts2=np.float32([[0,0], [width,0], [0, height], [width, height]])
    matrix=cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))
    imgCropped=imgOutput[0:imgOutput.shape[0]-10, 20:imgOutput.shape[1]-10]
    imgCropped=cv2.resize(imgCropped, (width, height))
    return imgCropped



image = cv2.imread("./opencv_basic/Images/documentscanner2.jpg")
#image_resize=cv2.resize(image, (640, 480))
image_contours = image.copy()
preprocessed_image=preprocess_image(image)

biggest = draw_contours(preprocessed_image)

imgWraped = warp_perscpective(image, biggest)
print("Output Image", imgWraped.shape)
cv2.imshow("Input Image", image)
cv2.imshow("Preprocessed Image", preprocessed_image)
cv2.imshow("Output Image", imgWraped)
cv2.waitKey(0)

cv2.destroyAllWindows()