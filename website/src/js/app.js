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

  // Mobile menu toggle (placeholder for future expansion)
  const mobileToggle = document.getElementById('mobile-menu-toggle');
  if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
      document.body.classList.toggle('mobile-menu-open');
    });
  }
})();
