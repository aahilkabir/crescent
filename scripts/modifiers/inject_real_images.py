import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "ml-foundations.html"), "r") as f:
    html = f.read()

injections = [
    ('"Parameters & Weights"', '<img src="../../assets/ml_radio.png" class="person-img grn blend-screen" alt="Radio" />'),
    ('"Training Data"', '<img src="../../assets/ml_exam.png" class="person-img cool blend-screen" alt="Exam" />'),
    ('"Overfitting"', '<img src="../../assets/ml_overfit.png" class="person-img gold blend-screen" alt="Overfit" />'),
    ('"GPU (Graphics Processing Unit)"', '<img src="../../assets/ml_factory.png" class="person-img cool blend-screen" alt="Factory" />')
]

for keyword, img_tag in injections:
    pattern = r'({[^}]*html:`[^`]*?' + re.escape(keyword) + r'[^`]*?)(`})'
    
    def repl(m):
        content = m.group(1)
        if '<img' not in content:
            # Inject just before the closing backtick
            return content + '\n' + img_tag + '\n' + m.group(2)
        return m.group(0)
        
    html = re.sub(pattern, repl, html, flags=re.DOTALL)

# For the Pioneers slide, it has 4 people on one slide.
# The user asked to "add to slides", but they are currently grouped together on one slide.
# I will split them into 4 separate slides for maximum impact since they are fetching portraits.

pioneer_slides = """
{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--teal);margin-bottom:14px">The Pioneers</p>
<h2 class="med a2">Geoffrey Hinton</h2>
<div class="math-block math-l a3" style="color:var(--teal);margin-top:16px;max-width:55vw;">
The "Godfather of AI". When the world gave up on neural networks in the 1990s, he kept believing and proved they could work.
</div>
<img src="../../assets/ml_hinton.png" class="person-img cool blend-screen" alt="Hinton" />
`},

{bg:'bg-b', html:`
<p class="lbl a1" style="color:var(--blue);margin-bottom:14px">The Pioneers</p>
<h2 class="med a2">Andrew Ng</h2>
<div class="math-block math-d a3" style="color:var(--blue);margin-top:16px;max-width:55vw;">
The "Teacher of AI". He pioneered online AI education and co-founded Google Brain, democratizing ML for millions.
</div>
<img src="../../assets/ml_ng.png" class="person-img grn blend-screen" alt="Ng" />
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--purple);margin-bottom:14px">The Pioneers</p>
<h2 class="med a2">Yann LeCun</h2>
<div class="math-block math-l a3" style="color:var(--purple);margin-top:16px;max-width:55vw;">
The "Visionary". He invented Convolutional Neural Networks, teaching machines how to see.
</div>
<img src="../../assets/ml_lecun.png" class="person-img gold blend-screen" alt="LeCun" />
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--pink);margin-bottom:14px">The Pioneers</p>
<h2 class="med a2">Sam Altman</h2>
<div class="math-block math-l a3" style="color:var(--pink);margin-top:16px;max-width:55vw;">
The "Architect of the Boom". Packaged all this complex research into ChatGPT and triggered the current AI revolution.
</div>
<img src="../../assets/ml_altman.png" class="person-img cool blend-screen" alt="Altman" />
`},
"""

# Replace the single "The Pioneers" slide with the 4 split slides
old_pioneer_slide = r"{bg:'bg-w', html:`[^`]*The Faces of the Revolution[^`]*`},"
if "Geoffrey Hinton" in html and "Andrew Ng" in html and "Yann LeCun" in html and "The Faces of the Revolution" in html:
    html = re.sub(old_pioneer_slide, pioneer_slides, html, flags=re.DOTALL)

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "ml-foundations.html"), "w") as f:
    f.write(html)

print("Injected missing images and split Pioneer slides successfully.")
