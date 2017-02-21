#VideoCaptureTest

import numpy as np
import cv2

#initialize Window
cv2.namedWindow('image')	

cap = cv2.VideoCapture(1)
cap.set(3, 320)
cap.set(4, 240)

while(True):
	#Capture frame-by-frame
	ret, frame = cap.read()
	cv2.rectangle(frame, (260, 137), (296,163), (0, 0, 255), 2)
	cv2.rectangle(frame, (260, 72), (281,88), (0, 0, 255), 2)
	#Display frame
	cv2.imshow('image',frame)
	if cv2.waitKey(5) & 0xFF == 27:
		break
	
cap.release()
cv2.destroyAllWindows()
