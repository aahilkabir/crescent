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

# Extract the existing NOTES array using regex
match = re.search(r'const NOTES=\[(.*?)\];\nconst slides=', html, re.DOTALL)
if match:
    notes_str = "[" + match.group(1) + "]"
    notes = json.loads(notes_str)
    
    # Update Slide 3 (Index 2)
    notes[2] = "<b>Speaker Point:</b> A coffee vending machine is 'smart', but it's not learning. You press a button, it mixes 20ml decoction and 80ml milk. If someone breaks the button, it breaks. It's rigid."
    
    # Update Slide 4 (Index 3)
    notes[3] = "<b>Deep Insight:</b> In traditional programming, humans write the coffee recipe. In Machine Learning, humans provide the ingredients and the ratings, and the machine writes the <i>recipe</i>. It learns the perfect ratio on its own."
    
    # Update Slide 5 (Index 4)
    notes[4] = "<b>Speaker Point:</b> Deep Learning is just Machine Learning with specialized layers. Like a panel of master tasters. One expert checks temperature, one checks bitterness, one checks aroma. It's a deep hierarchy."
    
    # Update Slide 6 (Index 5)
    notes[5] = "<b>The Rare Fact:</b> Generative AI doesn't just classify good or bad coffee. It looks at the mathematical 'Latent Space' of flavors and pulls out a brand new recipe that has never existed in human history."
    
    notes_js = "const NOTES=" + json.dumps(notes) + ";"
    
    # Replace it back
    html = html[:match.start()] + notes_js + "\nconst slides=" + html[match.end():]
    
    with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully updated Speaker Notes in JS array.")
else:
    print("Could not find NOTES array.")
