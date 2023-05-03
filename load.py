import pandas as pd
from sqlalchemy import create_engine, text

def load():
    engine = create_engine('postgresql://postgres:johnsdata1@localhost:5432/weather')

    df = pd.read_csv('stations/harmonized/harmonized_data.csv')

    df.to_sql('weather', engine, if_exists='replace', index=False)

    with engine.connect() as connection:
        result = connection.execute(text("select * from weather"))
        for row in result:
            print(row)

    engine.dispose()

load()