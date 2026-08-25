import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import sys

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>The Foundations — RiseLabs Keynote</title>
<style>
:root{
  --bg:#000;--bg2:#0a0a0c;--ink:#f5f5f7;--dim:#86868b;--dimmer:#6e6e73;
  --gold:#d4a24e;--gold-soft:#e8c583;--blue:#2997ff;--green:#5fd39b;
  --line:rgba(255,255,255,.08);--card:rgba(255,255,255,.04);
}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{height:100%;background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Helvetica Neue",Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;overflow:hidden;}
.deck{position:fixed;inset:0;}
.slide{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;
  padding:7.5vh 8.5vw;opacity:0;transform:scale(1.04);
  transition:opacity .7s cubic-bezier(.22,.61,.36,1),transform .7s cubic-bezier(.22,.61,.36,1);pointer-events:none;}
.slide.active{opacity:1;transform:scale(1);pointer-events:auto;}
.slide.prev{transform:scale(.98);}
.slide.center{align-items:center;text-align:center;}
.slide.center .lead{margin-left:auto;margin-right:auto;}

/* Auto Reveal Animations */
.slide.active .reveal{animation:rise .9s cubic-bezier(.22,.61,.36,1) both;}
.slide.active .reveal:nth-child(1){animation-delay:.08s;}
.slide.active .reveal:nth-child(2){animation-delay:.18s;}
.slide.active .reveal:nth-child(3){animation-delay:.28s;}
.slide.active .reveal:nth-child(4){animation-delay:.38s;}
.slide.active .reveal:nth-child(5){animation-delay:.48s;}
.slide.active .reveal:nth-child(6){animation-delay:.58s;}

/* Manual Step Reveal */
.step { opacity: 0; transform: translateY(20px); transition: all 0.6s cubic-bezier(0.22, 0.61, 0.36, 1); }
.step.revealed { opacity: 1; transform: translateY(0); }

@keyframes rise{from{opacity:0;transform:translateY(24px);}to{opacity:1;transform:translateY(0);}}
.eyebrow{font-size:clamp(.66rem,1vw,.88rem);letter-spacing:.3em;text-transform:uppercase;font-weight:600;color:var(--gold);margin-bottom:1.6rem;}
.eyebrow.cool{color:var(--blue);}.eyebrow.grn{color:var(--green);}
h1{font-size:clamp(2.6rem,7.5vw,7rem);font-weight:700;letter-spacing:-.03em;line-height:.98;}
h2{font-size:clamp(1.9rem,5vw,4.4rem);font-weight:700;letter-spacing:-.028em;line-height:1.03;}
h3{font-size:clamp(1.3rem,2.8vw,2.3rem);font-weight:600;letter-spacing:-.02em;line-height:1.12;}
.lead{font-size:clamp(1.05rem,1.85vw,1.55rem);font-weight:400;color:var(--dim);line-height:1.42;letter-spacing:-.01em;max-width:64ch;}
.kicker{font-size:clamp(.92rem,1.4vw,1.15rem);color:var(--dimmer);margin-top:1.4rem;font-weight:450;max-width:64ch;}
.grad{background:linear-gradient(120deg,#fff,var(--gold-soft) 55%,var(--gold));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.grad-cool{background:linear-gradient(120deg,#fff,#8ab6ff 55%,var(--blue));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.grad-grn{background:linear-gradient(120deg,#fff,#9fe8c4 55%,var(--green));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.mono{font-family:"SF Mono",ui-monospace,Menlo,monospace;font-size:.92em;}
em{font-style:italic;color:var(--ink);}
.big-num{font-size:clamp(5rem,19vw,17rem);font-weight:700;letter-spacing:-.05em;line-height:.85;}
.mod-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin-top:.4rem;width:100%;}
.mod{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:1.5rem 1.4rem;min-height:140px;
  display:flex;flex-direction:column;justify-content:space-between;transition:transform .4s ease,border-color .4s ease,background .4s ease;}
.slide.active .mod:hover{transform:translateY(-4px);border-color:rgba(212,162,78,.45);background:rgba(212,162,78,.06);}
.mod .k{font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);font-weight:600;}
.mod .t{font-size:clamp(1rem,1.55vw,1.35rem);font-weight:600;letter-spacing:-.01em;line-height:1.15;}
.mod .d{font-size:.82rem;color:var(--dimmer);line-height:1.35;}
.concepts{list-style:none;display:flex;flex-direction:column;gap:.75rem;max-width:70ch;}
.concepts li{font-size:clamp(.95rem,1.45vw,1.2rem);color:var(--dim);line-height:1.38;padding-left:1.5rem;position:relative;}
.concepts li::before{content:"";position:absolute;left:0;top:.6em;width:6px;height:6px;border-radius:50%;background:var(--gold);}
.concepts.cool li::before{background:var(--blue);}.concepts.grn li::before{background:var(--green);}
.concepts li b{color:var(--ink);font-weight:600;}
.split{display:grid;grid-template-columns:.92fr 1.08fr;gap:clamp(2rem,5vw,4.5rem);align-items:center;width:100%;}
.split.even{grid-template-columns:1fr 1fr;}
.build{background:linear-gradient(160deg,rgba(212,162,78,.12),rgba(212,162,78,.02));border:1px solid rgba(212,162,78,.28);border-radius:22px;padding:1.7rem 1.8rem;width:100%;}
.build.cool{background:linear-gradient(160deg,rgba(41,151,255,.12),rgba(41,151,255,.02));border-color:rgba(41,151,255,.28);}
.build.grn{background:linear-gradient(160deg,rgba(95,211,155,.12),rgba(95,211,155,.02));border-color:rgba(95,211,155,.28);}
.build .bl{font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);font-weight:600;margin-bottom:1rem;}
.build.cool .bl{color:var(--blue);}.build.grn .bl{color:var(--green);}
.build ul{list-style:none;display:flex;flex-direction:column;gap:.7rem;}
.build li{font-size:clamp(.92rem,1.4vw,1.15rem);line-height:1.35;padding-left:1.7rem;position:relative;color:var(--ink);font-weight:450;}
.build li::before{content:"\\2192";position:absolute;left:0;color:var(--gold);font-weight:600;}
.build.cool li::before{color:var(--blue);}.build.grn li::before{color:var(--green);}
.outcomes{list-style:none;display:flex;flex-direction:column;gap:1rem;margin-top:1.6rem;max-width:66ch;}
.outcomes li{font-size:clamp(1rem,1.6vw,1.35rem);color:var(--dim);line-height:1.3;padding-left:2.1rem;position:relative;}
.outcomes li::before{content:"\\2713";position:absolute;left:0;top:0;color:var(--gold);font-weight:700;font-size:1.05em;}
.outcomes li b{color:var(--ink);font-weight:600;}
.price-badge{display:inline-flex;flex-direction:column;align-items:center;padding:1.8rem 3rem;border-radius:26px;
  background:linear-gradient(160deg,rgba(212,162,78,.14),rgba(212,162,78,.03));border:1px solid rgba(212,162,78,.3);margin-top:2rem;}
.price-badge .pl{font-size:.74rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);font-weight:600;}
.price-badge .pv{font-weight:700;letter-spacing:-.03em;margin-top:.4rem;line-height:1;}
.glow{position:absolute;border-radius:50%;filter:blur(120px);opacity:.5;pointer-events:none;z-index:-1;}
.glow.g1{width:600px;height:600px;background:radial-gradient(circle,rgba(212,162,78,.22),transparent 70%);top:-15%;right:-10%;}
.glow.g2{width:520px;height:520px;background:radial-gradient(circle,rgba(41,151,255,.14),transparent 70%);bottom:-20%;left:-8%;}
.glow.g3{width:520px;height:520px;background:radial-gradient(circle,rgba(95,211,155,.13),transparent 70%);top:-12%;left:-8%;}
/* progress + chrome */
.progress{position:fixed;top:0;left:0;height:2px;background:linear-gradient(90deg,var(--gold),var(--gold-soft));z-index:50;transition:width .5s ease;}
.chrome{position:fixed;bottom:2vh;left:0;right:0;display:flex;justify-content:space-between;align-items:center;padding:0 8.5vw;z-index:40;font-size:.76rem;color:var(--dimmer);pointer-events:none;}
.chrome .brand{font-weight:600;letter-spacing:.02em;color:var(--dim);}
.chrome .brand b{color:var(--gold);}
.chrome .right{display:flex;gap:1.2rem;align-items:center;pointer-events:auto;}
.notesbtn{cursor:pointer;border:1px solid var(--line);border-radius:6px;padding:3px 9px;color:var(--dim);font-size:.72rem;transition:all .3s;}
.notesbtn:hover{border-color:var(--gold);color:var(--gold);}
.counter{font-family:"SF Mono",ui-monospace,monospace;letter-spacing:.05em;}
/* speaker notes panel */
.notes{position:fixed;left:0;right:0;bottom:0;z-index:60;background:rgba(12,12,14,.97);
  border-top:1px solid var(--line);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  transform:translateY(100%);transition:transform .4s cubic-bezier(.22,.61,.36,1);max-height:46vh;display:flex;flex-direction:column;}
.notes.open{transform:translateY(0);}
.notes-head{display:flex;justify-content:space-between;align-items:center;padding:.9rem 8.5vw .6rem;border-bottom:1px solid var(--line);}
.notes-head .lbl{font-size:.7rem;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);font-weight:700;}
.notes-head .x{cursor:pointer;color:var(--dim);font-size:1.1rem;line-height:1;}
.notes-body{overflow-y:auto;padding:1.1rem 8.5vw 1.6rem;font-size:.95rem;line-height:1.6;color:#cfcfd4;}
.notes-body a{color:var(--gold-soft);text-decoration:underline;text-underline-offset:2px;}
.notes-body a:hover{color:var(--gold);}
.notes-body b{color:var(--ink);}.notes-body i,.notes-body em{color:#e8c583;font-style:italic;}
.notes-body u{text-decoration:underline;}
.hint{position:fixed;bottom:2vh;left:50%;transform:translateX(-50%);font-size:.72rem;color:var(--dimmer);z-index:41;display:flex;gap:.5rem;align-items:center;animation:fade 4s ease 3s forwards;}
@keyframes fade{to{opacity:0;visibility:hidden;}}
.key{display:inline-flex;align-items:center;justify-content:center;min-width:20px;height:20px;padding:0 5px;border:1px solid var(--line);border-radius:5px;font-family:"SF Mono",monospace;font-size:.66rem;}
@media (max-width:860px){
  .slide{padding:8vh 6vw;}.split,.split.even{grid-template-columns:1fr;gap:1.4rem;}
  .mod-grid{grid-template-columns:1fr;}
  .notes-head,.notes-body{padding-left:6vw;padding-right:6vw;}
}
@media (prefers-reduced-motion:reduce){.slide,.slide .reveal{transition:opacity .2s;animation:none!important;}}
.tanglish-sub{font-size:clamp(1rem,1.5vw,1.25rem);font-weight:500;color:var(--gold-soft);margin-top:.5rem;font-style:italic;opacity:.9;}
.person-img {
  position: absolute;
  right: 5vw;
  bottom: 0;
  height: 80vh;
  object-fit: contain;
  z-index: -1;
  opacity: 0;
  transform: translateX(40px);
  transition: opacity 1.2s cubic-bezier(0.22, 0.61, 0.36, 1), transform 1.2s cubic-bezier(0.22, 0.61, 0.36, 1);
  filter: grayscale(40%) contrast(1.1) brightness(0.9);
  mask-image: linear-gradient(to top, transparent 0%, black 25%, black 95%, transparent 100%);
  -webkit-mask-image: linear-gradient(to top, transparent 0%, black 25%, black 95%, transparent 100%);
}
.slide.active .person-img { opacity: 0.6; transform: translateX(0); }
.person-img.cool { filter: drop-shadow(0 0 40px rgba(41,151,255,0.25)) grayscale(40%) contrast(1.1); }
.person-img.grn { filter: drop-shadow(0 0 40px rgba(95,211,155,0.25)) grayscale(40%) contrast(1.1); }
.person-img.gold { filter: drop-shadow(0 0 40px rgba(212,162,78,0.25)) grayscale(40%) contrast(1.1); }
.person-img.blend-screen { mix-blend-mode: screen; right: -5vw; height: 90vh; }
.slide.has-img { align-items: flex-start; }
.slide.has-img > *:not(.person-img):not(.glow) { max-width: 55vw; position: relative; z-index: 2; }
.slide.center.has-img { text-align: left; }
.slide.center.has-img .lead { margin-left: 0; }
</style>
</head>
<body>
<div class="progress" id="progress"></div>
<div class="deck" id="deck">

<!-- 1. INTRO -->
<section class="slide center active"><div class="glow g1"></div><div class="glow g2"></div>
<div class="eyebrow reveal">Part 1 &middot; The Hook</div>
<h1 class="reveal">The<br><span class="grad">Foundations</span></h1>
<p class="lead reveal" style="margin-top:2rem;">The mathematics, the history, and the hard truth about the job market —<br>for the engineer who refuses to be replaced.</p>
</section>

<section class="slide center"><div class="glow g1"></div>
<div class="eyebrow reveal">Part 1 &middot; The Hook</div>
<h2 class="reveal">Your Marks<br>won't get you the job.</h2>
<p class="lead reveal" style="margin-top:2.2rem;">In 2015, high marks got you an interview.<br>In 2026, they just put you in a huge pile of identical resumes.</p>
<p class="kicker reveal">We will show you the exact secret to stand <em>out</em> from that pile.</p>
</section>

<!-- TERMINOLOGY (5 SLIDES) -->
<section class="slide center">
<div class="glow g2"></div>
<div class="eyebrow cool reveal">Terminology &middot; The Basics</div>
<h2 class="reveal">Wait. What is AI?</h2>
<p class="lead reveal" style="margin-top:1.4rem;">Everyone uses the word. What does it actually mean?</p>
<div class="step" style="margin-top:3rem;">
<h3 class="grad-cool">The "Smart" Washing Machine Analogy</h3>
<p class="lead" style="margin-top:1rem; max-width: 800px; margin-left: auto; margin-right: auto;">
If a machine does something that usually requires human intelligence — like washing clothes based on weight — it's Artificial Intelligence. But it's just following rigid rules written by a programmer. <b>(If X, then Y)</b>.
</p>
</div>
</section>

<section class="slide center">
<div class="eyebrow grn reveal">Terminology &middot; The Basics</div>
<h2 class="reveal">What is Machine Learning (ML)?</h2>
<div class="step" style="margin-top:3rem;">
<h3 class="grad-grn">The "Bicycle Riding" Analogy</h3>
<p class="lead" style="margin-top:1rem; max-width: 800px; margin-left: auto; margin-right: auto;">
You cannot teach someone to ride a bicycle by giving them a rulebook. They have to fall down 100 times until their brain learns the balance. ML is the same: the machine learns the rules by looking at data and making mistakes, not by code.
</p>
</div>
</section>

<section class="slide center">
<div class="eyebrow cool reveal">Terminology &middot; The Basics</div>
<h2 class="reveal">What is Deep Learning (DL)?</h2>
<div class="step" style="margin-top:3rem;">
<h3 class="grad-cool">The "Corporate Hierarchy" Analogy</h3>
<p class="lead" style="margin-top:1rem; max-width: 800px; margin-left: auto; margin-right: auto;">
It's Machine Learning, but passed through a huge corporate structure (Neural Networks). The intern looks at the edges. The manager looks at the shapes. The CEO says, "That's a picture of a cat." Many layers deep.
</p>
</div>
</section>

<section class="slide center">
<div class="eyebrow grn reveal">Terminology &middot; The Basics</div>
<h2 class="reveal">What is Generative AI?</h2>
<div class="step" style="margin-top:3rem;">
<h3 class="grad-grn">The "Making Dosa" Analogy</h3>
<p class="lead" style="margin-top:1rem; max-width: 800px; margin-left: auto; margin-right: auto;">
Earlier AI just looked at a Dosa and said "Yes, it is Dosa" (Classification). Generative AI looks at a million Dosas, learns the pattern, and <b>cooks a brand new Dosa that has never existed before</b> (Creation). ChatGPT is GenAI.
</p>
</div>
</section>

<section class="slide has-img">
<div class="eyebrow reveal">Terminology &middot; The Basics</div>
<h3 class="reveal">AI is a set of nested dolls.</h3>
<ul class="concepts reveal" style="margin-top:1.8rem;">
<li><b>Artificial Intelligence</b> — the big doll: any machine doing something "smart"</li>
<li><b>Machine Learning</b> — inside it: machines that learn from data, not rules</li>
<li><b>Deep Learning</b> — inside that: learning with many-layered neural networks</li>
<li><b>Generative AI</b> — the smallest doll: deep nets that <em>create</em></li>
</ul>
<img src="../../assets/matryoshka.png" class="person-img gold blend-screen" alt="Matryoshka" />
</section>

<!-- THE 3 TYPES OF ML -->
<section class="slide">
<div class="eyebrow reveal">Part 1 &middot; How Machines Learn</div>
<h2 class="reveal grad" style="font-size:clamp(3rem,6vw,5.5rem);line-height:1;">Supervised<br>Learning</h2>
<h3 class="reveal" style="margin-top:1rem;margin-bottom:1.6rem;">Exam-kku Padikkurathu</h3>
<div class="tanglish-sub reveal">Pazhaya question paper vechu padikkurathu thaan Supervised Learning.</div>
<p class="lead reveal" style="margin-top:1.8rem;">When we give the AI both the questions and the answers. Just like studying with 10 years of solved question papers, the AI looks at the answers until it memorizes the pattern.</p>
</section>

<section class="slide">
<div class="eyebrow cool reveal">Part 1 &middot; How Machines Learn</div>
<h2 class="reveal grad-cool" style="font-size:clamp(3rem,6vw,5.5rem);line-height:1;">Unsupervised<br>Learning</h2>
<h3 class="reveal" style="margin-top:1rem;margin-bottom:1.6rem;">Room-a Sutham Pandrathu</h3>
<div class="tanglish-sub reveal">Amma illatha neram, enga edhu irukkum nu naama set pandrathu.</div>
<p class="lead reveal" style="margin-top:1.8rem;">Finding patterns with no answer key. Nobody tells you what the groups are, but you naturally put all the shirts in one pile, and books in another. The AI clusters raw data exactly like this.</p>
</section>

<section class="slide">
<div class="eyebrow grn reveal">Part 1 &middot; How Machines Learn</div>
<h2 class="reveal grad-grn" style="font-size:clamp(3rem,6vw,5.5rem);line-height:1;">Reinforcement<br>Learning</h2>
<h3 class="reveal" style="margin-top:1rem;margin-bottom:1.6rem;">PUBG-la Adi Vaangi Kathukurathu</h3>
<div class="tanglish-sub reveal">Thappu panna adi, correct-a panna Chicken Dinner.</div>
<p class="lead reveal" style="margin-top:1.8rem;">Learning by reward and punishment. You don't have a manual, you just land in the game, get shot (penalty), and learn never to stand there again. Over time, the AI becomes a pro through pure trial and error.</p>
</section>

<!-- THE HISTORY / PEOPLE -->
<section class="slide"><div class="glow g2"></div>
<div class="eyebrow cool reveal">Part 2 &middot; The Foundations</div>
<div class="big-num grad-cool reveal">02</div><h2 class="reveal" style="margin-top:1rem;">The people they<br>didn't tell you about.</h2>
<p class="lead reveal" style="margin-top:1.4rem;">AI wasn't born in Silicon Valley.<br>It was built by outsiders, exiles, and geniuses history forgot.</p>
</section>

<section class="slide has-img">
<div class="eyebrow cool reveal">Part 2 &middot; The Foundations</div>
<h3 class="reveal">Veedu Illa, Degree Illa...</h3>
<div class="step">
<h2 class="grad-cool" style="font-size:4rem; margin: 1rem 0;">Walter Pitts.</h2>
</div>
<p class="lead reveal" style="margin-top:1.6rem;">15 vayasu payyan, veeta vittu odi vanthu Chicago park-la thoongi kittu irunthan. Avan thaan 1943-la <em>Artificial Neuron</em>-oda first mathematical model-a ezhuthunaan.</p>
<p class="kicker reveal">Inniku irukka ChatGPT, Deep Learning ellathukum adippadai intha veedu illatha payyan thaan. He had no degree.</p>
<img src="../../assets/walter_pitts.png" class="person-img cool" alt="Walter Pitts" />
</section>

<section class="slide has-img">
<div class="eyebrow cool reveal">Part 2 &middot; The Foundations</div>
<h3 class="reveal">Kaalathukku Mundhina Thalaivan.</h3>
<div class="step">
<h2 class="grad-cool" style="font-size:3.5rem; margin: 1rem 0;">Frank Rosenblatt.</h2>
</div>
<p class="lead reveal" style="margin-top:1.6rem;">1958-la avar oru machine senjaar. Athu athuvave shape-a paarthu <em>kattukkum</em> (learn pannum). New York Times paper-la potanga: "Ithu thaan nadakkum, pesum, yosikkum computer-oda aarambam" nu.</p>
<p class="kicker reveal">Aana ulagam avara nambala. 1971-la avaroda 43rd birthday anniku avar padagu vibathula iranthutaar.</p>
<img src="../../assets/frank_rosenblatt.png" class="person-img cool" alt="Frank Rosenblatt" />
</section>

<section class="slide">
<div class="eyebrow cool reveal">Part 2 &middot; The Foundations</div>
<h3 class="reveal">The Book That Killed AI.</h3>
<div class="step">
<h2 class="grad-cool" style="font-size:3rem; margin: 1rem 0;">15 Varusha Iruttu (AI Winter).</h2>
</div>
<p class="lead reveal" style="margin-top:1.6rem;">1969-la Minsky and Papert oru book ezhuthinanga. Oru single neuron-aala oru simple logic (XOR) kooda panna mudiyathu nu prove pannitanga. Udane US government funding-a niruthitanga. 15 varusham AI research dead!</p>
<p class="kicker reveal">Problem enna-na, oru neuron-ala mudiyathu, aana neraya neurons-a "Layers" a vecha mudiyum. Ulagathuku athu appo puriyala.</p>
</section>

<section class="slide has-img">
<div class="eyebrow cool reveal">Part 2 &middot; The Foundations</div>
<h3 class="reveal">The Soviet Secret.</h3>
<div class="step">
<h2 class="grad-cool" style="font-size:3rem; margin: 1rem 0;">Alexey Ivakhnenko.</h2>
</div>
<p class="lead reveal" style="margin-top:1.6rem;">America AI sethu pochu nu thoongitu iruntha nerathula, 1965-la Soviet Ukraine-la ivar 8 layers aazham ulla first Deep Learning network-a uruvakkitar.</p>
<p class="kicker reveal">Geoffrey Hinton deep learning-a famous aakurathuku 20 varusham munnadiye, Ivakhnenko katti mudichitar. History is written by those who market best.</p>
<img src="../../assets/alexey_ivakhnenko.png" class="person-img cool portrait" alt="Alexey Ivakhnenko" />
</section>

<section class="slide">
<div class="eyebrow cool reveal">Part 2 &middot; The Foundations</div>
<h3 class="reveal">The First Chatbot (1966).</h3>
<div class="step">
<h2 class="grad-cool" style="font-size:3.5rem; margin: 1rem 0;">ELIZA.</h2>
</div>
<p class="lead reveal" style="margin-top:1.6rem;">Joseph Weizenbaum built a program that acted like a therapist. It didn't understand anything — it just matched text patterns and repeated your words back as questions. "I feel sad" -> "Why do you feel sad?"</p>
<p class="kicker reveal">Makkal athu kitta manasa vittu pesinanga. ChatGPT-kku 50 varusham munnadi vantha muthal AI illusion.</p>
</section>

<section class="slide has-img">
<div class="eyebrow cool reveal">Part 2 &middot; The Foundations</div>
<h3 class="reveal">The Man Who Taught The World.</h3>
<div class="step">
<h2 class="grad-cool" style="font-size:3.5rem; margin: 1rem 0;">Andrew Ng.</h2>
</div>
<p class="lead reveal" style="margin-top:1.6rem;">Google Brain co-founder. Avaroda Coursera Machine Learning course-a mattum 5 million students padichirkanga. AI-a corporate secrets-la irunthu veliya kondu vanthu ellarukkum solli kudutha aasaan.</p>
<p class="kicker reveal">"AI is the new electricity."</p>
<img src="../../assets/ml_ng.png" class="person-img cool portrait" alt="Andrew Ng" />
</section>

<section class="slide has-img">
<div class="eyebrow cool reveal">Part 2 &middot; The Foundations</div>
<h3 class="reveal">The Architect of the Panic.</h3>
<div class="step">
<h2 class="grad-cool" style="font-size:3.5rem; margin: 1rem 0;">Sam Altman.</h2>
</div>
<p class="lead reveal" style="margin-top:1.6rem;">Decades of research-a oru product a maathi, 2 maasathula 100 million users-kku kondu ponaar. Nov 30, 2022-la ChatGPT launch aana appuram ulagam pazhaya padi illa.</p>
<p class="kicker reveal">Research is great, but distribution changes the world.</p>
<img src="../../assets/ml_altman.png" class="person-img cool portrait" alt="Sam Altman" />
</section>


<!-- MATH / VECTORS / MATRICES -->
<section class="slide has-img"><div class="glow g3"></div>
<div class="eyebrow grn reveal">Part 3 &middot; The Machine</div>
<div class="big-num grad-grn reveal">03</div><h2 class="reveal" style="margin-top:1rem;">The Engineering.</h2>
<p class="lead reveal" style="margin-top:1.4rem;">Clean, crystal clear words.<br>No jargon. Just the engine that powers the modern world.</p>
<img src="../../assets/abacus.png" class="person-img gold blend-screen" alt="Abacus" />
</section>

<section class="slide has-img">
<div class="eyebrow grn reveal">Part 3 &middot; The Machine</div>
<div style="max-width: 55vw;">
<h3 class="reveal">The Vector: Kolam</h3>
<div class="tanglish-sub reveal">Pulligal sernthaa kolam, numbers sernthaa vector.</div>
<p class="lead reveal" style="margin-top:1.6rem;">Every word is just a dot in a Kolam. A vector is a list of numbers pointing to a specific dot. AI turns words, faces, and songs into these points. It measures meaning using <em>distance</em> between the dots.</p>
<p class="kicker reveal">King − Man + Woman ≈ Queen.</p>
</div>
<img src="../../assets/kolam.png" class="person-img grn blend-screen" alt="Kolam Pattern" />
</section>

<section class="slide">
<div class="eyebrow grn reveal">Part 3 &middot; The Machine</div>
<h2 class="reveal grad-grn" style="font-size:3.5rem; margin-bottom: 1rem;">The Vector: Bookshelf</h2>
<h3 class="reveal">A Crystal Clear Analogy</h3>
<div class="tanglish-sub reveal">Oru library-la book-a thedurathu thaan Vector Search.</div>
<p class="lead reveal" style="margin-top:1.6rem;">Imagine a massive library. If you want a book about "Space Travel", you don't read every book. You go to the Science Fiction aisle (the coordinate). A Vector is exactly this: a coordinate that tells the AI exactly which shelf a concept lives on.</p>
<p class="kicker reveal">When you ask ChatGPT a question, it converts your sentence into a Vector, finds the shelf, and returns the nearest ideas.</p>
</section>

<section class="slide has-img">
<div class="eyebrow grn reveal">Part 3 &middot; The Machine</div>
<div style="max-width: 55vw;">
<h3 class="reveal">The Matrix: Maavu Aatra Machine.</h3>
<div class="tanglish-sub reveal">Arisiya maava maathuradhu dhaan Matrix.</div>
<p class="lead reveal" style="margin-top:1.6rem;">If a vector is raw rice, a <b>Matrix</b> is the grinder machine that stretches and reshapes it into batter. A neural network is just a series of these grinders stacked together. It takes raw data, crushes it, and transforms it into an answer.</p>
<p class="kicker reveal">"Deep" learning literally means: many Matrix transformations, stacked deep.</p>
</div>
<img src="../../assets/ml_idli.png" class="person-img gold blend-screen" alt="Idli" />
</section>

<section class="slide">
<div class="eyebrow grn reveal">Part 3 &middot; The Machine</div>
<h2 class="reveal grad-grn" style="font-size:3.5rem; margin-bottom: 1rem;">Matrix Multiplication<br>is the Universe.</h2>
<p class="lead reveal" style="margin-top:1.6rem;">In 1850, James Joseph Sylvester coined the term "Matrix". It was pure math. Today, 99% of the computational power on Earth is dedicated to multiplying matrices together.</p>
<ul class="concepts grn reveal" style="margin-top:1.8rem;">
<li>When ChatGPT generates a word? <b>Matrix Multiplication.</b></li>
<li>When your phone recognizes your face? <b>Matrix Multiplication.</b></li>
<li>When Nvidia sells a $40,000 GPU? <b>It is just a calculator built specifically to multiply matrices incredibly fast.</b></li>
</ul>
</section>


<!-- THE MARKET & T-SHAPED -->
<section class="slide center has-img"><div class="glow g2"></div>
<div class="eyebrow reveal">Part 4 &middot; The Market</div>
<h2 class="reveal grad">The T-Shaped Engineer.</h2>
<p class="lead reveal" style="margin-top:2rem;">Companies don't hire people who know "a little bit of everything".<br>They hire T-Shaped Researchers.</p>
<div class="step" style="margin-top:3rem;">
<h3 class="grad-cool" style="margin-bottom:1rem;">What is a T-Shape?</h3>
<p class="lead" style="text-align: left; max-width: 800px; margin: 0 auto;">
<b>The Horizontal Bar (Breadth):</b> You understand the whole landscape. You know what Python, Data, Models, Deployment, and Security are. You can talk to any team.<br><br>
<b>The Vertical Bar (Depth):</b> You are an absolute master in ONE specific thing. (Example: RAG Systems, or Computer Vision). When a hard problem in that specific area comes up, YOU are the person they call.<br><br>
<em>Generalists get automated. Specialists get isolated. T-Shaped Engineers get hired.</em>
</p>
</div>
<img src="../../assets/t_shape.png" class="person-img cool blend-screen" alt="T-Shape" />
</section>

<section class="slide center">
<div class="eyebrow reveal">Part 5 &middot; The Bridge</div>
<h2 class="reveal">Don't leave this room<br><span class="grad">the same as you walked in.</span></h2>
<p class="lead reveal" style="margin-top:2rem;">Talk to me before you go. Claim a founding-cohort seat.<br>Start building the version of your career that AI can't touch.</p>
<div class="price-badge reveal"><div class="pl">Founding Cohort · This Room Only</div><div class="pv" style="font-size:clamp(2rem,5vw,3.2rem);">Talk to me →</div></div>
</section>

</div>

<div class="chrome">
  <div class="brand">RISE<b>LABS</b> · The Foundations</div>
  <div class="right">
    <div class="notesbtn" id="notesbtn">S · Speaker Notes</div>
    <div class="counter"><span id="cur">01</span> / <span id="tot">...</span></div>
  </div>
</div>
<div class="hint"><span class="key">&larr;</span><span class="key">&rarr;</span> navigate · <span class="key">S</span> speaker notes · <span class="key">F</span> fullscreen</div>

<div class="notes" id="notes">
  <div class="notes-head"><div class="lbl">Speech Track</div><div class="x" id="notesx">&times;</div></div>
  <div class="notes-body" id="notesbody"></div>
</div>

<script>
const NOTES=[];
const slides=[...document.querySelectorAll('.slide')];
const progress=document.getElementById('progress');
const cur=document.getElementById('cur');
const tot=document.getElementById('tot');
const notesEl=document.getElementById('notes');
const notesBody=document.getElementById('notesbody');
let i=0;

tot.textContent = slides.length;

function renderNotes(){notesBody.innerHTML=NOTES[i]||'<i>No notes for this slide.</i>';notesBody.scrollTop=0;}
function go(n){
  if(n<0||n>=slides.length)return;
  slides[i].classList.remove('active');
  slides[i].querySelectorAll('.step.revealed').forEach(el=>el.classList.remove('revealed'));
  slides[i].classList.add('prev');
  i=n;
  slides.forEach(s=>s.classList.remove('prev'));
  slides[i].classList.add('active');
  progress.style.width=((i+1)/slides.length*100)+'%';
  cur.textContent=String(i+1).padStart(2,'0');
  if(notesEl.classList.contains('open'))renderNotes();
}

function next() {
  const currentSlide = slides[i];
  const steps = currentSlide.querySelectorAll('.step:not(.revealed)');
  if (steps.length > 0) {
    steps[0].classList.add('revealed');
  } else {
    go(i + 1);
  }
}

function prev() {
  go(i - 1);
}

go(0);
function toggleNotes(){notesEl.classList.toggle('open');if(notesEl.classList.contains('open'))renderNotes();}
document.getElementById('notesbtn').addEventListener('click',toggleNotes);
document.getElementById('notesx').addEventListener('click',()=>notesEl.classList.remove('open'));
document.addEventListener('keydown',e=>{
  if(e.key==='ArrowRight'||e.key==='ArrowDown'||e.key===' '){e.preventDefault();next();}
  else if(e.key==='ArrowLeft'||e.key==='ArrowUp'){e.preventDefault();prev();}
  else if(e.key==='Home'){go(0);}else if(e.key==='End'){go(slides.length-1);}
  else if(e.key==='s'||e.key==='S'){toggleNotes();}
  else if(e.key==='f'||e.key==='F'){if(!document.fullscreenElement)document.documentElement.requestFullscreen();else document.exitFullscreen();}
  else if(e.key==='Escape'){notesEl.classList.remove('open');}
});
let x0=null;
document.addEventListener('touchstart',e=>x0=e.touches[0].clientX,{passive:true});
document.addEventListener('touchend',e=>{
  if(x0===null)return;
  const dx=e.changedTouches[0].clientX-x0;
  if(Math.abs(dx)>50){ dx<0?next():prev(); }
  x0=null;
},{passive:true});
document.getElementById('deck').addEventListener('click',e=>{
  if(e.target.closest('.mod')||e.target.closest('a')||e.target.closest('.notes'))return;
  e.clientX>innerWidth/2 ? next() : prev();
});
</script>
</body>
</html>
"""

with open(os.path.join(PROJECT_ROOT, "HTML", "AI Foundations", "The Foundations.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated 'The Foundations.html' successfully.")
