import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re
with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html"), "r") as f:
    html = f.read()

# Let's fix the invalid escaping in the NOTES array.
# The error is 'for.\'\", "This is' -> it should be 'for.\'", "This is' or just 'for.'", "This is'
# Actually, the string was probably ".... for.\"", "This is ..."
# Wait, let's just replace all \'\", with '", 
# Let's see how many occurrences there are:
matches = re.findall(r'\\\'\\",', html)
print(f"Found {len(matches)} occurrences of \\'\\\",")

# Also, there's `reciprocity \\` at the end of the next line!
# Let's print out the exact text around `for.'` to see.
start = html.find('big money for.')
if start != -1:
    print("Found around 'big money for.':")
    print(repr(html[start:start+100]))

