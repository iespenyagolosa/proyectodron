from picamera import PiCamera
from time import sleep
from datetime import datetime
from gpiozero import Button

camara = PiCamera()
fecha=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

sleep(90)

camara.start_recording('/home/pi/drone/videos/video'+fecha+'.h264')
sleep(300)
camara.stop_recording()



