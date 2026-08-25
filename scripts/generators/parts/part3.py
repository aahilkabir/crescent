import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

# ====================================================
# SECTION 4: ADVANCED CONCEPTS & OOP (ADVANCED)
# Abstraction, Inheritance, Recursion, Error Traps, Big O, Hash Maps
# ====================================================

# Slide: Section 4 Roadmap
slides_html.append("""
<section class="slide">
  <div class="badge red reveal"><i data-lucide="layers"></i> SECTION 4 · ADVANCED CONCEPTS & OOP</div>
  <h2 class="reveal">Level 3: Pro Techniques 🚀</h2>
  <div class="reveal" style="width:100%; max-width:900px; background:#111; border:1px solid var(--border); border-radius:12px; padding:1rem 2rem;">
    <table>
      <tr><th>#</th><th>Real World Story</th><th>Concept Name</th></tr>
      <tr><td>13</td><td>A.R. Rahman Sound Board Slider</td><td><b style="color:var(--cyan);">Abstraction (OOP)</b></td></tr>
      <tr><td>14</td><td>Vijay Mass Hero Template Reuse</td><td><b style="color:var(--purple);">Inheritance (OOP)</b></td></tr>
      <tr><td>15</td><td>Wedding Gift Box inside Box</td><td><b style="color:var(--red);">Call Stack & Recursion</b></td></tr>
      <tr><td>16</td><td>Tagore Canteen UPS Fallback</td><td><b style="color:var(--gold);">Defensive Error Traps</b></td></tr>
      <tr><td>17</td><td>Metro Gate Tap vs Crowd Search</td><td><b style="color:var(--green);">Big O Scalability</b></td></tr>
      <tr><td>18</td><td>Marina Beach Token Parking</td><td><b style="color:var(--blue);">Hash Maps (O(1))</b></td></tr>
    </table>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> Welcome to Level 3. Object Oriented Programming and algorithmic efficiency!""")


# CONCEPT 13: ABSTRACTION
# Story
slides_html.append("""
<section class="slide">
  <div class="badge cyan reveal"><i data-lucide="zap"></i> CONCEPT 13 · SUSPENSE STORY</div>
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
  <div class="badge cyan reveal"><i data-lucide="award"></i> CONCEPT #13 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-cool" style="font-size:clamp(3.5rem, 8vw, 7.2rem); margin-top:0.6rem; letter-spacing:-.03em;">ABSTRACTION</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Hiding Complex Internal Wiring Behind Simple APIs)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> ABSTRACTION.""")

# CONCEPT 14: INHERITANCE
# Story
slides_html.append("""
<section class="slide">
  <div class="badge purp reveal"><i data-lucide="zap"></i> CONCEPT 14 · SUSPENSE STORY</div>
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
  <div class="badge purp reveal"><i data-lucide="award"></i> CONCEPT #14 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-purp" style="font-size:clamp(3.5rem, 8vw, 7.2rem); margin-top:0.6rem; letter-spacing:-.03em;">INHERITANCE</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Reusing Parent Code Blueprints in Child Classes)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> INHERITANCE.""")

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

# CONCEPT 16: DEFENSIVE ERROR TRAPS
# Story
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="zap"></i> CONCEPT 16 · SUSPENSE STORY</div>
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
  <div class="badge gold reveal"><i data-lucide="award"></i> CONCEPT #16 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">DEFENSIVE ERROR TRAPS</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Try / Catch / Finally Fallback Resilience)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> DEFENSIVE ERROR TRAPS.""")

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

# CONCEPT 18: HASH MAPS
# Story
slides_html.append("""
<section class="slide">
  <div class="badge blue reveal"><i data-lucide="zap"></i> CONCEPT 18 · SUSPENSE STORY</div>
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
  <div class="badge blue reveal"><i data-lucide="award"></i> CONCEPT #18 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-cool" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">HASH MAPS</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(O(1) Instant Key-Value Dictionary Lookups)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> HASH MAPS.""")

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
