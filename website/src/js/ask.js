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

  var PROMPTS = {
    zh: {
      system: '你是一个熟悉人形机器人行业的知识图谱助手。请严格依据下面提供的知识图谱内容回答问题。' +
        '如果资料中没有足够信息，请明确说明。回答请使用中文，并在相关处引用条目 ID（如 ent_process_p4_1_1）。',
      labels: { type: '类型', summary: '摘要', content: '内容', relations: '关系' },
      wrap: function (context, question) {
        return '知识图谱资料：\n\n' + context + '\n\n用户问题：' + question + '\n\n请回答：';
      },
    },
    en: {
      system: 'You are a knowledge-graph assistant familiar with the humanoid robot industry. ' +
        'Answer strictly based on the knowledge graph material provided below. If the material is ' +
        'insufficient, say so explicitly. Answer in English and cite entry IDs (e.g. ent_process_p4_1_1) where relevant.',
      labels: { type: 'Type', summary: 'Summary', content: 'Content', relations: 'Relations' },
      wrap: function (context, question) {
        return 'Knowledge graph material:\n\n' + context + '\n\nUser question: ' + question + '\n\nPlease answer:';
      },
    },
    ko: {
      system: '당신은 휴로봇 산업에 정통한 지식 그래프 어시스턴트입니다. 아래 제공된 지식 그래프 자료만을 근거로 ' +
        '답변하세요. 자료가 부족하면 명확히 밝히세요. 한국어로 답변하고, 관련된 곳에 개체 ID(예: ent_process_p4_1_1)를 인용하세요.',
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
    var sendBtn = el('button', 'ask-send-btn', strings.send || 'Send');
    sendBtn.type = 'submit';
    var stopBtn = el('button', 'btn btn-secondary hidden', strings.stop || 'Stop');
    stopBtn.type = 'button';

    var actions = el('div', 'ask-actions');
    actions.appendChild(settingsToggle);
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
    var corpusPromise = null;
    var history = []; // {role: 'user'|'assistant', content: string}
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

    function ensureCorpus() {
      if (!corpusPromise) {
        corpusPromise = fetch(basePath + '/data/qa-corpus.json')
          .then(function (res) {
            if (!res.ok) throw new Error('Failed to load Q&A corpus');
            return res.json();
          });
      }
      return corpusPromise;
    }

    function retrieve(question) {
      return ensureSearchIndex().then(function () {
        return window.KGSearch.search(question, 'all').slice(0, TOP_K);
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
      var bubble = appendMessage('assistant', strings.thinking || '…');

      try {
        var retrieved = await retrieve(question);
        if (!retrieved.length) {
          bubble.innerHTML = renderMarkdown(strings.noContext || '');
          history.push({ role: 'user', content: question });
          history.push({ role: 'assistant', content: strings.noContext || '' });
          return;
        }

        var corpus = await ensureCorpus();
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
          .concat(history.slice(-MAX_HISTORY_MESSAGES))
          .concat([{ role: 'user', content: userContent }]);

        var answer = await streamChat(cfg, messages, function (text) {
          bubble.innerHTML = renderMarkdown(text);
          scrollToBottom();
        }, abortController.signal);

        bubble.innerHTML = renderMarkdown(answer);
        renderSources(bubble, sources);
        history.push({ role: 'user', content: question });
        history.push({ role: 'assistant', content: answer });
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
    providerSel.addEventListener('change', onProviderChange);
    saveBtn.addEventListener('click', saveSettings);
    clearBtn.addEventListener('click', clearSettings);

    loadSettingsForm();
  }

  window.KGAsk = { mount: mount };

  // Auto-mount on the standalone /ask/ page; the graph page mounts explicitly.
  var autoRoot = document.getElementById('ask-root');
  if (autoRoot && window.KGSearch) {
    mount(autoRoot, { mode: 'fullPage' });
  }
})();
