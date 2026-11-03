// Validate actual math using the repository's pinned, local KaTeX runtime.
const fs = require('node:fs');
const path = require('node:path');
const katex = require(path.join(__dirname, '../API_DOCUMENTATION/interactive/vendor/katex/katex.min.js'));
const rows = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const errors = [];
for (const row of rows) {
  try {
    katex.renderToString(row.tex, { displayMode: !!row.display, throwOnError: true,
      strict: 'ignore', trust: false, output: 'mathml', maxExpand: 1000 });
  } catch (error) {
    errors.push({id: row.id, message: error.message});
  }
}
process.stdout.write(JSON.stringify({version: katex.version, checked: rows.length, errors}));
