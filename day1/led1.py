import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)#GPIO.BCM
GPIO.setup(3,GPIO.OUT)#for defining pin as output
while 1:
    GPIO.output(3,1) #turning on led
    print("Led is on")
    time.sleep(1) #1 second delay
    GPIO.output(3,0) #turnng of led
    print("led is off")
    time.sleep(1)
