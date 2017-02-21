#RectangleFinder
#Find rectangles representing ports and their centers

#COMPLETED:
#1. found thresholds for edge detection

#TO DO
#1. Find contours in edged (binary) image
#2. Determine areas of countours
#3. Determine focal length of camera
#4. Determine pixel width and height (area) of ports from focal length of camera and actual width and height
#5. Throw out contours with areas not similar to area of ports
#6. Find centers of contours with areas similar to area of ports
#7. Compare centers with center of numbers
#8. Desired rectangle has center near center of number

import imutils
import numpy as np
import cv2

def nothing(*arg):
	pass
	
#define width and height (area) of ports in pixels
width=36
height=26
area=width*height
minArea=area-20
maxArea=area+20

#initialize vector of similar area contours
simArea=None

#initialize camera
camera = cv2.VideoCapture(1)
camera.set(3, 320)
camera.set(4,240)

#keep looping
while True:
	#grab current frame
	ret, image = camera.read()
	
	#convert image to grayscale, blur it
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.bilateralFilter(gray, 11, 17, 17)
	
	#Find edges
	edged = cv2.Canny(gray, 54, 90)
	#show edged image
	cv2.imshow("edged", edged)

	#show frame
	cv2.imshow("Image", image)
	#cv2.imshow("Mask", mask)

	#wait for 'esc' key
	if cv2.waitKey(5) & 0xFF == 27:
		break
	
#release camera and close windows
camera.release()
cv2.destroyAllWindows()
