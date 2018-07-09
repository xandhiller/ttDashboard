import pandas as pd
import datetime as dt
import logging

# Logging config:
logging.basicConfig(level=logging.CRITICAL, format= ' %(asctime)s - %(levelname)s - %(message)s')

# Necessary info for currency conversion
tt_currencies = ['USD', 'PHP', 'ZAR', 'AUD']
currency_data_filepath = './currency2.json'

def api_call(currencies):
    logging.info('Running api_call function.')
    link = 'https://free.currencyconverterapi.com/api/v5/convert?q=USD_PHP,PHP_USD&compact=ultra&date=2018-07-01&endDate=2018-07-08'
    link = link.split('&')
    link[0] = link[0].split(sep='?')
    link_base = link[0][0]
    currency = link[0][1].split(',')
    joiner = '&'
    today = pd.to_datetime('today')
    latest_day = today - pd.to_timedelta('7 days')
    latest_day = str(latest_day).split()[0]
    today = str(today).split()[0]
    url_array = []
    for i in range(len(tt_currencies)-1):
        for j in range(1, len(tt_currencies)-i):
            path = link_base + '?q=' + tt_currencies[i] + '_' + tt_currencies[i+j] + ',' + tt_currencies[i+j] + '_' + tt_currencies[i] + joiner + link[1] + joiner + 'date=' + latest_day + joiner + 'endDate=' + today
            url_array.append(path)
    logging.info('Array of URLs to pull from is:' + str(url_array))
    df_= pd.DataFrame()
    for i in range(len(url_array)):
        data = pd.read_json(url_array[i])
        # Transpose for proper formatting
        data = data.T
        df_ = df_.append(data)
    logging.info('Data frame after iterative api call is:' + str(df_))
    # Transpose for proper date logic below and indexing later on
    df_ = df_.T
    logging.info('Data frame after transposition is:' + str(df_))
    return df_

def getCurrencyData():
    # if there is no data, make a file and download the api
    # If the file has the same date as today in it, then don't read the new data from the API
    try:
        df = pd.read_json(currency_data_filepath)
    except:
        df = pd.DataFrame({'dummy':[0,0]})
        df.to_json(currency_data_filepath)

    today = pd.to_datetime('today')
    most_recent_data_date = df.index[-1]

    links = []
    if today != most_recent_data_date:
        df = api_call(tt_currencies)
        try:
            df.to_json(currency_data_filepath)
        except:
            logging.warning('Data did not successfully save locally.')

    else:
        logging.info('Program logic determined that the currency data stored locally is current to today.')

    logging.info('Retrieved currency conversion rates are as follows:' + str(df))
    return df
