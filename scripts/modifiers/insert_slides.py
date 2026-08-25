import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html"), "r") as f:
    html = f.read()

# Match the parts
match = re.search(r'(.*<div class="deck" id="deck">\n)(.*?)(\n</div>\n\n<div class="chrome">.*)', html, re.DOTALL)
if not match:
    print("Could not match HTML structure.")
    exit(1)

pre = match.group(1)
deck = match.group(2)
post = match.group(3)

sections = re.findall(r'<section.*?</section>', deck, re.DOTALL)

# Indices to insert (based on current sections)
# Slide 30 is "Let's open the box." We'll insert before it.
idx1 = 0
for i, s in enumerate(sections):
    if "Let's open the box." in s:
        idx1 = i
        break

# "Engineers are splitting into two groups."
idx2 = 0
for i, s in enumerate(sections):
    if "Engineers are splitting<br>into two groups." in s:
        idx2 = i
        break

# "A portfolio<br>beats a marksheet."
idx3 = 0
for i, s in enumerate(sections):
    if "A portfolio<br>beats a marksheet." in s:
        idx3 = i
        break

slide1 = """<section class="slide"><div class="glow g1"></div>
<h2 class="reveal" style="margin-top: 25vh; font-size: clamp(3rem, 6vw, 5rem); line-height: 1.1;">Theory becomes<br><span class="grad">Reality.</span></h2>
<img src="../../assets/mechanical_brain.png" class="person-img gold blend-screen" alt="Mechanical Brain" />
</section>"""

slide2 = """<section class="slide"><div class="glow g2"></div>
<h2 class="reveal" style="margin-top: 25vh; font-size: clamp(3rem, 6vw, 5rem); line-height: 1.1;">Adapt or<br><span class="grad-cool">Automate.</span></h2>
<img src="../../assets/great_split.png" class="person-img cool blend-screen" alt="Adapt or Automate" />
</section>"""

slide3 = """<section class="slide"><div class="glow g3"></div>
<h2 class="reveal" style="margin-top: 25vh; font-size: clamp(3rem, 6vw, 5rem); line-height: 1.1;">Your Code.<br><span class="grad-grn">Your Proof.</span></h2>
<img src="../../assets/portfolio.png" class="person-img grn blend-screen" alt="Portfolio" />
</section>"""

# Insert in reverse order to keep indices valid!
if idx3 > 0:
    sections.insert(idx3, slide3)
if idx2 > 0:
    sections.insert(idx2, slide2)
if idx1 > 0:
    sections.insert(idx1, slide1)

new_deck = "".join(sections)

# Now update the NOTES array in `post`
# The NOTES array is like: const NOTES=["...", "...", ...];
script_match = re.search(r'const NOTES=\[(.*?)\];', post, re.DOTALL)
if script_match:
    notes_str = script_match.group(1)
    # Split the array. This is tricky because of commas inside strings.
    # We can use ast.literal_eval on the string wrapped in []
    import ast
    try:
        notes_arr = ast.literal_eval('[' + notes_str + ']')
        if idx3 > 0:
            notes_arr.insert(idx3, "")
        if idx2 > 0:
            notes_arr.insert(idx2, "")
        if idx1 > 0:
            notes_arr.insert(idx1, "")
            
        import json
        new_notes_str = json.dumps(notes_arr)
        # JSON dumps escapes forward slashes and double quotes. We need to be careful.
        # But wait! JSON uses `\"` for double quotes inside strings, which is valid JS.
        # It also might output valid JSON.
        post = post.replace('const NOTES=[' + notes_str + '];', f'const NOTES={new_notes_str};')
    except Exception as e:
        print("Failed to parse NOTES:", e)
        # Fallback: Just append empty strings to the end so it doesn't crash
        post = post.replace('];', ', "", "", ""];')

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html"), "w") as f:
    f.write(pre + new_deck + post)

print("Insertion complete!")
