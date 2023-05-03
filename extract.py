import requests
import pandas as pd
import json
from sqlalchemy import create_engine, text

response = requests.get('https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/16.158/lat/58.5812/data.json')

def extract(response):

    data = response.json()

    with open("stations/raw/raw_data.json", "w") as outfile:
        json.dump(data, outfile)

extract(response)