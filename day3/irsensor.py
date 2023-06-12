import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
while 1:
    x=GPIO.input(5)
    # print(x)
    if x==0:
        print("object detect")
        GPIO.output(3,1)
    else:
        print("object not found")
        GPIO.output(3,0)