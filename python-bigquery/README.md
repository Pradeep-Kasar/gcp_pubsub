# gcp_pubsub : set up pubsub using google client libaries and run the python code using VS Code

Prerequisites :
    1. Visual Studio Code. 
    2. Google pubsub Client Libraries 
    3. Python extension in VS Code. 
    4. Google Cloud Free Account.
    
Steps in Google Cloud Console : 

    1. Open Google Cloud Console. 
    2. Create a project
    3. Create a service account and assign the role as Bigquery Admin.
    4. go to the service account, under keys tab click on add key, create a new key with key type as JSON. This JSON key file will be downloaded on your          local machine
    5. Go to Bigquery
          Create dataset under your project. 
          Create table under the dataset. 
          I have created a table with columns as State (string), Capital (string), Zipcode (INT), Timezone (string). 

On your computer :
    1. Create a folder in VS code named python-bigquery. 
    2. Install google pubsub libraries in the pubsub folder using VS code terminal or system terminal.
            pip install --upgrade google-cloud
            pip install --upgrade google-cloud-bigquery
            pip install --upgrade google-cloud-storage
    3. Add the service account key to the folder. 
    4. Create a python file and copy the code from insert_data.py
    5. Replace the service account key path "credentials_path"
    6. on the google console page, go to bigquery table that was created earlier, under preview tab you should be able to find the tableid.
    7. Copy the table id and replace in the code where the variable table_id is set. 
    
Execute the code.
    1. Run the inser_data.py file, if the data is inserted successfully, you should find the message as "New Rows inserted", else the error should display on your terminal
    2. Go to bigquery table and you should be able to find the rows inserted. 
   

