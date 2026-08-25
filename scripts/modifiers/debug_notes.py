import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re
import json

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "r", encoding="utf-8") as f:
    html = f.read()

# Extract slides
slides = re.findall(r'<section class="[^"]*slide[^"]*".*?</section>', html, re.DOTALL)

# Extract notes
match = re.search(r'const NOTES=\[(.*?)\];\nconst slides=', html, re.DOTALL)
if match:
    notes_str = "[" + match.group(1) + "]"
    notes = json.loads(notes_str)
else:
    notes = []

print(f"Total Slides: {len(slides)}")
print(f"Total Notes: {len(notes)}")

for i in range(max(len(slides), len(notes))):
    slide_text = ""
    if i < len(slides):
        # find the first h1, h2, or h3
        header_match = re.search(r'<h[123][^>]*>(.*?)</h[123]>', slides[i], re.DOTALL)
        if header_match:
            slide_text = re.sub(r'<[^>]+>', '', header_match.group(1)).strip().replace('\n', ' ')
        else:
            slide_text = "No header"
            
    note_text = ""
    if i < len(notes):
        note_text = re.sub(r'<[^>]+>', '', notes[i]).strip()[:50] + "..."
        
    print(f"[{i}] SLIDE: {slide_text[:40]:<40} | NOTE: {note_text}")
