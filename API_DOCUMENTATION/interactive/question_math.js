/* Render JSON question fields without re-decoding backslashes or trusting HTML. */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else root.QuestionMath = api;
})(typeof window === 'object' ? window : this, function () {
  'use strict';
  function tokens(value) {
    const text = String(value ?? '');
    const pattern = /(?<!\\)\$\$([\s\S]+?)(?<!\\)\$\$|(?<!\\)\$(?!\$)((?:\\.|[^$])+?)(?<!\\)\$|\\\[([\s\S]+?)\\\]|\\\(([\s\S]+?)\\\)/g;
    const result = [];
    let offset = 0, match;
    while ((match = pattern.exec(text))) {
      if (match.index > offset) result.push({kind: 'text', value: text.slice(offset, match.index)});
      result.push({kind: 'math', value: match.slice(1).find(v => v !== undefined),
                   display: match[1] !== undefined || match[3] !== undefined});
      offset = pattern.lastIndex;
    }
    if (offset < text.length) result.push({kind: 'text', value: text.slice(offset)});
    return result;
  }
  function render(element, value, katex) {
    const document = element.ownerDocument;
    const fragment = document.createDocumentFragment();
    for (const token of tokens(value)) {
      if (token.kind === 'text') fragment.appendChild(document.createTextNode(token.value));
      else {
        const span = document.createElement(token.display ? 'div' : 'span');
        katex.render(token.value, span, {displayMode: token.display, throwOnError: true,
          trust: false, strict: 'ignore', output: 'htmlAndMathml'});
        fragment.appendChild(span);
      }
    }
    element.replaceChildren(fragment);
  }
  return {tokens, render};
});
