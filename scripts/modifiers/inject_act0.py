import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "ml-foundations.html"), "r") as f:
    html = f.read()

act_0_slides = """
// ──────── ACT 0: THE PANIC ────────
{bg:'bg-b', html:`
<div class="glow" style="width:600px;height:600px;background:var(--red);top:-10%;right:-5%"></div>
<p class="pill a1" style="background:rgba(255,59,48,.12);color:var(--red)">Act 0</p>
<h2 class="hero a2" style="font-size:clamp(36px,5.5vw,76px)">The AI<br><span class="grc">Panic.</span></h2>
<p class="sub a3" style="margin-top:18px;opacity:.5">You hear these words in every meeting, on every news channel, and on every LinkedIn post. But what do they actually mean?</p>
<p class="a4" style="font-size:clamp(12px,1vw,14px);opacity:.3;margin-top:8px">Let's decode the buzzwords.</p>
<img src="../../assets/ml_panic.png" class="person-img cool blend-screen" alt="Panic" />
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--blue);margin-bottom:14px">Buzzword #1</p>
<h2 class="med a2">"Algorithm"</h2>
<div class="math-block math-l a3" style="color:var(--blue);margin-top:16px;">
Question: What does this actually mean?<br><br>
Real-Life Answer:<br>
It's just a cooking recipe. Step 1, Step 2, Step 3. If you follow the steps exactly, you get the dish. If you miss a step, it fails.
</div>
<img src="../../assets/ml_recipe.png" class="person-img gold blend-screen" alt="Recipe" />
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--purple);margin-bottom:14px">Buzzword #2</p>
<h2 class="med a2">"Parameters & Weights"</h2>
<div class="math-block math-l a3" style="color:var(--purple);margin-top:16px;">
Question: What does this actually mean?<br><br>
Real-Life Answer:<br>
Think of an old radio. The parameters are the tuning knobs for volume, bass, and frequency. You twist and adjust them until the music comes through perfectly clear.
</div>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--green);margin-bottom:14px">Buzzword #3</p>
<h2 class="med a2">"Training Data"</h2>
<div class="math-block math-l a3" style="color:var(--green);margin-top:16px;">
Question: What does this actually mean?<br><br>
Real-Life Answer:<br>
It is like solving the past 10 years of Anna University question papers before a final exam. The more diverse the past papers, the better you perform on the real test.
</div>
`},

{bg:'bg-b', html:`
<p class="lbl a1" style="color:var(--orange);margin-bottom:14px">Buzzword #4</p>
<h2 class="med a2">"Overfitting"</h2>
<div class="math-block math-d a3" style="color:var(--orange);margin-top:16px;">
Question: What does this actually mean?<br><br>
Real-Life Answer:<br>
Mugging up the textbook line-by-line. You score 100% on the practice test, but when the professor twists the question slightly in the real exam, you fail completely.
</div>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--pink);margin-bottom:14px">Buzzword #5</p>
<h2 class="med a2">"GPU (Graphics Processing Unit)"</h2>
<div class="math-block math-l a3" style="color:var(--pink);margin-top:16px;">
Question: Why does AI need GPUs instead of CPUs?<br><br>
Real-Life Answer:<br>
A CPU is like 4 genius professors solving complex math one by one. A GPU is like 10,000 average students working together to solve thousands of simple math problems at the exact same time.
</div>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--teal);margin-bottom:14px">The Pioneers</p>
<h2 class="med a2">The Faces of the Revolution</h2>
<div class="row a3" style="margin-top:20px;">
<div class="card card-l" style="border-top:3px solid var(--blue)">
<div class="ct" style="color:var(--blue)">Geoffrey Hinton</div>
<div class="cb">The "Godfather of AI". When the world gave up on neural networks in the 1990s, he kept believing.</div>
</div>
<div class="card card-l" style="border-top:3px solid var(--purple)">
<div class="ct" style="color:var(--purple)">Andrew Ng</div>
<div class="cb">The "Teacher of AI". He pioneered online AI education and co-founded Google Brain.</div>
</div>
</div>
<div class="row a4" style="margin-top:10px;">
<div class="card card-l" style="border-top:3px solid var(--green)">
<div class="ct" style="color:var(--green)">Yann LeCun</div>
<div class="cb">The "Visionary". He invented Convolutional Neural Networks, teaching machines how to see.</div>
</div>
<div class="card card-l" style="border-top:3px solid var(--orange)">
<div class="ct" style="color:var(--orange)">Sam Altman</div>
<div class="cb">The "Architect of the Boom". Packaged all this research into ChatGPT and triggered the current panic.</div>
</div>
</div>
`},
"""

# Inject right before ACT 1
act1_marker = "// ──────── ACT 1: WHAT IS ML ────────"
if act1_marker in html and "ACT 0" not in html:
    html = html.replace(act1_marker, act_0_slides + "\n" + act1_marker)
    with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "ml-foundations.html"), "w") as f:
        f.write(html)
    print("Injected Act 0 successfully.")
else:
    print("Could not find insertion point or Act 0 already exists.")
