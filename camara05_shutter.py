from picamera import PiCamera
from time import sleep
from datetime import datetime
from gpiozero import Button

rele = Button(17,pull_up=False) #donde tenemos conectado el relé de la APM
camara = PiCamera()
camara.shutter_speed=6000000
fecha=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

imagen = 1
while True:
    try:
        rele.wait_for_press()
        sleep(2)
        camara.capture('/home/pi/drone/imagen%03d' % imagen + fecha +'.jpg')
        imagen += 1
    except KeyboardInterrupt:
        break
