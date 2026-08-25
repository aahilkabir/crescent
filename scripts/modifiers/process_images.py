import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import requests
from io import BytesIO
from PIL import Image
from duckduckgo_search import DDGS
from rembg import remove

def get_image_url(query):
    try:
        with DDGS() as ddgs:
            results = list(ddgs.images(
                query,
                region="wt-wt",
                safesearch="moderate",
                size="Medium",
                max_results=5
            ))
            if results:
                # return the first valid result
                for res in results:
                    url = res.get("image")
                    if url:
                        return url
    except Exception as e:
        print(f"Error searching for {query}: {e}")
    return None

def process_image(url, output_path, remove_bg=True):
    try:
        print(f"Downloading {url}...")
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        input_image = Image.open(BytesIO(response.content)).convert("RGBA")
        
        if remove_bg:
            print(f"Removing background for {output_path}...")
            output_image = remove(input_image)
        else:
            output_image = input_image
            
        output_image.save(output_path, "PNG")
        print(f"Saved {output_path}")
    except Exception as e:
        print(f"Error processing {url}: {e}")

def main():
    assets_dir = os.path.join(PROJECT_ROOT, 'assets')
    os.makedirs(assets_dir, exist_ok=True)

    targets = [
        {"query": "Walter Pitts mathematician portrait real photo", "filename": "walter_pitts.png", "bg": True},
        {"query": "Frank Rosenblatt perceptron portrait real photo", "filename": "frank_rosenblatt.png", "bg": True},
        {"query": "Alexey Ivakhnenko scientist portrait photo", "filename": "alexey_ivakhnenko.png", "bg": True},
        {"query": "Seppo Linnainmaa computer scientist portrait photo", "filename": "seppo_linnainmaa.png", "bg": True},
        {"query": "cricket player catching a ball action photo transparent background", "filename": "cricket_catch.png", "bg": True},
        {"query": "south indian traditional kolam pattern beautiful", "filename": "kolam.png", "bg": True}
    ]

    for target in targets:
        url = get_image_url(target["query"])
        if url:
            out_path = os.path.join(assets_dir, target["filename"])
            process_image(url, out_path, remove_bg=target["bg"])
        else:
            print(f"Could not find image for {target['query']}")

if __name__ == "__main__":
    main()
