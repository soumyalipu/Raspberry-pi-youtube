import requests
import time
import random
while 1:
    print('sending data to thingspeak')
    data=random.randint(0,200)
    URL='https://api.thingspeak.com/update?api_key=8NDT4518NSNNIYTG&field1='+str(data)
    r=requests.get(URL)
    print(r)
    time.sleep(15)