import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)#GPIO.BCM
GPIO.setup(3,GPIO.OUT)#for defining pin as output
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

while 1:
    GPIO.output(3,1) #turning on led
    time.sleep(1) #1 second delay
    GPIO.output(5,1) #turnng of led
    time.sleep(1)
    GPIO.output(7,1) #turnng of led
    time.sleep(1)
    GPIO.output(7,0) #turnng of led
    time.sleep(1)
    GPIO.output(5,0) #turnng of led
    time.sleep(1)
    GPIO.output(3,0) #turnng of led
    time.sleep(1)
