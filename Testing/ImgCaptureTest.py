#VideoCaptureTest

import numpy as np
import cv2


cap = cv2.VideoCapture(1)

#Capture frame-by-frame
ret, frame = cap.read()

cv2.imwrite(testimg, frame)

cap.release()
cv2.destroyAllWindows()
