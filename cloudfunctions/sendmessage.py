import requests
import json

def send_message():
    url = "https://us-central1-mypubsubproject0709.cloudfunctions.net/cloudfunction-pubsub"
    data = {
         'seasonName': 'Winter',
            'temperature': '0 degrees',
            'startMonth' : 'December'
    }
    headers = {'Content-type' : 'application/json', Accept : 'text/plain'}
    req = requests.post(url, data=json.dumps(data), headers=headers)
    print(f'req = {req}')


if __name__ == '__main__':
    send_message()
    