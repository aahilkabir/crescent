import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

from PIL import Image
from rembg import remove

def process():
    input_path = os.path.join(PROJECT_ROOT, "assets/aatukkal2.jpg")
    output_path = os.path.join(PROJECT_ROOT, "assets/aatukkal2_nobg.png")
    print(f"Removing background for {input_path}")
    try:
        input_image = Image.open(input_path).convert("RGBA")
        output_image = remove(input_image)
        output_image.save(output_path, "PNG")
        print(f"Saved {output_path}")
    except Exception as e:
        print(f"Error processing: {e}")

if __name__ == "__main__":
    process()
