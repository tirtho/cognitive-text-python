import os
import tweepy as tw
import pandas as pd

def getTwitterFeed(searchString):
    # Get Twitter feed for the Organization
    consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN_KEY")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    date_since = "2020-05-13"
    print("\nSearch Twitter messages for %s since %s" % (searchString, date_since))
    # Collect tweets
    tweets = tw.Cursor(api.search, q=searchString, lang="en", since=date_since).items(5)
    # Iterate, create the document array for Azure Cog Text Analytics and also print tweets

    listOfTweets = []
    for tweet in tweets:
        listOfTweets.append(tweet.text)
        print("\tTweet -> " + tweet.text)

    if (not listOfTweets):
        print ("No tweets found")
        exit()
    
    return listOfTweets