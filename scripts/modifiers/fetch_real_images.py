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

queries = {
    "ml_radio": "vintage radio dials knobs close up photography",
    "ml_exam": "stack of old exam question papers on desk",
    "ml_overfit": "complex tangled padlock padlock security",
    "ml_factory": "massive futuristic automated factory floor robots",
    "ml_hinton": "Geoffrey Hinton portrait photography",
    "ml_ng": "Andrew Ng portrait photography",
    "ml_lecun": "Yann LeCun portrait photography",
    "ml_altman": "Sam Altman portrait photography"
}

assets_dir = os.path.join(PROJECT_ROOT, 'assets')
os.makedirs(assets_dir, exist_ok=True)

with DDGS() as ddgs:
    for name, query in queries.items():
        print(f"Searching for {name} ({query})...")
        results = list(ddgs.images(query, max_results=5))
        
        success = False
        for res in results:
            url = res['image']
            print(f"  Trying {url}...")
            try:
                # Add headers to masquerade as browser
                headers = {'User-Agent': 'Mozilla/5.0'}
                response = requests.get(url, timeout=5, headers=headers)
                response.raise_for_status()
                
                # Remove background directly
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

print("Image fetch and bg removal complete.")
