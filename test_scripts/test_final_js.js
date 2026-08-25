const fs = require('fs');
const html = fs.readFileSync('AI Foundations Seminar - Simplified.html', 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
fs.writeFileSync('extracted_script_final.js', scriptMatch[1]);
