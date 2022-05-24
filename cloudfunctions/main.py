from email import message, message_from_bytes
import json
import os
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
PROJECT_ID = os.getenv('mypubsubproject0709')

def four_seasons(request):
    data = request.data

    if data is None:
        print('request data is empty')
        return ('request data is empty', 400)

    print(f'request data: {data}')

    data_json = json.loads(data)
    print(f'json = {data_json}')

    season_name = data_json('seasonName')
    temperature = data_json('temperature')
    start_month = data_json('startMonth')

    print(f'season_name = {season_name}')
    print(f'temperature = {temperature}')
    print(f'start_month = {start_month}')

    # move the data to pubsub

    topic_path = 'projects/mypubsubproject0709/topics/cloudfunctionspubsub'

    message_json = json.dumps({
        'data': {'message' : 'four seasons !'},
        'seasons':{
            'seasonName': season_name,
            'temperature': temperature,
            'startMonth' : start_month
        }
    })
    message_bytes = message_json.encode('utf-8')

    try:
        publish_msg = publisher.publish(topic_path, data=message_bytes)
        publish_msg.result()
    except Exception as ex:
        print(ex)
        return (ex, 500)

    return ('Message received from Cloud Function and published in Pubsub', 200)

