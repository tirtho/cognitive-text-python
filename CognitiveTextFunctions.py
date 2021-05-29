import os
import sys

key = os.getenv("COGNITIVE_SERVICE_KEY")
endpoint = os.getenv("COGNITIVE_SERVICE_ENDPOINT")

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

def get_sentiments(client, documents):
    return client.analyze_sentiment(documents=documents)[0]

def get_language(client, documents):
    try:
        return client.detect_language(documents = documents, country_hint = 'us')[0]
    except Exception as err:
        print("Encountered exception. {}".format(err))
        exit

def get_named_entities(client, documents):

    try:
        return client.recognize_entities(documents = documents)[0]
    except Exception as err:
        print("Encountered exception. {}".format(err))
    exit

def get_key_phrases(client, documents):

    try:
        response = client.extract_key_phrases(documents = documents)[0]
        
        if not response.is_error:
            return response.key_phrases
        else:
            print(response.id, response.error)
            return ""
    except Exception as err:
        print("Encountered exception. {}".format(err))
        exit
