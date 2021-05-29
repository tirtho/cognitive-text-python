from StockFeed import get_stock_feed
import CognitiveTextFunctions as ctf
import os
from utils import *

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
status, twitterSearchString = getArgumentValue("-q", "--query")
if status == False:
    needHelp(True)
    exit()

status, ticker_symbol = getArgumentValue("-s", "--symbol")
# Asking code to retrieve stock market data, if symbol is passed
if status == True:
    stock_data = get_stock_feed(ticker_symbol)
    if (not stock_data):
        print("No stock information available")
    else:
        print(stock_data)


# Get Twitter feed for the Organization
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN_KEY")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#search_words = 'FLUOR+Corp+News'
search_words = twitterSearchString

date_since = "2020-05-13"
print("\nSearch Twitter messages for %s since %s" % (search_words, date_since))
# Collect tweets
tweets = tw.Cursor(api.search, q=search_words, lang="en", since=date_since).items(5)
# Iterate, create the document array for Azure Cog Text Analytics and also print tweets

documents = []
for tweet in tweets:
    documents.append(tweet.text)
    print("\tTweet -> " + tweet.text)

if (not documents):
    print ("No tweets found")
    exit()
# Get Key Phrases from Twitter Feed
client = ctf.authenticate_client()

#documents = ["My cat might need to see a veterinarian who lives in New York near the Chubb Insurance office."]
#documents = ["Here's How Microsoft Can Rally to All-Time Highs;Microsoft is pushing higher as the stock rotates to multi-week highs. Is the pattern setting up for another run at all-time highs? "]

key_phrases = ctf.get_key_phrases(client, documents)
print("\nKey Phrases:")
phrase_list = []
for phrase in key_phrases:
    phrase_list.append(phrase)
print("\t", phrase_list)

result = ctf.get_named_entities(client, documents)
print("\nNamed Entities:")
for entity in result.entities:
    if entity.category == 'Organization':
        print("\tText: \t", entity.text, "\n\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
            "\tConfidence Score: \t", round(entity.confidence_score, 2)) #"\tLength: \t", entity.length, "\tOffset: \t", entity.offset)

sentiments = ctf.get_sentiments(client, documents)
print("\nDocument Sentiment: {}".format(sentiments.sentiment))
print("\nOverall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
    sentiments.confidence_scores.positive,
    sentiments.confidence_scores.neutral,
    sentiments.confidence_scores.negative,
))