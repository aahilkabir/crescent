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

math_slide_end_regex = r'(<h2 class="reveal grad-grn".*?The Math You Actually Need\.</h2.*?</section>)'

new_math_slides = """
<section class="slide center has-img">
<div class="eyebrow grn reveal">Part 3 &middot; The Math</div>
<h3 class="reveal" style="font-size:3rem;">Why did we study<br><span class="grad-grn">Linear Algebra?</span></h3>
<p class="lead reveal" style="margin-top:2rem;"><b>(Vectors &amp; Matrices)</b></p>
<ul class="concepts grn reveal" style="margin-top:2rem; list-style:none; text-align:left; max-width:800px; margin-left:auto; margin-right:auto;">
<li><i data-lucide="check-circle-2" style="color:var(--green); margin-right:12px; vertical-align:-5px;"></i><b>Eigenvectors:</b> Used to build Google's original PageRank algorithm.</li>
<li><i data-lucide="check-circle-2" style="color:var(--green); margin-right:12px; vertical-align:-5px;"></i><b>Dimensionality Reduction (PCA):</b> Used in facial recognition to compress millions of pixels into key features.</li>
<li><i data-lucide="check-circle-2" style="color:var(--green); margin-right:12px; vertical-align:-5px;"></i><b>Matrix Multiplication:</b> The exact mechanism behind ChatGPT's 1.7 Trillion parameters.</li>
</ul>
</section>

<section class="slide center has-img">
<div class="eyebrow grn reveal">Part 3 &middot; The Math</div>
<h3 class="reveal" style="font-size:3rem;">Why did we study<br><span class="grad-grn">Calculus?</span></h3>
<p class="lead reveal" style="margin-top:2rem;"><b>(Derivatives &amp; The Chain Rule)</b></p>
<ul class="concepts grn reveal" style="margin-top:2rem; list-style:none; text-align:left; max-width:800px; margin-left:auto; margin-right:auto;">
<li><i data-lucide="check-circle-2" style="color:var(--green); margin-right:12px; vertical-align:-5px;"></i><b>Derivatives (dy/dx):</b> Calculates exactly how much the AI's guess was wrong (the Loss gradient).</li>
<li><i data-lucide="check-circle-2" style="color:var(--green); margin-right:12px; vertical-align:-5px;"></i><b>The Chain Rule:</b> Powers <b>Backpropagation</b>. It sends the error signal backward through 100+ layers of the neural network to adjust the weights.</li>
<li><i data-lucide="check-circle-2" style="color:var(--green); margin-right:12px; vertical-align:-5px;"></i><b>Bottom Line:</b> Without Calculus, an AI cannot learn from its mistakes.</li>
</ul>
</section>

<section class="slide center has-img">
<div class="eyebrow grn reveal">Part 3 &middot; The Math</div>
<h3 class="reveal" style="font-size:3rem;">Why did we study<br><span class="grad-grn">Probability &amp; Stats?</span></h3>
<p class="lead reveal" style="margin-top:2rem;"><b>(Markov Chains &amp; Normal Distribution)</b></p>
<ul class="concepts grn reveal" style="margin-top:2rem; list-style:none; text-align:left; max-width:800px; margin-left:auto; margin-right:auto;">
<li><i data-lucide="check-circle-2" style="color:var(--green); margin-right:12px; vertical-align:-5px;"></i><b>Markov Chains:</b> State transitions based on probability. This is exactly how self-driving cars predict pedestrian movement.</li>
<li><i data-lucide="check-circle-2" style="color:var(--green); margin-right:12px; vertical-align:-5px;"></i><b>Generative AI:</b> When ChatGPT types a sentence, it doesn't "think." It uses probability distributions to statistically guess the most mathematically likely next word.</li>
</ul>
</section>
"""

# Insert the HTML
html = re.sub(math_slide_end_regex, r'\1\n\n' + new_math_slides, html, flags=re.DOTALL)

# Insert the notes
notes_match = re.search(r'const NOTES=\[(.*?)\];\nconst slides=', html, re.DOTALL)
if notes_match:
    notes_str = "[" + notes_match.group(1) + "]"
    notes = json.loads(notes_str)
    
    # Find the index of the math intro note
    math_note = "<b>Speaker Point:</b> You don't need a PhD in math. You just need the intuition. Linear Algebra tells you the shape of the data. Calculus tells you how to correct the errors. Probability tells you how to guess the next step."
    if math_note in notes:
        idx = notes.index(math_note)
        
        # Insert notes in reverse order so they end up in 1, 2, 3 order after idx
        notes.insert(idx + 1, "<b>The Deep Insight:</b> Next time you look at a Matrix in your textbook, remember that multiplying them together is exactly how ChatGPT processes language.")
        notes.insert(idx + 2, "<b>The Deep Insight:</b> Calculus is the engine of learning. The Chain Rule isn't just an exam question, it is the exact mathematical algorithm (Backpropagation) that allowed AI to surpass human intelligence.")
        notes.insert(idx + 3, "<b>The Deep Insight:</b> Generative AI is just probability at a massive scale. It's essentially a giant Markov Chain guessing the next word.")
        
        notes_js = "const NOTES=" + json.dumps(notes) + ";"
        html = html[:notes_match.start()] + notes_js + "\nconst slides=" + html[notes_match.end():]
        print("Inserted slides and notes.")
    else:
        print("Math note not found.")

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "w", encoding="utf-8") as f:
    f.write(html)
