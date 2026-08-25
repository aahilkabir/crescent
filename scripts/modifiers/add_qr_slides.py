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

qr_register_slide = """
<!-- 0. REGISTER -->
<section class="slide center active"><div class="glow g1"></div>
<div class="eyebrow reveal">Welcome</div>
<h2 class="reveal" style="font-size:3.5rem; margin-bottom: 1rem;">Scan to <span class="grad">Register</span>.</h2>
<img src="../../assets/qr_register.png" class="reveal" style="display:block; margin: 2rem auto; max-width: 280px; border-radius: 16px; border: 6px solid white; box-shadow: 0 20px 50px rgba(0,0,0,0.5);" alt="Register QR" />
<p class="lead reveal" style="margin-top:2rem;">Please register before the seminar begins.</p>
</section>
"""

# Remove 'active' from the original first slide
html = html.replace('<section class="slide center active">', '<section class="slide center">')

# Insert before <!-- 1. INTRO -->
html = html.replace('<!-- 1. INTRO -->', qr_register_slide + '\n<!-- 1. INTRO -->')


qr_cert_slide = """
<section class="slide center">
<div class="eyebrow reveal">Thank You</div>
<h2 class="reveal" style="font-size:3.5rem; margin-bottom: 1rem;">Claim your <span class="grad">Certificate</span>.</h2>
<img src="../../assets/qr_certificate.png" class="reveal" style="display:block; margin: 2rem auto; max-width: 280px; border-radius: 16px; border: 6px solid white; box-shadow: 0 20px 50px rgba(0,0,0,0.5);" alt="Certificate QR" />
<p class="lead reveal" style="margin-top:2rem;">Scan the QR code to receive your participation certificate.</p>
</section>
"""

# Insert after the last slide
html = html.replace('<div class="price-badge reveal"><div class="pl">Founding Cohort · This Room Only</div><div class="pv" style="font-size:clamp(2rem,5vw,3.2rem);">Talk to me →</div></div>\n</section>', '<div class="price-badge reveal"><div class="pl">Founding Cohort · This Room Only</div><div class="pv" style="font-size:clamp(2rem,5vw,3.2rem);">Talk to me →</div></div>\n</section>\n\n' + qr_cert_slide)


# Update NOTES array
notes_match = re.search(r'const NOTES=\[(.*?)\];\nconst slides=', html, re.DOTALL)
if notes_match:
    notes_str = "[" + notes_match.group(1) + "]"
    notes = json.loads(notes_str)
    
    # Insert at beginning
    notes.insert(0, "<b>Speaker Point:</b> Welcome everyone. Please scan the QR code to register your attendance before we begin.")
    
    # Append at end
    notes.append("<b>Speaker Point:</b> Thank you for your time. Scan this QR code to claim your certificate of participation.")
    
    notes_js = "const NOTES=" + json.dumps(notes) + ";"
    html = html[:notes_match.start()] + notes_js + "\nconst slides=" + html[notes_match.end():]

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("QR slides injected successfully.")
