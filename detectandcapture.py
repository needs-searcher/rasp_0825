import RPi.GPIO as GPIO
import time
import smtplib, subprocess, datetime, time
from email.mime.text import MIMEText
import picamera

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from subprocess import call

camera=picamera.PiCamera()

camera.hflip=True
camera.vflip=True

GPIO.setmode(GPIO.BCM)
PIR = 12
LED = 21

GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

print("System Working")

SMTP_USERNAME='jh03130'
SMTP_PASSWORD='wngudslaxmrtn'
SMTP_RECIPIENT='jh03130@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SSL_PORT=465

while True:
    try:
        while True:
            if GPIO.input(PIR):
                print('Motion Detected')
                GPIO.output(LED,1)
                #camera capture
                call (["raspistill -o i1.jpg -w 640 -h 480 -t 0"], shell=True)
                print("Image Shot")
                p = subprocess.Popen(["runlevel"], stdout=subprocess.PIPE)
                
                #camera.capture('image_new.jpg')
                time.sleep(.1)
                GPIO.output(LED,0)
                #p=subprocess.Popen(["runlevel"], stdout=subprocess.PIPE)
                out, err=p.communicate()
                print("Connected to mail")
                TO=SMTP_RECIPIENT
                FROM=SMTP_USERNAME
                
                #create the container (outer) email message
                TO = SMTP_RECIPIENT
                FROM = SMTP_USERNAME
                msg = MIMEMultipart()
                msg.preamble = 'Rpi Sends image'
                
                #localtime=datetime.datetime.now()
                #strTime=localtime.strftime("%Y-%m-%d %H:%M")
                #msg = MIMEText('Motion Detected in RPi: '+strTime)
                #msg['Subject']='Raspi Noti'
                #msg['From']='jh03130@gmail.com'
                #msg['To']='jh03130@gmail.com'
                
                
                
                #attached image
                fp = open('i1.jpg', 'rb')
                img = MIMEImage(fp.read())
                fp.close()
                msg.attach(img)
                
                # Send the email via Gmail
                print("Sending the mail")
                server = smtplib.SMTP_SSL(SMTP_SERVER, SSL_PORT)
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
                server.sendmail(FROM, [TO], msg.as_string())
                server.quit()
                print("Mail sent")

            
    except IOError:
        print("Error")
    
    except KeyboardInterrupt:
        GPIO.output(LED, GPIO.LOW)
        GPIO.cleanup()
