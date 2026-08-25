import sys
import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)


html_head = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Think Like an Industry Developer — Ultimate Seminar Deck</title>
<style>
:root{
  --bg:#000000;--bg2:#0a0a0d;--ink:#f5f5f7;--dim:#a0a0b8;--dimmer:#78788c;
  --gold:#d4a24e;--gold-soft:#e8c583;--blue:#2997ff;--green:#5fd39b;--red:#ff453a;--purple:#bf5af2;
  --line:rgba(255,255,255,.14);--card:rgba(255,255,255,.05);
}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{height:100%;background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Helvetica Neue",Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;overflow:hidden;}
.deck{position:fixed;inset:0;}
.slide{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;
  padding:7.5vh 8.5vw;opacity:0;transform:scale(1.04);
  transition:opacity .5s cubic-bezier(.22,.61,.36,1),transform .5s cubic-bezier(.22,.61,.36,1);pointer-events:none;}
.slide.active{opacity:1;transform:scale(1);pointer-events:auto;}
.slide.prev{transform:scale(.98);}
.slide.center{align-items:center;text-align:center;}
.slide.center .lead{margin-left:auto;margin-right:auto;}

/* Radial Ambient Glow Behind Headers */
.glow-bg {
  position: absolute;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(41, 151, 255, 0.15) 0%, rgba(212, 162, 78, 0.08) 40%, transparent 70%);
  top: 20%;
  left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
  z-index: 0;
}

/* Auto Reveal Animations */
.slide.active .reveal{animation:rise .75s cubic-bezier(.22,.61,.36,1) both;}
.slide.active .reveal:nth-child(1){animation-delay:.05s;}
.slide.active .reveal:nth-child(2){animation-delay:.12s;}
.slide.active .reveal:nth-child(3){animation-delay:.19s;}
.slide.active .reveal:nth-child(4){animation-delay:.26s;}
.slide.active .reveal:nth-child(5){animation-delay:.33s;}
.slide.active .reveal:nth-child(6){animation-delay:.40s;}

@keyframes rise{from{opacity:0;transform:translateY(18px);}to{opacity:1;transform:translateY(0);}}

/* Category Pill Badges */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.35rem 0.85rem;
  border-radius: 100px;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 1rem;
}
.badge.blue { background: rgba(41, 151, 255, 0.15); color: #2997ff; border: 1px solid rgba(41, 151, 255, 0.35); }
.badge.gold { background: rgba(212, 162, 78, 0.15); color: #d4a24e; border: 1px solid rgba(212, 162, 78, 0.35); }
.badge.green { background: rgba(95, 211, 155, 0.15); color: #5fd39b; border: 1px solid rgba(95, 211, 155, 0.35); }
.badge.red  { background: rgba(255, 69, 58, 0.15);  color: #ff453a; border: 1px solid rgba(255, 69, 58, 0.35); }
.badge.purple { background: rgba(191, 90, 242, 0.15); color: #bf5af2; border: 1px solid rgba(191, 90, 242, 0.35); }

.eyebrow{font-size:clamp(.72rem,1.05vw,.92rem);letter-spacing:.25em;text-transform:uppercase;font-weight:700;color:var(--gold);margin-bottom:1.1rem;display:flex;align-items:center;gap:.6rem;}
.eyebrow.cool{color:var(--blue);}.eyebrow.grn{color:var(--green);}.eyebrow.purp{color:var(--purple);}.eyebrow.red{color:var(--red);}
h1{font-size:clamp(2.6rem,7.2vw,6.2rem);font-weight:700;letter-spacing:-.03em;line-height:1.04;}
h2{font-size:clamp(1.9rem,4.5vw,3.8rem);font-weight:700;letter-spacing:-.028em;line-height:1.1;}
h3{font-size:clamp(1.35rem,2.8vw,2.4rem);font-weight:600;letter-spacing:-.02em;line-height:1.18;}
.lead{font-size:clamp(1.08rem,1.85vw,1.55rem);font-weight:400;color:#d0d0e2;line-height:1.5;letter-spacing:-.01em;max-width:68ch;}
.kicker{font-size:clamp(.95rem,1.4vw,1.18rem);color:#a5a5c0;margin-top:1.2rem;font-weight:450;max-width:66ch;}
.grad{background:linear-gradient(120deg,#fff,var(--gold-soft) 55%,var(--gold));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.grad-cool{background:linear-gradient(120deg,#fff,#8ab6ff 55%,var(--blue));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.grad-grn{background:linear-gradient(120deg,#fff,#9fe8c4 55%,var(--green));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.grad-purp{background:linear-gradient(120deg,#fff,#d8b4fe 55%,var(--purple));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.grad-red{background:linear-gradient(120deg,#fff,#ff9994 55%,var(--red));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.mono{font-family:"SF Mono",ui-monospace,Menlo,monospace;font-size:.95em;color:var(--gold-soft);font-weight:500;}
em{font-style:italic;color:var(--ink);}

.split{display:grid;grid-template-columns:1fr 1fr;gap:clamp(1.5rem,4vw,3.2rem);align-items:start;width:100%;position:relative;}
.split.even{grid-template-columns:1fr 1fr;}

/* Floating VS Badge for Comparison Slides */
.vs-badge {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 46px;
  height: 46px;
  background: #000000;
  border: 2px solid var(--gold);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 0.9rem;
  color: var(--gold);
  box-shadow: 0 0 25px rgba(212, 162, 78, 0.5);
  z-index: 10;
}

.build{background:linear-gradient(160deg,rgba(212,162,78,.14),rgba(212,162,78,.03));border:1px solid rgba(212,162,78,.32);border-radius:20px;padding:1.6rem 1.7rem;width:100%;}
.build.cool{background:linear-gradient(160deg,rgba(41,151,255,.14),rgba(41,151,255,.03));border-color:rgba(41,151,255,.32);}
.build.grn{background:linear-gradient(160deg,rgba(95,211,155,.14),rgba(95,211,155,.03));border-color:rgba(95,211,155,.32);}
.build.red{background:linear-gradient(160deg,rgba(255,69,58,.14),rgba(255,69,58,.03));border-color:rgba(255,69,58,.32);}
.build .bl{font-size:.78rem;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:.9rem;}
.build.cool .bl{color:var(--blue);}.build.grn .bl{color:var(--green);}.build.red .bl{color:var(--red);}
.build ul{list-style:none;display:flex;flex-direction:column;gap:.75rem;}
.build li{font-size:clamp(.92rem,1.35vw,1.1rem);line-height:1.45;padding-left:1.6rem;position:relative;color:var(--ink);font-weight:450;}
.build li::before{content:"→";position:absolute;left:0;color:var(--gold);font-weight:600;}
.build.cool li::before{color:var(--blue);}.build.grn li::before{color:var(--green);}.build.red li::before{color:var(--red);}

/* Story Card Styling */
.story-card {
  background: linear-gradient(145deg, rgba(255,255,255,.07), rgba(255,255,255,.02));
  border: 1px solid rgba(212,162,78,.4);
  border-radius: 20px;
  padding: 1.8rem 2rem;
  width: 100%;
  margin-top: 1.2rem;
}
.story-card.cool { border-color: rgba(41,151,255,.4); }
.story-card.grn { border-color: rgba(95,211,155,.4); }
.story-card.red { border-color: rgba(255,69,58,.4); }
.story-card .sc-title { font-size: 1.08rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; color: var(--gold); margin-bottom: .6rem; }
.story-card.cool .sc-title { color: var(--blue); }
.story-card.grn .sc-title { color: var(--green); }
.story-card.red .sc-title { color: var(--red); }
.story-card .sc-text { font-size: clamp(1.05rem, 1.55vw, 1.3rem); line-height: 1.6; color: #e2e8f0; }

/* macOS Glassmorphism IDE Card */
.code-box-clean {
  background: rgba(10, 11, 16, 0.88) !important;
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border: 1px solid rgba(255, 255, 255, 0.15) !important;
  border-top: 1px solid rgba(255, 255, 255, 0.3) !important;
  border-radius: 20px !important;
  padding: 1.8rem 2.2rem;
  font-family: "SF Mono", ui-monospace, Menlo, monospace;
  font-size: clamp(1.02rem, 1.55vw, 1.35rem);
  line-height: 1.7;
  color: #f8fafc;
  width: 100%;
  box-shadow: 0 20px 50px rgba(0,0,0,0.8), 0 0 30px rgba(41, 151, 255, 0.12) !important;
  margin-top: 1.4rem;
  position: relative;
}
/* macOS Window Dots */
.code-box-clean::before {
  content: "";
  display: block;
  height: 12px;
  width: 12px;
  border-radius: 50%;
  background: #ff5f56;
  box-shadow: 20px 0 0 #ffbd2e, 40px 0 0 #27c93f;
  margin-bottom: 1.2rem;
}

.code-box-clean.cool { border-color: rgba(41,151,255,.5) !important; }
.code-box-clean.grn { border-color: rgba(95,211,155,.5) !important; }
.code-box-clean.red { border-color: rgba(255,69,58,.5) !important; }

/* Code Line Highlights */
.code-line.highlight-green {
  background: rgba(95, 211, 155, 0.15);
  border-left: 3px solid var(--green);
  padding-left: 0.8rem;
  margin-left: -0.8rem;
  border-radius: 0 6px 6px 0;
}
.code-line.highlight-gold {
  background: rgba(212, 162, 78, 0.15);
  border-left: 3px solid var(--gold);
  padding-left: 0.8rem;
  margin-left: -0.8rem;
  border-radius: 0 6px 6px 0;
}
.code-line.highlight-red {
  background: rgba(255, 69, 58, 0.15);
  border-left: 3px solid var(--red);
  padding-left: 0.8rem;
  margin-left: -0.8rem;
  border-radius: 0 6px 6px 0;
}

.code-box-clean .kw { color: #ff79c6; font-weight: 700; }
.code-box-clean .fn { color: #50fa7b; font-weight: 700; }
.code-box-clean .str { color: #f1fa8c; }
.code-box-clean .cm { color: #8b9bb4; font-style: italic; }
.code-box-clean .num { color: #bd93f9; font-weight: 700; }

/* Keyword Mapping Ribbon */
.kw-mapping {
  background: rgba(212,162,78,.12);
  border: 1px solid rgba(212,162,78,.35);
  border-radius: 12px;
  padding: .75rem 1.2rem;
  margin-top: 1.1rem;
  font-size: clamp(.9rem, 1.3vw, 1.1rem);
  color: #e8c583;
}
.kw-mapping.cool { background: rgba(41,151,255,.12); border-color: rgba(41,151,255,.35); color: #9ec5ff; }
.kw-mapping.grn { background: rgba(95,211,155,.12); border-color: rgba(95,211,155,.35); color: #abf0d0; }
.kw-mapping.red { background: rgba(255,69,58,.12); border-color: rgba(255,69,58,.35); color: #ffb3b0; }

.tanglish-box{background:rgba(212,162,78,.08);border-left:3px solid var(--gold);border-radius:0 12px 12px 0;padding:.9rem 1.2rem;margin-top:1.2rem;}
.tanglish-box.cool{background:rgba(41,151,255,.08);border-color:var(--blue);}
.tanglish-box.grn{background:rgba(95,211,155,.08);border-color:var(--green);}
.tanglish-box.red{background:rgba(255,69,58,.08);border-color:var(--red);}
.tanglish-box .tb-lbl{font-size:.7rem;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);font-weight:700;margin-bottom:.3rem;}
.tanglish-box.cool .tb-lbl{color:var(--blue);}.tanglish-box.grn .tb-lbl{color:var(--green);}.tanglish-box.red .tb-lbl{color:var(--red);}
.tanglish-box .tb-txt{font-size:clamp(.92rem,1.35vw,1.12rem);font-style:italic;color:#e8c583;line-height:1.45;}
.tanglish-box.cool .tb-txt{color:#9ec5ff;}.tanglish-box.grn .tb-txt{color:#abf0d0;}.tanglish-box.red .tb-txt{color:#ffb3b0;}

.table-custom{width:100%;border-collapse:collapse;margin-top:1.1rem;font-size:clamp(.85rem,1.2vw,1.02rem);}
.table-custom th,.table-custom td{padding:.8rem 1.1rem;border:1px solid var(--line);text-align:left;}
.table-custom th{background:rgba(255,255,255,.07);color:var(--gold);font-weight:700;letter-spacing:.03em;}
.table-custom tr:nth-child(even){background:rgba(255,255,255,.025);}

/* Progress & Chrome Footer */
.progress{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,var(--gold),var(--blue),var(--green));z-index:50;transition:width .4s ease;}
.chrome{position:fixed;bottom:2vh;left:0;right:0;display:flex;justify-content:space-between;align-items:center;padding:0 8.5vw;z-index:40;font-size:.78rem;color:var(--dimmer);pointer-events:none;}
.chrome .brand{font-weight:600;letter-spacing:.02em;color:var(--dim);display:flex;align-items:center;gap:.6rem;}
.chrome .brand b{color:var(--gold);}
.chrome .right{display:flex;gap:1.2rem;align-items:center;pointer-events:auto;}
.notesbtn{cursor:pointer;border:1px solid var(--line);border-radius:6px;padding:4px 10px;color:var(--dim);font-size:.74rem;transition:all .3s;}
.notesbtn:hover{border-color:var(--gold);color:var(--gold);}
.counter{font-family:"SF Mono",ui-monospace,monospace;letter-spacing:.05em;}

/* Speaker Notes Panel Drawer */
.notes{position:fixed;left:0;right:0;bottom:0;z-index:60;background:rgba(10,10,12,.98);
  border-top:1px solid var(--line);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
  transform:translateY(100%);transition:transform .4s cubic-bezier(.22,.61,.36,1);max-height:46vh;display:flex;flex-direction:column;}
.notes.open{transform:translateY(0);}
.notes-head{display:flex;justify-content:space-between;align-items:center;padding:.9rem 8.5vw .6rem;border-bottom:1px solid var(--line);}
.notes-head .lbl{font-size:.72rem;letter-spacing:.24em;text-transform:uppercase;color:var(--gold);font-weight:700;}
.notes-head .x{cursor:pointer;color:var(--dim);font-size:1.1rem;line-height:1;}
.notes-body{overflow-y:auto;padding:1.1rem 8.5vw 1.6rem;font-size:.98rem;line-height:1.65;color:#d5d5e0;}
.notes-body a{color:var(--gold-soft);text-decoration:underline;text-underline-offset:2px;}
.notes-body a:hover{color:var(--gold);}
.notes-body b{color:var(--ink);}.notes-body i,.notes-body em{color:#e8c583;font-style:italic;}
.notes-body u{text-decoration:underline;}
.hint{position:fixed;bottom:2vh;left:50%;transform:translateX(-50%);font-size:.74rem;color:var(--dimmer);z-index:41;display:flex;gap:.5rem;align-items:center;animation:fade 4s ease 3s forwards;}
@keyframes fade{to{opacity:0;visibility:hidden;}}
.key{display:inline-flex;align-items:center;justify-content:center;min-width:20px;height:20px;padding:0 5px;border:1px solid var(--line);border-radius:5px;font-family:"SF Mono",monospace;font-size:.68rem;}

@media (max-width:860px){
  .slide{padding:8vh 6vw;}.split,.split.even{grid-template-columns:1fr;gap:1.4rem;}
  .notes-head,.notes-body{padding-left:6vw;padding-right:6vw;}
}
@media (prefers-reduced-motion:reduce){.slide,.slide .reveal{transition:opacity .2s;animation:none!important;}}
</style>
<script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
<div class="progress" id="progress"></div>
<div class="deck" id="deck">
"""

slides_html = []
notes = []

# ====================================================
# SECTION 1: MINDSET SHIFT (COLLEGE VS PRODUCTION)
# ====================================================

# Slide 0: Attendance Registration QR
slides_html.append("""
<section class="slide center active">
  <div class="glow-bg"></div>
  <div class="badge gold reveal"><i data-lucide="qr-code"></i> SEMINAR REGISTRATION</div>
  <h2 class="reveal" style="font-size:clamp(2.4rem, 5.5vw, 4.8rem);">Scan to <span class="grad">Register</span></h2>
  <img src="../../assets/qr_thinktg101.png" class="reveal" style="display:block; margin: 1.4rem auto; max-width: 250px; border-radius: 18px; border: 5px solid #ffffff; box-shadow: 0 20px 50px rgba(0,0,0,0.6);" alt="Registration QR Code" />
  <p class="lead reveal" style="margin-top:1rem; font-size:clamp(1.05rem, 1.6vw, 1.35rem);">Scan the QR code on your phone before we begin to register your attendance & claim workshop resources.</p>
  <p class="mono reveal" style="margin-top:.5rem; font-size:1.05rem; color:var(--gold-soft);">https://riselabs.one/events/register?code=THINKTG101</p>
  <div class="tanglish-box reveal" style="max-width:550px; margin-left:auto; margin-right:auto;">
    <div class="tb-lbl">Seminar Access Callout</div>
    <div class="tb-txt">"Bro! Seminar start panradhuku munadi QR code scan panni attendance-a register pannedunga!"</div>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> Welcome everyone! Please scan this QR code to register your attendance.""")

# Slide 1: Interactive Split Hero Opener
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green reveal"><i data-lucide="radio"></i> LIVE · TAGORE CAMPUS KEYNOTE · 2026 EDITION</div>
  <div class="split even reveal" style="align-items:center;">
    <div>
      <h1 style="font-size:clamp(2.5rem, 5.2vw, 4.6rem); line-height:1.06;">Think Like an<br><span class="grad">Industry Developer</span></h1>
      <p class="lead" style="margin-top:1.2rem; font-size:clamp(1.05rem, 1.5vw, 1.25rem);">Transitioning from academic lab coding to production-grade software engineering.</p>
      <div class="tanglish-box cool" style="margin-top:1.4rem;">
        <div class="tb-lbl">Seminar Mission</div>
        <div class="tb-txt">"Textbook CS-a Swiggy, Zomato & Production Scale-a maatha porom!"</div>
      </div>
    </div>
    <div>
      <div class="code-box-clean cool">
        <div class="cm">// Terminal Execution Preview</div>
        <span class="kw">$</span> antigravity init --mode production-developer<br>
        <span class="str">[✔] Compiling Academic CS Foundations...</span><br>
        <span class="str">[✔] Connecting High-Scale Tamil Analogies...</span><br>
        <span class="fn">[🚀] SYSTEM READY: 1,000,000 requests/sec!</span>
      </div>
    </div>
  </div>
</section>
""")
notes.append("""<b>2-Minute Intro Kickoff:</b> Welcome to Think Like an Industry Developer! Today we bridge the gap between classroom theory and real-world industry practice.""")

# Slide 2: Core Philosophy (College Code vs Production Code)
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue reveal"><i data-lucide="user-check"></i> SECTION 1 · THE CORE PHILOSOPHY</div>
  <h2 class="reveal">College Mode vs. Production Mode</h2>
  <div class="split even reveal" style="margin-top:1.4rem;">
    <div class="build red">
      <div class="bl">College Lab Mode 🎓</div>
      <ul>
        <li>Clear semester lab exams & pass static test cases</li>
        <li>"Run aachis, output vandhuchu, lab record submit pannedu"</li>
        <li>Single run output is enough</li>
      </ul>
    </div>
    <div class="vs-badge">VS</div>
    <div class="build grn">
      <div class="bl">Production Mode 🚀</div>
      <ul>
        <li>Runs 24/7 for 1,000,000+ live active concurrent users</li>
        <li>Handles network drops, timeout errors & heavy spikes</li>
        <li>Teammates can read, debug & refactor 6 months later</li>
      </ul>
    </div>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> Transition from lab assignment mindset to production engineering.""")

# Slide 3: Two Hats Principle
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge gold reveal"><i data-lucide="hard-hat"></i> SECTION 1 · DAILY REALITY</div>
  <h2 class="reveal">The "Two Hats" Principle</h2>
  <div class="split even reveal" style="margin-top:1.4rem;">
    <div class="build cool">
      <div class="bl">🔵 Builder Hat (30% of Time)</div>
      <ul>
        <li>Writing new feature modules & UI components</li>
        <li>Creating REST API endpoints & database schemas</li>
      </ul>
    </div>
    <div class="vs-badge">VS</div>
    <div class="build red">
      <div class="bl">🔴 Editor & Reader Hat (70% of Time)</div>
      <ul>
        <li>Reading teammate code to debug issues</li>
        <li>Reviewing Pull Requests & giving constructive feedback</li>
        <li>Refactoring & writing automated test suites</li>
      </ul>
    </div>
  </div>
  <div class="tanglish-box grn reveal" style="margin-top:1.2rem;">
    <div class="tb-lbl">The 70% Code Reading Rule</div>
    <div class="tb-txt">"Developers 70% time mathavanga code-ah read panni edit panra role-la thaan iruppom. Readable code ezhudhuradhu mandatory!"</div>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> Developers spend 70% of their time reading code.""")

# Slide 4: Tanglish Analogy: Aalim Canteen vs Swiggy Scale
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge red reveal"><i data-lucide="zap"></i> SECTION 1 · SCALE ANALOGY</div>
  <h2 class="reveal">Aalim Canteen vs.<br><span class="grad-cool">Swiggy Production Scale</span></h2>
  <div class="story-card cool reveal">
    <div class="sc-title">Real-World Scale Story 🍔</div>
    <div class="sc-text">
      Aalim Canteen-la 50 per-ukku token pottu tea kuduthu counter manage panradhum, Swiggy New Year Night-la 100,000 orders-a collapse aagama route panradhum vera level!<br><br>
      College-la 1 token order run aana podhum;<br>
      Industry-la New Year Night spike-a handle pannanum without crashing!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Aalim Canteen token vs Swiggy New Year scale.""")

# ====================================================
# SECTION 2: CORE CS CONCEPTS REIMAGINED
# ====================================================

# CONCEPT 1: ABSTRACTION LAYERS
# Slide 5: Concept 1 Story
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge gold reveal"><i data-lucide="layers"></i> SECTION 2 · CONCEPT 1 (ABSTRACTION)</div>
  <h2 class="reveal">A.R. Rahman Live Concert<br><span class="grad">Mixing Console</span></h2>
  <div class="story-card reveal">
    <div class="sc-title">Concert Sound Board Story 🎛️</div>
    <div class="sc-text">
      Nehru Stadium concert-la A.R. Rahman single slider-a mela thookuraru — bass blast aagudhu!<br>
      Stage keela irukura 500 physical copper wires-a spanner vecha adjust panraaru? No! High-level slider interface pushes commands down to power amps & sound cards.<br><br>
      <b>In Code:</b> <code>console.log("Hello")</code> ezhudhuna, hardware layer CPU-la irukura 10,000 transistors-a automatically align pannudhu.
    </div>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> High-level interface hiding low-level execution.""")

# Slide 6: Concept 1 Code
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge gold reveal"><i data-lucide="code-2"></i> SECTION 2 · TANGLISH CODE</div>
  <h2 class="reveal">🎛️ Abstraction Layers<br><span class="grad">(Hidden Hardware Execution)</span></h2>
  <div class="code-box-clean reveal">
    <div class="code-line highlight-gold"><span class="cm">// High-Level Framework Command</span></div>
    System.audio.<span class="fn">increaseVolume</span>({ level: <span class="num">90</span> });<br><br>
    <span class="cm">// Lower Engine Execution (Hidden Abstraction)</span><br>
    <span class="cm">// [User Interface] -> [API Gateway] -> [Native Module] -> [CPU Registers]</span>
  </div>
  <div class="kw-mapping reveal">
    🔑 <b>Tamil Mapping:</b> Abstraction = <b>உள்ளே இருக்கும் சிக்கலான வையரிங்கை மறைத்து எளிய பட்டன் தருவது</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> High level command vs hidden lower engine execution.""")

# CONCEPT 2: ARRAY INDEXING & MEMORY OFFSETS
# Slide 7: Concept 2 Story
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue reveal"><i data-lucide="zap"></i> SECTION 2 · CONCEPT 2 (ARRAYS)</div>
  <h2 class="reveal">MTC Bus #23C Door Entrance<br><span class="grad-cool">Memory Offset Math</span></h2>
  <div class="story-card cool reveal">
    <div class="sc-title">MTC Bus Seat Offset Story 🚌</div>
    <div class="sc-text">
      Broadway MTC bus bench-la 4 per ukkaandhirukkaanga: <b>['Conductor', 'Kamal', 'Rajini', 'Vijay']</b>.<br><br>
      <b>Index 0-na "1st Person" illa!</b> Adhu <b>Door Entrance-la irundhu 0 steps distance!</b><br>
      Index 1 = Door-la irundhu 1 step offset (Kamal). Index 2 = 2 steps offset (Rajini).<br><br>
      <b>Memory-la array index-na: Start address-la irundhu evlavu steps thalli irukkeenga!</b>
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Bus seat door offset indexing.""")

# Slide 8: Concept 2 Code
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue reveal"><i data-lucide="code-2"></i> SECTION 2 · TANGLISH CODE</div>
  <h2 class="reveal">🧵 Array Indexing &amp; Memory Offsets<br><span class="grad-cool">(0-Offset Math)</span></h2>
  <div class="code-box-clean cool reveal">
    <span class="cm">// const = மாற்ற முடியாத பேருந்து இருக்கை (Fixed Bus Bench)</span><br>
    <span class="kw">const</span> mtcBench = [<span class="str">'Conductor'</span>, <span class="str">'Kamal'</span>, <span class="str">'Rajini'</span>, <span class="str">'Vijay'</span>];<br><br>
    <div class="code-line highlight-green"><span class="cm">// Address Offset Calculation: Start Address (0x1000) + (Index * Element Size)</span><br>
    <span class="kw">let</span> frontSeat = mtcBench[<span class="num">0</span>]; <span class="cm">// 0 Steps away from door -> 'Conductor'</span></div>
    <span class="kw">let</span> thirdSeat = mtcBench[<span class="num">2</span>]; <span class="cm">// 2 Steps away from door -> 'Rajini'</span>
  </div>
  <div class="kw-mapping cool reveal">
    🔑 <b>Tamil Mapping:</b> <code>mtcBench[0]</code> = <b>வாசலில் இருந்து 0 அடிகள் தொலைவு</b> (Memory Offset Distance)
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Memory offset calculation formula.""")

# CONCEPT 3: INHERITANCE & METHOD OVERRIDING
# Slide 9: Concept 3 Story
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge gold reveal"><i data-lucide="zap"></i> SECTION 2 · CONCEPT 3 (INHERITANCE)</div>
  <h2 class="reveal">Thalapathy Vijay Movie Intro<br><span class="grad">Template Inheritance</span></h2>
  <div class="story-card reveal">
    <div class="sc-title">Mass Hero Movie Template Story 🎬</div>
    <div class="sc-text">
      Pudhu movie shoot start aagum podhu — director mass entry camera angle-a scratch-la irundhu invent panraara? No!<br><br>
      Base Hero Class-la irundhu <b>Slow-motion walk, Title card</b> automatic-a inherit aagudhu.<br>
      Director pudhusa <b>1 specific mass dialogue-a override</b> panraaru.<br><br>
      <b>Child Class = Parent Class Baseline + Specific Pudhu Extensions!</b>
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Movie template inheritance.""")

# Slide 10: Concept 3 Code
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge gold reveal"><i data-lucide="code-2"></i> SECTION 2 · TANGLISH CODE</div>
  <h2 class="reveal">🎬 Mass Hero Template<br><span class="grad">(Inheritance & Override)</span></h2>
  <div class="code-box-clean reveal">
    <span class="cm">// class = அடிப்படை வடிவம் (Baseline Template Blueprint)</span><br>
    <span class="kw">class</span> <span class="fn">MassHero</span> { introWalk = <span class="str">"🔥 Slow-Motion Entry"</span>; }<br><br>
    <div class="code-line highlight-gold"><span class="cm">// extends = பரம்பரைத் தொடர்ச்சி (Inherit parent capabilities)</span><br>
    <span class="kw">class</span> <span class="fn">GOATHero</span> <span class="kw">extends</span> <span class="fn">MassHero</span> { punchLine = <span class="str">"I am waiting!"</span>; }</div>
  </div>
  <div class="kw-mapping reveal">
    🔑 <b>Tamil Mappings:</b> <code>class</code> = <b>அடிப்படை வடிவம்</b> (Blueprint) | <code>extends</code> = <b>பரம்பரைத் தொடர்ச்சி</b> (Inherit)
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Inheritance class and extends Tamil mappings.""")

# CONCEPT 4: HASH MAPS VS LINEAR SEARCH (O(1) vs O(n))
# Slide 11: Concept 4 Story
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue reveal"><i data-lucide="zap"></i> SECTION 2 · CONCEPT 4 (HASH MAPS)</div>
  <h2 class="reveal">Marina Beach Sunday Evening<br><span class="grad-cool">Bike Parking System</span></h2>
  <div class="story-card cool reveal">
    <div class="sc-title">Marina Parking Token Story 🏍️</div>
    <div class="sc-text">
      <b>Linear Search (O(n)):</b> Attendant 2,000 bikes-a line-by-line number plate read panni unga bike-a theduradhu (2 hours aagum).<br><br>
      <b>Hash Map (O(1)):</b> Attendant ungalukku <b>Token #842</b> kuduthutu, bike-a <b>Slot #842</b>-la vechuruvaar.<br>
      Token-a kaatuna 1 second-la bike pickup! (Key = Token, Value = Bike Details).
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Marina beach bike parking token map.""")

# Slide 12: Concept 4 Code
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue reveal"><i data-lucide="code-2"></i> SECTION 2 · TANGLISH CODE</div>
  <h2 class="reveal">⚡ Instant Token Bike Pickup<br><span class="grad-cool">(Hash Map O(1) vs O(n))</span></h2>
  <div class="code-box-clean cool reveal">
    <span class="cm">// Key-Value Parking Map (சாவி - மதிப்பு ஜோடி)</span><br>
    <span class="kw">const</span> marinaParkingMap = <span class="kw">new</span> <span class="fn">Map</span>();<br>
    marinaParkingMap.<span class="fn">set</span>(<span class="num">842</span>, { bikeNo: <span class="str">"TN-01-AB-1234"</span>, owner: <span class="str">"Kabir"</span> });<br><br>
    <div class="code-line highlight-green"><span class="cm">// O(1) Instant Direct Access</span><br>
    <span class="kw">let</span> myBike = marinaParkingMap.<span class="fn">get</span>(<span class="num">842</span>); <span class="cm">// Returns object in 0.001ms!</span></div>
  </div>
  <div class="kw-mapping cool reveal">
    🔑 <b>Tamil Mapping:</b> Key-Value Pair = <b>சாவி - மதிப்பு ஜோடி</b> (Direct O(1) Token Pickup)
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Hash map O(1) direct access.""")

# CONCEPT 5: DEFENSIVE PROGRAMMING & RESILIENCE
# Slide 13: Concept 5 Story
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green reveal"><i data-lucide="shield-check"></i> SECTION 2 · CONCEPT 5 (DEFENSIVE CODE)</div>
  <h2 class="reveal">Canteen Generator Backup System<br><span class="grad-grn">(Defensive Resilience)</span></h2>
  <div class="story-card grn reveal">
    <div class="sc-title">Canteen Generator Backup Story ⚡</div>
    <div class="sc-text">
      Canteen rush hour billing-la sudden-a current cut aagudhu. App crash aagi queue block aana disaster.<br><br>
      <code>try</code> online billing ➔ <code>catch</code> current poona automatic-a UPS generator-ku shift aagi zero customer disruption!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Defensive programming try/catch UPS generator.""")

# Slide 14: Concept 5 Code
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green reveal"><i data-lucide="code-2"></i> SECTION 2 · TANGLISH CODE</div>
  <h2 class="reveal">🛡️ Defensive Billing Engine<br><span class="grad-grn">(Try / Catch / Finally)</span></h2>
  <div class="code-box-clean grn reveal">
    <span class="cm">// try = முயற்சி பண்ணு (Primary Online Billing)</span><br>
    <span class="kw">try</span> { <span class="fn">processOnlineBilling</span>(orderData); } <br>
    <div class="code-line highlight-green"><span class="cm">// catch = பிரச்சனை வந்தால் சமாளி (UPS Backup System)</span><br>
    <span class="kw">catch</span> (PowerCutError) { <span class="fn">processOfflineUPSBilling</span>(orderData); }</div>
    <span class="kw">finally</span> { <span class="fn">syncAuditLogs</span>(); }
  </div>
  <div class="kw-mapping grn reveal">
    🔑 <b>Tamil Mappings:</b> <code>try</code> = <b>முயற்சி பண்ணு</b> | <code>catch</code> = <b>பிரச்சனை வந்தால் சமாளி</b> (UPS Backup)
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Try/Catch/Finally resilience engine.""")

# ====================================================
# SECTION 3: SYSTEM ARCHITECTURE & SCALING PATTERNS
# ====================================================

# CONCEPT 6: DATABASE INDEXING VS FULL TABLE SCAN
# Slide 15: Concept 6 Story
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue reveal"><i data-lucide="database"></i> SECTION 3 · SYSTEM ARCHITECTURE</div>
  <h2 class="reveal">Trichy Bus Stand Inquiry vs.<br><span class="grad-cool">Database Indexing (O(log n))</span></h2>
  <div class="story-card cool reveal">
    <div class="sc-title">Trichy Bus Stand Alpha-Board Story 🚌</div>
    <div class="sc-text">
      Trichy bus stand-la <b>Bus #12B</b> entha bay-la irukku-nu kandupidikkanum.<br><br>
      <b>No Index (Full Table Scan O(n)):</b> 150 bays-kukum nadandhu poi, ovvoru bus board-aiyum line-by-line padikka 45 mins aagum!<br><br>
      <b>Database Index (O(log n)):</b> Entrance-la <code>Bus Number -> Bay Number</code> Alpha-Board vechurukanga. Single look-la direct-a <b>Bay #12</b>-ku straight-a poradhu!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Database B-Tree Indexing vs Full Table Scan.""")

# Slide 16: Concept 6 Code
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue reveal"><i data-lucide="code-2"></i> SECTION 3 · TANGLISH CODE</div>
  <h2 class="reveal">🔍 Database B-Tree Indexing<br><span class="grad-cool">(Instagram Search O(log n))</span></h2>
  <div class="code-box-clean cool reveal">
    <span class="cm">// ❌ WITHOUT INDEX: Scanning 10 Million Users (Slow 4,200ms O(n))</span><br>
    db.users.<span class="fn">find</span>({ instagramHandle: <span class="str">"@kabir"</span> });<br><br>
    <div class="code-line highlight-green"><span class="cm">// ✅ WITH INDEX: B-Tree Fast Lookup (அகராதிப் பட்டியல் O(log n))</span><br>
    db.users.<span class="fn">createIndex</span>({ instagramHandle: <span class="num">1</span> });<br>
    db.users.<span class="fn">find</span>({ instagramHandle: <span class="str">"@kabir"</span> }); <span class="cm">// Instant 2ms pickup!</span></div>
  </div>
  <div class="kw-mapping cool reveal">
    🔑 <b>Tamil Mapping:</b> DB Index = <b>அகராதிப் பட்டியல்</b> (Fast B-Tree Search O(log n))
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Database indexing query optimization.""")

# CONCEPT 7: MICROSERVICES VS MONOLITH
# Slide 17: Concept 7 Story
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green reveal"><i data-lucide="cpu"></i> SECTION 3 · SYSTEM ARCHITECTURE</div>
  <h2 class="reveal">Diwali Supermarket vs.<br><span class="grad-grn">Zomato Microservices</span></h2>
  <div class="story-card grn reveal">
    <div class="sc-title">Diwali Sale Billing Story 🛍️</div>
    <div class="sc-text">
      <b>Monolith (Single Big Shop):</b> Cashier, billing, veggie weighing ellathukkum <b>ஒரே ஒரு Billing Master</b> thaan. Master collapse aana entire shop door close!<br><br>
      <b>Microservices (Multiplex Counters):</b> Veggies-ku thani counter, Cash-ku thani counter, Delivery-ku thani exit.<br>
      Delivery boy bike puncher aanaalum billing counter 100% functional-a run aagum!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Monolith vs Microservices architecture.""")

# Slide 18: Concept 7 Code
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green reveal"><i data-lucide="code-2"></i> SECTION 3 · TANGLISH CODE</div>
  <h2 class="reveal">🏗️ Microservices Fault Isolation<br><span class="grad-grn">(Zomato Order Handling)</span></h2>
  <div class="code-box-clean grn reveal">
    <span class="kw">async function</span> <span class="fn">processZomatoOrderResilient</span>(order) {<br>
    &nbsp;&nbsp;<span class="kw">try</span> {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">await</span> paymentMicroservice.<span class="fn">charge</span>(order);<br>
    &nbsp;&nbsp;} <span class="kw">catch</span> (PaymentError) {<br>
    <div class="code-line highlight-green">&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">// Payment service down-aanaalum, Zomato Cart stays safe!</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">return</span> <span class="fn">showAlternativePaymentOptions</span>();</div><br>
    &nbsp;&nbsp;}<br>
    }
  </div>
  <div class="kw-mapping grn reveal">
    🔑 <b>Tamil Mapping:</b> Microservices = <b>தனித்தனி சுயாதீன சேவை அமைப்புகள்</b> (Isolated Resilience)
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Microservices fault isolation.""")

# CONCEPT 8: LOAD BALANCING & HORIZONTAL SCALING
# Slide 19: Concept 8 Story
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge gold reveal"><i data-lucide="network"></i> SECTION 3 · SYSTEM ARCHITECTURE</div>
  <h2 class="reveal">Highway Multi-Lane Toll Plaza vs.<br><span class="grad">NGINX Load Balancer</span></h2>
  <div class="story-card reveal">
    <div class="sc-title">Highway Toll Plaza Story 🚗</div>
    <div class="sc-text">
      Pongal holiday-la Chennai-Trichy highway-la 10,000 cars varudhu.<br><br>
      <b>Vertical Scaling:</b> Single toll booth master-ku 5 Red Bull kuduthu fast-a work panna solradhu. He will still collapse!<br><br>
      <b>Horizontal Scaling (Load Balancer):</b> 20 Toll Gates parallel-a open panni, incoming cars-a Round-Robin method-la automatic-a split panni anuppuradhu!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Horizontal scaling vs vertical scaling.""")

# Slide 20: Concept 8 Code
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge gold reveal"><i data-lucide="code-2"></i> SECTION 3 · TANGLISH CODE</div>
  <h2 class="reveal">🚦 Round-Robin Load Balancer<br><span class="grad">(Traffic Splitter)</span></h2>
  <div class="code-box-clean reveal">
    <span class="kw">const</span> backendServers = [<span class="str">'Server_A'</span>, <span class="str">'Server_B'</span>, <span class="str">'Server_C'</span>];<br>
    <span class="kw">let</span> currentServerIndex = <span class="num">0</span>;<br><br>
    <span class="kw">function</span> <span class="fn">routeIncomingUserRequest</span>(userRequest) {<br>
    <div class="code-line highlight-gold">&nbsp;&nbsp;<span class="kw">let</span> targetServer = backendServers[currentServerIndex];<br>
    &nbsp;&nbsp;currentServerIndex = (currentServerIndex + <span class="num">1</span>) % backendServers.length;</div><br>
    &nbsp;&nbsp;<span class="kw">return</span> targetServer.<span class="fn">forward</span>(userRequest);<br>
    }
  </div>
  <div class="kw-mapping reveal">
    🔑 <b>Tamil Mapping:</b> Load Balancer = <b>சுழற்சி முறையில் சுமையை பிரிப்பவர்</b> (Round-Robin Splitter)
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Load balancer round-robin routing logic.""")

# CONCEPT 9: DEBOUNCING & THROTTLING
# Slide 21: Concept 9 Story
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue reveal"><i data-lucide="zap"></i> SECTION 3 · EVENT OPTIMIZATION</div>
  <h2 class="reveal">Flipkart Search Bar Debouncing vs.<br><span class="grad-cool">Uber Live GPS Throttling</span></h2>
  <div class="story-card cool reveal">
    <div class="sc-title">Search Pause Story 🔍</div>
    <div class="sc-text">
      <b>Without Debouncing:</b> Student ovvoru letter ezhudhum podhum teacher-kitta poitu "Sir correct-a?"-nu 50 thadava kekkuradhu (50 unnecessary API calls!).<br><br>
      <b>Debouncing (Flipkart Search):</b> User ezhudhi mudichu <b>300ms pause panra varai wait panni</b> single-a search API call anuppuradhu!<br><br>
      <b>Throttling (Uber GPS):</b> Driver car odum podhu per millisecond-kum location update anuppaama, <b>strict-a every 2 seconds-ku 1 time</b> location data emit panradhu.
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Debouncing vs Throttling event optimization.""")

# Slide 22: Concept 9 Code
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue reveal"><i data-lucide="code-2"></i> SECTION 3 · TANGLISH CODE</div>
  <h2 class="reveal">⏱️ Smart Search Debouncer<br><span class="grad-cool">(Event Rate Limiting)</span></h2>
  <div class="code-box-clean cool reveal">
    <span class="kw">function</span> <span class="fn">debounceSearch</span>(searchFunction, delay = <span class="num">300</span>) {<br>
    &nbsp;&nbsp;<span class="kw">let</span> timer;<br>
    &nbsp;&nbsp;<span class="kw">return</span> <span class="kw">function</span> (...args) {<br>
    <div class="code-line highlight-green">&nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">clearTimeout</span>(timer); <span class="cm">// Reset countdown on every keystroke</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;timer = <span class="fn">setTimeout</span>(() => { searchFunction(...args); }, delay);</div><br>
    &nbsp;&nbsp;};<br>
    }
  </div>
  <div class="kw-mapping cool reveal">
    🔑 <b>Tamil Mapping:</b> Debounce = <b>பயனர் தட்டச்சை நிறுத்திய பின் இயக்கப்படும் காலதாபனம்</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Debounce implementation code.""")

# CONCEPT 10: IN-MEMORY CACHING (O(1))
# Slide 23: Concept 10 Story
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green reveal"><i data-lucide="database"></i> SECTION 3 · IN-MEMORY CACHING</div>
  <h2 class="reveal">Thinnai Cooler Water Pot vs.<br><span class="grad-grn">Deep Well Water (Redis Caching)</span></h2>
  <div class="story-card grn reveal">
    <div class="sc-title">Thinnai Water Pot Caching Story 🏺</div>
    <div class="sc-text">
      Veyil kaalathula daagam edukku:<br><br>
      <b>No Cache (Database Hit):</b> Ovvoru thadava thanni kekkum podhum kinathula (PostgreSQL DB) vaali thooki thanni eduradhu (30 mins delay!).<br><br>
      <b>In-Memory Cache (Redis Layer):</b> House entrance thinnai-la <b>Cooler Water Pot</b> vechurukom. Instant-a 1 second-la sip panni poite irukalaam!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Redis cache vs PostgreSQL DB hit.""")

# Slide 24: Concept 10 Code
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green reveal"><i data-lucide="code-2"></i> SECTION 3 · TANGLISH CODE</div>
  <h2 class="reveal">⚡ Redis In-Memory Cache<br><span class="grad-grn">(1ms Response Speed)</span></h2>
  <div class="code-box-clean grn reveal">
    <span class="kw">async function</span> <span class="fn">getSwiggyMenu</span>(restaurantId) {<br>
    <div class="code-line highlight-green">&nbsp;&nbsp;<span class="kw">let</span> cachedMenu = <span class="kw">await</span> redis.<span class="fn">get</span>(<span class="str">`menu:${restaurantId}`</span>);<br>
    &nbsp;&nbsp;<span class="kw">if</span> (cachedMenu) <span class="kw">return</span> JSON.<span class="fn">parse</span>(cachedMenu); <span class="cm">// Instant 1ms Return!</span></div><br>
    &nbsp;&nbsp;<span class="kw">let</span> dbMenu = <span class="kw">await</span> postgresDB.<span class="fn">query</span>(<span class="str">"SELECT * FROM menu WHERE id = $1"</span>, [restaurantId]);<br>
    &nbsp;&nbsp;<span class="kw">await</span> redis.<span class="fn">setex</span>(<span class="str">`menu:${restaurantId}`</span>, <span class="num">1800</span>, JSON.<span class="fn">stringify</span>(dbMenu));<br>
    &nbsp;&nbsp;<span class="kw">return</span> dbMenu;<br>
    }
  </div>
  <div class="kw-mapping grn reveal">
    🔑 <b>Tamil Mapping:</b> Redis Cache = <b>திண்ணைக் குளிர்ந்த நீர் பானை</b> (Fast In-Memory Layer)
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Redis caching query logic.""")

# CONCEPT 11: PUB/SUB & EVENT QUEUES
# Slide 25: Concept 11 Story
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge purple reveal"><i data-lucide="rss"></i> SECTION 3 · EVENT QUEUES</div>
  <h2 class="reveal">Dinakaran Newspaper Delivery Boy vs.<br><span class="grad-purp">Pub/Sub Message Queues</span></h2>
  <div class="story-card reveal">
    <div class="sc-title">Newspaper Agent Subscription Story 📰</div>
    <div class="sc-text">
      Daily morning newspaper padikka 1,000 per Dinakaran press office-ku nadandhu poitu news kekkuradhukku badhila, <b>Newspaper Delivery Agent-kitta Subscribe</b> panniruvanga.<br><br>
      Agent 5:00 AM-ku automatic-a ella veetukum paper poduvar!<br>
      <b>In Code:</b> Server-a repetitively poll pannaama, Message Broker (RabbitMQ/Kafka) event-a publish panna subscribers automatically react aavanga!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Pub/Sub message broker agent story.""")

# Slide 26: Concept 11 Code
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge purple reveal"><i data-lucide="code-2"></i> SECTION 3 · TANGLISH CODE</div>
  <h2 class="reveal">📡 Pub/Sub Event-Driven Broker<br><span class="grad-purp">(RabbitMQ / Kafka)</span></h2>
  <div class="code-box-clean reveal">
    <span class="cm">// Publisher: Swiggy Order Service</span><br>
    <div class="code-line highlight-gold"><span class="kw">function</span> <span class="fn">onOrderPlaced</span>(orderData) {<br>
    &nbsp;&nbsp;messageBroker.<span class="fn">publish</span>(<span class="str">"ORDER_PLACED_EVENT"</span>, orderData);<br>
    }</div><br>
    <span class="cm">// Subscriber: Kitchen Display App</span><br>
    messageBroker.<span class="fn">subscribe</span>(<span class="str">"ORDER_PLACED_EVENT"</span>, (data) => { kitchenPrinter.<span class="fn">printToken</span>(data.items); });
  </div>
  <div class="kw-mapping reveal">
    🔑 <b>Tamil Mapping:</b> Publish/Subscribe = <b>செய்தி வெளிவிடுவது & சந்தா செலுத்தி பெறுவது</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Pub/Sub event-driven message queue code.""")

# ====================================================
# SECTION 4: INDUSTRY BEST PRACTICES & SUMMARY MATRIX
# ====================================================

# Slide 27: Naming Conventions
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green reveal"><i data-lucide="check-square"></i> SECTION 4 · BEST PRACTICE #1</div>
  <h2 class="reveal">Clean Naming Conventions</h2>
  <div class="split even reveal" style="margin-top:1.4rem;">
    <div class="build red">
      <div class="bl">Academic Trap 🎓</div>
      <div class="mono" style="font-size:1.1rem; color:#ffb3b0; margin-top:.5rem;">let x = a * b;</div>
    </div>
    <div class="vs-badge">VS</div>
    <div class="build grn">
      <div class="bl">Industry Standard 🚀</div>
      <div class="mono" style="font-size:1.1rem; color:#abf0d0; margin-top:.5rem;">let totalBill = itemPrice * quantity;</div>
    </div>
  </div>
  <div class="tanglish-box grn reveal" style="margin-top:1.4rem;">
    <div class="tb-lbl">The 6-Month Naming Rule</div>
    <div class="tb-txt">"Un code-a 6 months kazhichu padicha unakkum puriyanum, team-ukum puriyanum!"</div>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> Naming conventions for code maintainability.""")

# Slide 28: Defensive Input Validation
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge red reveal"><i data-lucide="shield-alert"></i> SECTION 4 · BEST PRACTICE #2</div>
  <h2 class="reveal">Defensive Input Validation</h2>
  <div class="split even reveal" style="margin-top:1.4rem;">
    <div class="build red">
      <div class="bl">Academic Trap 🎓</div>
      <ul><li>Assuming user inputs are always 100% valid and formatted</li></ul>
    </div>
    <div class="vs-badge">VS</div>
    <div class="build grn">
      <div class="bl">Industry Standard 🚀</div>
      <ul><li>Strict boundary validation + graceful fallback defaults</li></ul>
    </div>
  </div>
  <div class="tanglish-box red reveal" style="margin-top:1.4rem;">
    <div class="tb-lbl">Resilience Rule</div>
    <div class="tb-txt">"User thappa input kudutha app crash aagakoodadhu."</div>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> Input validation and error bounds.""")

# Slide 29: Version Control & Git Branching
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue reveal"><i data-lucide="git-pull-request"></i> SECTION 4 · BEST PRACTICE #3</div>
  <h2 class="reveal">Version Control &amp; Git Branching</h2>
  <div class="split even reveal" style="margin-top:1.4rem;">
    <div class="build red">
      <div class="bl">Academic Trap 🎓</div>
      <div class="mono" style="font-size:1.05rem; color:#ffb3b0; margin-top:.5rem;">WhatsApp-la project_final_v2_final.zip send panradhu</div>
    </div>
    <div class="vs-badge">VS</div>
    <div class="build grn">
      <div class="bl">Industry Standard 🚀</div>
      <div class="mono" style="font-size:1.05rem; color:#abf0d0; margin-top:.5rem;">Git Feature Branching (feature/login) &amp; PR Reviews</div>
    </div>
  </div>
  <div class="tanglish-box cool reveal" style="margin-top:1.4rem;">
    <div class="tb-lbl">Git Branching Rule</div>
    <div class="tb-txt">"Main branch-a overwrite panni fight pannaama branch-la work pannedu."</div>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> Git feature branching vs zip file sharing.""")

# Slide 30: REST API Verbs
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge gold reveal"><i data-lucide="globe"></i> SECTION 4 · BEST PRACTICE #4</div>
  <h2 class="reveal">REST API Verbs &amp; Endpoint Contracts</h2>
  <table class="table-custom reveal">
    <thead><tr><th>HTTP Verb</th><th>Resource Endpoint</th><th>Industry Action Contract</th></tr></thead>
    <tbody>
      <tr><td>GET</td><td>/canteen/menu</td><td>Read / fetch resource data</td></tr>
      <tr><td>POST</td><td>/canteen/orders</td><td>Create new resource record</td></tr>
      <tr><td>PUT</td><td>/canteen/orders/102</td><td>Update existing resource record</td></tr>
      <tr><td>DELETE</td><td>/canteen/cart/5</td><td>Remove resource record</td></tr>
    </tbody>
  </table>
  <div class="tanglish-box reveal" style="margin-top:1.4rem;">
    <div class="tb-lbl">API Protocol Rule</div>
    <div class="tb-txt">"Saravana Bhavan-la order panra process maadhiri HTTP verbs-a strict-a handle pannanum."</div>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> REST API HTTP verb standards.""")

# Slide 31: Master Concept Summary Matrix Table
slides_html.append("""
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green reveal"><i data-lucide="grid"></i> SECTION 4 · MASTER SUMMARY MATRIX</div>
  <h2 class="reveal">Master Concept Summary Matrix</h2>
  <table class="table-custom reveal" style="font-size:clamp(.78rem, 1.1vw, .95rem);">
    <thead><tr><th>CS Concept</th><th>Industry Pattern</th><th>Real-Life Analogy</th><th>Key Metric / Tanglish Code</th></tr></thead>
    <tbody>
      <tr><td><b>Database Indexing</b></td><td>B-Tree Lookups</td><td>Trichy Bus Stand Alpha-Board</td><td class="mono">createIndex() (O(log n))</td></tr>
      <tr><td><b>Microservices</b></td><td>Distributed Systems</td><td>Multiplex Mall Independent Counters</td><td class="mono">Decoupled try/catch</td></tr>
      <tr><td><b>Load Balancing</b></td><td>Horizontal Scaling</td><td>Highway Multi-Lane Toll Plaza Gates</td><td class="mono">% backendServers.length</td></tr>
      <tr><td><b>Debouncing</b></td><td>Event Optimization</td><td>Typing Pause before Asking Teacher</td><td class="mono">clearTimeout & setTimeout</td></tr>
      <tr><td><b>Caching</b></td><td>Redis In-Memory</td><td>Thinnai Cooler Water Pot vs Well</td><td class="mono">redis.get() vs DB query</td></tr>
      <tr><td><b>Pub/Sub Queues</b></td><td>Event-Driven Broker</td><td>Dinakaran Newspaper Delivery Boy</td><td class="mono">broker.publish() & subscribe()</td></tr>
    </tbody>
  </table>
</section>
""")
notes.append("""<b>Speaker Point:</b> Master concept summary matrix.""")

# ====================================================
# SECTION 5: SEMINAR CLOSING & INTERACTIVE Q&A
# ====================================================

# Slide 32: Impostor Syndrome Reality Check
slides_html.append("""
<section class="slide center">
  <div class="glow-bg"></div>
  <div class="badge gold reveal"><i data-lucide="smile"></i> SECTION 5 · REAL TALK</div>
  <h2 class="reveal">The Impostor Syndrome Reality Check</h2>
  <blockquote class="lead reveal" style="margin-top:1.6rem;">"Senior developers syntax-a memory panni vechurukura superhumans illa bro. Avanga problem-a break panni, system structure-a design panni, Google-la enna search pannanum-nu purinjukutavanga!"</blockquote>
</section>
""")
notes.append("""<b>Speaker Point:</b> Senior developers search smart and design architecture.""")

# Slide 33: Developer Oath & Q&A
slides_html.append("""
<section class="slide center">
  <div class="glow-bg"></div>
  <div class="badge green reveal"><i data-lucide="heart"></i> SECTION 5 · CLOSING OATH</div>
  <h2 class="reveal">The Developer Oath</h2>
  <blockquote class="lead reveal" style="margin-top:1.4rem; font-size:1.35rem; text-align:left; border-left:3px solid var(--gold); padding-left:1.5rem;">
    "• Write code for humans to read, not just compilers to run.<br>
    • Test edge cases before production users find them.<br>
    • Build resilient fallback safety nets.<br>
    • Respect readability, the team, and the craft."
  </blockquote>
  <h3 class="reveal grad" style="margin-top:2rem;">Q &amp; A Session</h3>
</section>
""")
notes.append("""<b>Speaker Point:</b> Developer Oath and Q&A session.""")

# Slide 34: Seminar Feedback QR Slide
slides_html.append("""
<section class="slide center">
  <div class="glow-bg"></div>
  <div class="badge blue reveal"><i data-lucide="message-square"></i> SECTION 5 · SEMINAR FEEDBACK</div>
  <h2 class="reveal" style="font-size:clamp(2.4rem, 5.5vw, 4.8rem);">Share Your <span class="grad-cool">Feedback</span></h2>
  <img src="../../assets/qr_feedback_thinktg101.png" class="reveal" style="display:block; margin: 1.4rem auto; max-width: 250px; border-radius: 18px; border: 5px solid #ffffff; box-shadow: 0 20px 50px rgba(0,0,0,0.6);" alt="Feedback QR Code" />
  <p class="lead reveal" style="margin-top:1rem; font-size:clamp(1.05rem, 1.6vw, 1.35rem);">Scan the QR code to rate today's seminar session and share your thoughts with the RiseLabs team.</p>
  <p class="mono reveal" style="margin-top:.5rem; font-size:1.05rem; color:var(--gold-soft);">https://riselabs.one/events/feedback?code=THINKTG101</p>
</section>
""")
notes.append("""<b>Speaker Point:</b> Ask students to scan Feedback QR code.""")

# Slide 35: Certificate Download QR Slide (The Very Last Slide)
slides_html.append("""
<section class="slide center">
  <div class="glow-bg"></div>
  <div class="badge green reveal"><i data-lucide="award"></i> SECTION 5 · PARTICIPATION CERTIFICATE</div>
  <h2 class="reveal" style="font-size:clamp(2.4rem, 5.5vw, 4.8rem);">Claim Your <span class="grad-grn">Certificate</span></h2>
  <img src="../../assets/qr_certificate_thinktg101.png" class="reveal" style="display:block; margin: 1.4rem auto; max-width: 250px; border-radius: 18px; border: 5px solid #ffffff; box-shadow: 0 20px 50px rgba(0,0,0,0.6);" alt="Certificate QR Code" />
  <p class="lead reveal" style="margin-top:1rem; font-size:clamp(1.05rem, 1.6vw, 1.35rem);">Scan the QR code to instantly download your verified Seminar Participation Certificate.</p>
  <p class="mono reveal" style="margin-top:.5rem; font-size:1.05rem; color:var(--gold-soft);">https://riselabs.one/events/certificate?code=THINKTG101</p>
  <div class="tanglish-box grn reveal" style="max-width:550px; margin-left:auto; margin-right:auto; margin-top:.8rem;">
    <div class="tb-lbl">Certificate Callout</div>
    <div class="tb-txt">"Unga official certificate-a instant-ah download panni LinkedIn-la share pannedunga!"</div>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> Thank you everyone! Scan this final QR code to download your verified certificate.""")

# Footers & JavaScript logic
html_tail = """
</div>

<div class="chrome">
  <div class="brand">
    <span style="color:var(--gold); font-size:1.1em;">🎓</span>
    <span style="font-weight:600; letter-spacing:0.5px;">Think Like an Industry Developer</span>
  </div>
  <div class="right">
    <div class="notesbtn" id="notesbtn">S · Speaker Notes</div>
    <div class="counter"><span id="cur">01</span> / <span id="tot">...</span></div>
  </div>
</div>
<div class="hint"><span class="key">←</span><span class="key">→</span> navigate · <span class="key">S</span> speaker notes · <span class="key">F</span> fullscreen</div>

<div class="notes" id="notes">
  <div class="notes-head"><div class="lbl">Speaker Track & Tanglish Guidance</div><div class="x" id="notesx">&times;</div></div>
  <div class="notes-body" id="notesbody"></div>
</div>

<script>
const NOTES = """ + str(notes) + """;
const slides=[...document.querySelectorAll('.slide')];
const progress=document.getElementById('progress');
const cur=document.getElementById('cur');
const tot=document.getElementById('tot');
const notesEl=document.getElementById('notes');
const notesBody=document.getElementById('notesbody');
let i=0;

tot.textContent = slides.length;

function renderNotes(){
  notesBody.innerHTML = NOTES[i] || '<i>No notes for this slide.</i>';
  notesBody.scrollTop = 0;
}

function go(n){
  if(n<0||n>=slides.length) return;
  slides[i].classList.remove('active');
  slides[i].querySelectorAll('.step.revealed').forEach(el=>el.classList.remove('revealed'));
  slides[i].classList.add('prev');
  i=n;
  slides.forEach(s=>s.classList.remove('prev'));
  slides[i].classList.add('active');
  progress.style.width=((i+1)/slides.length*100)+'%';
  cur.textContent=String(i+1).padStart(2,'0');
  if(notesEl.classList.contains('open')) renderNotes();
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

function toggleNotes(){
  notesEl.classList.toggle('open');
  if(notesEl.classList.contains('open')) renderNotes();
}

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
  if(e.target.closest('.mod')||e.target.closest('a')||e.target.closest('.notes')||e.target.closest('.code-block')||e.target.closest('.code-box-clean'))return;
  e.clientX>innerWidth/2 ? next() : prev();
});

lucide.createIcons();
</script>
</body>
</html>
"""

output_path = os.path.join(PROJECT_ROOT, "HTML", "Industry Developer", "Think Like an Industry Developer - New Blueprint.html")

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_head + "\n".join(slides_html) + html_tail)

print(f"Successfully generated ultimate 36-slide presentation deck at:\n{output_path}")
