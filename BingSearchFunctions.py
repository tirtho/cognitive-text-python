import os
import requests
import json
from requests.exceptions import HTTPError

key = os.getenv("BING_SEARCH_KEY")
endpoint = os.getenv("BING_SEARCH_ENDPOINT")

def getSearchResults(queryString):
    headers = {"Ocp-Apim-Subscription-Key" : key}
    # All parameters are here - https://docs.microsoft.com/en-us/bing/search-apis/bing-news-search/reference/query-parameters
    params  = {"q": queryString, "setLang": "en-US", "count": 5}

    # Check if any error in response
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        newsJson = response.json()
        newsBodies = []
        for value in newsJson["value"]:
            newsBodies.append(value["description"])
        return True, newsBodies
    except Exception as e:
        print(e)
        return False, ""