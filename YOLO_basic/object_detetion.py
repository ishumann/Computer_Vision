import cv2

cap = cv2.VideoCapture(0)

if (cap.isOpened()=="False"):
    print("Error Reading the Video")
    
    
frame_width = int(cap.get(3))
frame_width = int(cap.get(4))

output = cv2.VideoWriter("outputs.avi", cv2.VideoWriter_fourcc("M","J", "P", "G") , 10 ,(frame_width, frame_width))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        resize_frame = cv2.resize(frame, (0,0), fx=0.6, interpolation=cv2.INTER_AREA)
        
        output.write(frame)
        cv2.imshow("Frame", resize_frame)
        
        
        
                         
                        