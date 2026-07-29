/* BYOK ChatGPT-style Q&A over the knowledge graph.
 *
 * Pure frontend: the user's API key is stored only in this browser's
 * localStorage and requests go directly from the browser to the provider.
 * Retrieval reuses the search-page scoring via window.KGSearch (search.js),
 * then fetches data/qa-corpus.json lazily for RAG context.
 */

(function () {
  'use strict';

  var root = document.getElementById('ask-root');
  if (!root || !window.KGSearch) return;

  var basePath = root.dataset.basePath || '';
  var lang = document.body.dataset.lang || 'zh';
  var strings = root.dataset;

  var messagesEl = document.getElementById('ask-messages');
  var form = document.getElementById('ask-form');
  var input = document.getElementById('ask-input');
  var sendBtn = document.getElementById('ask-send-btn');
  var stopBtn = document.getElementById('ask-stop-btn');
  var settingsPanel = document.getElementById('ask-settings');
  var settingsToggle = document.getElementById('ask-settings-toggle');
  var providerSel = document.getElementById('ask-provider');
  var apiKeyInput = document.getElementById('ask-api-key');
  var baseUrlInput = document.getElementById('ask-base-url');
  var modelInput = document.getElementById('ask-model');
  var saveBtn = document.getElementById('ask-settings-save');
  var clearBtn = document.getElementById('ask-settings-clear');
  var settingsStatus = document.getElementById('ask-settings-status');

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
  var prompt = PROMPTS[lang] || PROMPTS.zh;

  var searchIndexPromise = null;
  var corpusPromise = null;
  var history = []; // {role: 'user'|'assistant', content: string}
  var streaming = false;
  var abortController = null;

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
    if (settingsStatus) settingsStatus.textContent = strings.settingsSaved || '';
  }

  function clearSettings() {
    Object.keys(LS).forEach(function (k) { localStorage.removeItem(LS[k]); });
    loadSettingsForm();
    if (settingsStatus) settingsStatus.textContent = strings.settingsCleared || '';
  }

  /* ---------- retrieval (reuses search.js scoring) ---------- */

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
      for (var j = 0; j < lines.length; j++) {
        var line = lines[j];
        var heading = line.match(/^(#{1,4})\s+(.*)$/);
        var ulItem = line.match(/^\s*[-*•]\s+(.*)$/);
        var olItem = line.match(/^\s*\d+[.)]\s+(.*)$/);
        var closeList = function () {
          if (listType) { out.push('</' + listType + '>'); listType = null; }
        };
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
      if (listType) { out.push('</' + listType + '>'); listType = null; }
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
    var item = document.createElement('div');
    item.className = 'ask-message ask-' + role;
    var bubble = document.createElement('div');
    bubble.className = 'ask-bubble';
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
    var note = document.createElement('div');
    note.className = 'ask-note';
    note.textContent = text;
    messagesEl.appendChild(note);
    scrollToBottom();
  }

  function renderSources(bubble, sources) {
    if (!sources.length) return;
    var wrap = document.createElement('div');
    wrap.className = 'ask-sources';
    var label = document.createElement('span');
    label.className = 'ask-sources-label';
    label.textContent = strings.sources || 'Sources';
    wrap.appendChild(label);
    for (var i = 0; i < sources.length; i++) {
      var chip = document.createElement('a');
      chip.className = 'ask-source-chip';
      chip.href = basePath + '/entry/' + sources[i].id + '/';
      chip.textContent = sources[i].name;
      chip.title = sources[i].id;
      wrap.appendChild(chip);
    }
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

      var messages = [{ role: 'system', content: prompt.system }]
        .concat(history.slice(-MAX_HISTORY_MESSAGES))
        .concat([{ role: 'user', content: prompt.wrap(contextParts.join('\n\n---\n\n'), question) }]);

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
    if (settingsStatus) settingsStatus.textContent = '';
  });
  providerSel.addEventListener('change', onProviderChange);
  saveBtn.addEventListener('click', saveSettings);
  clearBtn.addEventListener('click', clearSettings);

  loadSettingsForm();
})();
