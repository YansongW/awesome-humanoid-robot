/* KaTeX rendering for arithmatex elements produced by pymdownx.arithmatex. */

(function () {
  'use strict';

  function renderArithmatexMath() {
    if (typeof katex === 'undefined') return;

    document.querySelectorAll('.arithmatex').forEach(function (el) {
      // Skip elements that have already been rendered by KaTeX.
      if (el.querySelector('.katex')) return;

      const raw = (el.textContent || '').trim();
      if (!raw) return;

      // Determine display mode and strip fences.
      let tex = raw;
      let display = false;

      if (/^\$\$/.test(tex) && /\$\$$/.test(tex)) {
        display = true;
        tex = tex.replace(/^\$\$\s*/, '').replace(/\s*\$\$$/, '');
      } else if (/^\$/.test(tex) && /\$$/.test(tex)) {
        display = false;
        tex = tex.replace(/^\$\s*/, '').replace(/\s*\$$/, '');
      } else if (/^\\\[/.test(tex) && /\\\]$/.test(tex)) {
        display = true;
        tex = tex.replace(/^\\\[\s*/, '').replace(/\s*\\\]$/, '');
      } else if (/^\\\(/.test(tex) && /\\\)$/.test(tex)) {
        display = false;
        tex = tex.replace(/^\\\(\s*/, '').replace(/\s*\\\)$/, '');
      } else if (/^\[/.test(tex) && /\]$/.test(tex)) {
        display = true;
        tex = tex.replace(/^\[\s*/, '').replace(/\s*\]$/, '');
      } else if (/^\(/.test(tex) && /\)$/.test(tex)) {
        display = false;
        tex = tex.replace(/^\(\s*/, '').replace(/\s*\)$/, '');
      }

      tex = tex.trim();
      if (!tex) return;

      try {
        el.innerHTML = katex.renderToString(tex, {
          displayMode: display,
          throwOnError: false,
          trust: false,
        });
      } catch (err) {
        // Leave original text if KaTeX fails.
      }
    });
  }

  window.renderArithmatexMath = renderArithmatexMath;

  function runWhenReady() {
    if (typeof katex === 'undefined') {
      // Wait for the KaTeX library to load.
      var checkCount = 0;
      var interval = setInterval(function () {
        if (typeof katex !== 'undefined') {
          clearInterval(interval);
          renderArithmatexMath();
          return;
        }
        checkCount += 1;
        if (checkCount > 100) {
          clearInterval(interval);
        }
      }, 100);
      return;
    }
    renderArithmatexMath();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', runWhenReady);
  } else {
    runWhenReady();
  }
})();
