import wiringpi2 as wpi

wpi.wiringPiSetupGpio()

command = [0x84, 0x01, 0x70, 0x2E]

servoController = wpi.serialOpen('/dev/ttySAC0', 115200)

if servoController<0:
	print('Serial opening error')

else:
	print('Serial connection opened!')
	print('Sending commands...')
	wpi.serialPutchar(servoController, command[0])
	wpi.serialPutchar(servoController, command[1])
	wpi.serialPutchar(servoController, command[2])
	wpi.serialPutchar(servoController, command[3])
	#wpi.serialPuts(servoController, command)
	print('Serial Commands sent')
	
