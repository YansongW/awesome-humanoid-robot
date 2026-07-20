/* Wiki page enhancements: Mermaid diagrams, KaTeX math, and info-box blockquotes. */

(function () {
  'use strict';

  function initWiki() {
    // Convert fenced mermaid code blocks into native mermaid containers.
    document.querySelectorAll('.wiki-body pre code.language-mermaid, .wiki-body pre code.mermaid, .entry-body pre code.language-mermaid, .entry-body pre code.mermaid').forEach(function (code) {
      var pre = code.parentElement;
      if (!pre || !pre.parentElement) return;
      var figure = document.createElement('pre');
      figure.className = 'mermaid';
      // Preserve exact diagram source; Mermaid parses this text directly.
      figure.textContent = code.textContent;
      pre.parentElement.replaceChild(figure, pre);
    });

    // Style terminology / example / note blockquotes as info panels.
    document.querySelectorAll('.wiki-body blockquote, .entry-body blockquote').forEach(function (bq) {
      var text = (bq.textContent || '').trim();
      if (/^(术语解释框|生活实例|自然语言逻辑|Note|提示|注意|Note:|Tip:|Info:|Warning:)/i.test(text)) {
        bq.classList.add('info-box');
      }
    });

    // Trigger Mermaid rendering lazily: only render diagrams as they approach
    // the viewport, so chapters with 100+ diagrams don't freeze on load.
    if (typeof mermaid !== 'undefined') {
      try {
        mermaid.initialize({
          startOnLoad: false,
          theme: 'default',
          securityLevel: 'loose',
        });
        var diagrams = Array.from(document.querySelectorAll('.mermaid'));
        var renderOne = function (el) {
          if (el.dataset.mermaidDone) return;
          el.dataset.mermaidDone = '1';
          mermaid.run({ nodes: [el] }).catch(function (err) {
            console.error('Mermaid render failed:', err);
          });
        };
        if ('IntersectionObserver' in window && diagrams.length > 10) {
          var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
              if (entry.isIntersecting) {
                io.unobserve(entry.target);
                renderOne(entry.target);
              }
            });
          }, { rootMargin: '300px 0px' });
          diagrams.forEach(function (el) { io.observe(el); });
        } else {
          diagrams.forEach(renderOne);
        }
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
