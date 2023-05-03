import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('stations/harmonized/harmonized_data.csv')

df['Date'] = pd.to_datetime(df['Date'])

temps = df['Temperature']

plt.plot(df['Date'], temps)

plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Data')

plt.show()

