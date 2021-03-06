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
print(minArea, maxArea)


#initialize camera
camera = cv2.VideoCapture(1)
camera.set(3, 320)
camera.set(4,240)

#keep looping
#while True:
#grab current frame
ret, image = camera.read()

simArea=(0,0)

#convert image to grayscale, blur it
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)

#Find edges
edged = cv2.Canny(gray, 54, 90)
#show edged image
cv2.imshow("edged", edged)

#Find contours and cmopute hierarchy between them
_, cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(len(cnts))
count=0
#loop over contours and make vector of contours with area similar to port area
for c in cnts:
	area=cv2.contourArea(c)
	if area<maxArea and area>minArea:
		simArea=np.append((simArea, c), 0)
		count=count+1
		print(area)
print(count)
print(len(simArea))
	#show frame
	#cv2.imshow("Image", image)
	#cv2.imshow("Mask", mask)

	#wait for 'esc' key
	#if cv2.waitKey(5) & 0xFF == 27:
	#break
	
#release camera and close windows
camera.release()
cv2.destroyAllWindows()
