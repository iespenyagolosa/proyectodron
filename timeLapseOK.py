from time import sleep
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
camera.resolution = (3280, 2464)

fecha=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

sleep(180) # wait 3 minutes for the drone to set up
for filename in camera.capture_continuous('/home/pi/drone/imagenes/timelapse/img{counter:03d}'+fecha+'.jpg'):
    print('Captured %s' % filename)
    sleep(2) # wait 2 seconds

