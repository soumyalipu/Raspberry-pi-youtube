import adafruit_dht
from board import *
import time
from Adafruit_IO import *


dht_device = adafruit_dht.DHT11(23)
ADAFRUIT_IO_USERNAME = "soumya1234"
ADAFRUIT_IO_KEY = "f59655943a284c748e2d6b9576cf691e"
aio=Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)

# test=aio.feeds('text')
while 1:
    temperature = dht_device.temperature
    humidity = dht_device.humidity
    data=aio.send('temp',temperature)
    data1=aio.send('humi',humidity)
    print(data)
    time.sleep(5)