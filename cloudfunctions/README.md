Prequisites : 

# gcp_pubsub : calling pubsub service using cloud functions. 

Prerequisites :
    1. Development IDE with Python 3 or above installed. I am using VS code for my development purpose. 
    2. Access to Google Cloud Console
    2. Google pubsub Client Libraries
    
Steps in Google Cloud Console : 

    1. Open Google Cloud Console. 
    2. Create a project
    3. Create a service account and assign the role as "Pub Sub Admin" OR  you can also assign the "Pubsub Publisher" and "Pubsub Subscriber" role.
    4. go to the service account, under keys tab click on add key, create a new key with key type as JSON. This JSON key file will be downloaded on your          local machine
    5. Enable Pubsub API
    6. Go to PubSub and create a topic. By default the system should create an Subscription as well with extension as "-sub" to your topic, if not then     
       create one. 

On your computer :
    1. Create a folder in VS code named cf-ps. 
    2. Install google pubsub libraries in the pubsub folder using VS code terminal or system terminal.
    3. Add the service account key to the folder. 
    4. Create a python file and copy the code from main.py
    5. Replace the service account key path "credentials_path"
    5. on the google console page, go to pubsub--> topic, copy the topic name and replace it in the VS code for the variable "topic_path"
    6. Create a python file and copy the code from sendmessage.py
 
Cloud Function : 
    1. Go to Google Cloud Console. 
    2. Create an  cloud function with HTTP trigger and Allow unauthorized authentication ( for testing purpose only).
    3. click next --> select runtime as Python 3.10, copy the funtion from main.py to the online editor. make sure the entry point name and defination name is same else the cloud function creation will fail. In my case it have the entry point name as "four_seasons"
    4. Click Deploy.
    5. Once the cloud the function is created, go to triggers tab and copy the URL.
    6. Paste the url in send_message() ( variable name : url) 
   
    
Execute the code.
    1. Run the sendmessage.py file
    3. On Google Console page, cloud function, go to logs and you should see the data that has been set up as part of send_message() function. 
    
   
