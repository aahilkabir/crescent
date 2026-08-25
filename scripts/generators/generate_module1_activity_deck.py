# -*- coding: utf-8 -*-
import os, sys
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)


output_filename = "GEE 1102 - Design Thinking Module 1 Activity Deck.html"

html_head = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>GEE 1102 — Design Thinking (Module 1 Activity Deck: 22 Case Studies)</title>
<script src="https://unpkg.com/lucide@latest"></script>
<style>
:root{
  --bg:#07080b;
  --bg2:#0f1117;
  --ink:#f8fafc;
  --dim:#94a3b8;
  --dimmer:#64748b;
  --accent:#f59e0b;
  --accent-soft:rgba(245, 158, 11, 0.15);
  --blue:#38b6ff;
  --blue-soft:rgba(56, 182, 255, 0.15);
  --green:#10b981;
  --green-soft:rgba(16, 185, 129, 0.15);
  --purple:#a855f7;
  --purple-soft:rgba(168, 85, 247, 0.15);
  --rose:#f43f5e;
  --rose-soft:rgba(244, 63, 94, 0.15);
  --line:rgba(255,255,255,.10);
  --card:rgba(255,255,255,.04);
}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{height:100%;background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"SF Pro Display","SF Pro Text","Inter","Helvetica Neue",sans-serif;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;overflow:hidden;}
.deck{position:fixed;inset:0;}
.slide{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;
  padding:3.5vh 5.0vw;opacity:0;transform:scale(1.02);
  transition:opacity .4s cubic-bezier(.22,.61,.36,1),transform .4s cubic-bezier(.22,.61,.36,1);pointer-events:none;}
.slide.active{opacity:1;transform:scale(1);pointer-events:auto;}
.slide.prev{transform:scale(.98);}
.slide.center{align-items:center;text-align:center;}
.slide.center .lead{margin-left:auto;margin-right:auto;}

/* Step-by-Step Reveal Animation */
.step {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity 0.35s cubic-bezier(.22,.61,.36,1), transform 0.35s cubic-bezier(.22,.61,.36,1);
  pointer-events: none;
}
.step.revealed {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

/* Subtle Ambient Glow Behind Headers */
.glow-bg {
  position: absolute;
  width: 750px;
  height: 750px;
  background: radial-gradient(circle, rgba(245, 158, 11, 0.08) 0%, rgba(56, 182, 255, 0.05) 50%, transparent 70%);
  top: 25%;
  left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
  z-index: 0;
}

/* Unified Clean Badge System */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 1.1rem;
  border-radius: 100px;
  font-size: clamp(0.8rem, 1.1vw, 1.0rem);
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 0.7rem;
  width: fit-content;
  background: rgba(255, 255, 255, 0.06);
  color: var(--ink);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.badge.accent { background: var(--accent-soft); color: var(--accent); border-color: rgba(245, 158, 11, 0.35); }
.badge.blue { background: var(--blue-soft); color: var(--blue); border-color: rgba(56, 182, 255, 0.35); }
.badge.green { background: var(--green-soft); color: var(--green); border-color: rgba(16, 185, 129, 0.35); }
.badge.purple { background: var(--purple-soft); color: var(--purple); border-color: rgba(168, 85, 247, 0.35); }
.badge.rose { background: var(--rose-soft); color: var(--rose); border-color: rgba(244, 63, 94, 0.35); }

/* AUDITORIUM-LEVEL HERO TYPOGRAPHY */
h1{font-size:clamp(2.8rem, 6.0vw, 5.0rem);font-weight:900;letter-spacing:-.03em;line-height:1.06;color:#ffffff;}
h2{font-size:clamp(2.0rem, 4.0vw, 3.2rem);font-weight:800;letter-spacing:-.025em;line-height:1.12;color:#ffffff;}
h3{font-size:clamp(1.3rem, 2.4vw, 1.9rem);font-weight:700;letter-spacing:-.02em;line-height:1.2;color:#ffffff;}

.lead{font-size:clamp(1.1rem, 1.7vw, 1.45rem);font-weight:400;color:#cbd5e1;line-height:1.5;max-width:78ch;}

.grad{background:linear-gradient(120deg,#ffffff,#fef3c7 60%,var(--accent));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.grad-cool{background:linear-gradient(120deg,#ffffff,#e0f2fe 60%,var(--blue));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.grad-green{background:linear-gradient(120deg,#ffffff,#d1fae5 60%,var(--green));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.grad-purple{background:linear-gradient(120deg,#ffffff,#f3e8ff 60%,var(--purple));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;}
.mono{font-family:"SF Mono",ui-monospace,Menlo,monospace;font-size:0.9em;color:var(--accent);font-weight:700;}

/* CASE STUDY WORKSHEET CARDS GRID */
.split{display:grid;grid-template-columns:1fr 1fr;gap:clamp(1.2rem, 2.5vw, 2.0rem);align-items:stretch;width:100%;}
.grid-4{display:grid;grid-template-columns:1fr 1fr;gap:1.0rem;width:100%;margin-top:0.8rem;}

.ws-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  padding: 1.2rem 1.4rem;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}
.ws-card.highlight {
  border-color: rgba(245, 158, 11, 0.35);
  background: rgba(245, 158, 11, 0.05);
}
.ws-card.cool-hl {
  border-color: rgba(56, 182, 255, 0.35);
  background: rgba(56, 182, 255, 0.05);
}
.ws-card.green-hl {
  border-color: rgba(16, 185, 129, 0.35);
  background: rgba(16, 185, 129, 0.05);
}
.ws-card.purple-hl {
  border-color: rgba(168, 85, 247, 0.35);
  background: rgba(168, 85, 247, 0.05);
}

.ws-label {
  font-size: clamp(0.75rem, 1.0vw, 0.9rem);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  font-weight: 800;
  color: var(--accent);
  margin-bottom: 0.4rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}
.ws-label.blue { color: var(--blue); }
.ws-label.green { color: var(--green); }
.ws-label.purple { color: var(--purple); }

.ws-title {
  font-size: clamp(1.1rem, 1.8vw, 1.4rem);
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 0.3rem;
}
.ws-body {
  font-size: clamp(0.95rem, 1.3vw, 1.15rem);
  line-height: 1.45;
  color: #cbd5e1;
}
.ws-body b { color: #ffffff; }

/* SOCRATIC "THINK" PROMPT & OPTIONS CARDS */
.think-box {
  background: rgba(255, 255, 255, 0.04);
  border-left: 5px solid var(--accent);
  border-radius: 0 16px 16px 0;
  padding: 1.2rem 1.6rem;
  margin-top: 0.8rem;
}
.think-box.cool { border-left-color: var(--blue); }
.think-box.green { border-left-color: var(--green); }
.think-box.purple { border-left-color: var(--purple); }

.hero-quote-card {
  background: rgba(245, 158, 11, 0.06);
  border: 2px solid rgba(245, 158, 11, 0.4);
  border-radius: 18px;
  padding: 1.2rem 1.8rem;
  margin-top: 0.9rem;
  text-align: center;
}
.hero-quote-card.cool { border-color: rgba(56, 182, 255, 0.4); background: rgba(56, 182, 255, 0.06); }
.hero-quote-card.green { border-color: rgba(16, 185, 129, 0.4); background: rgba(16, 185, 129, 0.06); }
.hero-quote-card.purple { border-color: rgba(168, 85, 247, 0.4); background: rgba(168, 85, 247, 0.06); }

.hero-quote-title {
  font-size: clamp(0.75rem, 1.0vw, 0.95rem);
  font-weight: 800;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 0.4rem;
}
.hero-quote-card.cool .hero-quote-title { color: var(--blue); }
.hero-quote-card.green .hero-quote-title { color: var(--green); }
.hero-quote-card.purple .hero-quote-title { color: var(--purple); }

.hero-quote-text {
  font-size: clamp(1.2rem, 2.2vw, 1.8rem);
  font-weight: 800;
  line-height: 1.35;
  color: #ffffff;
}

/* REGIONAL TIP CALLOUT */
.regional-tip {
  background: rgba(255, 255, 255, 0.03);
  border-left: 3px solid rgba(255, 255, 255, 0.2);
  border-radius: 0 12px 12px 0;
  padding: 0.5rem 0.9rem;
  margin-top: 0.6rem;
}
.regional-tip .rt-lbl { font-size: 0.7rem; letter-spacing: 0.12em; text-transform: uppercase; font-weight: 700; color: var(--dim); margin-bottom: 0.2rem; }
.regional-tip .rt-txt { font-size: clamp(0.85rem, 1.1vw, 1.05rem); font-style: italic; color: #cbd5e1; }

/* MATRIX TABLE FOR SELECTION */
.matrix-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 0.8rem;
  font-size: clamp(0.8rem, 1.1vw, 0.95rem);
}
.matrix-table th {
  background: rgba(255, 255, 255, 0.08);
  color: var(--accent);
  padding: 0.6rem 0.8rem;
  text-align: left;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border: 1px solid rgba(255, 255, 255, 0.12);
}
.matrix-table td {
  padding: 0.55rem 0.8rem;
  border: 1px solid rgba(255, 255, 255, 0.08);
  color: #e2e8f0;
}
.matrix-table tr:nth-child(even) { background: rgba(255, 255, 255, 0.02); }

/* FOOTER CHROME */
.chrome {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  height: 48px;
  background: rgba(7, 8, 11, 0.65);
  backdrop-filter: blur(12px);
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 2.0rem;
  z-index: 100;
  font-size: 0.86rem;
  color: var(--dim);
}
.chrome .brand { display: flex; align-items: center; gap: 0.6rem; font-weight: 500; color: #cbd5e1; }
.chrome .brand b { color: #ffffff; font-weight: 700; }
.chrome .right { display: flex; align-items: center; gap: 1.5rem; }
.notesbtn {
  background: transparent;
  color: #94a3b8;
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 0.35rem 0.9rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  font-size: 0.8rem;
  transition: all 0.2s ease;
}
.notesbtn:hover { background: rgba(255, 255, 255, 0.08); color: #fff; border-color: rgba(255, 255, 255, 0.25); }
.counter { font-family: "SF Mono", monospace; font-weight: 700; color: var(--accent); font-size:1.0rem; }

/* SINGLE ACCENT PROGRESS LINE */
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: var(--accent);
  z-index: 101;
  transition: width 0.3s ease;
}

.notes {
  position: fixed;
  bottom: 48px;
  right: 2.0rem;
  width: 480px;
  max-height: 380px;
  background: rgba(15, 17, 23, 0.96);
  backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 16px 16px 0 0;
  padding: 1.2rem;
  z-index: 99;
  display: none;
  flex-direction: column;
  box-shadow: 0 -10px 40px rgba(0,0,0,0.7);
}
.notes.open { display: flex; }
.notes-head { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.6rem; margin-bottom: 0.8rem; }
.notes-head .lbl { font-size: 0.8rem; letter-spacing: 0.12em; text-transform: uppercase; font-weight: 800; color: var(--accent); }
.notes-head .x { cursor: pointer; color: var(--dim); font-size: 1.2rem; font-weight: 700; }
.notes-body { font-size: 0.9rem; line-height: 1.55; color: #cbd5e1; overflow-y: auto; }
</style>
</head>
<body>

<div class="progress-bar" id="progress"></div>

<div class="deck" id="deck">
"""

# Slides definitions and Speaker Notes tracking
slides = []
notes = []

def add_slide(slide_html, note_text):
    slides.append(slide_html)
    notes.append(note_text)

# SLIDE 1: Title Slide
s1 = """
<section class="slide center active">
  <div class="glow-bg"></div>
  <div class="badge accent"><i data-lucide="layers"></i> GEE 1102 · DESIGN THINKING · MODULE 1 CASE STUDY DECK</div>
  <h1>Module 1 <span class="grad">Case Study Masterclass</span></h1>
  <p class="lead" style="margin-top:0.8rem;">22 Real-World Brand Innovations Analyzed Across Customer-Centricity, Solution Types &amp; User Personas</p>
  <div class="step" style="margin-top:1.2rem; background:rgba(255,255,255,0.04); border:1px solid rgba(255,255,255,0.12); padding:0.8rem 1.8rem; border-radius:14px; display:inline-block;">
    <p style="font-weight:700; color:var(--accent); font-size:1.1rem;">Interactive Group Activity &amp; Worksheet Reference Deck</p>
    <p style="font-size:0.9rem; color:var(--dim); margin-top:0.2rem;">Netflix · Uber · Spotify · Apple · GE Healthcare · Tesla · Starbucks · IKEA &amp; More</p>
  </div>
  <div class="think-box cool step" style="max-width:780px; margin-top:1.2rem; text-align:left;">
    <div style="font-size:0.8rem; letter-spacing:0.15em; text-transform:uppercase; font-weight:800; color:var(--blue);"><i data-lucide="user-check"></i> Course Instructor Attribution</div>
    <div style="font-size:1.1rem; font-weight:600; color:#fff; margin-top:0.3rem;"><b>Kabir</b> · Professor of Practice, Department of Computer Science<br>BS Abdur Rahman Crescent Institute of Science and Technology</div>
  </div>
</section>
"""
n1 = "<b>Slide 1 Speaker Notes:</b> Welcome students! Today we are applying Module 1 concepts (Customer-Centricity, Product/Process/System/Software, Persona Development, Opportunity Identification) to 22 real-world company case studies. Student groups will select 1 topic to analyze on their worksheet."
add_slide(s1, n1)

# SLIDE 2: Worksheet Framework Overview
s2 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue"><i data-lucide="file-text"></i> GROUP ACTIVITY INSTRUCTIONS</div>
  <h2>The 4-Step <span class="grad-cool">Module 1 Worksheet</span></h2>
  <p class="lead">Every group picks ONE company topic and completes this 4-step analysis framework:</p>
  
  <div class="grid-4 step" style="margin-top:1.2rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="cpu"></i> Step 1: Solution Type</div>
      <div class="ws-title">Classify Core Innovation</div>
      <div class="ws-body">Identify if the solution is primarily a <b>Product</b> (tangible item), <b>Process</b> (method/workflow), <b>System</b> (interconnected network), or <b>Software</b> (digital code).</div>
    </div>
    
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> Step 2: Target Persona</div>
      <div class="ws-title">Define Human Profile</div>
      <div class="ws-body">Detail <b>Name &amp; Profile</b> (e.g. Sarah, 28, traveler), <b>User Goal</b> (what they accomplish), and <b>Core Frustration</b> (emotion/friction).</div>
    </div>

    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> Step 3: Identify Opportunity</div>
      <div class="ws-title">Exact Moment of Pivot</div>
      <div class="ws-body">State the precise micro-moment of human friction where the company intervened to transform the experience.</div>
    </div>

    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> Step 4: Customer-Centricity</div>
      <div class="ws-title">Human Feeling vs Features</div>
      <div class="ws-body">Write 2 sentences explaining why targeting <b>human emotion</b> (fear, boredom, waiting) succeeded over adding tech features.</div>
    </div>
  </div>
</section>
"""
n2 = "<b>Slide 2 Speaker Notes:</b> Walk students through the 4-step worksheet framework. Emphasize that tech is useless without human alignment. Remind them to distinguish between Product, Process, System, and Software."
add_slide(s2, n2)

# SLIDE 3: Category A Header
s3 = """
<section class="slide center">
  <div class="glow-bg"></div>
  <div class="badge accent"><i data-lucide="tv"></i> CATEGORY A</div>
  <h1>Entertainment &amp; <span class="grad">Media Streaming</span></h1>
  <p class="lead" style="margin-top:1.0rem;">Case Studies 1 to 5: Netflix, Spotify, YouTube, Disney+, and Twitch</p>
  <div class="step" style="margin-top:1.5rem; display:flex; gap:1.0rem; justify-content:center; flex-wrap:wrap;">
    <span class="badge">1. Netflix DVD → Streaming</span>
    <span class="badge blue">2. Spotify Discover Weekly</span>
    <span class="badge green">3. YouTube Go Offline</span>
    <span class="badge purple">4. Disney+ Family Profiles</span>
    <span class="badge rose">5. Twitch Live Chat</span>
  </div>
</section>
"""
n3 = "<b>Slide 3 Speaker Notes:</b> Category A focuses on digital media & entertainment. How companies turned frustration in consumption into seamless digital rituals."
add_slide(s3, n3)

# CASE STUDY 1: NETFLIX
s4 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge accent"><i data-lucide="film"></i> CASE STUDY 1 · NETFLIX</div>
  <h2>DVD Rentals to <span class="grad">Digital Streaming</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">System + Software</div>
      <div class="ws-body">Ecosystem transition from physical logistics (mail order DVDs with zero late fees) to cloud-based instant video software on all devices.</div>
    </div>
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Marcus, 32 · Busy Professional</div>
      <div class="ws-body">
        <b>User Goal:</b> Enjoy weekend movie nights with family.<br>
        <b>Core Frustration:</b> Guilt and anxiety from $4/day Blockbuster late fees for missing return deadlines.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Identifying that physical store trips and punitive late fees turned relaxing movie nights into stressful chores, prompting a subscription model.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Removing financial fear and travel effort gave users total freedom. Prioritizing consumer emotional comfort transformed Netflix into a global streaming giant while Blockbuster went bankrupt.</div>
    </div>
  </div>
</section>
"""
n4 = "<b>Slide 4 Speaker Notes:</b> Netflix Case Study: Reed Hastings started Netflix after getting a $40 late fee for Apollo 13. Focusing on removing friction & guilt beat Blockbuster's 9,000 stores."
add_slide(s4, n4)

# CASE STUDY 2: SPOTIFY
s5 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue"><i data-lucide="music"></i> CASE STUDY 2 · SPOTIFY</div>
  <h2>Music Discovery &amp; <span class="grad-cool">"Discover Weekly"</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Software (AI Algorithmic Engine)</div>
      <div class="ws-body">Machine learning recommendation software analyzing listening histories, playlist overlaps, and audio features to curate 30 personalized tracks weekly.</div>
    </div>
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Elena, 24 · Daily Commuter &amp; Music Lover</div>
      <div class="ws-body">
        <b>User Goal:</b> Discover fresh indie music matching her specific vibe.<br>
        <b>Core Frustration:</b> Choice fatigue and overwhelming effort when manually searching through a 70M+ track catalog.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Realizing listeners spent more time searching than listening, Spotify automated discovery into a zero-effort weekly Monday morning mixtape delivery.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">By understanding the emotional thrill of finding a new favorite song, Spotify turned raw data into an intimate personal bond. Effortless delight retention beat having a static search bar.</div>
    </div>
  </div>
</section>
"""
n5 = "<b>Slide 5 Speaker Notes:</b> Spotify Case Study: Discover Weekly felt like a gift from a friend who knows your music taste. Software algorithms solved choice overload."
add_slide(s5, n5)

# CASE STUDY 3: YOUTUBE GO
s6 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green"><i data-lucide="wifi-off"></i> CASE STUDY 3 · YOUTUBE</div>
  <h2>Mobile Buffering in <span class="grad-green">Low-Data Regions</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Software + Process</div>
      <div class="ws-body">Lightweight app software with progressive video preview, offline local storage, and peer-to-peer Wi-Fi Direct file transfer processes.</div>
    </div>
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Rohan, 19 · Tier-3 City Student</div>
      <div class="ws-body">
        <b>User Goal:</b> Watch tutorials and comedy clips without blowing cellular data.<br>
        <b>Core Frustration:</b> Infinite buffering spinners and sudden data exhaust panic mid-video on weak 3G networks.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Recognizing emerging market users had strict data budgets and spotty signals, YouTube enabled downloading videos on free night Wi-Fi for offline viewing.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Addressing financial data anxiety and connection frustration unlocked hundreds of millions of users. Respecting infrastructure reality built massive brand trust in developing nations.</div>
    </div>
  </div>
</section>
"""
n6 = "<b>Slide 6 Speaker Notes:</b> YouTube Go Case Study: Designed specifically for India & emerging markets. Offline sharing via Bluetooth/Wi-Fi Direct solved data fear."
add_slide(s6, n6)

# CASE STUDY 4: DISNEY+
s7 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge purple"><i data-lucide="shield-check"></i> CASE STUDY 4 · DISNEY+</div>
  <h2>Family Profiles &amp; <span class="grad-purple">Parental Controls</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Software (UI/UX System)</div>
      <div class="ws-body">Curated child UI sandboxes, age-rating content filters, PIN-protected adult exit gates, and kid-friendly avatar customization software.</div>
    </div>
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Priya, 35 · Mother of Two Young Children</div>
      <div class="ws-body">
        <b>User Goal:</b> Keep toddlers safely entertained while cooking dinner.<br>
        <b>Core Frustration:</b> Fear of kids stumbling onto violent/scary PG-13 content or ruining watch histories on shared screens.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Identifying the moment parents felt hesitation handing iPads to kids, Disney created strict visual Kid Profiles with zero ad tracking and child-safe navigation.</div>
    </div>
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Prioritizing parental peace of mind established Disney+ as the essential home family service. Caring for parental emotional relief drove higher retention than raw video resolution.</div>
    </div>
  </div>
</section>
"""
n7 = "<b>Slide 7 Speaker Notes:</b> Disney+ Case Study: Child profiles aren't just a UI feature; they represent trust and parental peace of mind."
add_slide(s7, n7)

# CASE STUDY 5: TWITCH
s8 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge rose"><i data-lucide="message-square"></i> CASE STUDY 5 · TWITCH</div>
  <h2>Real-Time Live Stream <span class="grad">Chat Interaction</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Software + System</div>
      <div class="ws-body">Ultra-low latency live video streaming software coupled with real-time websocket chat, animated Emotes, and channel point audience reward mechanics.</div>
    </div>
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Leo, 20 · Gaming Enthusiast</div>
      <div class="ws-body">
        <b>User Goal:</b> Watch favorite gamers and feel part of a lively community.<br>
        <b>Core Frustration:</b> Feeling isolated and invisible when watching traditional passive TV or pre-recorded YouTube videos.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Realizing gaming commentary is a social event, Twitch integrated live chat right next to video streams so audience reactions shape the broadcast live.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Fulfilling the deep human need for belonging and live social recognition created an addictive stadium effect. Shared emotion proved infinitely more engaging than 4K broadcast specs.</div>
    </div>
  </div>
</section>
"""
n8 = "<b>Slide 8 Speaker Notes:</b> Twitch Case Study: Twitch transformed game watching from passive TV into a interactive virtual stadium experience."
add_slide(s8, n8)

# SLIDE 9: Category B Header
s9 = """
<section class="slide center">
  <div class="glow-bg"></div>
  <div class="badge blue"><i data-lucide="truck"></i> CATEGORY B</div>
  <h1>Mobility &amp; <span class="grad-cool">Food Logistics</span></h1>
  <p class="lead" style="margin-top:1.0rem;">Case Studies 6 to 10: Uber, UberEats, DoorDash/Swiggy, Airbnb, and Tesla</p>
  <div class="step" style="margin-top:1.5rem; display:flex; gap:1.0rem; justify-content:center; flex-wrap:wrap;">
    <span class="badge">6. Uber Bad Weather Taxi</span>
    <span class="badge blue">7. UberEats Driver Parking</span>
    <span class="badge green">8. DoorDash/Swiggy Hot Food</span>
    <span class="badge purple">9. Airbnb Photo Quality</span>
    <span class="badge rose">10. Tesla Superchargers</span>
  </div>
</section>
"""
n9 = "<b>Slide 9 Speaker Notes:</b> Category B covers transportation, delivery, and hospitality logistics. How physical real-world friction was conquered by smart systems & empathy."
add_slide(s9, n9)

# CASE STUDY 6: UBER TAXI
s10 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge accent"><i data-lucide="car"></i> CASE STUDY 6 · UBER</div>
  <h2>Hailing Taxis in <span class="grad">Bad Weather</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Software + System</div>
      <div class="ws-body">GPS location matching algorithm software backed by a two-sided driver/rider dispatch network system with upfront pricing and live map telemetry.</div>
    </div>
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Sarah, 28 · Corporate Consultant</div>
      <div class="ws-body">
        <b>User Goal:</b> Get home safely and reliably during a heavy rainstorm.<br>
        <b>Core Frustration:</b> Standing on wet curbs waving at full taxis, unsure if a cab will ever stop or how much cash it will cost.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Targeting the exact moment of physical vulnerability on a rainy street, replacing blind hailing with 1-tap booking showing the incoming driver on a live map.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Eliminating helpless waiting and price uncertainty gave riders complete control. Solved emotional anxiety around urban travel, disrupting the global taxi industry forever.</div>
    </div>
  </div>
</section>
"""
n10 = "<b>Slide 10 Speaker Notes:</b> Uber Case Study: Travis Kalanick and Garrett Camp couldn't hail a cab in Paris in the rain. Uber replaced anxiety with live map visibility."
add_slide(s10, n10)

# CASE STUDY 7: UBEREATS PARKING
s11 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue"><i data-lucide="map-pin"></i> CASE STUDY 7 · UBEREATS</div>
  <h2>The Driver <span class="grad-cool">Parking Problem</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Process + Software</div>
      <div class="ws-body">Empathy-driven field research process leading to driver app software updates (curbside pickup indicators, indoor walking directions, and parking zone hints).</div>
    </div>
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Carlos, 29 · Urban Delivery Courier</div>
      <div class="ws-body">
        <b>User Goal:</b> Deliver 4 food orders an hour cleanly without traffic fines.<br>
        <b>Core Frustration:</b> Circling congested downtown blocks for 15 minutes looking for legal parking, getting cold food complaints from customers.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Designers went on field 'walkabouts' shadowing drivers in city traffic, discovering parking—not driving speed—was the true bottleneck in food logistics.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Observing real driver stress and physical struggle yielded effective app navigation fixes. Treating couriers as primary human users improved total system efficiency.</div>
    </div>
  </div>
</section>
"""
n11 = "<b>Slide 11 Speaker Notes:</b> UberEats Case Study: Uber designers went on field 'walkabouts' to ride along with couriers. They discovered parking was ruining delivery times."
add_slide(s11, n11)

# CASE STUDY 8: DOORDASH / SWIGGY
s12 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green"><i data-lucide="utensils"></i> CASE STUDY 8 · DOORDASH / SWIGGY</div>
  <h2>Cold Food During <span class="grad-green">Peak Delivery Hours</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Process + Software</div>
      <div class="ws-body">Algorithmic kitchen dispatch process synchronizing restaurant stove prep timers directly with driver GPS arrival software for zero shelf downtime.</div>
    </div>
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Ananya, 26 · Hungry Office Worker</div>
      <div class="ws-body">
        <b>User Goal:</b> Enjoy a hot, fresh dinner after a grueling 10-hour workday.<br>
        <b>Core Frustration:</b> Disappointment of receiving lukewarm, soggy pizza or biryani because it sat under a counter for 20 minutes before pickup.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Redesigning the order fulfillment sequence so drivers are dispatched to arrive at the exact minute the chef packs the bag, eliminating heat loss.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Protecting the sensory pleasure of piping hot food prevented customer churn. Optimizing process timing around human appetite beat handing out discount apology vouchers.</div>
    </div>
  </div>
</section>
"""
n12 = "<b>Slide 12 Speaker Notes:</b> DoorDash / Swiggy Case Study: Decoupling order placement from courier dispatch ensures drivers arrive just as food exits the kitchen."
add_slide(s12, n12)

# CASE STUDY 9: AIRBNB
s13 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge purple"><i data-lucide="camera"></i> CASE STUDY 9 · AIRBNB</div>
  <h2>Low Quality <span class="grad-purple">Listing Photos</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Process + Service</div>
      <div class="ws-body">Concierge photography service process where professional photographers were dispatched to hosts' homes to capture high-res lighting and angles.</div>
    </div>
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">David, 40 · Vacationer Booking NYC Stay</div>
      <div class="ws-body">
        <b>User Goal:</b> Book a safe, clean, welcoming apartment in an unfamiliar city.<br>
        <b>Core Frustration:</b> Anxiety and distrust caused by dark, blurry 2009 phone photos making great apartments look like gloomy basements.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Founders Gebbia &amp; Chesky flew to NYC, rented a camera, and photographed listings themselves, realizing trust is built visually before code even matters.</div>
    </div>
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Recognizing that guest trust depends on visual clarity doubled weekly revenue instantly. Solving human trust anxiety rescued Airbnb from early bankruptcy when code tweaks failed.</div>
    </div>
  </div>
</section>
"""
n13 = "<b>Slide 13 Speaker Notes:</b> Airbnb Case Study: In 2009 revenue was stuck at $200/week. Joe Gebbia realized photos were awful. Going in-person to photograph listings saved the company."
add_slide(s13, n13)

# CASE STUDY 10: TESLA
s14 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge rose"><i data-lucide="zap"></i> CASE STUDY 10 · TESLA</div>
  <h2>The EV Charging Station <span class="grad">Network (Supercharger)</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">System (Hardware + Software Network)</div>
      <div class="ws-body">Global Supercharger hardware grid integrated seamlessly with car battery thermal preconditioning software and plug-and-charge automatic billing.</div>
    </div>
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Alex, 38 · Long-Distance EV Driver</div>
      <div class="ws-body">
        <b>User Goal:</b> Drive 500+ miles on interstate road trips without getting stranded.<br>
        <b>Core Frustration:</b> Severe 'range anxiety' and fear of broken, slow, incompatible third-party charging stations in remote highway areas.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Realizing building great electric cars (Product) was useless if drivers feared getting stuck, Tesla built a proprietary worldwide charging ecosystem (System).</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Overcoming psychological range panic unlocked mass EV adoption. Designing a complete supportive system proved far more important than just selling standalone vehicles.</div>
    </div>
  </div>
</section>
"""
n14 = "<b>Slide 14 Speaker Notes:</b> Tesla Case Study: Tesla didn't just build cars (Product); they built the Supercharger System to eliminate range anxiety entirely."
add_slide(s14, n14)

# SLIDE 15: Category C Header
s15 = """
<section class="slide center">
  <div class="glow-bg"></div>
  <div class="badge green"><i data-lucide="smartphone"></i> CATEGORY C</div>
  <h1>Everyday Consumer <span class="grad-green">Tech &amp; Hardware</span></h1>
  <p class="lead" style="margin-top:1.0rem;">Case Studies 11 to 15: Apple, Oral-B, Dyson, GE Healthcare, and Amazon</p>
  <div class="step" style="margin-top:1.5rem; display:flex; gap:1.0rem; justify-content:center; flex-wrap:wrap;">
    <span class="badge">11. Apple AirTags Tracking</span>
    <span class="badge blue">12. Oral-B Smart Toothbrush</span>
    <span class="badge green">13. Dyson Bagless Vacuum</span>
    <span class="badge purple">14. GE Pediatric MRI</span>
    <span class="badge rose">15. Amazon 1-Click Buy</span>
  </div>
</section>
"""
n15 = "<b>Slide 15 Speaker Notes:</b> Category C focuses on consumer products and hardware ecosystems. Balancing physical design, ergonomics, and seamless software."
add_slide(s15, n15)

# CASE STUDY 11: APPLE AIRTAGS
s16 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge accent"><i data-lucide="tag"></i> CASE STUDY 11 · APPLE</div>
  <h2>AirTags &amp; The <span class="grad">"Lost Keys" Panic</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Product + Software + System</div>
      <div class="ws-body">Compact U1 Ultra-Wideband puck hardware linked to Precision Finding iPhone UI software, leveraging 1 billion active devices in the Apple Find My network system.</div>
    </div>
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Michael, 45 · Forgetful Traveler</div>
      <div class="ws-body">
        <b>User Goal:</b> Find keys or luggage instantly when heading out the door.<br>
        <b>Core Frustration:</b> Sudden panic, self-blame, and frantic searching when missing items disappear right before an airport departure.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Converting the universal human micro-panic of lost belongings into a serene haptic screen arrow pointing directly to the hidden keys under a couch cushion.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Relieving daily micro-anxiety and memory stress made AirTags an instant hit. Emotional peace of mind turned simple beacon hardware into a mandatory lifestyle accessory.</div>
    </div>
  </div>
</section>
"""
n16 = "<b>Slide 16 Speaker Notes:</b> Apple AirTags Case Study: Apple didn't invent bluetooth tags; they solved micro-panic using Ultra-Wideband direction arrows & 1B device mesh."
add_slide(s16, n16)

# CASE STUDY 12: ORAL-B
s17 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue"><i data-lucide="smile"></i> CASE STUDY 12 · ORAL-B</div>
  <h2>Smart Toothbrush <span class="grad-cool">Redesign</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Product</div>
      <div class="ws-body">Ergonomic physical toothbrush hardware focusing on magnetic induction charging base design and clean visual replacement indicator lights.</div>
    </div>
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Jessica, 31 · Health-Conscious Adult</div>
      <div class="ws-body">
        <b>User Goal:</b> Maintain clean dental hygiene effortlessly every night.<br>
        <b>Core Frustration:</b> Over-engineered gadgets requiring phone apps, bluetooth setup, or complex buttons just to brush teeth before sleep.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Designers convinced Oral-B *not* to add gimmicky music/tracking features, focusing instead on seamless USB travel charging and simple head-replacement reminders.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Respecting nighttime human tiredness by rejecting feature creep won user loyalty. Simple, thoughtful product design beat useless tech clutter.</div>
    </div>
  </div>
</section>
"""
n17 = "<b>Slide 17 Speaker Notes:</b> Oral-B Case Study: Designers Kim Colin and Sam Hecht convinced Oral-B to stop adding music & apps, and fix USB charging & easy brush replacements instead."
add_slide(s17, n17)

# CASE STUDY 13: DYSON
s18 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green"><i data-lucide="wind"></i> CASE STUDY 13 · DYSON</div>
  <h2>Bagless Vacuum <span class="grad-green">Cleaners</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Product + Process</div>
      <div class="ws-body">Dual-cyclone centrifugal separation physical product architecture eliminating porous paper dust filter bags entirely.</div>
    </div>
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Hannah, 36 · Homeowner with Pets</div>
      <div class="ws-body">
        <b>User Goal:</b> Vacuum rugs efficiently with constant high suction power.<br>
        <b>Core Frustration:</b> Suction dropping by 80% as dust clogs paper bags, plus recurring expense and hassle of buying replacement dust bags.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">James Dyson observed industrial cyclone sawmills separating dust without filters, prototyping 5,127 models to reinvent home vacuuming.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Eliminating performance decay and recurring bag costs gave users immense satisfaction. Solving underlying functional annoyance built a world-class premium brand.</div>
    </div>
  </div>
</section>
"""
n18 = "<b>Slide 18 Speaker Notes:</b> Dyson Case Study: James Dyson built 5,127 prototypes over 5 years. Solving suction loss and eliminating paper bags revolutionized home cleaning."
add_slide(s18, n18)

# CASE STUDY 14: GE HEALTHCARE
s19 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge purple"><i data-lucide="heart-pulse"></i> CASE STUDY 14 · GE HEALTHCARE</div>
  <h2>Pediatric MRI <span class="grad-purple">"Adventure Series"</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Process + Product Environment</div>
      <div class="ws-body">Immersive room decals, pirate/space scanner skins, operator storytelling scripts, and child-soothing ambient sound processes.</div>
    </div>
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Timmy (Age 6, Patient) &amp; Maria (Mother)</div>
      <div class="ws-body">
        <b>User Goal:</b> Complete a vital head MRI scan safely and quickly.<br>
        <b>Core Frustration:</b> Terrifying, loud, dark cold tube making children scream in panic, requiring 80% pediatric sedation rates.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Designer Doug Dietz saw a crying child trembling before an MRI scan he engineered, realizing the machine felt like a dungeon to a 6-year-old.</div>
    </div>
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Transforming scary medical equipment into a pirate ship game reduced sedation rates from 80% to under 1%. Empathy for child fear unlocked human clinical success.</div>
    </div>
  </div>
</section>
"""
n19 = "<b>Slide 19 Speaker Notes:</b> GE Healthcare Case Study: Doug Dietz redesigned the experience into a Pirate Adventure. Sedation dropped from 80% to under 1%, saving lives and time."
add_slide(s19, n19)

# CASE STUDY 15: AMAZON 1-CLICK
s20 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge rose"><i data-lucide="shopping-cart"></i> CASE STUDY 15 · AMAZON</div>
  <h2>The 1-Click <span class="grad">Buy Button</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Software + Process</div>
      <div class="ws-body">Patented zero-friction payment processing software utilizing stored credit card and shipping address state to bypass multi-step checkout pages.</div>
    </div>
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Jason, 29 · Mobile Online Shopper</div>
      <div class="ws-body">
        <b>User Goal:</b> Purchase a book or gadget instantly when impulse strikes.<br>
        <b>Core Frustration:</b> Tedious re-entry of shipping address, credit card numbers, and 5-stage checkout forms on mobile screens leading to cart abandonment.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Identifying that every extra step in checkout created buyer hesitation and frustration, Amazon compressed the entire purchasing flow into a single button.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Removing checkout effort and cognitive hesitation drove billions in impulse revenue. Eliminating digital friction transformed e-commerce behavior worldwide.</div>
    </div>
  </div>
</section>
"""
n20 = "<b>Slide 20 Speaker Notes:</b> Amazon 1-Click Case Study: Peri Hartman invented 1-Click in 1997. Removing friction between intent and purchase drove billions."
add_slide(s20, n20)

# SLIDE 21: Category D Header
s21 = """
<section class="slide center">
  <div class="glow-bg"></div>
  <div class="badge purple"><i data-lucide="credit-card"></i> CATEGORY D</div>
  <h1>Retail, Banking &amp; <span class="grad-purple">Digital Services</span></h1>
  <p class="lead" style="margin-top:1.0rem;">Case Studies 16 to 22: Bank of America, Starbucks, IKEA, Nike, Google Maps, Duolingo, and Zomato</p>
  <div class="step" style="margin-top:1.5rem; display:flex; gap:0.8rem; justify-content:center; flex-wrap:wrap;">
    <span class="badge">16. Bank of America Micro-Savings</span>
    <span class="badge blue">17. Starbucks Mobile Queue</span>
    <span class="badge green">18. IKEA Flat-Pack</span>
    <span class="badge purple">19. Nike+ Ecosystem</span>
    <span class="badge rose">20. Google Maps Traffic</span>
    <span class="badge">21. Duolingo Gamification</span>
    <span class="badge blue">22. Zomato Table Booking</span>
  </div>
</section>
"""
n21 = "<b>Slide 21 Speaker Notes:</b> Category D covers daily consumer services, banking, retail, and digital habits. How subtle human behavior shifts created massive business models."
add_slide(s21, n21)

# CASE STUDY 16: BANK OF AMERICA
s22 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge accent"><i data-lucide="piggy-bank"></i> CASE STUDY 16 · BANK OF AMERICA</div>
  <h2>"Keep the Change" <span class="grad">Savings Program</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Software + System</div>
      <div class="ws-body">Automated debit transaction software that rounds purchases up to the nearest dollar and transfers spare change into savings accounts.</div>
    </div>
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Karen, 27 · Young Professional</div>
      <div class="ws-body">
        <b>User Goal:</b> Build a safety-net savings account without feeling financial sacrifice.<br>
        <b>Core Frustration:</b> Guilt and difficulty of manually transferring lump sums to savings when living paycheck-to-paycheck.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Observing mothers round up checkbook balances for easy mental math, IDEO &amp; BofA turned that micro-habit into automatic micro-savings.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Aligning with subconscious micro-behaviors helped users save over $3 Billion effortlessly. Overcoming saving guilt with painless software created massive user loyalty.</div>
    </div>
  </div>
</section>
"""
n22 = "<b>Slide 22 Speaker Notes:</b> Bank of America Case Study: IDEO observed people rounding up transaction entries in checkbooks. Keep the Change created millions of new savings accounts."
add_slide(s22, n22)

# CASE STUDY 17: STARBUCKS
s23 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue"><i data-lucide="coffee"></i> CASE STUDY 17 · STARBUCKS</div>
  <h2>Mobile Order &amp; Pay <span class="grad-cool">Queue Bypassing</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Software + Process</div>
      <div class="ws-body">Mobile app pre-order software synchronized with dedicated store barista pickup bar workflow processes.</div>
    </div>
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Daniel, 33 · Morning Commuter</div>
      <div class="ws-body">
        <b>User Goal:</b> Grab a favorite morning latte before taking an 8:15 AM train.<br>
        <b>Core Frustration:</b> Seeing a 20-person morning counter queue and walking away empty-handed due to train schedule panic.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Allowing commuters to order and pay on their phone 10 minutes away, walking straight to the pickup counter to grab their labeled cup without waiting.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Respecting morning time-poverty and line anxiety drove over 30% of total revenue to mobile ordering. Customer convenience outperformed adding new drink flavors.</div>
    </div>
  </div>
</section>
"""
n23 = "<b>Slide 23 Speaker Notes:</b> Starbucks Case Study: Mobile Order & Pay eliminated the 15-minute morning queue friction, driving over 30% of US digital transactions."
add_slide(s23, n23)

# CASE STUDY 18: IKEA
s24 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green"><i data-lucide="box"></i> CASE STUDY 18 · IKEA</div>
  <h2>Flat-Pack Furniture &amp; <span class="grad-green">Self-Assembly</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Process + System + Product</div>
      <div class="ws-body">Knock-down furniture product engineering, flat-box warehouse shipping logistics system, and user self-assembly process.</div>
    </div>
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Siddharth, 23 · First-Time Apartment Renter</div>
      <div class="ws-body">
        <b>User Goal:</b> Furnish a stylish modern apartment on a tight student budget.<br>
        <b>Core Frustration:</b> Pre-built furniture being outrageously expensive to ship and impossible to transport in a small sedan car trunk.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">An IKEA worker unscrewed table legs to fit a table into a car trunk, realizing flat packing slashes shipping volume by 80% and democratizes pricing.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Turning assembly into personal pride ('IKEA effect') gave customers affordable luxury. Innovating distribution logistics made high design accessible to everyone.</div>
    </div>
  </div>
</section>
"""
n24 = "<b>Slide 24 Speaker Notes:</b> IKEA Case Study: Gillis Lundgren unscrewed a table's legs in 1956 to fit it into a car trunk. Flat-pack logistics disrupted global home retail."
add_slide(s24, n24)

# CASE STUDY 19: NIKE+
s25 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge purple"><i data-lucide="activity"></i> CASE STUDY 19 · NIKE</div>
  <h2>The Nike+ Running App &amp; <span class="grad-purple">Ecosystem</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Software + System</div>
      <div class="ws-body">GPS &amp; shoe sensor tracking software connected to social leaderboards, audio coaching cues, and digital trophy milestone ecosystems.</div>
    </div>
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Vikram, 30 · Casual Runner</div>
      <div class="ws-body">
        <b>User Goal:</b> Stay consistent running 5km 3 times a week.<br>
        <b>Core Frustration:</b> Loneliness, boredom, and lack of visible progress or motivation when jogging alone in neighborhood streets.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Connecting physical running shoes with digital iPhone feedback so every mile earned real-time cheers and visual milestone trophies.</div>
    </div>
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Transforming solitary exertion into social achievement built profound brand loyalty. Focusing on runner motivation sold more shoes than shoe padding specs alone.</div>
    </div>
  </div>
</section>
"""
n25 = "<b>Slide 25 Speaker Notes:</b> Nike+ Case Study: Partnering with Apple in 2006, Nike turned running into a gamified social experience, building a loyal runner community."
add_slide(s25, n25)

# CASE STUDY 20: GOOGLE MAPS
s26 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge rose"><i data-lucide="navigation"></i> CASE STUDY 20 · GOOGLE MAPS</div>
  <h2>Real-Time Traffic &amp; <span class="grad">Route Re-Direction</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Software + System</div>
      <div class="ws-body">Crowdsourced Smartphone GPS telemetry software coupled with predictive machine learning traffic flow algorithms and dynamic rerouting systems.</div>
    </div>
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Fatima, 34 · City Commuter</div>
      <div class="ws-body">
        <b>User Goal:</b> Arrive at an important work presentation on time.<br>
        <b>Core Frustration:</b> Getting trapped unexpectedly in a 2-hour highway traffic jam with zero advance warning or exit options.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Aggregating live speed data from millions of active devices to detect slowdowns ahead, automatically re-routing drivers onto faster side streets live.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Relieving helplessness and commute panic made Google Maps indispensable. Providing stress-free navigation predictability won universal consumer trust.</div>
    </div>
  </div>
</section>
"""
n26 = "<b>Slide 26 Speaker Notes:</b> Google Maps Case Study: Crowdsourcing smartphone GPS data created live traffic heatmaps and automatic rerouting, conquering urban commute anxiety."
add_slide(s26, n26)

# CASE STUDY 21: DUOLINGO
s27 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge accent"><i data-lucide="gamepad-2"></i> CASE STUDY 21 · DUOLINGO</div>
  <h2>Language Learning <span class="grad">Dropout Rate</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Software (Gamified Mobile App)</div>
      <div class="ws-body">Bite-sized micro-lesson software using streak counters, XP leaderboards, heart mechanics, and Duo mascot push notification triggers.</div>
    </div>
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Kevin, 22 · Student Learning Spanish</div>
      <div class="ws-body">
        <b>User Goal:</b> Practice a foreign language daily for 5 minutes.<br>
        <b>Core Frustration:</b> Boredom and lack of discipline from dry grammar textbooks leading to a 90% learning dropout rate within 2 weeks.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Recognizing that people play mobile games daily for streak rewards, Duolingo structured language acquisition into fun 3-minute video game levels.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Overcoming boredom and discipline loss turned education into a daily habit. Gamifying psychological reward loops built the world's #1 learning app.</div>
    </div>
  </div>
</section>
"""
n27 = "<b>Slide 27 Speaker Notes:</b> Duolingo Case Study: Luis von Ahn gamified education using streaks & XP loops. Solving dropout boredom created over 50M daily active learners."
add_slide(s27, n27)

# CASE STUDY 22: ZOMATO
s28 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge blue"><i data-lucide="calendar"></i> CASE STUDY 22 · ZOMATO</div>
  <h2>Restaurant Table <span class="grad-cool">Reservation Friction</span></h2>
  
  <div class="split step" style="margin-top:1.0rem;">
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="cpu"></i> 1. Solution Type</div>
      <div class="ws-title">Software + Process</div>
      <div class="ws-body">Live table inventory software integrated directly into restaurant discovery listings for instant 1-tap booking confirmation.</div>
    </div>
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="user"></i> 2. Target User Persona</div>
      <div class="ws-title">Rohan &amp; Neha · Anniversary Couple</div>
      <div class="ws-body">
        <b>User Goal:</b> Reserve a romantic table at a top restaurant hassle-free.<br>
        <b>Core Frustration:</b> Calling noisy restaurants during peak hours, being placed on hold, or arriving to find a 45-minute door waiting list.
      </div>
    </div>
  </div>

  <div class="split step" style="margin-top:0.9rem;">
    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="zap"></i> 3. Moment of Opportunity</div>
      <div class="ws-body">Removing telephone phone-tag by giving users real-time table availability and instant booking right inside the restaurant review app.</div>
    </div>
    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="heart"></i> 4. Customer-Centric Assessment</div>
      <div class="ws-body">Eliminating social awkwardness and waiting embarrassment made dining out special. Enhancing emotional ease boosted restaurant partner bookings significantly.</div>
    </div>
  </div>
</section>
"""
n28 = "<b>Slide 28 Speaker Notes:</b> Zomato Case Study: Integrating real-time table reservations into restaurant discovery removed phone call awkwardness and long door queues."
add_slide(s28, n28)

# SLIDE 29: Master Overview Selection Matrix
s29 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge accent"><i data-lucide="grid"></i> GROUP SELECTION MATRIX</div>
  <h2>22 Case Studies <span class="grad">At A Glance</span></h2>
  <p class="lead" style="font-size:1.0rem;">Select 1 topic for your student group worksheet presentation:</p>

  <div style="overflow-y:auto; max-height:420px; margin-top:0.6rem;" class="step">
    <table class="matrix-table">
      <thead>
        <tr>
          <th>#</th>
          <th>Brand &amp; Case Topic</th>
          <th>Category</th>
          <th>Primary Solution Type</th>
          <th>Core Human Emotion / Friction Solved</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>1</td><td>Netflix (DVD → Streaming)</td><td>A. Media</td><td>System + Software</td><td>Guilt &amp; financial penalty of late fees</td></tr>
        <tr><td>2</td><td>Spotify (Discover Weekly)</td><td>A. Media</td><td>Software</td><td>Choice fatigue &amp; search overwhelm</td></tr>
        <tr><td>3</td><td>YouTube Go (Offline Video)</td><td>A. Media</td><td>Software + Process</td><td>Buffering panic &amp; mobile data fear</td></tr>
        <tr><td>4</td><td>Disney+ (Family Profiles)</td><td>A. Media</td><td>Software</td><td>Parental anxiety over child safety</td></tr>
        <tr><td>5</td><td>Twitch (Live Stream Chat)</td><td>A. Media</td><td>Software + System</td><td>Loneliness &amp; passive viewing isolation</td></tr>
        <tr><td>6</td><td>Uber (Rainy Taxi Hailing)</td><td>B. Logistics</td><td>Software + System</td><td>Helplessness waiting on wet curbs</td></tr>
        <tr><td>7</td><td>UberEats (Courier Parking)</td><td>B. Logistics</td><td>Process + Software</td><td>Driver stress &amp; urban parking fines</td></tr>
        <tr><td>8</td><td>DoorDash/Swiggy (Hot Food)</td><td>B. Logistics</td><td>Process + Software</td><td>Disappointment of lukewarm delivery</td></tr>
        <tr><td>9</td><td>Airbnb (Listing Photo Quality)</td><td>B. Logistics</td><td>Process + Service</td><td>Distrust caused by dark/blurry photos</td></tr>
        <tr><td>10</td><td>Tesla (Supercharger Network)</td><td>B. Logistics</td><td>System</td><td>Highway EV range anxiety</td></tr>
        <tr><td>11</td><td>Apple (AirTag Precision Finding)</td><td>C. Tech</td><td>Product + Software</td><td>Micro-panic of lost keys/wallet</td></tr>
        <tr><td>12</td><td>Oral-B (Smart Toothbrush)</td><td>C. Tech</td><td>Product</td><td>Frustration with over-engineered app clutter</td></tr>
        <tr><td>13</td><td>Dyson (Bagless Vacuum)</td><td>C. Tech</td><td>Product + Process</td><td>Annoyance over suction loss &amp; paper bags</td></tr>
        <tr><td>14</td><td>GE Healthcare (Pediatric MRI)</td><td>C. Tech</td><td>Process + Product</td><td>Child terror inside dark medical tubes</td></tr>
        <tr><td>15</td><td>Amazon (1-Click Checkout)</td><td>C. Tech</td><td>Software + Process</td><td>Mobile checkout form exhaustion</td></tr>
        <tr><td>16</td><td>Bank of America (Keep Change)</td><td>D. Services</td><td>Software + System</td><td>Guilt of not saving money paycheck-to-paycheck</td></tr>
        <tr><td>17</td><td>Starbucks (Mobile Order &amp; Pay)</td><td>D. Services</td><td>Software + Process</td><td>Morning commuter line panic &amp; time poverty</td></tr>
        <tr><td>18</td><td>IKEA (Flat-Pack Furniture)</td><td>D. Services</td><td>Process + System</td><td>High shipping costs &amp; bulky transport</td></tr>
        <tr><td>19</td><td>Nike (Nike+ Running App)</td><td>D. Services</td><td>Software + System</td><td>Boredom &amp; loneliness of solo running</td></tr>
        <tr><td>20</td><td>Google Maps (Traffic Reroute)</td><td>D. Services</td><td>Software + System</td><td>Gridlock commute frustration &amp; helplessness</td></tr>
        <tr><td>21</td><td>Duolingo (Gamified Streaks)</td><td>D. Services</td><td>Software</td><td>Language learning boredom &amp; dropout</td></tr>
        <tr><td>22</td><td>Zomato (Table Reservation)</td><td>D. Services</td><td>Software + Process</td><td>Phone reservation awkwardness &amp; waiting lines</td></tr>
      </tbody>
    </table>
  </div>
</section>
"""
n29 = "<b>Slide 29 Speaker Notes:</b> Group Selection Matrix: Use this table for student groups to browse all 22 real-world case study topics across Categories A, B, C, and D."
add_slide(s29, n29)

# SLIDE 30: Module 1 Core Takeaways & Summary
s30 = """
<section class="slide">
  <div class="glow-bg"></div>
  <div class="badge green"><i data-lucide="check-circle-2"></i> MODULE 1 MASTER SUMMARY</div>
  <h2>4 Core Principles of <span class="grad-green">Design Thinking</span></h2>
  
  <div class="grid-4 step" style="margin-top:1.2rem;">
    <div class="ws-card highlight">
      <div class="ws-label"><i data-lucide="heart"></i> 1. Customer-Centricity</div>
      <div class="ws-title">Human Emotion First</div>
      <div class="ws-body">Great products solve human feelings (fear, anxiety, boredom, guilt). Raw technical features fail if human fit is missing.</div>
    </div>
    
    <div class="ws-card cool-hl">
      <div class="ws-label blue"><i data-lucide="layers"></i> 2. Solution Typology</div>
      <div class="ws-title">Beyond Just "Products"</div>
      <div class="ws-body">Know the difference: <b>Product</b> (physical item), <b>Process</b> (workflow/method), <b>System</b> (ecosystem/network), <b>Software</b> (digital code).</div>
    </div>

    <div class="ws-card green-hl">
      <div class="ws-label green"><i data-lucide="user-check"></i> 3. User Persona</div>
      <div class="ws-title">You Are Not The User!</div>
      <div class="ws-body">Build data-driven personas with explicit Goals and Frustrations rather than guessing user preferences from your own bias.</div>
    </div>

    <div class="ws-card purple-hl">
      <div class="ws-label purple"><i data-lucide="compass"></i> 4. Opportunity Spotting</div>
      <div class="ws-title">Friction into Possibility</div>
      <div class="ws-body">Average engineers see complaints; Design Thinkers spot the exact micro-moment of opportunity to intervene and delight.</div>
    </div>
  </div>

  <div class="hero-quote-card green step" style="margin-top:1.0rem;">
    <div class="hero-quote-title">EXAM &amp; INDUSTRY GOLDEN RULE</div>
    <div class="hero-quote-text">"Technology is WHAT we build. Design Thinking is WHY we build it and WHO it serves."</div>
  </div>
</section>
"""
n30 = "<b>Slide 30 Speaker Notes:</b> Final Summary: Summarize Module 1 core takeaways. Remind students to submit their completed 4-step worksheet."
add_slide(s30, n30)

# Build HTML document structure
slides_html = "\n".join(slides)

# Format speaker notes as JS array
notes_js_array = "[\n" + ",\n".join([repr(n) for n in notes]) + "\n]"

html_foot = f"""
</div>

<!-- FOOTER CHROME -->
<div class="chrome">
  <div class="brand">
    <i data-lucide="book-open"></i> <b>GEE 1102</b> · Design Thinking · Module 1 Activity Deck
  </div>
  <div class="right">
    <button class="notesbtn" id="notesbtn">Speaker Notes (S)</button>
    <span class="counter"><span id="cur">01</span> / <span id="tot">30</span></span>
  </div>
</div>

<!-- SPEAKER NOTES OVERLAY -->
<div class="notes" id="notes">
  <div class="notes-head">
    <div class="lbl"><i data-lucide="message-square"></i> Instructor Speaker Notes</div>
    <div class="x" id="notesx">&times;</div>
  </div>
  <div class="notes-body" id="notesbody"></div>
</div>

<script>
const NOTES = {notes_js_array};

const slides = [...document.querySelectorAll('.slide')];
const progress = document.getElementById('progress');
const cur = document.getElementById('cur');
const tot = document.getElementById('tot');
const notesEl = document.getElementById('notes');
const notesBody = document.getElementById('notesbody');
let i = 0;

tot.textContent = String(slides.length).padStart(2, '0');

function renderNotes() {{
  notesBody.innerHTML = NOTES[i] || '<i>No notes available for this slide.</i>';
  notesBody.scrollTop = 0;
}}

function go(n) {{
  if (n < 0 || n >= slides.length) return;
  slides[i].classList.remove('active');
  slides[i].classList.add('prev');
  i = n;
  slides.forEach(s => s.classList.remove('prev'));
  slides[i].classList.add('active');
  
  // Reset steps on slide transition
  slides[i].querySelectorAll('.step').forEach(step => step.classList.remove('revealed'));
  
  progress.style.width = ((i + 1) / slides.length * 100) + '%';
  cur.textContent = String(i + 1).padStart(2, '0');
  if (notesEl.classList.contains('open')) renderNotes();
}}

function next() {{
  const currentSlide = slides[i];
  const unrevealedSteps = currentSlide.querySelectorAll('.step:not(.revealed)');
  if (unrevealedSteps.length > 0) {{
    unrevealedSteps[0].classList.add('revealed');
  }} else {{
    go(i + 1);
  }}
}}

function prev() {{
  const currentSlide = slides[i];
  const revealedSteps = currentSlide.querySelectorAll('.step.revealed');
  if (revealedSteps.length > 0) {{
    revealedSteps[revealedSteps.length - 1].classList.remove('revealed');
  }} else {{
    go(i - 1);
  }}
}}

go(0);

function toggleNotes() {{
  notesEl.classList.toggle('open');
  if (notesEl.classList.contains('open')) renderNotes();
}}

document.getElementById('notesbtn').addEventListener('click', toggleNotes);
document.getElementById('notesx').addEventListener('click', () => notesEl.classList.remove('open'));

document.addEventListener('keydown', e => {{
  if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === ' ') {{ e.preventDefault(); next(); }}
  else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {{ e.preventDefault(); prev(); }}
  else if (e.key === 'Home') {{ go(0); }}
  else if (e.key === 'End') {{ go(slides.length - 1); }}
  else if (e.key === 's' || e.key === 'S') {{ toggleNotes(); }}
  else if (e.key === 'f' || e.key === 'F') {{
    if (!document.fullscreenElement) document.documentElement.requestFullscreen();
    else document.exitFullscreen();
  }}
  else if (e.key === 'Escape') {{ notesEl.classList.remove('open'); }}
}});

let x0 = null;
document.addEventListener('touchstart', e => x0 = e.touches[0].clientX, {{ passive: true }});
document.addEventListener('touchend', e => {{
  if (x0 === null) return;
  const dx = e.changedTouches[0].clientX - x0;
  if (Math.abs(dx) > 50) {{ dx < 0 ? next() : prev(); }}
  x0 = null;
}}, {{ passive: true }});

document.getElementById('deck').addEventListener('click', e => {{
  if (e.target.closest('.notes') || e.target.closest('.notesbtn') || e.target.closest('a') || e.target.closest('table')) return;
  e.clientX > innerWidth / 2 ? next() : prev();
}});

lucide.createIcons();
</script>
</body>
</html>
"""

full_html = html_head + slides_html + html_foot

with open(output_filename, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Successfully generated {output_filename} with {len(slides)} slides.")
