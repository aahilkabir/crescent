import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re

with open(os.path.join(PROJECT_ROOT, "generate_55_slides.py"), "r") as f:
    content = f.read()

# We need to extract the raw concepts.
# A concept block typically starts with `# CONCEPT XX: NAME` or `# ENGINE CONCEPT XX: NAME`
# But because I modified them to match the new numbering (01, 02, etc.), I can find them by their Big Hero Reveal Names!

def extract_concept(reveal_title):
    # Regex to find the start of the concept (starts with # CONCEPT or # Slide or similar just before the story)
    # The block ends right before the next concept or section header
    pattern = r"(# CONCEPT \d+: .*?|# ENGINE CONCEPT \d+: .*?)(?=\n# CONCEPT |\n# ENGINE CONCEPT |\n# ====================================================)"
    matches = list(re.finditer(pattern, content, re.DOTALL))
    for m in matches:
        if reveal_title in m.group(0):
            return m.group(0)
    return ""

def extract_system_design():
    # System design concepts start around Slide 51
    # Find Section 5 header
    pattern = r"(# ====================================================\n# SECTION 5: SYSTEM DESIGN.*?\n# ====================================================.*?)(?=\n# ====================================================\n# SECTION 6)"
    m = re.search(pattern, content, re.DOTALL)
    return m.group(1) if m else ""

# Extract all concepts
ram = extract_concept("RAM MEMORY LOCKERS")
stack = extract_concept("STACK MEMORY")
heap = extract_concept("HEAP MEMORY")
recursion = extract_concept("CALL STACK &amp; RECURSION")
big_o = extract_concept("BIG O SCALABILITY")

abstraction = extract_concept("ABSTRACTION")
inheritance = extract_concept("INHERITANCE")
array_offsets = extract_concept("ARRAY OFFSETS")
functions = extract_concept("FUNCTIONS")
immutability = extract_concept("IMMUTABILITY")
type_overflow = extract_concept("TYPE OVERFLOW")
conditionals = extract_concept("CONDITIONALS")
safety_loops = extract_concept("SAFETY LOOPS")
hash_maps = extract_concept("HASH MAPS")
error_traps = extract_concept("DEFENSIVE ERROR TRAPS")
var_scope = extract_concept("VARIABLE SCOPE")
pass_by_ref = extract_concept("PASS-BY-REFERENCE")
queues = extract_concept("QUEUES (FIFO)")


# Extract headers
header_pattern = r"(.*?)(?=\n# ====================================================\n# SECTION 2)"
m_head = re.search(header_pattern, content, re.DOTALL)
header = m_head.group(1)

footer_pattern = r"(# ====================================================\n# SECTION 6.*)"
m_foot = re.search(footer_pattern, content, re.DOTALL)
footer = m_foot.group(1)


# Rename the badges and comments to their original numbers
# We can do some simple string replacements for the badges.
def renumber_engine(text, num):
    text = re.sub(r"ENGINE CONCEPT \d+", f"ENGINE CONCEPT {num}", text)
    text = re.sub(r"ENGINE CONCEPT #\d+ REVEAL", f"ENGINE CONCEPT #0{num} REVEAL", text)
    return text

def renumber_concept(text, num):
    text = re.sub(r"CONCEPT \d+", f"CONCEPT {num}", text)
    text = re.sub(r"CONCEPT #\d+ REVEAL", f"CONCEPT #{num:02d} REVEAL", text)
    return text

ram = renumber_engine(ram, 1)
stack = renumber_engine(stack, 2)
heap = renumber_engine(heap, 3)
recursion = renumber_engine(recursion, 4)
big_o = renumber_engine(big_o, 5)

abstraction = renumber_concept(abstraction, 1)
inheritance = renumber_concept(inheritance, 2)
array_offsets = renumber_concept(array_offsets, 3)
functions = renumber_concept(functions, 4)
immutability = renumber_concept(immutability, 5)
type_overflow = renumber_concept(type_overflow, 6)
conditionals = renumber_concept(conditionals, 7)
safety_loops = renumber_concept(safety_loops, 8)
hash_maps = renumber_concept(hash_maps, 9)
error_traps = renumber_concept(error_traps, 10)
var_scope = renumber_concept(var_scope, 11)
pass_by_ref = renumber_concept(pass_by_ref, 12)
queues = renumber_concept(queues, 13)


# Rebuild the file
new_content = header + "\n"

# Section 2
new_content += """# ====================================================
# SECTION 2: COMPUTER ENGINE UNDER THE HOOD (STACK, HEAP, RECURSION, BIG O)
# ====================================================
""" + "\n"
new_content += ram + "\n\n"
new_content += stack + "\n\n"
new_content += heap + "\n\n"
new_content += recursion + "\n\n"
new_content += big_o + "\n\n"

# Section 3
new_content += """# ====================================================
# SECTION 3: 13 CORE CS CONCEPTS IN TANGLISH
# ====================================================

# Foundations Roadmap Part 1 (Concepts 1 - 5)
slides_html.append(\"\"\"
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="layers"></i> SECTION 3 · FOUNDATIONS ROADMAP (1 - 5)</div>
  <h2 class="reveal">Concepts 1 to 5</h2>
  <div class="reveal" style="width:100%; max-width:900px; background:#111; border:1px solid var(--border); border-radius:12px; padding:1rem 2rem;">
    <table>
      <tr><th>#</th><th>Real World Story</th><th>Concept Name</th></tr>
      <tr><td>01</td><td>A.R. Rahman Concert Sound Board</td><td><b style="color:var(--gold);">Abstraction</b></td></tr>
      <tr><td>02</td><td>Vijay Movie Base Template Reuse</td><td><b style="color:var(--blue);">Inheritance</b></td></tr>
      <tr><td>03</td><td>Sathyam Cinemas Row A Seat Index</td><td><b style="color:var(--accent);">Array Offsets</b></td></tr>
      <tr><td>04</td><td>Swiggy Delivery Partner Subcontract</td><td><b style="color:var(--green);">Functions</b></td></tr>
      <tr><td>05</td><td>Exam Hall Ticket vs Mobile Data</td><td><b style="color:var(--purple);">Immutability</b></td></tr>
    </table>
  </div>
</section>
\"\"\")
notes.append(\"\"\"<b>Foundations Roadmap:</b> Concepts 1 through 5 overview table.\"\"\")

""" + "\n"
new_content += abstraction + "\n\n"
new_content += inheritance + "\n\n"
new_content += array_offsets + "\n\n"
new_content += functions + "\n\n"
new_content += immutability + "\n\n"

new_content += """# Foundations Roadmap Part 2 (Concepts 6 - 10)
slides_html.append(\"\"\"
<section class="slide">
  <div class="badge red reveal"><i data-lucide="layers"></i> SECTION 3 · FOUNDATIONS ROADMAP (6 - 10)</div>
  <h2 class="reveal">Concepts 6 to 10</h2>
  <div class="reveal" style="width:100%; max-width:900px; background:#111; border:1px solid var(--border); border-radius:12px; padding:1rem 2rem;">
    <table>
      <tr><th>#</th><th>Real World Story</th><th>Concept Name</th></tr>
      <tr><td>06</td><td>5L Bisleri Can in 200ml Tea Glass</td><td><b style="color:var(--red);">Type Overflow</b></td></tr>
      <tr><td>07</td><td>EA Cinema Gate Ticket Check</td><td><b style="color:var(--gold);">Conditionals</b></td></tr>
      <tr><td>08</td><td>Max Showroom Dress Trial Room</td><td><b style="color:var(--blue);">Safety Loops</b></td></tr>
      <tr><td>09</td><td>Marina Beach Token Parking</td><td><b style="color:var(--green);">Hash Maps</b></td></tr>
      <tr><td>10</td><td>Tagore Canteen UPS Fallback</td><td><b style="color:var(--purple);">Error Traps</b></td></tr>
    </table>
  </div>
</section>
\"\"\")
notes.append(\"\"\"<b>Foundations Roadmap:</b> Concepts 6 through 10 overview table.\"\"\")

""" + "\n"
new_content += type_overflow + "\n\n"
new_content += conditionals + "\n\n"
new_content += safety_loops + "\n\n"
new_content += hash_maps + "\n\n"
new_content += error_traps + "\n\n"

new_content += var_scope + "\n\n"
new_content += pass_by_ref + "\n\n"
new_content += queues + "\n\n"

new_content += extract_system_design() + "\n\n"
new_content += footer + "\n"

with open(os.path.join(PROJECT_ROOT, "generate_55_slides.py"), "w") as f:
    f.write(new_content)

print("Successfully reverted generate_55_slides.py to previous structure!")
