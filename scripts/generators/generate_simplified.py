import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re

file_path = os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar.html")
out_path = os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html")

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace Slide 2
html = html.replace('Your CGPA is<br>no longer your résumé.', 'Your Marks<br>won\'t get you the job.')
html = html.replace('In 2015, a good CGPA got you an interview.<br>In 2026, it gets you into a pile of 4,000 identical CVs.', 'In 2015, high marks got you an interview.<br>In 2026, they just put you in a huge pile of identical resumes.')
html = html.replace('What gets you <em>out</em> of that pile is the one thing this room is about to learn.', 'We will show you the exact secret to stand <em>out</em> from that pile.')

# Replace Slide 5
html = html.replace('Strip away the hype and the sci-fi.', 'Forget the movie magic and robots.')
html = html.replace('At its core, intelligence is one thing: <em>prediction</em>.', 'At its heart, intelligence is just one thing: <em>guessing correctly</em>.')

# Replace Embeddings Slide
html = html.replace('Embeddings: turning<br>meaning into coordinates.', 'Embeddings: turning<br>words into map points.')
html = html.replace('A model can\'t read "Chennai." So it assigns it a point in a 1,000-dimensional space, placed so that "Chennai," "Madras," and "Tamil Nadu" cluster together — learned purely from how humans use the words.', 'A computer can\'t taste "Idly". But if we put foods on a map, it learns that "Idly", "Vada", and "Sambar" sit closely together, while "Pizza" is far away. AI learns meaning by looking at distance!')

# Replace Neuron Slide
html = html.replace('Multiply, add, bend.', 'Let\'s learn using<br>Filter Coffee.')
html = html.replace('Perukki, kootti, thevaiyaana valaikkuradhu.', 'Decoction, paal, sakkarai alavu dhaan weight!')
html = html.replace('A neuron takes its inputs, multiplies each by a <b>weight</b> (how much it trusts that input), adds them up, and passes the result through a bend that decides whether to "fire."', 'A neuron is like making coffee. Decoction, milk, and sugar are inputs. The <b>weights</b> are how much of each you pour. Too bitter? Adjust the weight. Too sweet? Adjust the weight.')
html = html.replace('Those weights <em>are</em> the knobs. Learning = finding the right weights. That\'s the entire game.', 'Learning is just finding the perfect recipe. That is the entire secret of a neural network.')

# Replace Group A / Group B Slide
html = html.replace('Group A · Replaceable', 'Group A · Can be replaced')
html = html.replace('Writes code AI can now write', 'Writes basic code AI can easily write')
html = html.replace('Knows tools, not foundations', 'Only knows how to copy-paste code')
html = html.replace('Competes with 4,000 identical CVs', 'Competes with 4,000 similar students')
html = html.replace('Salary: flat or falling', 'Salary drops')

html = html.replace('Group B · Un-automatable', 'Group B · Super safe career')
html = html.replace('Directs AI to build systems', 'Uses AI as a smart assistant')
html = html.replace('Understands why things work', 'Understands the deep basics')
html = html.replace('Builds what others can\'t', 'Builds real, powerful products')
html = html.replace('Salary: rising fast', 'Salary goes up fast')

# Update Speaker Notes
notes_match = re.search(r'const NOTES=\[.*?\];', html, flags=re.DOTALL)
if notes_match:
    old_notes = notes_match.group(0)
    # Just do a rough replacement in the existing notes to inject the wow factor
    new_notes = old_notes.replace('This visually proves the \'king \u2212 man + woman = queen\' claim from Part 3.', 'This visually proves our point. WOW FACTOR: Tell them the Idly/Vada analogy! "A machine doesn\'t know what Idly is. But it learns that Idly, Vada, Sambar always appear together. So it puts them close on a map. Pizza goes far away." Tell them they just learned Embeddings.')
    new_notes = new_notes.replace('A single artificial neuron \u2014 the descendant of Pitts\' 1943 idea \u2014 does three tiny things:', 'WOW FACTOR - Let\'s learn doing Filter Coffee! "Making a neural network is exactly like making the perfect Madras Filter Coffee. Decoction, milk, sugar are inputs. How much of each you pour is the weight. Too bitter? Adjust the milk weight. That is exactly what a neural network does." The students will absolutely love this.')
    html = html.replace(old_notes, new_notes)

with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Simplified file generated successfully.")
