#ContourTest

import numpy as np
import cv2


cap = cv2.VideoCapture(1)

while(True):
	#Capture frame-by-frame
	ret, frame = cap.read()
	
	h, w = img.shape[:2]
	
	_, contours0, hierarchy = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	contours = [cv2.approxPolyDP(cnt, 3, True) for cnt in contours0]
	
	def update(levels):
		vis = np.zeros((h, w, 3), np.uint8)
		levels = levels - 3
		cv2.drawContours(vis, contours, (-1, 2)[levels <= 0], (128, 255, 255), 3, cv2.LINE_AA, hierarchy, abs(levels))
		cv2.imshow('contours', vis)
		
	update(3)
	cv2.createTrackbar("levels+3", "contours", 3, 7, update)
	cv2.imshow('image', img)
	if cv2.waitKey(5) & 0xFF == 27:
		break
		
cap.release()
cv2.destroyAllWindows()
