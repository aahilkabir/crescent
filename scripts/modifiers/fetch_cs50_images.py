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
import time

# Using direct image URLs from reliable sources
image_sources = {
    "ml_perceptron": [
        "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800",  # AI brain
        "https://images.unsplash.com/photo-1677442135703-1787eea5ce01?w=800",  # neural network
    ],
    "ml_backprop": [
        "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=800",  # chain/dominos
        "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=800",  # code debug
    ],
    "ml_attention": [
        "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800",  # spotlight
        "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=800",  # spotlight event
    ],
    "ml_rocket": [
        "https://images.unsplash.com/photo-1517976487492-5750f3195933?w=800",  # rocket launch
        "https://images.unsplash.com/photo-1457364559154-aa2644600ebb?w=800",  # rocket
    ],
    "ml_openbook": [
        "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=800",  # open book study
        "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800",  # library books
    ],
    "ml_chart": [
        "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800",  # stock chart growth
        "https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=800",  # stock trading
    ],
    "ml_india": [
        "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=800",  # India gate
        "https://images.unsplash.com/photo-1532664189809-02133fee698d?w=800",  # India tech
    ],
    "ml_salary": [
        "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=800",  # money/salary
        "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800",  # cash growth
    ],
}

assets_dir = os.path.join(PROJECT_ROOT, 'assets')
os.makedirs(assets_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

for name, urls in image_sources.items():
    out_path = os.path.join(assets_dir, f"{name}.png")
    if os.path.exists(out_path):
        print(f"Skipping {name} (already exists)")
        continue
    
    success = False
    for url in urls:
        print(f"Fetching {name} from {url}...")
        try:
            response = requests.get(url, timeout=10, headers=headers)
            response.raise_for_status()
            
            print(f"  Removing background for {name}...")
            input_image = Image.open(io.BytesIO(response.content)).convert("RGBA")
            input_image.thumbnail((800, 800))
            output_image = remove(input_image)
            
            output_image.save(out_path, "PNG")
            print(f"  Saved {out_path} successfully!")
            success = True
            break
        except Exception as e:
            print(f"  Failed: {e}")
    
    if not success:
        print(f"FAILED to get any image for {name}")
    
    time.sleep(0.5)

print("All new images fetched and processed!")
