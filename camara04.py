from picamera import PiCamera
from time import sleep
from gpiozero import InputDevice

rele = InputDevice(17) #donde tenemos conectado el relé de la APM
camara = PiCamera()

#camara.start_preview()
imagen = 1
while True:
    try:
        if (rele.pull_up):
            print("Activo")
            #camara.capture('/home/pi/Desktop/camara/imagenes/imagen%03d.jpg' % imagen)
            imagen += 1
    except KeyboardInterrupt:
 #       camara.stop_preview()
        break
