import numpy as np

import pandas as pd

import requests

data=requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=AMZN&apikey=NPSUYHEF4CQO62UT")

parsed_data=data.json()

print(type(parsed_data))

print(parsed_data)

dailydata=pd.read_csv("AMZN.csv")

print(dailydata)

print(type("dailydata"))

dailydata.sort_values("Open")

dailydata.head()
print(dailydata)

dailydata.info()

dailydata.sort_values("Volume")

print(dailydata.columns)

print(dailydata.sort_values("Volume"))
print(dailydata.sort_values("Volume" , ascending=False))

print(dailydata.duplicated())

print(dailydata.duplicated(subset=["Volume"]))

print(dailydata.isnull())

print(dailydata.isna())

print(dailydata.isna().sum())
print(type(parsed_data))

newdata=pd.read_csv("AMZN new.csv")
print(newdata)

joined_data=dailydata.merge(newdata, on= 'Volume')
print(joined_data)

newdataform=pd.read_csv("AMZN new 2.csv")
print(newdataform)

latest_data=newdataform[newdataform["Date"] > "2020-09-23"]
print(latest_data)

joined_numbers=dailydata.merge(latest_data, on='Date')
print(joined_numbers)

df_row=pd.concat([dailydata, newdataform])
print(df_row)

df_row_reindex = pd.concat([dailydata, newdataform], ignore_index=True)
print(df_row_reindex)

print(df_row_reindex.sort_values("Date"))

print(df_row_reindex.drop_duplicates(subset=['Date']))