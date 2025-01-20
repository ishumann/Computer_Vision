import cv2
from ultralytics import YOLO


cap = cv2.VideoCapture("./Videos/1.mp4")

model = YOLO('yolov8n.pt')


if (cap.isOpened()=="False"):
    print("Error Reading the video")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))


output = cv2.VideoWriter(
    "output.avi",
    cv2.VideoWriter_fourcc('M','J' ,'P', 'G'),
    # -1,
    10,
    (frame_width, frame_height)
)

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret:
        #object Detections using YOLOv8, frame by frame
        #stream = True, # it will be using generator and it is more efficient than the normal
        
        
        results = model(frame, stream=True)
        
        for r in results:
            boxes = r.boxes

            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                print(x1, y1, x2, y2)
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame,(x1,y1),(x2,y2), (0,255,0),3)
            
            
        resize_frame = cv2.resize(frame, (0,0), fx=0.6, fy=0.6,interpolation=cv2.INTER_AREA)
        output.write(frame)
        cv2.imshow('frame', resize_frame) 
    
        if cv2.waitKey(1) & 0xff == ord("q"):
            break


output.release()
cap.release()
cv2.destroyAllWindows()
