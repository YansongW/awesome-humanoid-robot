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
  const DEBOUNCE_MS = 150;
  let debounceTimer = null;

  /**
   * Tokenize a query or text into searchable units.
   * - Latin/number sequences are kept as whole tokens.
   * - Chinese characters are emitted individually (client-side fallback)
   *   and also as overlapping bigrams for better phrase matching.
   */
  function tokenize(text) {
    if (!text) return [];
    const tokens = [];
    const parts = text.toLowerCase().match(/[a-z0-9]+|[\u4e00-\u9fff]+/g) || [];
    for (const part of parts) {
      if (/^[a-z0-9]+$/.test(part)) {
        tokens.push(part);
      } else {
        // Chinese: single chars + bigrams
        const chars = Array.from(part);
        for (const ch of chars) tokens.push(ch);
        for (let i = 0; i < chars.length - 1; i++) {
          tokens.push(chars[i] + chars[i + 1]);
        }
      }
    }
    return tokens;
  }

  /**
   * Split English/CJK text into words/characters for token-set comparison.
   */
  function textTokens(text) {
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

  function tokenSet(text) {
    return new Set(textTokens(text));
  }

  async function loadIndex() {
    if (!resultsList) return;
    resultsList.innerHTML = '<div class="loading-state">Loading search index…</div>';
    try {
      const res = await fetch(basePath + '/data/search-index.json');
      if (!res.ok) throw new Error('Failed to load search index');
      searchData = await res.json();
      init();
    } catch (err) {
      resultsList.innerHTML = `<div class="empty-state">${escapeHtml(err.message)}</div>`;
    }
  }

  function scoreEntry(e, q, qTokens) {
    let score = 0;
    let strongMatches = 0;
    const name = (e.name || '').toLowerCase();
    const nameEn = (e.name_en || '').toLowerCase();
    const summary = (e.summary || '').toLowerCase();
    const eid = (e.id || '').toLowerCase();
    const type = (e.type || '').toLowerCase();

    const nameTokens = tokenSet(name);
    const nameEnTokens = tokenSet(nameEn);
    const summaryTokens = tokenSet(summary);
    const idTokens = tokenSet(eid);
    const typeTokens = tokenSet(type);

    // Exact/prefix matches on name get the biggest boost.
    if (q) {
      if (name === q) { score += 500; strongMatches++; }
      else if (name.startsWith(q)) { score += 250; strongMatches++; }
      else if (nameEn === q) { score += 400; strongMatches++; }
      else if (nameEn.startsWith(q)) { score += 200; strongMatches++; }
      else if (eid === q) { score += 150; strongMatches++; }
      else if (eid.startsWith(q)) { score += 100; strongMatches++; }

      // Containment (only meaningful for longer queries or non-Latin)
      if (name.includes(q)) { score += 100; strongMatches++; }
      if (nameEn.includes(q)) { score += 80; strongMatches++; }
      if (eid.includes(q)) { score += 60; strongMatches++; }
      if (summary.includes(q)) { score += 40; }
    }

    // Token overlap scoring. Prefer whole-token matches over substring matches
    // by checking membership in pre-tokenized sets.
    for (const t of qTokens) {
      if (t.length === 0) continue;
      const isLatin = /^[a-z0-9]+$/.test(t);
      const tokenScore = isLatin ? 12 : 8;
      const partialScore = isLatin ? 2 : 5;
      let matched = false;

      if (nameTokens.has(t)) { score += tokenScore; matched = true; strongMatches++; }
      else if (isLatin && name.includes(t)) score += partialScore;

      if (nameEnTokens.has(t)) { score += tokenScore - 2; matched = true; strongMatches++; }
      else if (isLatin && nameEn.includes(t)) score += partialScore;

      if (idTokens.has(t)) { score += tokenScore - 4; matched = true; strongMatches++; }
      else if (isLatin && eid.includes(t)) score += partialScore;

      if (summaryTokens.has(t)) { score += 4; matched = true; }
      else if (summary.includes(t)) score += 2;

      if (typeTokens.has(t)) { score += 5; matched = true; strongMatches++; }
      if (e.domains && e.domains.some(d => d.toLowerCase().includes(t))) { score += 4; matched = true; strongMatches++; }
      if (e.layers && e.layers.some(l => l.toLowerCase().includes(t))) { score += 3; matched = true; strongMatches++; }

      // For Latin tokens, require at least one strong (whole-token) match somewhere
      // to avoid substring pollution (e.g. "pid" matching "rapid").
      if (isLatin && !matched) score -= 5;
    }

    // Slight boost for entities with summaries so stubs don't dominate.
    if (summary.length > 20) score += 2;

    // Require at least one strong match (name/id/type/domain/layer) unless the
    // full query is found in the summary.
    if (strongMatches === 0 && !(q && summary.includes(q))) return 0;

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

  function highlight(text, q) {
    if (!text || !q) return escapeHtml(text);
    const tokens = tokenize(q).filter(t => t.length >= 2 || !/^[a-z0-9]$/.test(t));
    if (tokens.length === 0) return escapeHtml(text);
    // Sort by length desc so longer matches are replaced first.
    tokens.sort((a, b) => b.length - a.length);
    let html = escapeHtml(text);
    for (const t of tokens) {
      const re = new RegExp('(' + escapeRegex(t) + ')', 'gi');
      html = html.replace(re, '<mark>$1</mark>');
    }
    return html;
  }

  function escapeRegex(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
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

    const q = query.trim().toLowerCase();
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
        <h3>${highlight(e.name, q)} <small>${highlight(e.name_en || '', q)}</small></h3>
        <p>${highlight(excerpt, q)}${hasMore ? '…' : ''}</p>
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
