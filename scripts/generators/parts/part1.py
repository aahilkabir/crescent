import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

import json

slides_html = []
notes = []

# --- CSS AND SETUP (Using exact previous code) ---
slides_html.append("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Think Like an Industry Developer — Ultimate Keynote</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&family=Fira+Code:wght@400;500;700&display=swap');
    
    :root {
      --bg: #09090b;
      --fg: #fafafa;
      --dim: #a1a1aa;
      --border: #27272a;
      
      --accent: #3b82f6; /* Blue */
      --green: #10b981;
      --red: #ef4444;
      --gold: #f59e0b;
      --purple: #8b5cf6;
      --cyan: #06b6d4;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body, html {
      width: 100%; height: 100%;
      background: var(--bg);
      color: var(--fg);
      font-family: 'Inter', -apple-system, sans-serif;
      overflow: hidden; /* Hide scrollbars, managed by JS */
      font-size: 16px;
    }

    /* Deck Container */
    #deck {
      position: relative;
      width: 100%; height: 100%;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow: hidden;
    }

    /* Individual Slide */
    .slide {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: flex-start;
      padding: 6rem 8rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.4s ease, transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
      transform: translateY(40px); /* vertical slide in */
    }
    .slide.active {
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0);
    }
    .slide.center {
      align-items: center;
      text-align: center;
    }

    /* Typography */
    h1 {
      font-size: clamp(3rem, 7vw, 6rem);
      font-weight: 900;
      line-height: 1.1;
      letter-spacing: -0.04em;
      margin-bottom: 1.5rem;
    }
    h2 {
      font-size: clamp(2rem, 4vw, 3.5rem);
      font-weight: 800;
      line-height: 1.2;
      letter-spacing: -0.03em;
      margin-bottom: 2rem;
      color: var(--fg);
    }
    h3 {
      font-size: 2rem;
      font-weight: 700;
      color: var(--dim);
      margin-bottom: 1.5rem;
    }
    p, li, .sc-text {
      font-size: 1.7rem;
      line-height: 1.6;
      color: var(--dim);
      margin-bottom: 1.5rem;
      font-weight: 500;
    }
    .lead {
      font-size: 2rem;
      color: var(--fg);
    }

    /* Text Gradients */
    .grad { background: linear-gradient(135deg, #f59e0b, #fbbf24); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .grad-cool { background: linear-gradient(135deg, #3b82f6, #06b6d4); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .grad-red { background: linear-gradient(135deg, #ef4444, #f43f5e); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .grad-grn { background: linear-gradient(135deg, #10b981, #34d399); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .grad-purp { background: linear-gradient(135deg, #8b5cf6, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }

    /* Badges */
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.6rem 1rem;
      border-radius: 6px;
      font-size: 0.9rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      margin-bottom: 1.5rem;
      background: transparent;
    }
    .badge i { width: 16px; height: 16px; }
    .badge.gold { color: var(--gold); }
    .badge.blue { color: var(--accent); }
    .badge.red { color: var(--red); }
    .badge.green { color: var(--green); }
    .badge.purp { color: var(--purple); }

    /* Story Card */
    .story-card {
      background: #111113;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 2.5rem;
      width: 100%;
      max-width: 1000px;
      margin-top: 1rem;
      border-left: 4px solid var(--gold);
    }
    .story-card.cool { border-left-color: var(--accent); }
    .story-card.red { border-left-color: var(--red); }
    .story-card.grn { border-left-color: var(--green); }
    .story-card.purp { border-left-color: var(--purple); }
    
    .sc-title {
      font-size: 1.1rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--fg);
      margin-bottom: 1rem;
    }
    
    /* Code Box Clean */
    .code-box-clean {
      background: #000;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 2.5rem;
      width: 100%;
      max-width: 1000px;
      font-family: 'Fira Code', monospace;
      font-size: 1.4rem;
      line-height: 1.6;
      color: #e5e7eb;
      overflow-x: auto;
      margin-bottom: 1.5rem;
      border-top: 2px solid var(--gold);
    }
    .code-box-clean.cool { border-top-color: var(--accent); }
    .code-box-clean.red { border-top-color: var(--red); }
    .code-box-clean.grn { border-top-color: var(--green); }
    .code-box-clean.purp { border-top-color: var(--purple); }

    /* Syntax Highlighting */
    .kw { color: #c678dd; font-weight: 600; } /* keyword (purple) */
    .fn { color: #61afef; } /* function (blue) */
    .str { color: #98c379; } /* string (green) */
    .cm { color: #5c6370; font-style: italic; } /* comment (gray) */
    .num { color: #d19a66; } /* number (orange) */

    /* Highlight Line */
    .code-line { display: block; width: 100%; padding: 0.2rem 0; }
    .highlight-gold { background: rgba(245, 158, 11, 0.1); border-left: 3px solid var(--gold); padding-left: 1rem; margin-left: -1rem; }
    .highlight-blue { background: rgba(59, 130, 246, 0.1); border-left: 3px solid var(--accent); padding-left: 1rem; margin-left: -1rem; }
    .highlight-green { background: rgba(16, 185, 129, 0.1); border-left: 3px solid var(--green); padding-left: 1rem; margin-left: -1rem; }
    .highlight-red { background: rgba(239, 68, 68, 0.1); border-left: 3px solid var(--red); padding-left: 1rem; margin-left: -1rem; }
    .highlight-purp { background: rgba(139, 92, 246, 0.1); border-left: 3px solid var(--purple); padding-left: 1rem; margin-left: -1rem; }

    /* Tamil Mappings */
    .kw-mapping {
      background: #111;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 1.2rem 2rem;
      font-size: 1.2rem;
      color: var(--fg);
      display: inline-block;
      border-left: 3px solid var(--gold);
    }
    .kw-mapping.cool { border-left-color: var(--accent); }
    .kw-mapping.red { border-left-color: var(--red); }
    .kw-mapping.grn { border-left-color: var(--green); }
    .kw-mapping.purp { border-left-color: var(--purple); }
    .kw-mapping code { font-family: 'Fira Code', monospace; color: var(--dim); background: #000; padding: 2px 6px; border-radius: 4px; }

    /* Tables (Roadmap) */
    table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
    th, td { padding: 1.5rem 1rem; text-align: left; border-bottom: 1px solid var(--border); }
    th { font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--dim); }
    td { font-size: 1.2rem; font-weight: 500; }
    tr:last-child td { border-bottom: none; }

    /* Tanglish Code Box (Intro/Misc) */
    .tanglish-box {
      background: #111;
      border: 1px solid var(--border);
      padding: 2rem;
      border-radius: 12px;
      font-family: 'Fira Code', monospace;
      font-size: 1.4rem;
      line-height: 1.6;
      width: 100%;
      max-width: 900px;
      color: #e5e7eb;
      margin-top: 1rem;
    }

    /* Reveal Animation for inner elements */
    .reveal { opacity: 0; transform: translateY(15px); transition: opacity 0.5s ease, transform 0.5s ease; }
    .active .reveal { opacity: 1; transform: translateY(0); }
    .active .reveal:nth-child(1) { transition-delay: 0.1s; }
    .active .reveal:nth-child(2) { transition-delay: 0.2s; }
    .active .reveal:nth-child(3) { transition-delay: 0.3s; }
    .active .reveal:nth-child(4) { transition-delay: 0.4s; }
    .active .reveal:nth-child(5) { transition-delay: 0.5s; }
    .active .reveal:nth-child(6) { transition-delay: 0.6s; }
    
    /* Utility */
    .flex-row { display: flex; gap: 4rem; width: 100%; max-width: 1100px; align-items: stretch; margin-top: 1rem;}
    .flex-col { flex: 1; display: flex; flex-direction: column; }
    
    /* Progress Bar */
    #progress-bar {
      position: fixed; top: 0; left: 0; height: 2px;
      background: var(--gold);
      width: 0%; transition: width 0.3s ease;
      z-index: 100;
    }
  </style>
  <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
  <div id="progress-bar"></div>
  <div id="deck">
""")

# ====================================================
# SECTION 1: THE MINDSET SHIFT (Remains unchanged)
# ====================================================

# Slide 1: Title
slides_html.append("""
<section class="slide center">
  <div class="badge gold reveal"><i data-lucide="terminal"></i> MASTERCLASS KEYNOTE</div>
  <h1 class="reveal">Think Like an<br><span class="grad">Industry Developer</span></h1>
  <p class="lead reveal" style="margin-top: 1rem;">Bridging the gap between Academic Syntax and Production Reality</p>
  <div class="reveal" style="margin-top: 3rem; font-family: 'Fira Code'; color: var(--dim); font-size: 1.1rem;">
    $ execute masterclass.sh --lang=tanglish
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> Welcome everyone! Today is about breaking the academic bubble. We aren't just learning syntax; we are learning how to build systems that scale.""")

# Slide 2: The Problem
slides_html.append("""
<section class="slide">
  <div class="badge red reveal"><i data-lucide="alert-triangle"></i> THE REALITY</div>
  <h2 class="reveal">College expects <span class="grad-red">Outputs.</span><br>Industry expects <span class="grad-red">Outcomes.</span></h2>
  <div class="flex-row">
    <div class="flex-col reveal">
      <div style="background: #111; padding: 2rem; border-radius: 12px; border: 1px solid var(--border); height:100%;">
        <h3 style="color:var(--fg); font-size:1.3rem; margin-bottom:1rem; text-transform:uppercase;">Academic Mindset</h3>
        <p style="font-size:1.2rem; color:var(--dim);">"En code run aagudhu, output vandhuduchu!"</p>
        <ul style="list-style:none; margin-top:1.5rem; font-size:1.1rem;">
          <li style="margin-bottom:0.8rem;">❌ Hardcoded values</li>
          <li style="margin-bottom:0.8rem;">❌ Global variables everywhere</li>
          <li style="margin-bottom:0.8rem;">❌ Crashes on unexpected input</li>
        </ul>
      </div>
    </div>
    <div class="flex-col reveal">
      <div style="background: #111; padding: 2rem; border-radius: 12px; border: 1px solid var(--gold); height:100%;">
        <h3 style="color:var(--gold); font-size:1.3rem; margin-bottom:1rem; text-transform:uppercase;">Industry Mindset</h3>
        <p style="font-size:1.2rem; color:var(--dim);">"En code 10,000 users vandhalum crash aagadhu!"</p>
        <ul style="list-style:none; margin-top:1.5rem; font-size:1.1rem;">
          <li style="margin-bottom:0.8rem;">✅ Dynamic & Configurable</li>
          <li style="margin-bottom:0.8rem;">✅ Memory safe & Scoped</li>
          <li style="margin-bottom:0.8rem;">✅ Graceful Error Handling</li>
        </ul>
      </div>
    </div>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> In college, getting the right output is 100% of the grade. In the industry, it's only 10%. The rest is maintainability, safety, and scalability.""")

# Slide 3: The Syllabus
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="map"></i> THE ROADMAP</div>
  <h2 class="reveal">What we are unlocking today</h2>
  <div class="story-card reveal" style="max-width: 800px; padding: 2rem 3rem;">
    <ul style="list-style:none;">
      <li style="margin-bottom:1.5rem; display:flex; align-items:center; gap:1rem;">
        <div style="background:rgba(16, 185, 129, 0.1); color:var(--green); padding:0.5rem; border-radius:8px;"><i data-lucide="code-2"></i></div>
        <span style="color:var(--fg); font-size:1.4rem;"><b>Level 1:</b> Programming Fundamentals</span>
      </li>
      <li style="margin-bottom:1.5rem; display:flex; align-items:center; gap:1rem;">
        <div style="background:rgba(59, 130, 246, 0.1); color:var(--accent); padding:0.5rem; border-radius:8px;"><i data-lucide="cpu"></i></div>
        <span style="color:var(--fg); font-size:1.4rem;"><b>Level 2:</b> Memory & Data Architecture</span>
      </li>
      <li style="margin-bottom:1.5rem; display:flex; align-items:center; gap:1rem;">
        <div style="background:rgba(239, 68, 68, 0.1); color:var(--red); padding:0.5rem; border-radius:8px;"><i data-lucide="layers"></i></div>
        <span style="color:var(--fg); font-size:1.4rem;"><b>Level 3:</b> Advanced Concepts & OOP</span>
      </li>
      <li style="display:flex; align-items:center; gap:1rem;">
        <div style="background:rgba(139, 92, 246, 0.1); color:var(--purple); padding:0.5rem; border-radius:8px;"><i data-lucide="network"></i></div>
        <span style="color:var(--fg); font-size:1.4rem;"><b>Level 4:</b> System Design Architecture</span>
      </li>
    </ul>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> We will start from basic variables and logic, build up to how memory works, jump into OOP, and finish with Pro System Design.""")

# Slide 4: Secret Weapon
slides_html.append("""
<section class="slide center">
  <div class="badge blue reveal"><i data-lucide="lightbulb"></i> OUR SECRET WEAPON</div>
  <h2 class="reveal">How are we going to learn this?</h2>
  <h1 class="reveal grad-cool" style="margin-top: 1rem;">TANGLISH CODE</h1>
  <p class="lead reveal" style="margin-top: 1.5rem; max-width: 800px; line-height: 1.5;">
    Complex English programming terms are just simple everyday concepts disguised in fancy words. Let's decode them.
  </p>
</section>
""")
notes.append("""<b>Speaker Point:</b> Don't be intimidated by terms like Polymorphism or Recursion. We are going to map them to things you do every day in Tamil Nadu.""")

# Slide 5: Tanglish Demo
slides_html.append("""
<section class="slide">
  <div class="badge blue reveal"><i data-lucide="play-circle"></i> DEMO</div>
  <h2 class="reveal">Translating Logic to Life</h2>
  <div class="tanglish-box cool reveal">
    <span class="kw">let</span> pasi = <span class="num">true</span>;<br>
    <span class="kw">while</span> (pasi) {<br>
    &nbsp;&nbsp;<span class="fn">saapdu</span>(biryani);<br>
    &nbsp;&nbsp;<span class="kw">if</span> (vayiruFull) {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;pasi = <span class="num">false</span>;<br>
    &nbsp;&nbsp;}<br>
    }
  </div>
  <p class="reveal" style="margin-top:2rem; font-size:1.3rem; color:var(--fg);">
    If you understand this, you already understand <b>State Management</b> and <b>Event Loops</b>.
  </p>
</section>
""")
notes.append("""<b>Speaker Point:</b> You intuitively know logic. My job is to connect your real-world intuition to industry syntax.""")

# Slide 6: Transition to Level 1
slides_html.append("""
<section class="slide center">
  <div class="badge green reveal"><i data-lucide="check-circle"></i> MINDSET READY</div>
  <h2 class="reveal">Section 1 Complete!</h2>
  <p class="lead reveal" style="margin-top:1.4rem;">Next up: Let's start with Level 1 - Programming Fundamentals</p>
</section>
""")
notes.append("""<b>Speaker Point:</b> Transition from Intro to Level 1 (Fundamentals).""")

# ====================================================
# SECTION 2: PROGRAMMING FUNDAMENTALS (BEGINNER)
# Immutability, Scope, Conditionals, Safety Loops, Array Offsets, Functions
# ====================================================

# Slide 7: Section 2 Roadmap
slides_html.append("""
<section class="slide">
  <div class="badge green reveal"><i data-lucide="layers"></i> SECTION 2 · PROGRAMMING FUNDAMENTALS</div>
  <h2 class="reveal">Level 1: Building Blocks 🧱</h2>
  <div class="reveal" style="width:100%; max-width:900px; background:#111; border:1px solid var(--border); border-radius:12px; padding:1rem 2rem;">
    <table>
      <tr><th>#</th><th>Real World Story</th><th>Concept Name</th></tr>
      <tr><td>01</td><td>Hall Ticket vs Mobile Data Pack</td><td><b style="color:var(--green);">Immutability (Const/Let)</b></td></tr>
      <tr><td>02</td><td>Hostel Room Privacy vs Corridor</td><td><b style="color:var(--gold);">Variable Scope</b></td></tr>
      <tr><td>03</td><td>EA Cinema Gate Ticket Check</td><td><b style="color:var(--accent);">Conditionals (If/Else)</b></td></tr>
      <tr><td>04</td><td>Max Showroom Dress Trial Room</td><td><b style="color:var(--red);">Safety Loops</b></td></tr>
      <tr><td>05</td><td>Sathyam Cinemas Row A Seat Index</td><td><b style="color:var(--blue);">Array Offsets</b></td></tr>
      <tr><td>06</td><td>Swiggy Delivery Partner Subcontract</td><td><b style="color:var(--purple);">Functions & Delegation</b></td></tr>
    </table>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> These 6 are the fundamental building blocks of all logic. Let's go through them one by one.""")

# CONCEPT 01: IMMUTABILITY (Const vs Let)
# Story
slides_html.append("""
<section class="slide">
  <div class="badge green reveal"><i data-lucide="zap"></i> CONCEPT 01 · SUSPENSE STORY</div>
  <h2 class="reveal">Exam Hall Ticket vs Mobile Data Pack 📄</h2>
  <div class="story-card grn reveal">
    <div class="sc-title">Change vs Permanent Story</div>
    <div class="sc-text">
      Mobile data balance daily maariyite irukkum (Mutable). Aana unga exam hall ticket register number eppovume maaradhu (Immutable)! Code-layum indha maadhiri permanent values-a lock pannanum, illana theriyaama maathiduvom.
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Permanent vs changing variables.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge green reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">📄 Data Balance vs Register Number Code</h2>
  <div class="code-box-clean grn reveal">
    <span class="cm">// let = Data balance maarikite irukkum!</span><br>
    <span class="kw">let</span> mobileDataGB = <span class="num">2.0</span>;<br>
    <div class="code-line highlight-green">mobileDataGB = <span class="num">1.5</span>; <span class="cm">// Allowed! Value successfully updated.</span></div><br>
    <span class="cm">// const = Hall Ticket Register Number permanent!</span><br>
    <span class="kw">const</span> registerNumber = <span class="str">"20IT045"</span>;<br>
    registerNumber = <span class="str">"20IT099"</span>; <span class="cm">// 💥 Error! Cannot reassign a constant!</span>
  </div>
  <div class="kw-mapping grn reveal">
    🔑 <b>Tamil Mappings:</b> <code>let</code> = <b>மாறும் (Mutable)</b> | <code>const</code> = <b>மாறாது (Immutable)</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> let vs const.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge green reveal"><i data-lucide="award"></i> CONCEPT #01 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-grn" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">IMMUTABILITY</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Const vs Let / Permanent vs Modifiable)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> IMMUTABILITY.""")

# CONCEPT 02: VARIABLE SCOPE
# Story
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="zap"></i> CONCEPT 02 · SUSPENSE STORY</div>
  <h2 class="reveal">Hostel Room Privacy vs Public Corridor 🚪</h2>
  <div class="story-card reveal">
    <div class="sc-title">Hostel Room Scope Story</div>
    <div class="sc-text">
      Hostel public corridor-la vechurukka Water Purifier-a ellarum use pannalam (Global Scope). Aana unga private room-kulla irukka Snacks-a veliya irukkavanga edukka mudiyadhu (Local Scope)! Room-kulla lock aana variable veliya access aagadhu.
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Global vs Local Variable Scope.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🚪 Hostel Variable Scope Code</h2>
  <div class="code-box-clean reveal">
    <span class="kw">let</span> corridorWater = <span class="str">"Available to all!"</span>; <span class="cm">// Global Scope</span><br><br>
    <span class="kw">function</span> <span class="fn">myPrivateRoom</span>() {<br>
    <div class="code-line highlight-gold">&nbsp;&nbsp;<span class="kw">let</span> roomSnacks = <span class="str">"Only for me!"</span>; <span class="cm">// Local Scope (Locked inside)</span></div><br>
    &nbsp;&nbsp;<span class="fn">console.log</span>(corridorWater); <span class="cm">// Works! Can access global</span><br>
    }<br><br>
    <span class="fn">console.log</span>(roomSnacks); <span class="cm">// 💥 Error! Room snacks veliya kedaikadhu!</span>
  </div>
  <div class="kw-mapping reveal">
    🔑 <b>Tamil Mappings:</b> <code>Global Scope</code> = <b>பொதுவான இடம்</b> | <code>Local Scope</code> = <b>தனியார் அறை</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Global vs Local Scope code.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge gold reveal"><i data-lucide="award"></i> CONCEPT #02 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">VARIABLE SCOPE</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Global Public Access vs Local Block Privacy)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> VARIABLE SCOPE.""")

# CONCEPT 03: CONDITIONALS
# Story
slides_html.append("""
<section class="slide">
  <div class="badge blue reveal"><i data-lucide="zap"></i> CONCEPT 03 · SUSPENSE STORY</div>
  <h2 class="reveal">EA Cinema Gate Ticket Counter-la Check How It Works? 🎟️</h2>
  <div class="story-card cool reveal">
    <div class="sc-title">EA Cinema Security Gate Check</div>
    <div class="sc-text">
      FDFS A-rated movie-ku EA Mall gate-la nirkureenga.<br>
      <b>IF</b> Age &gt;= 18 <b>AND</b> QR Ticket is Valid ➔ Allow entry to Audi 1!<br>
      <b>ELSE</b> ➔ Divert to ticket refund counter!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> EA Cinema gate conditional check.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge blue reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🔀 EA Cinema Security Gate Code</h2>
  <div class="code-box-clean cool reveal">
    <span class="kw">function</span> <span class="fn">checkEntry</span>(age, ticketValid) {<br>
    <div class="code-line highlight-blue">&nbsp;&nbsp;<span class="kw">if</span> (age >= <span class="num">18</span> && ticketValid) {</div>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">openAudiDoor</span>();<br>
    &nbsp;&nbsp;} <span class="kw">else</span> {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">sendToRefundCounter</span>();<br>
    &nbsp;&nbsp;}<br>
    }
  </div>
  <div class="kw-mapping cool reveal">
    🔑 <b>Tamil Mappings:</b> <code>if</code> = <b>நிபந்தனை சரி என்றால்</b> | <code>else</code> = <b>இல்லை என்றால்</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Basic boolean conditionals.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge blue reveal"><i data-lucide="award"></i> CONCEPT #03 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-cool" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">CONDITIONALS</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Branching Logic &amp; Decision Making)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> CONDITIONALS.""")

# CONCEPT 04: SAFETY LOOPS
# Story
slides_html.append("""
<section class="slide">
  <div class="badge red reveal"><i data-lucide="zap"></i> CONCEPT 04 · SUSPENSE STORY</div>
  <h2 class="reveal">Max Showroom-la Unlimited Trial Panna Enna Aagum? 👗</h2>
  <div class="story-card red reveal">
    <div class="sc-title">Dress Trial Memory Leak</div>
    <div class="sc-text">
      Max showroom: <code>while (wantToTry) { tryNextDress(); }</code>. Customer "Stop!" nu sollama trial room-la continuous-a dress try panna, queue perusaagi mall traffic jam aagum! CPU 100% lockup aagi server crash aagum!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Max showroom dress trial infinite loop memory leak.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge red reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🔁 Max Dress Trial Safety Trap Code</h2>
  <div class="code-box-clean red reveal">
    <span class="cm">// Dress pudikira varai try pannu...</span><br>
    <span class="kw">while</span> (dressPudikala) {<br>
    &nbsp;&nbsp;<span class="fn">tryNextDress</span>();<br>
    <div class="code-line highlight-red">&nbsp;&nbsp;<span class="cm">// Safety Check: 5 dress mela try panna, veliya anuppidu! (Server safety!)</span><br>
    &nbsp;&nbsp;<span class="kw">if</span> (dressTryCount > <span class="num">5</span>) <span class="kw">break</span>; <span class="cm">// Safety Trap Break!</span></div><br>
    }
  </div>
  <div class="kw-mapping red reveal">
    🔑 <b>Tamil Mappings:</b> <code>while</code> = <b>இருக்கும் வரை</b> | <code>break</code> = <b>நிறுத்து</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Safety bounds on while loops.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge red reveal"><i data-lucide="award"></i> CONCEPT #04 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-red" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">SAFETY LOOPS</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Infinite Loop Prevention &amp; Bounds Checking)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> SAFETY LOOPS.""")

# CONCEPT 05: ARRAY OFFSETS
# Story
slides_html.append("""
<section class="slide">
  <div class="badge blue reveal"><i data-lucide="zap"></i> CONCEPT 05 · SUSPENSE STORY</div>
  <h2 class="reveal">Sathyam Cinemas Row A Seat Index 0 Endha Edam? 🍿</h2>
  <div class="story-card cool reveal">
    <div class="sc-title">Theater Seat Offset Story</div>
    <div class="sc-text">
      Array is a continuous block of memory boxes. Adhu Sathyam Cinemas Row A maadhiri! <code>['Door', 'Kamal', 'Rajini', 'Vijay']</code>.<br>
      Index 0-na "1st Person" illa! Adhu Door Entrance-la irundhu 0 steps distance! Index 1 = 1 step offset (Kamal). Index 2 = 2 steps offset (Rajini).
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Theater seat door offset indexing.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge blue reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🧵 Sathyam Cinemas Offset Code</h2>
  <div class="code-box-clean cool reveal">
    <span class="kw">const</span> sathyamRowA = [<span class="str">'Door'</span>, <span class="str">'Kamal'</span>, <span class="str">'Rajini'</span>, <span class="str">'Vijay'</span>];<br><br>
    <div class="code-line highlight-blue"><span class="cm">// Index 0 = Door entrance-la irundhu 0 steps distance!</span><br>
    <span class="kw">let</span> frontSeat = sathyamRowA[<span class="num">0</span>]; <span class="cm">// Answer: 'Door'</span></div>
    <span class="cm">// Index 2 = Door entrance-la irundhu 2 steps thalli utkaruradhu!</span><br>
    <span class="kw">let</span> massSeat = sathyamRowA[<span class="num">2</span>]; <span class="cm">// Answer: 'Rajini'</span>
  </div>
  <div class="kw-mapping cool reveal">
    🔑 <b>Tamil Mapping:</b> <code>sathyamRow[0]</code> = <b>வாசலில் இருந்து 0 அடிகள் தொலைவு</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Zero-based array indexing.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge blue reveal"><i data-lucide="award"></i> CONCEPT #05 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-cool" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">ARRAY OFFSETS</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Zero-Based Indexing &amp; Memory Pointers)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> ARRAY OFFSETS.""")

# CONCEPT 06: FUNCTIONS & DELEGATION
# Story
slides_html.append("""
<section class="slide">
  <div class="badge purp reveal"><i data-lucide="zap"></i> CONCEPT 06 · SUSPENSE STORY</div>
  <h2 class="reveal">Namma Samachu Saapduradha, Swiggy-la Order Panna Enna Difference? 🛵</h2>
  <div class="story-card purp reveal">
    <div class="sc-title">Swiggy Delivery Partner Story</div>
    <div class="sc-text">
      Nammale samachal main thread block aagidum (naama vera vela paaka mudiyadhu). Adhuve Swiggy-la order pottu, <b>"Address = Chennai, Item = Biryani"</b> nu argument pass panna... Swiggy partner (Function) velaya mudichu food-a return pannuvaaru! Naama rest edukalam!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Swiggy delivery partner as a function.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge purp reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🛵 Swiggy Order Function Code</h2>
  <div class="code-box-clean purp reveal">
    <span class="cm">// Function = Sub-contractor taking arguments</span><br>
    <div class="code-line highlight-purp"><span class="kw">function</span> <span class="fn">swiggyOrder</span>(item, location) {</div>
    &nbsp;&nbsp;<span class="fn">findRestaurant</span>(item, location);<br>
    &nbsp;&nbsp;<span class="kw">return</span> <span class="str">"Hot Food Delivered!"</span>; <span class="cm">// Result back to you</span><br>
    }<br><br>
    <span class="cm">// Main program calls the function</span><br>
    <span class="kw">let</span> dinner = <span class="fn">swiggyOrder</span>(<span class="str">"Biryani"</span>, <span class="str">"T-Nagar"</span>);
  </div>
  <div class="kw-mapping purp reveal">
    🔑 <b>Tamil Mappings:</b> <code>function</code> = <b>ஏற்றுக்கொள்ளப்பட்ட வேலை</b> | <code>return</code> = <b>முடிந்த வேலையின் பலன்</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Passing arguments and receiving returns from functions.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge purp reveal"><i data-lucide="award"></i> CONCEPT #06 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-purp" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">FUNCTIONS</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Code Delegation, Parameters &amp; Return Values)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> FUNCTIONS.""")
