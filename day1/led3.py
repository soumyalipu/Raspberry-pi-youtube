import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)#GPIO.BCM
GPIO.setup(3,GPIO.OUT)#for defining pin as output
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.output(5,0) #turning on led
GPIO.output(3,0) #turning on led
GPIO.output(7,0) #turning on led
while 1:
    x=input("enter the pin you want to turn on")
    print(x)
    if x=='1':
        GPIO.output(3,1) #turning on led
        GPIO.output(5,0) #turning on led
        GPIO.output(7,0) #turning on led
        print("1 st led is on")
    elif x=='2':
        GPIO.output(5,1) #turning on led
        GPIO.output(3,0) #turning on led
        GPIO.output(7,0) #turning on led
        print("2 st led is on")
    elif x=='3':
        GPIO.output(5,0) #turning on led
        GPIO.output(3,0) #turning on led
        GPIO.output(7,1) #turning on led
        print("3 st led is on")
    else:
        GPIO.output(5,0) #turning on led
        GPIO.output(3,0) #turning on led
        GPIO.output(7,0) #turning on led
        print("poweroff")