import numpy as np
import imutils
import cv2

#Define bounds of color
Lower = (107, 195, 26)
Upper = (121, 255, 156)

#initialize camera
camera = cv2.VideoCapture(1)
camera.set(3, 320)
camera.set(4,240)

#keep looping
while True:
	#grab current frame
	ret, frame = camera.read()
	
	#Blur frame and convert to HSV color space
	blurred = cv2.GaussianBlur(frame, (11,11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	#Make bitmask for color, the dilate and erod to remove small blobs left in mask
	mask = cv2.inRange(hsv, Lower, Upper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	
	#Find contours in bitmasked image
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None
	
	#only proceed if at least one contour found
	if len(cnts)>0:
		#find largest contour in bitmasked image, and compute its minimum enclosing circle and centroid
		c = max(cnts, key=cv2.contourArea)
		((x,y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
		print (radius)
		
		#draw circle and centroid on frame
		cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
		cv2.circle(frame, center, 5, (0, 0, 255), -1)
		
		
		
	#show frame
	cv2.imshow("Frame", frame)
	#cv2.imshow("Mask", mask)

	#wait for 'esc' key
	if cv2.waitKey(5) & 0xFF == 27:
		break
		
#release camera and close windows
camera.release()
cv2.destroyAllWindows()
