#FindEdgeThreshold
#Determine thresholds for Canny edge detector for finding edges of ports
import imutils
import numpy as np
import cv2
import sys

def nothing(*arg):
	pass

#initialize window
cv2.namedWindow('edge')
cv2.createTrackbar('thrs1', 'edge', 2000, 5000, nothing)
cv2.createTrackbar('thrs2', 'edge', 4000, 5000, nothing)

#initialize camera
camera = cv2.VideoCapture(1)
#camera.set(3, 320)
#camera.set(4,240)
#314,700
#keep looping
while True:
	#grab current frame
	ret, image = camera.read()
	
	#convert image to grayscale, blur it
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.bilateralFilter(gray, 11, 17, 17)
	
	#retrieve thresholds
	thrs1 = cv2.getTrackbarPos('thrs1', 'edge')
	thrs2 = cv2.getTrackbarPos('thrs2', 'edge')
	
	#Find edges
	edged = cv2.Canny(gray, thrs1, thrs2)
	
	#show edged image
	cv2.imshow("edge", edged)
	
	#show frame
	#cv2.imshow("Image", image)
	#cv2.imshow("Mask", mask)

	#wait for 'esc' key
	if cv2.waitKey(5) & 0xFF == 27:
		break
	
#release camera and close windows
camera.release()
cv2.destroyAllWindows()
