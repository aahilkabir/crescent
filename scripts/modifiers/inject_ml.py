import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "ml-foundations.html"), "r") as f:
    html = f.read()

# 1. Inject CSS
css_to_add = """
.person-img {
  position: absolute;
  right: 5vw;
  bottom: 0;
  height: 80vh;
  object-fit: contain;
  z-index: 1;
  opacity: 0;
  transform: translateX(40px);
  transition: opacity 1.2s cubic-bezier(0.22, 0.61, 0.36, 1), transform 1.2s cubic-bezier(0.22, 0.61, 0.36, 1);
  filter: grayscale(40%) contrast(1.1) brightness(0.9);
  mask-image: linear-gradient(to top, transparent 0%, black 25%, black 95%, transparent 100%);
  -webkit-mask-image: linear-gradient(to top, transparent 0%, black 25%, black 95%, transparent 100%);
}
.slide.active .person-img { opacity: 0.6; transform: translateX(0); }
.person-img.cool { filter: drop-shadow(0 0 40px rgba(41,151,255,0.25)) grayscale(40%) contrast(1.1); }
.person-img.grn { filter: drop-shadow(0 0 40px rgba(95,211,155,0.25)) grayscale(40%) contrast(1.1); }
.person-img.gold { filter: drop-shadow(0 0 40px rgba(212,162,78,0.25)) grayscale(40%) contrast(1.1); }
.person-img.blend-screen { mix-blend-mode: screen; right: -5vw; height: 90vh; }
.slide.has-img { align-items: flex-start; }
.slide.has-img > *:not(.person-img):not(.glow) { max-width: 55vw; position: relative; z-index: 2; }
.slide.center.has-img { text-align: left; }
.slide.center.has-img .lead { margin-left: 0; }
</style>
"""

if '.person-img {' not in html:
    html = html.replace('</style>', css_to_add)

# 2. Inject Images into Slides
injections = [
    ("Idli Maavu Madiri", '<img src="../../assets/ml_idli.png" class="person-img gold blend-screen" alt="Idli" />'),
    ("Malai Erangirathu Madiri", '<img src="../../assets/ml_mountain.png" class="person-img cool blend-screen" alt="Mountain" />'),
    ("CNNs — Convolutional", '<img src="../../assets/ml_lens.png" class="person-img cool blend-screen" alt="Lens" />'),
    ("Google Maps Madiri", '<img src="../../assets/ml_map.png" class="person-img grn blend-screen" alt="Map" />'),
    ("Filter Coffee Madiri", '<img src="../../assets/ml_coffee.png" class="person-img gold blend-screen" alt="Coffee" />'),
    ("The Bridge", '<img src="../../assets/ml_bridge.png" class="person-img gold blend-screen" alt="Bridge" />')
]

# The slides are in a JS array `const S = [ {bg: 'bg-b', html: `...`}, ... ];`
for keyword, img_tag in injections:
    # Find the slide containing the keyword
    # We look for the closing backtick of that slide's html
    pattern = r'({[^}]*html:`[^`]*?' + re.escape(keyword) + r'[^`]*?)(`})'
    match = re.search(pattern, html, re.DOTALL)
    if match and '<img' not in match.group(1): # prevent double injection
        # Also need to add .has-img to the slide class if possible, but the JS creates the slide div dynamically!
        # Wait, the JS says:
        # div.className = `slide ${s.bg}` + (i===0?' active':'');
        # It doesn't use classes from the HTML string for the section.
        pass

# Ah, wait! `ml-foundations.html` DOES NOT use `<section class="slide">` in the HTML string!
# The JS does:
# div.className = `slide ${s.bg}` + (i===0?' active':'');
# div.innerHTML = s.html;
# So if we want to add `.has-img` to the slide div, we need to modify the JS, or we can just wrap the image tag and rely on CSS hitting the `.slide:has(.person-img)`? 
# `:has()` is widely supported now!
# Let's use `.slide:has(.person-img)` instead of `.slide.has-img` in CSS! That's brilliant and requires zero JS changes.

css_to_add_modern = """
.person-img {
  position: absolute;
  right: 5vw;
  bottom: 0;
  height: 80vh;
  object-fit: contain;
  z-index: 1;
  opacity: 0;
  transform: translateX(40px);
  transition: opacity 1.2s cubic-bezier(0.22, 0.61, 0.36, 1), transform 1.2s cubic-bezier(0.22, 0.61, 0.36, 1);
  filter: grayscale(40%) contrast(1.1) brightness(0.9);
  mask-image: linear-gradient(to top, transparent 0%, black 25%, black 95%, transparent 100%);
  -webkit-mask-image: linear-gradient(to top, transparent 0%, black 25%, black 95%, transparent 100%);
}
.slide.active .person-img { opacity: 0.6; transform: translateX(0); }
.person-img.cool { filter: drop-shadow(0 0 40px rgba(41,151,255,0.25)) grayscale(40%) contrast(1.1); }
.person-img.grn { filter: drop-shadow(0 0 40px rgba(95,211,155,0.25)) grayscale(40%) contrast(1.1); }
.person-img.gold { filter: drop-shadow(0 0 40px rgba(212,162,78,0.25)) grayscale(40%) contrast(1.1); }
.person-img.blend-screen { mix-blend-mode: screen; right: -5vw; height: 90vh; }
.slide:has(.person-img) { align-items: flex-start; }
.slide:has(.person-img) > *:not(.person-img):not(.glow) { max-width: 55vw; position: relative; z-index: 2; }
.slide.center:has(.person-img) { text-align: left; }
.slide.center:has(.person-img) .lead { margin-left: 0; }
</style>
"""

# Reset html
with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "ml-foundations.html"), "r") as f:
    html = f.read()

if '.person-img {' not in html:
    html = html.replace('</style>', css_to_add_modern)

for keyword, img_tag in injections:
    pattern = r'({[^}]*html:`[^`]*?' + re.escape(keyword) + r'[^`]*?)(`})'
    
    def repl(m):
        content = m.group(1)
        if '<img' not in content:
            # Inject just before the closing backtick
            return content + '\n' + img_tag + '\n' + m.group(2)
        return m.group(0)
        
    html = re.sub(pattern, repl, html, flags=re.DOTALL)

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "ml-foundations.html"), "w") as f:
    f.write(html)

print("Injections complete!")
