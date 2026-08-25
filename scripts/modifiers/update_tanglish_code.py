import os
# Dynamic PROJECT_ROOT resolution
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = SCRIPT_DIR
while os.path.basename(PROJECT_ROOT) in ["generators", "modifiers", "scripts", "utilities", "parts"]:
    PROJECT_ROOT = os.path.dirname(PROJECT_ROOT)


file_path = os.path.join(PROJECT_ROOT, "generate_55_slides.py")
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    # 1. Abstraction
    """<div class="code-box-clean reveal">
    <div class="code-line highlight-gold"><span class="cm">// High-Level Framework Command</span><br>
    System.audio.<span class="fn">increaseVolume</span>({ level: <span class="num">90</span> });</div><br>
    <span class="cm">// Lower Engine Execution (Hidden Abstraction)</span><br>
    <span class="cm">// [User Interface] -> [API Gateway] -> [Native Module] -> [CPU Registers]</span>
  </div>""": """<div class="code-box-clean reveal">
    <div class="code-line highlight-gold"><span class="cm">// High-Level Abstraction: Oru slider-a mela thookuradhu</span><br>
    arrRahmanConsole.<span class="fn">increaseBassVolume</span>({ volumeLevel: <span class="str">"MAX"</span> });</div><br>
    <span class="cm">// Lower Engine Execution (Ulla irukka complex wiring)</span><br>
    <span class="cm">// [Slider Move] -> [Digital Signal Processor] -> [Copper Wires] -> [5000W Amp Blast!]</span>
  </div>""",

    # 2. Inheritance
    """<div class="code-box-clean reveal">
    <span class="cm">// class = அடிப்படை வடிவம் (Baseline Template Blueprint)</span><br>
    <span class="kw">class</span> <span class="fn">MassHero</span> { introWalk = <span class="str">"🔥 Slow-Motion Entry"</span>; }<br><br>
    <div class="code-line highlight-gold"><span class="cm">// extends = பரம்பரைத் தொடர்ச்சி (Inherit parent capabilities)</span><br>
    <span class="kw">class</span> <span class="fn">GOATHero</span> <span class="kw">extends</span> <span class="fn">MassHero</span> { punchLine = <span class="str">"I am waiting!"</span>; }</div>
  </div>""": """<div class="code-box-clean reveal">
    <span class="cm">// class = அடிப்படை வடிவம் (Base Template)</span><br>
    <span class="kw">class</span> <span class="fn">DirectorMassHero</span> { <br>
    &nbsp;&nbsp;introBGM = <span class="str">"🔥 Slow-Motion BGM"</span>; <br>
    }<br><br>
    <div class="code-line highlight-gold"><span class="cm">// extends = பரம்பரைத் தொடர்ச்சி (GOAT Thalapathy adding punchline to base template)</span><br>
    <span class="kw">class</span> <span class="fn">GOAT_Thalapathy</span> <span class="kw">extends</span> <span class="fn">DirectorMassHero</span> { <br>
    &nbsp;&nbsp;massPunchLine = <span class="str">"I am waiting!"</span>; <br>
    }</div>
  </div>""",

    # 3. Array Offsets
    """<div class="code-box-clean cool reveal">
    <span class="kw">const</span> mtcBench = [<span class="str">'Conductor'</span>, <span class="str">'Kamal'</span>, <span class="str">'Rajini'</span>, <span class="str">'Vijay'</span>];<br><br>
    <div class="code-line highlight-green"><span class="cm">// Address Offset: Start Address (0x1000) + (Index * Element Size)</span><br>
    <span class="kw">let</span> frontSeat = mtcBench[<span class="num">0</span>]; <span class="cm">// 0 Steps away from door -> 'Conductor'</span></div>
    <span class="kw">let</span> thirdSeat = mtcBench[<span class="num">2</span>]; <span class="cm">// 2 Steps away from door -> 'Rajini'</span>
  </div>""": """<div class="code-box-clean cool reveal">
    <span class="kw">const</span> mtcBusBenchRow = [<span class="str">'Conductor'</span>, <span class="str">'Kamal'</span>, <span class="str">'Rajini'</span>, <span class="str">'Vijay'</span>];<br><br>
    <div class="code-line highlight-green"><span class="cm">// Index 0 = Door entrance-la irundhu 0 steps distance!</span><br>
    <span class="kw">let</span> frontSeat = mtcBusBenchRow[<span class="num">0</span>]; <span class="cm">// Answer: 'Conductor'</span></div>
    <span class="cm">// Index 2 = Door entrance-la irundhu 2 steps thalli utkaruradhu!</span><br>
    <span class="kw">let</span> massSeat = mtcBusBenchRow[<span class="num">2</span>]; <span class="cm">// Answer: 'Rajini'</span>
  </div>""",

    # 4. Functions & Delegation
    """<div class="code-box-clean grn reveal">
    <span class="kw">function</span> <span class="fn">swiggyRunner</span>(dishName, address) {<br>
    <div class="code-line highlight-green">&nbsp;&nbsp;<span class="kw">return</span> { food: dishName, status: <span class="str">"Delivered to "</span> + address };</div><br>
    }<br><br>
    <span class="kw">let</span> orderStatus = <span class="fn">swiggyRunner</span>(<span class="str">"Chicken Biryani"</span>, <span class="str">"Hostel Block A"</span>);
  </div>""": """<div class="code-box-clean grn reveal">
    <span class="cm">// function = Namma velaiya innoruthar-kitta delegate panradhu</span><br>
    <span class="kw">function</span> <span class="fn">swiggyDeliveryPartner</span>(saapaduMenu, roomAddress) {<br>
    <div class="code-line highlight-green">&nbsp;&nbsp;<span class="cm">// return = Task mudichutu saapadu kondu vandhu kudukuradhu</span><br>
    &nbsp;&nbsp;<span class="kw">return</span> { food: saapaduMenu, deliveryStatus: <span class="str">"Vandhutrukken bro!"</span> };</div><br>
    }<br><br>
    <span class="cm">// Input arguments pass panrom</span><br>
    <span class="kw">let</span> orderStatus = <span class="fn">swiggyDeliveryPartner</span>(<span class="str">"Chicken Biryani"</span>, <span class="str">"Hostel Block A"</span>);
  </div>""",

    # 5. Immutability
    """<div class="code-box-clean cool reveal">
    <div class="code-line highlight-gold"><span class="cm">// const = மாற்ற முடியாத பூட்டு (Locked Identity)</span><br>
    <span class="kw">const</span> HALL_TICKET_NO = <span class="str">"312822104001"</span>;</div><br>
    <span class="cm">// let = மாற்றக்கூடிய மதிப்பு (Daily Data Remaining)</span><br>
    <span class="kw">let</span> remainingDataMB = <span class="num">2048</span>;<br>
    remainingDataMB = remainingDataMB - <span class="num">500</span>; <span class="cm">// Valid Update</span>
  </div>""": """<div class="code-box-clean cool reveal">
    <div class="code-line highlight-gold"><span class="cm">// const = மாற்ற முடியாத பூட்டு (Hall Ticket number cannot be changed)</span><br>
    <span class="kw">const</span> hallTicketNo = <span class="str">"312822104001"</span>;</div><br>
    <span class="cm">// let = மாற்றக்கூடிய மதிப்பு (Daily 5G data korainjute varum)</span><br>
    <span class="kw">let</span> dailyDataMB = <span class="num">2048</span>;<br>
    dailyDataMB = dailyDataMB - <span class="num">500</span>; <span class="cm">// Valid Update: Insta Reels pathu 500MB gaali!</span>
  </div>""",

    # 6. Type Overflow
    """<div class="code-box-clean red reveal">
    <span class="kw">let</span> rocketVelocity: <span class="kw">Float64</span> = <span class="num">32768.95</span>; <span class="cm">// 5-Liter Payload</span><br><br>
    <div class="code-line highlight-red"><span class="cm">// Int16 = 200ml Glass (Max Capacity = 32,767!)</span><br>
    <span class="kw">let</span> sensorBuffer: <span class="kw">Int16</span> = rocketVelocity; <span class="cm">// 💥 Int16 Max Overflow -> Boom!</span></div>
  </div>""": """<div class="code-box-clean red reveal">
    <span class="kw">let</span> bisleriCanWater: <span class="kw">Float64</span> = <span class="num">5.0</span>; <span class="cm">// 5 Liters of Water</span><br><br>
    <div class="code-line highlight-red"><span class="cm">// Int16 = 200ml Cutting Chai Glass (Max Capacity!)</span><br>
    <span class="kw">let</span> cuttingChaiGlass: <span class="kw">Int16</span> = bisleriCanWater; <span class="cm">// 💥 Overflow - Kottidum! Rocket Boom!</span></div>
  </div>""",

    # 7. Conditionals
    """<div class="code-box-clean grn reveal">
    <div class="code-line highlight-green"><span class="kw">if</span> (userAge >= <span class="num">18</span> && ticket.<span class="fn">isValid</span>()) {<br>
    &nbsp;&nbsp;<span class="fn">allowEntryToAudi</span>();<br>
    } <span class="kw">else</span> {<br>
    &nbsp;&nbsp;<span class="fn">redirectToRefundCounter</span>();<br>
    }</div>
  </div>""": """<div class="code-box-clean grn reveal">
    <div class="code-line highlight-green"><span class="cm">// Gate Check: Vayasu 18 & Ticket Unmaiya irundhal...</span><br>
    <span class="kw">if</span> (userVayasu >= <span class="num">18</span> && cinemaTicket.<span class="fn">isOriginal</span>()) {<br>
    &nbsp;&nbsp;<span class="fn">openGateForAudi1</span>();<br>
    } <span class="kw">else</span> {<br>
    &nbsp;&nbsp;<span class="cm">// Illati... Refund counter-ku anupidu!</span><br>
    &nbsp;&nbsp;<span class="fn">divertToRefundCounter</span>();<br>
    }</div>
  </div>""",

    # 8. Safety Loops
    """<div class="code-box-clean red reveal">
    <span class="kw">while</span> (isPlateEmpty) {<br>
    &nbsp;&nbsp;<span class="fn">pourSambhar</span>();<br>
    <div class="code-line highlight-red">&nbsp;&nbsp;<span class="kw">if</span> (refillCount > <span class="num">5</span>) <span class="kw">break</span>; <span class="cm">// Safety Trap!</span></div><br>
    }
  </div>""": """<div class="code-box-clean red reveal">
    <span class="cm">// Saapadu thattu empty-a irukkum varai...</span><br>
    <span class="kw">while</span> (isThattuEmpty) {<br>
    &nbsp;&nbsp;<span class="fn">oothuSambhar</span>();<br>
    <div class="code-line highlight-red">&nbsp;&nbsp;<span class="cm">// Safety Check: 5 vaati mela oothuna, stop pannu! (AWS Bill limit!)</span><br>
    &nbsp;&nbsp;<span class="kw">if</span> (sambharOothunaCount > <span class="num">5</span>) <span class="kw">break</span>; <span class="cm">// Safety Trap Break!</span></div><br>
    }
  </div>""",

    # 9. Hash Maps
    """<div class="code-box-clean cool reveal">
    <span class="kw">const</span> marinaParkingMap = <span class="kw">new</span> <span class="fn">Map</span>();<br>
    marinaParkingMap.<span class="fn">set</span>(<span class="num">842</span>, { bikeNo: <span class="str">"TN-01-AB-1234"</span> });<br><br>
    <div class="code-line highlight-green"><span class="cm">// O(1) Instant Direct Access</span><br>
    <span class="kw">let</span> myBike = marinaParkingMap.<span class="fn">get</span>(<span class="num">842</span>);</div>
  </div>""": """<div class="code-box-clean cool reveal">
    <span class="kw">const</span> marinaBikeParkingMap = <span class="kw">new</span> <span class="fn">Map</span>();<br>
    marinaBikeParkingMap.<span class="fn">set</span>(<span class="num">842</span>, { bikeVandiNo: <span class="str">"TN-01-AB-1234"</span> });<br><br>
    <div class="code-line highlight-green"><span class="cm">// O(1) Instant Direct Access - Token kudutha odane Vandi varum!</span><br>
    <span class="kw">let</span> enBikeVandi = marinaBikeParkingMap.<span class="fn">get</span>(<span class="num">842</span>);</div>
  </div>""",

    # 10. Error Traps
    """<div class="code-box-clean grn reveal">
    <span class="kw">try</span> { <span class="fn">processOnlineBilling</span>(); } <br>
    <div class="code-line highlight-green"><span class="kw">catch</span> (PowerCutError) { <span class="fn">processOfflineUPSBilling</span>(); }</div><br>
    <span class="kw">finally</span> { <span class="fn">syncAuditLogs</span>(); }
  </div>""": """<div class="code-box-clean grn reveal">
    <span class="kw">try</span> { <br>
    &nbsp;&nbsp;<span class="cm">// Muyarchi pannu: Normal current-la billing</span><br>
    &nbsp;&nbsp;<span class="fn">runNormalOnlineBilling</span>(); <br>
    } <br>
    <div class="code-line highlight-green"><span class="kw">catch</span> (CurrentCutError) { <br>
    &nbsp;&nbsp;<span class="cm">// Prachanai vandhal: Odane UPS Generator on pannu!</span><br>
    &nbsp;&nbsp;<span class="fn">runUPSOfflineBilling</span>(); <br>
    }</div><br>
    <span class="kw">finally</span> { <span class="cm">// Enna aanaalum: Audit logs update pannidu!</span><br>
    &nbsp;&nbsp;<span class="fn">saveBillsToLedger</span>(); <br>
    }
  </div>""",

    # 11. Database Indexing
    """<div class="code-box-clean cool reveal">
    <span class="cm">// ❌ WITHOUT INDEX: Full Table Scan (Slow 4,200ms O(n))</span><br>
    db.users.<span class="fn">find</span>({ instagramHandle: <span class="str">"@kabir"</span> });<br><br>
    <div class="code-line highlight-green"><span class="cm">// ✅ WITH INDEX: B-Tree Fast Lookup (அகராதிப் பட்டியல் O(log n))</span><br>
    db.users.<span class="fn">createIndex</span>({ instagramHandle: <span class="num">1</span> });<br>
    db.users.<span class="fn">find</span>({ instagramHandle: <span class="str">"@kabir"</span> }); <span class="cm">// Instant 2ms pickup!</span></div>
  </div>""": """<div class="code-box-clean cool reveal">
    <span class="cm">// ❌ WITHOUT INDEX: Full Table Scan (Ellaa bay-kum nadandhu poi thedu - O(n))</span><br>
    db.busBays.<span class="fn">find</span>({ oorDestination: <span class="str">"Chennai"</span> });<br><br>
    <div class="code-line highlight-green"><span class="cm">// ✅ WITH INDEX: B-Tree Alpha-Board (Direct-a board pathu bus-a pudi - O(log n))</span><br>
    db.busBays.<span class="fn">createIndex</span>({ oorDestination: <span class="num">1</span> });<br>
    db.busBays.<span class="fn">find</span>({ oorDestination: <span class="str">"Chennai"</span> }); <span class="cm">// Instant pickup!</span></div>
  </div>""",

    # 12. Microservices
    """<div class="code-box-clean grn reveal">
    <span class="kw">async function</span> <span class="fn">processZomatoOrderResilient</span>(order) {<br>
    &nbsp;&nbsp;<span class="kw">try</span> {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">await</span> paymentMicroservice.<span class="fn">charge</span>(order);<br>
    &nbsp;&nbsp;} <span class="kw">catch</span> (PaymentError) {<br>
    <div class="code-line highlight-green">&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">// Payment service down-aanaalum, Zomato Cart stays safe!</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">return</span> <span class="fn">showAlternativePaymentOptions</span>();</div><br>
    &nbsp;&nbsp;}<br>
    }
  </div>""": """<div class="code-box-clean grn reveal">
    <span class="kw">async function</span> <span class="fn">processMultiplexOrderResilient</span>(customerOrder) {<br>
    &nbsp;&nbsp;<span class="kw">try</span> {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">// Veggies counter-ku thaan payment anupurom</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">await</span> veggiesCounterMicroservice.<span class="fn">chargeCash</span>(customerOrder);<br>
    &nbsp;&nbsp;} <span class="kw">catch</span> (CounterClosedError) {<br>
    <div class="code-line highlight-green">&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">// Veggies counter closed aanaalum, Delivery Exit remains open & safe!</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="kw">return</span> <span class="fn">divertToFruitsCounter</span>();</div><br>
    &nbsp;&nbsp;}<br>
    }
  </div>""",

    # 13. Load Balancing
    """<div class="code-box-clean reveal">
    <span class="kw">const</span> backendServers = [<span class="str">'Server_A'</span>, <span class="str">'Server_B'</span>, <span class="str">'Server_C'</span>];<br>
    <span class="kw">let</span> currentServerIndex = <span class="num">0</span>;<br><br>
    <span class="kw">function</span> <span class="fn">routeIncomingUserRequest</span>(userRequest) {<br>
    <div class="code-line highlight-gold">&nbsp;&nbsp;<span class="kw">let</span> targetServer = backendServers[currentServerIndex];<br>
    &nbsp;&nbsp;currentServerIndex = (currentServerIndex + <span class="num">1</span>) % backendServers.length;</div><br>
    &nbsp;&nbsp;<span class="kw">return</span> targetServer.<span class="fn">forward</span>(userRequest);<br>
    }
  </div>""": """<div class="code-box-clean reveal">
    <span class="cm">// 20 parallel Toll Gates available!</span><br>
    <span class="kw">const</span> tollGateQueue = [<span class="str">'Gate_1'</span>, <span class="str">'Gate_2'</span>, <span class="str">'Gate_3'</span>];<br>
    <span class="kw">let</span> currentGateIndex = <span class="num">0</span>;<br><br>
    <span class="kw">function</span> <span class="fn">routeIncomingCar</span>(pongalTrafficCar) {<br>
    <div class="code-line highlight-gold">&nbsp;&nbsp;<span class="cm">// Round-Robin: Oru car Gate_1 na, adutha car Gate_2...</span><br>
    &nbsp;&nbsp;<span class="kw">let</span> targetGate = tollGateQueue[currentGateIndex];<br>
    &nbsp;&nbsp;currentGateIndex = (currentGateIndex + <span class="num">1</span>) % tollGateQueue.length;</div><br>
    &nbsp;&nbsp;<span class="kw">return</span> targetGate.<span class="fn">allowCarThrough</span>(pongalTrafficCar);<br>
    }
  </div>""",

    # 14. Debouncing
    """<div class="code-box-clean cool reveal">
    <span class="kw">function</span> <span class="fn">debounceSearch</span>(searchFunction, delay = <span class="num">300</span>) {<br>
    &nbsp;&nbsp;<span class="kw">let</span> timer;<br>
    &nbsp;&nbsp;<span class="kw">return</span> <span class="kw">function</span> (...args) {<br>
    <div class="code-line highlight-green">&nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">clearTimeout</span>(timer); <span class="cm">// Reset countdown on every keystroke</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;timer = <span class="fn">setTimeout</span>(() => { searchFunction(...args); }, delay);</div><br>
    &nbsp;&nbsp;};<br>
    }
  </div>""": """<div class="code-box-clean cool reveal">
    <span class="kw">function</span> <span class="fn">debounceTeacherDoubt</span>(doubtKetka, kaathirukumNaeram = <span class="num">300</span>) {<br>
    &nbsp;&nbsp;<span class="kw">let</span> timerCountdown;<br>
    &nbsp;&nbsp;<span class="kw">return</span> <span class="kw">function</span> (...kodu) {<br>
    <div class="code-line highlight-green">&nbsp;&nbsp;&nbsp;&nbsp;<span class="fn">clearTimeout</span>(timerCountdown); <span class="cm">// Ovvoru letter type pannumbothum reset aagum!</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">// 300ms pause panni ezhudhi mudichadhum -> Single-a Teacher call!</span><br>
    &nbsp;&nbsp;&nbsp;&nbsp;timerCountdown = <span class="fn">setTimeout</span>(() => { doubtKetka(...kodu); }, kaathirukumNaeram);</div><br>
    &nbsp;&nbsp;};<br>
    }
  </div>""",

    # 15. Caching
    """<div class="code-box-clean grn reveal">
    <span class="kw">async function</span> <span class="fn">getSwiggyMenu</span>(restaurantId) {<br>
    <div class="code-line highlight-green">&nbsp;&nbsp;<span class="kw">let</span> cachedMenu = <span class="kw">await</span> redis.<span class="fn">get</span>(<span class="str">`menu:${restaurantId}`</span>);<br>
    &nbsp;&nbsp;<span class="kw">if</span> (cachedMenu) <span class="kw">return</span> JSON.<span class="fn">parse</span>(cachedMenu); <span class="cm">// Instant 1ms Return!</span></div><br>
    &nbsp;&nbsp;<span class="kw">let</span> dbMenu = <span class="kw">await</span> postgresDB.<span class="fn">query</span>(<span class="str">"SELECT * FROM menu WHERE id = $1"</span>, [restaurantId]);<br>
    &nbsp;&nbsp;<span class="kw">await</span> redis.<span class="fn">setex</span>(<span class="str">`menu:${restaurantId}`</span>, <span class="num">1800</span>, JSON.<span class="fn">stringify</span>(dbMenu));<br>
    &nbsp;&nbsp;<span class="kw">return</span> dbMenu;<br>
    }
  </div>""": """<div class="code-box-clean grn reveal">
    <span class="kw">async function</span> <span class="fn">getDaagamThannir</span>(personId) {<br>
    <div class="code-line highlight-green">&nbsp;&nbsp;<span class="cm">// 1st check: Thinnai-la Water Pot (Redis Cache) irukka?</span><br>
    &nbsp;&nbsp;<span class="kw">let</span> thinnaiWaterPot = <span class="kw">await</span> redis.<span class="fn">get</span>(<span class="str">`water:${personId}`</span>);<br>
    &nbsp;&nbsp;<span class="kw">if</span> (thinnaiWaterPot) <span class="kw">return</span> thinnaiWaterPot; <span class="cm">// Instant 1ms sip!</span></div><br>
    &nbsp;&nbsp;<span class="cm">// Illati... Deep Well (PostgreSQL) poi water edukanum (Slow!)</span><br>
    &nbsp;&nbsp;<span class="kw">let</span> deepWellQueryData = <span class="kw">await</span> postgresDB.<span class="fn">query</span>(<span class="str">"SELECT * FROM well WHERE id = $1"</span>, [personId]);<br>
    &nbsp;&nbsp;<span class="kw">await</span> redis.<span class="fn">setex</span>(<span class="str">`water:${personId}`</span>, <span class="num">1800</span>, deepWellQueryData); <span class="cm">// Pot-la store pannu</span><br>
    &nbsp;&nbsp;<span class="kw">return</span> deepWellQueryData;<br>
    }
  </div>""",

    # 16. Pub/Sub
    """<div class="code-box-clean reveal">
    <span class="cm">// Publisher: Swiggy Order Service</span><br>
    <div class="code-line highlight-gold"><span class="kw">function</span> <span class="fn">onOrderPlaced</span>(orderData) {<br>
    &nbsp;&nbsp;messageBroker.<span class="fn">publish</span>(<span class="str">"ORDER_PLACED_EVENT"</span>, orderData);<br>
    }</div><br>
    <span class="cm">// Subscriber: Kitchen Display App</span><br>
    messageBroker.<span class="fn">subscribe</span>(<span class="str">"ORDER_PLACED_EVENT"</span>, (data) => { kitchenPrinter.<span class="fn">printToken</span>(data.items); });
  </div>""": """<div class="code-box-clean reveal">
    <span class="cm">// Publisher: Daily Press Office</span><br>
    <div class="code-line highlight-gold"><span class="kw">function</span> <span class="fn">printMorningEdition</span>(newsData) {<br>
    &nbsp;&nbsp;<span class="cm">// Delivery boy-kitta (Message Broker) papers kodukuradhu</span><br>
    &nbsp;&nbsp;paperBoyBroker.<span class="fn">publishMorningNews</span>(<span class="str">"DINAKARAN_READY"</span>, newsData);<br>
    }</div><br>
    <span class="cm">// Subscriber: Veetu kaaranga list</span><br>
    paperBoyBroker.<span class="fn">subscribersList</span>(<span class="str">"DINAKARAN_READY"</span>, (paper) => { <br>
    &nbsp;&nbsp;veedu.<span class="fn">readMorningNews</span>(paper); <span class="cm">// Automatic-a paper vizhundhudum!</span><br>
    });
  </div>"""
}

# Apply all replacements
for old_block, new_block in replacements.items():
    if old_block in content:
        content = content.replace(old_block, new_block)
    else:
        print(f"WARNING: Could not find block to replace:\n{old_block[:50]}...")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Applied {len(replacements)} code block Tanglish transformations to {file_path}")
