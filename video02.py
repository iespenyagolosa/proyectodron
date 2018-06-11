from picamera import PiCamera
from time import sleep

camera = picamera.PiCamera(resolution=(3280, 2464))

sleep(90)


for filename in camera.record_sequence(
        '/home/pi/drone/videos/video%d.h264' % i for i in range(1, 300)):
    camera.wait_recording(20)
