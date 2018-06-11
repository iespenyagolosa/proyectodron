from picamera import PiCamera
from time import sleep
from datetime import datetime

camara = PiCamera(resolution=(1640, 1232), framerate=30)
# Inicializamos el valor ISO 
# 100 and 200 are reasonable values for daytime, while 400 and 800 are better for low light
camara.iso = 100

# Esperamos a que se establezca el control automático de la ganancia
sleep(2)

# Ahora fijamos los valores
# Para poner un valor razonable de shutter_speed, consultamos el valor de exposure_speed
camara.shutter_speed = camara.exposure_speed
#print (camara.exposure_speed)
# Para fijar las ganancias de exposicón, apagamos el exposure_mode
camara.exposure_mode = 'off'
# Valores de BlancosNegros analógicos
g = camara.awb_gains
camara.awb_mode = 'off'
camara.awb_gains = g

#camara.sensor_mode=2
#camara.framerate=0.1
#camara.shutter_speed = 33116
#camara.resolution= (3280, 2464)
#camara.resolution= (1640, 1232)
fecha=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

sleep(180)


for filename in camara.capture_continuous('/home/pi/drone/imagenes/timelapse/img{counter:03d}'+fecha+'.jpg'):
    print('Captured %s' % filename)
    sleep(4) # espera 4 segundos


