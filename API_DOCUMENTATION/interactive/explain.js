/* Accessible local LaTeX and plain-language explanations for the documentation. */
(function () {
  'use strict';
  const esc = value => String(value ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  function math(tex, display = true) {
    try {
      return window.katex.renderToString(tex, {
        displayMode: display, throwOnError: true, trust: false,
        output: 'htmlAndMathml', strict: 'warn',
      });
    } catch (error) {
      return `<p class="formula-error" role="alert">Persamaan belum dapat ditampilkan: ${esc(error.message)}</p><code>${esc(tex)}</code>`;
    }
  }
  function formula(card) {
    return `<article class="math-card"><h4>${esc(card.title)}</h4><div class="math-render">${math(card.tex)}</div>
      ${card.symbols?.length ? `<dl class="symbol-definitions">${card.symbols.map(s=>`<div><dt>${math(s.symbol,false)}</dt><dd>${esc(s.meaning)}</dd></div>`).join('')}</dl>`:''}
      ${card.why?`<p class="math-why"><b>Mengapa dihitung begitu?</b> ${esc(card.why)}</p>`:''}
      <details class="latex-source"><summary>Kode LaTeX</summary><pre><code>${esc(card.tex)}</code></pre><button type="button" data-copy-tex="${esc(card.tex)}">Salin LaTeX</button></details></article>`;
  }
  function terms(values) {
    return `<dl class="term-definitions">${values.map(item=>`<div><dt>${esc(item.term)}</dt><dd>${esc(item.meaning)}${item.why?`<span class="term-purpose"><b>Fungsinya:</b> ${esc(item.why)}</span>`:''}</dd></div>`).join('')}</dl>`;
  }
  function metrics(rows) {
    return `<dl class="result-metrics">${rows.map(row=>`<div><dt>${esc(row.label)}</dt><dd${row.key?` data-metric="${esc(row.key)}"`:''}>${esc(row.value)}</dd></div>`).join('')}</dl>`;
  }
  window.FlowExplain = { esc, math, formula, terms, metrics };
})();
