import cv2

cap=cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

cap.set(0, 150)
while True:
    success, frame = cap.read()
    print("Frame", frame.shape)
    if success:
        cv2.imshow("Output", frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

qq