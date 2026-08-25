
const S = [
// ──────── WELCOME ────────
{bg:'bg-b', html:`
<div class="glow" style="width:600px;height:600px;background:var(--blue);top:-10%;right:-5%"></div>
<p class="lbl dim" style="margin-bottom:18px">RiseLabs presents</p>
<h1 class="hero">AI Foundations<br><span class="grb">Seminar.</span></h1>
<p class="sub" style="margin-top:20px;opacity:.5">Decoding the jargon. Understanding the reality.</p>
`},

// ──────── ACT 0: THE PANIC ────────
{bg:'bg-b', html:`
<p class="lbl" style="color:var(--red);margin-bottom:14px">The State of the World</p>
<h2 class="hero">The AI<br><span class="grc">Panic.</span></h2>
<p class="sub" style="margin-top:18px;opacity:.5">You hear these words in every meeting, on every news channel, and on every LinkedIn post. But what do they actually mean?</p>
<div class="step">
<img src="assets/ml_panic.png" class="person-img cool" alt="Panic" />
</div>
`},

{bg:'bg-w', html:`
<p class="lbl" style="color:var(--blue);margin-bottom:14px">Buzzword Decoding</p>
<h2 class="med">"Algorithm"</h2>
<p class="sub" style="margin-top:14px;opacity:.6">You hear it everywhere. What is it really?</p>
<div class="step">
<div class="math-block math-l" style="color:var(--blue);">
<strong>The Simple Analogy:</strong><br><br>
It's just a cooking recipe. Step 1, Step 2, Step 3. If you follow the steps exactly, you get the dish. If you miss a step, it fails.
</div>
<img src="assets/ml_recipe.png" class="person-img gold" alt="Recipe" style="mix-blend-mode:multiply;" />
</div>
`},

{bg:'bg-g', html:`
<p class="lbl" style="color:var(--purple);margin-bottom:14px">Buzzword Decoding</p>
<h2 class="med">"Parameters & Weights"</h2>
<p class="sub" style="margin-top:14px;opacity:.6">A model has "175 Billion Parameters". What are they?</p>
<div class="step">
<div class="math-block math-l" style="color:var(--purple);">
<strong>The Simple Analogy:</strong><br><br>
Think of an old radio. The parameters are the tuning knobs for volume, bass, and frequency. You twist and adjust them until the music comes through perfectly clear.
</div>
<img src="assets/ml_radio.png" class="person-img cool" alt="Radio" style="mix-blend-mode:multiply;" />
</div>
`},

{bg:'bg-w', html:`
<p class="lbl" style="color:var(--green);margin-bottom:14px">Buzzword Decoding</p>
<h2 class="med">"Training Data"</h2>
<p class="sub" style="margin-top:14px;opacity:.6">Why do AI models need terabytes of data?</p>
<div class="step">
<div class="math-block math-l" style="color:var(--green);">
<strong>The Simple Analogy:</strong><br><br>
It is like solving the past 10 years of Anna University question papers before a final exam. The more past papers you see, the better you perform on the real test.
</div>
<img src="assets/ml_exam.png" class="person-img gold" alt="Exam" style="mix-blend-mode:multiply;" />
</div>
`},

{bg:'bg-b', html:`
<p class="lbl" style="color:var(--orange);margin-bottom:14px">Buzzword Decoding</p>
<h2 class="med">"Overfitting"</h2>
<p class="sub" style="margin-top:14px;opacity:.6">Why does the AI sometimes fail in the real world?</p>
<div class="step">
<div class="math-block math-d" style="color:var(--orange);">
<strong>The Simple Analogy:</strong><br><br>
Mugging up the textbook line-by-line. You score 100% on the practice test, but when the professor twists the question slightly in the real exam, you fail completely.
</div>
<img src="assets/ml_overfit.png" class="person-img cool" alt="Overfit" />
</div>
`},

{bg:'bg-g', html:`
<p class="lbl" style="color:var(--pink);margin-bottom:14px">Buzzword Decoding</p>
<h2 class="med">"GPU (Graphics Processing Unit)"</h2>
<p class="sub" style="margin-top:14px;opacity:.6">Why is everyone buying Nvidia GPUs for AI?</p>
<div class="step">
<div class="math-block math-l" style="color:var(--pink);">
<strong>The Simple Analogy:</strong><br><br>
A CPU is like 4 genius professors solving complex math one by one. A GPU is like 10,000 average students working together to solve thousands of simple math problems at the exact same time.
</div>
<img src="assets/ml_factory.png" class="person-img cool" alt="Factory" style="mix-blend-mode:multiply;" />
</div>
`},

{bg:'bg-w', html:`
<p class="lbl" style="color:var(--teal);margin-bottom:14px">The Pioneers</p>
<h2 class="med">Geoffrey Hinton</h2>
<p class="sub" style="margin-top:14px;opacity:.6">Who is he?</p>
<div class="step">
<div class="math-block math-l" style="color:var(--teal);">
The "Godfather of AI". When the world gave up on neural networks in the 1990s, he kept believing and proved they could work.
</div>
<img src="assets/ml_hinton.png" class="person-img cool" alt="Hinton" style="mix-blend-mode:multiply;" />
</div>
`},

{bg:'bg-b', html:`
<p class="lbl" style="color:var(--blue);margin-bottom:14px">The Pioneers</p>
<h2 class="med">Andrew Ng</h2>
<p class="sub" style="margin-top:14px;opacity:.6">Who is he?</p>
<div class="step">
<div class="math-block math-d" style="color:var(--blue);">
The "Teacher of AI". He pioneered online AI education and co-founded Google Brain, democratizing ML for millions.
</div>
<img src="assets/ml_ng.png" class="person-img grn" alt="Ng" />
</div>
`},

{bg:'bg-g', html:`
<p class="lbl" style="color:var(--purple);margin-bottom:14px">The Pioneers</p>
<h2 class="med">Yann LeCun</h2>
<p class="sub" style="margin-top:14px;opacity:.6">Who is he?</p>
<div class="step">
<div class="math-block math-l" style="color:var(--purple);">
The "Visionary". He invented Convolutional Neural Networks, teaching machines how to see.
</div>
<img src="assets/ml_lecun.png" class="person-img gold" alt="LeCun" style="mix-blend-mode:multiply;" />
</div>
`},

{bg:'bg-w', html:`
<p class="lbl" style="color:var(--pink);margin-bottom:14px">The Pioneers</p>
<h2 class="med">Sam Altman</h2>
<p class="sub" style="margin-top:14px;opacity:.6">Who is he?</p>
<div class="step">
<div class="math-block math-l" style="color:var(--pink);">
The "Architect of the Boom". Packaged all this complex research into ChatGPT and triggered the current AI revolution.
</div>
<img src="assets/ml_altman.png" class="person-img cool" alt="Altman" style="mix-blend-mode:multiply;" />
</div>
`},

// ──────── ACT 1: ML FUNDAMENTALS ────────
{bg:'bg-b', html:`
<p class="lbl" style="color:var(--blue);margin-bottom:14px">The Foundation</p>
<h2 class="hero">Traditional Code vs.<br><span class="gbp">Machine Learning</span></h2>
<p class="sub" style="margin-top:14px;opacity:.6">What makes Machine Learning different from standard programming?</p>
<div class="step">
<div class="math-block math-d" style="color:var(--blue);">
<strong>The Simple Analogy (Idli Maavu):</strong><br><br>
In Traditional Code, you write exactly how much rice and urad dal to mix. (Rules → Answers)<br><br>
In Machine Learning, you show the computer 100 perfect Idlis and the ingredients, and it figures out the recipe itself! (Answers + Data → Rules)
</div>
<img src="assets/ml_idli.png" class="person-img gold" alt="Idli" />
</div>
`},

// ──────── ACT 2: MATHEMATICS ────────
{bg:'bg-g', html:`
<p class="lbl" style="color:var(--green);margin-bottom:14px">The Core Math</p>
<h2 class="med">"Gradient Descent"</h2>
<p class="sub" style="margin-top:14px;opacity:.6">How do models actually "learn" and improve?</p>
<div class="step">
<div class="math-block math-l" style="color:var(--green);">
<strong>The Simple Analogy (Malai Erangirathu):</strong><br><br>
Imagine you are blindfolded on top of a mountain. To get to the bottom, you feel the slope with your feet and take a small step downwards. You repeat this until it's flat. That's how AI minimizes its errors!
</div>
<img src="assets/ml_mountain.png" class="person-img cool" alt="Mountain" style="mix-blend-mode:multiply;" />
</div>
`},

// ──────── ACT 3: VISION ────────
{bg:'bg-w', html:`
<p class="lbl" style="color:var(--orange);margin-bottom:14px">Computer Vision</p>
<h2 class="med">"Convolutional Neural Networks (CNN)"</h2>
<p class="sub" style="margin-top:14px;opacity:.6">How do computers recognize a cat in a photo?</p>
<div class="step">
<div class="math-block math-l" style="color:var(--orange);">
<strong>The Simple Analogy:</strong><br><br>
Looking through a magnifying glass. First you scan for simple edges. Then you combine edges to see shapes. Then you combine shapes to see an ear or a tail. Finally, you recognize the cat.
</div>
<img src="assets/ml_lens.png" class="person-img cool" alt="Lens" style="mix-blend-mode:multiply;" />
</div>
`},

// ──────── ACT 4: NLP ────────
{bg:'bg-b', html:`
<p class="lbl" style="color:var(--teal);margin-bottom:14px">Language AI</p>
<h2 class="med">"Word Embeddings"</h2>
<p class="sub" style="margin-top:14px;opacity:.6">How does a computer understand that "King" and "Queen" are related?</p>
<div class="step">
<div class="math-block math-d" style="color:var(--teal);">
<strong>The Simple Analogy (Google Maps for Words):</strong><br><br>
Words are mapped as locations in space. "King" and "Queen" live on the same street. "Apple" and "Banana" live in a different neighborhood. The computer calculates the distance between them.
</div>
<img src="assets/ml_map.png" class="person-img grn" alt="Map" />
</div>
`},

{bg:'bg-w', html:`
<p class="lbl" style="color:var(--purple);margin-bottom:14px">Language AI</p>
<h2 class="med">"Next Token Prediction"</h2>
<p class="sub" style="margin-top:14px;opacity:.6">How does ChatGPT write paragraphs?</p>
<div class="step">
<div class="math-block math-l" style="color:var(--purple);">
<strong>The Simple Analogy:</strong><br><br>
It’s simply the world's most advanced autocomplete. It predicts the very next word based on all the previous words, over and over again.
</div>
<img src="assets/ml_tokens.png" class="person-img cool" alt="Tokens" style="mix-blend-mode:multiply;" />
</div>
`},

// ──────── ACT 5: TRANSFORMERS ────────
{bg:'bg-b', html:`
<p class="lbl" style="color:var(--yellow);margin-bottom:14px">The Breakthrough</p>
<h2 class="med">"Attention Is All You Need"</h2>
<p class="sub" style="margin-top:14px;opacity:.6">What makes modern AI (Transformers) so smart?</p>
<div class="step">
<div class="math-block math-d" style="color:var(--yellow);">
<strong>The Simple Analogy:</strong><br><br>
Instead of reading a book word-by-word and forgetting the start by the time it reaches the end, "Attention" allows the AI to look at the entire sentence at once, focusing only on the words that matter.
</div>
<img src="assets/ml_library.png" class="person-img cool" alt="Library" />
</div>
`},

// ──────── ACT 6: JOBS ────────
{bg:'bg-g', html:`
<p class="lbl" style="color:var(--red);margin-bottom:14px">The Reality Check</p>
<h2 class="sect">"AI Unga Job-a Edukkathu"</h2>
<p class="sub" style="margin-top:14px;opacity:.6">Will AI replace software engineers?</p>
<div class="step">
<div class="tang tang-l" style="color:var(--red);">
"AI won't take your job. But a person who knows how to use AI will take your job."<br><br>
Don't fear the tool. Learn how to wield it.
</div>
<img src="assets/ml_job.png" class="person-img grn" alt="Job" style="mix-blend-mode:multiply;" />
</div>
`},

{bg:'bg-w', html:`
<p class="lbl" style="color:var(--blue);margin-bottom:14px">The Path Forward</p>
<h2 class="med">The AI Engineer Career Pathway</h2>
<p class="sub" style="margin-top:14px;opacity:.6">How do you become an AI Engineer?</p>
<div class="step">
<div class="math-block math-l" style="color:var(--blue);">
<strong>The Simple Analogy (Filter Coffee):</strong><br><br>
You can't rush filter coffee. Math, Code, Theory, Projects — you must build them layer by layer. Skip the fundamentals, and your skills will taste watered down. Start building today.
</div>
<img src="assets/ml_coffee.png" class="person-img gold" alt="Coffee" style="mix-blend-mode:multiply;" />
</div>
`},

{bg:'bg-b', html:`
<div class="glow" style="width:700px;height:700px;background:var(--orange);top:-20%;left:-10%"></div>
<p class="pill" style="background:rgba(255,149,0,.15);color:var(--orange)">RiseLabs</p>
<h2 class="sect"><span class="goy">Learn to Build.</span></h2>
<p class="sub" style="margin-top:14px;opacity:.6">Join the RiseLabs AI Bootcamp. Real datasets, deployment, and industry mentorship.</p>
<div class="step">
<div style="font-size:32px;font-weight:700;color:var(--green);margin-top:24px;">WhatsApp: 9087929229</div>
<div style="font-size:24px;color:var(--blue);margin-top:8px;">riselabs.one</div>
<img src="assets/ml_bridge.png" class="person-img gold" alt="Bridge" />
</div>
`}
]; // end slides

const deck = document.getElementById('deck');
S.forEach((s,i) => {
  const div = document.createElement('div');
  div.className = `slide ${s.bg}` + (i===0?' active':'');
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
    steps[0].classList.add('revealed');
  } else {
    if (cur < tot - 1) go(cur + 1);
  }
}

function prev() {
  // Simple previous implementation
  if (cur > 0) go(cur - 1);
}

document.addEventListener('click', e => {
  if(e.target.closest('a')) return;
  e.clientX < window.innerWidth*.2 ? prev() : next();
});
document.addEventListener('keydown', e => {
  if(e.key==='ArrowRight'||e.key===' ') { e.preventDefault(); next(); }
  if(e.key==='ArrowLeft') prev();
});

go(0);
