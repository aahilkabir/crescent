import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import sys
import re

file_path = os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "AI Foundations Seminar - Simplified.html")

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace ML slides
old_ml_slide = '<section class="slide"><div class="eyebrow reveal">How Machines Learn — Three Ways</div><h3 class="reveal" style="margin-bottom:1.6rem;">Veetla Amma Eppadi Solli Tharanga?</h3><ul class="concepts reveal"><li><b>Supervised</b> — learning with an answer key. Like studying with solved question papers.</li><li><b>Unsupervised</b> — finding patterns with no answer key. Like sorting your wardrobe into "groups" nobody named.</li><li><b>Reinforcement</b> — learning by reward &amp; punishment. Like training a dog, or getting good at a video game.</li></ul></section>'

new_ml_slides = """<section class="slide"><div class="eyebrow reveal">How Machines Learn — Part 1</div><h3 class="reveal" style="margin-bottom:1.6rem;">Exam-kku Padikkurathu</h3><div class="tanglish-sub reveal">Pazhaya question paper vechu padikkurathu thaan Supervised Learning.</div><p class="lead reveal" style="margin-top:1.8rem;"><b>Supervised Learning</b> happens when we give the AI both the questions and the answers. Just like studying with 10 years of solved question papers, the AI looks at the answers until it memorizes the pattern.</p></section><section class="slide"><div class="eyebrow reveal">How Machines Learn — Part 2</div><h3 class="reveal" style="margin-bottom:1.6rem;">Room-a Sutham Pandrathu</h3><div class="tanglish-sub reveal">Amma illatha neram, enga edhu irukkum nu naama set pandrathu.</div><p class="lead reveal" style="margin-top:1.8rem;"><b>Unsupervised Learning</b> is finding patterns with no answer key. Nobody tells you what the groups are, but you naturally put all the shirts in one pile, and books in another. The AI does this with raw data.</p></section><section class="slide"><div class="eyebrow reveal">How Machines Learn — Part 3</div><h3 class="reveal" style="margin-bottom:1.6rem;">PUBG-la Adi Vaangi Kathukurathu</h3><div class="tanglish-sub reveal">Thappu panna adi, correct-a panna Chicken Dinner.</div><p class="lead reveal" style="margin-top:1.8rem;"><b>Reinforcement Learning</b> is learning by reward and punishment. You don't have a manual, you just land in the game, get shot (penalty), and learn never to stand there again. Over time, you become a pro.</p></section>"""

if old_ml_slide in html:
    html = html.replace(old_ml_slide, new_ml_slides)
else:
    print("Warning: old_ml_slide not found!")

# Replace ChatGPT and add RAG/FT slides
chatgpt_slide_base = '<section class="slide"><div class="eyebrow reveal">How ChatGPT Actually Works</div><h3 class="reveal">It predicts the next<br>word. That\'s the whole trick.</h3><p class="lead reveal" style="margin-top:1.6rem;">"The capital of France is ___." The model doesn\'t "know" — it computes that "Paris" is the least surprising next word. Do that one word at a time, and you get essays, code, poetry.</p><p class="kicker reveal">First it breaks text into <em>tokens</em> — chunks of words. "Unbelievable" might be "un + believ + able."</p></section>'

rag_ft_slides = """<section class="slide"><div class="eyebrow reveal">Beyond ChatGPT — RAG</div><h3 class="reveal" style="margin-bottom:1.6rem;">Open Book Exam Ezhudhalam!</h3><div class="tanglish-sub reveal">Thappa solla koodadhu nu, book-a paathu ezhudhurathu.</div><p class="lead reveal" style="margin-top:1.8rem;">ChatGPT on its own is a closed-book exam (it can hallucinate or forget). <b>Retrieval-Augmented Generation (RAG)</b> is giving the AI a textbook right before the exam. It searches the book, finds the exact paragraph, and writes the perfect, accurate answer.</p></section><section class="slide"><div class="eyebrow reveal">Beyond ChatGPT — Fine Tuning</div><h3 class="reveal" style="margin-bottom:1.6rem;">Appa-oda Bike-a Modify Pandrathu</h3><div class="tanglish-sub reveal">Pazhaya engine, aana namakku etha maari exhaust maathurathu.</div><p class="lead reveal" style="margin-top:1.8rem;">You don't build a new bike from scratch. You take the existing powerful engine (a Base Model) and modify the exhaust and paint to make it do exactly what you want. That is <b>Fine-Tuning</b>.</p></section>"""

if chatgpt_slide_base in html:
    html = html.replace(chatgpt_slide_base, chatgpt_slide_base + rag_ft_slides)
else:
    print("Warning: chatgpt_slide_base not found!")

# Update user feedback request: Father of AI
html = html.replace("Aana AI-oda Appa.", "Aana Father of AI.")

# Update Notes
old_ml_note = '"Three analogies, one per line, all from student life. \\"Supervised: you had solved papers with answers \\u2014 you learned to match question to answer. That\'s 90% of industry ML. Unsupervised: nobody tells you the categories, you discover them \\u2014 that\'s how Netflix groups viewers. Reinforcement: reward and penalty \\u2014 that\'s how AlphaGo beat the world champion, and how you subconsciously got better at PUBG.\\" <br><br>Keep it fast and fun; this is a breather before the emotional history section."'
new_ml_notes = '"This is Supervised Learning. Ask them if they ever studied by just looking at 10 years of past question papers and answer keys. \'Exam-kku padikkurathu. You look at the answers until you figure out the pattern. That is exactly what an AI does.\'", "This is Unsupervised Learning. Nobody tells you what the groups are. \'Room-a sutham pandrathu. You just naturally group similar things together. AI does this to figure out which customers are similar without being given any labels.\'", "This is Reinforcement Learning. \'PUBG-la adi vaangi kathukurathu.\' You just try something, and if it fails, you get a penalty (die). If it works, you get a reward (Chicken dinner). This is how AI learns to play games and drive cars."'

if old_ml_note in html:
    html = html.replace(old_ml_note, new_ml_notes)
else:
    print("Warning: old_ml_note not found!")


old_chatgpt_note = '"The grand finale of the box: ChatGPT, at its core, does one humble thing \\u2014 it predicts the next word. \'The capital of France is \\u2014\' and it computes that \'Paris\' is the least <i>surprising</i> continuation (there\'s Shannon again). Then it adds that word and predicts the next. One word at a time, it writes essays and code.\\" <br><br>\\"One wrinkle: it doesn\'t see words, it sees <b>tokens</b> \\u2014 pieces of words. \'Unbelievable\' might be three tokens. This is why models sometimes miscount letters, and it\'s why your API bill is measured in tokens.\\" <br><br><b>Live demo:</b> <a href=\\"https://platform.openai.com/tokenizer\\" target=\\"_blank\\">platform.openai.com/tokenizer</a> \\u2014 type a sentence, watch it shatter into tokens in real time."'

new_rag_ft_notes = r""", "Introduce RAG. 'What happens if the model doesn\'t know the answer? It hallucinates. So we give it an open book exam. RAG is literally just giving the AI the document and asking it to read from it. Very easy to build, huge demand in the market.'", "Introduce Fine Tuning. 'Appa-oda bike-a modify pandrathu. Don\'t build a massive AI from scratch. Take an open source model, and tweak it with your own data. This is what companies pay big money for.'\""""

if old_chatgpt_note in html:
    html = html.replace(old_chatgpt_note, old_chatgpt_note + new_rag_ft_notes)
else:
    print("Warning: old_chatgpt_note not found!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated slides generated successfully.")
