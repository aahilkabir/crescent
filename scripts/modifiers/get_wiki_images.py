import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import requests
from duckduckgo_search import DDGS

def search_ddg_with_retries(query):
    for i in range(3):
        try:
            with DDGS() as ddgs:
                results = list(ddgs.images(query, max_results=3))
                if results:
                    return results[0]['image']
        except Exception as e:
            pass
    return None

def get_wiki_image(title):
    try:
        url = f'https://en.wikipedia.org/w/api.php?action=query&titles={title}&prop=pageimages&format=json&pithumbsize=1000'
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).json()
        pages = res['query']['pages']
        for page_id in pages:
            if 'thumbnail' in pages[page_id]:
                return pages[page_id]['thumbnail']['source']
    except Exception as e:
        print(f"Error fetching wiki image for {title}: {e}")
    return None

targets = [
    {"title": "Artificial_brain", "filename": "mechanical_brain.png"},
    {"title": "Crossroads_(mythology)", "filename": "great_split.png"},
    {"title": "Data_visualization", "filename": "portfolio.png"}
]

import urllib.request
for t in targets:
    url = get_wiki_image(t['title'])
    if url:
        print(f"Found {url} for {t['filename']}")
        # download and save
        urllib.request.urlretrieve(url, f"assets/{t['filename']}")
    else:
        print(f"Could not find wiki image for {t['title']}")
