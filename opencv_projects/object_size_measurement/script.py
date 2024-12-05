import cv2
import numpy as np

# step 1 : read the image
image = cv2.imread('./Images/object_size_5.jpeg')
scale = 3
width = 210 * scale
height = 297 * scale


# step 2: Create a function to convert to img to gray
# apply gaussian blur
# canny edge detector
# dilation
# erosion



def preprocessing_image(image):
    gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    # cv2.imshow('img', gray)
    imageBlur = cv2.GaussianBlur(gray, (5, 5), 1)
    lower_threshold = 100
    upper_threshold = 100
    
    # apply canny edge edge detector
    canny_edge = cv2.Canny(imageBlur, lower_threshold, upper_threshold)
    kernel = np.ones((5,5), np.uint8)
    
    # applying dilation
    dilation = cv2.dilate(canny_edge, kernel, iterations=3)
    
    # applying erosion

    erosion = cv2.erode(dilation, kernel, iterations=2)
    return erosion



def find_draw_contours(pre_img):
    contours, hirearchy = cv2.findContours(preprocessed_image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        cv2.drawContours(original_image_copy, cnt, -1,(0,255,0),3)
        area = cv2.contourArea(cnt)
        print('area for each of the contour in the image: {area}')
    return original_image_copy


def get_contours(preprocessed_image, draw_image, minArea=1000, filter=4, draw = False):
    contours, hirearchy = cv2.findContours(preprocessed_image.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    print('length of the Contours', len(contours))
    finalContours=[]
    for cnt in contours:
        # cv2.drawContours(original_image_copy, cnt, -1, (0,255,0),3)
        area = cv2.contourArea(cnt)
        print(f'Area for each of the contour in the image:{area}') 
        if area > minArea:
            peri = cv2.arcLength(cnt, True)
            approx  = cv2.approxPolyDP(cnt, 0.02+peri, True)
            bbox = cv2.boundingRect(approx)
            if filter > 0:
                if len(approx) == filter:
                    finalContours.append([len(approx), area, approx, bbox, cnt])
                else:
                    finalContours.append([len(approx),area, approx, bbox, cnt])
                    
        finalContours = sorted(finalContours, key = lambda x:x[1], reverse=True)
        
        if draw:  
            for cont in finalContours:
                cv2.drawContours(draw_image, cont[4], -1 , (0,0,255),2)        
    return draw_image, finalContours


def warp_image(image, points, width,height):
    # points = reorder(points)
    pts1  = np.float32(points)
    pts2 = np.float32([[0, 0], [width, 0], [height, 0], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imageWrap = cv2.wrapPerspective(image, matrix, (width,height))
    return imageWrap
     
     
      
      
image = cv2.resize(image, (0,0), None, 0.2, 0.2)
pre_img = preprocessing_image(image)
original_image_copy = image.copy()
original_image_copy_two = image.copy()

preprocessed_image = preprocessing_image(image)
draw_contours = find_draw_contours(preprocessed_image)

contour_area, finalContours = get_contours(preprocessed_image, original_image_copy_two, minArea= 1000, draw=True)



if len(finalContours) != 0:
    biggest = finalContours[0][2]
    warp_image_one = warp_image(image,biggest, width, height)


cv2.imshow('Input Image', image)
cv2.imshow('preprocessed Image', pre_img)
cv2.imshow('find and Draw Contours', draw_contours)
cv2.imshow('Get Contours', contour_area)
# cv2.imshow('Warped Image One', warp_image_one)
cv2.waitKey(0)


