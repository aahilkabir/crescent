import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import requests
from PIL import Image
from rembg import remove
import io
import time

assets_dir = os.path.join(PROJECT_ROOT, 'assets')
os.makedirs(assets_dir, exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}

# Strategy: Find images with DARK/BLACK backgrounds that blend with mix-blend-mode:screen
# OR iconic clean-cut objects that rembg handles well.
image_sources = {
    # Buzzword analogies - use dark-background, high-contrast images
    "ml_recipe": [
        "https://images.unsplash.com/photo-1466637574441-749b8f19452f?w=800",  # spices on dark surface
    ],
    "ml_radio": [
        "https://images.unsplash.com/photo-1558618666-fcd25c85f82e?w=800",  # dark vintage radio
        "https://images.unsplash.com/photo-1571330735066-03aaa9429d89?w=800",  # radio on dark
    ],
    "ml_exam": [
        "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800",  # studying dark mood
    ],
    "ml_overfit": [
        "https://images.unsplash.com/photo-1614064641938-3bbee52942c7?w=800",  # tangled wires neon dark
    ],
    "ml_factory": [
        "https://images.unsplash.com/photo-1563207153-f403bf289096?w=800",  # dark factory robotic arms
        "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=800",  # tech dark
    ],
    # CS50 depth images - dark background, high contrast
    "ml_perceptron": [
        "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800",  # AI brain neural dark
        "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=800",  # math formulas dark
    ],
    "ml_backprop": [
        "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=800",  # code on dark screen
        "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=800",  # code dark
    ],
    "ml_rocket": [
        "https://images.unsplash.com/photo-1516849841032-87cbac4d88f7?w=800",  # rocket at night
        "https://images.unsplash.com/photo-1457364559154-aa2644600ebb?w=800",  # rocket launch dark
    ],
    "ml_openbook": [
        "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=800",  # library books dramatic
        "https://images.unsplash.com/photo-1507842217343-583bb7270b66?w=800",  # library dark
    ],
    # Upsell section - dramatic dark images
    "ml_chart": [
        "https://images.unsplash.com/photo-1642790106117-e829e14a795f?w=800",  # stock chart dark neon
        "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800",  # trading dark
    ],
    "ml_india": [
        "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=800",  # Taj Mahal dramatic
        "https://images.unsplash.com/photo-1532664189809-02133fee698d?w=800",  # India
    ],
    "ml_salary": [
        "https://images.unsplash.com/photo-1621761191319-c6fb62004040?w=800",  # gold coins dark
        "https://images.unsplash.com/photo-1633158829585-23ba8f7c8caf?w=800",  # crypto/money dark
    ],
}

for name, urls in image_sources.items():
    out_path = os.path.join(assets_dir, f"{name}.png")
    
    success = False
    for url in urls:
        print(f"Fetching {name} from {url}...")
        try:
            response = requests.get(url, timeout=10, headers=headers)
            response.raise_for_status()
            
            img = Image.open(io.BytesIO(response.content)).convert("RGBA")
            img.thumbnail((900, 900))
            
            # Save directly without bg removal — dark images blend via mix-blend-mode:screen
            img.save(out_path, "PNG")
            print(f"  Saved {out_path} ({img.size[0]}x{img.size[1]})")
            success = True
            break
        except Exception as e:
            print(f"  Failed: {e}")
    
    if not success:
        print(f"FAILED: {name}")
    
    time.sleep(0.3)

# For portraits, re-do with rembg since they need clean cutouts
portrait_sources = {
    "ml_hinton": "https://pbs.twimg.com/profile_images/1857541833025323008/T2YFJDoR_400x400.jpg",
    "ml_altman": "https://pbs.twimg.com/profile_images/1905296677803798529/oNLuHUeX_400x400.jpg",
    "ml_ng": "https://pbs.twimg.com/profile_images/1602787340675297281/RlBNRNQ6_400x400.jpg",
    "ml_lecun": "https://pbs.twimg.com/profile_images/1669613227082563584/WdmDrE1h_400x400.jpg",
}

for name, url in portrait_sources.items():
    out_path = os.path.join(assets_dir, f"{name}.png")
    print(f"Fetching portrait {name}...")
    try:
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        
        img = Image.open(io.BytesIO(response.content)).convert("RGBA")
        output = remove(img)
        output.save(out_path, "PNG")
        print(f"  Saved portrait {out_path}")
    except Exception as e:
        print(f"  Failed: {e}")
    time.sleep(0.3)

print("\\nAll images refreshed!")
