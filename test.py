import json
import pandas as pd
import requests


def get_image(SEARCH_TERM):
    API_KEY = "AIzaSyAHrKsi_x2oDvOtorOWIgJfJS-F7sbST_I"
    SEARCH_ENGINE_ID = "c2cfb4d8340e14562"
    URL = "https://www.googleapis.com/customsearch/v1"

    params = {
        "q": SEARCH_TERM,
        "key": API_KEY,
        "cx": SEARCH_ENGINE_ID,
        "searchType": "image",
    }

    response = requests.get(URL, params=params)
    data = response.json()['items']
    for item in data:
        print(item['link'])
    with open('data.json', 'w') as f:
        json.dump(data, f)
