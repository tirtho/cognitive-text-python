from CognitiveTextFunctions import displayTextAnalytics
import os
from utils import *
from TwitterFeedFunctions import getTwitterFeed
from BingSearchFunctions import getSearchResults
from StockFeedFunctions import getStockFeed

# Stock Feed package
from stocknews import StockNews
import requests

# Twitter packages
import os
import tweepy as tw
import pandas as pd

# Get input args
if needHelp(False) == True:
    exit() 
status, searchString = getArgumentValue("-q", "--query")
if status == False:
    needHelp(True)
    exit()

status, ticker_symbol = getArgumentValue("-s", "--symbol")
# Asking code to retrieve stock market data, if symbol is passed
if status == True:
    stock_data = getStockFeed(ticker_symbol)
    if (not stock_data):
        print("No stock information available")
    else:
        print(stock_data)

# Get Twitter Feed for search string
documents = getTwitterFeed(searchString)

# Get Key Phrases from Twitter Feed
print("### Twitter Feed Insight ###")
displayTextAnalytics(documents)

# Get Bing News Feed
status, newsFeeds = getSearchResults(searchString)
if status == False:
    print("### No news found for bing search text: %s ###" %(searchString))
    exit()
print("### Bing Search Results Insight ###")
displayTextAnalytics(newsFeeds)
