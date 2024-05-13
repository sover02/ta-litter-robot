import ConfigParser
import requests
import calendar
import time
import json
import os

state_file  = os.path.dirname(os.path.realpath(__file__)) + "/state"

config = ConfigParser.ConfigParser()
config.read(state_file)
last_update = config.get('activity', 'last_update')

headers = { 'x-api-key' : config.get('auth', 'x-api-key') }
params = { 'limit' : 200 }

url_base = 'https://muvnkjeut7.execute-api.us-east-1.amazonaws.com/'
activity_endpoint = config.get('auth', 'endpoint')
url = url_base + activity_endpoint

activities = json.loads(requests.get(url, headers=headers, params=params).text)['activities']

for activity in reversed(activities):
    event_time = calendar.timegm(time.strptime(activity['timestamp'], '%Y-%m-%dT%H:%M:%S.%f'))
    new_last_update = int(event_time)
    if int(event_time) > int(last_update):
        print json.dumps(activity, indent=4)

config.set('activity', 'last_update', new_last_update)
with open(state_file, 'wb') as configfile:
     config.write(configfile)

# fin
