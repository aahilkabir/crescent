import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re
with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html"), "r") as f:
    html = f.read()

# Replace the broken JS syntax
fixed_html = html.replace('\\", "', '", "')

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html"), "w") as f:
    f.write(fixed_html)
