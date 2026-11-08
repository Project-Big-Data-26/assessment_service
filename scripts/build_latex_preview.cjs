const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const katex = require(path.join(root, 'API_DOCUMENTATION/interactive/vendor/katex/katex.min.js'));
const changes = JSON.parse(fs.readFileSync(path.join(root, 'runs/latex_audit/changes.json'), 'utf8'));
const tokens = require(path.join(root, 'API_DOCUMENTATION/interactive/question_math.js')).tokens;
const escape = value => String(value).replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
function mathText(value) {
  return tokens(value).map(token => token.kind === 'text' ? escape(token.value) : katex.renderToString(token.value,
    {displayMode: token.display, throwOnError: true, strict: 'ignore', trust: false})).join('');
}
const examples = [String.raw`$\left(2^{-1}+4^{-1}\right)^{-1}=2+4$`,
  String.raw`$2^{3^{2}}=\left(2^3\right)^2$`, String.raw`$2^{-1}+4^{-1}=8^{-1}$`,
  String.raw`$\left(\dfrac{3}{2}\right)^{-2}=\dfrac{4}{9}$`];
const unique = [...new Map(changes.map(row => [row.after, row])).values()].slice(0, 12);
const cards = examples.map((text, i) => `<article><b>Contoh ${'ABCD'[i]}</b><div class="equation">${mathText(text)}</div></article>`).join('');
const rows = unique.map(row => `<article><small>${escape(row.file)} ${escape(row.pointer)}</small><pre>${escape(row.before)}</pre><div>${mathText(row.after)}</div></article>`).join('');
const html = `<!doctype html><html lang="id"><meta charset="utf-8"><title>Pratinjau perbaikan LaTeX</title>
<link rel="stylesheet" href="../../API_DOCUMENTATION/interactive/vendor/katex/katex.min.css">
<style>body{font:16px system-ui;color:#172033;background:#f4f7fc;max-width:1100px;margin:40px auto;padding:0 20px}h1{font-size:26px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}article{background:white;border:1px solid #dce3ef;border-radius:14px;padding:24px;margin:16px 0;overflow:auto}.equation{padding:20px 0}small{color:#526176}pre{white-space:pre-wrap;color:#884a23;background:#fff6ed;padding:12px;border-radius:6px}.katex{font-size:1.25em}</style>
<h1>Pratinjau perbaikan LaTeX</h1><p>Contoh tampilan opsi seperti laporan pengguna. Kebenaran matematis distraktor tidak diubah oleh perbaikan format.</p>
<div class="grid">${cards}</div><h2>Contoh perbaikan dari data</h2>${rows}</html>`;
fs.writeFileSync(path.join(root, 'runs/latex_audit/preview.html'), html, 'utf8');
process.stdout.write(`Rendered ${examples.length + unique.length} examples without KaTeX errors.\n`);
