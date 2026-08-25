import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

html_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI Foundations Seminar — RiseLabs</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #000000;
  --text: #ffffff;
  --dim: rgba(255,255,255,0.5);
  --mute: rgba(255,255,255,0.3);
  --glass: rgba(255,255,255,0.04);
  --glass-border: rgba(255,255,255,0.08);
  --blue: #2997ff;
  --purple: #bf5af2;
  --green: #30d158;
  --orange: #ff9f0a;
  --red: #ff453a;
  --yellow: #ffd60a;
  --pink: #ff375f;
  --teal: #64d2ff;
  --indigo: #5e5ce6;
  --mint: #66d4cf;
  --cyan: #5ac8fa;
}
* { margin:0; padding:0; box-sizing:border-box; }
body, html { width:100%; height:100%; font-family:'Inter',-apple-system,sans-serif; overflow:hidden; background:#000; color:#fff; }

/* Every slide is AMOLED black */
.slide { position:absolute; top:0; left:0; width:100%; height:100%; display:flex; flex-direction:column; justify-content:center; padding:8vw; opacity:0; visibility:hidden; transition:opacity .5s ease, visibility .5s; overflow:hidden; background:#000; color:#fff; }
.slide.active { opacity:1; visibility:visible; z-index:10; }

/* Typography */
.hero { font-size:clamp(48px,7vw,100px); font-weight:900; line-height:1.05; letter-spacing:-.04em; }
.sect { font-size:clamp(36px,5vw,72px); font-weight:800; line-height:1.1; letter-spacing:-.03em; }
.med { font-size:clamp(28px,4vw,56px); font-weight:700; line-height:1.15; letter-spacing:-.025em; }
.body { font-size:clamp(16px,1.8vw,24px); font-weight:400; line-height:1.6; max-width:800px; color:var(--dim); }
.sub { font-size:clamp(18px,2.2vw,32px); font-weight:500; line-height:1.4; max-width:800px; color:var(--dim); }
.lbl { font-size:clamp(12px,1.2vw,16px); font-weight:700; letter-spacing:.15em; text-transform:uppercase; }
.pill { display:inline-block; padding:8px 20px; border-radius:40px; font-size:13px; font-weight:700; letter-spacing:.08em; text-transform:uppercase; margin-bottom:24px; }
.bignum { font-size:clamp(48px,6vw,96px); font-weight:900; letter-spacing:-.04em; line-height:1; }
.statlbl { font-size:clamp(12px,1.2vw,16px); font-weight:500; color:var(--mute); margin-top:8px; }

/* Gradients */
.grb { background:linear-gradient(135deg,var(--blue),var(--purple)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.gbp { background:linear-gradient(135deg,var(--blue),var(--pink)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.gpo { background:linear-gradient(135deg,var(--purple),var(--orange)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.ggt { background:linear-gradient(135deg,var(--green),var(--teal)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.goy { background:linear-gradient(135deg,var(--orange),var(--yellow)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.grc { background:linear-gradient(135deg,var(--red),var(--orange)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }

/* Glass Card */
.glass-card { background:var(--glass); border:1px solid var(--glass-border); border-radius:20px; padding:32px; backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px); max-width:900px; }
.glass-card strong { color:#fff; }

/* Stat Row */
.stat-row { display:flex; gap:clamp(20px,4vw,60px); flex-wrap:wrap; margin-top:24px; }
.stat-item { text-align:center; }

/* Tang (Tamil Quote) */
.tang { font-style:italic; font-size:clamp(16px,1.8vw,24px); line-height:1.6; padding:24px 32px; border-left:4px solid; max-width:800px; background:rgba(255,255,255,.02); border-radius:0 16px 16px 0; }

/* Timeline */
.tl { display:flex; flex-direction:column; gap:16px; margin-top:16px; }
.tli { display:flex; align-items:flex-start; gap:16px; }
.tldot { width:12px; height:12px; border-radius:50%; margin-top:6px; flex-shrink:0; }
.tlc { font-weight:700; font-size:clamp(14px,1.4vw,18px); }
.tls { font-size:clamp(12px,1.1vw,15px); color:var(--mute); margin-top:2px; }

/* Animations */
.slide > *:not(.glow):not(.person-img) { opacity:0; transform:translateY(24px); transition:all .8s cubic-bezier(.22,.61,.36,1); }
.slide.active > *:not(.glow):not(.person-img):not(.step) { opacity:1; transform:translateY(0); }

/* The Reveal Step */
.step { opacity:0!important; transform:translateY(24px); visibility:hidden; transition:opacity .6s ease, transform .6s ease, visibility .6s; }
.step.revealed { opacity:1!important; transform:translateY(0); visibility:visible; }

/* UI */
.pbar { position:fixed; top:0; left:0; height:3px; background:linear-gradient(90deg,var(--blue),var(--purple)); width:0%; z-index:100; transition:width .3s ease; }
.counter { position:fixed; bottom:24px; left:24px; font-family:'JetBrains Mono',monospace; font-size:13px; font-weight:500; opacity:.3; z-index:100; color:#fff; }
.hint { position:fixed; bottom:24px; right:24px; font-size:13px; font-weight:500; opacity:.3; z-index:100; color:#fff; transition:opacity .3s; }

/* Image styling */
.person-img { position:absolute; right:3vw; bottom:0; height:85vh; object-fit:contain; z-index:1; opacity:0; filter:drop-shadow(0 0 60px rgba(41,151,255,.2)) grayscale(20%) contrast(1.1); mix-blend-mode:screen; transition:opacity .8s ease; }
.person-img.revealed, .slide.active > .person-img:not(.step) { opacity:.7; }
.person-img.gold { filter:drop-shadow(0 0 60px rgba(255,159,10,.2)) grayscale(20%) contrast(1.1); }
.person-img.grn { filter:drop-shadow(0 0 60px rgba(48,209,88,.2)) grayscale(20%) contrast(1.1); }
.person-img.pink { filter:drop-shadow(0 0 60px rgba(255,55,95,.2)) grayscale(20%) contrast(1.1); }

.slide:has(.person-img) { align-items:flex-start; }
.slide:has(.person-img) > *:not(.person-img):not(.glow) { max-width:52vw; position:relative; z-index:2; }

.glow { position:absolute; border-radius:50%; filter:blur(150px); opacity:.12; z-index:0; pointer-events:none; }

/* Cards Row */
.card-row { display:flex; gap:16px; flex-wrap:wrap; margin-top:20px; }
.card-item { background:var(--glass); border:1px solid var(--glass-border); border-radius:16px; padding:20px 24px; flex:1; min-width:200px; }
.card-item .ct { font-weight:700; font-size:clamp(14px,1.4vw,18px); margin-bottom:6px; }
.card-item .cb { font-size:clamp(12px,1.1vw,15px); color:var(--mute); line-height:1.5; }
</style>
</head>
<body>
<div class="pbar" id="pb"></div>
<div class="counter" id="ctr"></div>
<div class="hint" id="hint">Press → to reveal &amp; advance</div>
<div id="deck"></div>

<script>
const S = [

// ═══════════════════════════════════════
// WELCOME
// ═══════════════════════════════════════
{html:`
<div class="glow" style="width:700px;height:700px;background:var(--blue);top:-15%;right:-10%"></div>
<div class="glow" style="width:500px;height:500px;background:var(--purple);bottom:-20%;left:5%"></div>
<p class="lbl" style="color:var(--mute);margin-bottom:18px">RiseLabs presents</p>
<h1 class="hero">AI Foundations<br><span class="grb">Seminar.</span></h1>
<p class="sub" style="margin-top:20px">From buzzwords to building blocks.<br>A CS50-depth journey into how machines think.</p>
`},

// ═══════════════════════════════════════
// ACT 0: BUZZWORD PANIC
// ═══════════════════════════════════════
{html:`
<div class="glow" style="width:600px;height:600px;background:var(--red);top:-10%;left:-5%"></div>
<p class="lbl" style="color:var(--red);margin-bottom:14px">Act 0 · The State of the World</p>
<h2 class="hero">The AI<br><span class="grc">Panic.</span></h2>
<p class="sub" style="margin-top:18px">You hear these words in every meeting, on every news channel, and on every LinkedIn post.<br>But what do they actually mean?</p>
<img src="../../assets/ml_panic.png" class="step person-img" alt="Panic" />
`},

{html:`
<p class="lbl" style="color:var(--blue);margin-bottom:14px">Buzzword #1 · Algorithm</p>
<h2 class="med">"What is an Algorithm?"</h2>
<p class="sub" style="margin-top:14px">Everyone says "the algorithm decided." What does that even mean?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--blue);font-size:clamp(14px,1.4vw,18px)">🍳 The Simple Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">It's just a cooking recipe.<br>Step 1 → Step 2 → Step 3.<br>Follow the steps exactly, you get the dish. Miss a step, it fails.</span>
</div>
<img src="../../assets/ml_recipe.png" class="step person-img gold" alt="Recipe" />
`},

{html:`
<p class="lbl" style="color:var(--purple);margin-bottom:14px">Buzzword #2 · Parameters</p>
<h2 class="med">"175 Billion Parameters"</h2>
<p class="sub" style="margin-top:14px">GPT-4 has 1.7 Trillion parameters. What are they?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--purple);font-size:clamp(14px,1.4vw,18px)">📻 The Simple Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">Think of an old radio. The parameters are the tuning knobs — volume, bass, frequency. You twist them until the music comes through perfectly clear. A model with more knobs can produce richer music.</span>
</div>
<img src="../../assets/ml_radio.png" class="step person-img" alt="Radio" />
`},

{html:`
<p class="lbl" style="color:var(--green);margin-bottom:14px">Buzzword #3 · Training Data</p>
<h2 class="med">"Trained on the Entire Internet"</h2>
<p class="sub" style="margin-top:14px">Why do AI models need terabytes of data?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--green);font-size:clamp(14px,1.4vw,18px)">📝 The Simple Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">Solving the past 10 years of Anna University question papers before a final exam. The more past papers you see, the better you perform on the real test. AI does the same thing — at planetary scale.</span>
</div>
<img src="../../assets/ml_exam.png" class="step person-img grn" alt="Exam" />
`},

{html:`
<p class="lbl" style="color:var(--orange);margin-bottom:14px">Buzzword #4 · Overfitting</p>
<h2 class="med">"The Model is Overfitting"</h2>
<p class="sub" style="margin-top:14px">Why does the AI ace tests but fail in production?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--orange);font-size:clamp(14px,1.4vw,18px)">📖 The Simple Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">Mugging up the textbook line-by-line. You score 100% on practice tests, but when the professor twists the question slightly in the real exam — you blank out completely.</span>
</div>
<img src="../../assets/ml_overfit.png" class="step person-img gold" alt="Overfit" />
`},

{html:`
<p class="lbl" style="color:var(--pink);margin-bottom:14px">Buzzword #5 · GPU</p>
<h2 class="med">"Why is Nvidia Worth $3 Trillion?"</h2>
<p class="sub" style="margin-top:14px">Why does AI need GPUs instead of CPUs?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--pink);font-size:clamp(14px,1.4vw,18px)">🏭 The Simple Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">A CPU = 4 genius professors solving complex math one by one.<br>A GPU = 10,000 average students working together to solve thousands of simple math problems at the exact same time.<br><br>AI needs brute force, not brilliance.</span>
</div>
<img src="../../assets/ml_factory.png" class="step person-img pink" alt="Factory" />
`},

// ═══════════════════════════════════════
// THE PIONEERS
// ═══════════════════════════════════════
{html:`
<p class="lbl" style="color:var(--teal);margin-bottom:14px">The Pioneers · The Godfather</p>
<h2 class="med">Geoffrey Hinton</h2>
<p class="sub" style="margin-top:14px">The man who refused to give up on neural networks when everyone else did.</p>
<div class="step glass-card" style="margin-top:24px;">
<span style="color:var(--dim);font-size:clamp(16px,1.8vw,24px)">In the 1990s, the entire AI community abandoned neural networks. Hinton kept working alone. In 2012, his student's network crushed the ImageNet competition — and the deep learning revolution began. Nobel Prize 2024.</span>
</div>
<img src="../../assets/ml_hinton.png" class="step person-img" alt="Hinton" />
`},

{html:`
<p class="lbl" style="color:var(--blue);margin-bottom:14px">The Pioneers · The Teacher</p>
<h2 class="med">Andrew Ng</h2>
<p class="sub" style="margin-top:14px">The man who taught AI to the world.</p>
<div class="step glass-card" style="margin-top:24px;">
<span style="color:var(--dim);font-size:clamp(16px,1.8vw,24px)">Co-founded Google Brain. Created the most popular ML course on Coursera (5M+ students). Founded DeepLearning.AI. His belief: "AI is the new electricity." He didn't just build AI — he democratized it.</span>
</div>
<img src="../../assets/ml_ng.png" class="step person-img grn" alt="Ng" />
`},

{html:`
<p class="lbl" style="color:var(--purple);margin-bottom:14px">The Pioneers · The Visionary</p>
<h2 class="med">Yann LeCun</h2>
<p class="sub" style="margin-top:14px">The man who taught machines how to see.</p>
<div class="step glass-card" style="margin-top:24px;">
<span style="color:var(--dim);font-size:clamp(16px,1.8vw,24px)">Invented Convolutional Neural Networks (CNNs). Every time your phone recognizes your face, every time Google Photos tags you — that's LeCun's invention at work. Turing Award 2018. Now Chief AI Scientist at Meta.</span>
</div>
<img src="../../assets/ml_lecun.png" class="step person-img gold" alt="LeCun" />
`},

{html:`
<p class="lbl" style="color:var(--pink);margin-bottom:14px">The Pioneers · The Architect</p>
<h2 class="med">Sam Altman</h2>
<p class="sub" style="margin-top:14px">The man who packaged it all and triggered the panic.</p>
<div class="step glass-card" style="margin-top:24px;">
<span style="color:var(--dim);font-size:clamp(16px,1.8vw,24px)">CEO of OpenAI. Took decades of research, packaged it into ChatGPT, and launched it to 100M users in 2 months — the fastest-growing product in human history. The world hasn't been the same since Nov 30, 2022.</span>
</div>
<img src="../../assets/ml_altman.png" class="step person-img" alt="Altman" />
`},

// ═══════════════════════════════════════
// ACT 1: WHAT IS ML?
// ═══════════════════════════════════════
{html:`
<div class="glow" style="width:600px;height:600px;background:var(--blue);bottom:-20%;left:-10%"></div>
<p class="lbl" style="color:var(--blue);margin-bottom:14px">Act 1 · The Foundation</p>
<h2 class="hero">Traditional Code<br>vs. <span class="gbp">Machine Learning</span></h2>
<p class="sub" style="margin-top:14px">What makes ML fundamentally different?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--blue);font-size:clamp(14px,1.4vw,18px)">🫕 The Idli Maavu Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)"><strong>Traditional Code:</strong> You write exactly how much rice and urad dal to mix. (Rules → Answers)<br><br>
<strong>Machine Learning:</strong> You show the computer 100 perfect Idlis and the ingredients, and it figures out the recipe itself! (Data + Answers → Rules)</span>
</div>
<img src="../../assets/ml_idli.png" class="step person-img gold" alt="Idli" />
`},

// ═══════════════════════════════════════
// ACT 2: THE CORE MATH
// ═══════════════════════════════════════
{html:`
<p class="lbl" style="color:var(--green);margin-bottom:14px">Act 2 · How Machines Learn</p>
<h2 class="med">"Gradient Descent"</h2>
<p class="sub" style="margin-top:14px">How does the model actually improve itself?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--green);font-size:clamp(14px,1.4vw,18px)">⛰️ The Mountain Descent Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">You're blindfolded on a mountain. To reach the bottom, you feel the slope with your feet and take a small step downhill. Repeat until it's flat. That's gradient descent — the model walks downhill on its error surface until it finds the minimum.</span>
</div>
<img src="../../assets/ml_mountain.png" class="step person-img grn" alt="Mountain" />
`},

{html:`
<p class="lbl" style="color:var(--purple);margin-bottom:14px">Act 2 · The Perceptron</p>
<h2 class="med">"The Simplest Neural Network"</h2>
<p class="sub" style="margin-top:14px">What is a single neuron in a neural network?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--purple);font-size:clamp(14px,1.4vw,18px)">🗳️ The Voting Committee Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">Imagine 5 judges voting on a cooking competition. Each judge has a different "weight" (importance). The perceptron adds up the weighted votes and fires a decision: "Delicious!" or "Needs work." A neural network is thousands of these judges voting in layers.</span>
</div>
<img src="../../assets/ml_perceptron.png" class="step person-img" alt="Perceptron" />
`},

{html:`
<p class="lbl" style="color:var(--orange);margin-bottom:14px">Act 2 · Backpropagation</p>
<h2 class="med">"How Does it Learn from Mistakes?"</h2>
<p class="sub" style="margin-top:14px">The model got the answer wrong. How does it fix itself?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--orange);font-size:clamp(14px,1.4vw,18px)">📢 The Telephone Game Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">Imagine a message passed through 10 people and the last person says it wrong. Backpropagation traces the error backwards — person by person — figuring out exactly who distorted the message and by how much, so next time it's correct.</span>
</div>
<img src="../../assets/ml_backprop.png" class="step person-img gold" alt="Backprop" />
`},

// ═══════════════════════════════════════
// ACT 3: VISION
// ═══════════════════════════════════════
{html:`
<p class="lbl" style="color:var(--teal);margin-bottom:14px">Act 3 · Computer Vision</p>
<h2 class="med">"How Do Machines See?"</h2>
<p class="sub" style="margin-top:14px">How does your phone recognize faces in photos?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--teal);font-size:clamp(14px,1.4vw,18px)">🔍 The Magnifying Glass Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">A CNN scans an image like a magnifying glass. First pass: edges. Second pass: shapes. Third pass: ears, tails, eyes. Final pass: "That's a cat!" Each layer builds on the previous one — from pixels to understanding.</span>
</div>
<img src="../../assets/ml_lens.png" class="step person-img" alt="Lens" />
`},

// ═══════════════════════════════════════
// ACT 4: LANGUAGE
// ═══════════════════════════════════════
{html:`
<div class="glow" style="width:500px;height:500px;background:var(--teal);top:-10%;right:-5%"></div>
<p class="lbl" style="color:var(--cyan);margin-bottom:14px">Act 4 · Language AI</p>
<h2 class="med">"Word Embeddings"</h2>
<p class="sub" style="margin-top:14px">How does a computer know that "King" and "Queen" are related?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--cyan);font-size:clamp(14px,1.4vw,18px)">🗺️ The Google Maps for Words Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">Words are mapped as locations in space. "King" and "Queen" live on the same street. "Apple" and "Banana" live in a different neighborhood. The magic: King − Man + Woman = Queen. Distance = Meaning.</span>
</div>
<img src="../../assets/ml_map.png" class="step person-img grn" alt="Map" />
`},

{html:`
<p class="lbl" style="color:var(--purple);margin-bottom:14px">Act 4 · How ChatGPT Works</p>
<h2 class="med">"Next Token Prediction"</h2>
<p class="sub" style="margin-top:14px">How does ChatGPT write entire essays?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--purple);font-size:clamp(14px,1.4vw,18px)">📱 The Autocomplete Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">It's the world's most advanced autocomplete. It reads everything you've typed, predicts the single most likely next word, writes it, and repeats. One word at a time, 100 times per second. That's all ChatGPT does.</span>
</div>
<img src="../../assets/ml_tokens.png" class="step person-img" alt="Tokens" />
`},

// ═══════════════════════════════════════
// ACT 5: TRANSFORMERS & SCALING
// ═══════════════════════════════════════
{html:`
<div class="glow" style="width:600px;height:600px;background:var(--yellow);top:-15%;right:-8%"></div>
<p class="lbl" style="color:var(--yellow);margin-bottom:14px">Act 5 · The Breakthrough Paper</p>
<h2 class="med">"Attention Is All You Need"</h2>
<p class="sub" style="margin-top:14px">The 2017 paper that changed everything. What is "Attention"?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--yellow);font-size:clamp(14px,1.4vw,18px)">👀 The Crowded Room Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">Imagine you're at a noisy party. Your brain automatically focuses on the one person speaking to you and filters out everyone else. That's "Attention" — the AI learns to focus on the most relevant words in a sentence, regardless of how far apart they are.</span>
</div>
<img src="../../assets/ml_library.png" class="step person-img" alt="Library" />
`},

{html:`
<p class="lbl" style="color:var(--orange);margin-bottom:14px">Act 5 · The Scaling Hypothesis</p>
<h2 class="med">"Why Bigger = Smarter"</h2>
<p class="sub" style="margin-top:14px">GPT-3 has 175B parameters. GPT-4 has 1.7T. Why does more = better?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--orange);font-size:clamp(14px,1.4vw,18px)">🚀 The Rocket Fuel Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">More data = more fuel. More parameters = bigger engine. More compute = longer runway. The breakthrough: performance follows predictable power laws. Double the investment → reliably, measurably smarter. This is why billions are pouring in.</span>
</div>
<img src="../../assets/ml_rocket.png" class="step person-img gold" alt="Rocket" />
`},

{html:`
<p class="lbl" style="color:var(--green);margin-bottom:14px">Act 5 · The #1 AI Skill of 2026</p>
<h2 class="med">"RAG — Retrieval-Augmented Generation"</h2>
<p class="sub" style="margin-top:14px">LLMs hallucinate. They make things up. How do we fix this?</p>
<div class="step glass-card" style="margin-top:24px;">
<strong style="color:var(--green);font-size:clamp(14px,1.4vw,18px)">📖 The Open-Book Exam Analogy:</strong><br><br>
<span style="color:var(--dim);font-size:clamp(18px,2vw,28px)">Instead of making the AI memorize everything, you let it take an open-book exam. When it gets a question, it first searches your private documents for the answer, then writes a response using that real data. No hallucinations. No guessing. RAG is the #1 most in-demand AI engineering skill in 2026.</span>
</div>
<img src="../../assets/ml_openbook.png" class="step person-img" alt="OpenBook" />
`},

// ═══════════════════════════════════════
// ACT 6: THE INVISIBLE UPSELL
// ═══════════════════════════════════════
{html:`
<div class="glow" style="width:800px;height:800px;background:var(--red);top:-20%;right:-15%"></div>
<p class="lbl" style="color:var(--red);margin-bottom:14px">Act 6 · The Shift</p>
<h2 class="hero">The World<br>Is <span class="grc">Moving.</span></h2>
<p class="sub" style="margin-top:18px">Let's look at what the data actually says.</p>
`},

{html:`
<p class="lbl" style="color:var(--blue);margin-bottom:14px">Global Demand</p>
<h2 class="med">AI Talent Demand — Global</h2>
<div class="step">
<div class="stat-row">
<div class="stat-item"><div class="bignum gbp">74%</div><div class="statlbl">YoY AI/ML talent demand growth</div></div>
<div class="stat-item"><div class="bignum gpo">143%</div><div class="statlbl">AI Engineer job posting growth</div></div>
<div class="stat-item"><div class="bignum ggt">$301B</div><div class="statlbl">Global AI spending in 2026</div></div>
</div>
<p style="margin-top:24px;font-size:clamp(14px,1.4vw,18px);color:var(--dim)">LinkedIn ranked <strong style="color:#fff">AI Engineer</strong> as the #1 fastest-growing job title. Four of the top five fastest-growing positions are AI-related.</p>
<p style="font-size:12px;color:var(--mute);margin-top:12px">Sources: LinkedIn 2026 Jobs on the Rise, Mordor Intelligence, McKinsey</p>
</div>
<img src="../../assets/ml_chart.png" class="step person-img" alt="Chart" />
`},

{html:`
<p class="lbl" style="color:var(--green);margin-bottom:14px">India's AI Boom</p>
<h2 class="med">India is Leading the Charge</h2>
<div class="step">
<div class="stat-row">
<div class="stat-item"><div class="bignum" style="color:var(--green)">59.5%</div><div class="statlbl">YoY AI hiring growth in India</div></div>
<div class="stat-item"><div class="bignum" style="color:var(--teal)">3.8L</div><div class="statlbl">AI roles projected in 2026</div></div>
<div class="stat-item"><div class="bignum" style="color:var(--mint)">33%</div><div class="statlbl">India leads global AI hiring rate</div></div>
</div>
<p style="margin-top:24px;font-size:clamp(14px,1.4vw,18px);color:var(--dim)">India's AI market: <strong style="color:#fff">$22.8B in 2025 → $131B by 2032</strong>. Growth: 42.2% CAGR. GenAI skills demand jumped 60% YoY.</p>
<p style="font-size:12px;color:var(--mute);margin-top:12px">Sources: LinkedIn AI Labor Market Report 2026, Stanford AI Index, foundit Report</p>
</div>
<img src="../../assets/ml_india.png" class="step person-img grn" alt="India" />
`},

{html:`
<p class="lbl" style="color:var(--pink);margin-bottom:14px">What Companies Pay</p>
<h2 class="med">AI Salaries in India — 2026</h2>
<div class="step">
<div class="card-row">
<div class="card-item"><div class="ct" style="color:var(--blue)">AI/ML Engineer</div><div style="font-size:clamp(24px,3vw,40px);font-weight:900;color:var(--blue);margin:8px 0">₹20-22L</div><div class="cb">Average · Senior up to ₹60L</div></div>
<div class="card-item"><div class="ct" style="color:var(--pink)">GenAI/LLM Engineer</div><div style="font-size:clamp(24px,3vw,40px);font-weight:900;color:var(--pink);margin:8px 0">₹12-74L</div><div class="cb">Hottest role · Freshers ₹12-20L</div></div>
<div class="card-item"><div class="ct" style="color:var(--green)">Data Scientist</div><div style="font-size:clamp(24px,3vw,40px);font-weight:900;color:var(--green);margin:8px 0">₹15-25L</div><div class="cb">Average · Lead ₹35L+</div></div>
</div>
<p style="margin-top:20px;font-size:clamp(13px,1.3vw,17px);color:var(--dim)">AI professionals earn a <strong style="color:#fff">56% wage premium</strong> over non-AI peers. First job switch: 40-70% jump.</p>
</div>
<img src="../../assets/ml_salary.png" class="step person-img gold" alt="Salary" />
`},

{html:`
<div class="glow" style="width:500px;height:500px;background:var(--green);bottom:-15%;right:-5%"></div>
<p class="lbl" style="color:var(--red);margin-bottom:14px">The Reality Check</p>
<h2 class="sect"><span class="grc">"AI Unga Job-a Edukkathu"</span></h2>
<p class="sub" style="margin-top:14px">Will AI replace software engineers?</p>
<div class="step">
<div class="tang" style="border-color:var(--red);color:var(--dim)">
"AI won't take your job. But a person who knows AI <strong style="color:#fff">will</strong> take your job. The question isn't whether AI will affect your career — it's whether you'll be the one wielding it or being replaced by it."
</div>
</div>
<img src="../../assets/ml_job.png" class="step person-img grn" alt="Job" />
`},

{html:`
<p class="lbl" style="color:var(--indigo);margin-bottom:14px">Your Roadmap</p>
<h2 class="med">The AI Engineer Career Pathway</h2>
<div class="step">
<div class="tl">
<div class="tli"><div class="tldot" style="background:var(--blue)"></div><div><div class="tlc" style="color:var(--blue)">Phase 1: Foundations (Months 1-3)</div><div class="tls">Python, NumPy, Pandas, Linear Algebra, Probability</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--purple)"></div><div><div class="tlc" style="color:var(--purple)">Phase 2: Core ML (Months 3-6)</div><div class="tls">Scikit-learn, Regression, Classification, Trees, Evaluation</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--green)"></div><div><div class="tlc" style="color:var(--green)">Phase 3: Deep Learning (Months 6-9)</div><div class="tls">PyTorch, CNNs, RNNs, Training loops, GPU computing</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--orange)"></div><div><div class="tlc" style="color:var(--orange)">Phase 4: NLP & LLMs (Months 9-12)</div><div class="tls">Transformers, Hugging Face, Fine-tuning, RAG</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--pink)"></div><div><div class="tlc" style="color:var(--pink)">Phase 5: Production (Months 12-15)</div><div class="tls">FastAPI, Docker, MLOps, AWS/GCP, CI/CD</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--red)"></div><div><div class="tlc" style="color:var(--red)">Phase 6: Specialization (15+ months)</div><div class="tls">AI Agents, Computer Vision, Multi-modal, Research</div></div></div>
</div>
<p style="margin-top:20px;font-size:clamp(14px,1.4vw,18px);color:var(--dim)">This is a 15-month journey. You can't shortcut it. <strong style="color:#fff">But you can accelerate it with the right mentorship.</strong></p>
</div>
<img src="../../assets/ml_pathway.png" class="step person-img" alt="Pathway" />
`},

{html:`
<p class="lbl" style="color:var(--orange);margin-bottom:14px">The Key Takeaway</p>
<h2 class="sect"><span class="goy">"Filter Coffee Madiri"</span></h2>
<p class="sub" style="margin-top:14px">What's the secret to mastering AI?</p>
<div class="step">
<div class="tang" style="border-color:var(--orange);color:var(--dim)">
"Filter coffee madiri — decoction thani-ya, paal thani-ya, sugar thani-ya pottu mix pannum bodhu thaan taste varum. Math, code, theory, projects — ellathayum layer layer-a kaththukkanum. Shortcut pottaa weak coffee thaan kidaikkum."
</div>
</div>
<img src="../../assets/ml_coffee.png" class="step person-img gold" alt="Coffee" />
`},

// ═══════════════════════════════════════
// RISELABS PITCH
// ═══════════════════════════════════════
{html:`
<div class="glow" style="width:800px;height:800px;background:var(--orange);top:-25%;left:-15%"></div>
<div class="glow" style="width:500px;height:500px;background:var(--yellow);bottom:-20%;right:0"></div>
<p class="pill" style="background:rgba(255,149,0,.15);color:var(--orange)">The Bridge</p>
<h2 class="sect">Everything we covered today?<br><span class="goy">We teach all of it.</span></h2>
<div class="step">
<p class="sub" style="margin-top:14px">RiseLabs AI Engineering Bootcamp — real datasets, actual deployment, 3 portfolio projects, direct industry mentorship. 18 weeks of building, not just watching.</p>
<div class="tang" style="border-color:var(--orange);color:var(--dim);margin-top:20px">
"3rd year is the perfect time. Final year-la poi project theda koodathu. Build things that matter. Start now."
</div>
</div>
<img src="../../assets/ml_bridge.png" class="step person-img gold" alt="Bridge" />
`},

{html:`
<div class="glow" style="width:600px;height:600px;background:var(--blue);top:-10%;right:-5%"></div>
<div class="glow" style="width:400px;height:400px;background:var(--green);bottom:-10%;left:10%"></div>
<div style="text-align:center;display:flex;flex-direction:column;align-items:center">
<p class="lbl" style="color:var(--blue);margin-bottom:14px">Join the Revolution</p>
<h2 class="hero">Your future starts<br><span class="grb">right now.</span></h2>
<p class="sub" style="margin-top:14px;text-align:center;margin-left:auto;margin-right:auto">Scan the QR. Send a message. Lock in your spot.</p>
<div class="step" style="margin-top:32px;text-align:center">
<div style="display:flex;align-items:center;gap:12px;justify-content:center">
<svg width="30" height="30" viewBox="0 0 24 24" fill="#30d158"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 2C6.477 2 2 6.477 2 12c0 1.89.525 3.66 1.438 5.168L2 22l4.832-1.438A9.955 9.955 0 0012 22c5.523 0 10-4.477 10-10S17.523 2 12 2z"/></svg>
<span style="font-size:clamp(28px,4vw,48px);font-weight:900;letter-spacing:.04em;color:var(--green)">9087929229</span>
</div>
<div style="margin-top:16px;font-size:clamp(18px,2vw,28px);font-weight:700;color:var(--blue)">riselabs.one</div>
<p style="margin-top:40px;font-size:13px;color:var(--mute)">RiseLabs · Zerone Technologies · Chennai</p>
</div>
</div>
`}

]; // end slides

// ═══════════ RENDER ═══════════
const deck = document.getElementById('deck');
S.forEach((s,i) => {
  const div = document.createElement('div');
  div.className = 'slide' + (i===0?' active':'');
  div.innerHTML = s.html;
  deck.appendChild(div);
});

const slides = document.querySelectorAll('.slide');
const pb = document.getElementById('pb');
const ctr = document.getElementById('ctr');
let cur = 0;
const tot = slides.length;

function go(i) {
  slides[cur].classList.remove('active');
  slides[cur].querySelectorAll('.step').forEach(el => el.classList.remove('revealed'));
  slides[i].classList.add('active');
  cur = i;
  pb.style.width = ((i+1)/tot*100)+'%';
  ctr.textContent = (i+1)+' / '+tot;
}

function next() {
  const currentSlide = slides[cur];
  const steps = currentSlide.querySelectorAll('.step:not(.revealed)');
  if (steps.length > 0) {
    steps.forEach(el => el.classList.add('revealed'));
  } else {
    if (cur < tot - 1) go(cur + 1);
  }
}

function prev() {
  if (cur > 0) go(cur - 1);
}

document.addEventListener('click', e => {
  if(e.target.closest('a')) return;
  e.clientX < window.innerWidth * 0.2 ? prev() : next();
});
document.addEventListener('keydown', e => {
  if(e.key==='ArrowRight'||e.key===' ') { e.preventDefault(); next(); }
  if(e.key==='ArrowLeft') prev();
});
let tx=0;
document.addEventListener('touchstart', e => { tx=e.touches[0].clientX; });
document.addEventListener('touchend', e => {
  const d=tx-e.changedTouches[0].clientX;
  if(Math.abs(d)>50) d>0?next():prev();
});
go(0);
</script>
</body>
</html>
"""

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "ml-foundations.html"), "w") as f:
    f.write(html_content)

print("Regenerated ml-foundations.html — AMOLED Dark, CS50 Depth, Invisible Upsell!")
