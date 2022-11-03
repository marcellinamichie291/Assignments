#!/usr/bin/env python
# coding: utf-8

# # Cryptocurrency API

# In[2]:


import numpy as np
import pandas as pd
import requests
import csv

url = 'https://api.coincap.io/v2/assets'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data={})

json_file = response.json()
#print(json_file)

emptydata = []

csvheader = ['ID', 'Symbol', 'Name', 'Price(USD)']

for i in json_file['data']:
    emptydata.append([i['id'], i['symbol'], i['name'], i['priceUsd']])

crypto_table = pd.DataFrame(emptydata, columns=['ID','Symbol', 'Name', 'Price(USD)'])
print(crypto_table)

crypto_table.to_csv('C://Users//chaithra.chandru//Desktop//crypto_csv.csv')


# # List of Public APIs

# In[3]:


import numpy as np
import pandas as pd
import requests
import csv

url = 'https://api.publicapis.org/entries'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data={})

json_file = response.json()
#print(json_file)

emptydata = []

csvheader = ['API', 'Auth', 'HTTPS', 'Cors', 'Category']

for i in json_file['entries']:
    emptydata.append([i['API'], i['Auth'], i['HTTPS'], i['Cors'], i['Category']])

df = pd.DataFrame(emptydata, columns=['API', 'Auth', 'HTTPS', 'Cors', 'Category'])
print(df)

df.to_csv('C://Users//chaithra.chandru//Desktop//apis_csv.csv')


# # US Population API

# In[4]:


import numpy as np
import pandas as pd
import requests
import csv

url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data={})

json_file = response.json()
#print(json_file)

emptydata = []


csvheader = ['ID Nation','Nation', 'Year', 'Population', 'Slug Nation']

for i in json_file['data']:
    emptydata.append([i['ID Nation'], i['Nation'], i['Year'], i['Population'], i['Slug Nation']])

df = pd.DataFrame(emptydata, columns=['ID Nation','Nation', 'Year', 'Population', 'Slug Nation'])
print(df)

df.to_csv('C://Users//chaithra.chandru//Desktop//population_csv.csv')


# # YouTube API

# In[5]:


import requests
import pandas as pd
import time

API_KEY='AIzaSyBQ-tAo1B8iOppBSIVnqVKTYMZ2SoZT7_Q'

Channel_Id='UCW8Ews7tdKKkBT6GdtQaXvQ'

pageToken=""
url="https://www.googleapis.com/youtube/v3/search?key="+API_KEY+"&channelId="+Channel_Id+"&part=snippet,id&order=date&maxResults=10000"+pageToken
response = requests.get(url).json()

#response['items'][0]

#video_id=response['items'][0]['id']['videoId']
#video_id
#video_title=response['items'][0]['snippet']['title']
#video_title = str(video_title).replace("&amp;","")
#video_title
#upload_date=response['items'][0]['snippet']['publishedAt']
#upload_date = str(upload_date).split("T")[0]
#upload_date

data=[]
for video in response['items']:
    if video['id']['kind'] == 'youtube#video':
        video_id = video['id']['videoId']
        video_title=video['snippet']['title']
        video_title = str(video_title).replace("&amp;","")
        upload_date=video['snippet']['publishedAt']
        upload_date = str(upload_date).split("T")[0]
        #print(video_id)
        #print(video_title)
        #print(upload_date)
        data.append([video_id, video_title, upload_date])
df=pd.DataFrame(data, columns=['Video ID', 'Video Title', 'Upload Date'])
print(df)
df.to_csv('C://Users//chaithra.chandru//Desktop//youtube_csv.csv')


# In[ ]:




