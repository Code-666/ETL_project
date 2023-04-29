import requests
import pandas as pd
import json

#response = requests.get('https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16.158/lat/58.5812/data.json')

def extract(response):

    data = response.json()

    with open("data.json", "w") as outfile:
        json.dump(data, outfile)

with open('data.json', 'r') as f:
    data = json.load(f)

def transform(data_index):
    big_df = []
    test = {}

    test['Date'] = data['timeSeries'][data_index]['validTime']

    for i in data['timeSeries'][data_index]['parameters']:
        if i['name'] == 't':
            test['Temperature'] = i['values'][0]

    for i in data['timeSeries'][data_index]['parameters']:
        if i['name'] == 'msl':
            test['Air pressure'] = i['values'][0]

    for i in data['timeSeries'][data_index]['parameters']:
        if i['name'] == 'pcat':
            test['Precipitation'] = i['values'][0]

    big_df.append(test)
    return pd.DataFrame(big_df)

big_df = []
for i in range(len(data['timeSeries'])):
    print(i)
    df = transform(i)
    big_df.append(df)

new_df = pd.concat(big_df, ignore_index=True)
new_df.to_csv('test.csv')
