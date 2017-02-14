#HoughCircleTest

from __future__ import print_function

import cv2
import numpy as np

import sys

cap = cv2.VideoCapture(1)

while(True):
	#Capture frame-by-frame
	ret, src = cap.read()
	
	#Convert to grayscale
	img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
	
	#Blur image
	img = cv2.medianBlur(img, 5)
	cimg = src.copy()
	
	#Run Hough Transform
	circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 100, 30, 1, 30)
	
	if circles is not None:
		circles = np.round(circles[0,:]).astype("int")
		
		for (x, y, r) in circles:
			cv2.circle(cimg, (x, y), r, (0, 0, 255), 4)	#edge of circle
			cv2.circle(cimg, (x, y), 2, (0, 255, 0), 1) #center of circle
			#cv2.imshow("source", src)
			cv2.imshow("detected circles", cimg)
			print(x, y)
			
			
	if cv2.waitKey(5) & 0xFF == 27:
		break
		
cap.release()
cv2.destroyAllWindows()
