import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re
with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html"), "r") as f:
    html = f.read()

# We will just replace all `\", ` with `", ` since an array of strings in JS is separated by `", "`
# Wait, if the string actually ends with an escaped quote, it would be `\"", `!
# Let's see if replacing `\", ` with `", ` fixes the node syntax error.

# First let's extract the script and test our replacements on it.
script_match = re.search(r'<script>([\s\S]*?)</script>', html)
script = script_match.group(1)

# Fix: Replace `\", ` with `", `
fixed_script = script.replace('\\", "', '", "')

# Let's save and test with node.
with open("test_fixed.js", "w") as f:
    f.write(fixed_script)
