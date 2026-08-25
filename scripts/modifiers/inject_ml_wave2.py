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
    ("Attention Is All You Need", '<img src="../../assets/ml_library.png" class="person-img cool blend-screen" alt="Library" />'),
    ("Transformer Architecture", '<img src="../../assets/ml_architecture.png" class="person-img cool blend-screen" alt="Architecture" />'),
    ("Next Token Prediction", '<img src="../../assets/ml_tokens.png" class="person-img gold blend-screen" alt="Tokens" />'),
    ('"AI Unga Job-a Edukkathu"', '<img src="../../assets/ml_job.png" class="person-img grn blend-screen" alt="Job" />'),
    ("The AI Engineer Career Pathway", '<img src="../../assets/ml_pathway.png" class="person-img cool blend-screen" alt="Pathway" />')
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

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "ml-foundations.html"), "w") as f:
    f.write(html)

print("Injections complete for wave 2!")
