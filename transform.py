import json
import pandas as pd

with open('stations/raw/raw_data.json', 'r') as f:
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
new_df.to_csv('stations/harmonized/harmonized_data.csv')