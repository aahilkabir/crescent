import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

with open("part1.py", "r") as f1, open("part2.py", "r") as f2, open("part3.py", "r") as f3:
    content = f1.read() + "\n" + f2.read() + "\n" + f3.read()

with open(os.path.join(PROJECT_ROOT, "generate_55_slides.py"), "w") as out:
    out.write(content)

print("Successfully merged part1.py, part2.py, and part3.py into generate_55_slides.py")
