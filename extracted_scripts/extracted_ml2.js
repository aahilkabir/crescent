
// ═══════════ SLIDE DATA ═══════════
const S = [

// ──────── ACT 1: WELCOME ────────
{bg:'bg-b', html:`
<div class="glow" style="width:600px;height:600px;background:var(--blue);top:-10%;right:-5%"></div>
<div class="glow" style="width:500px;height:500px;background:var(--purple);bottom:-15%;left:10%"></div>
<div class="glow" style="width:400px;height:400px;background:var(--pink);top:30%;right:30%"></div>
<p class="lbl dim a1" style="margin-bottom:18px">RiseLabs presents</p>
<h1 class="hero a2">Machine Learning<br><span class="grb">Foundations.</span></h1>
<p class="sub a3" style="margin-top:20px;opacity:.5">From linear algebra to large language models.<br>A CS50-depth journey into how machines learn.</p>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--blue);margin-bottom:16px">What We'll Cover</p>
<h2 class="sect a2" style="font-size:clamp(26px,3.5vw,48px)">Six acts.<br>One foundation.</h2>
<div class="tl a3">
<div class="tli"><div class="tldot" style="background:var(--blue)"></div><div><div class="tlc">Act 1 — What is Machine Learning?</div><div class="tls">Traditional code vs learning code</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--purple)"></div><div><div class="tlc">Act 2 — The Math That Makes It Work</div><div class="tls">Vectors, loss functions, gradient descent</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--green)"></div><div><div class="tlc">Act 3 — Neural Networks</div><div class="tls">Perceptrons, backprop, deep learning</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--orange)"></div><div><div class="tlc">Act 4 — NLP & Understanding Language</div><div class="tls">Tokenization, embeddings, RNNs</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--pink)"></div><div><div class="tlc">Act 5 — Transformers & LLMs</div><div class="tls">Attention, GPT, BERT, scaling laws</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--red)"></div><div><div class="tlc">Act 6 — Your Career & The Market</div><div class="tls">Jobs, pathway, resources, RiseLabs</div></div></div>
</div>
`},

// ──────── ACT 1: WHAT IS ML ────────
{bg:'bg-b', html:`
<div class="glow" style="width:500px;height:500px;background:var(--blue);bottom:-20%;left:-10%"></div>
<p class="pill a1" style="background:rgba(0,122,255,.12);color:var(--blue)">Act 1</p>
<h2 class="hero a2" style="font-size:clamp(36px,5.5vw,76px)">What is<br><span class="gbp">Machine Learning?</span></h2>
<p class="sub a3" style="margin-top:18px;opacity:.5">"A computer program is said to learn from experience E, with respect to task T, if its performance P improves with experience."</p>
<p class="a4" style="font-size:clamp(12px,1vw,14px);opacity:.3;margin-top:8px">— Tom Mitchell, 1997</p>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--indigo);margin-bottom:14px">The Core Difference</p>
<h2 class="med a2">Traditional Code vs. ML Code</h2>
<div class="row a3">
<div class="card card-l" style="border-top:3px solid var(--red)">
<div class="ct" style="color:var(--red)">Traditional Programming</div>
<div class="diagram" style="margin-top:12px">
<div class="dbox" style="background:rgba(255,59,48,.1);color:var(--red)">Rules</div>
<div class="darr">+</div>
<div class="dbox" style="background:rgba(255,59,48,.1);color:var(--red)">Data</div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(255,59,48,.15);color:var(--red)">Answers</div>
</div>
<div class="cb" style="margin-top:10px">You write every rule by hand.<br>if temperature > 30: print("hot")</div>
</div>
<div class="card card-l" style="border-top:3px solid var(--green)">
<div class="ct" style="color:var(--green)">Machine Learning</div>
<div class="diagram" style="margin-top:12px">
<div class="dbox" style="background:rgba(52,199,89,.1);color:var(--green)">Data</div>
<div class="darr">+</div>
<div class="dbox" style="background:rgba(52,199,89,.1);color:var(--green)">Answers</div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(52,199,89,.15);color:var(--green)">Rules</div>
</div>
<div class="cb" style="margin-top:10px">The machine discovers the rules.<br>model.fit(temperatures, labels)</div>
</div>
</div>
`},

{bg:'bg-b', html:`
<p class="lbl a1" style="color:var(--teal);margin-bottom:14px">Tanglish Analogy</p>
<h2 class="sect a2" style="font-size:clamp(28px,4vw,56px)"><span class="ggt">"Idli Maavu Madiri"</span></h2>
<p class="body a3" style="margin-top:16px;opacity:.7">Traditional programming is like following an exact idli recipe — 2 cups rice, 1 cup dal, exactly 8 hours fermentation. If anything changes, it fails.</p>
<p class="body a4" style="margin-top:12px;opacity:.7">Machine learning is like your grandmother who <em>knows</em> from the feel of the batter, the weather, the smell — she learned from <strong>thousands of batches</strong>. She can't write the exact rules, but she gets perfect idlis every time.</p>
<div class="tang tang-d a5">"ML-la code ezhutharathu illai. Data kuduththu, computer-ai kaththukka vidurathu. Paatti idli maavu madiri — experience la irundu rules-a kandupidikkum."</div>

<img src="assets/ml_idli.png" class="person-img gold blend-screen" alt="Idli" />
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--purple);margin-bottom:14px">Three Paradigms</p>
<h2 class="med a2">Types of Machine Learning</h2>
<div class="row a3">
<div class="card card-l">
<div class="ci">🏷️</div>
<div class="ct" style="color:var(--blue)">Supervised Learning</div>
<div class="cb">You give the model labeled examples.<br>"This image = cat, this = dog."<br>It learns the mapping from input → output.</div>
<div style="margin-top:8px;font-size:11px;opacity:.4">Regression, Classification</div>
</div>
<div class="card card-l">
<div class="ci">🔍</div>
<div class="ct" style="color:var(--purple)">Unsupervised Learning</div>
<div class="cb">No labels. The model finds hidden patterns and structure in data on its own.<br>"Group these customers by behavior."</div>
<div style="margin-top:8px;font-size:11px;opacity:.4">Clustering, Dimensionality Reduction</div>
</div>
<div class="card card-l">
<div class="ci">🎮</div>
<div class="ct" style="color:var(--green)">Reinforcement Learning</div>
<div class="cb">The model learns by trial & reward. Like training a dog — good action gets a treat, bad action gets nothing.</div>
<div style="margin-top:8px;font-size:11px;opacity:.4">Games, Robotics, AlphaGo</div>
</div>
</div>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--orange);margin-bottom:14px">The ML Workflow</p>
<h2 class="med a2">How Every ML Project Works</h2>
<div class="diagram a3" style="flex-wrap:wrap;gap:12px;margin-top:24px">
<div class="dbox" style="background:rgba(0,122,255,.1);color:var(--blue);padding:14px 22px">1. Collect<br><span style="font-size:11px;opacity:.6">Gather data</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(175,82,222,.1);color:var(--purple);padding:14px 22px">2. Clean<br><span style="font-size:11px;opacity:.6">Remove noise</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(52,199,89,.1);color:var(--green);padding:14px 22px">3. Split<br><span style="font-size:11px;opacity:.6">Train / Test</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(255,149,0,.1);color:var(--orange);padding:14px 22px">4. Train<br><span style="font-size:11px;opacity:.6">Fit model</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(255,45,85,.1);color:var(--pink);padding:14px 22px">5. Evaluate<br><span style="font-size:11px;opacity:.6">Test accuracy</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(88,86,214,.1);color:var(--indigo);padding:14px 22px">6. Deploy<br><span style="font-size:11px;opacity:.6">Ship to prod</span></div>
</div>
<p class="body a4" style="margin-top:20px;opacity:.5;font-size:clamp(13px,1.2vw,16px)">80% of ML work is steps 1–3. The glamorous model training is only 20%.</p>
`},

// ──────── ACT 2: THE MATH ────────
{bg:'bg-b', html:`
<div class="glow" style="width:600px;height:600px;background:var(--purple);top:-15%;right:-10%"></div>
<p class="pill a1" style="background:rgba(175,82,222,.12);color:var(--purple)">Act 2</p>
<h2 class="hero a2" style="font-size:clamp(36px,5.5vw,76px)">The Math<br><span class="gip">Behind It All.</span></h2>
<p class="sub a3" style="margin-top:16px;opacity:.5">Don't panic. Every concept here builds on the one before it. By the end, you'll read equations like sentences.</p>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--blue);margin-bottom:14px">Building Block #1</p>
<h2 class="med a2">Vectors & Matrices</h2>
<p class="body a3" style="margin-top:12px">Everything in ML is a number. An image? A matrix of pixel values. A sentence? A vector of word encodings. A dataset? A big matrix where each row is one example.</p>
<div class="math-block math-l a4">
A vector:  x⃗ = [3, 7, 2]<br>
A matrix:  X = [[1, 2],<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3, 4],<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5, 6]]
</div>
<p class="a5" style="font-size:clamp(12px,1.1vw,15px);opacity:.4;margin-top:12px">Think of a vector as a point in space. A matrix is a spreadsheet.</p>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--purple);margin-bottom:14px">Building Block #2</p>
<h2 class="med a2">The Dot Product</h2>
<p class="body a3" style="margin-top:12px">The dot product measures <strong>similarity</strong> between two vectors. This single operation powers everything from recommendation systems to attention in transformers.</p>
<div class="math-block math-l a4" style="color:var(--purple)">
a⃗ · b⃗ = a₁b₁ + a₂b₂ + a₃b₃<br><br>
[1, 2, 3] · [4, 5, 6]<br>
= (1×4) + (2×5) + (3×6)<br>
= 4 + 10 + 18 = <span style="color:var(--green)">32</span>
</div>
<p class="a5" style="font-size:clamp(12px,1.1vw,15px);opacity:.4;margin-top:12px">High dot product = similar vectors. This is how search engines find relevant documents.</p>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--green);margin-bottom:14px">The Simplest Model</p>
<h2 class="med a2">Linear Regression</h2>
<p class="body a3" style="margin-top:12px">The "Hello World" of ML. Find the best line through your data points. Predict house price from area, salary from experience.</p>
<div class="math-block math-l a4" style="color:var(--green)">
ŷ = w · x + b<br><br>
<span style="font-size:.7em;opacity:.6">w = weight (slope)</span><br>
<span style="font-size:.7em;opacity:.6">b = bias (y-intercept)</span><br>
<span style="font-size:.7em;opacity:.6">ŷ = prediction</span>
</div>
<p class="a5" style="font-size:clamp(12px,1.1vw,15px);opacity:.4;margin-top:12px">The goal: find the w and b that make ŷ as close to the real y as possible.</p>
`},

{bg:'bg-b', html:`
<div class="glow" style="width:500px;height:500px;background:var(--red);top:-15%;left:10%"></div>
<p class="lbl a1" style="color:var(--red);margin-bottom:14px">How Machines Know They're Wrong</p>
<h2 class="med a2">Loss Functions</h2>
<p class="body a3" style="margin-top:12px;opacity:.7">A loss function measures how far the model's prediction is from reality. The model's entire goal is to <strong>minimize this number</strong>.</p>
<div class="math-block math-d a4">
Mean Squared Error (MSE):<br><br>
L = (1/n) × Σ(yᵢ - ŷᵢ)²<br><br>
<span style="font-size:.65em;opacity:.5">For each example: (actual - predicted)²</span><br>
<span style="font-size:.65em;opacity:.5">Average them all. That's your loss.</span>
</div>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--orange);margin-bottom:14px">Tanglish Analogy</p>
<h2 class="sect a2" style="font-size:clamp(28px,4vw,52px)"><span style="color:var(--orange)">"Malai Erangirathu Madiri"</span></h2>
<p class="body a3" style="margin-top:14px">Imagine you're blindfolded on top of a mountain. You can only feel the slope under your feet. To reach the bottom (lowest loss), you take small steps in the direction that goes downhill.</p>
<p class="body a4" style="margin-top:12px"><strong>That's gradient descent.</strong> The "slope" is the derivative. The "step" is the learning rate. The "bottom" is the optimal weights.</p>
<div class="tang tang-l a5">"Kanna mooditu malai-la nikunga. Kaal keezha epdi slope irukku nu feel pannunga. Antha direction-la nadangu. Apdi thaan gradient descent velai seiyudhu — lowest error-a keddi keddi pokum."</div>

<img src="assets/ml_mountain.png" class="person-img cool blend-screen" alt="Mountain" />
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--orange);margin-bottom:14px">The Core Algorithm</p>
<h2 class="med a2">Gradient Descent — Step by Step</h2>
<div class="math-block math-l a3" style="color:var(--orange)">
1. Start with random weights  w<br>
2. Predict:  ŷ = w · x + b<br>
3. Compute loss:  L = (y - ŷ)²<br>
4. Compute gradient:  ∂L/∂w<br>
5. Update:  w = w − α · (∂L/∂w)<br>
6. Repeat until loss is tiny
</div>
<p class="body a4" style="margin-top:14px"><strong>α (alpha)</strong> is the learning rate — how big each step is. Too big? You overshoot. Too small? You'll be walking forever.</p>
`},

{bg:'bg-b', html:`
<div class="glow" style="width:400px;height:400px;background:var(--yellow);bottom:-10%;right:5%"></div>
<p class="lbl a1" style="color:var(--yellow);margin-bottom:14px">The Goldilocks Problem</p>
<h2 class="med a2">Learning Rate</h2>
<div class="row a3">
<div class="card card-d" style="text-align:center">
<div style="font-size:36px">🐢</div>
<div class="ct" style="color:var(--teal)">α = 0.0001</div>
<div class="cb">Too small. Takes forever to converge. May get stuck in local minima.</div>
</div>
<div class="card card-d" style="text-align:center;border:1px solid rgba(52,199,89,.3)">
<div style="font-size:36px">✅</div>
<div class="ct" style="color:var(--green)">α = 0.01</div>
<div class="cb">Just right. Steady progress toward the minimum. Converges smoothly.</div>
</div>
<div class="card card-d" style="text-align:center">
<div style="font-size:36px">💥</div>
<div class="ct" style="color:var(--red)">α = 10</div>
<div class="cb">Too big. Overshoots the minimum. Loss explodes. Model diverges.</div>
</div>
</div>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--indigo);margin-bottom:14px">Beyond Straight Lines</p>
<h2 class="med a2">Logistic Regression & Classification</h2>
<p class="body a3" style="margin-top:12px">What if the output isn't a number, but a category? "Spam or not spam?" We squeeze the output through the <strong>sigmoid function</strong> to get a probability between 0 and 1.</p>
<div class="math-block math-l a4" style="color:var(--indigo)">
σ(z) = 1 / (1 + e⁻ᶻ)<br><br>
<span style="font-size:.65em;opacity:.5">z = w · x + b</span><br>
<span style="font-size:.65em;opacity:.5">If σ(z) > 0.5 → Class 1 (spam)</span><br>
<span style="font-size:.65em;opacity:.5">If σ(z) ≤ 0.5 → Class 0 (not spam)</span>
</div>
`},

// ──────── ACT 3: NEURAL NETWORKS ────────
{bg:'bg-b', html:`
<div class="glow" style="width:600px;height:600px;background:var(--green);top:-15%;left:-10%"></div>
<p class="pill a1" style="background:rgba(52,199,89,.12);color:var(--green)">Act 3</p>
<h2 class="hero a2" style="font-size:clamp(36px,5.5vw,76px)">Neural<br><span class="ggt">Networks.</span></h2>
<p class="sub a3" style="margin-top:16px;opacity:.5">What happens when you stack hundreds of tiny linear regressions together and add a twist? Magic.</p>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--green);margin-bottom:14px">The Single Neuron</p>
<h2 class="med a2">The Perceptron</h2>
<p class="body a3" style="margin-top:12px">A perceptron is a single neuron. It takes inputs, multiplies each by a weight, sums them, adds a bias, and passes through an activation function.</p>
<div class="math-block math-l a4" style="color:var(--green)">
output = activation(w₁x₁ + w₂x₂ + w₃x₃ + b)<br><br>
<span style="font-size:.65em;opacity:.5">Inputs × Weights → Sum → Activation → Output</span><br>
<span style="font-size:.65em;opacity:.5">It's just linear regression + a non-linear twist!</span>
</div>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--purple);margin-bottom:14px">The Non-Linear Twist</p>
<h2 class="med a2">Activation Functions</h2>
<p class="body a3" style="margin-top:12px">Without activation functions, stacking layers would just give you another straight line. Activations add the curves that let networks learn complex patterns.</p>
<div class="row a4">
<div class="card card-l" style="text-align:center">
<div class="ct" style="color:var(--blue)">ReLU</div>
<div class="mono" style="font-size:14px;margin-top:6px">f(x) = max(0, x)</div>
<div class="cb" style="margin-top:6px">Most popular. Simple. Fast. If negative, output 0. If positive, keep it.</div>
</div>
<div class="card card-l" style="text-align:center">
<div class="ct" style="color:var(--purple)">Sigmoid</div>
<div class="mono" style="font-size:14px;margin-top:6px">f(x) = 1/(1+e⁻ˣ)</div>
<div class="cb" style="margin-top:6px">Squashes to 0–1. Good for probabilities. Can saturate.</div>
</div>
<div class="card card-l" style="text-align:center">
<div class="ct" style="color:var(--green)">Softmax</div>
<div class="mono" style="font-size:14px;margin-top:6px">eˣⁱ / Σeˣʲ</div>
<div class="cb" style="margin-top:6px">For multi-class. Outputs a probability distribution over all classes.</div>
</div>
</div>
`},

{bg:'bg-b', html:`
<p class="lbl a1" style="color:var(--teal);margin-bottom:14px">Stacking Layers</p>
<h2 class="med a2">Deep Neural Network</h2>
<p class="body a3" style="margin-top:12px;opacity:.7">Connect neurons in layers. Each layer learns a different level of abstraction. Layer 1 learns edges, Layer 2 learns shapes, Layer 3 learns objects.</p>
<div class="nn a4">
<div class="nn-layer">
<div class="nn-node" style="border-color:var(--blue)"></div>
<div class="nn-node" style="border-color:var(--blue)"></div>
<div class="nn-node" style="border-color:var(--blue)"></div>
<div class="nn-node" style="border-color:var(--blue)"></div>
<div class="nn-label">Input<br>Layer</div>
</div>
<div style="font-size:20px;opacity:.3">→</div>
<div class="nn-layer">
<div class="nn-node" style="border-color:var(--purple);background:rgba(175,82,222,.2)"></div>
<div class="nn-node" style="border-color:var(--purple);background:rgba(175,82,222,.2)"></div>
<div class="nn-node" style="border-color:var(--purple);background:rgba(175,82,222,.2)"></div>
<div class="nn-node" style="border-color:var(--purple);background:rgba(175,82,222,.2)"></div>
<div class="nn-node" style="border-color:var(--purple);background:rgba(175,82,222,.2)"></div>
<div class="nn-label">Hidden<br>Layer 1</div>
</div>
<div style="font-size:20px;opacity:.3">→</div>
<div class="nn-layer">
<div class="nn-node" style="border-color:var(--green);background:rgba(52,199,89,.2)"></div>
<div class="nn-node" style="border-color:var(--green);background:rgba(52,199,89,.2)"></div>
<div class="nn-node" style="border-color:var(--green);background:rgba(52,199,89,.2)"></div>
<div class="nn-node" style="border-color:var(--green);background:rgba(52,199,89,.2)"></div>
<div class="nn-node" style="border-color:var(--green);background:rgba(52,199,89,.2)"></div>
<div class="nn-label">Hidden<br>Layer 2</div>
</div>
<div style="font-size:20px;opacity:.3">→</div>
<div class="nn-layer">
<div class="nn-node" style="border-color:var(--orange);background:rgba(255,149,0,.3)"></div>
<div class="nn-node" style="border-color:var(--orange);background:rgba(255,149,0,.3)"></div>
<div class="nn-label">Output<br>Layer</div>
</div>
</div>
<p class="a5" style="font-size:clamp(12px,1vw,14px);opacity:.3;margin-top:14px;text-align:center">"Deep" learning = many hidden layers. GPT-4 has ~120 layers.</p>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--orange);margin-bottom:14px">Forward Pass</p>
<h2 class="med a2">How a Network Makes a Prediction</h2>
<div class="math-block math-l a3" style="color:var(--orange);font-size:clamp(13px,1.5vw,20px)">
Layer 1:  h₁ = ReLU(W₁ · x + b₁)<br>
Layer 2:  h₂ = ReLU(W₂ · h₁ + b₂)<br>
Output:   ŷ = Softmax(W₃ · h₂ + b₃)
</div>
<p class="body a4" style="margin-top:14px">Data flows forward through each layer, getting transformed at each step. The output is the network's prediction.</p>
<p class="a5" style="font-size:clamp(12px,1.1vw,15px);opacity:.4;margin-top:10px">The weights (W) and biases (b) are what the network <em>learns</em>. Everything else is fixed architecture.</p>
`},

{bg:'bg-b', html:`
<div class="glow" style="width:500px;height:500px;background:var(--pink);bottom:-15%;right:-5%"></div>
<p class="lbl a1" style="color:var(--pink);margin-bottom:14px">The Learning Algorithm</p>
<h2 class="med a2">Backpropagation</h2>
<p class="body a3" style="margin-top:12px;opacity:.7">After a forward pass, the network compares its prediction to reality (loss). Then it works <strong>backwards</strong> through each layer, computing how much each weight contributed to the error.</p>
<div class="math-block math-d a4">
Chain Rule (Calculus):<br><br>
∂L/∂w₁ = ∂L/∂ŷ · ∂ŷ/∂h₂ · ∂h₂/∂h₁ · ∂h₁/∂w₁<br><br>
<span style="font-size:.6em;opacity:.5">Each layer passes its gradient backward to the layer before it.</span>
</div>
<p class="a5" style="font-size:clamp(12px,1.1vw,15px);opacity:.4;margin-top:10px">Forward: predict. Backward: learn. Repeat millions of times.</p>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--green);margin-bottom:14px">The Training Loop</p>
<h2 class="med a2">Epochs, Batches, Iterations</h2>
<div class="blist a3">
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div><strong>Epoch</strong> — one complete pass through the entire dataset</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div><strong>Batch</strong> — a subset of data processed together (e.g., 32 examples)</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--green)"></div><div><strong>Iteration</strong> — one batch forward + backward pass</div></div>
</div>
<div class="code-block code-d a4" style="background:rgba(0,0,0,.04);border:1px solid rgba(0,0,0,.06);color:#333">for epoch in range(100):
    for batch in data_loader:
        predictions = model(batch)
        loss = loss_fn(predictions, labels)
        loss.backward()        # backprop
        optimizer.step()       # update weights
        optimizer.zero_grad()  # reset</div>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--red);margin-bottom:14px">The Big Trap</p>
<h2 class="med a2">Overfitting vs. Underfitting</h2>
<div class="row a3">
<div class="card card-l" style="text-align:center">
<div style="font-size:36px">📐</div>
<div class="ct" style="color:var(--blue)">Underfitting</div>
<div class="cb">Model is too simple. Can't even learn the training data. Like memorizing only the chapter headings.</div>
</div>
<div class="card card-l" style="text-align:center;border:2px solid var(--green)">
<div style="font-size:36px">🎯</div>
<div class="ct" style="color:var(--green)">Good Fit</div>
<div class="cb">Model captures the true pattern. Generalizes well to new, unseen data.</div>
</div>
<div class="card card-l" style="text-align:center">
<div style="font-size:36px">🧠</div>
<div class="ct" style="color:var(--red)">Overfitting</div>
<div class="cb">Model memorizes training data including noise. Like memorizing answers but failing new questions.</div>
</div>
</div>
<p class="a4" style="font-size:clamp(12px,1.1vw,15px);opacity:.4;margin-top:14px">Solutions: more data, dropout, regularization, early stopping, data augmentation.</p>
`},

{bg:'bg-b', html:`
<p class="lbl a1" style="color:var(--cyan);margin-bottom:14px">Seeing the World</p>
<h2 class="med a2">CNNs — Convolutional Neural Networks</h2>
<p class="body a3" style="margin-top:12px;opacity:.7">CNNs are how machines <strong>see</strong>. Instead of looking at every pixel independently, they slide small filters across the image to detect patterns — edges, textures, objects.</p>
<div class="diagram a4" style="gap:14px">
<div class="dbox" style="background:rgba(0,199,190,.1);color:var(--mint);padding:14px">Image<br><span style="font-size:10px;opacity:.5">224×224×3</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(0,122,255,.1);color:var(--blue);padding:14px">Conv<br><span style="font-size:10px;opacity:.5">Edges</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(175,82,222,.1);color:var(--purple);padding:14px">Conv<br><span style="font-size:10px;opacity:.5">Shapes</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(52,199,89,.1);color:var(--green);padding:14px">Conv<br><span style="font-size:10px;opacity:.5">Objects</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(255,149,0,.1);color:var(--orange);padding:14px">Dense<br><span style="font-size:10px;opacity:.5">Classify</span></div>
</div>
<p class="a5" style="font-size:clamp(12px,1vw,14px);opacity:.3;margin-top:14px">Used in: medical imaging, self-driving cars, facial recognition, satellite analysis.</p>

<img src="assets/ml_lens.png" class="person-img cool blend-screen" alt="Lens" />
`},

// ──────── ACT 4: NLP ────────
{bg:'bg-b', html:`
<div class="glow" style="width:600px;height:600px;background:var(--orange);top:-15%;right:-10%"></div>
<p class="pill a1" style="background:rgba(255,149,0,.12);color:var(--orange)">Act 4</p>
<h2 class="hero a2" style="font-size:clamp(36px,5.5vw,76px)">Understanding<br><span class="goy">Language.</span></h2>
<p class="sub a3" style="margin-top:16px;opacity:.5">How do you teach a machine to read, write, translate, and converse? You turn words into numbers.</p>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--orange);margin-bottom:14px">Step 1</p>
<h2 class="med a2">Tokenization — Breaking Text Apart</h2>
<p class="body a3" style="margin-top:12px">Before any ML, text must be split into tokens — words, subwords, or characters. Each token gets a numeric ID.</p>
<div class="code-block a4" style="background:rgba(0,0,0,.03);border:1px solid rgba(0,0,0,.06);color:#333;white-space:pre-wrap">
"Machine learning is amazing"

Word-level:  ["Machine", "learning", "is", "amazing"]
             [  4821,      1293,    52,     7834    ]

Subword (BPE): ["Mach", "ine", "learn", "ing", "is", "amaz", "ing"]
               [ 892,    421,   673,    102,   52,   3421,   102 ]</div>
<p class="a5" style="font-size:clamp(12px,1.1vw,15px);opacity:.4;margin-top:10px">GPT uses Byte Pair Encoding (BPE) — ~50,000 subword tokens in its vocabulary.</p>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--purple);margin-bottom:14px">From Words to Vectors</p>
<h2 class="med a2">Bag of Words & TF-IDF</h2>
<p class="body a3" style="margin-top:12px">The simplest NLP: count how often each word appears. TF-IDF improves this by weighing rare, informative words higher than common ones like "the" or "is".</p>
<div class="math-block math-l a4" style="color:var(--purple);font-size:clamp(13px,1.4vw,19px)">
TF-IDF(word, doc) = TF × IDF<br><br>
TF = count(word) / total_words<br>
IDF = log(total_docs / docs_with_word)<br><br>
<span style="font-size:.6em;opacity:.5">"Transformer" in an ML paper → high TF-IDF (rare & relevant)</span><br>
<span style="font-size:.6em;opacity:.5">"The" in any paper → low TF-IDF (common everywhere)</span>
</div>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--blue);margin-bottom:14px">The Breakthrough</p>
<h2 class="med a2">Word Embeddings — Word2Vec</h2>
<p class="body a3" style="margin-top:12px">Instead of sparse counts, represent each word as a dense vector in continuous space. Words with similar meanings cluster together.</p>
<div class="math-block math-l a4" style="color:var(--blue);font-size:clamp(13px,1.4vw,19px)">
king - man + woman ≈ queen<br><br>
Paris - France + India ≈ Delhi<br><br>
<span style="font-size:.6em;opacity:.5">Each word → a vector of 300 numbers</span><br>
<span style="font-size:.6em;opacity:.5">Trained on billions of words from the web</span>
</div>
<div class="paper paper-l a5" style="margin-top:14px">
<div class="paper-title">📄 "Efficient Estimation of Word Representations in Vector Space"</div>
<div class="paper-meta">Mikolov et al., 2013 — Google</div>
<div class="paper-link">arxiv.org/abs/1301.3781</div>
</div>
`},

{bg:'bg-b', html:`
<p class="lbl a1" style="color:var(--teal);margin-bottom:14px">Tanglish Analogy</p>
<h2 class="sect a2" style="font-size:clamp(28px,4vw,52px)"><span class="ggt">"Google Maps Madiri"</span></h2>
<p class="body a3" style="margin-top:14px;opacity:.7">Think of word embeddings like Google Maps. Every word has coordinates. "King" and "Queen" are in the same neighborhood. "Car" and "Truck" are nearby. "Car" and "Democracy" are on different continents.</p>
<div class="tang tang-d a4">"Oru word-ku oru address irukku — 300-dimension address! 'King' um 'Queen' um pakkathu pakkathu-la irukku. 'Cat' um 'Dog' um same locality. 'Banana' vera oorula irukku. Google Maps madiri, words-ku location irukkum."</div>

<img src="assets/ml_map.png" class="person-img grn blend-screen" alt="Map" />
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--red);margin-bottom:14px">Sequential Processing</p>
<h2 class="med a2">RNNs — Recurrent Neural Networks</h2>
<p class="body a3" style="margin-top:12px">Language is sequential — word order matters. "Dog bites man" ≠ "Man bites dog." RNNs process one word at a time, passing a hidden state forward like a conveyor belt of context.</p>
<div class="diagram a4" style="gap:10px">
<div class="dbox" style="background:rgba(0,122,255,.1);color:var(--blue);padding:12px">I</div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(175,82,222,.1);color:var(--purple);padding:12px">love</div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(52,199,89,.1);color:var(--green);padding:12px">machine</div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(255,149,0,.1);color:var(--orange);padding:12px">learning</div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(255,45,85,.15);color:var(--pink);padding:12px">ŷ</div>
</div>
<p class="a5" style="font-size:clamp(12px,1.1vw,15px);opacity:.4;margin-top:12px">Problem: by the time it reaches word 100, it has forgotten word 1. The vanishing gradient problem.</p>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--indigo);margin-bottom:14px">Solving Long-Term Memory</p>
<h2 class="med a2">LSTMs & GRUs</h2>
<p class="body a3" style="margin-top:12px">LSTMs add "gates" — forget gate, input gate, output gate — that let the network decide what to remember and what to forget. GRUs are a simpler version with fewer gates.</p>
<div class="row a4">
<div class="card card-l">
<div class="ct" style="color:var(--indigo)">Forget Gate</div>
<div class="cb">"Should I forget the old context?"<br>σ(W_f · [h_{t-1}, x_t] + b_f)</div>
</div>
<div class="card card-l">
<div class="ct" style="color:var(--purple)">Input Gate</div>
<div class="cb">"What new info should I store?"<br>σ(W_i · [h_{t-1}, x_t] + b_i)</div>
</div>
<div class="card card-l">
<div class="ct" style="color:var(--green)">Output Gate</div>
<div class="cb">"What should I output now?"<br>σ(W_o · [h_{t-1}, x_t] + b_o)</div>
</div>
</div>
<div class="paper paper-l a5" style="margin-top:10px">
<div class="paper-title">📄 "Long Short-Term Memory"</div>
<div class="paper-meta">Hochreiter & Schmidhuber, 1997 — the paper that changed sequence modeling</div>
</div>
`},

// ──────── ACT 5: TRANSFORMERS ────────
{bg:'bg-b', html:`
<div class="glow" style="width:700px;height:700px;background:var(--pink);top:-20%;right:-15%"></div>
<div class="glow" style="width:400px;height:400px;background:var(--purple);bottom:-10%;left:5%"></div>
<p class="pill a1" style="background:rgba(255,45,85,.12);color:var(--pink)">Act 5</p>
<h2 class="hero a2" style="font-size:clamp(36px,5.5vw,76px)">Transformers<br><span class="gip">&amp; LLMs.</span></h2>
<p class="sub a3" style="margin-top:16px;opacity:.5">The architecture that replaced everything before it. This is where modern AI lives.</p>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--purple);margin-bottom:14px">The Paper That Changed Everything</p>
<h2 class="med a2">"Attention Is All You Need"</h2>
<p class="body a3" style="margin-top:12px">In 2017, 8 Google researchers threw away RNNs entirely and built an architecture based on one idea: <strong>attention</strong>. Instead of reading word-by-word, look at ALL words simultaneously.</p>
<div class="tang tang-l a4">"Google-oda intha oru paper thaan motha game-aiyum maathiduchu. Transformers don't read word by word; they look at the whole context. Athuthaan ithoda superpower."</div>
<div class="paper paper-l a5" style="margin-top:12px">
<div class="paper-title">📄 "Attention Is All You Need"</div>
<div class="paper-meta">Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin — 2017</div>
<div class="paper-link">arxiv.org/abs/1706.03762</div>
</div>

<img src="assets/ml_library.png" class="person-img cool blend-screen" alt="Library" />
`},

{bg:'bg-b', html:`
<div class="glow" style="width:500px;height:500px;background:var(--indigo);top:-10%;left:-5%"></div>
<p class="lbl a1" style="color:var(--teal);margin-bottom:14px">The Core Mechanism</p>
<h2 class="med a2">Self-Attention — How It Works</h2>
<p class="body a3" style="margin-top:12px;opacity:.7">For each word, the model asks: "How relevant is every other word to understanding THIS word?"</p>
<div class="math-block math-d a4" style="font-size:clamp(13px,1.5vw,20px)">
Attention(Q, K, V) = softmax(Q·Kᵀ / √dₖ) · V<br><br>
<span style="font-size:.6em;opacity:.5">Q = Query ("what am I looking for?")</span><br>
<span style="font-size:.6em;opacity:.5">K = Key ("what do I contain?")</span><br>
<span style="font-size:.6em;opacity:.5">V = Value ("what information do I carry?")</span><br>
<span style="font-size:.6em;opacity:.5">√dₖ = scaling factor (prevents exploding gradients)</span>
</div>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--orange);margin-bottom:14px">Self-Attention Example</p>
<h2 class="med a2">Why Context Matters</h2>
<p class="body a3" style="margin-top:12px">In "The <strong>bank</strong> of the <strong>river</strong> was muddy" — the word "bank" attends strongly to "river" (not "money"). That's how the model knows which meaning of "bank" to use.</p>
<div class="row a4">
<div class="card card-l" style="flex:2">
<div class="ct" style="color:var(--orange)">Attention Scores for "bank"</div>
<div style="margin-top:10px;display:flex;gap:6px;flex-wrap:wrap">
<span style="padding:6px 12px;border-radius:8px;font-size:13px;font-weight:600;background:rgba(255,149,0,.05)">The <span style="opacity:.3">0.02</span></span>
<span style="padding:6px 12px;border-radius:8px;font-size:13px;font-weight:700;background:rgba(255,149,0,.4);color:var(--orange)">bank <span>0.31</span></span>
<span style="padding:6px 12px;border-radius:8px;font-size:13px;font-weight:600;background:rgba(255,149,0,.05)">of <span style="opacity:.3">0.03</span></span>
<span style="padding:6px 12px;border-radius:8px;font-size:13px;font-weight:600;background:rgba(255,149,0,.05)">the <span style="opacity:.3">0.02</span></span>
<span style="padding:6px 12px;border-radius:8px;font-size:13px;font-weight:700;background:rgba(52,199,89,.3);color:var(--green)">river <span>0.45</span></span>
<span style="padding:6px 12px;border-radius:8px;font-size:13px;font-weight:600;background:rgba(255,149,0,.1)">was <span style="opacity:.4">0.09</span></span>
<span style="padding:6px 12px;border-radius:8px;font-size:13px;font-weight:600;background:rgba(255,149,0,.1)">muddy <span style="opacity:.4">0.08</span></span>
</div>
</div>
</div>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--indigo);margin-bottom:14px">Multiple Perspectives</p>
<h2 class="med a2">Multi-Head Attention</h2>
<p class="body a3" style="margin-top:12px">Instead of one attention pattern, Transformers run <strong>multiple attention heads in parallel</strong>. Each head can focus on a different relationship: one looks at grammar, another at meaning, another at position.</p>
<div class="math-block math-l a4" style="color:var(--indigo);font-size:clamp(13px,1.4vw,19px)">
MultiHead(Q, K, V) = Concat(head₁, head₂, ..., headₕ) · Wₒ<br><br>
<span style="font-size:.6em;opacity:.5">GPT-3 uses 96 attention heads per layer</span><br>
<span style="font-size:.6em;opacity:.5">Each head = 128 dimensions (96 × 128 = 12,288 total)</span>
</div>
`},

{bg:'bg-b', html:`
<p class="lbl a1" style="color:var(--green);margin-bottom:14px">Position Awareness</p>
<h2 class="med a2">Positional Encoding</h2>
<p class="body a3" style="margin-top:12px;opacity:.7">Since Transformers process all words at once (unlike RNNs), they need a way to know word order. Positional encoding adds a unique "position signal" to each token.</p>
<div class="math-block math-d a4" style="font-size:clamp(12px,1.3vw,18px)">
PE(pos, 2i)   = sin(pos / 10000^(2i/d))<br>
PE(pos, 2i+1) = cos(pos / 10000^(2i/d))<br><br>
<span style="font-size:.6em;opacity:.5">Each position gets a unique combination of sine/cosine waves.</span><br>
<span style="font-size:.6em;opacity:.5">The model learns to use these signals to understand order.</span>
</div>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--purple);margin-bottom:14px">The Full Picture</p>
<h2 class="med a2">Transformer Architecture</h2>
<div class="col2 a3">
<div>
<div class="smtitle" style="color:var(--blue)">Encoder Stack</div>
<div class="blist" style="margin-top:8px">
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div>Self-Attention</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div>Add & Normalize</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div>Feed-Forward Network</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div>Add & Normalize</div></div>
</div>
<p style="font-size:12px;opacity:.4;margin-top:8px">× N layers (BERT uses 12)</p>
</div>
<div>
<div class="smtitle" style="color:var(--purple)">Decoder Stack</div>
<div class="blist" style="margin-top:8px">
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div>Masked Self-Attention</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div>Cross-Attention (to encoder)</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div>Feed-Forward Network</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div>Add & Normalize × N</div></div>
</div>
<p style="font-size:12px;opacity:.4;margin-top:8px">× N layers (GPT-3 uses 96)</p>
</div>
</div>

<img src="assets/ml_architecture.png" class="person-img cool blend-screen" alt="Architecture" />
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--pink);margin-bottom:14px">Two Schools</p>
<h2 class="med a2">BERT vs GPT</h2>
<div class="row a3">
<div class="card card-l" style="border-top:3px solid var(--blue)">
<div class="ct" style="color:var(--blue)">BERT (Encoder-only)</div>
<div class="cb">Reads text <strong>bidirectionally</strong>. Sees the full sentence. Built for understanding: classification, NER, Q&A.</div>
<div style="margin-top:8px;font-size:11px;opacity:.4">Google, 2018 · 340M params</div>
</div>
<div class="card card-l" style="border-top:3px solid var(--green)">
<div class="ct" style="color:var(--green)">GPT (Decoder-only)</div>
<div class="cb">Reads text <strong>left-to-right</strong>. Predicts the next token. Built for generation: writing, chat, code.</div>
<div style="margin-top:8px;font-size:11px;opacity:.4">OpenAI, 2018→2024 · 1.7T params</div>
</div>
</div>
<div class="paper paper-l a4" style="margin-top:12px">
<div class="paper-title">📄 BERT: "Pre-training of Deep Bidirectional Transformers"</div>
<div class="paper-meta">Devlin et al., 2018 — arxiv.org/abs/1810.04805</div>
</div>
<div class="paper paper-l a5">
<div class="paper-title">📄 GPT-1: "Improving Language Understanding by Generative Pre-Training"</div>
<div class="paper-meta">Radford et al., 2018 — OpenAI</div>
</div>
`},

{bg:'bg-b', html:`
<div class="glow" style="width:500px;height:500px;background:var(--orange);bottom:-15%;left:-5%"></div>
<p class="lbl a1" style="color:var(--orange);margin-bottom:14px">How LLMs Learn</p>
<h2 class="med a2">Pre-Training: Next Token Prediction</h2>
<p class="body a3" style="margin-top:12px;opacity:.7">GPT's entire training objective is stunningly simple: given all previous words, predict the <strong>next word</strong>. Do this on trillions of tokens from the internet.</p>
<div class="code-block code-d a4">
Input:  "The capital of France is"
Target: "Paris"

Input:  "Machine learning is a subset of"
Target: "artificial"

<span style="color:var(--green)">// The model adjusts its 175 billion
// weights to get better at this task.
// That's it. That's the whole trick.</span></div>

<img src="assets/ml_tokens.png" class="person-img gold blend-screen" alt="Tokens" />
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--pink);margin-bottom:14px">Making It Useful</p>
<h2 class="med a2">Fine-Tuning & RLHF</h2>
<p class="body a3" style="margin-top:12px">Pre-training gives the model knowledge. Fine-tuning and RLHF (Reinforcement Learning from Human Feedback) teach it to be <strong>helpful, honest, and harmless</strong>.</p>
<div class="diagram a4" style="gap:12px">
<div class="dbox" style="background:rgba(0,122,255,.1);color:var(--blue);padding:14px">Pre-train<br><span style="font-size:10px;opacity:.5">Trillions of tokens</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(175,82,222,.1);color:var(--purple);padding:14px">SFT<br><span style="font-size:10px;opacity:.5">Supervised Fine-Tuning</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(255,45,85,.1);color:var(--pink);padding:14px">RLHF<br><span style="font-size:10px;opacity:.5">Human preference</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(52,199,89,.15);color:var(--green);padding:14px">ChatGPT<br><span style="font-size:10px;opacity:.5">Useful assistant</span></div>
</div>
<div class="paper paper-l a5" style="margin-top:14px">
<div class="paper-title">📄 "Training language models to follow instructions with human feedback"</div>
<div class="paper-meta">Ouyang et al., 2022 — OpenAI · arxiv.org/abs/2203.02155</div>
</div>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--green);margin-bottom:14px">Subword Magic</p>
<h2 class="med a2">BPE — Byte Pair Encoding</h2>
<p class="body a3" style="margin-top:12px">LLMs don't see words — they see <strong>tokens</strong>. BPE splits text into frequent subword units. "unhappiness" → ["un", "happiness"]. This handles any word, even new ones the model has never seen.</p>
<div class="code-block a4" style="background:rgba(0,0,0,.03);border:1px solid rgba(0,0,0,.06);color:#333;white-space:pre-wrap">
"Transformer" → ["Trans", "former"]         2 tokens
"ChatGPT"     → ["Chat", "G", "PT"]         3 tokens
"நன்றி"        → ["ந", "ன்", "றி"]           3 tokens
"Tokenization" → ["Token", "ization"]       2 tokens

GPT-4 vocabulary: ~100,000 tokens
1 token ≈ ¾ of a word in English</div>
`},

{bg:'bg-b', html:`
<p class="lbl a1" style="color:var(--cyan);margin-bottom:14px">The Scaling Hypothesis</p>
<h2 class="med a2">Scaling Laws</h2>
<p class="body a3" style="margin-top:12px;opacity:.7">A surprising discovery: model performance follows <strong>predictable power laws</strong>. More data + more parameters + more compute = reliably better performance.</p>
<div class="stat-row a4">
<div class="stat-item"><div class="bignum gbp" style="font-size:clamp(32px,4vw,56px)">175B</div><div class="statlbl">GPT-3 params</div></div>
<div class="stat-item"><div class="bignum gpo" style="font-size:clamp(32px,4vw,56px)">1.7T</div><div class="statlbl">GPT-4 params (est.)</div></div>
<div class="stat-item"><div class="bignum ggt" style="font-size:clamp(32px,4vw,56px)">13T</div><div class="statlbl">Training tokens</div></div>
</div>
<div class="paper paper-d a5" style="margin-top:16px">
<div class="paper-title">📄 "Scaling Laws for Neural Language Models"</div>
<div class="paper-meta">Kaplan et al., 2020 — OpenAI · arxiv.org/abs/2001.08361</div>
</div>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--blue);margin-bottom:14px">Context & Memory</p>
<h2 class="med a2">Context Windows</h2>
<p class="body a3" style="margin-top:12px">An LLM can only "see" a fixed number of tokens at once — its context window. Everything outside that window is invisible.</p>
<div class="row a4">
<div class="card card-l" style="text-align:center">
<div class="ct" style="color:var(--blue)">GPT-3</div>
<div class="bignum" style="font-size:32px;color:var(--blue)">4K</div>
<div class="cb">~3,000 words</div>
</div>
<div class="card card-l" style="text-align:center">
<div class="ct" style="color:var(--purple)">GPT-4</div>
<div class="bignum" style="font-size:32px;color:var(--purple)">128K</div>
<div class="cb">~96,000 words</div>
</div>
<div class="card card-l" style="text-align:center">
<div class="ct" style="color:var(--green)">Claude</div>
<div class="bignum" style="font-size:32px;color:var(--green)">200K</div>
<div class="cb">~150,000 words</div>
</div>
<div class="card card-l" style="text-align:center">
<div class="ct" style="color:var(--orange)">Gemini 1.5</div>
<div class="bignum" style="font-size:32px;color:var(--orange)">1M</div>
<div class="cb">~750,000 words</div>
</div>
</div>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--green);margin-bottom:14px">Giving LLMs Real-Time Knowledge</p>
<h2 class="med a2">RAG — Retrieval-Augmented Generation</h2>
<p class="body a3" style="margin-top:12px">LLMs have a knowledge cutoff. RAG fixes this by <strong>retrieving relevant documents first</strong>, then feeding them to the LLM as context before it generates an answer.</p>
<div class="diagram a4" style="gap:12px">
<div class="dbox" style="background:rgba(0,122,255,.1);color:var(--blue);padding:14px">User Query</div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(175,82,222,.1);color:var(--purple);padding:14px">Embed<br><span style="font-size:10px;opacity:.5">Vector search</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(52,199,89,.1);color:var(--green);padding:14px">Retrieve<br><span style="font-size:10px;opacity:.5">Top-K docs</span></div>
<div class="darr">→</div>
<div class="dbox" style="background:rgba(255,149,0,.1);color:var(--orange);padding:14px">LLM + Context<br><span style="font-size:10px;opacity:.5">Generate answer</span></div>
</div>
<p class="a5" style="font-size:clamp(12px,1.1vw,15px);opacity:.4;margin-top:14px">RAG is the #1 most in-demand AI engineering skill in 2026. Every company with documents needs it.</p>
`},

{bg:'bg-b', html:`
<p class="lbl a1" style="color:var(--yellow);margin-bottom:14px">The Frontier</p>
<h2 class="med a2">AI Agents & Tool Use</h2>
<p class="body a3" style="margin-top:12px;opacity:.7">The next evolution: LLMs that don't just answer questions — they <strong>take actions</strong>. Browse the web, write code, call APIs, book flights, manage databases.</p>
<div class="row a4">
<div class="card card-d">
<div class="ci">🔗</div>
<div class="ct" style="color:var(--yellow)">Tool Use</div>
<div class="cb">LLM decides which tool to call (calculator, search, code interpreter) based on the task.</div>
</div>
<div class="card card-d">
<div class="ci">🔄</div>
<div class="ct" style="color:var(--orange)">Planning</div>
<div class="cb">LLM breaks complex tasks into steps, executes them in order, handles failures.</div>
</div>
<div class="card card-d">
<div class="ci">🧠</div>
<div class="ct" style="color:var(--green)">Memory</div>
<div class="cb">Agents maintain context across sessions. They remember past interactions.</div>
</div>
</div>
<p class="a5" style="font-size:clamp(11px,1vw,13px);opacity:.3;margin-top:10px">The agentic AI market: projected $7.6B → $236B by 2034.</p>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--indigo);margin-bottom:14px">Working With LLMs</p>
<h2 class="med a2">Prompt Engineering</h2>
<p class="body a3" style="margin-top:12px">How you <em>ask</em> matters as much as what the model knows. Prompt engineering is the art of crafting inputs that get optimal outputs.</p>
<div class="row a4">
<div class="card card-l" style="border-top:3px solid var(--red)">
<div class="ct" style="color:var(--red)">Bad Prompt</div>
<div class="code-block" style="background:rgba(255,59,48,.05);color:#333;padding:12px;font-size:12px;margin-top:6px;white-space:pre-wrap">"Summarize this."</div>
</div>
<div class="card card-l" style="border-top:3px solid var(--green)">
<div class="ct" style="color:var(--green)">Good Prompt</div>
<div class="code-block" style="background:rgba(52,199,89,.05);color:#333;padding:12px;font-size:12px;margin-top:6px;white-space:pre-wrap">"You are a senior analyst. Summarize
this quarterly report in 5 bullet
points, focusing on revenue growth
and risks. Use data from the tables.
Format as: [Metric]: [Finding]"</div>
</div>
</div>
`},

// ──────── ACT 6: JOB MARKET ────────
{bg:'bg-b', html:`
<div class="glow" style="width:700px;height:700px;background:var(--red);top:-15%;right:-10%"></div>
<div class="glow" style="width:400px;height:400px;background:var(--orange);bottom:-10%;left:5%"></div>
<p class="pill a1" style="background:rgba(255,59,48,.12);color:var(--red)">Act 6</p>
<h2 class="hero a2" style="font-size:clamp(36px,5.5vw,76px)">Your Career<br><span class="grc">Starts Here.</span></h2>
<p class="sub a3" style="margin-top:16px;opacity:.5">The market data is clear. AI isn't coming — it's already here. And it's hiring.</p>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--blue);margin-bottom:14px">The Numbers Don't Lie</p>
<h2 class="med a2">AI Job Market — Global</h2>
<div class="stat-row a3">
<div class="stat-item"><div class="bignum gbp" style="font-size:clamp(36px,5vw,64px)">74%</div><div class="statlbl">YoY AI/ML talent demand growth</div></div>
<div class="stat-item"><div class="bignum gpo" style="font-size:clamp(36px,5vw,64px)">143%</div><div class="statlbl">AI Engineer job posting growth</div></div>
<div class="stat-item"><div class="bignum ggt" style="font-size:clamp(36px,5vw,64px)">$301B</div><div class="statlbl">Global AI spending 2026</div></div>
</div>
<p class="body a4" style="margin-top:20px;font-size:clamp(13px,1.2vw,16px)">LinkedIn ranked <strong>AI Engineer</strong> as the #1 fastest-growing job title. Four of the top five fastest-growing positions are AI-related.</p>
<p class="a5" style="font-size:11px;opacity:.3;margin-top:8px">Sources: LinkedIn 2026 Jobs on the Rise, Mordor Intelligence, McKinsey</p>
`},

{bg:'bg-b', html:`
<div class="glow" style="width:500px;height:500px;background:var(--green);bottom:-15%;right:-5%"></div>
<p class="lbl a1" style="color:var(--green);margin-bottom:14px">India-Specific</p>
<h2 class="med a2"><span class="ggt">India's AI Boom</span></h2>
<div class="stat-row a3">
<div class="stat-item"><div class="bignum" style="font-size:clamp(32px,4.5vw,56px);color:var(--green)">59.5%</div><div class="statlbl">YoY AI hiring growth in India</div></div>
<div class="stat-item"><div class="bignum" style="font-size:clamp(32px,4.5vw,56px);color:var(--teal)">3.8L</div><div class="statlbl">AI roles projected in 2026</div></div>
<div class="stat-item"><div class="bignum" style="font-size:clamp(32px,4.5vw,56px);color:var(--mint)">33%</div><div class="statlbl">India leads global AI hiring rate</div></div>
</div>
<p class="body a4" style="margin-top:16px;opacity:.6;font-size:clamp(13px,1.2vw,16px)">India's AI market: $22.8B in 2025 → projected $131B by 2032. Growth rate: 42.2% CAGR. Generative AI and LLM skills demand jumped 60% year-on-year.</p>
<p class="a5" style="font-size:11px;opacity:.3;margin-top:8px">Sources: LinkedIn AI Labor Market Report 2026, Stanford AI Index, foundit Report</p>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--pink);margin-bottom:14px">What Companies Pay</p>
<h2 class="med a2">AI Salaries in India — 2026</h2>
<div class="row a3">
<div class="card card-l" style="text-align:center">
<div class="ct" style="color:var(--blue)">AI/ML Engineer</div>
<div style="font-size:clamp(22px,2.5vw,32px);font-weight:800;color:var(--blue);margin:6px 0">₹20-22L</div>
<div class="cb">Average · Up to ₹60L senior</div>
</div>
<div class="card card-l" style="text-align:center">
<div class="ct" style="color:var(--pink)">GenAI/LLM Engineer</div>
<div style="font-size:clamp(22px,2.5vw,32px);font-weight:800;color:var(--pink);margin:6px 0">₹12-74L</div>
<div class="cb">Hottest role · Freshers ₹12-20L</div>
</div>
<div class="card card-l" style="text-align:center">
<div class="ct" style="color:var(--green)">Data Scientist</div>
<div style="font-size:clamp(22px,2.5vw,32px);font-weight:800;color:var(--green);margin:6px 0">₹15-25L</div>
<div class="cb">Average · Lead roles ₹35L+</div>
</div>
</div>
<p class="a4" style="font-size:clamp(12px,1.1vw,15px);opacity:.4;margin-top:12px">AI professionals see 15-25% annual salary growth vs 8-10% in traditional IT. First job switch: 40-70% jump.</p>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--orange);margin-bottom:14px">The Workforce Shift</p>
<h2 class="med a2">Skills Changing at 2× Speed</h2>
<p class="body a3" style="margin-top:12px">According to the World Economic Forum, 39% of current skill sets will become outdated between 2025–2030. Workers with AI skills now earn a <strong>56% wage premium</strong>.</p>
<div class="blist a4">
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div><strong>77%</strong> of employers plan to reskill workforce for AI</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div><strong>78%</strong> of tech roles now include AI skills requirements</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--green)"></div><div><strong>72%</strong> of organizations have adopted AI in at least one function</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--orange)"></div><div><strong>170%</strong> increase in generative AI job postings (2024→2025)</div></div>
</div>
<p class="a5" style="font-size:11px;opacity:.3;margin-top:10px">Sources: WEF Future of Jobs 2025, PwC AI Jobs Barometer, McKinsey, Indeed Hiring Lab</p>
`},

{bg:'bg-b', html:`
<p class="lbl a1" style="color:var(--teal);margin-bottom:14px">Tanglish Reality Check</p>
<h2 class="sect a2" style="font-size:clamp(26px,3.5vw,48px)"><span class="ggt">"AI Unga Job-a Edukkathu"</span></h2>
<p class="body a3" style="margin-top:14px;opacity:.7">AI won't take your job. But someone who knows AI will take your job. The question isn't whether AI will affect your career — it's whether you'll be the one wielding it or being replaced by it.</p>
<div class="tang tang-d a4">"Oru common bayam irukku: AI namma job-a eduthuruma nu. AI unga job-a edukkathu. Aana, AI use panna theriyaatha oruthan, AI use panna therinja oruthan kitta job-a ilappaan. Ippo learn pannittal, neenga-thaan antha 'therinja oruthan.'"</div>

<img src="assets/ml_job.png" class="person-img grn blend-screen" alt="Job" />
`},

// ──────── CAREER PATHWAY ────────
{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--indigo);margin-bottom:14px">Your Roadmap</p>
<h2 class="med a2">The AI Engineer Career Pathway</h2>
<div class="tl a3">
<div class="tli"><div class="tldot" style="background:var(--blue)"></div><div><div class="tlc" style="color:var(--blue)">Phase 1: Foundations (Months 1-3)</div><div class="tls">Python, NumPy, Pandas, Statistics, Linear Algebra, Probability</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--purple)"></div><div><div class="tlc" style="color:var(--purple)">Phase 2: Core ML (Months 3-6)</div><div class="tls">Scikit-learn, Regression, Classification, Trees, Evaluation metrics</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--green)"></div><div><div class="tlc" style="color:var(--green)">Phase 3: Deep Learning (Months 6-9)</div><div class="tls">PyTorch, CNNs, RNNs, Training loops, GPU computing</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--orange)"></div><div><div class="tlc" style="color:var(--orange)">Phase 4: NLP & LLMs (Months 9-12)</div><div class="tls">Transformers, Hugging Face, Fine-tuning, RAG, Prompt Engineering</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--pink)"></div><div><div class="tlc" style="color:var(--pink)">Phase 5: Production (Months 12-15)</div><div class="tls">FastAPI, Docker, MLOps, CI/CD, AWS/GCP, monitoring</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--red)"></div><div><div class="tlc" style="color:var(--red)">Phase 6: Specialization (15+ months)</div><div class="tls">AI Agents, Computer Vision, Multi-modal, Research</div></div></div>
</div>

<img src="assets/ml_pathway.png" class="person-img cool blend-screen" alt="Pathway" />
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--blue);margin-bottom:14px">Phase 1 Deep Dive</p>
<h2 class="med a2">Build Your Foundation</h2>
<div class="col2 a3">
<div>
<div class="smtitle" style="color:var(--blue)">Math You Need</div>
<div class="blist">
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div>Linear Algebra — vectors, matrices, dot products</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div>Calculus — derivatives, chain rule, gradients</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div>Probability — Bayes theorem, distributions</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div>Statistics — mean, variance, hypothesis testing</div></div>
</div>
</div>
<div>
<div class="smtitle" style="color:var(--purple)">Python Stack</div>
<div class="blist">
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div>NumPy — numerical computation</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div>Pandas — data manipulation</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div>Matplotlib — visualization</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div>Jupyter Notebooks — experimentation</div></div>
</div>
</div>
</div>
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--purple);margin-bottom:14px">Phase 2-3 Deep Dive</p>
<h2 class="med a2">Core ML → Deep Learning</h2>
<div class="col2 a3">
<div>
<div class="smtitle" style="color:var(--purple)">Classical ML</div>
<div class="blist">
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div>Linear & Logistic Regression</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div>Decision Trees & Random Forests</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div>SVMs, K-Means, PCA</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--purple)"></div><div>Cross-validation, F1, AUC-ROC</div></div>
</div>
</div>
<div>
<div class="smtitle" style="color:var(--green)">Deep Learning</div>
<div class="blist">
<div class="blist-item"><div class="bdot" style="background:var(--green)"></div><div>PyTorch from scratch</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--green)"></div><div>Build CNNs, train on CIFAR-10</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--green)"></div><div>Transfer learning (ResNet, VGG)</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--green)"></div><div>GPU training, mixed precision</div></div>
</div>
</div>
</div>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--orange);margin-bottom:14px">Phase 4-5 Deep Dive</p>
<h2 class="med a2">LLMs → Production</h2>
<div class="col2 a3">
<div>
<div class="smtitle" style="color:var(--orange)">NLP & LLMs</div>
<div class="blist">
<div class="blist-item"><div class="bdot" style="background:var(--orange)"></div><div>Hugging Face Transformers library</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--orange)"></div><div>Fine-tune BERT/GPT-2 on custom data</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--orange)"></div><div>Build RAG with LangChain + vector DB</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--orange)"></div><div>Prompt engineering & evaluation</div></div>
</div>
</div>
<div>
<div class="smtitle" style="color:var(--pink)">Production</div>
<div class="blist">
<div class="blist-item"><div class="bdot" style="background:var(--pink)"></div><div>FastAPI for model serving</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--pink)"></div><div>Docker & Kubernetes</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--pink)"></div><div>AWS SageMaker / GCP Vertex AI</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--pink)"></div><div>Model monitoring & A/B testing</div></div>
</div>
</div>
</div>
`},

// ──────── PAPERS & RESOURCES ────────
{bg:'bg-b', html:`
<div class="glow" style="width:500px;height:500px;background:var(--blue);top:-10%;left:-5%"></div>
<p class="lbl a1" style="color:var(--blue);margin-bottom:14px">Required Reading</p>
<h2 class="med a2">The 10 Most Important Papers</h2>
<div style="display:flex;flex-direction:column;gap:8px;margin-top:14px;max-height:65vh;overflow-y:auto" class="a3">
<div class="paper paper-d"><div class="paper-title">1. Attention Is All You Need</div><div class="paper-meta">Vaswani et al., 2017 · arxiv.org/abs/1706.03762</div></div>
<div class="paper paper-d"><div class="paper-title">2. BERT: Pre-training of Deep Bidirectional Transformers</div><div class="paper-meta">Devlin et al., 2018 · arxiv.org/abs/1810.04805</div></div>
<div class="paper paper-d"><div class="paper-title">3. Language Models are Few-Shot Learners (GPT-3)</div><div class="paper-meta">Brown et al., 2020 · arxiv.org/abs/2005.14165</div></div>
<div class="paper paper-d"><div class="paper-title">4. Deep Residual Learning (ResNet)</div><div class="paper-meta">He et al., 2015 · arxiv.org/abs/1512.03385</div></div>
<div class="paper paper-d"><div class="paper-title">5. Word2Vec: Efficient Estimation of Word Representations</div><div class="paper-meta">Mikolov et al., 2013 · arxiv.org/abs/1301.3781</div></div>
<div class="paper paper-d"><div class="paper-title">6. ImageNet Classification with Deep CNNs (AlexNet)</div><div class="paper-meta">Krizhevsky et al., 2012 · The 2012 moment</div></div>
<div class="paper paper-d"><div class="paper-title">7. Generative Adversarial Networks (GANs)</div><div class="paper-meta">Goodfellow et al., 2014 · arxiv.org/abs/1406.2661</div></div>
<div class="paper paper-d"><div class="paper-title">8. Training LMs to Follow Instructions (InstructGPT)</div><div class="paper-meta">Ouyang et al., 2022 · arxiv.org/abs/2203.02155</div></div>
<div class="paper paper-d"><div class="paper-title">9. Scaling Laws for Neural Language Models</div><div class="paper-meta">Kaplan et al., 2020 · arxiv.org/abs/2001.08361</div></div>
<div class="paper paper-d"><div class="paper-title">10. Retrieval-Augmented Generation (RAG)</div><div class="paper-meta">Lewis et al., 2020 · arxiv.org/abs/2005.11401</div></div>
</div>

<img src="assets/ml_library.png" class="person-img cool blend-screen" alt="Library" />
`},

{bg:'bg-g', html:`
<p class="lbl a1" style="color:var(--green);margin-bottom:14px">Free Resources</p>
<h2 class="med a2">Best Courses & Blogs</h2>
<div class="col2 a3">
<div>
<div class="smtitle" style="color:var(--green)">Courses (Free)</div>
<div class="blist">
<div class="blist-item"><div class="bdot" style="background:var(--green)"></div><div><strong>CS50 AI</strong> — Harvard (edx.org)</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--green)"></div><div><strong>fast.ai</strong> — Practical Deep Learning</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--green)"></div><div><strong>CS231n</strong> — Stanford CNNs</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--green)"></div><div><strong>CS224n</strong> — Stanford NLP</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--green)"></div><div><strong>Andrew Ng</strong> — ML Specialization</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--green)"></div><div><strong>Karpathy</strong> — Neural Nets: Zero to Hero</div></div>
</div>
</div>
<div>
<div class="smtitle" style="color:var(--blue)">Blogs & Newsletters</div>
<div class="blist">
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div><strong>Lil'Log</strong> — lilianweng.github.io</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div><strong>Jay Alammar</strong> — jalammar.github.io</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div><strong>Distill.pub</strong> — Visual ML research</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div><strong>The Batch</strong> — Andrew Ng's newsletter</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div><strong>Hugging Face Blog</strong> — huggingface.co</div></div>
<div class="blist-item"><div class="bdot" style="background:var(--blue)"></div><div><strong>Chip Huyen</strong> — ML systems design</div></div>
</div>
</div>
</div>
`},

{bg:'bg-w', html:`
<p class="lbl a1" style="color:var(--purple);margin-bottom:14px">Build in Public</p>
<h2 class="med a2">5 Portfolio Projects That Get You Hired</h2>
<div class="tl a3">
<div class="tli"><div class="tldot" style="background:var(--blue)"></div><div><div class="tlc">1. End-to-End ML Pipeline</div><div class="tls">Data cleaning → training → evaluation → FastAPI deployment → Docker</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--purple)"></div><div><div class="tlc">2. RAG Chatbot on Custom Documents</div><div class="tls">LangChain + ChromaDB/Pinecone + OpenAI/Claude API + Streamlit UI</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--green)"></div><div><div class="tlc">3. Fine-Tuned Domain Model</div><div class="tls">Take a base model, fine-tune on domain data (medical, legal, Tamil), evaluate</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--orange)"></div><div><div class="tlc">4. Computer Vision Application</div><div class="tls">Object detection / image classification with real-world data, deployed as API</div></div></div>
<div class="tli"><div class="tldot" style="background:var(--pink)"></div><div><div class="tlc">5. AI Agent with Tool Use</div><div class="tls">Build an agent that searches the web, reads PDFs, and generates reports</div></div></div>
</div>
<p class="a4" style="font-size:clamp(12px,1.1vw,15px);opacity:.4;margin-top:12px">Put everything on GitHub with clean READMEs. Write a blog post for each project.</p>
`},

{bg:'bg-b', html:`
<p class="lbl a1" style="color:var(--orange);margin-bottom:14px">Key Takeaway</p>
<h2 class="sect a2" style="font-size:clamp(26px,3.5vw,48px)"><span class="goy">"Filter Coffee Madiri"</span></h2>
<p class="body a3" style="margin-top:14px;opacity:.7">Learning ML is like making perfect filter coffee. You can't rush it. The decoction needs time. Each layer of knowledge sits on top of the previous one. Skip the math? Your deep learning will taste watered down. Skip the fundamentals? Your LLM work will have no depth.</p>
<div class="tang tang-d a4">"Filter coffee madiri — decoction thani-ya, paal thani-ya, sugar thani-ya pottu mix pannum bodhu thaan taste varum. Math, code, theory, projects — ellathayum seri-ya layer layer-a kaththukkanum. Shortcut pottaa weak coffee thaan kidaikkum."</div>

<img src="assets/ml_coffee.png" class="person-img gold blend-screen" alt="Coffee" />
`},

// ──────── RISELABS PITCH ────────
{bg:'bg-b', html:`
<div class="glow" style="width:700px;height:700px;background:var(--orange);top:-20%;left:-10%"></div>
<div class="glow" style="width:500px;height:500px;background:var(--yellow);bottom:-20%;right:0"></div>
<p class="pill a1" style="background:rgba(255,149,0,.15);color:var(--orange)">The Bridge</p>
<h2 class="sect a2" style="font-size:clamp(30px,4.5vw,60px)">Everything we covered today?<br><span class="goy">We teach all of it.</span></h2>
<p class="body a3" style="margin-top:14px;opacity:.6">RiseLabs AI Engineering Bootcamp — real datasets, actual deployment, 3 portfolio projects, direct industry mentorship. 18 weeks of building, not just watching.</p>
<div class="tang tang-d a4">"3rd year is the perfect time to build your portfolio. Final year-la poi project theda koodathu. You need to build things that matter. Ippo start pannunga."</div>

<img src="assets/ml_bridge.png" class="person-img gold blend-screen" alt="Bridge" />
`},

// ──────── CLOSE ────────
{bg:'bg-w', html:`
<div style="text-align:center;display:flex;flex-direction:column;align-items:center">
<p class="lbl a1" style="color:var(--blue);margin-bottom:14px">Join the Revolution</p>
<h2 class="hero a2" style="font-size:clamp(32px,5vw,64px)">Your future starts<br><span class="grb">right now.</span></h2>
<p class="sub a3" style="margin-top:14px;opacity:.5;text-align:center;margin-left:auto;margin-right:auto">Scan the QR. Send a message. Lock in your spot.</p>
<div class="a4" style="display:flex;align-items:center;gap:12px;margin-top:24px">
<svg width="26" height="26" viewBox="0 0 24 24" fill="#34C759"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 2C6.477 2 2 6.477 2 12c0 1.89.525 3.66 1.438 5.168L2 22l4.832-1.438A9.955 9.955 0 0012 22c5.523 0 10-4.477 10-10S17.523 2 12 2z"/></svg>
<span style="font-size:clamp(24px,3vw,40px);font-weight:700;letter-spacing:.04em;color:var(--green)">9087929229</span>
</div>
<div class="a5" style="margin-top:24px">
<div style="font-size:clamp(14px,1.4vw,18px);font-weight:600;color:var(--blue)">riselabs.one</div>
<p style="margin-top:32px;font-size:12px;opacity:.3">RiseLabs · Zerone Technologies · Chennai</p>
</div>
</div>
`},

]; // end slides

// ═══════════ RENDER ═══════════
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
const hint = document.getElementById('hint');
let cur = 0;
const tot = slides.length;

function go(i) {
  slides[cur].classList.remove('active');
  // reset anims
  slides[i].querySelectorAll('.a1,.a2,.a3,.a4,.a5').forEach(el => {
    el.style.animation = 'none';
    el.offsetHeight;
    el.style.animation = '';
  });
  slides[i].classList.add('active');
  cur = i;
  pb.style.width = ((i+1)/tot*100)+'%';
  ctr.textContent = (i+1)+' / '+tot;
  if(i>0) hint.style.opacity='0';
}

function next(){ if(cur<tot-1) go(cur+1); }
function prev(){ if(cur>0) go(cur-1); }

document.addEventListener('click', e => {
  if(e.target.closest('a')) return;
  e.clientX < window.innerWidth*.2 ? prev() : next();
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
