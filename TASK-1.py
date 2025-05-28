pip install requests matplotlib seaborn pandas
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
# Configure
API_KEY = "9c034daa8cec67966dce937d5b1c4d8d"
CITY = "New York"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
# Fetch data
response = requests.get(URL)
data = response.json()
# Check for errors
if data.get("cod") != "200":
    print("Error fetching data:", data.get("message"))
    exit()
# Process data
forecast_list = data['list']
weather_data = {
    "datetime": [datetime.fromtimestamp(item['dt']) for item in forecast_list],
    "temperature": [item['main']['temp'] for item in forecast_list],
    "humidity": [item['main']['humidity'] for item in forecast_list],
    "weather": [item['weather'][0]['description'] for item in forecast_list]
}
df = pd.DataFrame(weather_data)
# Plotting
plt.figure(figsize=(12, 6))
sns.lineplot(x='datetime', y='temperature', data=df, label='Temperature (°C)', marker='o')
sns.lineplot(x='datetime', y='humidity', data=df, label='Humidity (%)', marker='x')
plt.title(f'5-Day Weather Forecast for {CITY}')
plt.xlabel('Date and Time')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
# Show plot
plt.show()
