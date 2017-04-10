import maestro
import time

vert=4
horz=1

################################################################3

servos=maestro.Controller()
servos.setSpeed(vert, 4)
servos.setSpeed(horz, 4)
servos.setAccel(vert, 1)
servos.setAccel(horz, 1)

servos.setTarget(vert, 6000)
servos.setTarget(horz, 6400)
