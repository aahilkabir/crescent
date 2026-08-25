import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import sys

file_path = os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar.html")

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    ('<h3 class="reveal">Intelligence is prediction<br>under uncertainty.</h3>', 
     '<h3 class="reveal">Intelligence is prediction<br>under uncertainty.</h3><div class="tanglish-sub reveal">Kuthu-madhipa thappaama kanikrathu thaan intelligence.</div>'),
    ('<h3 class="reveal">A vector is just<br>an arrow of meaning.</h3>',
     '<h3 class="reveal">A vector is just<br>an arrow of meaning.</h3><div class="tanglish-sub reveal">Meaning-a oru direction-la point panra arrow.</div>'),
    ('<h3 class="reveal">A matrix is a machine<br>that transforms space.</h3>',
     '<h3 class="reveal">A matrix is a machine<br>that transforms space.</h3><div class="tanglish-sub reveal">Vectors-a pudichu valaikkara oru machine.</div>'),
    ('<h3 class="reveal">A derivative answers<br>one question:<br><em>which way is downhill?</em></h3>',
     '<h3 class="reveal">A derivative answers<br>one question:<br><em>which way is downhill?</em></h3><div class="tanglish-sub reveal">Keezha pora vazhi edhu-nu kandupidikuradhu.</div>'),
    ('<h3 class="reveal">Gradient descent:<br>learning blindfolded<br>on a mountain.</h3>',
     '<h3 class="reveal">Gradient descent:<br>learning blindfolded<br>on a mountain.</h3><div class="tanglish-sub reveal">Kanna kattikitu malai-la irunthu keezha varadhu.</div>'),
    ('<h3 class="reveal">Backpropagation is just<br>assigning blame.</h3>',
     '<h3 class="reveal">Backpropagation is just<br>assigning blame.</h3><div class="tanglish-sub reveal">Thappu yaru mela-nu kandupidichu thiruthradhu.</div>'),
    ('<h3 class="reveal">Bayes: how to update<br>a belief with evidence.</h3>',
     '<h3 class="reveal">Bayes: how to update<br>a belief with evidence.</h3><div class="tanglish-sub reveal">Pudhu aadharam kedacha, pazhaya nambikkaiya maathikradhu.</div>'),
    ('<h3 class="reveal">Markov: the future<br>depends only on <em>now</em>.</h3>',
     '<h3 class="reveal">Markov: the future<br>depends only on <em>now</em>.</h3><div class="tanglish-sub reveal">Nalai-kku nadakkurathu innaiku nadakradha vechu thaan.</div>'),
    ('<h3 class="reveal">Shannon: information<br>is surprise.</h3>',
     '<h3 class="reveal">Shannon: information<br>is surprise.</h3><div class="tanglish-sub reveal">Ethirpaarkadha vishayam thaan mukkiyamana information.</div>'),
    ('<h3 class="reveal">Embeddings: turning<br>meaning into coordinates.</h3>',
     '<h3 class="reveal">Embeddings: turning<br>meaning into coordinates.</h3><div class="tanglish-sub reveal">Vaarthaigal-a map-la points-a maathuradhu.</div>'),
    ('<h3 class="reveal">Multiply, add, bend.</h3>',
     '<h3 class="reveal">Multiply, add, bend.</h3><div class="tanglish-sub reveal">Perukki, kootti, thevaiyaana valaikkuradhu.</div>'),
    ('</style>\n</head>',
     '.tanglish-sub{font-size:clamp(1rem,1.5vw,1.25rem);font-weight:500;color:var(--gold-soft);margin-top:.5rem;font-style:italic;opacity:.9;}\n</style>\n</head>')
]

for old, new in replacements:
    content = content.replace(old, new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Done")
