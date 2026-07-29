/* BYOK ChatGPT-style Q&A over the knowledge graph.
 *
 * Pure frontend: the user's API key is stored only in this browser's
 * localStorage and requests go directly from the browser to the provider.
 * Retrieval reuses the search-page scoring via window.KGSearch (search.js),
 * then fetches data/qa-corpus.json lazily for RAG context.
 *
 * Exported as a reusable component: window.KGAsk.mount(container, opts).
 *   opts.mode           'fullPage' (standalone /ask/ page) | 'panel' (graph page)
 *   opts.onSourceClick  (entryId, event) => void — panel mode chip action
 *   opts.onHighlightAll (entryIds) => void — panel mode "highlight all" action
 *   opts.strings        i18n object; defaults to the container's data-* attrs
 */

(function () {
  'use strict';

  var LS = {
    provider: 'kg_ask_provider',
    apiKey: 'kg_ask_api_key',
    baseUrl: 'kg_ask_base_url',
    model: 'kg_ask_model',
  };

  var PROVIDERS = {
    deepseek: { baseUrl: 'https://api.deepseek.com', model: 'deepseek-chat' },
    openai: { baseUrl: 'https://api.openai.com', model: 'gpt-4o-mini' },
    custom: { baseUrl: '', model: '' },
  };

  var TOP_K = 8;
  var MAX_HISTORY_MESSAGES = 12; // last 6 rounds (user + assistant)
  var MAX_SAVED_MESSAGES = 50; // sessionStorage history cap

  // Chat-only re-ranking: keep papers/news from flooding the RAG context.
  var TYPE_WEIGHTS = {
    component: 1.3, technology: 1.3, concept: 1.3, method: 1.3, robot_system: 1.3,
    paper: 0.7, news: 0.7,
  };

  var PROMPTS = {
    zh: {
      system: '你是一个熟悉人形机器人行业的知识图谱助手。请严格依据下面提供的知识图谱内容回答问题。' +
        '如果资料中没有足够信息，请明确说明。回答请使用中文，并在相关处引用条目 ID（如 ent_process_p4_1_1）。' +
        '对比类问题优先用表格呈现；严禁引用资料之外的条目 ID。',
      labels: { type: '类型', summary: '摘要', content: '内容', relations: '关系' },
      wrap: function (context, question) {
        return '知识图谱资料：\n\n' + context + '\n\n用户问题：' + question + '\n\n请回答：';
      },
    },
    en: {
      system: 'You are a knowledge-graph assistant familiar with the humanoid robot industry. ' +
        'Answer strictly based on the knowledge graph material provided below. If the material is ' +
        'insufficient, say so explicitly. Answer in English and cite entry IDs (e.g. ent_process_p4_1_1) where relevant. ' +
        'For comparison questions, prefer a table. Never cite entry IDs that are not present in the provided material.',
      labels: { type: 'Type', summary: 'Summary', content: 'Content', relations: 'Relations' },
      wrap: function (context, question) {
        return 'Knowledge graph material:\n\n' + context + '\n\nUser question: ' + question + '\n\nPlease answer:';
      },
    },
    ko: {
      system: '당신은 휴로봇 산업에 정통한 지식 그래프 어시스턴트입니다. 아래 제공된 지식 그래프 자료만을 근거로 ' +
        '답변하세요. 자료가 부족하면 명확히 밝히세요. 한국어로 답변하고, 관련된 곳에 개체 ID(예: ent_process_p4_1_1)를 인용하세요. ' +
        '비교 질문에는 표를 우선 사용하고, 제공된 자료에 없는 개체 ID는 절대 인용하지 마세요.',
      labels: { type: '유형', summary: '요약', content: '내용', relations: '관계' },
      wrap: function (context, question) {
        return '지식 그래프 자료:\n\n' + context + '\n\n사용자 질문: ' + question + '\n\n답변해 주세요:';
      },
    },
  };

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  function mount(container, opts) {
    opts = opts || {};
    var mode = opts.mode || 'fullPage';
    var basePath = container.dataset.basePath || '';
    var lang = document.body.dataset.lang || 'zh';
    var strings = opts.strings || container.dataset;
    var prompt = PROMPTS[lang] || PROMPTS.zh;

    /* ---------- DOM (same structure/classes as the old static markup) ---------- */

    container.classList.add('ask-root');

    var messagesEl = el('div', 'ask-messages');
    messagesEl.appendChild(el('div', 'empty-state', strings.empty || ''));

    var input = el('textarea');
    input.rows = 2;
    input.placeholder = strings.inputPlaceholder || '';
    input.autocomplete = 'off';

    var settingsToggle = el('button', 'btn btn-secondary', strings.settings || 'Settings');
    settingsToggle.type = 'button';
    var clearHistoryBtn = el('button', 'btn btn-secondary', strings.clearHistory || 'Clear chat');
    clearHistoryBtn.type = 'button';
    clearHistoryBtn.title = strings.clearHistory || 'Clear chat';
    var sendBtn = el('button', 'ask-send-btn', strings.send || 'Send');
    sendBtn.type = 'submit';
    var stopBtn = el('button', 'btn btn-secondary hidden', strings.stop || 'Stop');
    stopBtn.type = 'button';

    var actions = el('div', 'ask-actions');
    actions.appendChild(settingsToggle);
    actions.appendChild(clearHistoryBtn);
    actions.appendChild(sendBtn);
    actions.appendChild(stopBtn);

    var form = el('form', 'ask-form');
    form.appendChild(input);
    form.appendChild(actions);

    var settingsPanel = el('div', 'ask-settings hidden');
    settingsPanel.appendChild(el('h2', null, strings.settingsTitle || 'API Settings'));
    settingsPanel.appendChild(el('p', 'ask-privacy-note', strings.privacyNote || ''));

    var grid = el('div', 'ask-settings-grid');

    function field(labelText, control) {
      var label = el('label', 'ask-field');
      label.appendChild(el('span', null, labelText));
      label.appendChild(control);
      return label;
    }

    var providerSel = el('select');
    [['deepseek', 'DeepSeek'], ['openai', 'OpenAI'], ['custom', strings.providerCustom || 'Custom']]
      .forEach(function (p) {
        var opt = el('option', null, p[1]);
        opt.value = p[0];
        providerSel.appendChild(opt);
      });

    var apiKeyInput = el('input');
    apiKeyInput.type = 'password';
    apiKeyInput.autocomplete = 'off';
    apiKeyInput.placeholder = 'sk-…';

    var baseUrlInput = el('input');
    baseUrlInput.type = 'text';
    baseUrlInput.autocomplete = 'off';
    baseUrlInput.placeholder = 'https://api.deepseek.com';

    var modelInput = el('input');
    modelInput.type = 'text';
    modelInput.autocomplete = 'off';
    modelInput.placeholder = 'deepseek-chat';

    grid.appendChild(field(strings.provider || 'Provider', providerSel));
    grid.appendChild(field('API Key', apiKeyInput));
    grid.appendChild(field(strings.baseUrl || 'Base URL', baseUrlInput));
    grid.appendChild(field(strings.model || 'Model', modelInput));

    var saveBtn = el('button', 'ask-send-btn', strings.save || 'Save');
    saveBtn.type = 'button';
    var clearBtn = el('button', 'btn btn-secondary', strings.clear || 'Clear');
    clearBtn.type = 'button';
    var settingsStatus = el('span', 'ask-settings-status');

    var settingsActions = el('div', 'ask-settings-actions');
    settingsActions.appendChild(saveBtn);
    settingsActions.appendChild(clearBtn);
    settingsActions.appendChild(settingsStatus);

    settingsPanel.appendChild(grid);
    settingsPanel.appendChild(settingsActions);

    container.appendChild(messagesEl);
    container.appendChild(form);
    container.appendChild(settingsPanel);

    /* ---------- settings ---------- */

    function getConfig() {
      var provider = localStorage.getItem(LS.provider) || 'deepseek';
      var preset = PROVIDERS[provider] || PROVIDERS.deepseek;
      return {
        provider: provider,
        apiKey: localStorage.getItem(LS.apiKey) || '',
        baseUrl: localStorage.getItem(LS.baseUrl) || preset.baseUrl,
        model: localStorage.getItem(LS.model) || preset.model,
      };
    }

    function loadSettingsForm() {
      var cfg = getConfig();
      providerSel.value = cfg.provider in PROVIDERS ? cfg.provider : 'deepseek';
      apiKeyInput.value = cfg.apiKey;
      baseUrlInput.value = cfg.baseUrl;
      modelInput.value = cfg.model;
    }

    function onProviderChange() {
      var preset = PROVIDERS[providerSel.value] || PROVIDERS.custom;
      baseUrlInput.value = preset.baseUrl;
      modelInput.value = preset.model;
    }

    function saveSettings() {
      localStorage.setItem(LS.provider, providerSel.value);
      localStorage.setItem(LS.apiKey, apiKeyInput.value.trim());
      localStorage.setItem(LS.baseUrl, baseUrlInput.value.trim());
      localStorage.setItem(LS.model, modelInput.value.trim());
      settingsStatus.textContent = strings.settingsSaved || '';
    }

    function clearSettings() {
      Object.keys(LS).forEach(function (k) { localStorage.removeItem(LS[k]); });
      loadSettingsForm();
      settingsStatus.textContent = strings.settingsCleared || '';
    }

    /* ---------- retrieval (reuses search.js scoring) ---------- */

    var searchIndexPromise = null;
    var corpusManifestPromise = null;
    var corpusShards = {}; // filename -> Promise<shard>
    var corpusShardsLoaded = {}; // filename -> shard (for sync lookup after await)
    var history = []; // {role: 'user'|'assistant', content: string, sources?: [...]}
    var streaming = false;
    var abortController = null;
    var lastFocusNames = []; // panel mode: recently highlighted entries (<= 3)

    function ensureSearchIndex() {
      if (!searchIndexPromise) {
        searchIndexPromise = fetch(basePath + '/data/search-index.json')
          .then(function (res) {
            if (!res.ok) throw new Error('Failed to load search index');
            return res.json();
          })
          .then(function (data) { window.KGSearch.setData(data); });
      }
      return searchIndexPromise;
    }

    function ensureCorpusManifest() {
      if (!corpusManifestPromise) {
        corpusManifestPromise = fetch(basePath + '/data/qa-corpus/manifest.json')
          .then(function (res) {
            if (!res.ok) throw new Error('Failed to load Q&A corpus manifest');
            return res.json();
          });
      }
      return corpusManifestPromise;
    }

    function ensureCorpusFile(fname) {
      if (!corpusShards[fname]) {
        corpusShards[fname] = fetch(basePath + '/data/qa-corpus/' + fname)
          .then(function (res) {
            if (!res.ok) throw new Error('Failed to load Q&A corpus shard');
            return res.json();
          })
          .then(function (shard) { corpusShardsLoaded[fname] = shard; return shard; });
      }
      return corpusShards[fname];
    }

    // Fetch only the shard files covering the retrieved entries (per the
    // manifest), then look each record up by id.
    function fetchCorpusFor(entries) {
      return ensureCorpusManifest().then(function (manifest) {
        var files = [];
        var plan = entries.map(function (e) {
          var d = (e.domains && e.domains[0]) || 'unknown';
          var listed = manifest[d] || [d + '.json'];
          var fname;
          if (listed.length === 1) {
            fname = listed[0];
          } else {
            var typed = d + '--' + e.type;
            if (listed.indexOf(typed + '.json') !== -1) {
              fname = typed + '.json';
            } else {
              // Type group split into char-sum buckets (same hash as builder).
              var buckets = listed.filter(function (f) { return f.indexOf(typed + '--') === 0; });
              if (buckets.length) {
                var h = 0;
                for (var i = 0; i < e.id.length; i++) h += e.id.charCodeAt(i);
                fname = typed + '--' + (h % buckets.length) + '.json';
              } else {
                fname = listed[0];
              }
            }
          }
          if (files.indexOf(fname) === -1) files.push(fname);
          return { id: e.id, fname: fname };
        });
        return Promise.all(files.map(ensureCorpusFile)).then(function () {
          var out = {};
          plan.forEach(function (p) {
            var shard = corpusShardsLoaded[p.fname];
            if (shard && shard[p.id]) out[p.id] = shard[p.id];
          });
          return out;
        });
      });
    }

    // Score with the shared search core, then re-rank (chat only): downweight
    // papers/news, upweight knowledge-bearing entity types, and drop
    // duplicate names keeping the highest-scored entry.
    function retrieve(question) {
      return ensureSearchIndex().then(function () {
        var q = question.trim().toLowerCase();
        var qTokens = window.KGSearch.uniqueTokens(q);
        var candidates = window.KGSearch.findCandidates(qTokens);
        var pool = window.KGSearch.search(question, 'all').slice(0, 50);
        pool.forEach(function (e) {
          var base = window.KGSearch.scoreEntry(e, q, qTokens, candidates.get(e.i) || 0);
          e._wscore = base * (TYPE_WEIGHTS[e.type] || 1);
        });
        pool.sort(function (a, b) { return b._wscore - a._wscore; });
        var seen = {};
        var out = [];
        for (var i = 0; i < pool.length && out.length < TOP_K; i++) {
          var key = (pool[i].name || pool[i].id).toLowerCase();
          if (seen[key]) continue;
          seen[key] = true;
          out.push(pool[i]);
        }
        return out;
      });
    }

    function entryContext(rec) {
      var lines = [
        '【' + (rec.name || rec.id) + '】 (ID: ' + rec.id + ')',
        prompt.labels.type + ': ' + rec.type,
        prompt.labels.summary + ': ' + (rec.summary || ''),
      ];
      if (rec.body) lines.push(prompt.labels.content + ':\n' + rec.body);
      if (rec.relations && rec.relations.length) {
        var relLines = rec.relations.map(function (r) {
          return r.direction === 'out'
            ? '  → ' + r.type + ' → ' + r.other_name + ' (' + r.other_id + ')'
            : '  ← ' + r.type + ' ← ' + r.other_name + ' (' + r.other_id + ')';
        });
        lines.push(prompt.labels.relations + ':\n' + relLines.join('\n'));
      }
      return lines.join('\n');
    }

    /* ---------- LLM streaming (OpenAI-compatible SSE) ---------- */

    function humanError(err) {
      if (err && err.status === 401 || err && err.status === 403) return strings.errorAuth;
      if (err && err.status === 429) return strings.errorRate;
      if (err && err.network) return strings.errorNetwork;
      return (strings.errorGeneric || 'Request failed: {detail}').replace('{detail}', String(err && err.message || err));
    }

    async function streamChat(cfg, messages, onUpdate, signal) {
      var res;
      try {
        res = await fetch(cfg.baseUrl.replace(/\/+$/, '') + '/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + cfg.apiKey,
          },
          body: JSON.stringify({
            model: cfg.model,
            messages: messages,
            temperature: 0.2,
            max_tokens: 2048,
            stream: true,
          }),
          signal: signal,
        });
      } catch (err) {
        if (err && err.name === 'AbortError') throw err;
        var netErr = new Error('network error');
        netErr.network = true;
        throw netErr;
      }
      if (!res.ok) {
        var detail = '';
        try {
          var body = await res.json();
          detail = body && body.error && body.error.message ? body.error.message : '';
        } catch (ignore) { /* non-JSON error body */ }
        var httpErr = new Error(detail || ('HTTP ' + res.status));
        httpErr.status = res.status;
        throw httpErr;
      }

      var reader = res.body.getReader();
      var decoder = new TextDecoder('utf-8');
      var buffer = '';
      var full = '';
      for (;;) {
        var chunk = await reader.read();
        if (chunk.done) break;
        buffer += decoder.decode(chunk.value, { stream: true });
        var nl;
        while ((nl = buffer.indexOf('\n')) !== -1) {
          var line = buffer.slice(0, nl).trim();
          buffer = buffer.slice(nl + 1);
          if (line.indexOf('data:') !== 0) continue;
          var payload = line.slice(5).trim();
          if (payload === '[DONE]') return full;
          try {
            var parsed = JSON.parse(payload);
            var choice = parsed.choices && parsed.choices[0];
            var delta = choice && choice.delta && choice.delta.content;
            if (delta) {
              full += delta;
              onUpdate(full);
            }
          } catch (ignore) { /* keepalive or partial JSON line */ }
        }
      }
      return full;
    }

    /* ---------- lightweight Markdown rendering ---------- */

    function escapeHtml(text) {
      var div = document.createElement('div');
      div.textContent = text == null ? '' : String(text);
      return div.innerHTML;
    }

    function renderInline(text) {
      var html = escapeHtml(text);
      html = html.replace(/`([^`]+)`/g, '<code>$1</code>');
      html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
      html = html.replace(/(^|[^*])\*([^*\n]+)\*/g, '$1<em>$2</em>');
      html = html.replace(/\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g,
        '<a href="$2" target="_blank" rel="noopener">$1</a>');
      return html;
    }

    function renderMarkdown(text) {
      // Split out fenced code blocks first so their content is never formatted.
      var parts = String(text || '').split(/```/);
      var out = [];
      for (var i = 0; i < parts.length; i++) {
        var part = parts[i];
        if (i % 2 === 1) {
          var code = part.replace(/^[a-zA-Z0-9+#-]*\n/, '');
          out.push('<pre><code>' + escapeHtml(code.replace(/\n$/, '')) + '</code></pre>');
          continue;
        }
        var lines = part.split('\n');
        var listType = null;
        var closeList = function () {
          if (listType) { out.push('</' + listType + '>'); listType = null; }
        };
        for (var j = 0; j < lines.length; j++) {
          var line = lines[j];
          var heading = line.match(/^(#{1,4})\s+(.*)$/);
          var ulItem = line.match(/^\s*[-*•]\s+(.*)$/);
          var olItem = line.match(/^\s*\d+[.)]\s+(.*)$/);
          if (heading) {
            closeList();
            var level = Math.min(heading[1].length + 2, 6);
            out.push('<h' + level + '>' + renderInline(heading[2]) + '</h' + level + '>');
          } else if (ulItem || olItem) {
            var want = ulItem ? 'ul' : 'ol';
            if (listType !== want) {
              closeList();
              out.push('<' + want + '>');
              listType = want;
            }
            out.push('<li>' + renderInline((ulItem || olItem)[1]) + '</li>');
          } else if (line.trim() === '') {
            closeList();
          } else {
            closeList();
            out.push('<p>' + renderInline(line) + '</p>');
          }
        }
        closeList();
      }
      return out.join('\n');
    }

    /* ---------- chat UI ---------- */

    function scrollToBottom() {
      messagesEl.scrollTop = messagesEl.scrollHeight;
    }

    function clearEmptyState() {
      var empty = messagesEl.querySelector('.empty-state');
      if (empty) empty.remove();
    }

    function appendMessage(role, text) {
      clearEmptyState();
      var item = el('div', 'ask-message ask-' + role);
      var bubble = el('div', 'ask-bubble');
      if (role === 'assistant') {
        bubble.innerHTML = renderMarkdown(text);
      } else {
        bubble.textContent = text;
      }
      item.appendChild(bubble);
      messagesEl.appendChild(item);
      scrollToBottom();
      return bubble;
    }

    function appendNote(text) {
      clearEmptyState();
      messagesEl.appendChild(el('div', 'ask-note', text));
      scrollToBottom();
    }

    function recordFocus(names) {
      lastFocusNames = names.filter(Boolean).slice(0, 3);
    }

    function renderSources(bubble, sources) {
      if (!sources.length) return;
      var wrap = el('div', 'ask-sources');
      wrap.appendChild(el('span', 'ask-sources-label', strings.sources || 'Sources'));

      if (mode === 'panel') {
        var allBtn = el('button', 'ask-highlight-all', strings.highlightAll || 'Highlight all in graph');
        allBtn.type = 'button';
        allBtn.addEventListener('click', function () {
          recordFocus(sources.map(function (s) { return s.name; }));
          var ids = sources.map(function (s) { return s.id; });
          if (opts.onHighlightAll) opts.onHighlightAll(ids);
          else if (opts.onSourceClick) ids.forEach(function (id) { opts.onSourceClick(id, null); });
        });
        wrap.appendChild(allBtn);
      }

      sources.forEach(function (s) {
        if (mode === 'panel') {
          // Chip body highlights the node in the graph; the ↗ link opens the
          // entry page.
          var chip = el('span', 'ask-source-chip ask-source-chip-btn');
          var nameBtn = el('button', 'ask-source-name', s.name);
          nameBtn.type = 'button';
          nameBtn.title = s.id;
          nameBtn.addEventListener('click', function (ev) {
            recordFocus([s.name]);
            if (opts.onSourceClick) opts.onSourceClick(s.id, ev);
          });
          var openLink = el('a', 'ask-source-open', '↗');
          openLink.href = basePath + '/entry/' + s.id + '/';
          openLink.title = strings.openEntry || 'Open entry';
          chip.appendChild(nameBtn);
          chip.appendChild(openLink);
          wrap.appendChild(chip);
        } else {
          var link = el('a', 'ask-source-chip', s.name);
          link.href = basePath + '/entry/' + s.id + '/';
          link.title = s.id;
          wrap.appendChild(link);
        }
      });
      bubble.appendChild(wrap);
      scrollToBottom();
    }

    function setStreaming(on) {
      streaming = on;
      sendBtn.classList.toggle('hidden', on);
      stopBtn.classList.toggle('hidden', !on);
      input.disabled = on;
      if (!on) input.focus();
    }

    async function handleSubmit() {
      var question = input.value.trim();
      if (!question || streaming) return;

      var cfg = getConfig();
      if (!cfg.apiKey) {
        settingsPanel.classList.remove('hidden');
        appendNote(strings.noKey || 'Please configure your API key first.');
        return;
      }

      appendMessage('user', question);
      input.value = '';
      setStreaming(true);
      abortController = new AbortController();
      var bubble = appendMessage('assistant', strings.stageRetrieving || strings.thinking || '…');

      try {
        var retrieved = await retrieve(question);
        if (!retrieved.length) {
          bubble.innerHTML = renderMarkdown(strings.noContext || '');
          history.push({ role: 'user', content: question });
          history.push({ role: 'assistant', content: strings.noContext || '' });
          saveHistory();
          return;
        }

        bubble.innerHTML = renderMarkdown(strings.stageLoading || strings.thinking || '…');
        var corpus = await fetchCorpusFor(retrieved);
        var contextParts = [];
        var sources = [];
        for (var i = 0; i < retrieved.length; i++) {
          var rec = corpus[retrieved[i].id];
          if (!rec) continue;
          contextParts.push(entryContext(rec));
          sources.push({ id: rec.id, name: rec.name || rec.id });
        }

        var userContent = prompt.wrap(contextParts.join('\n\n---\n\n'), question);
        // Panel mode: tell the model which entries are currently highlighted,
        // so follow-ups like "and their common neighbors?" make sense.
        if (mode === 'panel' && lastFocusNames.length) {
          userContent = (strings.focusPrefix || 'Current graph focus: ') +
            lastFocusNames.join(', ') + '\n' + userContent;
        }

        var messages = [{ role: 'system', content: prompt.system }]
          .concat(history.slice(-MAX_HISTORY_MESSAGES).map(function (m) {
            return { role: m.role, content: m.content };
          }))
          .concat([{ role: 'user', content: userContent }]);

        bubble.innerHTML = renderMarkdown(strings.stageGenerating || strings.thinking || '…');
        var answer = await streamChat(cfg, messages, function (text) {
          bubble.innerHTML = renderMarkdown(text);
          scrollToBottom();
        }, abortController.signal);

        bubble.innerHTML = renderMarkdown(answer);
        renderSources(bubble, sources);
        history.push({ role: 'user', content: question });
        history.push({ role: 'assistant', content: answer, sources: sources });
        saveHistory();
      } catch (err) {
        if (err && err.name === 'AbortError') {
          bubble.innerHTML += '<p class="ask-stopped">' + escapeHtml(strings.stopped || '(stopped)') + '</p>';
        } else {
          bubble.innerHTML = '<p class="ask-error">' + escapeHtml(humanError(err)) + '</p>';
        }
      } finally {
        setStreaming(false);
        scrollToBottom();
      }
    }

    /* ---------- session history (survives in-tab navigation/refresh) ---------- */

    var HISTORY_KEY = 'kg_ask_history_' + lang;

    function saveHistory() {
      try {
        sessionStorage.setItem(HISTORY_KEY, JSON.stringify(history.slice(-MAX_SAVED_MESSAGES)));
      } catch (ignore) { /* storage blocked or full */ }
    }

    function restoreHistory() {
      var saved = [];
      try { saved = JSON.parse(sessionStorage.getItem(HISTORY_KEY) || '[]'); } catch (ignore) { saved = []; }
      if (!saved || !saved.length) return;
      history = saved.slice(-MAX_SAVED_MESSAGES);
      history.forEach(function (m) {
        var bubble = appendMessage(m.role, m.content);
        if (m.role === 'assistant' && m.sources && m.sources.length) {
          renderSources(bubble, m.sources);
        }
      });
    }

    function clearHistory() {
      history = [];
      try { sessionStorage.removeItem(HISTORY_KEY); } catch (ignore) { /* noop */ }
      messagesEl.innerHTML = '';
      messagesEl.appendChild(el('div', 'empty-state', strings.empty || ''));
    }

    /* ---------- wiring ---------- */

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      handleSubmit();
    });

    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !e.shiftKey && !e.isComposing) {
        e.preventDefault();
        handleSubmit();
      }
    });

    stopBtn.addEventListener('click', function () {
      if (abortController) abortController.abort();
    });

    settingsToggle.addEventListener('click', function () {
      settingsPanel.classList.toggle('hidden');
      settingsStatus.textContent = '';
    });
    clearHistoryBtn.addEventListener('click', clearHistory);
    providerSel.addEventListener('change', onProviderChange);
    saveBtn.addEventListener('click', saveSettings);
    clearBtn.addEventListener('click', clearSettings);

    loadSettingsForm();
    restoreHistory();
  }

  window.KGAsk = { mount: mount };

  // Auto-mount on the standalone /ask/ page; the graph page mounts explicitly.
  var autoRoot = document.getElementById('ask-root');
  if (autoRoot && window.KGSearch) {
    mount(autoRoot, { mode: 'fullPage' });
  }
})();
