from picamera import PiCamera
from time import sleep
#from gpiozero import Button
import RPi.GPIO as GPIO
imagen = 1

camara = PiCamera()

GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


def hazFoto(channel):
	global imagen
	camara.capture('/home/pi/Desktop/camara/imagenes/imagen%03d.jpg' % imagen)
	imagen += 1
	time.sleep(1)

GPIO.add_event_detect(17, GPIO.RISING, callback=hazFoto)  # add rising edge detection on a channel


while True:
	try:
		if GPIO.input(17):
			time.sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()
	break
