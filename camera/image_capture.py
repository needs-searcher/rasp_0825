import picamera
import time

camera=picamera.PiCamera()

camera.hflip=True
camera.vflip=True

camera.start_preview()
time.sleep(1)
camera.stop_preview()

camera.capture('image.jpg')