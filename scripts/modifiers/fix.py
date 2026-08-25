import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html"), "r") as f:
    content = f.read()

# The file contains multiple copies of the slides inside <div class="deck" id="deck">
# We will extract the part before the deck div, and the part after the deck div (from </div>\n\n<div class="chrome">)
match = re.search(r'(.*<div class="deck" id="deck">\n)(.*)(\n</div>\n\n<div class="chrome">.*)', content, re.DOTALL)
if not match:
    print("Could not find the deck section")
    exit(1)

pre = match.group(1)
deck = match.group(2)
post = match.group(3)

# Inside the deck, there are multiple <section>...</section> tags.
# We will just extract all <section ...>...</section> tags.
sections = re.findall(r'<section.*?</section>', deck, re.DOTALL)

# Since the slides might be duplicated, we take the first 25, which should be the original ones (or we can just dedup them by title)
# Actually, the original presentation has exactly 25 slides.
# Let's count the number of slides
print(f"Total sections found: {len(sections)}")

# Filter out duplicates by looking at the inner HTML
unique_sections = []
seen = set()
for s in sections:
    # Remove any previously inserted images so we can deduplicate properly
    s_clean = re.sub(r'<img src="../../assets/[^"]+".*?/>', '', s)
    if s_clean not in seen:
        seen.add(s_clean)
        unique_sections.append(s_clean)

print(f"Unique sections found: {len(unique_sections)}")

# Now we have the clean unique sections. Let's add the images back to the specific sections.
for i, s in enumerate(unique_sections):
    if "Cricket-la Catch" in s:
        unique_sections[i] = s.replace('</section>', '<img src="../../assets/cricket_catch.png" class="person-img gold blend-screen" alt="Cricket Catch" /></section>')
    elif "Walter Pitts" in s or "1943 · The First Neuron" in s:
        unique_sections[i] = s.replace('</section>', '<img src="../../assets/walter_pitts.png" class="person-img cool" alt="Walter Pitts" /></section>')
    elif "Frank Rosenblatt" in s or "1958 · The Machine That Learned" in s:
        unique_sections[i] = s.replace('</section>', '<img src="../../assets/frank_rosenblatt.png" class="person-img cool" alt="Frank Rosenblatt" /></section>')
    elif "Alexey Ivakhnenko" in s or "1965 · The Forgotten Father" in s:
        unique_sections[i] = s.replace('</section>', '<img src="../../assets/alexey_ivakhnenko.png" class="person-img cool" alt="Alexey Ivakhnenko" /></section>')
    elif "Kolam Podalama" in s:
        unique_sections[i] = s.replace('</section>', '<img src="../../assets/kolam.png" class="person-img grn blend-screen" alt="Kolam Pattern" /></section>')

# Join them back into a single string (without newlines, as it originally was, or with newlines for readability)
new_deck = "".join(unique_sections)

# Write back
with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html"), "w") as f:
    f.write(pre + new_deck + post)

print("Fixed HTML written successfully!")
