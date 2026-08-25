import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)

# ====================================================
# SECTION 3: MEMORY & DATA ARCHITECTURE (INTERMEDIATE)
# Queues, RAM Lockers, Pass-By-Ref, Stack Memory, Heap & GC, Type Overflow
# ====================================================

# Slide: Section 3 Roadmap
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="layers"></i> SECTION 3 · MEMORY & DATA ARCHITECTURE</div>
  <h2 class="reveal">Level 2: Under the Hood ⚙️</h2>
  <div class="reveal" style="width:100%; max-width:900px; background:#111; border:1px solid var(--border); border-radius:12px; padding:1rem 2rem;">
    <table>
      <tr><th>#</th><th>Real World Story</th><th>Concept Name</th></tr>
      <tr><td>07</td><td>Kumar Canteen Billing Line</td><td><b style="color:var(--gold);">Queues (FIFO)</b></td></tr>
      <tr><td>08</td><td>Central Station Cloakroom Locker</td><td><b style="color:var(--blue);">RAM Memory Lockers</b></td></tr>
      <tr><td>09</td><td>Xerox Copy vs Original Bike Key</td><td><b style="color:var(--accent);">Pass-By-Reference</b></td></tr>
      <tr><td>10</td><td>Hostel Mess Plate Stack</td><td><b style="color:var(--green);">Stack Memory</b></td></tr>
      <tr><td>11</td><td>Mall Store Room & Auto Sweeper</td><td><b style="color:var(--purple);">Heap Memory & GC</b></td></tr>
      <tr><td>12</td><td>5L Bisleri Can in 200ml Tea Glass</td><td><b style="color:var(--red);">Type Overflow</b></td></tr>
    </table>
  </div>
</section>
""")
notes.append("""<b>Speaker Point:</b> Welcome to Level 2. Here we learn how data is stored, queued, and cleaned up in memory.""")

# CONCEPT 07: QUEUES (FIFO)
# Story
slides_html.append("""
<section class="slide">
  <div class="badge gold reveal"><i data-lucide="zap"></i> CONCEPT 07 · SUSPENSE STORY</div>
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
  <div class="badge gold reveal"><i data-lucide="award"></i> CONCEPT #07 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad" style="font-size:clamp(3.8rem, 9vw, 8rem); margin-top:0.6rem; letter-spacing:-.03em;">QUEUES (FIFO)</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(First-In, First-Out Sequential Processing lines)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> QUEUES (FIFO).""")

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


# CONCEPT 09: PASS-BY-REFERENCE
# Story
slides_html.append("""
<section class="slide">
  <div class="badge accent reveal"><i data-lucide="zap"></i> CONCEPT 09 · SUSPENSE STORY</div>
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
  <div class="badge accent reveal"><i data-lucide="award"></i> CONCEPT #09 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-cool" style="font-size:clamp(3.5rem, 8vw, 7.2rem); margin-top:0.6rem; letter-spacing:-.03em;">PASS-BY-REFERENCE</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Independent Xerox Copies vs Shared Pointer Addresses)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> PASS-BY-REFERENCE.""")

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

# CONCEPT 12: TYPE OVERFLOW
# Story
slides_html.append("""
<section class="slide">
  <div class="badge red reveal"><i data-lucide="zap"></i> CONCEPT 12 · SUSPENSE STORY</div>
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
  <div class="badge red reveal"><i data-lucide="award"></i> CONCEPT #12 REVEAL</div>
  <p class="lead reveal" style="font-size:1.4rem; color:var(--dim); margin-top:1rem;">This concept is called...</p>
  <h1 class="reveal grad-red" style="font-size:clamp(3.5rem, 8.5vw, 7.5rem); margin-top:0.6rem; letter-spacing:-.03em;">TYPE OVERFLOW</h1>
  <p class="kicker reveal" style="margin-top:1.5rem; font-size:1.25rem;">(Memory Container Capacity Exceeded Disasters)</p>
</section>
""")
notes.append("""<b>Big Hero Impact Reveal Slide:</b> TYPE OVERFLOW.""")

# END OF PART 2
