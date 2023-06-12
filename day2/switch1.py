import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3,GPIO.OUT)
while 1:
    x=GPIO.input(5)
    if x==0:
        GPIO.output(3,1)
        print("Button Pressed")
    else:
        GPIO.output(3,0)
        print("Button Release")
   