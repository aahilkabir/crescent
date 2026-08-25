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
# SECTION 2: COMPUTER ENGINE UNDER THE HOOD (STACK, HEAP, RECURSION, BIG O)
# ====================================================

# CONCEPT 08: RAM MEMORY LOCKERS
# Story
slides_html.append("""
<section class="slide">
  <div class="badge blue reveal"><i data-lucide="zap"></i> CONCEPT 08 · SUSPENSE STORY</div>
  <h2 class="reveal">Central Station Cloakroom-la Token Kidaicha Box Enge? 🧳</h2>
  <div class="story-card cool reveal">
    <div class="sc-title">Cloakroom Token vs Locker Box Story</div>
    <div class="sc-text">
      RAM (Random Access Memory) is the temporary workspace of the computer. Adhu central station cloakroom maadhiri! Bag-a vetchu Token #0x7FFF vaangureenga. Variable name (<code>appaKuduthaKasu</code>) is just the paper token tag! Real 500 Rupees value sits inside physical RAM Locker Address <code>0x7FFF</code>.
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> RAM Cloakroom Locker Address.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge blue reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🧳 RAM Address Locker Code</h2>
  <div class="code-box-clean cool reveal">
    <span class="cm">// Variable Name = Cloakroom-la kudutha Token Tag (appaKuduthaKasu)</span><br>
    <div class="code-line highlight-blue"><span class="kw">let</span> appaKuduthaKasu = <span class="num">500</span>; <span class="cm">// Physical RAM Locker Address: 0x7FFF</span></div><br>
    <span class="cm">// CPU Address Bus Token #0x7FFF-a look up panni 500 Rupees-a fetch pannum!</span>
  </div>
  <div class="kw-mapping cool reveal">
    🔑 <b>Tamil Mappings:</b> <code>variable</code> = <b>டோக்கன் அடையாளம்</b> | <code>RAM Address</code> = <b>மெமரி பெட்டி</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Variables pointing to RAM locker addresses.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge blue reveal"><i data-lucide="award"></i> CONCEPT #08 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-cool" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">RAM MEMORY LOCKERS</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Variables as Pointers to Physical Memory Address Lockers)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> RAM MEMORY LOCKERS.""")



# CONCEPT 10: STACK MEMORY
# Story
slides_html.append("""
<section class="slide">
  <div class="badge green reveal"><i data-lucide="zap"></i> CONCEPT 10 · SUSPENSE STORY</div>
  <h2 class="reveal">Mess Meal Thattu Stack-la Keela irukura Thattu-a Edukka Mudiyuma? 🍽️</h2>
  <div class="story-card grn reveal">
    <div class="sc-title">Hostel Mess Plate Stack Story</div>
    <div class="sc-text">
      Stack Memory is a fast, temporary memory for executing functions. Adhu Hostel Mess-la irukka clean plate stack maadhiri! Mela vacha plate-a dhaan instant-a edukka mudiyum (Last In, First Out). Fixed size memory, function return aana odane automatic-a pop cleanup!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Stack Memory LIFO plate stack.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge green reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🍽️ Stack Memory LIFO Push/Pop Code</h2>
  <div class="code-box-clean grn reveal">
    <span class="kw">function</span> <span class="fn">calculateCollegeFee</span>() {<br>
    <div class="code-line highlight-green">&nbsp;&nbsp;<span class="kw">let</span> tutionFee = <span class="num">45000</span>; <span class="cm">// Stack-la Top Plate-a Push aagudhu!</span><br>
    &nbsp;&nbsp;<span class="kw">return</span> tutionFee; <span class="cm">// Function mudinjadhum Stack Pop cleanup!</span></div><br>
    }<br><br>
    <span class="fn">calculateCollegeFee</span>(); <span class="cm">// Stack Push -> Execute -> Stack Pop</span>
  </div>
  <div class="kw-mapping grn reveal">
    🔑 <b>Tamil Mappings:</b> <code>Push</code> = <b>தட்டை வைப்பது</b> | <code>Pop</code> = <b>தட்டை எடுப்பது</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Stack pushes and pops on function execution.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge green reveal"><i data-lucide="award"></i> CONCEPT #10 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-grn" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">STACK MEMORY</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(LIFO Fast Execution Memory with Automatic Cleanup)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> STACK MEMORY.""")


# CONCEPT 11: HEAP MEMORY & GC
# Story
slides_html.append("""
<section class="slide">
  <div class="badge purp reveal"><i data-lucide="zap"></i> CONCEPT 11 · SUSPENSE STORY</div>
  <h2 class="reveal">Express Avenue Mall Store Room & Automatic Sweeper 🧹</h2>
  <div class="story-card purp reveal">
    <div class="sc-title">Mall Store Room & Sweeper Story</div>
    <div class="sc-text">
      Big objects (like a user list) Stack-la vekka mudiyadhu (too heavy). Adha Heap (Mall Store Room) la poduvom. Yaarachum point pannitu irundha safe. Ellarum adha use pandradha stop pannita, Garbage Collector (Automatic Sweeper) vandhu clean pannidum!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Heap memory and Garbage collection.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge purp reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🧹 Heap Allocation & Garbage Collector Code</h2>
  <div class="code-box-clean purp reveal">
    <span class="kw">let</span> heavyData = { name: <span class="str">"Big File"</span>, size: <span class="str">"1GB"</span> }; <span class="cm">// Heap-la allocate aachu!</span><br><br>
    <div class="code-line highlight-purp"><span class="cm">// User close pannitaaru, variable disconnect aagidchu!</span><br>
    heavyData = <span class="num">null</span>; <span class="cm">// Reference disconnected! No one points to it.</span></div><br>
    <span class="cm">// Garbage Collector Background-la vandhu 1GB-a clean pannidum! 🧹✨</span>
  </div>
  <div class="kw-mapping purp reveal">
    🔑 <b>Tamil Mappings:</b> <code>Heap</code> = <b>குடோன்</b> | <code>Garbage Collector</code> = <b>துப்புரவு பணியாளர்</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Heap objects and nullifying references for GC.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge purp reveal"><i data-lucide="award"></i> CONCEPT #11 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-purp" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">HEAP MEMORY &amp; GC</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Dynamic Storage for Large Objects &amp; Automatic Cleanup)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> HEAP MEMORY & GC.""")


# CONCEPT 15: CALL STACK & RECURSION
# Story
slides_html.append("""
<section class="slide">
  <div class="badge red reveal"><i data-lucide="zap"></i> CONCEPT 15 · SUSPENSE STORY</div>
  <h2 class="reveal">Kalyana Parisu Box-kulla Innoru Box, Adhukulla Innoru Box! 🎁</h2>
  <div class="story-card red reveal">
    <div class="sc-title">Nested Wedding Gift Box Story</div>
    <div class="sc-text">
      Kalyanathula oru periya gift box kudukuranga. Open panna ulla innoru box! Adha open panna innoru box! Kadaisiya oru chinna box-la iPhone irukku (Base Condition). Idhu dhaan Recursion! Oru function adhaye thirumba thirumba call pannikum, untill it finds the iPhone!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Recursion nested gift box.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge red reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🎁 Recursion &amp; Base Condition Code</h2>
  <div class="code-box-clean red reveal">
    <span class="kw">function</span> <span class="fn">openGiftBox</span>(boxLevel) {<br>
    <div class="code-line highlight-red">&nbsp;&nbsp;<span class="cm">// Base Condition: Stop check illati Stack Overflow!</span><br>
    &nbsp;&nbsp;<span class="kw">if</span> (boxLevel === <span class="num">0</span>) <span class="kw">return</span> <span class="str">"🔥 iPhone Gift Found!"</span>;</div><br>
    &nbsp;&nbsp;<span class="cm">// Recursive Call: Function-a thaniyae call pannudhu</span><br>
    &nbsp;&nbsp;<span class="kw">return</span> <span class="fn">openGiftBox</span>(boxLevel - <span class="num">1</span>);<br>
    }
  </div>
  <div class="kw-mapping red reveal">
    🔑 <b>Tamil Mappings:</b> <code>recursion</code> = <b>சுய அழைப்பு</b> | <code>base condition</code> = <b>நிறுத்தும் விதி</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Recursion call stack and base case.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge red reveal"><i data-lucide="award"></i> CONCEPT #15 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-red" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">CALL STACK &amp; RECURSION</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Self-Calling Functions &amp; Base Condition Safety Gates)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> CALL STACK & RECURSION.""")


# CONCEPT 17: BIG O SCALABILITY
# Story
slides_html.append("""
<section class="slide">
  <div class="badge green reveal"><i data-lucide="zap"></i> CONCEPT 17 · SUSPENSE STORY</div>
  <h2 class="reveal">Metro Turnstile Tap O(1) vs. Bus Stand Search O(n) 🚉</h2>
  <div class="story-card grn reveal">
    <div class="sc-title">Metro Gate vs Passenger Search Story</div>
    <div class="sc-text">
      Metro card tap: 10,000 per kootam irundhalum 0.001s-la gate open aagum (O(1)). Aana 5,000 crowd-la passenger-a item-by-item search panna time scale aagum (O(n))!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Metro card tap efficiency vs linear search.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge green reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🚉 Big O Efficiency Code</h2>
  <div class="code-box-clean grn reveal">
    <div class="code-line highlight-green"><span class="cm">// O(1) Constant Time (Metro Tap - Super Fast!)</span><br>
    <span class="kw">let</span> entry = metroGate[<span class="str">"Card_99"</span>]; <span class="cm">// Instant lookup</span></div><br>
    <span class="cm">// O(n) Linear Time (Bus Stand Search - Slow!)</span><br>
    <span class="kw">for</span> (<span class="kw">let</span> passenger <span class="kw">of</span> crowd) {<br>
    &nbsp;&nbsp;<span class="kw">if</span> (passenger.name === <span class="str">"Kamal"</span>) <span class="kw">return</span> <span class="str">"Found!"</span>; <span class="cm">// Checks every single one</span><br>
    }
  </div>
  <div class="kw-mapping grn reveal">
    🔑 <b>Tamil Mappings:</b> <code>O(1)</code> = <b>உடனடி (Instant)</b> | <code>O(n)</code> = <b>கூட்டத்திற்கு ஏற்ப நேரம் ஆகும்</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> O(1) constant time vs O(n) linear time.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge green reveal"><i data-lucide="award"></i> CONCEPT #17 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-grn" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">BIG O SCALABILITY</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Algorithmic Efficiency &amp; Computational Complexity)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> BIG O SCALABILITY.""")


# ====================================================
# SECTION 3: 13 CORE CS CONCEPTS IN TANGLISH
# ====================================================

# Foundations Roadmap Part 1 (Concepts 1 - 5)
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="layers"></i> SECTION 3 · FOUNDATIONS ROADMAP (1 - 5)</div>
  <h2 class="reveal">Concepts 1 to 5</h2>
  <div class="reveal" style="width:100%; max-width:900px; background:#111; border:1px solid var(--border); border-radius:12px; padding:1rem 2rem;">
    <table>
      <tr><th>#</th><th>Real World Story</th><th>Concept Name</th></tr>
      <tr><td>01</td><td>A.R. Rahman Concert Sound Board</td><td><b style="color:var(--gold);">Abstraction</b></td></tr>
      <tr><td>02</td><td>Vijay Movie Base Template Reuse</td><td><b style="color:var(--blue);">Inheritance</b></td></tr>
      <tr><td>03</td><td>Sathyam Cinemas Row A Seat Index</td><td><b style="color:var(--accent);">Array Offsets</b></td></tr>
      <tr><td>04</td><td>Swiggy Delivery Partner Subcontract</td><td><b style="color:var(--green);">Functions</b></td></tr>
      <tr><td>05</td><td>Exam Hall Ticket vs Mobile Data</td><td><b style="color:var(--purple);">Immutability</b></td></tr>
    </table>
  </div>
</section>
""")
notes.append("""<b>Foundations Roadmap:</b> Concepts 1 through 5 overview table.""")


# CONCEPT 1: ABSTRACTION
# Story
slides_html.append("""
<section class="slide">
  <div class="badge cyan reveal"><i data-lucide="zap"></i> CONCEPT 1 · SUSPENSE STORY</div>
  <h2 class="reveal">A.R. Rahman Keyboard-la Volume Slider Mattum Dhane Irukku? 🎹</h2>
  <div class="story-card cool reveal">
    <div class="sc-title">Concert Sound Board Story</div>
    <div class="sc-text">
      A.R. Rahman keyboard-la "Bass Increase" panna ore oru slider thaan irukkum. Aana ulla 100+ wires, circuits run aagum! User-ku theva illadha complex wiring-a hide pannitu, verum clean UI slider-a matum kudukuradhu dhaan Abstraction!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Sound board abstraction.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge cyan reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🎹 A.R. Rahman Console Code</h2>
  <div class="code-box-clean cool reveal">
    <div class="code-line highlight-blue"><span class="cm">// User sees only this Simple Public Method! (The Slider)</span><br>
    arrRahmanConsole.<span class="fn">increaseBassVolume</span>();</div><br>
    <span class="cm">// Inside the black box (Hidden from user):</span><br>
    <span class="kw">private function</span> <span class="fn">_increaseBassVolume</span>() {<br>
    &nbsp;&nbsp;<span class="fn">connectCircuit</span>(freq40Hz);<br>
    &nbsp;&nbsp;<span class="fn">boostVoltage</span>(1.5);<br>
    &nbsp;&nbsp;<span class="fn">syncWithSpeakers</span>();<br>
    }
  </div>
  <div class="kw-mapping cool reveal">
    🔑 <b>Tamil Mappings:</b> <code>Abstraction</code> = <b>சிக்கலை மறைத்து எளிமையை தருதல்</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Hiding complex private logic behind a simple public method.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge cyan reveal"><i data-lucide="award"></i> CONCEPT #01 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-cool" style="font-size:clamp(3.5rem, 8vw, 7.2rem); margin-top:0.6rem; letter-spacing:-.03em;">ABSTRACTION</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Hiding Complex Internal Wiring Behind Simple APIs)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> ABSTRACTION.""")


# CONCEPT 2: INHERITANCE
# Story
slides_html.append("""
<section class="slide">
  <div class="badge purp reveal"><i data-lucide="zap"></i> CONCEPT 2 · SUSPENSE STORY</div>
  <h2 class="reveal">Thalapathy Vijay Padam Intro Ellame Ore Base Template Dhane? 🕶️</h2>
  <div class="story-card purp reveal">
    <div class="sc-title">Mass Hero Intro Story</div>
    <div class="sc-text">
      Vijay padathula Intro Scene-na: Slow motion walk, Anirudh BGM, Sunglass remove! Idhu oru Base Template (Parent Class). GOAT, Leo, Master nu endha padam eduthalum, indha base template-a copy pannitu (Inherit), konjam puthusa add pannikuvanga (Child Class)!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Vijay movie mass intro template.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge purp reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🕶️ Mass Hero Template Code</h2>
  <div class="code-box-clean purp reveal">
    <span class="kw">class</span> DirectorMassHero {<br>
    &nbsp;&nbsp;<span class="fn">slowMotionWalk</span>() { <span class="fn">playBGM</span>(); }<br>
    }<br><br>
    <div class="code-line highlight-purp"><span class="cm">// GOAT Padam reuses the parent's base logic without rewriting!</span><br>
    <span class="kw">class</span> GOAT_Thalapathy <span class="kw">extends</span> DirectorMassHero {</div><br>
    &nbsp;&nbsp;<span class="fn">deagingEffect</span>() { <span class="cm">/* new specific GOAT feature */</span> }<br>
    }
  </div>
  <div class="kw-mapping purp reveal">
    🔑 <b>Tamil Mappings:</b> <code>extends</code> = <b>பண்புகளை பெற்றுக்கொள் (Inherit)</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Class inheritance using extends.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge purp reveal"><i data-lucide="award"></i> CONCEPT #02 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-purp" style="font-size:clamp(3.5rem, 8vw, 7.2rem); margin-top:0.6rem; letter-spacing:-.03em;">INHERITANCE</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Reusing Parent Code Blueprints in Child Classes)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> INHERITANCE.""")


# CONCEPT 3: ARRAY OFFSETS
# Story
slides_html.append("""
<section class="slide">
  <div class="badge blue reveal"><i data-lucide="zap"></i> CONCEPT 3 · SUSPENSE STORY</div>
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
  <div class="badge blue reveal"><i data-lucide="award"></i> CONCEPT #03 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-cool" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">ARRAY OFFSETS</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Zero-Based Indexing &amp; Memory Pointers)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> ARRAY OFFSETS.""")


# CONCEPT 4: FUNCTIONS & DELEGATION
# Story
slides_html.append("""
<section class="slide">
  <div class="badge purp reveal"><i data-lucide="zap"></i> CONCEPT 4 · SUSPENSE STORY</div>
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
  <div class="badge purp reveal"><i data-lucide="award"></i> CONCEPT #04 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-purp" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">FUNCTIONS</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Code Delegation, Parameters &amp; Return Values)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> FUNCTIONS.""")


# CONCEPT 5: IMMUTABILITY (Const vs Let)
# Story
slides_html.append("""
<section class="slide">
  <div class="badge green reveal"><i data-lucide="zap"></i> CONCEPT 5 · SUSPENSE STORY</div>
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
  <div class="badge green reveal"><i data-lucide="award"></i> CONCEPT #05 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-grn" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">IMMUTABILITY</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Const vs Let / Permanent vs Modifiable)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> IMMUTABILITY.""")


# Foundations Roadmap Part 2 (Concepts 6 - 10)
slides_html.append("""
<section class="slide">
  <div class="badge red reveal"><i data-lucide="layers"></i> SECTION 3 · FOUNDATIONS ROADMAP (6 - 10)</div>
  <h2 class="reveal">Concepts 6 to 10</h2>
  <div class="reveal" style="width:100%; max-width:900px; background:#111; border:1px solid var(--border); border-radius:12px; padding:1rem 2rem;">
    <table>
      <tr><th>#</th><th>Real World Story</th><th>Concept Name</th></tr>
      <tr><td>06</td><td>5L Bisleri Can in 200ml Tea Glass</td><td><b style="color:var(--red);">Type Overflow</b></td></tr>
      <tr><td>07</td><td>EA Cinema Gate Ticket Check</td><td><b style="color:var(--gold);">Conditionals</b></td></tr>
      <tr><td>08</td><td>Max Showroom Dress Trial Room</td><td><b style="color:var(--blue);">Safety Loops</b></td></tr>
      <tr><td>09</td><td>Marina Beach Token Parking</td><td><b style="color:var(--green);">Hash Maps</b></td></tr>
      <tr><td>10</td><td>Tagore Canteen UPS Fallback</td><td><b style="color:var(--purple);">Error Traps</b></td></tr>
    </table>
  </div>
</section>
""")
notes.append("""<b>Foundations Roadmap:</b> Concepts 6 through 10 overview table.""")


# CONCEPT 6: TYPE OVERFLOW
# Story
slides_html.append("""
<section class="slide">
  <div class="badge red reveal"><i data-lucide="zap"></i> CONCEPT 6 · SUSPENSE STORY</div>
  <h2 class="reveal">5L Bisleri Can Thanni-a 200ml Tea Glass-la Oothuna? 🌊</h2>
  <div class="story-card red reveal">
    <div class="sc-title">Water Overflow Story</div>
    <div class="sc-text">
      Computer memory is exactly like containers! Oru 200ml tea glass-la (<code>int8</code> = Max 127) poi 5L Bisleri can thanni-a (value = 300) oothuna enna aagum? Veliya kotti chithari waste aagum! Adhu thaan Memory Type Overflow!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Water overflow analogy for data types.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge red reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🌊 200ml Tea Glass Overflow Code</h2>
  <div class="code-box-clean red reveal">
    <span class="cm">// 8-bit Integer = 200ml Tea Glass (Max capacity holds upto 127)</span><br>
    <div class="code-line highlight-red"><span class="kw">let</span> teaGlass: <span class="kw">int8</span> = <span class="num">120</span>;</div>
    teaGlass = teaGlass + <span class="num">10</span>; <span class="cm">// 120 + 10 = 130! (Crosses 127 limit!)</span><br><br>
    <span class="cm">// 💥 BOOM! Overflow Error / Wraps around to negative numbers!</span><br>
    <span class="fn">console.log</span>(teaGlass); <span class="cm">// Output: -126 (Data Corrupted!)</span>
  </div>
  <div class="kw-mapping red reveal">
    🔑 <b>Tamil Mappings:</b> <code>Data Type</code> = <b>பாத்திரம்</b> | <code>Overflow</code> = <b>வழிந்து சிந்துதல்</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Type limits and overflow.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge red reveal"><i data-lucide="award"></i> CONCEPT #06 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-red" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">TYPE OVERFLOW</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Memory Container Capacity Exceeded Disasters)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> TYPE OVERFLOW.""")

# END OF PART 2


# CONCEPT 7: CONDITIONALS
# Story
slides_html.append("""
<section class="slide">
  <div class="badge blue reveal"><i data-lucide="zap"></i> CONCEPT 7 · SUSPENSE STORY</div>
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
  <div class="badge blue reveal"><i data-lucide="award"></i> CONCEPT #07 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-cool" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">CONDITIONALS</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Branching Logic &amp; Decision Making)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> CONDITIONALS.""")


# CONCEPT 8: SAFETY LOOPS
# Story
slides_html.append("""
<section class="slide">
  <div class="badge red reveal"><i data-lucide="zap"></i> CONCEPT 8 · SUSPENSE STORY</div>
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
  <div class="badge red reveal"><i data-lucide="award"></i> CONCEPT #08 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-red" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">SAFETY LOOPS</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Infinite Loop Prevention &amp; Bounds Checking)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> SAFETY LOOPS.""")


# CONCEPT 9: HASH MAPS
# Story
slides_html.append("""
<section class="slide">
  <div class="badge blue reveal"><i data-lucide="zap"></i> CONCEPT 9 · SUSPENSE STORY</div>
  <h2 class="reveal">Marina Beach-la 10,000 Vandi Irukku, Un Vandi Enga Irukku? 🏍️</h2>
  <div class="story-card cool reveal">
    <div class="sc-title">Marina Parking Token Story</div>
    <div class="sc-text">
      Marina beach parking-la 10,000 vandi irukku. Nee un vandi theda maatay! "Token #45 = Pillar B". Direct-a Pillar B poi vandi eduppay (Key-Value Pair). Idhu dhaan Hash Map (O(1) Speed)! Search panna theva illa, direct access.
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Marina Beach Token Parking (Key-Value lookup).""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge blue reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🏍️ Marina Parking Hash Map Code</h2>
  <div class="code-box-clean cool reveal">
    <span class="cm">// Dictionary (Hash Map): Key = Token Number, Value = Location</span><br>
    <span class="kw">let</span> marinaParking = {<br>
    &nbsp;&nbsp;<span class="str">"Token_10"</span>: <span class="str">"Pillar A"</span>,<br>
    &nbsp;&nbsp;<span class="str">"Token_45"</span>: <span class="str">"Pillar B"</span><br>
    };<br><br>
    <div class="code-line highlight-blue"><span class="cm">// No looping! Direct O(1) Instant Access!</span><br>
    <span class="kw">let</span> myBikeLocation = marinaParking[<span class="str">"Token_45"</span>]; <span class="cm">// "Pillar B"</span></div>
  </div>
  <div class="kw-mapping cool reveal">
    🔑 <b>Tamil Mappings:</b> <code>Key</code> = <b>டோக்கன்</b> | <code>Value</code> = <b>பைக் இருக்கும் இடம்</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Key-Value mappings for O(1) instant lookups.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge blue reveal"><i data-lucide="award"></i> CONCEPT #09 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-cool" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">HASH MAPS</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(O(1) Instant Key-Value Dictionary Lookups)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> HASH MAPS.""")


# CONCEPT 10: DEFENSIVE ERROR TRAPS
# Story
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="zap"></i> CONCEPT 10 · SUSPENSE STORY</div>
  <h2 class="reveal">Tagore Canteen-la Current Ponaal Enna Aagum? 💡</h2>
  <div class="story-card reveal">
    <div class="sc-title">UPS Generator Fallback Story</div>
    <div class="sc-text">
      Tagore canteen-la current cut aagidchu! Current cut aana udane (Error Throw), automatic-a UPS Generator on aagi light eriyum (Catch Block). Enna aanaalum paravala, kadaisiya bill potruvaanga (Finally Block)!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Tagore Canteen UPS generator fallback (Try/Catch).""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">💡 UPS Fallback Generator Code</h2>
  <div class="code-box-clean reveal">
    <span class="kw">try</span> {<br>
    &nbsp;&nbsp;<span class="fn">runMainPowerLine</span>(); <span class="cm">// Try keeping the lights on</span><br>
    } <span class="kw">catch</span> (currentCutError) {<br>
    <div class="code-line highlight-gold">&nbsp;&nbsp;<span class="cm">// Oh no! Error aagidchu! Fallback to Generator!</span><br>
    &nbsp;&nbsp;<span class="fn">turnOnUPSGenerator</span>(); </div><br>
    } <span class="kw">finally</span> {<br>
    &nbsp;&nbsp;<span class="fn">collectMoneyForFood</span>(); <span class="cm">// Eppudiyum idhu run aagum!</span><br>
    }
  </div>
  <div class="kw-mapping reveal">
    🔑 <b>Tamil Mappings:</b> <code>try/catch</code> = <b>முயற்சி செய் / தவறினால் மாற்று வழி தேடு</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Try, Catch, and Finally blocks for error handling.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge gold reveal"><i data-lucide="award"></i> CONCEPT #10 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">DEFENSIVE ERROR TRAPS</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Try / Catch / Finally Fallback Resilience)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> DEFENSIVE ERROR TRAPS.""")


# CONCEPT 11: VARIABLE SCOPE
# Story
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="zap"></i> CONCEPT 11 · SUSPENSE STORY</div>
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
  <div class="badge gold reveal"><i data-lucide="award"></i> CONCEPT #11 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">VARIABLE SCOPE</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Global Public Access vs Local Block Privacy)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> VARIABLE SCOPE.""")


# CONCEPT 12: PASS-BY-REFERENCE
# Story
slides_html.append("""
<section class="slide">
  <div class="badge accent reveal"><i data-lucide="zap"></i> CONCEPT 12 · SUSPENSE STORY</div>
  <h2 class="reveal">Xerox Copy Kudukuradha illa Original Key Kudukuradha? 🔑</h2>
  <div class="story-card cool reveal">
    <div class="sc-title">Assignment Notes vs Bike Key Story</div>
    <div class="sc-text">
      Friend assignment notes ketta, Xerox eduthu kudupom. Avan adha kizhichalum namma original safe (Pass-by-Value). Aana Bike ketta, Original Key kudupom! Avan petrol gaali panna namma vandi-layum gaali (Pass-by-Reference)!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Pass-by-Value vs Pass-by-Reference.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge accent reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🔑 Xerox vs Original Key Code</h2>
  <div class="code-box-clean cool reveal">
    <span class="cm">// Primitive: Pass-by-Value (Xerox Copy)</span><br>
    <span class="kw">let</span> enNotes = <span class="str">"Maths"</span>;<br>
    <span class="kw">let</span> friendNotes = enNotes; <span class="cm">// Creates a Xerox copy</span><br>
    friendNotes = <span class="str">"Torn!"</span>; <span class="cm">// enNotes is still "Maths"</span><br><br>
    <span class="cm">// Object: Pass-by-Reference (Original Bike Key)</span><br>
    <span class="kw">let</span> enBike = { petrol: <span class="num">100</span> };<br>
    <div class="code-line highlight-blue"><span class="kw">let</span> friendBike = enBike; <span class="cm">// Handing over the SAME Original Key!</span><br>
    friendBike.petrol = <span class="num">0</span>; <span class="cm">// 💥 En bike-layum petrol gaali!</span></div>
  </div>
  <div class="kw-mapping cool reveal">
    🔑 <b>Tamil Mappings:</b> <code>Value</code> = <b>ஜெராக்ஸ் காப்பி</b> | <code>Reference</code> = <b>அசல் சாவி</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Primitive values vs Object references.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge accent reveal"><i data-lucide="award"></i> CONCEPT #12 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-cool" style="font-size:clamp(3.5rem, 8vw, 7.2rem); margin-top:0.6rem; letter-spacing:-.03em;">PASS-BY-REFERENCE</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Independent Xerox Copies vs Shared Pointer Addresses)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> PASS-BY-REFERENCE.""")


# CONCEPT 13: QUEUES (FIFO)
# Story
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="zap"></i> CONCEPT 13 · SUSPENSE STORY</div>
  <h2 class="reveal">Kumar Canteen Token Line-la Yaaru First Povaa? 🎫</h2>
  <div class="story-card reveal">
    <div class="sc-title">Kumar Canteen Billing Line FIFO Story</div>
    <div class="sc-text">
      Kumar canteen token counter-la munnadi nirkuravar dhaan first bill pottu veliya povaar. Pinnadi vara aal line-oda last-la dhaan nippaar! (First In, First Out). Stack-oda exact opposite!
    </div>
  </div>
</section>
""")
notes.append("""<b>Story Setup:</b> Kumar Canteen Queue FIFO.""")

# Code
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="code-2"></i> TANGLISH CODE REVEAL</div>
  <h2 class="reveal">🎫 Kumar Canteen Queue FIFO Code</h2>
  <div class="code-box-clean reveal">
    <span class="kw">let</span> tokenLine = [];<br><br>
    <div class="code-line highlight-gold"><span class="cm">// Enqueue: Line-la pinnadi poi nillu (Push to end)</span><br>
    tokenLine.<span class="fn">push</span>(<span class="str">"Kamal"</span>);<br>
    tokenLine.<span class="fn">push</span>(<span class="str">"Rajini"</span>); <span class="cm">// Line: [Kamal, Rajini]</span></div><br>
    <span class="cm">// Dequeue: First aalu bill pottutu veliya povaar (Shift from front)</span><br>
    <span class="kw">let</span> servedPerson = tokenLine.<span class="fn">shift</span>(); <span class="cm">// Kamal gets served!</span>
  </div>
  <div class="kw-mapping reveal">
    🔑 <b>Tamil Mappings:</b> <code>Enqueue</code> = <b>வரிசையில் சேர்</b> | <code>Dequeue</code> = <b>வரிசையில் இருந்து வெளியேறு</b>
  </div>
</section>
""")
notes.append("""<b>Code Walkthrough:</b> Array push (enqueue) and shift (dequeue) for queues.""")

# Reveal
slides_html.append("""
<section class="slide center">
  <div class="badge gold reveal"><i data-lucide="award"></i> CONCEPT #13 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad" style="font-size:clamp(3.8rem, 9vw, 8rem); margin-top:0.6rem; letter-spacing:-.03em;">QUEUES (FIFO)</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(First-In, First-Out Sequential Processing lines)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> QUEUES (FIFO).""")


# ====================================================
# SECTION 5: SYSTEM DESIGN & REAL-WORLD APPS
# Database Indexing, Microservices, Load Balancing, Debouncing, Caching, Pub/Sub
# ====================================================

# Slide 51: Intro to System Design
slides_html.append("""
<section class="slide center">
  <div class="badge purple reveal"><i data-lucide="server"></i> SECTION 5 COMPLETE</div>
  <h2 class="reveal">Foundations & Architecture Locked In!</h2>
  <p class="lead reveal" style="margin-top:1.4rem;">Next up: Let's scale it to 1 Million Users with System Design.</p>
</section>
""")
notes.append("""<b>Speaker Point:</b> Transition to Section 5 System Design.""")

# SYSTEM DESIGN CONCEPTS (from previous script, mapped exactly)

# 19. DATABASE INDEXING (from previous script Concept 11)
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="database"></i> PRO CONCEPT 19</div>
  <h2 class="reveal">Trichy Bus Stand-la Thanjavur Bus Enga Nikkum? 🚌</h2>
  <div class="story-card reveal">
    <div class="sc-text">
      Trichy bus stand-la 100 buses irukku. Ovvoru bus kittayum poi "Nee Thanjavur poriya?" nu keta time waste. Adhukku bathila Board paapom: "Bay 5 = Thanjavur". Direct-a Bay 5 polam! Adhu dhaan <b>Database Indexing</b>.
    </div>
  </div>
</section>
<section class="slide center">
  <div class="badge gold reveal"><i data-lucide="award"></i> PRO CONCEPT #19 REVEAL</div>
  <h1 class="reveal grad">DATABASE INDEXING</h1>
  <p class="kicker reveal" style="margin-top:1rem; font-size:1.25rem;">(Creating Lookup Tables to Prevent Full-Table Scans)</p>
</section>
""")

# 20. MICROSERVICES (from previous script Concept 12)
slides_html.append("""
<section class="slide">
  <div class="badge blue reveal"><i data-lucide="boxes"></i> PRO CONCEPT 20</div>
  <h2 class="reveal">Saravana Bhavan-la Oru Master Dhaan Ellam Samaippara? 👨‍🍳</h2>
  <div class="story-card cool reveal">
    <div class="sc-text">
      Oru aalu Dosa, Idli, Meals, Juice ellam pota (Monolith), avaru sick aana whole hotel close! Adhukku bathila Dosa Master, Parotta Master, Juice Master nu thani thaniya vecha (Microservices), Parotta Master leave potalum Juice kedaikum!
    </div>
  </div>
</section>
<section class="slide center">
  <div class="badge blue reveal"><i data-lucide="award"></i> PRO CONCEPT #20 REVEAL</div>
  <h1 class="reveal grad-cool">MICROSERVICES</h1>
  <p class="kicker reveal" style="margin-top:1rem; font-size:1.25rem;">(Splitting Monoliths into Independent Functional Nodes)</p>
</section>
""")

# 21. LOAD BALANCING (from previous script Concept 13)
slides_html.append("""
<section class="slide">
  <div class="badge green reveal"><i data-lucide="git-merge"></i> PRO CONCEPT 21</div>
  <h2 class="reveal">Tirupati Darshan-la Yean Kootathula Free-a Poraanga? 🙏</h2>
  <div class="story-card grn reveal">
    <div class="sc-text">
      Tirupati temple-la 1 lakh per vandha ore line-la vida maattanga. Oru Traffic Police ninnu Q1, Q2, Q3 nu aala pirichu anuppuvaar. Oru line full aana, adutha line-ku divert pannuvar. Adhu dhaan <b>Load Balancer</b>!
    </div>
  </div>
</section>
<section class="slide center">
  <div class="badge green reveal"><i data-lucide="award"></i> PRO CONCEPT #21 REVEAL</div>
  <h1 class="reveal grad-grn">LOAD BALANCING</h1>
  <p class="kicker reveal" style="margin-top:1rem; font-size:1.25rem;">(Distributing Traffic Across Multiple Server Nodes)</p>
</section>
""")

# 22. DEBOUNCING (from previous script Concept 14)
slides_html.append("""
<section class="slide">
  <div class="badge red reveal"><i data-lucide="mouse-pointer-click"></i> PRO CONCEPT 22</div>
  <h2 class="reveal">Lift Button-a 100 Thadava Amukkuna Lift Fast-a Varuma? 🛗</h2>
  <div class="story-card red reveal">
    <div class="sc-text">
      Chinna pasanga lift button-a spam pannikite irupanga (10 clicks/sec). Aana Lift logic eppadi? "Nee evlo thadava spam pannalum, nee amukki mudichu 2 seconds wait pannu, appo dhaan naan call edupen". Idhu dhaan <b>Debouncing & Throttling</b>.
    </div>
  </div>
</section>
<section class="slide center">
  <div class="badge red reveal"><i data-lucide="award"></i> PRO CONCEPT #22 REVEAL</div>
  <h1 class="reveal grad-red">DEBOUNCING & THROTTLING</h1>
  <p class="kicker reveal" style="margin-top:1rem; font-size:1.25rem;">(Preventing API Spam by Delaying or Limiting Function Execution)</p>
</section>
""")

# 23. IN-MEMORY CACHING (from previous script Concept 15)
slides_html.append("""
<section class="slide">
  <div class="badge purp reveal"><i data-lucide="cpu"></i> PRO CONCEPT 23</div>
  <h2 class="reveal">Exam Hall-la Book Thurandhu Paapoma illa Memory-la Irundha? 🧠</h2>
  <div class="story-card purp reveal">
    <div class="sc-text">
      Question paper kedaichadhum Library (Database) poi book thedina late aagum (Disk I/O Slow). Adhuku pathila already padicha answer-a short-term Memory (Cache) la vechurundha instant-a ezhudhalam! Redis & Memcached work like this.
    </div>
  </div>
</section>
<section class="slide center">
  <div class="badge purp reveal"><i data-lucide="award"></i> PRO CONCEPT #23 REVEAL</div>
  <h1 class="reveal grad-purp">IN-MEMORY CACHING</h1>
  <p class="kicker reveal" style="margin-top:1rem; font-size:1.25rem;">(Storing High-Read Data in RAM for Ultra-Fast Retrieval)</p>
</section>
""")

# 24. PUB/SUB MESSAGE QUEUES (from previous script Concept 16)
slides_html.append("""
<section class="slide">
  <div class="badge cyan reveal"><i data-lucide="message-square"></i> PRO CONCEPT 24</div>
  <h2 class="reveal">Kalyana Pathirikai Ellarukkum Thani Thaniya Kudukuradha? 💌</h2>
  <div class="story-card cool reveal">
    <div class="sc-text">
      1000 peruku thani thaniya message anuppuna time waste. Adhuku bathila oru WhatsApp Group (Topic) create panni oru message potta, andha group-la yaarellam Subscribe pannirukkangalo avangaluku ellam broadcast aagidum! Idhu dhaan Kafka Pub/Sub!
    </div>
  </div>
</section>
<section class="slide center">
  <div class="badge cyan reveal"><i data-lucide="award"></i> PRO CONCEPT #24 REVEAL</div>
  <h1 class="reveal grad-cool">PUB / SUB QUEUES</h1>
  <p class="kicker reveal" style="margin-top:1rem; font-size:1.25rem;">(Publish/Subscribe Asynchronous Event Broadcasting)</p>
</section>
""")


# ====================================================
# SECTION 6: CAREER, CRAFT & CLOSING
# ====================================================

# Slide: Senior Dev Reality
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="star"></i> THE CRAFT</div>
  <h2 class="reveal">Senior Developers aren't geniuses.<br>They just handle failures gracefully.</h2>
  <div class="story-card reveal">
    <ul style="list-style:none;">
      <li style="margin-bottom:1.5rem; color:var(--fg); display:flex; gap:1rem;"><i data-lucide="check" style="color:var(--green);"></i> They write code that anticipates missing data.</li>
      <li style="margin-bottom:1.5rem; color:var(--fg); display:flex; gap:1rem;"><i data-lucide="check" style="color:var(--green);"></i> They design systems that don't crash when servers go down.</li>
      <li style="display:flex; gap:1rem; color:var(--fg);"><i data-lucide="check" style="color:var(--green);"></i> They use Tamil/English/Any analogy to understand complex systems!</li>
    </ul>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> Being a senior dev isn't about memorizing syntax. It's about system resilience and clear mental models.""")

# Slide: Impostor Syndrome
slides_html.append("""
<section class="slide center">
  <div class="badge red reveal"><i data-lucide="heart"></i> REAL TALK</div>
  <h2 class="reveal">Impostor Syndrome is a Feature, not a Bug.</h2>
  <p class="lead reveal" style="max-width: 800px; margin-top:1rem;">If you feel like you don't know everything, it means you are in an industry that evolves every day. You are exactly where you need to be.</p>
</section>
""")
notes.append("""<b>Speaker Point:</b> Everyone feels impostor syndrome. Embrace it as proof of your growth.""")

# Slide: Wrap Up
slides_html.append("""
<section class="slide center">
  <h1 class="reveal grad">Thank You!</h1>
  <p class="lead reveal" style="margin-bottom: 3rem;">Keep coding. Keep translating logic to life.</p>
  <div class="reveal" style="font-family: 'Fira Code'; color: var(--dim); font-size: 1.2rem; background: #111; padding: 1rem 2rem; border: 1px solid var(--border); border-radius: 8px;">
    exit(0); <span class="cm">// Successfully compiled your mindset!</span>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> Thank you everyone! Keep building!""")


# --- ENGINE & JS INJECTION ---
slides_html.append("""
  </div> <!-- end #deck -->
  
  <script>
    const slides = document.querySelectorAll('.slide');
    const progressBar = document.getElementById('progress-bar');
    let currentSlide = 0;

    function showSlide(index) {
      if(index < 0) index = 0;
      if(index >= slides.length) index = slides.length - 1;
      
      slides.forEach((slide, i) => {
        if(i === index) {
          slide.classList.add('active');
        } else {
          slide.classList.remove('active');
        }
      });
      
      currentSlide = index;
      progressBar.style.width = ((currentSlide + 1) / slides.length) * 100 + '%';
      window.location.hash = currentSlide;
    }

    // Keyboard Navigation
    window.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
        showSlide(currentSlide + 1);
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        showSlide(currentSlide - 1);
      }
    });

    // Init based on URL hash
    const initialSlide = parseInt(window.location.hash.replace('#', '')) || 0;
    showSlide(initialSlide);
  </script>
</body>
</html>
""")

# Write exactly to the requested HTML file
output_filename = "Think Like an Industry Developer.html"
with open(output_filename, "w", encoding="utf-8") as f:
    f.write("\\n".join(slides_html))

print(f"Successfully generated {len(slides_html)} HTML fragments -> {output_filename}")
print("Presentation compiled successfully!")

