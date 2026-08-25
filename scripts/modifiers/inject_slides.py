import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import re

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "r", encoding="utf-8") as f:
    html = f.read()

# 1. Insert Comparison Table
comp_table = """
<section class="slide">
<div class="eyebrow reveal">Terminology &middot; The Basics</div>
<h2 class="reveal">The Cheat Sheet.</h2>
<p class="lead reveal" style="margin-top:1.4rem;">Don't get confused by the buzzwords anymore.</p>
<div class="mod-grid reveal" style="margin-top:2.5rem; grid-template-columns: 1fr 1fr;">
  <div class="mod"><div class="k">AI</div><div class="t" style="margin:1rem 0;">Artificial Intelligence</div><div class="d">Any machine that mimics human behavior. Mostly rule-based. (Smart Washing Machine)</div></div>
  <div class="mod"><div class="k">ML</div><div class="t" style="margin:1rem 0;">Machine Learning</div><div class="d">Machines that learn from data without explicit rules. (Bicycle Riding)</div></div>
  <div class="mod"><div class="k">DL</div><div class="t" style="margin:1rem 0;">Deep Learning</div><div class="d">ML using multi-layered Neural Networks. (Corporate Hierarchy)</div></div>
  <div class="mod" style="border-color:var(--gold); background:rgba(212,162,78,.05);"><div class="k">GenAI</div><div class="t" style="margin:1rem 0;">Generative AI</div><div class="d">Deep Learning that creates brand new data. (Making a new Dosa)</div></div>
</div>
</section>

"""
html = html.replace("<!-- THE 3 TYPES OF ML -->", comp_table + "<!-- THE 3 TYPES OF ML -->")

# 2. Insert Tokens, Parameters, Models
fundamentals = """
<section class="slide has-img">
<div class="eyebrow cool reveal">Part 2.5 &middot; AI Fundamentals</div>
<h2 class="reveal grad-cool">Tokens.</h2>
<div style="max-width: 55vw;">
<h3 class="reveal" style="margin-top:1rem;">Machines don't read words.</h3>
<p class="lead reveal" style="margin-top:1.6rem;">When you type "Hello World", the AI doesn't see those words. It shatters them into pieces called <b>Tokens</b>. <br><br>Think of Tokens like syllables or puzzle pieces. "Hamburger" might become "Ham", "bur", "ger". The AI reads these numeric pieces, processes them, and spits out new pieces.</p>
<p class="kicker reveal">1 Token ≈ 0.75 Words. When ChatGPT charges you per token, they are charging you per puzzle piece.</p>
</div>
<img src="../../assets/ml_tokens.png" class="person-img cool blend-screen" alt="Tokens" />
</section>

<section class="slide">
<div class="eyebrow cool reveal">Part 2.5 &middot; AI Fundamentals</div>
<h2 class="reveal grad-cool">Parameters &amp; Chips.</h2>
<h3 class="reveal" style="margin-top:1rem;">The Brain's Memory.</h3>
<p class="lead reveal" style="margin-top:1.6rem;">A <b>Parameter</b> is a tiny mathematical knob inside the AI. If the AI learns that the sky is blue, it turns a specific knob. A model like GPT-4 has <i>over 1 Trillion</i> of these knobs. <br><br>Processing a trillion knobs for every single word requires massive hardware. That is why <b>AI System Design</b> is the highest paying job today—figuring out how to fit 1 Trillion knobs onto physical Silicon chips (GPUs).</p>
</section>

<section class="slide">
<div class="eyebrow cool reveal">Part 2.5 &middot; AI Fundamentals</div>
<h2 class="reveal grad-cool">The Models.</h2>
<h3 class="reveal" style="margin-top:1rem;">Closed vs Open Source.</h3>
<p class="lead reveal" style="margin-top:1.6rem;">A "Model" is the final, trained brain. There are two worlds:</p>
<ul class="concepts cool reveal" style="margin-top:1.8rem;">
<li><b>Closed Source:</b> Owned by megacorps. You rent it via API. Examples: <i>GPT-4 (OpenAI), Claude (Anthropic), Gemini (Google)</i>.</li>
<li><b>Open Source:</b> Free to download, run on your laptop, and modify. Examples: <i>Llama-3 (Meta), Mistral (Mistral AI)</i>.</li>
</ul>
<p class="kicker reveal">In the future, every company will run their own Open Source models privately to protect their data.</p>
</section>

"""
html = html.replace("<!-- MATH / VECTORS / MATRICES -->", fundamentals + "<!-- MATH / VECTORS / MATRICES -->")


# 3. Update Vector Bookshelf Slide
# Convert `<section class="slide">` to `<section class="slide has-img">` for that specific slide.
# This requires a bit of regex or precise replace.
old_bookshelf = """<section class="slide">
<div class="eyebrow grn reveal">Part 3 &middot; The Machine</div>
<h2 class="reveal grad-grn" style="font-size:3.5rem; margin-bottom: 1rem;">The Vector: Bookshelf</h2>
<h3 class="reveal">A Crystal Clear Analogy</h3>
<div class="tanglish-sub reveal">Oru library-la book-a thedurathu thaan Vector Search.</div>
<p class="lead reveal" style="margin-top:1.6rem;">Imagine a massive library. If you want a book about "Space Travel", you don't read every book. You go to the Science Fiction aisle (the coordinate). A Vector is exactly this: a coordinate that tells the AI exactly which shelf a concept lives on.</p>
<p class="kicker reveal">When you ask ChatGPT a question, it converts your sentence into a Vector, finds the shelf, and returns the nearest ideas.</p>
</section>"""

new_bookshelf = """<section class="slide has-img">
<div class="eyebrow grn reveal">Part 3 &middot; The Machine</div>
<div style="max-width: 55vw;">
<h2 class="reveal grad-grn" style="font-size:3.5rem; margin-bottom: 1rem;">The Vector: Bookshelf</h2>
<h3 class="reveal">A Crystal Clear Analogy</h3>
<div class="tanglish-sub reveal">Oru library-la book-a thedurathu thaan Vector Search.</div>
<p class="lead reveal" style="margin-top:1.6rem;">Imagine a massive library. If you want a book about "Space Travel", you don't read every book. You go to the Science Fiction aisle (the coordinate). A Vector is exactly this: a coordinate that tells the AI exactly which shelf a concept lives on.</p>
<p class="kicker reveal">When you ask ChatGPT a question, it converts your sentence into a Vector, finds the shelf, and returns the nearest ideas.</p>
</div>
<img src="../../assets/ml_library.png" class="person-img gold blend-screen" alt="Library" />
</section>"""
html = html.replace(old_bookshelf, new_bookshelf)

# 4. Update Matrix Universe Slide
old_matrix = """<section class="slide">
<div class="eyebrow grn reveal">Part 3 &middot; The Machine</div>
<h2 class="reveal grad-grn" style="font-size:3.5rem; margin-bottom: 1rem;">Matrix Multiplication<br>is the Universe.</h2>
<p class="lead reveal" style="margin-top:1.6rem;">In 1850, James Joseph Sylvester coined the term "Matrix". It was pure math. Today, 99% of the computational power on Earth is dedicated to multiplying matrices together.</p>
<ul class="concepts grn reveal" style="margin-top:1.8rem;">
<li>When ChatGPT generates a word? <b>Matrix Multiplication.</b></li>
<li>When your phone recognizes your face? <b>Matrix Multiplication.</b></li>
<li>When Nvidia sells a $40,000 GPU? <b>It is just a calculator built specifically to multiply matrices incredibly fast.</b></li>
</ul>
</section>"""

new_matrix = """<section class="slide has-img">
<div class="eyebrow grn reveal">Part 3 &middot; The Machine</div>
<div style="max-width: 55vw;">
<h2 class="reveal grad-grn" style="font-size:3.5rem; margin-bottom: 1rem;">Matrix Multiplication<br>is the Universe.</h2>
<p class="lead reveal" style="margin-top:1.6rem;">In 1850, James Joseph Sylvester coined the term "Matrix". It was pure math. Today, 99% of the computational power on Earth is dedicated to multiplying matrices together.</p>
<ul class="concepts grn reveal" style="margin-top:1.8rem;">
<li>When ChatGPT generates a word? <b>Matrix Multiplication.</b></li>
<li>When your phone recognizes your face? <b>Matrix Multiplication.</b></li>
<li>When Nvidia sells a $40,000 GPU? <b>It is just a calculator built specifically to multiply matrices incredibly fast.</b></li>
</ul>
</div>
<img src="../../assets/ml_architecture.png" class="person-img cool blend-screen" alt="Matrix Architecture" />
</section>"""
html = html.replace(old_matrix, new_matrix)

# 5. Insert Hands-on, Books, Panic before THE MARKET & T-SHAPED
huge_block = """
<!-- HANDS ON -->
<section class="slide center active"><div class="glow g3"></div>
<div class="eyebrow grn reveal">Part 4 &middot; Hands On</div>
<h1 class="reveal">Building a<br><span class="grad-grn">Document Translator.</span></h1>
<p class="lead reveal" style="margin-top:2rem;">Let's build an AI that can translate ancient Tamil documents to English contextually. No code. Just the architectural blueprint.</p>
</section>

<section class="slide has-img">
<div class="eyebrow grn reveal">Part 4 &middot; Hands On</div>
<h3 class="reveal">Step 1: The Recipe</h3>
<div style="max-width: 55vw;">
<ul class="concepts grn reveal" style="margin-top:1.8rem;">
<li><b>Data Collection:</b> Gather millions of Tamil/English sentence pairs.</li>
<li><b>Tokenization:</b> Shatter the sentences into tiny tokens.</li>
<li><b>Embedding:</b> Convert those tokens into Vectors (coordinates in our library).</li>
<li><b>The Transformer:</b> The neural network engine that learns the relationship between the Tamil coordinates and the English coordinates.</li>
</ul>
</div>
<img src="../../assets/ml_recipe.png" class="person-img gold blend-screen" alt="Recipe" />
</section>

<section class="slide">
<div class="eyebrow grn reveal">Part 4 &middot; Hands On</div>
<h2 class="reveal grad-grn" style="font-size:3.5rem; margin-bottom: 1rem;">Step 2: The Tools</h2>
<div class="mod-grid reveal" style="margin-top:2.5rem; grid-template-columns: 1fr 1fr;">
  <div class="mod"><div class="k">Hugging Face</div><div class="t" style="margin:1rem 0;">The Hub</div><div class="d">The GitHub of AI. Where you download the base models, tokenizers, and datasets.</div></div>
  <div class="mod"><div class="k">PyTorch</div><div class="t" style="margin:1rem 0;">The Engine</div><div class="d">The Python library built by Meta that actually performs the Matrix Multiplications.</div></div>
  <div class="mod"><div class="k">CUDA</div><div class="t" style="margin:1rem 0;">The Hardware Bridge</div><div class="d">Nvidia's software that lets PyTorch talk directly to the raw GPU cores.</div></div>
</div>
</section>

<section class="slide">
<div class="eyebrow grn reveal">Part 4 &middot; Hands On</div>
<h3 class="reveal">Step 3: The Execution (Training Loop)</h3>
<p class="lead reveal" style="margin-top:1.6rem;">How does it actually learn? Through millions of micro-adjustments.</p>
<div class="build grn reveal" style="margin-top:2rem;">
<div class="bl">The Loop</div>
<ul>
<li><b>Guess:</b> The AI is fed a Tamil word and guesses the English translation.</li>
<li><b>Loss:</b> We measure how terribly wrong the guess was (Error Rate).</li>
<li><b>Backpropagation:</b> We send a signal backward through the network to slightly adjust the "knobs" (Parameters).</li>
<li><b>Repeat:</b> Do this 10 billion times until the Loss is almost zero.</li>
</ul>
</div>
</section>

<section class="slide">
<div class="eyebrow grn reveal">Part 4 &middot; Hands On</div>
<h3 class="reveal">Step 4: The Skills Needed</h3>
<p class="lead reveal" style="margin-top:1.6rem;">To actually build this, you don't need a PhD. You need a specific stack of skills:</p>
<ul class="outcomes reveal">
<li><b>Python Mastery:</b> Especially libraries like NumPy and Pandas.</li>
<li><b>Math Intuition:</b> Not solving equations, but understanding <i>what</i> a Matrix and Vector are doing.</li>
<li><b>System Design:</b> Knowing how to load a 10GB model into a 16GB GPU without crashing the server.</li>
<li><b>API Integration:</b> Wrapping your trained model in a FastAPI or Next.js app so real people can use it.</li>
</ul>
</section>

<!-- RESOURCES -->
<section class="slide"><div class="glow g1"></div>
<div class="eyebrow reveal">Resources &middot; Books</div>
<h2 class="reveal">1. Grokking Deep Learning</h2>
<h3 class="reveal grad" style="margin-top:1rem;">by Andrew Trask</h3>
<p class="lead reveal" style="margin-top:1.6rem;">The absolute best book for beginners. It teaches you Deep Learning without using heavy math frameworks. You literally build a neural network from scratch using just basic Python arrays. Pure intuition.</p>
</section>

<section class="slide">
<div class="eyebrow reveal">Resources &middot; Books</div>
<h2 class="reveal">2. Deep Learning</h2>
<h3 class="reveal grad" style="margin-top:1rem;">by Ian Goodfellow, Yoshua Bengio</h3>
<p class="lead reveal" style="margin-top:1.6rem;">The Bible of the industry. Co-authored by the Godfather of AI. It is heavy, math-dense, and unapologetic. You don't read this in a weekend; you keep it on your desk for the rest of your career.</p>
</section>

<section class="slide">
<div class="eyebrow reveal">Resources &middot; Books</div>
<h2 class="reveal">3. Pattern Recognition</h2>
<h3 class="reveal grad" style="margin-top:1rem;">by Christopher Bishop</h3>
<p class="lead reveal" style="margin-top:1.6rem;">The foundational math. Before "Deep Learning" was a buzzword, AI was just statistical pattern recognition. This book gives you the core mathematical grounding to understand <i>why</i> algorithms work.</p>
</section>

<section class="slide">
<div class="eyebrow cool reveal">Resources &middot; Blogs</div>
<h2 class="reveal">4. Andrej Karpathy</h2>
<h3 class="reveal grad-cool" style="margin-top:1rem;">Blog &amp; YouTube</h3>
<p class="lead reveal" style="margin-top:1.6rem;">Former Director of AI at Tesla and founding member of OpenAI. His YouTube series "Neural Networks: Zero to Hero" is the gold standard for understanding Large Language Models. If you watch one thing this year, watch him.</p>
</section>

<section class="slide">
<div class="eyebrow cool reveal">Resources &middot; Blogs</div>
<h2 class="reveal">5. Lilian Weng / HF</h2>
<h3 class="reveal grad-cool" style="margin-top:1rem;">Lil'Log &amp; HuggingFace Blog</h3>
<p class="lead reveal" style="margin-top:1.6rem;">Lilian Weng (OpenAI) writes the most comprehensive, deeply researched technical blogs on the internet. Pair this with the HuggingFace blog to stay updated on the absolute cutting-edge of Open Source AI.</p>
</section>

<!-- THE PANIC -->
<section class="slide has-img"><div class="glow g2"></div>
<div class="eyebrow cool reveal">The Reality Check</div>
<h2 class="reveal grad-cool">The 2026 Interview.</h2>
<div style="max-width: 55vw;">
<p class="lead reveal" style="margin-top:1.6rem;">You sit down for a Machine Learning Engineering interview. The interviewer doesn't ask you what AI stands for. They ask you this:</p>
<ul class="concepts cool reveal" style="margin-top:1.8rem;">
<li>"How do you handle a vanishing gradient in your NLP model?"</li>
<li>"Why is your validation loss spiking while training loss drops?"</li>
<li>"Design a system to scale a vector database for 10 Million embeddings with sub-50ms latency."</li>
</ul>
</div>
<img src="../../assets/ml_panic.png" class="person-img cool blend-screen" alt="Panic" />
</section>

<section class="slide">
<div class="eyebrow cool reveal">The Reality Check</div>
<h2 class="reveal grad-cool" style="font-size:3.5rem;">"import openai" is not a career.</h2>
<p class="lead reveal" style="margin-top:1.6rem;">If your only AI skill is calling an API endpoint and printing the result, you will fail that interview in exactly 30 seconds. API wrappers are being automated away by the platforms themselves.</p>
<p class="kicker reveal">You don't need a certificate. You need the Foundations. You need to understand the math, the architecture, and the system design.</p>
</section>

"""
html = html.replace("<!-- THE MARKET & T-SHAPED -->", huge_block + "<!-- THE MARKET & T-SHAPED -->")

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Injected all slides successfully.")
