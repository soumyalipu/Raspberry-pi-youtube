import Adafruit_BMP.BMP085 as BMP085
import time
import requests

sensor = BMP085.BMP085()


while 1:
    print('XXXXXXXXXXXXXXXXXXXXXXXX....................XXXXXXXXXXXXXXXXXXXXXXX')
    print('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
    print('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
    print('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
    print('Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure()))
    altitudeData=sensor.read_altitude()
    pressureData=sensor.read_pressure()
    print('sending data to thingspeak')
    URL='https://api.thingspeak.com/update?api_key=RNNVFR2G0TVJYQX5&field4='+str(altitudeData)+'&field5='+str(pressureData)
    r=requests.get(URL)
    print(r)
    time.sleep(15)