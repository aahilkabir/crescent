import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import json
import re

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "r", encoding="utf-8") as f:
    html = f.read()

match = re.search(r'const NOTES=\[(.*?)\];\nconst slides=', html, re.DOTALL)
if match:
    notes_str = "[" + match.group(1) + "]"
    notes = json.loads(notes_str)
    
    # Current indices:
    # 11: Tokens
    # 12: Parameters
    # 13: Models
    # 14: ""
    # 15: Pitts
    # 16: Frank
    # 17: Winter
    # 18: Alexey
    # 19: ELIZA
    # 20: Ng
    # 21: Altman
    
    tokens = notes[11]
    params = notes[12]
    models = notes[13]
    
    empty = notes[14]
    pitts = notes[15]
    frank = notes[16]
    winter = notes[17]
    alexey = notes[18]
    eliza = notes[19]
    ng = notes[20]
    altman = notes[21]
    
    # New order:
    # 11: empty
    # 12: pitts
    # 13: frank
    # 14: winter
    # 15: alexey
    # 16: eliza
    # 17: ng
    # 18: altman
    # 19: tokens
    # 20: params
    # 21: models
    
    notes[11] = empty
    notes[12] = pitts
    notes[13] = frank
    notes[14] = winter
    notes[15] = alexey
    notes[16] = eliza
    notes[17] = ng
    notes[18] = altman
    notes[19] = tokens
    notes[20] = params
    notes[21] = models
    
    notes_js = "const NOTES=" + json.dumps(notes) + ";"
    html = html[:match.start()] + notes_js + "\nconst slides=" + html[match.end():]
    
    with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Fixed NOTES array order.")
