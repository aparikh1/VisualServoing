#VideoCaptureTest

import numpy as np
import cv2


cap = cv2.VideoCapture(1)

while(True):
	#Capture frame-by-frame
	ret, frame = cap.read()
	
	#Display frame
	cv2.imshow('frame',frame)
	if cv2.waitKey(5) & 0xFF == 27:
		break
	
cap.release()
cv2.destroyAllWindows()
