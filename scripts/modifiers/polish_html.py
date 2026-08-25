import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re
import json

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html"), "r") as f:
    html = f.read()

deck_match = re.search(r'(.*<div class="deck" id="deck">\n)(.*?)(\n</div>\n\n<div class="chrome">.*)', html, re.DOTALL)
if not deck_match:
    print("Could not match HTML structure.")
    exit(1)

pre = deck_match.group(1)
deck = deck_match.group(2)
post = deck_match.group(3)

sections = re.findall(r'(<section[^>]*>.*?</section>)', deck, re.DOTALL)

script_match = re.search(r'const NOTES=\[(.*?)\];', post, re.DOTALL)
import ast
notes_arr = ast.literal_eval('[' + script_match.group(1) + ']') if script_match else [""] * len(sections)

new_sections = []
new_notes = []

current_act = "Part 1 &middot; The Hook"
act_color = ""

for i, s in enumerate(sections):
    # Determine the Act
    if "The people they" in s or "Walter Pitts" in s or "Kolam" in s:
        current_act = "Part 2 &middot; The Foundations"
        act_color = "grn"
    if "Theory becomes" in s or "Let's open the box" in s:
        current_act = "Part 3 &middot; The Machine"
        act_color = ""
    if "Adapt or" in s or "Great Split" in s or "Engineers are splitting" in s:
        current_act = "Part 4 &middot; The Market"
        act_color = "cool"
    if "The bridge." in s or "We teach you" in s:
        current_act = "Part 5 &middot; The Bridge"
        act_color = ""
        
    # Check for image and add class
    if '<img' in s:
        s = s.replace('<section class="slide center">', '<section class="slide center has-img">')
        s = s.replace('<section class="slide active">', '<section class="slide active has-img">')
        s = s.replace('<section class="slide center active">', '<section class="slide center active has-img">')
        if 'has-img' not in s:
            s = s.replace('<section class="slide">', '<section class="slide has-img">')
            
    # Standardize eyebrow
    # Remove existing eyebrow if any
    s = re.sub(r'<div class="eyebrow.*?</div>', '', s)
    
    # Inject new eyebrow
    eyebrow_html = f'<div class="eyebrow {act_color} reveal">{current_act}</div>\n'
    
    if '<div class="glow' in s:
        glows = list(re.finditer(r'<div class="glow.*?</div>', s))
        if glows:
            last_glow = glows[-1]
            insert_pos = last_glow.end()
            s = s[:insert_pos] + '\n' + eyebrow_html + s[insert_pos:]
    else:
        s = re.sub(r'(<section[^>]*>)', r'\1\n' + eyebrow_html, s, count=1)

    # Text tightening
    s = s.replace("This means that if you're an engineer in Group B, the old playbook won't work anymore.", "If you're in Group B, the old playbook is dead.")
    s = s.replace("They want people who can string together AI models into working software.", "They want engineers who build AI systems.")
    s = s.replace("We teach you to build real, production-ready AI applications using the actual frameworks the industry uses.", "We teach you to build production-ready AI.")
        
    new_sections.append(s)
    new_notes.append(notes_arr[i] if i < len(notes_arr) else "")

new_deck = "\n".join(new_sections)
new_notes_json = json.dumps(new_notes)

new_post = post
script_match_again = re.search(r'(const NOTES=)\[.*?\](;\n</script>)', post, re.DOTALL)
if script_match_again:
    new_post = post.replace(script_match_again.group(0), f'const NOTES={new_notes_json};')

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html"), "w") as f:
    f.write(pre + new_deck + new_post)

print(f"Polish complete on {len(sections)} slides.")
