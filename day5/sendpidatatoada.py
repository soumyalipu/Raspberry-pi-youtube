#send raspbery pi text data to adafruit io
from Adafruit_IO import *
ADAFRUIT_IO_USERNAME = "soumya1234"
ADAFRUIT_IO_KEY = "f59655943a284c748e2d6b9576cf691e"
aio=Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
test=aio.feeds('text')
data=aio.send('text',"Hello World1")
print(test)
print(data)