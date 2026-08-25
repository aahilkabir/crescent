import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import urllib.request
import time

image_sources = {
    "cs_splendor": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?w=800&q=80",
    "cs_canteen": "https://images.unsplash.com/photo-1601050690597-df0568f70950?w=800&q=80",
    "cs_register": "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=800&q=80",
    "cs_duck": "https://images.unsplash.com/photo-1559715745-e1b33a271c8f?w=800&q=80",
    "cs_locker": "https://images.unsplash.com/photo-1541829070764-84a7d30dd3f3?w=800&q=80",
    "cs_phonebook": "https://images.unsplash.com/photo-1512820790803-83ca734da794?w=800&q=80",
    "cs_rocket": "https://images.unsplash.com/photo-1517976487492-5750f3195933?w=800&q=80",
    "cs_warehouse": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=800&q=80",
    "cs_git": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&q=80",
    "cs_blueprint": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=800&q=80"
}

assets_dir = os.path.join(PROJECT_ROOT, 'assets')
os.makedirs(assets_dir, exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}

for name, url in image_sources.items():
    out_path = os.path.join(assets_dir, f"{name}.png")
    if os.path.exists(out_path):
        print(f"Skipping {name} (exists)")
        continue
    
    print(f"Downloading {name}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as res:
            with open(out_path, "wb") as f:
                f.write(res.read())
        print(f"  Successfully saved {name}.png")
    except Exception as e:
        print(f"  Error downloading {name}: {e}")
    time.sleep(0.3)

print("All high quality images saved!")
