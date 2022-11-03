import numpy as np
import pandas as pd
import requests
import csv

url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

try:
    response = requests.request("GET", url, headers=headers, data={})
    json_file = response.json()
    #print(json_file)
    emptydata = []
    for i in json_file['data']:
        emptydata.append([i['ID Nation'], i['Nation'], i['Year'], i['Population'], i['Slug Nation']])
    df = pd.DataFrame(emptydata, columns=['ID Nation','Nation', 'Year', 'Population', 'Slug Nation'])
    print(df)
    df.to_csv('C://Users//chaithra.chandru//Desktop//Use Cases//tasks//population.csv')

except Exception as error:
    print(error)