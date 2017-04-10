import numpy as np
import imutils
import cv2
import serial
import maestro
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

#Define bounds of color
Lower = (0, 0, 255)
Upper = (167, 17, 255)

#Define Servo Channels
vert=4
horz=1

#Center of Manipulator
cvert=1500
chorz=1600

#Define PID Gains
P=1
I=1 
D=1

def InitServos():
	'''scontrol = serial.Serial('/dev/ttyACM0')
	#init vertical servo
	scontrol.write(b 0x84, 0x04, 0x70, 0x2E) 
	#init horizontal servo
	scontrol.write(b 0x84, 0x01, 0x00, 0x19)'''
	servos = maestro.Controller() #InitServoController
	servos.setSpeed(vert, 16) #Limit Speeds to 1.5us/10milliseconds
	servos.setSpeed(horz, 16)
	servos.setAccel(vert, 2)
	servos.setAccel(horz, 2)
	servos.setRange(vert, 5200, 6800)
	servos.setRange(horz, 5600, 7200)
	servos.setTarget(vert, 6000) #Set vertical position to 1500us
	servos.setTarget(horz, 6400) #Set horizontal position to 1600us
	return(servos)
	
def MakeTargetCommand(target):
	command = target*4 #Command to servo = target*4
	return command


def SetTargetsCommand(horzcommand, vertcommand, servos):
	servos.setTarget(vert, vertcommand) #set vertical servo
	servos.setTarget(horz, horzcommand) #set horizontal servo


def InitCam():
	#initialize camera
	camera = cv2.VideoCapture(1)
	camera.set(3,640) #Set resolution to 320x240
	camera.set(4,480)
	camera.set(5, 90)
	return(camera)

def FindCenter(camera):
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
		#draw circle and centroid on frame
		cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
		cv2.circle(frame, center, 5, (0, 255, 0), -1)
	#print(center)
	return (center,frame)

def FindTarget(center, servos):
	dxPix = (center[0] - 320) #determine horizontal distance from center in pixels
	if dxPix<=15 and dxPix>=-15:
		dxPix = 0
	xCurrent = servos.getPosition(horz)/4 #get current position in us
	tx = xCurrent + 1.167*(dxPix/2) #targetX = current + 1.167[us/pixel]*pixelDistance
	
	dyPix = (center[1] - 240) #determine vertical distance from center in pixels
	if dyPix<=15 and dyPix>=-15:
		dyPix=0
	yCurrent = servos.getPosition(vert)/4 #get current position in us
	ty = yCurrent + 1.119*(dyPix/3) #targetY = current + 1.119[us/pixel]*pixelDistance
	
	return(int(tx), int(ty))
	


######################################################################

camera = InitCam()
servos = InitServos()
center=(320,240)
ccent=(320,240)
'''
i = 0

dx = []
dy = []
count = []
'''

while True:
	(center,frame) = FindCenter(camera)
	cv2.rectangle(frame, (305,225), (335,255), (0,0,255),2)
	if center != None:
		(tx, ty) = FindTarget(center, servos)
		#print(tx, ty)
		cx = MakeTargetCommand(tx)
		cy = MakeTargetCommand(ty)
		SetTargetsCommand(cx, cy, servos)
		ccent = center
	else:
		(tx, ty) = FindTarget(ccent, servos)
		cx = MakeTargetCommand(tx)
		cy = MakeTargetCommand(ty)
		SetTargetsCommand(cx, cy, servos)
	cv2.imshow("Frame", frame)

'''	
	dx.append(tx)
	#print(dx[i])

	dy.append(ty)
	#print(dx[i])

	count.append(i)
	#print(dx[i])

	i += 1
'''

	#wait for 'esc' key
	if cv2.waitKey(5) & 0xFF == 27:
		break
'''
f=open("dx Data1", "w+")
f.write("%s,%s" %(dx, count))
f.close()
g=open("dy Data1", "w+")
g.write("%s,%s" %(dy, count))
g.close()
'''


#release camera and close windows
camera.release()
cv2.destroyAllWindows()



