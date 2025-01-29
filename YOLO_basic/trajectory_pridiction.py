import cv2
from kalmanfilter import KalmanFilter


kf = KalmanFilter()

ball_positions = [
    (50, 100),
    (100, 100),
    (100, 100),
    (150, 100),
    (200, 100),
    (250, 100),
    (300, 100),
    (450, 150),
    (500, 200),
]

img = cv2.imread("./Images/image2.jpg")


for pt in ball_positions:
    cv2.circle(img, pt, 15, (255,0,0),-1)
    predicted = kf.predict(pt[0], pt[1])
    print(predicted)
    cv2.circle(img, predicted, 15, (0,255,0), 5)

# prdicted = kf.predict()

predicted1 = kf.predict(predicted[0], predicted[1])
cv2.circle(img, predicted1, 15, (0,255,0), 5)
for i in range(10):
    
    predicted = kf.predict(predicted[0], predicted[1])
    cv2.circle(img, predicted, 15, (0,255,0), 5)


cv2.imshow('Images', img)

cv2.waitKey(0)
