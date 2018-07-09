import pandas as pd
# import datetime as dt
# date_test = pd.to_datetime('today')
# print(str(date_test))
# # If it exists, open the file, if it doesn't call the API and save the data to a file
#
# # Check if it's the same day as when the API was previously called.
#
# # Take in the data as a pandas dataframe
#
# # Attempt to read all, if fail read old data
# df = pd.read_json('https://free.currencyconverterapi.com/api/v5/convert?q=USD_PHP,PHP_USD&compact=ultra&date=2018-07-01&endDate=2018-07-08')
#
# df.keys()
#
# print((df.index[-1]))
#
# if df.index[-1] == date_test:
#     print('True')
#
# df.to_json('./currency.json')
# pd.DataFrame = {}
#
# df2 = pd.read_json('./currency.json')
#
# df2
#
# # USD
# # EURO
# # ZAR
# # KWACHA
# # MAURITIUS RUPEES
# # ARYARI MADAGASCAR
# # CONGO CENTRAL AFRICAN FRANC
# # AUD

# df = pd.read_json('./currency.json')
# print(str(df.index[-1]))

# print(today)
# print(latest_day)
#
# tt_currencies = ['USD', 'PHP']
#
# for i in range(len(tt_currencies)):
#     print(i)

# df = pd.read_json('./currency2.json')
# print(df)
# print(df.index)
# df = df.T
# print(df)
# print(df.index)
# df.to_json('./currency2.json')

from currencyData import *

data = getCurrencyData()
# print('Data in currencyScratchpad0 is: \n' + str(data))

print(str(data.columns[0]))
