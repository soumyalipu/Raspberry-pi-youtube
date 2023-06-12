import adafruit_dht
from board import *
import time
from pushbullet import Pushbullet

pb = Pushbullet("o.KStpFExkqaYAtAGrQKJdBgASc2mFBvDe")
dht_device = adafruit_dht.DHT11(23)

while 1:
    temperature = dht_device.temperature
    humidity = dht_device.humidity
    if temperature>=28:
        push=pb.push_note("Tempereture is more than 28", str(temperature))
        print(push)
    if temperature<=27:
        push=pb.push_note("Tempereture is less than 28", str(temperature))
        print(push)
    time.sleep(5)
    