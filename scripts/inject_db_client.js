const fs = require('fs');
const path = require('path');

const HTML_FILES = [
  path.join(__dirname, '../HTML/C Programming/Introduction to C - Crescent.html'),
  path.join(__dirname, '../HTML/C Programming/Control Structures and Arrays - Crescent.html'),
  path.join(__dirname, '../HTML/C Programming/C Programming Lab Activity Deck - Crescent.html')
];

const injection = `
<!-- DATABASE CHECKIN OVERLAY -->
<div id="checkin-overlay" style="position:fixed;inset:0;background:rgba(0,0,0,0.92);backdrop-filter:blur(8px);display:flex;align-items:center;justify-content:center;z-index:9999;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;color:#fff;">
  <form id="checkin-form" style="background:#0e0f11;border:1px solid rgba(251,191,36,0.15);padding:3rem;border-radius:16px;max-width:420px;width:100%;text-align:center;box-shadow:0 25px 60px rgba(0,0,0,0.8);">
    <div style="font-size:3rem;margin-bottom:0.5rem;">🎓</div>
    <h2 style="margin-bottom:0.5rem;font-size:1.8rem;font-weight:700;">Classroom Check-in</h2>
    <p style="color:#64748b;font-size:0.95rem;margin-bottom:1.5rem;">Register your roll number and name to track slide activities.</p>
    
    <div style="text-align:left;margin-bottom:1rem;">
      <label style="font-family:monospace;font-size:0.75rem;color:#64748b;text-transform:uppercase;letter-spacing:0.05em;display:block;margin-bottom:0.4rem;">Roll Number</label>
      <input type="text" id="chk-roll" placeholder="e.g. 23CSE01" required style="width:100%;padding:0.75rem 1rem;background:#181a1f;border:1px solid rgba(255,255,255,0.08);color:#fff;border-radius:6px;outline:none;font-size:1rem;">
    </div>
    
    <div style="text-align:left;margin-bottom:1.5rem;">
      <label style="font-family:monospace;font-size:0.75rem;color:#64748b;text-transform:uppercase;letter-spacing:0.05em;display:block;margin-bottom:0.4rem;">Student Name</label>
      <input type="text" id="chk-name" placeholder="e.g. Arun Kumar" required style="width:100%;padding:0.75rem 1rem;background:#181a1f;border:1px solid rgba(255,255,255,0.08);color:#fff;border-radius:6px;outline:none;font-size:1rem;">
    </div>
    
    <button type="submit" style="width:100%;padding:0.8rem;background:#fbbf24;color:#000;border:none;border-radius:6px;font-weight:700;font-size:1rem;cursor:pointer;transition:background 0.2s;">Register & Enter</button>
    <button type="button" id="chk-skip" style="width:100%;padding:0.8rem;background:transparent;color:#64748b;border:1px solid rgba(255,255,255,0.08);border-radius:6px;margin-top:0.8rem;cursor:pointer;font-size:0.95rem;">Presenter View</button>
  </form>
</div>

<style>
.code .num { color: #f43f5e !important; }
.code .inc { color: #fb923c !important; }
.code .type { color: #60a5fa !important; font-weight: 700; }
.code .op { color: #fcd34d !important; }
</style>

<script>
(function() {
  const overlay = document.getElementById('checkin-overlay');
  const form = document.getElementById('checkin-form');
  const rollInput = document.getElementById('chk-roll');
  const nameInput = document.getElementById('chk-name');
  const skipBtn = document.getElementById('chk-skip');

  const checkStatus = () => {
    const roll = localStorage.getItem('crescent_roll_number');
    const name = localStorage.getItem('crescent_name');
    const skip = localStorage.getItem('crescent_presenter_view');
    if ((roll && name) || skip === 'true') {
      overlay.style.display = 'none';
    }
  };

  checkStatus();

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const roll = rollInput.value.trim().toUpperCase();
    const name = nameInput.value.trim();
    
    try {
      const res = await fetch('/api/checkin', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rollNumber: roll, name })
      });
      if (res.ok) {
        localStorage.setItem('crescent_roll_number', roll);
        localStorage.setItem('crescent_name', name);
        localStorage.removeItem('crescent_presenter_view');
        overlay.style.display = 'none';
      } else {
        alert('Check-in failed. Please try again.');
      }
    } catch (err) {
      alert('Connection error. Please try again.');
    }
  });

  skipBtn.addEventListener('click', () => {
    localStorage.setItem('crescent_presenter_view', 'true');
    localStorage.removeItem('crescent_roll_number');
    localStorage.removeItem('crescent_name');
    overlay.style.display = 'none';
  });

  // Inject quiz click tracking
  window.recordResponse = async function(slideId, answer, isCorrect) {
    const roll = localStorage.getItem('crescent_roll_number');
    if (!roll) return;
    try {
      await fetch('/api/submit-quiz', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ rollNumber: roll, slideId, answer, isCorrect })
      });
    } catch (err) {
      console.error(err);
    }
  };

  // Override verifyCard and solveBlank if they exist
  setTimeout(() => {
    const originalVerifyCard = window.verifyCard;
    window.verifyCard = function(btn, isCorrect, feedbackText) {
      if (originalVerifyCard) {
        originalVerifyCard(btn, isCorrect, feedbackText);
      }
      const cardQuestion = btn.closest('.card-quiz')?.querySelector('.card-question')?.textContent || 'Quiz Card';
      window.recordResponse(cardQuestion, btn.textContent, isCorrect);
    };

    const originalSolveBlank = window.solveBlank;
    window.solveBlank = function(el, val) {
      if (originalSolveBlank) {
        originalSolveBlank(el, val);
      }
      const blankTitle = el.closest('.slide')?.querySelector('.title')?.textContent || 'Code Blank';
      window.recordResponse(blankTitle, val, true);
    };
  }, 100);

  // Client-side C Code Syntax Highlighter
  const highlightCode = () => {
    const codeBlocks = document.querySelectorAll('pre.code, code.code, pre.code-template');
    codeBlocks.forEach(block => {
      if (block.querySelector('span.kw') || block.querySelector('span.type')) return;

      let html = block.innerHTML;

      // Comments
      html = html.replace(/(\\/\\*[\\s\\S]*?\\*\\/)/g, '<span class="cm">$1</span>');
      html = html.replace(/(\\/\\/.*)/g, '<span class="cm">$1</span>');

      // Double quoted strings
      html = html.replace(/(".*?")/g, '<span class="str">$1</span>');

      // Preprocessor
      html = html.replace(/(#include|#define)/g, '<span class="kw">$1</span>');

      // Header imports
      html = html.replace(/(&lt;[a-zA-Z0-9_\\.]+\\.h&gt;)/g, '<span class="inc">$1</span>');

      // Keywords
      const keywords = ['return', 'if', 'else', 'for', 'while', 'do', 'switch', 'case', 'break', 'continue', 'struct', 'union', 'typedef', 'const', 'static'];
      keywords.forEach(kw => {
        const regex = new RegExp(\`\\\\b\${kw}\\\\b\`, 'g');
        html = html.replace(regex, \`<span class="kw">\${kw}</span>\`);
      });

      // Types
      const types = ['int', 'float', 'char', 'double', 'void', 'unsigned', 'signed', 'long', 'short'];
      types.forEach(t => {
        const regex = new RegExp(\`\\\\b\${t}\\\\b\`, 'g');
        html = html.replace(regex, \`<span class="type">\${t}</span>\`);
      });

      // Common functions
      html = html.replace(/\\b(printf|scanf|main|malloc|free|exit|pow|sqrt)\\b/g, '<span class="fn">$1</span>');

      // Numbers
      html = html.replace(/\\b(\\d+)\\b/g, '<span class="num">$1</span>');

      block.innerHTML = html;
    });
  };

  setTimeout(highlightCode, 100);
})();
</script>
`;

HTML_FILES.forEach(filePath => {
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    return;
  }
  
  let html = fs.readFileSync(filePath, 'utf8');
  
  // Strip any previous checkin overlay to prevent duplication
  html = html.replace(/<!-- DATABASE CHECKIN OVERLAY -->[\s\S]*?<\/body>/, '</body>');
  
  // Inject the new overlay
  html = html.replace('</body>', () => injection + '\n</body>');
  
  fs.writeFileSync(filePath, html, 'utf8');
  console.log(`Successfully injected database check-in to ${path.basename(filePath)}`);
});
