/* Wiki page enhancements: Mermaid diagrams, KaTeX math, and info-box blockquotes. */

(function () {
  'use strict';

  function initWiki() {
    // Convert fenced mermaid code blocks into native mermaid containers.
    document.querySelectorAll('.wiki-body pre code.language-mermaid, .wiki-body pre code.mermaid').forEach(function (code) {
      var pre = code.parentElement;
      if (!pre || !pre.parentElement) return;
      var figure = document.createElement('pre');
      figure.className = 'mermaid';
      // Preserve exact diagram source; Mermaid parses this text directly.
      figure.textContent = code.textContent;
      pre.parentElement.replaceChild(figure, pre);
    });

    // Style terminology / example / note blockquotes as info panels.
    document.querySelectorAll('.wiki-body blockquote').forEach(function (bq) {
      var text = (bq.textContent || '').trim();
      if (/^(术语解释框|生活实例|自然语言逻辑|Note|提示|注意|Note:|Tip:|Info:|Warning:)/i.test(text)) {
        bq.classList.add('info-box');
      }
    });

    // Trigger Mermaid rendering manually so we can be sure the containers exist.
    if (typeof mermaid !== 'undefined') {
      try {
        mermaid.initialize({
          startOnLoad: false,
          theme: 'default',
          securityLevel: 'loose',
        });
        mermaid.run({ querySelector: '.mermaid' }).catch(function (err) {
          console.error('Mermaid render failed:', err);
        });
      } catch (err) {
        console.error('Mermaid initialization failed:', err);
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initWiki);
  } else {
    initWiki();
  }
})();
