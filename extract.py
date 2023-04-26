import requests
import pandas as pd

data = requests.get('https://dmigw.govcloud.dk/v1/forecastdata/collections/wam_dw/items?api-key=')

print(data.json())

