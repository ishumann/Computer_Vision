import cv2
import numpy as np

def lanedetection(video_path):
    '''
    this function is to find the lane cordinates on the video
    '''
    cap = cv2.VideoCapture(video_path)
    
    ret, frame = cap.read()
    
    # step 1: select the ROI
    
    roi = cv2.selectROI('select Area', frame)
    
    # step 2: Crop the area

    frame_copy = frame.copy()
    roi_area = frame_copy[int(roi[1]): int(
        roi[1] + roi[3]),  int(roi[0]) : int(roi[0] + roi[2])]

    # dilation
    
    kernel = np.array((3,3), np.uint8)
    
    dilate = cv2.dilate(roi_area, kernel, iterations=1)
    
    # step 3 : gray scale image
    
    gray_scale = cv2.cvtColor(dilate, cv2.COLOR_BGR2GRAY)
    
    # step 4 : threshold the Gray Scale Image to detect only white Colors
    
    mask = cv2.inRange(gray_scale, 215, 255)   
    
    bitwise_and = cv2.bitwise_and(gray_scale, gray_scale,mask=mask)
    
    # step 7: applying threshold
    
    thresh, gray = cv2.threshold(bitwise_and, 150, 255, cv2.THRESH_BINARY)
    
    # step 8  find the lane line using canny edge detector
    
    canny_edge = cv2.Canny(gray, 0.3*thresh,thresh)
    
    
    # step 9 apply the Hough transform
    
    
    lane_lines = cv2.HoughLinesP(canny_edge,2,np.pi/180,30, minLineLength=15,maxLineGap=40)
    
    return lane_lines,roi    
    
    


if __name__ == "__main__":
    video_path = './Videos/1.mp4'

    
    cap = cv2.VideoCapture(video_path)
    lines, r = lanedetection(video_path)
    print(lines, r)
    while True:
        ret, frame = cap.read()
        if ret:
            if lines is not None:
                for line in lines:
                    x1, y1, x2,y2 = line[0]
                    cv2.line(frame,(x1+r[0],y1+r[1]),(x2+r[0],y2+r[1]),(0,255,0),3,)
            cv2.imshow('Input Video',frame)   
        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cap.release() 
cv2.destroyAllWindows()

