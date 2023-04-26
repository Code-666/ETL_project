import requests
import pandas as pd

data = requests.get('https://dmigw.govcloud.dk/v1/forecastdata/collections/wam_dw/items?api-key=2e9d4a28-6ea9-4ffd-8575-d4f4e5599175')

print(data.json())

