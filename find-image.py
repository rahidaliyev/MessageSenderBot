import requests

def search_images(query, num_images=10):
    api_key = "67154d9a932e364f38574806f84ad72420c38229"
    search_engine_id = ""
    
    base_url = "https://www.googleapis.com/customsearch/v1"
    
    params = {
        "key": api_key,
        "cx": search_engine_id,
        "q": query,
        "searchType": "image",
        "num": num_images
        
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        image_links = [item["link"] for item in data.get("items", [])]
        return image_links
    else:
        print("Error:", response.status_code)
        return []

search_query = "beautiful landscapes"
image_links = search_images(search_query)

for i, link in enumerate(image_links, start=1):
    print(f"Image {i}: {link}")