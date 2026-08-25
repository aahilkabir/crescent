import React, { useState, useEffect } from 'react';
import { Play, RotateCcw, ChevronRight, Terminal, Layers, Info, CheckCircle2, XCircle } from 'lucide-react';

const EXERCISES = [
  {
    id: 1,
    title: "Ex 1: Simple Interest",
    desc: "Compute simple interest based on Principal, Rate, and Time inputs.",
    inputs: [
      { name: "Principal (P)", key: "p", default: "10000" },
      { name: "Rate of Interest (R)", key: "r", default: "5" },
      { name: "Time in Years (T)", key: "t", default: "2" }
    ],
    starter: `#include <stdio.h>

int main() {
    float principal, rate, time, interest;
    
    // TODO: Read inputs and compute interest
    principal = 10000.0;
    rate = 5.0;
    time = 2.0;
    
    interest = (principal * rate * time) / 100.0;
    
    printf("Simple Interest = %.2f\\n", interest);
    return 0;
}`,
    validate: (code) => {
      if (!code.includes('#include')) return "Missing preprocessor #include <stdio.h>";
      if (!code.includes('principal') || !code.includes('rate') || !code.includes('time')) return "You must declare variables: principal, rate, time";
      if (!code.includes('/') || !code.includes('*')) return "Missing formula logic: (P * R * T) / 100";
      return null;
    },
    run: (inputs) => {
      const p = parseFloat(inputs.p || 10000);
      const r = parseFloat(inputs.r || 5);
      const t = parseFloat(inputs.t || 2);
      const interest = (p * r * t) / 100.0;
      
      return {
        console: [
          `P = ${p}`,
          `R = ${r}%`,
          `T = ${t} years`,
          `Formula: (${p} * ${r} * ${t}) / 100`,
          `Simple Interest = ${interest.toFixed(2)}`
        ],
        ram: [
          { name: "principal", addr: "1000", val: p },
          { name: "rate", addr: "1004", val: r },
          { name: "time", addr: "1008", val: t },
          { name: "interest", addr: "1012", val: interest }
        ]
      };
    }
  },
  {
    id: 2,
    title: "Ex 2: Quadratic Roots",
    desc: "Calculate mathematical roots for coefficients a, b, and c.",
    inputs: [
      { name: "Coefficient a", key: "a", default: "1" },
      { name: "Coefficient b", key: "b", default: "-5" },
      { name: "Coefficient c", key: "c", default: "6" }
    ],
    starter: `#include <stdio.h>
#include <math.h>

int main() {
    float a, b, c, disc, r1, r2;
    
    a = 1.0;
    b = -5.0;
    c = 6.0;
    
    disc = b*b - 4*a*c;
    r1 = (-b + sqrt(disc)) / (2*a);
    r2 = (-b - sqrt(disc)) / (2*a);
    
    printf("Roots are: %.2f and %.2f\\n", r1, r2);
    return 0;
}`,
    validate: (code) => {
      if (!code.includes('math.h')) return "Missing math library #include <math.h>";
      if (!code.includes('disc') || !code.includes('sqrt')) return "Missing discriminant (b*b - 4*a*c) or square root calculation.";
      return null;
    },
    run: (inputs) => {
      const a = parseFloat(inputs.a || 1);
      const b = parseFloat(inputs.b || -5);
      const c = parseFloat(inputs.c || 6);
      const disc = b*b - 4*a*c;
      
      if (disc < 0) {
        return {
          console: ["Discriminant is negative. Roots are imaginary."],
          ram: [
            { name: "a", addr: "1000", val: a },
            { name: "b", addr: "1004", val: b },
            { name: "c", addr: "1008", val: c },
            { name: "disc", addr: "1012", val: disc }
          ]
        };
      }
      
      const r1 = (-b + Math.sqrt(disc)) / (2*a);
      const r2 = (-b - Math.sqrt(disc)) / (2*a);
      
      return {
        console: [
          `Coefficients: a=${a}, b=${b}, c=${c}`,
          `Discriminant = ${disc}`,
          `Root 1 = ${r1.toFixed(2)}`,
          `Root 2 = ${r2.toFixed(2)}`
        ],
        ram: [
          { name: "a", addr: "1000", val: a },
          { name: "b", addr: "1004", val: b },
          { name: "c", addr: "1008", val: c },
          { name: "disc", addr: "1012", val: disc },
          { name: "r1", addr: "1016", val: r1 },
          { name: "r2", addr: "1020", val: r2 }
        ]
      };
    }
  },
  {
    id: 3,
    title: "Ex 3: Largest of Three",
    desc: "Determine the maximum value among three integers.",
    inputs: [
      { name: "Number A", key: "a", default: "15" },
      { name: "Number B", key: "b", default: "45" },
      { name: "Number C", key: "c", default: "20" }
    ],
    starter: `#include <stdio.h>

int main() {
    int a = 15, b = 45, c = 20;
    
    if (a >= b && a >= c) {
        printf("Largest is %d\\n", a);
    } else if (b >= a && b >= c) {
        printf("Largest is %d\\n", b);
    } else {
        printf("Largest is %d\\n", c);
    }
    return 0;
}`,
    validate: (code) => {
      if (!code.includes('if') || !code.includes('else')) return "You must use if-else conditional branches.";
      return null;
    },
    run: (inputs) => {
      const a = parseInt(inputs.a || 15);
      const b = parseInt(inputs.b || 45);
      const c = parseInt(inputs.c || 20);
      const largest = Math.max(a, b, c);
      
      return {
        console: [
          `Inputs: A=${a}, B=${b}, C=${c}`,
          `Checking if-else gates...`,
          `Largest is: ${largest}`
        ],
        ram: [
          { name: "a", addr: "1000", val: a },
          { name: "b", addr: "1004", val: b },
          { name: "c", addr: "1008", val: c },
          { name: "largest", addr: "1012", val: largest }
        ]
      };
    }
  },
  {
    id: 5,
    title: "Ex 5: Swapping Values",
    desc: "Swap values of two integer variables using a temporary third storage.",
    inputs: [
      { name: "Variable X", key: "x", default: "10" },
      { name: "Variable Y", key: "y", default: "20" }
    ],
    starter: `#include <stdio.h>

int main() {
    int x = 10, y = 20, temp;
    
    // Swap logic
    temp = x;
    x = y;
    y = temp;
    
    printf("Swapped: X=%d, Y=%d\\n", x, y);
    return 0;
}`,
    validate: (code) => {
      if (!code.includes('temp')) return "You must declare a 'temp' storage variable.";
      if (!code.includes('temp =') || !code.includes('y = temp')) return "Missing swapping logic mapping.";
      return null;
    },
    run: (inputs) => {
      const x = parseInt(inputs.x || 10);
      const y = parseInt(inputs.y || 20);
      
      return {
        console: [
          `Initial: X = ${x}, Y = ${y}`,
          `temp = X (temp is now ${x})`,
          `X = Y (X is now ${y})`,
          `Y = temp (Y is now ${x})`,
          `Swapped Result: X = ${y}, Y = ${x}`
        ],
        ram: [
          { name: "x", addr: "1000", val: y },
          { name: "y", addr: "1004", val: x },
          { name: "temp", addr: "1008", val: x }
        ]
      };
    }
  },
  {
    id: 6,
    title: "Ex 6: Factorial Loop",
    desc: "Compute the factorial of a positive number using while loops.",
    inputs: [
      { name: "Input Number (N)", key: "n", default: "5" }
    ],
    starter: `#include <stdio.h>

int main() {
    int n = 5, fact = 1, i = 1;
    
    while (i <= n) {
        fact = fact * i;
        i++;
      }
      
    printf("Factorial of %d = %d\\n", n, fact);
    return 0;
}`,
    validate: (code) => {
      if (!code.includes('while')) return "Missing while iteration loop.";
      return null;
    },
    run: (inputs) => {
      const n = parseInt(inputs.n || 5);
      let fact = 1;
      let i = 1;
      const history = [];

      while (i <= n) {
        fact *= i;
        history.push(`Cycle i=${i}: fact = ${fact}`);
        i++;
      }

      return {
        console: [
          `Calculating factorial of ${n}...`,
          ...history,
          `Result: Factorial of ${n} = ${fact}`
        ],
        ram: [
          { name: "n", addr: "1000", val: n },
          { name: "fact", addr: "1004", val: fact },
          { name: "i", addr: "1008", val: i }
        ]
      };
    }
  },
  {
    id: 15,
    title: "Ex 15: String Length",
    desc: "Calculate length of a string manually without using strlen library.",
    inputs: [
      { name: "Enter Text", key: "text", default: "Crescent" }
    ],
    starter: `#include <stdio.h>

int main() {
    char str[] = "Crescent";
    int length = 0;
    
    while (str[length] != '\\0') {
        length++;
    }
    
    printf("Length = %d\\n", length);
    return 0;
}`,
    validate: (code) => {
      if (code.includes('strlen')) return "Do not use strlen! Implement a character array loop checking for '\\0'.";
      if (!code.includes('\\0')) return "Missing null terminator '\\0' boundary check.";
      return null;
    },
    run: (inputs) => {
      const text = inputs.text || "Crescent";
      const length = text.length;
      const history = [];

      for (let idx = 0; idx < length; idx++) {
        history.push(`Index ${idx}: '${text[idx]}' != '\\0'`);
      }
      history.push(`Index ${length}: hit '\\0' -> Loop Exited.`);

      return {
        console: [
          `Input String: "${text}"`,
          ...history,
          `Result: Length = ${length}`
        ],
        ram: [
          { name: "str", addr: "1000", val: `"${text}"` },
          { name: "length", addr: "1024", val: length }
        ]
      };
    }
  }
];

export default function CodePlayground() {
  const [selectedExId, setSelectedExId] = useState(1);
  const [code, setCode] = useState('');
  const [inputs, setInputs] = useState({});
  const [validationError, setValidationError] = useState('');
  const [consoleOutput, setConsoleOutput] = useState([]);
  const [ramCells, setRamCells] = useState([]);
  const [isRunning, setIsRunning] = useState(false);

  const activeEx = EXERCISES.find(ex => ex.id === selectedExId) || EXERCISES[0];

  // Set starter code when exercise changes
  useEffect(() => {
    setCode(activeEx.starter);
    setValidationError('');
    setConsoleOutput(['Console cleared. Select "Run Simulation" to execute.']);
    setRamCells([]);
    
    // Set default inputs
    const defaults = {};
    activeEx.inputs.forEach(inp => {
      defaults[inp.key] = inp.default;
    });
    setInputs(defaults);
  }, [selectedExId]);

  const handleInputChange = (key, val) => {
    setInputs(prev => ({ ...prev, [key]: val }));
  };

  const runSimulation = () => {
    setValidationError('');
    setIsRunning(true);
    
    // Simulate compilation delay
    setTimeout(() => {
      // 1. Run local validation checks
      const err = activeEx.validate(code);
      if (err) {
        setValidationError(err);
        setConsoleOutput([`⛔ Compile Error:`, err]);
        setIsRunning(false);
        return;
      }

      // 2. Run simulation logic
      const result = activeEx.run(inputs);
      setConsoleOutput(result.console);
      setRamCells(result.ram);
      setIsRunning(false);
    }, 600);
  };

  return (
    <div style={{ flex: '1', display: 'flex', overflow: 'hidden', padding: '2rem 3vw', gap: '2rem', height: 'calc(100vh - 75px)', background: 'var(--black)' }}>
      {/* EXERCISE SELECTION LIST */}
      <aside style={{
        width: '260px',
        background: 'var(--surface)',
        border: '1px solid var(--border)',
        borderRadius: '12px',
        padding: '1.2rem',
        display: 'flex',
        flexDirection: 'column',
        gap: '0.8rem'
      }}>
        <span className="bank-title" style={{ fontSize: '0.9rem', marginBottom: '0.4rem' }}>Practice Problems</span>
        <div style={{ flex: '1', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
          {EXERCISES.map(ex => (
            <button
              key={ex.id}
              onClick={() => setSelectedExId(ex.id)}
              style={{
                width: '100%',
                background: selectedExId === ex.id ? 'var(--accent-soft)' : 'var(--surface2)',
                color: selectedExId === ex.id ? 'var(--accent)' : 'var(--mid)',
                border: '1px solid',
                borderColor: selectedExId === ex.id ? 'var(--border-hi)' : 'transparent',
                padding: '0.8rem',
                borderRadius: '8px',
                textAlign: 'left',
                cursor: 'pointer',
                fontFamily: 'var(--sans)',
                fontWeight: '600',
                fontSize: '0.95rem',
                transition: 'all 0.2s'
              }}
            >
              {ex.title}
            </button>
          ))}
        </div>
      </aside>

      {/* CODE EDITOR WORKSPACE */}
      <main style={{ flex: '1.4', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
        <div style={{ background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: '12px', padding: '1.5rem', flex: '1', display: 'flex', flexDirection: 'column' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
            <div>
              <h3 style={{ fontFamily: 'var(--serif)', fontSize: '1.5rem', color: 'var(--hi)' }}>{activeEx.title}</h3>
              <p style={{ fontSize: '0.9rem', color: 'var(--low)', marginTop: '0.2rem' }}>{activeEx.desc}</p>
            </div>
            <button 
              onClick={runSimulation}
              disabled={isRunning}
              style={{
                background: 'var(--accent)',
                color: 'var(--black)',
                fontWeight: '700',
                padding: '0.6rem 1.2rem',
                borderRadius: '6px',
                border: 'none',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '0.4rem'
              }}
            >
              <Play size={16} /> {isRunning ? 'Compiling...' : 'Run Code'}
            </button>
          </div>

          {/* INPUT FIELDS CONTROL PANEL */}
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '1rem', background: 'var(--surface2)', padding: '1rem', borderRadius: '8px', marginBottom: '1rem' }}>
            {activeEx.inputs.map(inp => (
              <div key={inp.key} style={{ display: 'flex', flexDirection: 'column', gap: '0.3rem' }}>
                <span style={{ fontSize: '0.75rem', fontFamily: 'var(--mono)', color: 'var(--low)' }}>{inp.name}</span>
                <input 
                  type="text" 
                  value={inputs[inp.key] || ''}
                  onChange={(e) => handleInputChange(inp.key, e.target.value)}
                  style={{
                    background: 'var(--surface3)',
                    border: '1px solid var(--border)',
                    borderRadius: '4px',
                    color: 'var(--hi)',
                    padding: '0.4rem 0.6rem',
                    fontSize: '0.9rem',
                    width: '140px',
                    outline: 'none'
                  }}
                />
              </div>
            ))}
          </div>

          {/* CODE EDITOR TEXTAREA */}
          <div style={{ flex: '1', position: 'relative', borderRadius: '8px', overflow: 'hidden', border: '1px solid var(--border)' }}>
            <textarea
              value={code}
              onChange={(e) => setCode(e.target.value)}
              style={{
                width: '100%',
                height: '100%',
                background: '#0a0b0d',
                color: '#e2e8f0',
                fontFamily: 'var(--mono)',
                fontSize: '1rem',
                padding: '1.2rem',
                border: 'none',
                outline: 'none',
                resize: 'none',
                lineHeight: '1.6'
              }}
            />
          </div>
        </div>
      </main>

      {/* TERMINAL CONSOLE & RAM TRACKER */}
      <section style={{ flex: '1.1', display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
        
        {/* INTERACTIVE TERMINAL CONSOLE */}
        <div style={{ flex: '1', background: '#050607', border: '1px solid var(--border)', borderRadius: '12px', padding: '1.5rem', display: 'flex', flexDirection: 'column' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--accent)', marginBottom: '1rem' }}>
            <Terminal size={18} />
            <span style={{ fontSize: '0.85rem', fontFamily: 'var(--mono)', fontWeight: 'bold', letterSpacing: '0.12em' }}>SIMULATED CONSOLE</span>
          </div>
          <div style={{ flex: '1', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '0.4rem', fontFamily: 'var(--mono)', fontSize: '0.95rem' }}>
            {consoleOutput.map((line, idx) => {
              const isError = line.startsWith('⛔') || line.startsWith('❌');
              const isSuccess = line.startsWith('✔');
              return (
                <div 
                  key={idx} 
                  style={{
                    color: isError ? 'var(--rose)' : isSuccess ? 'var(--green)' : 'var(--mid)',
                    borderLeft: isError ? '3px solid var(--rose)' : 'none',
                    paddingLeft: isError ? '0.5rem' : '0'
                  }}
                >
                  {line}
                </div>
              );
            })}
          </div>
        </div>

        {/* LIVE RAM VARIABLE STORAGE GRID */}
        <div style={{ flex: '1', background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: '12px', padding: '1.5rem', display: 'flex', flexDirection: 'column' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--blue)', marginBottom: '1rem' }}>
            <Layers size={18} />
            <span style={{ fontSize: '0.85rem', fontFamily: 'var(--mono)', fontWeight: 'bold', letterSpacing: '0.12em' }}>RAM MEMORY TABLE</span>
          </div>
          <div style={{ flex: '1', overflowY: 'auto' }}>
            {ramCells.length === 0 ? (
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100%', color: 'var(--low)', border: '2px dashed var(--border)', borderRadius: '8px', fontSize: '0.9rem' }}>
                RAM is empty. Run correct code to register variables.
              </div>
            ) : (
              <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontFamily: 'var(--mono)' }}>
                <thead>
                  <tr style={{ borderBottom: '1px solid var(--border-hi)', color: 'var(--blue)', fontSize: '0.8rem' }}>
                    <th style={{ padding: '0.6rem' }}>Variable</th>
                    <th style={{ padding: '0.6rem' }}>Address (HEX)</th>
                    <th style={{ padding: '0.6rem' }}>Value</th>
                  </tr>
                </thead>
                <tbody>
                  {ramCells.map((cell, idx) => (
                    <tr key={idx} style={{ borderBottom: '1px solid var(--border)', fontSize: '0.95rem' }} className="table-row-hover">
                      <td style={{ padding: '0.6rem', color: 'var(--hi)', fontWeight: 'bold' }}>{cell.name}</td>
                      <td style={{ padding: '0.6rem', color: 'var(--low)' }}>0x{cell.addr}</td>
                      <td style={{ padding: '0.6rem', color: 'var(--accent)', fontWeight: 'bold' }}>{cell.val}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </div>
        </div>

      </section>
    </div>
  );
}
