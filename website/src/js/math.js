/* KaTeX rendering for arithmatex elements produced by pymdownx.arithmatex. */

(function () {
  'use strict';

  function renderArithmatexMath() {
    if (typeof katex === 'undefined') return;
    document.querySelectorAll('.arithmatex').forEach(function (el) {
      const raw = el.textContent || '';
      const display = /^\s*\[/.test(raw);
      const tex = raw
        .replace(/^\s*\\?[(\[]+/, '')
        .replace(/\\?[)\]]+\s*$/, '')
        .trim();
      if (!tex) return;
      try {
        el.innerHTML = katex.renderToString(tex, {
          displayMode: display,
          throwOnError: false,
        });
      } catch (err) {
        // Leave original text if KaTeX fails.
      }
    });
  }

  window.renderArithmatexMath = renderArithmatexMath;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderArithmatexMath);
  } else {
    renderArithmatexMath();
  }
})();
