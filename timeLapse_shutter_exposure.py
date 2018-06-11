from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()
camera.shutter_speed = 6000000

#camera.shutter_speed = camera.exposure_speed 
camera.resolution= (1640, 1232)
fecha=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

#sleep(90)


for filename in camera.capture_continuous('/home/pi/drone/imagenes/timelapse/img{counter:03d}'+fecha+'.jpg'):
    print('Captured %s' % filename)
    sleep(2) # wait 2 seconds
