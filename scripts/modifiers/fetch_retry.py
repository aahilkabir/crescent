import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import requests
from duckduckgo_search import DDGS
from rembg import remove
from PIL import Image
import io
import time

queries = {
    "ml_lecun": "Yann LeCun high resolution face portrait",
    "ml_altman": "Sam Altman high resolution face portrait"
}

assets_dir = os.path.join(PROJECT_ROOT, 'assets')
os.makedirs(assets_dir, exist_ok=True)

with DDGS() as ddgs:
    for name, query in queries.items():
        print(f"Searching for {name} ({query})...")
        try:
            results = list(ddgs.images(query, max_results=3))
            
            success = False
            for res in results:
                url = res['image']
                print(f"  Trying {url}...")
                try:
                    headers = {'User-Agent': 'Mozilla/5.0'}
                    response = requests.get(url, timeout=5, headers=headers)
                    response.raise_for_status()
                    
                    print(f"  Removing background for {name}...")
                    input_image = Image.open(io.BytesIO(response.content)).convert("RGBA")
                    output_image = remove(input_image)
                    
                    out_path = os.path.join(assets_dir, f"{name}.png")
                    output_image.save(out_path, "PNG")
                    print(f"  Saved {out_path} successfully!")
                    success = True
                    break
                except Exception as e:
                    print(f"  Failed: {e}")
                    
            if not success:
                print(f"Failed to get any image for {name}")
        except Exception as e:
            print(f"Search failed for {name}: {e}")
        
        time.sleep(2) # Prevent rate limits

print("Image fetch complete.")
