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

def displayTextAnalytics(documents):
    client = authenticate_client()
    key_phrases = get_key_phrases(client, documents)
    print("Key Phrases:")
    phrase_list = []
    for phrase in key_phrases:
        phrase_list.append(phrase)
    print("\t", phrase_list)

    result = get_named_entities(client, documents)
    print("Named Entities:")
    if (not result.entities):
        print("\tNot found")
    else:
        for entity in result.entities:
            if entity.category == 'Organization':
                print("\tText: \t", entity.text, "\n\tCategory: \t", entity.category, "\tSubCategory: \t", entity.subcategory,
                    "\tConfidence Score: \t", round(entity.confidence_score, 2)) #"\tLength: \t", entity.length, "\tOffset: \t", entity.offset)

    sentiments = get_sentiments(client, documents)
    if (not sentiments):  
        print("Sentiments not found")
    else:
        print("Document Sentiment: {}".format(sentiments.sentiment))
        print("Overall scores: positive={0:.2f}; neutral={1:.2f}; negative={2:.2f} \n".format(
            sentiments.confidence_scores.positive,
            sentiments.confidence_scores.neutral,
            sentiments.confidence_scores.negative,
        ))
