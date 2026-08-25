import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "ml-foundations.html"), "r") as f:
    html = f.read()

deck_match = re.search(r'(.*<div class="deck" id="deck">\n)(.*?)(\n</div>\n\n<script>.*)', html, re.DOTALL)
if not deck_match:
    print("Could not match HTML structure.")
    exit(1)

deck = deck_match.group(2)
sections = re.findall(r'(<section[^>]*>.*?</section>)', deck, re.DOTALL)

print(f"Total slides: {len(sections)}")
