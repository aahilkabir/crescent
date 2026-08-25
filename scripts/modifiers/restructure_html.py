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

# Extract notes
script_match = re.search(r'const NOTES=\[(.*?)\];', post, re.DOTALL)
import ast
notes_arr = ast.literal_eval('[' + script_match.group(1) + ']') if script_match else [""] * len(sections)

def get_slide(keyword):
    for i, s in enumerate(sections):
        if keyword in s:
            return s, notes_arr[i] if i < len(notes_arr) else ""
    print(f"Warning: could not find slide with keyword '{keyword}'")
    return None, ""

# Now build the new sequence
new_seq = []

def add(keyword):
    s, n = get_slide(keyword)
    if s:
        new_seq.append((s, n))

# Act 1: The Hook
add("AI<br><span") # Title
add("Your Marks<br>won't get you")
add("I'm Kabir")
add("Four promises.")
add("Josiyam Paakalama?")
add("Brewing<br><span") # Coffee Image
add("Cricket-la Catch")
add("nested dolls")
add("Exam-kku Padikkurathu")
add("Room-a Sutham Pandrathu")
add("PUBG-la Adi")

# Act 2 & 3: The Foundations (History + Math)
add("The people they didn't tell you about.") # Intro to history/math
add("Walter Pitts") # 1943
add("Kolam Podalama?") # Linear algebra
add("Maavu Aatra Machine.") # Matrix
add("Frank Rosenblatt") # 1958
add("15 Varusha Iruttu.") # Winter
add("Alexey Ivakhnenko") # Ukraine
add("Erakkam Enga Irukku?") # Derivative
add("Finding the<br><span") # Auto Rickshaw image
add("Kanna Kattikitu") # Gradient descent
add("Seppo Linnainmaa") # 1970 backprop
add("Kudumbathula") # Chain rule backprop
add("Pudhu Aadharam") # Bayes probability
add("Nethu Ennachu") # Markov
add("Carl Friedrich Gauss") # Stats
add("Chennai-la Snow Peidha?") # Entropy
add("Oru Rathiri-la") # 2012
add("Attention is all you need") # 2017 Transformer
add("The mathematics.") # Let's put this here as a recap
add("You can fake a demo.")
add("Roll downhill<br>to reduce surprise.")

# Act 4: The Machine
add("Theory becomes<br><span") # Mechanical Brain
add("Let's open the box.")
add("Navigating<br><span") # Compass
add("Yaarku Idly Pudikkum?")
add("Madras Filter Coffee.")
add("Four steps, repeated")
add("predicts the next<br>word")
add("Open Book Exam") # RAG
add("Appa-oda Bike-a") # Fine Tuning
add("Five links.")

# Act 5: The Market
add("Adapt or<br><span") # Great split image
add("Now &mdash; why this") # Wait, "Now - why this matters"
add("Engineers are splitting")
add("Campus interviews changed")
add("Could you answer these")
add("College gives you theory.")
add("Be a T-shaped")
add("Your Code.<br><span") # Portfolio image
add("A portfolio<br>beats")
add("The orchestrator") # Wait, "The<br><span class="grad">Orchestrator"
add("The<br><span class=\"grad\">Orchestrator") 

# The Pitch
add("The bridge.")
add("We teach you to build AI")
add("Foundations to production.")
add("Not a certificate.")
add("Built by a founder")
add("Compare the two prices.")
add("The window is open")
add("Don't leave this room")
add("Foundations first.")

# We also need to inject the 6 new images into specific slides.
image_injections = {
    "nested dolls": '<img src="../../assets/matryoshka.png" class="person-img gold blend-screen" alt="Matryoshka" />',
    "The mathematics.": '<img src="../../assets/abacus.png" class="person-img gold blend-screen" alt="Abacus" />',
    "Open Book Exam": '<img src="../../assets/library.png" class="person-img gold blend-screen" alt="Library" />',
    "Be a T-shaped": '<img src="../../assets/t_shape.png" class="person-img cool blend-screen" alt="T-Shape" />',
    "The window is open": '<img src="../../assets/telescope.png" class="person-img cool blend-screen" alt="Telescope" />',
    "Foundations first.": '<img src="../../assets/blueprint.png" class="person-img grn blend-screen" alt="Blueprint" />'
}

final_slides = []
final_notes = []

for s, n in new_seq:
    # Inject images if keyword matches
    for kw, img_tag in image_injections.items():
        if kw in s and '<img' not in s: # Only inject if it doesn't already have an image
            # Insert right before </section>
            s = s.replace('</section>', f'\n{img_tag}\n</section>')
    final_slides.append(s)
    final_notes.append(n)

new_deck_html = "".join(final_slides)
new_notes_json = json.dumps(final_notes)

new_post = post
script_match_again = re.search(r'(const NOTES=)\[.*?\](;\n</script>)', post, re.DOTALL)
if script_match_again:
    new_post = post.replace(script_match_again.group(0), f'const NOTES={new_notes_json};')

# Fix progress bar logic: The script has `document.getElementById('tot').innerText = slides.length;` 
# so it auto updates.

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Final.html"), "w") as f:
    f.write(pre + new_deck_html + new_post)

print(f"Restructure complete. Old slide count: {len(sections)}. New slide count: {len(final_slides)}.")
