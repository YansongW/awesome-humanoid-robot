/* Wiki page enhancements: Mermaid diagrams and info-box blockquotes. */

(function () {
  'use strict';

  function initWiki() {
    // Convert fenced mermaid code blocks into native mermaid containers.
    document.querySelectorAll('.wiki-body pre code.language-mermaid, .wiki-body pre code.mermaid').forEach(function (code) {
      var pre = code.parentElement;
      var figure = document.createElement('pre');
      figure.className = 'mermaid';
      figure.textContent = code.textContent;
      if (pre && pre.parentElement) {
        pre.parentElement.replaceChild(figure, pre);
      }
    });

    // Style terminology / example / note blockquotes as info panels.
    document.querySelectorAll('.wiki-body blockquote').forEach(function (bq) {
      var text = (bq.textContent || '').trim();
      if (/^(术语解释框|生活实例|自然语言逻辑|Note|提示|注意|Note:|Tip:|Info:|Warning:)/i.test(text)) {
        bq.classList.add('info-box');
      }
    });

    if (typeof mermaid !== 'undefined') {
      mermaid.initialize({ startOnLoad: true, theme: 'default' });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initWiki);
  } else {
    initWiki();
  }
})();
