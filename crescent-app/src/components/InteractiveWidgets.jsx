import React, { useState } from 'react';
import { Play, RotateCcw, Check, X, Code, HelpCircle, ArrowRight, Layers, Key } from 'lucide-react';

// API submission helper
async function recordResponse(slideId, answer, isCorrect) {
  const rollNumber = localStorage.getItem('crescent_roll_number');
  if (!rollNumber) return;

  try {
    await fetch('/api/submit-quiz', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        rollNumber,
        slideId,
        answer,
        isCorrect
      })
    });
  } catch (err) {
    console.error("Failed to submit response to database:", err);
  }
}

// ================= 1. SWAPPING LIQUID CUPS =================
export function SwappingCups() {
  const [step, setStep] = useState(0);
  const totalSteps = 4;

  const nextStep = () => setStep((prev) => (prev + 1) % totalSteps);
  const reset = () => setStep(0);

  const getLiquidClass = (cupId) => {
    if (step === 0) {
      if (cupId === 'X') return 'liquid gold';
      if (cupId === 'Y') return 'liquid blue';
      return 'liquid empty';
    }
    if (step === 1) {
      if (cupId === 'X') return 'liquid empty';
      if (cupId === 'Y') return 'liquid blue';
      if (cupId === 'Temp') return 'liquid gold';
    }
    if (step === 2) {
      if (cupId === 'X') return 'liquid blue';
      if (cupId === 'Y') return 'liquid empty';
      if (cupId === 'Temp') return 'liquid gold';
    }
    if (step === 3) {
      if (cupId === 'X') return 'liquid blue';
      if (cupId === 'Y') return 'liquid gold';
      if (cupId === 'Temp') return 'liquid empty';
    }
    return 'liquid empty';
  };

  const getStepDescription = () => {
    switch (step) {
      case 0: return 'Initial State: X has Gold, Y has Blue, Temp is empty.';
      case 1: return 'Step 1: temp = x; (Move Gold from X to Temp)';
      case 2: return 'Step 2: x = y; (Move Blue from Y to X)';
      case 3: return 'Step 3: y = temp; (Move Gold from Temp to Y)';
      default: return '';
    }
  };

  return (
    <div className="widget-container">
      <div className="cup-container">
        <div className="cup">
          <div className={getLiquidClass('X')}></div>
          <div className="cup-label">Cup X</div>
        </div>
        <div className="cup">
          <div className={getLiquidClass('Temp')}></div>
          <div className="cup-label">Cup Temp</div>
        </div>
        <div className="cup">
          <div className={getLiquidClass('Y')}></div>
          <div className="cup-label">Cup Y</div>
        </div>
      </div>
      
      <div className="controls-row">
        <p className="widget-desc">{getStepDescription()}</p>
        <div className="button-group">
          <button className="widget-btn" onClick={nextStep}>
            <Play size={16} /> Step {step + 1}/{totalSteps}
          </button>
          <button className="widget-btn-secondary" onClick={reset}>
            <RotateCcw size={16} /> Reset
          </button>
        </div>
      </div>
    </div>
  );
}

// ================= 2. PIGGY BANK SUM ACCUMULATOR =================
export function SumAccumulator() {
  const [step, setStep] = useState(0);
  const totalSteps = 4;
  const values = [10, 20, 15];

  const getSum = () => {
    if (step === 0) return 0;
    if (step === 1) return 10;
    if (step === 2) return 30;
    return 45;
  };

  return (
    <div className="widget-container bank-sim">
      <h4 className="bank-title">Accumulated Total Sum</h4>
      <div className="bank-val">{getSum()}</div>
      
      <div className="bank-inputs">
        {values.map((val, idx) => (
          <div key={idx} className={`input-bubble ${step > idx ? 'added' : ''}`}>
            +{val}
          </div>
        ))}
      </div>

      <div className="controls-row" style={{ marginTop: '2rem' }}>
        <p className="widget-desc">
          {step === 0 && 'Initial: Sum = 0.'}
          {step === 1 && 'Added first input: Sum = 10.'}
          {step === 2 && 'Added second input: Sum = 10 + 20 = 30.'}
          {step === 3 && 'Final Sum: Sum = 30 + 15 = 45.'}
        </p>
        <div className="button-group">
          <button className="widget-btn" onClick={() => setStep((s) => (s + 1) % totalSteps)}>
            <Play size={16} /> {step === 3 ? 'Restart' : 'Add Input'}
          </button>
          <button className="widget-btn-secondary" onClick={() => setStep(0)}>
            <RotateCcw size={16} /> Reset
          </button>
        </div>
      </div>
    </div>
  );
}

// ================= 3. TERNARY ELIGIBILITY GATE =================
export function TernaryGate() {
  const [age, setAge] = useState(15);
  const isEligible = age >= 18;

  return (
    <div className="widget-container gate-sim">
      <div className="input-slider-container">
        <label className="bank-title">Select User Age: <span className="accent">{age}</span></label>
        <input 
          type="range" 
          min="5" 
          max="50" 
          value={age} 
          onChange={(e) => setAge(parseInt(e.target.value))} 
          className="slider"
        />
      </div>

      <div className="gate-box">
        ({age} &gt;= 18) ?
      </div>

      <div className="gate-paths">
        <div className={`gate-path ${isEligible ? 'open-even' : ''}`}>
          Eligible to Vote
        </div>
        <div className={`gate-path ${!isEligible ? 'open-odd' : ''}`}>
          Not Eligible
        </div>
      </div>
    </div>
  );
}

// ================= 4. LOOP VARIABLE TRACER =================
export function LoopTracer() {
  const [step, setStep] = useState(0);
  const totalSteps = 4;

  return (
    <div className="widget-container">
      <div className="split" style={{ marginTop: '0', alignItems: 'stretch' }}>
        <div className="code-display" style={{ flex: '1', padding: '1rem', background: '#0e0f11', border: '1px solid var(--border)', borderRadius: '8px' }}>
          <pre style={{ margin: 0, fontSize: '1rem', color: '#e2e8f0', fontFamily: 'var(--mono)' }}>
            {`for (int i = 1; i <= 3; i++) {
    printf("i is %d\\n", i);
}`}
          </pre>
        </div>
        
        <div className="console-display" style={{ flex: '1', display: 'flex', flexDirection: 'column', gap: '0.5rem', background: '#070809', border: '1px solid var(--border)', borderRadius: '8px', padding: '1.2rem' }}>
          <span className="bank-title" style={{ fontSize: '0.75rem', marginBottom: '0.5rem' }}>Terminal Output Console</span>
          {step > 0 && <div className="console-line">i is 1</div>}
          {step > 1 && <div className="console-line">i is 2</div>}
          {step > 2 && <div className="console-line">i is 3</div>}
          {step === 3 && <div className="console-line text-accent">✔ Loop Condition (i &lt;= 3) became False. Exited loop!</div>}
        </div>
      </div>

      <div className="controls-row" style={{ marginTop: '1.5rem' }}>
        <p className="widget-desc">
          {step === 0 && 'Initial: i = 1 (Checking condition 1 <= 3 ... True)'}
          {step === 1 && 'Cycle 1 done. Output printed. i incremented to 2 (Checking 2 <= 3 ... True)'}
          {step === 2 && 'Cycle 2 done. Output printed. i incremented to 3 (Checking 3 <= 3 ... True)'}
          {step === 3 && 'Cycle 3 done. Output printed. i incremented to 4 (Checking 4 <= 3 ... False!)'}
        </p>
        <div className="button-group">
          <button className="widget-btn" onClick={() => setStep((s) => (s + 1) % totalSteps)}>
            <Play size={16} /> {step === 3 ? 'Restart Trace' : 'Next Cycle'}
          </button>
          <button className="widget-btn-secondary" onClick={() => setStep(0)}>
            <RotateCcw size={16} /> Reset
          </button>
        </div>
      </div>
    </div>
  );
}

// ================= 5. ARRAY ADDRESS MATH =================
export function ArrayMath() {
  const [index, setIndex] = useState(0);
  const base = 1000;
  const multiplier = 4;
  const finalAddr = base + index * multiplier;

  return (
    <div className="widget-container">
      <div className="seat-row" style={{ display: 'flex', gap: '0.8rem', justifyContent: 'center', marginBottom: '2rem' }}>
        {[0, 1, 2, 3, 4].map((idx) => (
          <div 
            key={idx} 
            className={`seat-box ${index === idx ? 'selected' : ''}`}
            onClick={() => setIndex(idx)}
            style={{
              padding: '1.5rem',
              border: '2px solid',
              borderColor: index === idx ? 'var(--accent)' : 'var(--border)',
              borderRadius: '8px',
              textAlign: 'center',
              cursor: 'pointer',
              background: index === idx ? 'var(--accent-soft)' : 'var(--surface)',
              transition: 'all 0.3s',
              minWidth: '75px'
            }}
          >
            <div style={{ fontFamily: 'var(--mono)', fontSize: '0.85rem', color: 'var(--low)' }}>J[{idx}]</div>
            <div style={{ fontSize: '1.25rem', fontWeight: 'bold', margin: '0.4rem 0', color: 'var(--hi)' }}>
              {base + idx * multiplier}
            </div>
          </div>
        ))}
      </div>

      <div className="math-details" style={{ background: 'var(--surface)', padding: '1.5rem', borderRadius: '12px', border: '1px solid var(--border)' }}>
        <h4 className="bank-title">Address Calculation Formula</h4>
        <div style={{ fontSize: '1.8rem', fontFamily: 'var(--mono)', fontWeight: 'bold', margin: '1rem 0' }}>
          Address = base + (index × sizeof(int))
        </div>
        <div style={{ fontFamily: 'var(--mono)', fontSize: '1.25rem', color: 'var(--mid)' }}>
          Address of J[{index}] = {base} + ({index} × {multiplier}) = <span className="accent">{finalAddr}</span>
        </div>
      </div>
    </div>
  );
}

// ================= 6. RECURSION CALL STACK =================
export function RecursionStack() {
  const [step, setStep] = useState(0);
  const totalSteps = 5;

  const getStackCards = () => {
    const cards = [];
    if (step >= 1) cards.push('sumOfDigits(123) → 3 + sumOfDigits(12)');
    if (step >= 2) cards.push('sumOfDigits(12) → 2 + sumOfDigits(1)');
    if (step >= 3) cards.push('sumOfDigits(1) → 1 + sumOfDigits(0)');
    if (step >= 4) cards.push('sumOfDigits(0) → base case returns 0');
    return cards;
  };

  return (
    <div className="widget-container" style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <div className="split" style={{ marginTop: '0', alignItems: 'stretch' }}>
        <div style={{ flex: '1', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
          <h4 className="bank-title">Recursive C Function</h4>
          <pre className="code" style={{ fontSize: '0.95rem', padding: '1.2rem', marginTop: '0.6rem' }}>
{`int sumOfDigits(int n) {
    if (n == 0) return 0;
    return (n % 10) + sumOfDigits(n / 10);
}`}
          </pre>
        </div>

        <div style={{ flex: '1', display: 'flex', flexDirection: 'column' }}>
          <h4 className="bank-title" style={{ marginBottom: '1rem' }}>Call Stack Memory Frames</h4>
          <div className="stack-container" style={{ flex: '1', minHeight: '220px' }}>
            {getStackCards().map((text, idx) => (
              <div key={idx} className="stack-card active" style={{ transitionDelay: `${idx * 0.1}s` }}>
                {text}
              </div>
            ))}
            {step === 0 && (
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '180px', color: 'var(--low)', border: '2px dashed var(--border)', borderRadius: '8px', fontSize: '1rem' }}>
                Stack is empty. Click Step to invoke function.
              </div>
            )}
          </div>
        </div>
      </div>

      <div className="controls-row">
        <p className="widget-desc">
          {step === 0 && 'Initial: Click Step to start recursion with input n = 123.'}
          {step === 1 && 'Call sumOfDigits(123): (123 % 10) is 3, calls sumOfDigits(12).'}
          {step === 2 && 'Call sumOfDigits(12): (12 % 10) is 2, calls sumOfDigits(1).'}
          {step === 3 && 'Call sumOfDigits(1): (1 % 10) is 1, calls sumOfDigits(0).'}
          {step === 4 && 'Base Case: n is 0. Returns 0, winding back: 0 + 1 + 2 + 3 = 6!'}
        </p>
        <div className="button-group">
          <button className="widget-btn" onClick={() => setStep((s) => (s + 1) % totalSteps)}>
            <Play size={16} /> {step === 4 ? 'Restart Stack' : 'Next Frame'}
          </button>
          <button className="widget-btn-secondary" onClick={() => setStep(0)}>
            <RotateCcw size={16} /> Reset
          </button>
        </div>
      </div>
    </div>
  );
}

// ================= 7. POINTER INDEX VISUALIZER =================
export function PointerVisualizer() {
  const [step, setStep] = useState(0);
  const totalSteps = 4;
  const addresses = [1000, 1004, 1008];
  const values = [10, 20, 30];

  return (
    <div className="widget-container" style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      <div className="ptr-visualizer" style={{ width: '100%', maxWidth: '600px', margin: '0 auto' }}>
        {values.map((val, idx) => (
          <div key={idx} className={`ptr-box ${step === idx ? 'focused' : ''}`} style={{ borderColor: step === idx ? 'var(--accent)' : 'var(--border)' }}>
            <span style={{ color: 'var(--low)', fontSize: '0.95rem' }}>
              arr[{idx}] (Address: <span className="accent">{addresses[idx]}</span>)
            </span>
            <span style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
              {step === idx && (
                <span className="accent" style={{ fontWeight: 'bold', fontSize: '1rem', animation: 'pulse 1.5s infinite' }}>
                  *ptr →
                </span>
              )}
              <span className="mono" style={{ fontSize: '1.3rem', fontWeight: 'bold' }}>{val}</span>
            </span>
          </div>
        ))}
      </div>

      <div className="controls-row">
        <p className="widget-desc">
          {step === 0 && 'ptr points to arr[0]. Address is 1000, value is 10.'}
          {step === 1 && 'ptr incremented by 1 (ptr+1). Address jumps by 4 bytes to 1004, value is 20.'}
          {step === 2 && 'ptr incremented by 2 (ptr+2). Address is 1008, value is 30.'}
          {step === 3 && 'Loop finished! Pointer traversed all 3 array elements successfully.'}
        </p>
        <div className="button-group">
          <button className="widget-btn" onClick={() => setStep((s) => (s + 1) % totalSteps)}>
            <Play size={16} /> {step === 3 ? 'Restart Traversal' : 'Increment Pointer'}
          </button>
          <button className="widget-btn-secondary" onClick={() => setStep(0)}>
            <RotateCcw size={16} /> Reset
          </button>
        </div>
      </div>
    </div>
  );
}

// ================= 8. INTERACTIVE QUIZ CARD =================
export function QuizCard({ slideId, question, options }) {
  const [selectedIdx, setSelectedIdx] = useState(null);
  const [isAnswered, setIsAnswered] = useState(false);

  const handleSelect = (idx) => {
    if (isAnswered) return;
    setSelectedIdx(idx);
    setIsAnswered(true);
    
    // Background database submission
    recordResponse(slideId || question, options[idx].text, options[idx].correct);
  };

  const reset = () => {
    setSelectedIdx(null);
    setIsAnswered(false);
  };

  return (
    <div className="card-quiz">
      <div className="card-question">{question}</div>
      <div className="card-buttons">
        {options.map((opt, idx) => (
          <button 
            key={idx}
            className={`quiz-btn ${isAnswered ? (opt.correct ? 'correct' : selectedIdx === idx ? 'incorrect' : '') : ''}`}
            onClick={() => handleSelect(idx)}
            disabled={isAnswered}
          >
            {opt.text}
          </button>
        ))}
      </div>

      {isAnswered && (
        <div className="card-feedback" style={{ opacity: 1, color: options[selectedIdx]?.correct ? 'var(--green)' : 'var(--rose)' }}>
          {options[selectedIdx]?.correct ? <Check size={18} inline="true" style={{ marginRight: '0.4rem', verticalAlign: 'middle' }} /> : <X size={18} inline="true" style={{ marginRight: '0.4rem', verticalAlign: 'middle' }} />}
          {options[selectedIdx]?.feedback || (options[selectedIdx]?.correct ? 'Correct Answer!' : 'Incorrect, try again!')}
        </div>
      )}

      {isAnswered && (
        <button className="widget-btn-secondary" onClick={reset} style={{ marginTop: '1.5rem', marginInline: 'auto' }}>
          <RotateCcw size={14} /> Reset Quiz
        </button>
      )}
    </div>
  );
}

// ================= 9. CODE COMPLETION BLANKS =================
export function CodeBlank({ slideId, code, blankVal }) {
  const [solved, setSolved] = useState(false);

  const handleSolve = () => {
    if (solved) return;
    setSolved(true);
    
    // Record solved check in database
    recordResponse(slideId || 'Code Blank', blankVal, true);
  };

  return (
    <div className="widget-container" style={{ textAlign: 'center' }}>
      <pre className="code" style={{ textAlign: 'left', display: 'inline-block', minWidth: '450px', fontSize: '1.25rem', padding: '2rem' }}>
        {code.split('______').map((part, index) => (
          <React.Fragment key={index}>
            {part}
            {index === 0 && (
              <span 
                className={`blank-fill ${solved ? 'solved' : ''}`}
                onClick={handleSolve}
              >
                {solved ? blankVal : '______'}
              </span>
            )}
          </React.Fragment>
        ))}
      </pre>
      <div style={{ marginTop: '1.5rem', color: 'var(--low)', fontSize: '1.1rem' }}>
        {solved ? (
          <span style={{ color: 'var(--green)', fontWeight: 'bold' }}>✔ Solved! click Reset to try again.</span>
        ) : (
          <span>💡 Click the dashed blank space inside the code block to complete it.</span>
        )}
      </div>

      {solved && (
        <button className="widget-btn-secondary" onClick={() => setSolved(false)} style={{ marginTop: '1rem', marginInline: 'auto' }}>
          <RotateCcw size={14} /> Reset Blank
        </button>
      )}
    </div>
  );
}

// ================= 10. TO-DO PRACTICE CARD =================
export function TodoCard({ title, desc, hint }) {
  const [showHint, setShowHint] = useState(false);

  return (
    <div className="todo-card">
      <div className="todo-title">To-Do Exercise 🧑‍💻</div>
      <div className="todo-text">{title}</div>
      <p style={{ color: 'var(--mid)', fontSize: '1.2rem', lineHeight: '1.6', marginBottom: '1.5rem' }}>{desc}</p>
      
      {showHint ? (
        <div className="todo-hint" style={{ animation: 'fadeIn 0.5s' }}>
          <strong>Implementation Guidelines:</strong> {hint}
        </div>
      ) : (
        <button className="widget-btn-secondary" onClick={() => setShowHint(true)}>
          <HelpCircle size={16} /> Show Hint
        </button>
      )}
    </div>
  );
}

// ================= 11. STRING GARLAND VISUALIZER =================
export function StringGarland() {
  const [step, setStep] = useState(0);
  const chars = ['H', 'I', '\\0'];
  const totalSteps = 4;

  return (
    <div className="widget-container" style={{ textAlign: 'center' }}>
      <div className="garland" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '1rem', marginBottom: '2rem' }}>
        {chars.map((char, idx) => (
          <div 
            key={idx}
            className={`garland-flower ${step > idx ? 'checked' : step === idx ? 'checking' : ''}`}
            style={{
              padding: '1.5rem',
              borderRadius: '50%',
              width: '80px',
              height: '80px',
              display: 'flex',
              flexDirection: 'column',
              justifyContent: 'center',
              alignItems: 'center',
              border: '2px solid',
              borderColor: step === idx ? 'var(--accent)' : 'var(--border)',
              background: step === idx ? 'var(--accent-soft)' : 'var(--surface)',
              transition: 'all 0.4s'
            }}
          >
            <span className="mono" style={{ fontSize: '1.5rem', fontWeight: 'bold', color: char === '\\0' ? 'var(--rose)' : 'var(--hi)' }}>{char}</span>
            <span style={{ fontSize: '0.75rem', color: 'var(--low)' }}>index {idx}</span>
          </div>
        ))}
      </div>

      <div className="controls-row">
        <p className="widget-desc">
          {step === 0 && "Reading msg[0]: Character is 'H'. Condition msg[0] != '\\0' matches... loop continues!"}
          {step === 1 && "Reading msg[1]: Character is 'I'. Condition msg[1] != '\\0' matches... loop continues!"}
          {step === 2 && "Reading msg[2]: Hit the Null Terminator '\\0'! Loop condition becomes False... terminated!"}
          {step === 3 && 'Traversed completed. Output printed to console successfully.'}
        </p>
        <div className="button-group">
          <button className="widget-btn" onClick={() => setStep((s) => (s + 1) % totalSteps)}>
            <Play size={16} /> {step === 3 ? 'Restart Trace' : 'Next Character'}
          </button>
          <button className="widget-btn-secondary" onClick={() => setStep(0)}>
            <RotateCcw size={16} /> Reset
          </button>
        </div>
      </div>
    </div>
  );
}
