const fs = require('fs');
const code = fs.readFileSync('extracted_script.js', 'utf8');
try {
  eval(code);
} catch (e) {
  // It doesn't give column number natively in older node easily without stack trace matching
  console.log(e.stack);
}
