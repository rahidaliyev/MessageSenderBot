import json
import random
import pandas as pd
import requests
from ImageVM import ImageVM
from main import send_message
global link 

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
    list = []
    response = requests.get(URL, params=params)
    data = response.json()['items']
    for item in data:
        image_vm_object = ImageVM(
            kind=item['kind'],
            title=item['title'],
            link=item['link'],
            displayLink=item['displayLink'],
            fileFormat=item['fileFormat']
        )
        list.append(image_vm_object)
    link = random.choice(list).link
    print(link)
    send_message(link)
             
        
    
 
    
