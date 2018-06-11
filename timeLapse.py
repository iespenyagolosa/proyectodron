from picamera import PiCamera
from time import sleep
from datetime import datetime

camara = PiCamera()
camara.exposure_mode='off'
camara.sensor_mode=2
#camara.framerate=0.1
camara.shutter_speed = 33116
#camara.resolution= (3280, 2464)
camara.resolution= (1640, 1232)
fecha=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

sleep(180)


for filename in camara.capture_continuous('/home/pi/drone/imagenes/timelapse/img{counter:03d}'+fecha+'.jpg'):
    print('Captured %s' % filename)
    sleep(2) # wait 2 seconds
