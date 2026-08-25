import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html"), "r") as f:
    html = f.read()

deck_match = re.search(r'(.*<div class="deck" id="deck">\n)(.*?)(\n</div>\n\n<div class="chrome">.*)', html, re.DOTALL)
if not deck_match:
    print("Could not match HTML structure.")
    exit(1)

deck = deck_match.group(2)
sections = re.findall(r'(<section[^>]*>.*?)</section>', deck, re.DOTALL)

print(f"Total slides: {len(sections)}")
for i, s in enumerate(sections):
    if '<img' not in s:
        # Extract title or some text to identify it
        title_match = re.search(r'<h[23][^>]*>(.*?)</h[23]>', s, re.DOTALL)
        title = title_match.group(1).replace('<br>', ' ').strip() if title_match else "No title"
        # strip html tags from title
        title = re.sub(r'<[^>]+>', '', title)
        print(f"Slide {i}: {title}")
