import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Lucide CDN to head
lucide_script = '<script src="https://unpkg.com/lucide@latest"></script>\n'
if lucide_script not in html:
    html = html.replace("</head>", lucide_script + "</head>")

# 2. Add icons to Cheat Sheet
html = html.replace('<div class="k">AI</div>', '<div class="k" style="display:flex;align-items:center;gap:0.5rem;"><i data-lucide="bot"></i> AI</div>')
html = html.replace('<div class="k">ML</div>', '<div class="k" style="display:flex;align-items:center;gap:0.5rem;"><i data-lucide="brain-circuit"></i> ML</div>')
html = html.replace('<div class="k">DL</div>', '<div class="k" style="display:flex;align-items:center;gap:0.5rem;"><i data-lucide="layers"></i> DL</div>')
html = html.replace('<div class="k">GenAI</div>', '<div class="k" style="display:flex;align-items:center;gap:0.5rem;"><i data-lucide="sparkles"></i> GenAI</div>')

# 3. Add icons to Supervised, Unsupervised, Reinforcement headers
html = html.replace('<h2 class="reveal grad" style="font-size:clamp(3rem,6vw,5.5rem);line-height:1;">Supervised<br>Learning</h2>',
                    '<h2 class="reveal grad" style="font-size:clamp(3rem,6vw,5.5rem);line-height:1;"><i data-lucide="book-open" style="width:48px;height:48px;display:block;margin-bottom:1rem;color:var(--gold);"></i>Supervised<br>Learning</h2>')
html = html.replace('<h2 class="reveal grad-cool" style="font-size:clamp(3rem,6vw,5.5rem);line-height:1;">Unsupervised<br>Learning</h2>',
                    '<h2 class="reveal grad-cool" style="font-size:clamp(3rem,6vw,5.5rem);line-height:1;"><i data-lucide="search" style="width:48px;height:48px;display:block;margin-bottom:1rem;color:var(--blue);"></i>Unsupervised<br>Learning</h2>')
html = html.replace('<h2 class="reveal grad-grn" style="font-size:clamp(3rem,6vw,5.5rem);line-height:1;">Reinforcement<br>Learning</h2>',
                    '<h2 class="reveal grad-grn" style="font-size:clamp(3rem,6vw,5.5rem);line-height:1;"><i data-lucide="gamepad-2" style="width:48px;height:48px;display:block;margin-bottom:1rem;color:var(--green);"></i>Reinforcement<br>Learning</h2>')

# 4. Add icons to Tools grid
html = html.replace('<div class="k">Hugging Face</div>', '<div class="k" style="display:flex;align-items:center;gap:0.5rem;"><i data-lucide="box"></i> Hugging Face</div>')
html = html.replace('<div class="k">PyTorch</div>', '<div class="k" style="display:flex;align-items:center;gap:0.5rem;"><i data-lucide="flame"></i> PyTorch</div>')
html = html.replace('<div class="k">CUDA</div>', '<div class="k" style="display:flex;align-items:center;gap:0.5rem;"><i data-lucide="cpu"></i> CUDA</div>')

# 5. Initialize Lucide at the end of the script tag
lucide_init = "lucide.createIcons();\n"
if "lucide.createIcons();" not in html:
    html = html.replace("</script>\n</body>", lucide_init + "</script>\n</body>")

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Injected Lucide icons.")
