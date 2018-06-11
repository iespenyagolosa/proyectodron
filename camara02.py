from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (2592, 1944)
camera.framerate = 15
#camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/camara/imagenes/image01.jpg')
#camera.stop_preview()
