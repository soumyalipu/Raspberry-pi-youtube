import adafruit_dht
from board import *
import time
dht_device = adafruit_dht.DHT11(23)

while 1:
    temperature = dht_device.temperature
    humidity = dht_device.humidity
    # print(f"Humidity= {humidity:.2f}")
    # print(f"Temperature= {temperature:.2f}°C")
    # time.sleep(.2)
    if temperature>=28:
        print("turn on alaram")
    if temperature<=27:
        print("alaram is off")