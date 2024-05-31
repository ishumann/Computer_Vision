
import cv2
import numpy as np
from pyzbar.pyzbar import decode


cap = cv2.VideoCapture('e:\Github\Computer_Vision\Videos\QRCodeVideo.mp4')
with open('E:/Github/Computer_Vision/resources/mydata.txt') as f:
       my_datalist = f.read().splitlines()
       print('My Approved Data', my_datalist)
count = 0
while True:
       ret, frame = cap.read()
       if ret:
              print(f'frame count: {count}')
              frame = cv2.resize(frame, (0,0), None, 0.2,0.2)
              for code in decode(frame):
                     my_data= code.data.decode('utf-8')
                     # print(my_data)
                     if my_data in my_datalist:
                            output = "Authorized"
                            color = (0,255,0)
                     else:
                            output = "Un-Authorized"
                            color = (0,0,255)
                     pts = np.array([code.polygon],np.int32)
                     pts = pts.reshape((-1,1,2))
                     cv2.polylines(frame,[pts], True, (255,0,0),2)
                     pts2 = code.rect
                     cv2.putText(
                         frame, output, (pts2[0], pts2[1]-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, color, 1)
              # cv2.imshow('frame', frame)
              count+=1       
              if cv2.waitKey(0) & 0xFF == ord('1'):
                     break
cap.release()
cv2.destroyAllWindows()


