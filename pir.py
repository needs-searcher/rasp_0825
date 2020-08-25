import RPi.GPIO as GPIO
import time
import smtplib, subprocess, datetime, time
from email.mime.text import MIMEText

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
                time.sleep(.1)
                GPIO.output(LED,0)
                p=subprocess.Popen(["runlevel"], stdout=subprocess.PIPE)
                out, err=p.communicate()
                print("Connected to mail")
                TO=SMTP_RECIPIENT
                FROM=SMTP_USERNAME
                
                localtime=datetime.datetime.now()
                strTime=localtime.strftime("%Y-%m-%d %H:%M")
                msg = MIMEText('Motion Detected in RPi: '+strTime)
                msg['Subject']='Raspi Noti'
                msg['From']='jh03130@gmail.com'
                msg['To']='jh03130@gmail.com'
                
                print("Sending the mail")
                server = smtplib.SMTP_SSL(SMTP_SERVER, SSL_PORT)
                server.login(SMTP_USERNAME, SMTP_PASSWORD)
                server.send_message(msg)
                server.quit()
                print("Mail sent")
            
    except IOError:
        print("Error")