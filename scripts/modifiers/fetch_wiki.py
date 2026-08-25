import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import requests
from rembg import remove
from PIL import Image
import io

titles = {
    "ml_lecun": "Yann_LeCun",
    "ml_altman": "Sam_Altman"
}

assets_dir = os.path.join(PROJECT_ROOT, 'assets')
os.makedirs(assets_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0'}

api_url = "https://en.wikipedia.org/w/api.php?action=query&titles=Yann_LeCun|Sam_Altman&prop=pageimages&format=json&pithumbsize=800"

print("Fetching from Wikipedia API...")
response = requests.get(api_url, headers=headers).json()
pages = response['query']['pages']

urls = {}
for page_id, page_data in pages.items():
    title = page_data['title']
    if 'thumbnail' in page_data:
        url = page_data['thumbnail']['source']
        if title == "Yann LeCun":
            urls["ml_lecun"] = url
        elif title == "Sam Altman":
            urls["ml_altman"] = url

for name, url in urls.items():
    print(f"Fetching {name} from {url}...")
    try:
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        
        print(f"Removing background for {name}...")
        input_image = Image.open(io.BytesIO(response.content)).convert("RGBA")
        output_image = remove(input_image)
        
        out_path = os.path.join(assets_dir, f"{name}.png")
        output_image.save(out_path, "PNG")
        print(f"Saved {out_path} successfully!")
    except Exception as e:
        print(f"Failed to process {name}: {e}")

print("Wiki fetch complete.")
