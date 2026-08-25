import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import glob
from PIL import Image
from rembg import remove

def process(input_path, output_path):
    print(f"Removing background for {input_path}")
    try:
        input_image = Image.open(input_path).convert("RGBA")
        output_image = remove(input_image)
        output_image.save(output_path, "PNG")
        print(f"Saved {output_path}")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

assets_dir = os.path.join(PROJECT_ROOT, 'assets')
os.makedirs(assets_dir, exist_ok=True)

artifacts_dir = "/Users/mohammedkabir/.gemini/antigravity-ide/brain/23df82f8-594d-4d1c-a958-9ed4535aecd8"

files = glob.glob(os.path.join(artifacts_dir, "*.png"))
target_prefixes = ["ml_idli", "ml_mountain", "ml_lens", "ml_map", "ml_coffee", "ml_bridge"]

for f in files:
    filename = os.path.basename(f)
    for p in target_prefixes:
        if filename.startswith(p):
            out_path = os.path.join(assets_dir, f"{p}.png")
            process(f, out_path)

print("Background removal started.")
