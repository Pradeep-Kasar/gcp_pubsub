from google.cloud import bigquery
import os

credentials_path = '/Users/Pradeep/VisualStudioCode/python-bq/python-bq-sa.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id = 'mypubsubproject0709.myfirstbqds.USAStates'

insert_data =[
    {u'State':'Colorado', u'Capital':'Denver', u'Zipcode': 80203, u'Timezone':'MST'},
    {u'State':'California', u'Capital':'Sacramento', u'Zipcode': 123286, u'Timezone':'PST'},
    {u'State':'Vermont', u'Capital':'Montpelier', u'Zipcode': 50609, u'Timezone':'EST'},
]

errors = client.insert_rows_json(table_id, insert_data)
if errors == []:
    print('New rows Inserted')
else:
    print(f'Error inserting data: {errors}')