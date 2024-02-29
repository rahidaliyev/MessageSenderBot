import requests


def get_image(SEARCH_TERM):
    # Replace 'Your_Pixabay_API_Key' with your actual Pixabay API key
    API_KEY = "AIzaSyAHrKsi_x2oDvOtorOWIgJfJS-F7sbST_I"
    SEARCH_ENGINE_ID = "c2cfb4d8340e14562"
    # SEARCH_TERM = ''  # Change 'nature' to whatever you wish to search for
    URL = "https://www.googleapis.com/customsearch/v1"

    # Parameters for the API request
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
