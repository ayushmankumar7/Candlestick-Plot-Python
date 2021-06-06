from matplotlib.pyplot import title
import requests
import json
import pandas as pd
import mplfinance as mpl 


start_date = "2021-04-25"
end_date = "2021-06-06"
freq = "1DAY"
coin = "XRP"

url = f'https://rest.coinapi.io/v1/exchangerate/{coin}/USD/history?period_id={freq}&time_start={start_date}T00:00:00&time_end={end_date}T00:00:00'
headers = {'X-CoinAPI-Key' : 'PASTE       YOUR       API     KEY      HERE'}
response = requests.get(url, headers=headers)























# Convert to JSON
content = json.loads(response.text)
print(content)

# Convert JSON to Dataframe
df = pd.json_normalize(content)

# Change DType to DataTime
df.time_period_start = pd.to_datetime(df.time_period_start)

# Set time period start as Index
df = df.set_index("time_period_start")

# Remove unnecessary columns 
df.drop(['time_period_end', "time_open", "time_close"], axis=1, inplace=True)
print(df.columns)

# Change Column names to derised names
df.rename(columns={"rate_open": "Open", "rate_high":"High", "rate_low":"Low", "rate_close": "Close"}, inplace=True)
print(df)

# Final Plot
mpl.plot(
    df,
    type="candle", 
    mav =(3,6,9),
    title = f"{coin} Price",  
    style="yahoo"
    )



