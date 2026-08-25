const fs = require('fs');
const path = require('path');
const vm = require('vm');

const htmlPath = path.join(__dirname, '../HTML/C Programming/Introduction to C - Crescent.html');
const html = fs.readFileSync(htmlPath, 'utf8');

// Find script tags
const scriptRegex = /<script>([\s\S]*?)<\/script>/gi;
let match;
let index = 1;

while ((match = scriptRegex.exec(html)) !== null) {
  const code = match[1];
  console.log(`Checking script block #${index}...`);
  try {
    new vm.Script(code);
    console.log(`Script block #${index} is syntactically correct.`);
  } catch (err) {
    console.error(`Syntax Error in script block #${index}:`);
    console.error(err.message);
    // Find the line number of error
    const lines = code.split('\n');
    const errLine = err.stack.match(/evalmachine\.<anonymous>:(\d+)/);
    if (errLine) {
      const lineNum = parseInt(errLine[1]);
      console.error(`Error around line ${lineNum}:`);
      for (let i = Math.max(0, lineNum - 5); i < Math.min(lines.length, lineNum + 5); i++) {
        console.error(`${i + 1}: ${lines[i]}`);
      }
    }
  }
  index++;
}
