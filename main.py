import numpy as np
import cv2

cap = cv2.VideoCapture('./video/video2.mp4')

width = int(cap.get(3))
height = int(cap.get(4))

frame_rate = 30.0

out = cv2.VideoWriter('./video/hasil2.mp4', cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (width, height))

while True:
    ret, frame = cap.read()

    if not ret: break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    

    upperThres = np.array([60,255,255])
    lowerThres = np.array([0,95,0])

    mask = cv2.inRange(hsv, lowerThres, upperThres)

    result = cv2.bitwise_and(frame,frame, mask=mask)

    out.write(result)
    cv2.imshow("frame", result)
    cv2.imshow("mask", mask)
    

    if cv2.waitKey(1) == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()