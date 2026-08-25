import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re

file_path = os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html")

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

replacements = {
    # Part 1 Intro
    '<h2 class="reveal" style="margin-top:1rem;">What is AI, really?</h2>': 
    '<h2 class="reveal" style="margin-top:1rem;">Josiyam Paakalama?</h2>',

    '<h3 class="reveal">Intelligence is prediction<br>under uncertainty.</h3><div class="tanglish-sub reveal">Kuthu-madhipa thappaama kanikrathu thaan intelligence.</div>': 
    '<h3 class="reveal">Cricket-la Catch<br>Pudikkurathu Eppadi?</h3><div class="tanglish-sub reveal">Kuthu-madhipa thappaama kanikrathu thaan intelligence.</div>',

    '<h3 class="reveal" style="margin-bottom:1.6rem;">And you already know all three.</h3>': 
    '<h3 class="reveal" style="margin-bottom:1.6rem;">Veetla Amma Eppadi Solli Tharanga?</h3>',

    # History
    '<h3 class="reveal">Walter Pitts:<br>a homeless teenager.</h3>': 
    '<h3 class="reveal">Veedu Illa, Degree Illa...<br>Aana AI-oda Appa.</h3>',
    
    '<h3 class="reveal">Frank Rosenblatt<br>&amp; the Perceptron.</h3>': 
    '<h3 class="reveal">Kaalathukku Mundhina<br>Thalaivan.</h3>',
    
    '<h3 class="reveal">One book froze the<br>field for 15 years.</h3>': 
    '<h3 class="reveal">Oru Puthagam...<br>15 Varusha Iruttu.</h3>',

    '<h3 class="reveal">Deep learning was born<br>in Ukraine — in 1965.</h3>': 
    '<h3 class="reveal">America Thoongum Pothu,<br>Ukraine-la Oru Mass.</h3>',

    '<h3 class="reveal">A Finnish master\'s student<br>wrote the algorithm<br>that runs all of AI.</h3>': 
    '<h3 class="reveal">Oru College Student<br>Panna Sambavam.</h3>',

    '<h3 class="reveal">AlexNet: the night<br>everything changed.</h3>': 
    '<h3 class="reveal">Oru Rathiri-la<br>Maarina Ulagam.</h3>',

    '<h3 class="reveal">"Attention is all<br>you need."</h3>': 
    '<h3 class="reveal">Google-oda Master Stroke:<br>"Attention is all you need."</h3>',

    # Math
    '<h3 class="reveal">A vector is just<br>an arrow of meaning.</h3><div class="tanglish-sub reveal">Meaning-a oru direction-la point panra arrow.</div>': 
    '<h3 class="reveal">Kolam Podalama?</h3><div class="tanglish-sub reveal">Pulligal sernthaa kolam, numbers sernthaa vector.</div>',

    '<p class="lead reveal" style="margin-top:1.6rem;">Every word, image, and user in an AI system becomes a list of numbers — a point in space. "King" is an arrow. "Queen" is a nearby arrow. AI measures meaning as <em>distance</em> and <em>direction</em>.</p>':
    '<p class="lead reveal" style="margin-top:1.6rem;">Every word is just a dot in a Kolam. A vector is a list of numbers pointing to a specific dot. AI turns words, faces, and songs into these points. It measures meaning using <em>distance</em> between the dots.</p>',

    '<h3 class="reveal">A matrix is a machine<br>that transforms space.</h3><div class="tanglish-sub reveal">Vectors-a pudichu valaikkara oru machine.</div>': 
    '<h3 class="reveal">Maavu Aatra Machine.</h3><div class="tanglish-sub reveal">Arisiya maava maathuradhu dhaan Matrix.</div>',

    '<p class="lead reveal" style="margin-top:1.6rem;">If a vector is an arrow, a <b>matrix</b> is a machine that stretches, rotates, and reshapes a whole space of arrows at once. A neural network is just a tall stack of these transformations.</p>':
    '<p class="lead reveal" style="margin-top:1.6rem;">If a vector is raw rice, a <b>matrix</b> is the grinder machine that stretches and reshapes it into batter. A neural network is just a series of these grinders stacked together.</p>',

    '<h3 class="reveal">A derivative answers<br>one question:<br><em>which way is downhill?</em></h3><div class="tanglish-sub reveal">Keezha pora vazhi edhu-nu kandupidikuradhu.</div>': 
    '<h3 class="reveal">Erakkam Enga Irukku?</h3><div class="tanglish-sub reveal">Keezha pora vazhi edhu-nu kandupidikuradhu derivative.</div>',

    '<h3 class="reveal">Gradient descent:<br>learning blindfolded<br>on a mountain.</h3><div class="tanglish-sub reveal">Kanna kattikitu malai-la irunthu keezha varadhu.</div>': 
    '<h3 class="reveal">Kanna Kattikitu<br>Kodaikanal Erakkam.</h3><div class="tanglish-sub reveal">Kuruttu-thanama keezha irangurathu thaan Gradient Descent.</div>',

    '<h3 class="reveal">Backpropagation is just<br>assigning blame.</h3><div class="tanglish-sub reveal">Thappu yaru mela-nu kandupidichu thiruthradhu.</div>': 
    '<h3 class="reveal">Kudumbathula<br>Yaar Mela Thappu?</h3><div class="tanglish-sub reveal">Thappu panna aala kandupidichu thiruthradhu thaan Backprop.</div>',

    '<h3 class="reveal">Bayes: how to update<br>a belief with evidence.</h3><div class="tanglish-sub reveal">Pudhu aadharam kedacha, pazhaya nambikkaiya maathikradhu.</div>': 
    '<h3 class="reveal">Pudhu Aadharam,<br>Pudhu Mudivu.</h3><div class="tanglish-sub reveal">Pudhu evidence kedacha pazhaya nambikkaiya maathikradhu.</div>',

    '<h3 class="reveal">Markov: the future<br>depends only on <em>now</em>.</h3><div class="tanglish-sub reveal">Nalai-kku nadakkurathu innaiku nadakradha vechu thaan.</div>': 
    '<h3 class="reveal">Nethu Ennachu-nu<br>Thevai Illa.</h3><div class="tanglish-sub reveal">Nalai-kku nadakkurathu innaiku nadakradha vechu thaan.</div>',

    '<h3 class="reveal">Shannon: information<br>is surprise.</h3><div class="tanglish-sub reveal">Ethirpaarkadha vishayam thaan mukkiyamana information.</div>': 
    '<h3 class="reveal">Chennai-la Snow Peidha?</h3><div class="tanglish-sub reveal">Ethirpaarkadha vishayam thaan Information!</div>',

    # The Machine
    '<h3 class="reveal">Embeddings: turning<br>words into map points.</h3><div class="tanglish-sub reveal">Vaarthaigal-a map-la points-a maathuradhu.</div>': 
    '<h3 class="reveal">Yaarku Idly Pudikkum?</h3><div class="tanglish-sub reveal">Orey maari words-a orey edathula vaikuradhu thaan Embedding.</div>',

    '<h3 class="reveal">Let\'s learn using<br>Filter Coffee.</h3><div class="tanglish-sub reveal">Decoction, paal, sakkarai alavu dhaan weight!</div>': 
    '<h3 class="reveal">Perfect-aana<br>Madras Filter Coffee.</h3><div class="tanglish-sub reveal">Decoction, paal, sakkarai alavu dhaan Weight!</div>'
}

for old, new in replacements.items():
    html = html.replace(old, new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updates successful")
