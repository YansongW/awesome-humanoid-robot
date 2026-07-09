/* Client-side search for the knowledge graph */

(function () {
  'use strict';

  const searchInput = document.getElementById('search-input');
  const searchForm = document.getElementById('search-form');
  const resultsList = document.getElementById('results-list');
  const resultsTitle = document.getElementById('results-title');
  const resultsCount = document.getElementById('results-count');
  const typeFilters = document.querySelectorAll('.filter-tag');
  const loadMoreBtn = document.getElementById('load-more');
  const section = document.querySelector('.search-results-section');
  const basePath = section ? (section.dataset.basePath || '') : '';
  const noResultsTemplate = section ? (section.dataset.noResults || 'No results for “{query}”.') : 'No results for “{query}”.';
  const resultsCountTemplate = section ? (section.dataset.resultsCount || '{count} results') : '{count} results';

  let searchData = { entries: [] };
  let activeType = 'all';
  let currentQuery = '';
  let currentResults = [];
  let displayedCount = 0;
  const PAGE_SIZE = 20;
  const DEBOUNCE_MS = 200;
  let debounceTimer = null;

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
      if (resultsList) {
        resultsList.innerHTML = `<div class="empty-state">${escapeHtml(err.message)}</div>`;
      }
    }
  }

  function scoreEntry(e, q, qTokens) {
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
      if (e.type && e.type.toLowerCase().includes(t)) score += 4;
      if (e.domains && e.domains.some(d => d.toLowerCase().includes(t))) score += 4;
      if (e.layers && e.layers.some(l => l.toLowerCase().includes(t))) score += 3;
    }

    return score;
  }

  function search(query, typeFilter) {
    const q = query.trim().toLowerCase();
    const qTokens = tokenize(q);
    const scores = [];

    for (const e of searchData.entries) {
      if (typeFilter !== 'all' && e.type !== typeFilter) continue;
      const score = scoreEntry(e, q, qTokens);
      if (score > 0) scores.push({ entry: e, score });
    }

    scores.sort((a, b) => b.score - a.score);
    return scores.map(s => s.entry);
  }

  function formatCount(count) {
    return resultsCountTemplate.replace('{count}', count);
  }

  function updateLoadMore() {
    if (!loadMoreBtn) return;
    if (displayedCount < currentResults.length) {
      loadMoreBtn.classList.remove('hidden');
    } else {
      loadMoreBtn.classList.add('hidden');
    }
  }

  function renderResults(results, query, append = false) {
    if (!append) {
      if (resultsList) resultsList.innerHTML = '';
      displayedCount = 0;
      currentResults = results;
      currentQuery = query;
    }

    if (resultsCount) resultsCount.textContent = formatCount(results.length);

    if (results.length === 0) {
      if (resultsList) {
        resultsList.innerHTML = `<div class="empty-state">${escapeHtml(noResultsTemplate.replace('{query}', query))}</div>`;
      }
      updateLoadMore();
      return;
    }

    const page = results.slice(displayedCount, displayedCount + PAGE_SIZE);
    displayedCount += page.length;

    for (const e of page) {
      const item = document.createElement('a');
      item.className = 'result-item';
      item.href = basePath + '/' + e.url;
      const metaTags = (e.domain_labels || e.domains || []).join(', ');
      const excerpt = (e.summary || '').slice(0, 200);
      const hasMore = (e.summary || '').length > 200;
      item.innerHTML = `
        <div class="result-meta">
          <span class="tag">${escapeHtml(e.type_label || e.type)}</span>
          <span>${escapeHtml(metaTags)}</span>
        </div>
        <h3>${escapeHtml(e.name)}</h3>
        <p>${escapeHtml(excerpt)}${hasMore ? '…' : ''}</p>
      `;
      if (resultsList) resultsList.appendChild(item);
    }

    updateLoadMore();
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

  function setUrlQuery(q) {
    const url = new URL(window.location.href);
    if (q) {
      url.searchParams.set('q', q);
    } else {
      url.searchParams.delete('q');
    }
    window.history.replaceState({}, '', url);
  }

  function init() {
    const params = new URLSearchParams(window.location.search);
    const q = params.get('q') || '';
    if (searchInput) searchInput.value = q;

    if (q) {
      if (resultsTitle) resultsTitle.textContent = `“${q}”`;
      performSearch();
    } else {
      if (resultsTitle) resultsTitle.textContent = '';
      if (resultsList) resultsList.innerHTML = `<div class="empty-state">输入关键词或选择类型以开始搜索。</div>`;
      if (resultsCount) resultsCount.textContent = formatCount(0);
      updateLoadMore();
    }

    if (searchInput) {
      searchInput.addEventListener('input', () => {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => {
          const q = searchInput.value;
          setUrlQuery(q);
          if (resultsTitle) resultsTitle.textContent = q ? `“${q}”` : '';
          performSearch();
        }, DEBOUNCE_MS);
      });
    }

    if (searchForm) {
      searchForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const q = searchInput ? searchInput.value : '';
        setUrlQuery(q);
        if (resultsTitle) resultsTitle.textContent = q ? `“${q}”` : '';
        performSearch();
        if (searchInput) searchInput.blur();
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

    if (loadMoreBtn) {
      loadMoreBtn.addEventListener('click', () => {
        renderResults(currentResults, currentQuery, true);
      });
    }
  }

  loadIndex();
})();
