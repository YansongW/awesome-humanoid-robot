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
  const emptyMessage = section ? (section.dataset.emptyMessage || 'Enter keywords or select a type to start searching.') : 'Enter keywords or select a type to start searching.';
  const loadingMessage = section ? (section.dataset.loading || 'Loading search index…') : 'Loading search index…';

  let searchData = { entries: [], index: {} };
  let activeType = 'all';
  let currentQuery = '';
  let currentResults = [];
  let displayedCount = 0;
  const PAGE_SIZE = 20;
  const DEBOUNCE_MS = 120;
  let debounceTimer = null;

  /**
   * Tokenize a query or text into searchable units.
   * - Latin/number sequences are kept as whole tokens.
   * - CJK text is emitted as individual characters and overlapping bigrams.
   */
  function tokenize(text) {
    if (!text) return [];
    const tokens = [];
    const parts = text.toLowerCase().match(/[a-z0-9]+|[\u4e00-\u9fff\uac00-\ud7af]+/g) || [];
    for (const part of parts) {
      if (/^[a-z0-9]+$/.test(part)) {
        tokens.push(part);
      } else {
        const chars = Array.from(part);
        for (const ch of chars) tokens.push(ch);
        for (let i = 0; i < chars.length - 1; i++) {
          tokens.push(chars[i] + chars[i + 1]);
        }
      }
    }
    return tokens;
  }

  function uniqueTokens(text) {
    const tokens = tokenize(text);
    const seen = new Set();
    const out = [];
    for (const t of tokens) {
      if (!seen.has(t)) {
        seen.add(t);
        out.push(t);
      }
    }
    return out;
  }

  async function loadIndex() {
    if (!resultsList) return;
    resultsList.innerHTML = `<div class="loading-state">${escapeHtml(loadingMessage)}</div>`;
    try {
      const res = await fetch(basePath + '/data/search-index.json');
      if (!res.ok) throw new Error('Failed to load search index');
      searchData = await res.json();
      if (!searchData.entries) searchData.entries = [];
      if (!searchData.index) searchData.index = {};
      init();
    } catch (err) {
      resultsList.innerHTML = `<div class="empty-state">${escapeHtml(err.message)}</div>`;
    }
  }

  /**
   * Find candidate entry indices for a query using the inverted index.
   * Returns a map of entry index -> number of matched tokens.
   */
  function findCandidates(qTokens) {
    const counts = new Map();
    for (const t of qTokens) {
      const hits = searchData.index[t];
      if (!hits) continue;
      for (const idx of hits) {
        counts.set(idx, (counts.get(idx) || 0) + 1);
      }
    }
    return counts;
  }

  function scoreEntry(e, q, qTokens, candidateMatchCount) {
    let score = 0;
    let strongMatches = 0;
    const name = (e.name || '').toLowerCase();
    const nameEn = (e.name_en || '').toLowerCase();
    const summary = (e.summary || '').toLowerCase();
    const eid = (e.id || '').toLowerCase();
    const type = (e.type || '').toLowerCase();

    // Exact / prefix / containment on the raw query string.
    if (q) {
      if (name === q) { score += 600; strongMatches += 2; }
      else if (name.startsWith(q)) { score += 300; strongMatches++; }
      else if (nameEn === q) { score += 500; strongMatches += 2; }
      else if (nameEn.startsWith(q)) { score += 250; strongMatches++; }
      else if (eid === q) { score += 200; strongMatches++; }
      else if (name.includes(q)) { score += 120; strongMatches++; }
      else if (nameEn.includes(q)) { score += 100; strongMatches++; }
      else if (eid.includes(q)) { score += 60; }
      else if (summary.includes(q)) { score += 40; }
    }

    // Token overlap scoring.  Latin tokens only score for whole-token matches
    // to avoid substring pollution (e.g. "pid" matching "rapid").
    for (const t of qTokens) {
      if (t.length === 0) continue;
      const isLatin = /^[a-z0-9]+$/.test(t);
      const inName = name.split(/[^a-z0-9\u4e00-\u9fff]+/).includes(t) || name.includes(t);
      const inNameEn = nameEn.split(/[^a-z0-9\u4e00-\u9fff]+/).includes(t) || nameEn.includes(t);
      const inId = eid.split(/[^a-z0-9_]+/).includes(t) || eid.includes(t);
      const inSummary = summary.includes(t);
      const inType = type.includes(t);
      const inDomain = e.domains && e.domains.some(d => d.toLowerCase().includes(t));

      if (isLatin) {
        // Require a whole-token match somewhere; otherwise penalize.
        const whole = inName || inNameEn || inId || inType || inDomain ||
          summary.split(/[^a-z0-9\u4e00-\u9fff]+/).includes(t);
        if (whole) {
          if (inName) { score += 20; strongMatches++; }
          else if (inNameEn) { score += 16; strongMatches++; }
          else if (inId) { score += 10; strongMatches++; }
          else if (inType) { score += 8; strongMatches++; }
          else if (inDomain) { score += 6; strongMatches++; }
          else if (inSummary) { score += 4; }
        } else {
          score -= 8;
        }
      } else {
        // CJK tokens: any occurrence counts.
        if (inName) { score += 18; strongMatches++; }
        else if (inNameEn) { score += 14; strongMatches++; }
        else if (inId) { score += 8; strongMatches++; }
        else if (inType) { score += 6; strongMatches++; }
        else if (inDomain) { score += 4; strongMatches++; }
        else if (inSummary) { score += 3; }
      }
    }

    // Boost candidates that matched more query tokens.
    score += candidateMatchCount * 15;

    // Slight boost for entities with real summaries so stubs don't dominate.
    if (summary.length > 20) score += 2;

    // Penalize very long names (typically auto-ingested paper titles) so
    // concise concept/method entities rank higher for the same token match.
    const primaryName = name || nameEn || eid;
    if (primaryName.length > 80) score -= 10;
    if (primaryName.length > 140) score -= 15;

    // Require at least one strong match unless the raw query appears in summary.
    if (strongMatches === 0 && !(q && summary.includes(q))) return 0;

    return score;
  }

  function search(query, typeFilter) {
    const q = query.trim().toLowerCase();
    const qTokens = uniqueTokens(q);

    // Use inverted index to get candidates.
    const candidates = findCandidates(qTokens);
    const scores = [];

    for (const [idx, matchCount] of candidates.entries()) {
      const e = searchData.entries[idx];
      if (!e) continue;
      if (typeFilter !== 'all' && e.type !== typeFilter) continue;
      // For multi-token queries, require at least one token match (already
      // guaranteed) but do not require all tokens to match.
      const score = scoreEntry(e, q, qTokens, matchCount);
      if (score > 0) scores.push({ entry: e, score });
    }

    // Fallback: if the inverted index returned nothing, try a slow scan.
    if (scores.length === 0 && q) {
      for (const e of searchData.entries) {
        if (typeFilter !== 'all' && e.type !== typeFilter) continue;
        const score = scoreEntry(e, q, qTokens, 0);
        if (score > 0) scores.push({ entry: e, score });
      }
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
    const tokens = uniqueTokens(q).filter(t => t.length >= 2 || !/^[a-z0-9]$/.test(t));
    if (tokens.length === 0) return escapeHtml(text);
    // Sort by length desc so longer phrases take precedence, then replace in one pass.
    tokens.sort((a, b) => b.length - a.length);
    const pattern = tokens.map(escapeRegex).join('|');
    const re = new RegExp('(' + pattern + ')', 'gi');
    return escapeHtml(text).replace(re, '<mark>$1</mark>');
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
      const nameHtml = highlight(e.name, q);
      const nameEnHtml = e.name_en && e.name_en !== e.name ? highlight(e.name_en, q) : '';
      item.innerHTML = `
        <div class="result-meta">
          <span class="tag">${escapeHtml(e.type_label || e.type)}</span>
          <span>${escapeHtml(metaTags)}</span>
        </div>
        <h3>${nameHtml}${nameEnHtml ? ' <small>' + nameEnHtml + '</small>' : ''}</h3>
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
      if (resultsList) resultsList.innerHTML = `<div class="empty-state">${escapeHtml(emptyMessage)}</div>`;
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
