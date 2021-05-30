# cognitive-text-python
Python code using Azure Cognitive Text Analytics on Twitter Feed, Stock Feed etc...
to extract key phrases, named entities, sentiment etc.

## Setup ##

#### Twitter Developer API Keys ###

Login to your Twitter account and go to the [Twitter Developer Page][twitter_api_keys] and get the Twitter API Key, API Key Secret, Access Token and Access Token Secret. You will need it to get Twitter Feed.  

#### Install Tweepy ####

Install the [tweepy python package][tweepy_pkg] in your python environment.

#### Marketstack API Keys ####

[Get a Marketstack API Key][marketstack_api_keys] to make API calls from python.

#### Install stocknews python package ####

Install the [stocknews python package][stocknews] in your python environment.

#### Setup an Azure Cognitive Service Instance ####

Create an [Azure subscription][azure] if do not have one already. You may want to ask the Azure administrator in your organization first.

Alternatively, you can create your own [free Azure subscription][azure_free] to test out.

Once you have your Azure Subscription, create an [Azure Cognitive Services resource][azure_cog] or check with your Azure adminstrator to create one for you. Once this created, get the key and endpoint from the Azure Portal under the "Keys and Endpoint" Menu under the Azur eCognitive Service resource.

![Azure Cognitive Service Page in Azure Portal](/images/azure_cog_properties.jpg)

#### Install Azure AI Text Analytics Python Packages ####

Install the [Azure AI Text Analytics python package][azure_text_analytics] in your python environment.

        > pip install azure-ai-textanalytics==5.1.0b7

## Run ##

The python code here has been tested with version 3.9.1 in Windows.

Before running any of the python code, from command line, set the following environment variables with the values of keys etc. you obtained from above.
```
set STOCK_NEWS_KEY=<YOUR MARKETSTACK API KEY>
set TWITTER_CONSUMER_KEY=<YOUR TWITTER CONSUMER KEY>
set TWITTER_CONSUMER_SECRET=<YOUR TWITTER CONSUMER SECRET>
set TWITTER_ACCESS_TOKEN_KEY=<YOUR TWITTER ACCESS TOKEN>
set TWITTER_ACCESS_TOKEN_SECRET=<YOUR TWITTER ACCESS TOKEN SECRET>
set COGNITIVE_SERVICE_KEY=<YOUR AZURE COGNITIVE SERVICE KEY>
set COGNITIVE_SERVICE_ENDPOINT=https://<YOUR AZURE COGNITIVE SERVICE NAME>.cognitiveservices.azure.com/
```

In order to get end of day stock market information of a ticker symbol and also to get twitter feed on a search string and then feed it to Azure Text Analytics APIs to extract key phrases, named entities, sentiment etc.. run this below -

	# Run text analytics on twitter feed
	> python ComputeCompanyScore.py -s TSLA -q "electric+car+chip" 

The output 
```
Date: 2021-05-28T00:00:00+0000, Name: Tesla Inc [TSLA], Open: 628.500000, High: 635.590000, Low: 622.380000, Closing: 625.220000, Volume: 22640034.000000

Search Twitter messages for electric+car+chip since 2020-05-13
        Tweet -> RT @NetDec: Find out more about the latest AI-driven Navy Submarine powered by an Nvidia chip and electric car battery. Is this the beginni…
        Tweet -> Find out more about the latest AI-driven Navy Submarine powered by an Nvidia chip and electric car battery. Is this… https://t.co/9WxSirayfb
        Tweet -> Chip shortage will hit electric car production https://t.co/ujU0NBAXFv
        Tweet -> @jimcramer Nah. Chip shortage is going to crush their delivery for the next year. Their share price is going to get… https://t.co/P4VjtvtjLB
        Tweet -> @Jchaps03 @The_Left_Prince @ElonLovesUs @Lunnaris01 @SenSanders Yeah Elon having control would be such a bad thing!… https://t.co/66aOnOGXAE

Key Phrases:
         ['Nvidia chip', 'latest AI-driven Navy Submarine', 'electric car battery', 'RT', 'NetDec', 'beginni']

Named Entities:
        Text:    Nvidia
        Category:        Organization   SubCategory:     None   Confidence Score:        0.54

Document Sentiment: neutral

Overall scores: positive=0.06; neutral=0.90; negative=0.04

```
[azure_text_analytics]: <https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/quickstarts/client-libraries-rest-api?tabs=version-3-1&pivots=programming-language-python>
[azure_cog]: <https://docs.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account?tabs=multiservice%2Cwindows>
[azure_free]: <https://azure.microsoft.com/en-us/free/>
[azure]: <https://docs.microsoft.com/en-us/azure/cost-management-billing/manage/create-subscription#create-a-subscription-in-the-azure-portal>
[stocknews]: <https://pypi.org/project/stocknews/>
[marketstack_api_keys]: <https://marketstack.com/signup>
[tweepy_pkg]: <https://docs.tweepy.org/en/latest/install.html>
[twitter_api_keys]: <https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api>

