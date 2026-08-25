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

# 1. Hardware Interconnection Slide
hardware_slide = """
<section class="slide">
<div class="eyebrow cool reveal">Part 2.5 &middot; AI Fundamentals</div>
<h2 class="reveal grad-cool" style="font-size:3.5rem; margin-bottom: 1rem;">The Silicon Pipeline.</h2>
<div class="tanglish-sub reveal" style="margin-bottom:1rem;">Software mattum pathathu, intha machine epdi velai seithu nu purinjal thaan mass panna mudiyum.</div>
<p class="lead reveal" style="margin-top:1.6rem;">Why must a software engineer understand hardware? Because AI is extreme physics.</p>
<ul class="concepts cool reveal" style="margin-top:1.8rem;">
<li><b>ASML (Netherlands):</b> Uses lasers to build the machines.</li>
<li><b>TSMC (Taiwan):</b> Uses those machines to print circuits on atomic levels.</li>
<li><b>Nvidia (USA):</b> Designs the Matrix Multiplication architecture (GPUs).</li>
</ul>
<p class="kicker reveal">When you write <code>import torch</code>, you are commanding the most complex global supply chain in human history to turn a Trillion parameters.</p>
</section>
"""

# Find Parameters slide end
param_regex = r'(<h2 class="reveal grad-cool">Parameters &amp; Chips.*?)(</section>)'
html = re.sub(param_regex, r'\1\2\n' + hardware_slide, html, flags=re.DOTALL)


# 2. Math Need to Know
math_slide = """
<section class="slide">
<div class="eyebrow grn reveal">Part 3 &middot; The Machine</div>
<h2 class="reveal grad-grn" style="font-size:3.5rem; margin-bottom: 1rem;">The Math You Actually Need.</h2>
<div class="tanglish-sub reveal" style="margin-bottom:1rem;">Math varathu nu bayapadathinga. Ithu school math illa.</div>
<div class="mod-grid reveal" style="margin-top:2.5rem; grid-template-columns: 1fr 1fr 1fr;">
  <div class="mod"><div class="k"><i data-lucide="grid-3x3"></i> Linear Algebra</div><div class="d" style="margin-top:1rem;">Vectors & Matrices. Used to understand how data is shaped and transformed.</div></div>
  <div class="mod"><div class="k"><i data-lucide="trending-up"></i> Calculus</div><div class="d" style="margin-top:1rem;">Derivatives & Chain Rule. Used to understand how the AI learns (Backpropagation).</div></div>
  <div class="mod"><div class="k"><i data-lucide="dice-5"></i> Probability</div><div class="d" style="margin-top:1rem;">Distributions. Used to understand how the AI guesses the next token.</div></div>
</div>
</section>
"""

matrix_regex = r'(<h2 class="reveal grad-grn" style="font-size:3.5rem; margin-bottom: 1rem;">Matrix Multiplication<br>is the Universe.*?)(</section>)'
html = re.sub(matrix_regex, r'\1\2\n' + math_slide, html, flags=re.DOTALL)


# 3. Job Blueprint 1 & 2 + RiseLabs
job_slides = """
<section class="slide">
<div class="eyebrow reveal">Part 5 &middot; The Blueprint</div>
<h2 class="reveal grad" style="font-size:3.5rem; margin-bottom: 1rem;">How to get the job (Part 1).</h2>
<div class="tanglish-sub reveal" style="margin-bottom:1rem;">Titanic dataset vechi velai thedathinga.</div>
<ul class="concepts reveal" style="margin-top:1.8rem;">
<li><b>Stop doing toy datasets:</b> Everyone has Titanic and Iris on their resume. It has zero value.</li>
<li><b>Build End-to-End:</b> Don't just train a model in a Jupyter Notebook. Wrap it in a FastAPI backend, connect a database, and deploy it on AWS.</li>
<li><b>Read the Papers:</b> Stop relying on medium articles. Read the original "Attention Is All You Need" paper.</li>
</ul>
</section>

<section class="slide">
<div class="eyebrow reveal">Part 5 &middot; The Blueprint</div>
<h2 class="reveal grad" style="font-size:3.5rem; margin-bottom: 1rem;">How to get the job (Part 2).</h2>
<div class="tanglish-sub reveal" style="margin-bottom:1rem;">HR portal-la apply pandratha niruthunga.</div>
<ul class="concepts reveal" style="margin-top:1.8rem;">
<li><b>Learn System Design:</b> How do you serve 10,000 users at once without the GPU crashing? That's what companies pay for.</li>
<li><b>Open Source:</b> Contribute to LangChain, HuggingFace, or LlamaIndex on GitHub. That is your real resume.</li>
<li><b>Bypass HR:</b> Build a working prototype for a company's problem and DM the technical founder on Twitter/LinkedIn directly.</li>
</ul>
</section>

<section class="slide">
<div class="eyebrow reveal">The Founding Cohort</div>
<h2 class="reveal grad" style="font-size:4rem; margin-bottom: 1rem;">RiseLabs.</h2>
<div class="tanglish-sub reveal" style="margin-bottom:1rem;">Inga marks-a vechu vela kidaikathu. Skill-a vechu thaan kidaikum.</div>
<div class="mod-grid reveal" style="margin-top:2.5rem; grid-template-columns: 1fr 1fr;">
  <div class="mod"><div class="k"><i data-lucide="hammer"></i> Guaranteed Skill Development</div><div class="d" style="margin-top:1rem;">You won't just watch videos. You will build extreme vertical depth by creating end-to-end, production-grade AI systems from scratch.</div></div>
  <div class="mod"><div class="k"><i data-lucide="briefcase"></i> Placement Assistance</div><div class="d" style="margin-top:1rem;">No fake job guarantees. We give you the portfolio, the network, and the exact system design knowledge that makes you undeniable to top tech companies.</div></div>
</div>
</section>
"""

tshape_regex = r'(<h2 class="reveal grad">The T-Shaped Engineer.*?)(</section>)'
html = re.sub(tshape_regex, r'\1\2\n' + job_slides, html, flags=re.DOTALL)


# Update NOTES array
notes_match = re.search(r'const NOTES=\[(.*?)\];\nconst slides=', html, re.DOTALL)
if notes_match:
    notes_str = "[" + notes_match.group(1) + "]"
    notes = json.loads(notes_str)
    
    # 21: Hardware
    notes.insert(21, "<b>Speaker Point:</b> You cannot write efficient software if you don't understand the hardware executing it. If you know how GPU memory works, you become a 10x engineer because you stop writing code that bottlenecks the processor.")
    
    # 28: Math
    notes.insert(28, "<b>Speaker Point:</b> You don't need a PhD in math. You just need the intuition. Linear Algebra tells you the shape of the data. Calculus tells you how to correct the errors. Probability tells you how to guess the next step.")
    
    # 42, 43, 44: Jobs & RiseLabs
    notes.insert(42, "<b>Speaker Point:</b> HR managers use LLMs to filter resumes. If your resume looks like everyone else's, the machine deletes it. Build real systems that solve real problems.")
    notes.insert(43, "<b>Speaker Point:</b> The backdoor to the industry is GitHub and Twitter. Build something, open source it, and DM founders. They are desperate for people who can actually build.")
    notes.insert(44, "<b>Speaker Point:</b> This is what RiseLabs is about. We aren't selling you a certificate. We are giving you the exact technical depth and placement support needed to make you undeniable in 2026.")
    
    notes_js = "const NOTES=" + json.dumps(notes) + ";"
    html = html[:notes_match.start()] + notes_js + "\nconst slides=" + html[notes_match.end():]


with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Slides injected successfully.")
