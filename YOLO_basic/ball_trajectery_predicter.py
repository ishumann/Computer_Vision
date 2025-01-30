import cv2
from ultralytics import YOLO
from kalmanfilter import KalmanFilter
import math

cap = cv2.VideoCapture("./Videos/demo1.mp4"
)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
kf = KalmanFilter()
output = cv2.VideoWriter(
    "output.avi", cv2.VideoWriter_fourcc(*"XVID"), 10, (frame_width, frame_height)
)

classNames = [
    "person",
    "bicycle",
    "car",
    "motorbike",
    "aeroplane",
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
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "sofa",
    "pottedplant",
    "bed",
    "diningtable",
    "toilet",
    "tvmonitor",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]
model = YOLO("./yolov8n.pt")


if not cap.isOpened():
    print("unable to read the file")


while (cap.isOpened()):
    ret, frame = cap.read()
    if  ret is False:
        break
    results = model(frame, stream=True) 

    for r in results:
        boxes = r.boxes
        for box in boxes:

            x1, y1, x2, y2 = box.xyxy[0]
            print(x1, y1, x2, y2)
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cx = int((x1+x2)/2)
            cy = int((y1+y2)/2)
            cv2.circle(frame, (cx,cy), 5, (0,0,255), -1)
            cv2.rectangle(frame, (x1, y1),(x2, y2),(255,0,0), 2)
            conf = math.ceil((box.conf[0]*100))/100
            cls = int(box.cls[0])
            class_name = classNames[cls]
            label = f'{class_name}{conf}'

            predicted = kf.predict(cx, cy)
            cv2.circle(frame, (predicted[0], predicted[1]), 10, (0, 255,0), -1)

    resize_frame = cv2.resize(
            frame, (0, 0), fx=0.4, fy=0.4, interpolation=cv2.INTER_AREA
        )
    output.write(resize_frame)
    cv2.imshow("output", resize_frame)

    if cv2.waitKey(1) & 0XFF== ord('q'):
        break

output.release()
cap.release()
cv2.destroyAllWindows()
