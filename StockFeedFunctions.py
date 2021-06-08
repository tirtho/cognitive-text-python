
from logging import exception
import os
# Stock Feed package
from stocknews import StockNews
import requests

def getStockFeed(ticker_symbol):
    stockNewsKey = os.getenv("STOCK_NEWS_KEY")
    endpoint = 'http://api.marketstack.com/v1/tickers/'
    params = {
        'access_key': stockNewsKey
    }

    #ticker_symbol = 'FLR'
    url = endpoint + ticker_symbol + '/eod'
    api_result = requests.get(url, params)
    api_response = api_result.json()
    #print(api_response)
    try:
        symbol = api_response['data']['symbol']
        organization_name = api_response['data']['name']
        open_val = api_response['data']['eod'][0]['open']
        high_val = api_response['data']['eod'][0]['high']
        low_val = api_response['data']['eod'][0]['low']
        close_val = api_response['data']['eod'][0]['close']
        volume_val = api_response['data']['eod'][0]['volume']
        date_val = api_response['data']['eod'][0]['date']
        #print('Date: ' + date_val + ', Name: ' + organization_name + '[' + symbol + ']' + ', O/H/L/C/V: ', open_val, high_val, low_val, close_val, volume_val)
        return 'Date: %s, Name: %s [%s], Open: %f, High: %f, Low: %f, Closing: %f, Volume: %f' % (date_val, organization_name, symbol, open_val, high_val, low_val, close_val, volume_val)
    except:
        print("Error getting End of Day Stock information for " + ticker_symbol)
        return

