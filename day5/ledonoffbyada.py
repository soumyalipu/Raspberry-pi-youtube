import RPi.GPIO as GPIO
from Adafruit_IO import *
import time
ADAFRUIT_IO_USERNAME = "soumya1234"
ADAFRUIT_IO_KEY = "f59655943a284c748e2d6b9576cf691e"
aio=Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

test=aio.feeds('led')
# print(test)
while 1:
    data = aio.receive(test.key)
    print(data.value)
    if data.value == 'ON':
        GPIO.output(3,0)
        aio.send('text','LED is ON')
    if data.value == 'OFF':
        GPIO.output(3,1)
        aio.send('text','LED is OFF')
    time.sleep(5)