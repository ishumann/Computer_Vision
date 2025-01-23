import cv2
from ultralytics import YOLO
import math

cap = cv2.VideoCapture('./Videos/video1.mp4')
model = YOLO("yolov8n.pt")
coco_classes = [
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "airplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis"]
center_points = []

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
output = cv2.VideoWriter(
    "output.avi", cv2.VideoWriter_fourcc(*"XVID"), 23.98, (frame_width, frame_height)
)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Object detections using YOLOv8, frame by frame
    results = model(frame, stream=True)

    # Flatten the list of boxes from all results
    boxes = [box for r in results for box in r.boxes]

    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        print(x1, y1, x2, y2)
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        cx = int((x1+x2)/2)
        cy = int((y1+y2)/2)
        center_points.append((cx,cy))
        cv2.rectangle(frame,(x1,y1),(x2,y2), (0,255,0),3)
        conf = math.ceil((box.conf[0]*100))/100
        cls = int(box.cls[0])
        class_name = coco_classes[cls]
        label = f'{class_name}{conf}'
        text_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
        c2 = x1+text_size[0],y1-text_size[1]-3
        cv2.rectangle(frame, (x1, y1), c2, [255,0,0], -1, cv2.LINE_AA)
        cv2.putText(frame, label, (x1, y1-2), 0,1,[255,255,255], thickness=1, lineType=cv2.LINE_AA)
        for pt in center_points:
            cv2.circle(frame, pt, 2, (0,255,0), -1)

    resize_frame = cv2.resize(
        frame, (0, 0), fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA
    )
    output.write(frame)
    cv2.imshow("frame", resize_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

output.release()
cap.release()
cv2.destroyAllWindows()
