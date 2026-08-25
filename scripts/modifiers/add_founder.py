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

founder_slide = """
<section class="slide">
<div class="eyebrow reveal">Who am I?</div>
<h2 class="reveal grad" style="font-size:3.5rem; margin-bottom: 1rem;">Mohammed Kabir.</h2>
<div class="tanglish-sub reveal" style="margin-bottom:1rem;">Founder, RiseLabs.</div>
<p class="lead reveal" style="margin-top:1rem; max-width:800px;">Before we talk about AI, let me introduce myself. I didn't get here by memorizing textbooks. I got here by building systems.</p>

<div class="reveal" style="display:grid; grid-template-columns: 1.5fr 1fr 1fr; grid-template-rows: 150px 150px; gap: 1rem; margin-top:2rem;">
  <div style="grid-row: span 2;">
    <img src="../../assets/founder_main.png" style="width:100%; height:100%; object-fit:cover; border-radius:12px; border:2px solid rgba(255,255,255,0.1); box-shadow: 0 10px 30px rgba(0,0,0,0.5);" alt="Founder" />
  </div>
  <div>
    <img src="../../assets/founder_1.jpg" style="width:100%; height:100%; object-fit:cover; border-radius:12px; border:2px solid rgba(255,255,255,0.1);" alt="Founder Action 1" />
  </div>
  <div>
    <img src="../../assets/founder_2.jpg" style="width:100%; height:100%; object-fit:cover; border-radius:12px; border:2px solid rgba(255,255,255,0.1);" alt="Founder Action 2" />
  </div>
  <div>
    <img src="../../assets/founder_3.png" style="width:100%; height:100%; object-fit:cover; border-radius:12px; border:2px solid rgba(255,255,255,0.1);" alt="Founder Action 3" />
  </div>
  <div>
    <img src="../../assets/founder_4.png" style="width:100%; height:100%; object-fit:cover; border-radius:12px; border:2px solid rgba(255,255,255,0.1);" alt="Founder Action 4" />
  </div>
</div>
</section>
"""

hook_regex = r'(<h2 class="reveal">The rules of hiring<br><span class="grad">have changed\.</span></h2>.*?<p class="kicker reveal">We will show you the exact secret to stand <em>out</em> from that pile\.</p>\n</section>)'
html = re.sub(hook_regex, r'\1\n\n' + founder_slide, html, flags=re.DOTALL)


notes_match = re.search(r'const NOTES=\[(.*?)\];\nconst slides=', html, re.DOTALL)
if notes_match:
    notes_str = "[" + notes_match.group(1) + "]"
    notes = json.loads(notes_str)
    
    # The QR slide is 0. 
    # Intro is 1. 
    # Rules of hiring is 2. 
    # Founder slide will be 3.
    notes.insert(3, "<b>Speaker Point:</b> Briefly introduce yourself. Establish credibility by showing you are a builder, not just a speaker. Point to the photos and mention a quick story about building RiseLabs.")
    
    notes_js = "const NOTES=" + json.dumps(notes) + ";"
    html = html[:notes_match.start()] + notes_js + "\nconst slides=" + html[notes_match.end():]

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Founder slide injected.")
