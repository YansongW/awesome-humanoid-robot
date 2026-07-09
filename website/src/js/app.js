/* Rounds Tech KG - shared app logic */

(function () {
  'use strict';

  // Theme toggle
  const themeToggle = document.getElementById('theme-toggle');
  const html = document.documentElement;

  function setTheme(theme) {
    html.setAttribute('data-theme', theme);
    localStorage.setItem('rtkg-theme', theme);
  }

  const savedTheme = localStorage.getItem('rtkg-theme');
  if (savedTheme === 'dark' || savedTheme === 'light') {
    setTheme(savedTheme);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    setTheme('dark');
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = html.getAttribute('data-theme') || 'light';
      setTheme(current === 'dark' ? 'light' : 'dark');
    });
  }

  // Language switcher
  const langSwitcher = document.getElementById('language-switcher');
  if (langSwitcher) {
    const currentLang = document.body.getAttribute('data-lang') || 'zh';
    langSwitcher.value = currentLang;
    langSwitcher.addEventListener('change', () => {
      const target = langSwitcher.value;
      if (target === currentLang) return;
      localStorage.setItem('rtkg-lang', target);
      const path = window.location.pathname;
      // Strip existing language prefix
      const clean = path.replace(/^\/(en|ko)(?=\/)/, '') || '/';
      const newPath = target === 'zh' ? clean : '/' + target + clean;
      window.location.href = newPath;
    });
  }

  // Mobile menu toggle (placeholder for future expansion)
  const mobileToggle = document.getElementById('mobile-menu-toggle');
  if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
      document.body.classList.toggle('mobile-menu-open');
    });
  }
})();
