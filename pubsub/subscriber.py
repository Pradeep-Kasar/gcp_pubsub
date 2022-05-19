import os 
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError

credentials_path = '/Users/Pradeep/VisualStudioCode/PubSub/mypubsubproject0709.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

subscriber = pubsub_v1.SubscriberClient()
subscriber_path = 'projects/mypubsubproject0709/subscriptions/myfirstpubsub-sub'

def callback(message):
    print(f'Received message: {message}')
    print(f'data: {message.data}')
    

    #if message.attributes():
    #     print("Attributes:")
    #     for key in message.attributes:
    #         value = message.attributes.get(key)
    #         print(f"{key} : {value}")

    message.ack()

subscriber_pull_data = subscriber.subscribe(subscriber_path, callback=callback)
print(f'Listening to message on {subscriber_path}')

with subscriber:
    try:
        subscriber_pull_data.result()
    except TimeoutError:
        subscriber_pull_data.cancel()
        subscriber_pull_data.result()
