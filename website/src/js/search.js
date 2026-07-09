/* Client-side search for the knowledge graph */

(function () {
  'use strict';

  const searchInput = document.getElementById('search-input');
  const searchForm = document.getElementById('search-form');
  const resultsList = document.getElementById('results-list');
  const resultsTitle = document.getElementById('results-title');
  const resultsCount = document.getElementById('results-count');
  const typeFilters = document.querySelectorAll('.filter-tag');
  const section = document.querySelector('.search-results-section');
  const basePath = section ? (section.dataset.basePath || '') : '';
  const noResultsTemplate = section ? (section.dataset.noResults || 'No results for “{query}”.') : 'No results for “{query}”.';
  const resultsCountTemplate = section ? (section.dataset.resultsCount || '{count} results') : '{count} results';

  let searchData = { entries: [], index: {} };
  let activeType = 'all';
  let displayedCount = 0;
  const PAGE_SIZE = 20;

  function tokenize(text) {
    if (!text) return [];
    const tokens = [];
    const parts = text.toLowerCase().match(/[a-z0-9]+|[\u4e00-\u9fff]/g) || [];
    for (const part of parts) {
      if (/^[a-z0-9]+$/.test(part)) {
        tokens.push(part);
      } else {
        for (const ch of part) tokens.push(ch);
      }
    }
    return tokens;
  }

  async function loadIndex() {
    try {
      const res = await fetch(basePath + '/data/search-index.json');
      if (!res.ok) throw new Error('Failed to load search index');
      searchData = await res.json();
      init();
    } catch (err) {
      resultsList.innerHTML = `<div class="empty-state">${escapeHtml(err.message)}</div>`;
    }
  }

  function search(query, typeFilter) {
    const q = query.trim().toLowerCase();
    const qTokens = tokenize(q);
    const scores = new Map();

    for (let i = 0; i < searchData.entries.length; i++) {
      const e = searchData.entries[i];
      if (typeFilter !== 'all' && e.type !== typeFilter) continue;

      let score = 0;
      const name = (e.name || '').toLowerCase();
      const nameEn = (e.name_en || '').toLowerCase();
      const summary = (e.summary || '').toLowerCase();

      if (q && name.includes(q)) score += 100;
      if (q && nameEn.includes(q)) score += 80;
      if (q && e.id.toLowerCase().includes(q)) score += 70;
      if (q && summary.includes(q)) score += 40;

      for (const t of qTokens) {
        if (name.includes(t)) score += 10;
        if (nameEn.includes(t)) score += 8;
        if (e.id.toLowerCase().includes(t)) score += 5;
        if (summary.includes(t)) score += 3;
        if (e.type.toLowerCase().includes(t)) score += 4;
        if (e.domains && e.domains.some(d => d.toLowerCase().includes(t))) score += 4;
        if (e.layers && e.layers.some(l => l.toLowerCase().includes(t))) score += 3;
      }

      if (score > 0) scores.set(i, score);
    }

    const sorted = Array.from(scores.entries()).sort((a, b) => b[1] - a[1]);
    return sorted.map(([idx]) => searchData.entries[idx]);
  }

  function formatCount(count) {
    return resultsCountTemplate.replace('{count}', count);
  }

  function renderResults(results, query, append = false) {
    if (!append) {
      resultsList.innerHTML = '';
      displayedCount = 0;
    }

    if (results.length === 0) {
      resultsList.innerHTML = `<div class="empty-state">${escapeHtml(noResultsTemplate.replace('{query}', query))}</div>`;
      resultsCount.textContent = formatCount(0);
      return;
    }

    const page = results.slice(displayedCount, displayedCount + PAGE_SIZE);
    displayedCount += page.length;

    for (const e of page) {
      const item = document.createElement('a');
      item.className = 'result-item';
      item.href = basePath + '/' + e.url;
      item.innerHTML = `
        <div class="result-meta">
          <span class="tag">${escapeHtml(e.type_label || e.type)}</span>
          <span>${escapeHtml((e.domain_labels || e.domains || []).join(', '))}</span>
        </div>
        <h3>${escapeHtml(e.name)}</h3>
        <p>${escapeHtml((e.summary || '').slice(0, 200))}${(e.summary || '').length > 200 ? '…' : ''}</p>
      `;
      resultsList.appendChild(item);
    }

    resultsCount.textContent = formatCount(results.length);
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  function performSearch(append = false) {
    const query = searchInput ? searchInput.value : '';
    const results = search(query, activeType);
    renderResults(results, query, append);
  }

  function init() {
    const params = new URLSearchParams(window.location.search);
    const q = params.get('q') || '';
    if (searchInput) searchInput.value = q;

    if (q) {
      resultsTitle.textContent = `“${q}”`;
      performSearch();
    } else {
      resultsTitle.textContent = '';
      const all = searchData.entries.filter(e => activeType === 'all' || e.type === activeType);
      renderResults(all, '');
    }

    if (searchForm) {
      searchForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const q = searchInput.value;
        const url = new URL(window.location.href);
        url.searchParams.set('q', q);
        window.history.replaceState({}, '', url);
        resultsTitle.textContent = q ? `“${q}”` : '';
        performSearch();
      });
    }

    typeFilters.forEach(btn => {
      btn.addEventListener('click', () => {
        typeFilters.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeType = btn.dataset.type;
        performSearch();
      });
    });
  }

  loadIndex();
})();
