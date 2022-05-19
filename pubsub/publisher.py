import os 
from google.cloud import pubsub_v1

credentials_path = '/Users/Pradeep/VisualStudioCode/PubSub/mypubsubproject0709.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/mypubsubproject0709/topics/myfirstpubsub'

data = 'set up pubsub using google client libaries and run the python code using Visual Studio Code'
data = data.encode('utf-8')

attributes = {
'country': 'USA',
'state': 'Colorado',
'city': 'Denver'
}

publish_data = publisher.publish(topic_path, data, **attributes)
print(f'published message id {publish_data.result()}')
