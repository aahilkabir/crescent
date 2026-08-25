import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html"), "r") as f:
    html = f.read()

match = re.search(r'(.*<div class="deck" id="deck">\n)(.*?)(\n</div>\n\n<div class="chrome">.*)', html, re.DOTALL)
if not match:
    print("Could not match HTML structure.")
    exit(1)

pre = match.group(1)
deck = match.group(2)
post = match.group(3)

sections = re.findall(r'<section.*?</section>', deck, re.DOTALL)

# Find indices
idx_coffee = 0
for i, s in enumerate(sections):
    if "Cricket-la Catch" in s:
        idx_coffee = i
        break

idx_compass = 0
for i, s in enumerate(sections):
    if "Yaarku Idly Pudikkum?" in s:
        idx_compass = i
        break

idx_auto = 0
for i, s in enumerate(sections):
    if "Kanna Kattikitu" in s:
        idx_auto = i
        break

idx_orch = 0
for i, s in enumerate(sections):
    if "Foundations to production." in s:
        idx_orch = i
        break

# Sort indices descending to safely insert without messing up subsequent indices
insertions = sorted([
    (idx_coffee, """<section class="slide"><div class="glow g1"></div>
<h2 class="reveal" style="margin-top: 25vh; font-size: clamp(3rem, 6vw, 5rem); line-height: 1.1;">Brewing<br><span class="grad">Intelligence.</span></h2>
<img src="../../assets/filter_coffee.png" class="person-img gold blend-screen" alt="Filter Coffee" />
</section>"""),
    (idx_compass, """<section class="slide"><div class="glow g2"></div>
<h2 class="reveal" style="margin-top: 25vh; font-size: clamp(3rem, 6vw, 5rem); line-height: 1.1;">Navigating<br><span class="grad-cool">Latent Space.</span></h2>
<img src="../../assets/vintage_compass.png" class="person-img cool blend-screen" alt="Vintage Compass" />
</section>"""),
    (idx_auto, """<section class="slide"><div class="glow g3"></div>
<h2 class="reveal" style="margin-top: 25vh; font-size: clamp(3rem, 6vw, 5rem); line-height: 1.1;">Finding the<br><span class="grad-grn">Optimal Path.</span></h2>
<img src="../../assets/auto_rickshaw.png" class="person-img grn blend-screen" alt="Auto Rickshaw" />
</section>"""),
    (idx_orch, """<section class="slide"><div class="glow g1"></div>
<h2 class="reveal" style="margin-top: 25vh; font-size: clamp(3rem, 6vw, 5rem); line-height: 1.1;">The<br><span class="grad">Orchestrator.</span></h2>
<img src="../../assets/orchestrator.png" class="person-img gold blend-screen" alt="Orchestrator" />
</section>""")
], key=lambda x: x[0], reverse=True)

# Insert the slides
for idx, slide in insertions:
    if idx > 0:
        sections.insert(idx, slide)

new_deck = "".join(sections)

# Update NOTES array
script_match = re.search(r'const NOTES=\[(.*?)\];', post, re.DOTALL)
if script_match:
    notes_str = script_match.group(1)
    import ast
    try:
        notes_arr = ast.literal_eval('[' + notes_str + ']')
        # Insert notes in descending order
        for idx, _ in insertions:
            if idx > 0:
                notes_arr.insert(idx, "")
            
        import json
        new_notes_str = json.dumps(notes_arr)
        post = post.replace('const NOTES=[' + notes_str + '];', f'const NOTES={new_notes_str};')
    except Exception as e:
        print("Failed to parse NOTES:", e)
        post = post.replace('];', ', "", "", "", ""];')

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html"), "w") as f:
    f.write(pre + new_deck + post)

print("Insertion complete!")
