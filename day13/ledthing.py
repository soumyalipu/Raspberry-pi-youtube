import requests
import time
import json
while 1:
    # print('Reading data from thingspeak')
    URL='https://api.thingspeak.com/channels/1873271/fields/6.json?api_key=2JRIHZLS3N9Q34D4&results=1'
    data=requests.get(URL).json()
    feeds_data=data['feeds']
    new_data=json.dumps(feeds_data)
    final_data=json.loads(new_data)
    # print(new_data)
    for item in final_data:
        # print(item['field6'])
        led_status=item['field6']
    if led_status == '1':
        print('Turn on Led')
    else:
        print('led is off')
    
    
    time.sleep(15)