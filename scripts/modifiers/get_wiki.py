import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import requests

def search_wiki(query):
    url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={query}&utf8=&format=json"
    res = requests.get(url).json()
    if res['query']['search']:
        title = res['query']['search'][0]['title']
        print(f"Found title: {title}")
        img_url = f"https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&format=json&pithumbsize=1000"
        img_res = requests.get(img_url).json()
        pages = img_res['query']['pages']
        for p in pages:
            if 'thumbnail' in pages[p]:
                return pages[p]['thumbnail']['source']
    return None

print("Brain:", search_wiki("Artificial neural network"))
print("Crossroads:", search_wiki("Crossroads"))
print("Graph:", search_wiki("Network theory"))
