import adafruit_dht
from board import *
import time
import requests


URL='https://api.thingspeak.com/update?api_key=8NDT4518NSNNIYTG&field2='
dht_device = adafruit_dht.DHT11(23)
def dhtdata():
    temperature = dht_device.temperature
    humidity = dht_device.humidity
    print(f"Humidity= {humidity:.2f}")
    print(f"Temperature= {temperature:.2f}°C")
    newURL=URL+str(temperature)+'&field3='+str(humidity)
    return newURL
while 1:
    newurl1=dhtdata()
    r=requests.get(newurl1)
    print(r)
    time.sleep(15)