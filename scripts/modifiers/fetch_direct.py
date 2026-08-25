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

urls = {
    "ml_lecun": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Yann_LeCun_-_2018_%28cropped%29.jpg",
    "ml_altman": "https://upload.wikimedia.org/wikipedia/commons/8/88/Sam_Altman_TechCrunch_Disrupt_San_Francisco_2019_-_Day_1_%2848834434641%29_%28cropped%29.jpg"
}

assets_dir = os.path.join(PROJECT_ROOT, 'assets')
os.makedirs(assets_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

for name, url in urls.items():
    print(f"Fetching {name}...")
    try:
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        
        print(f"Removing background for {name}...")
        input_image = Image.open(io.BytesIO(response.content)).convert("RGBA")
        
        # Resize to max 800px width/height to avoid memory issues with rembg on huge wikimedia images
        input_image.thumbnail((800, 800))
        
        output_image = remove(input_image)
        
        out_path = os.path.join(assets_dir, f"{name}.png")
        output_image.save(out_path, "PNG")
        print(f"Saved {out_path} successfully!")
    except Exception as e:
        print(f"Failed to process {name}: {e}")

print("Direct fetch complete.")
