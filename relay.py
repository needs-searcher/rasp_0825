import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relay=18
GPIO.setup(relay, GPIO.OUT)

GPIO.output(relay, 1)
time.sleep(5)
GPIO.output(relay, 0)