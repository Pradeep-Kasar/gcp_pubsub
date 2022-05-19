# gcp_pubsub : set up pubsub using google client libaries and run the python code using VS Code

Prerequisites :
    1. Visual Studio Code. 
    2. Google pubsub Client Libraries
    3. Python extension in VS Code. 
    
Steps in Google Cloud Console : 

    1. Open Google Cloud Console. 
    2. Create a project
    3. Create a service account and assign the role as "Pub Sub Admin" OR  you can also assign the "Pubsub Publisher" and "Pubsub Subscriber" role.
    4. go to the service account, under keys tab click on add key, create a new key with key type as JSON. This JSON key file will be downloaded on your          local machine
    5. Enable Pubsub API
    6. Go to PubSub and create a topic. By default the system should create an Subscription as well with extension as "-sub" to your topic, if not then     
       create one. 

On your computer :
    1. Create a folder in VS code named Pubsub. 
    2. Install google pubsub libraries in the pubsub folder using VS code terminal or system terminal.
    3. Add the service account key to the folder. 
    4. Create a python file and copy the code from publisher.py
    5. Replace the service account key path "credentials_path"
    5. on the google console page, go to pubsub--> topic, copy the topic name and replace it in the VS code for the variable "topic_path"
    6. Create a python file and copy the code from subscriber.py
    7. Replace the service account key path "credentials_path"
    8. on the google console page, go to pubsub--> subscription, copy the topic name and replace it in the VS code for the variable "subscriber_path"
    
Execute the code.
    1. Run the subscriber.py file, which should display message as "Listening...."
    2. Now Run the pusblisher.py file. It will return the publisher ID
    3. On Google Console page, go to pubsub --> topic --> messages --> click pull, you shoud be able to see the message present in the "data" variable in 
       publisher.py file.
    3. The subscriber.py file should display the message that is part of "data" variable in pusblisher.py file. 
    
    
    NOTE: I have added attributes to the publisher.py file, but for some reason the code fails when i try to display those attributes as part of subscriber output. I have commented the code.
   
