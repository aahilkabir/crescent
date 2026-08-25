const fs = require('fs');
const html = fs.readFileSync('ml-foundations.html', 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
fs.writeFileSync('extracted_ml4.js', scriptMatch[1]);
