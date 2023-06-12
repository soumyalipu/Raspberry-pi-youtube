from Adafruit_IO import *
ADAFRUIT_IO_USERNAME = "soumya1234"
ADAFRUIT_IO_KEY = "f59655943a284c748e2d6b9576cf691e"
aio=Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
test=aio.feeds('led')
print(test)
while 1:
    data = aio.receive(test.key)
    print(data.value)
   
