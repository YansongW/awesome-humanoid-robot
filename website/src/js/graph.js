/* Cytoscape.js graph visualization for the knowledge graph */

(function () {
  'use strict';

  const DOMAIN_COLORS = {
    '00_foundations': '#7c8798',
    '01_raw_materials': '#2a9d8f',
    '02_components': '#5d8c48',
    '03_manufacturing_processes': '#c38e3c',
    '04_assembly_integration_testing': '#b3592a',
    '05_mass_production': '#a84442',
    '06_design_engineering': '#7d5a8a',
    '07_ai_models_algorithms': '#3d7ea6',
    '08_software_middleware': '#5a8fbd',
    '09_data_datasets': '#2d5a7b',
    '10_evaluation_benchmarks': '#c9a227',
    '10_benchmarks_evaluation': '#c9a227',
    '11_applications_markets': '#b34d73',
    '12_policy_regulation_ethics': '#6b5b4f',
    unknown: '#6b7280',
  };

  const ACCENT = '#8b5a2b';
  const ACCENT_DARK = '#d4a574';
  const UI = window.GRAPH_TEXT || {
    loading: 'Loading graph…',
    empty: 'No relation data to display.',
    noRelations: 'No relation data yet',
    clusterCount: '{name}\n{count} entities',
    clusterPruned: '(showing top {count} core entities)',
    clusterTotal: '({count})',
    confirmFull: 'There are {total} nodes; the full graph will show only the top {count} most-connected nodes. Continue?',
    entityCount: '{count} entities',
    backToClusters: 'Cluster view',
  };

  function t(key, vars) {
    let s = UI[key] || key;
    if (vars) {
      for (const [k, v] of Object.entries(vars)) {
        s = s.replace(new RegExp('\\{' + k + '\\}', 'g'), v);
      }
    }
    return s;
  }

  function getBasePath() {
    const path = window.location.pathname;
    const m = path.match(/^\/(en|ko)(?=\/)/);
    return m ? '/' + m[1] : '';
  }
  const basePath = getBasePath();

  function isDark() {
    return document.documentElement.getAttribute('data-theme') === 'dark';
  }

  function themeColors() {
    if (isDark()) {
      return {
        text: '#f4f1ed',
        textSecondary: '#c4bdb5',
        bg: '#161412',
        surface: '#1f1c19',
        border: '#4f4942',
        clusterBorder: '#6b6560',
        edge: '#5a544e',
        clusterEdge: '#7a746e',
        accent: ACCENT_DARK,
      };
    }
    return {
      text: '#1f1d1a',
      textSecondary: '#5a5650',
      bg: '#faf9f7',
      surface: '#ffffff',
      border: '#d6d1c8',
      clusterBorder: '#b8b2a8',
      edge: '#b8b2a8',
      clusterEdge: '#9ca3af',
      accent: ACCENT,
    };
  }

  function getDomainColor(domain) {
    return DOMAIN_COLORS[domain] || DOMAIN_COLORS.unknown;
  }

  function getPrimaryDomain(node) {
    const domains = node.data('domains') || [];
    return domains[0] || 'unknown';
  }

  let cy = null;
  let currentMode = 'clusters';
  let fullGraphData = null;
  let clusterData = null;
  let tooltipEl = null;

  async function loadData() {
    try {
      const [relationsRes, clustersRes] = await Promise.all([
        fetch(basePath + '/data/relations.json'),
        fetch(basePath + '/data/clusters.json'),
      ]);
      if (!relationsRes.ok || !clustersRes.ok) throw new Error('Failed to load graph data');
      fullGraphData = await relationsRes.json();
      clusterData = await clustersRes.json();
      const labels = window.DOMAIN_LABELS || {};
      for (const node of clusterData.nodes) {
        const id = node.data.id;
        if (labels[id]) {
          node.data.name = labels[id];
        }
      }
    } catch (err) {
      console.error(err);
      fullGraphData = { nodes: [], edges: [] };
      clusterData = { nodes: [], edges: [] };
    }
  }

  function makeStylesheet() {
    const t = themeColors();
    return [
      {
        selector: 'node',
        style: {
          'background-color': ele => getDomainColor(getPrimaryDomain(ele)),
          'label': 'data(name)',
          'font-size': 14,
          'font-weight': 600,
          'color': t.text,
          'text-valign': 'bottom',
          'text-halign': 'center',
          'text-margin-y': 12,
          'text-wrap': 'wrap',
          'text-max-width': 160,
          'text-background-color': t.bg,
          'text-background-opacity': 0.98,
          'text-background-shape': 'roundrectangle',
          'text-background-padding': 5,
          'text-border-color': t.border,
          'text-border-width': 1,
          'text-border-opacity': 0.6,
          'border-width': 2,
          'border-color': t.border,
          'transition-property': 'background-color, border-color, width, height',
          'transition-duration': '0.15s',
        },
      },
      {
        selector: 'node[isCluster]',
        style: {
          'width': ele => Math.min(140, 56 + Math.sqrt(ele.data('count') || 1) * 10),
          'height': ele => Math.min(140, 56 + Math.sqrt(ele.data('count') || 1) * 10),
          'font-size': 15,
          'font-weight': 700,
          'text-valign': 'center',
          'text-halign': 'center',
          'text-margin-y': 0,
          'text-max-width': 120,
          'border-width': 3,
          'border-color': t.clusterBorder,
          'background-opacity': 0.95,
          'label': ele => t('clusterCount', { name: ele.data('name'), count: ele.data('count') }),
          'text-wrap': 'wrap',
          'color': t.text,
          'shape': 'roundrectangle',
        },
      },
      {
        selector: 'node[!isCluster]',
        style: {
          'width': 28,
          'height': 28,
          'min-zoomed-font-size': 12,
        },
      },
      {
        selector: 'edge',
        style: {
          'width': 2,
          'line-color': t.edge,
          'target-arrow-color': t.edge,
          'target-arrow-shape': 'triangle',
          'curve-style': 'unbundled-bezier',
          'control-point-step-size': 30,
          'arrow-scale': 0.9,
          'opacity': 0.75,
          'transition-property': 'line-color, target-arrow-color, width, opacity',
          'transition-duration': '0.15s',
        },
      },
      {
        selector: 'edge[isClusterEdge]',
        style: {
          'width': ele => Math.min(12, 2 + Math.log(ele.data('weight') || 1) * 2),
          'line-color': t.clusterEdge,
          'target-arrow-color': t.clusterEdge,
          'arrow-scale': 1,
          'opacity': 0.9,
        },
      },
      {
        selector: ':selected',
        style: {
          'border-width': 5,
          'border-color': t.accent,
          'border-opacity': 1,
          'background-color': t.accent,
          'color': '#fff',
          'text-background-color': t.accent,
          'text-border-color': t.accent,
        },
      },
      {
        selector: 'node[!isCluster]:hover',
        style: {
          'border-width': 4,
          'border-color': t.accent,
          'width': 36,
          'height': 36,
          'background-color': t.accent,
          'color': '#fff',
          'text-background-color': t.accent,
          'text-border-color': t.accent,
          'z-index': 999,
        },
      },
      {
        selector: '.highlighted',
        style: {
          'border-width': 4,
          'border-color': t.accent,
          'width': 34,
          'height': 34,
          'background-color': t.accent,
        },
      },
      {
        selector: '.dimmed',
        style: {
          'opacity': 0.12,
        },
      },
    ];
  }

  function runLayout(name, nodeCount) {
    if (!cy) return;
    const isLarge = nodeCount > 150;
    const opts = { animate: !isLarge, animationDuration: isLarge ? 0 : 500, padding: 36, fit: true };
    let layout;
    if (name === 'cose') {
      layout = cy.layout({
        name: 'cose',
        ...opts,
        nodeRepulsion: isLarge ? 12000 : 8000,
        idealEdgeLength: isLarge ? 160 : 120,
        componentSpacing: isLarge ? 160 : 100,
        nodeOverlap: isLarge ? 40 : 20,
        refresh: isLarge ? 10 : 20,
        fit: true,
        padding: 36,
        randomize: false,
        numIter: isLarge ? 1500 : 3000,
        coolingFactor: isLarge ? 0.9 : 0.95,
      });
    } else if (name === 'circle') {
      layout = cy.layout({ name: 'circle', ...opts });
    } else if (name === 'grid') {
      layout = cy.layout({ name: 'grid', ...opts });
    } else {
      layout = cy.layout({ name: 'cose', ...opts });
    }
    layout.run();
    return layout;
  }

  function showTooltip(content, renderedPos, container) {
    if (!tooltipEl || !container) return;
    tooltipEl.innerHTML = content;
    tooltipEl.style.display = 'block';
    tooltipEl.style.left = (renderedPos.x + container.offsetLeft + 12) + 'px';
    tooltipEl.style.top = (renderedPos.y + container.offsetTop + 12) + 'px';
  }

  function hideTooltip() {
    if (!tooltipEl) return;
    tooltipEl.style.display = 'none';
  }

  const activeDomains = new Set();

  const MAX_FULL_GRAPH_NODES = 250;

  function getFilteredFullElements() {
    const domainFilter = activeDomains.size > 0 ? activeDomains : null;
    let nodes = fullGraphData.nodes.filter(n => {
      if (!domainFilter) return true;
      const d = getPrimaryDomainFromData(n.data);
      return domainFilter.has(d);
    });

    // Prune very large full graphs to keep rendering interactive.
    if (nodes.length > MAX_FULL_GRAPH_NODES) {
      const degree = new Map();
      for (const n of nodes) degree.set(n.data.id, 0);
      for (const e of fullGraphData.edges) {
        if (degree.has(e.data.source)) degree.set(e.data.source, (degree.get(e.data.source) || 0) + 1);
        if (degree.has(e.data.target)) degree.set(e.data.target, (degree.get(e.data.target) || 0) + 1);
      }
      nodes = nodes
        .sort((a, b) => (degree.get(b.data.id) || 0) - (degree.get(a.data.id) || 0))
        .slice(0, MAX_FULL_GRAPH_NODES);
    }

    const nodeIds = new Set(nodes.map(n => n.data.id));
    const edges = fullGraphData.edges.filter(e => nodeIds.has(e.data.source) && nodeIds.has(e.data.target));
    return { nodes, edges };
  }

  function getPrimaryDomainFromData(data) {
    const domains = data.domains || [];
    return domains[0] || 'unknown';
  }

  function showLoading(container) {
    container.innerHTML = `<div class="graph-loading"><div class="spinner"></div><span>${escapeHtml(t('loading'))}</span></div>`;
  }

  function initGraph(container, mode) {
    currentMode = mode || 'clusters';
    if (cy) {
      cy.destroy();
      cy = null;
    }

    let elements = [];
    if (currentMode === 'clusters') {
      elements = [...clusterData.nodes, ...clusterData.edges];
    } else if (currentMode === 'full') {
      const filtered = getFilteredFullElements();
      elements = [...filtered.nodes, ...filtered.edges];
    }

    if (elements.length === 0) {
      container.innerHTML = `<div class="empty-state">${escapeHtml(t('empty'))}</div>`;
      return;
    }

    cy = cytoscape({
      container: container,
      elements: elements,
      style: makeStylesheet(),
      minZoom: 0.08,
      maxZoom: 4,
      wheelSensitivity: 0.2,
    });

    // Only show labels for nodes with degree >= 2 in full graph to reduce clutter.
    if (currentMode === 'full') {
      cy.nodes().forEach(n => {
        if (n.degree() < 2) {
          n.style('label', '');
        }
      });
    }

    cy.on('tap', 'node[isCluster]', evt => {
      const clusterId = evt.target.id();
      showClusterMembers(clusterId);
    });

    cy.on('tap', 'node[!isCluster]', evt => {
      const id = evt.target.id();
      window.location.href = basePath + '/entry/' + id + '/';
    });

    cy.on('mouseover', 'node', evt => {
      const node = evt.target;
      node.addClass('highlighted');
      const name = node.data('name') || node.data('id');
      const count = node.data('count');
      const type = node.data('type') || '';
      const domains = (node.data('domains') || []).join(', ');
      let html = `<strong>${escapeHtml(name)}</strong>`;
      if (count) html += `<br><span>${t('entityCount', { count })}</span>`;
      if (type && !count) html += `<br><span>${escapeHtml(type)}${domains ? ' · ' + escapeHtml(domains) : ''}</span>`;
      showTooltip(html, evt.renderedPosition, container);
    });

    cy.on('mouseout', 'node', evt => {
      evt.target.removeClass('highlighted');
      hideTooltip();
    });

    cy.on('tapstart drag', () => hideTooltip());

    const layoutName = 'cose';
    runLayout(layoutName, elements.length);
    updateDomainFilterState();
  }

  const MAX_SUBGRAPH_NODES = 250;

  function showClusterMembers(clusterId) {
    const cluster = clusterData.nodes.find(n => n.data.id === clusterId);
    if (!cluster) return;
    const members = new Set(cluster.data.members || []);

    let nodes = fullGraphData.nodes.filter(n => members.has(n.data.id));
    let edges = fullGraphData.edges.filter(
      e => members.has(e.data.source) && members.has(e.data.target)
    );

    // For very large clusters, keep only the most connected nodes to preserve
    // interactivity and readability.
    let pruned = false;
    if (nodes.length > MAX_SUBGRAPH_NODES) {
      pruned = true;
      const degree = new Map();
      for (const n of nodes) degree.set(n.data.id, 0);
      for (const e of edges) {
        degree.set(e.data.source, (degree.get(e.data.source) || 0) + 1);
        degree.set(e.data.target, (degree.get(e.data.target) || 0) + 1);
      }
      nodes = nodes
        .sort((a, b) => (degree.get(b.data.id) || 0) - (degree.get(a.data.id) || 0))
        .slice(0, MAX_SUBGRAPH_NODES);
      const keep = new Set(nodes.map(n => n.data.id));
      edges = edges.filter(e => keep.has(e.data.source) && keep.has(e.data.target));
    }

    if (cy) cy.destroy();
    const container = document.getElementById('full-graph');
    if (nodes.length === 0) {
      container.innerHTML = `<div class="empty-state">${escapeHtml(t('empty'))}</div>`;
      return;
    }
    showLoading(container);

    cy = cytoscape({
      container: container,
      elements: [...nodes, ...edges],
      style: makeStylesheet(),
      minZoom: 0.15,
      maxZoom: 4,
      wheelSensitivity: 0.2,
    });

    cy.on('tap', 'node', evt => {
      window.location.href = basePath + '/entry/' + evt.target.id() + '/';
    });

    cy.on('mouseover', 'node', evt => {
      evt.target.addClass('highlighted');
      const name = evt.target.data('name') || evt.target.id();
      const type = evt.target.data('type') || '';
      showTooltip(`<strong>${escapeHtml(name)}</strong>${type ? '<br><span>' + escapeHtml(type) + '</span>' : ''}`, evt.renderedPosition, container);
    });

    cy.on('mouseout', 'node', evt => {
      evt.target.removeClass('highlighted');
      hideTooltip();
    });

    cy.on('tapstart drag', () => hideTooltip());

    runLayout('cose', nodes.length);
    updateDomainFilterState();

    const titleEl = document.getElementById('graph-current-view');
    if (titleEl) {
      const suffix = pruned ? t('clusterPruned', { count: nodes.length }) : t('clusterTotal', { count: cluster.data.count });
      titleEl.textContent = `${cluster.data.name}${suffix}`;
      titleEl.classList.remove('hidden');
      titleEl.classList.add('cluster-drilldown');
    }
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Entry page subgraph
  const entryGraph = document.getElementById('entry-graph');
  if (entryGraph && typeof cytoscape !== 'undefined') {
    const centerId = entryGraph.dataset.centerId;
    entryGraph.innerHTML = `<div class="graph-loading"><div class="spinner"></div><span>${escapeHtml(t('loading'))}</span></div>`;
    fetch(`${basePath}/data/subgraphs/${centerId}.json`)
      .then(r => {
        if (!r.ok) throw new Error('subgraph not found');
        return r.json();
      })
      .then(sg => {
        const nodes = sg.nodes || [];
        const edges = sg.edges || [];
        if (nodes.length === 0) {
          entryGraph.innerHTML = `<div class="empty-state">${escapeHtml(t('noRelations'))}</div>`;
          return;
        }
        cy = cytoscape({
          container: entryGraph,
          elements: [...nodes, ...edges],
          style: makeStylesheet(),
          minZoom: 0.2,
          maxZoom: 3,
          wheelSensitivity: 0.3,
        });
        cy.on('tap', 'node', evt => {
          window.location.href = basePath + '/entry/' + evt.target.id() + '/';
        });
        const layout = runLayout('cose', nodes.length);
        if (layout && layout.one) {
          layout.one('layoutstop', () => {
            const centerNode = cy.getElementById(centerId);
            if (centerNode.length) {
              centerNode.style({
                'width': 38,
                'height': 38,
                'border-width': 5,
                'border-color': themeColors().accent,
                'background-color': themeColors().accent,
              });
              cy.fit(centerNode.closedNeighborhood(), 60);
            }
          });
        } else {
          setTimeout(() => {
            const centerNode = cy.getElementById(centerId);
            if (centerNode.length) {
              centerNode.style({
                'width': 38,
                'height': 38,
                'border-width': 5,
                'border-color': themeColors().accent,
                'background-color': themeColors().accent,
              });
              cy.fit(centerNode.closedNeighborhood(), 60);
            }
          }, 650);
        }
      })
      .catch(err => {
        console.error(err);
        entryGraph.innerHTML = `<div class="empty-state">${escapeHtml(t('empty'))}</div>`;
      });
  }

  // Full graph page
  const fullGraph = document.getElementById('full-graph');
  if (fullGraph && typeof cytoscape !== 'undefined') {
    tooltipEl = document.getElementById('graph-tooltip');

    loadData().then(() => {
      initGraph(fullGraph, 'clusters');

      const titleEl = document.getElementById('graph-current-view');

      function backToClusters() {
        if (titleEl) {
          titleEl.classList.remove('cluster-drilldown');
          titleEl.textContent = UI.backToClusters || 'Cluster view';
        }
        initGraph(fullGraph, 'clusters');
        updateActiveButton('view-clusters');
      }

      document.getElementById('view-clusters')?.addEventListener('click', backToClusters);
      if (titleEl) {
        titleEl.addEventListener('click', () => {
          if (titleEl.classList.contains('cluster-drilldown')) {
            backToClusters();
          }
        });
      }
      document.getElementById('view-full')?.addEventListener('click', () => {
        const visibleCount = Math.min(fullGraphData.nodes.length, MAX_FULL_GRAPH_NODES);
        if (fullGraphData.nodes.length > MAX_FULL_GRAPH_NODES) {
          const msg = t('confirmFull', { total: fullGraphData.nodes.length, count: visibleCount });
          if (!confirm(msg)) return;
        }
        if (titleEl) titleEl.classList.remove('cluster-drilldown');
        initGraph(fullGraph, 'full');
        updateActiveButton('view-full');
      });

      document.getElementById('fit-graph')?.addEventListener('click', () => cy && cy.fit());
      document.getElementById('reset-graph')?.addEventListener('click', () => {
        activeDomains.clear();
        document.querySelectorAll('#domain-filters input[type="checkbox"]').forEach(cb => {
          cb.checked = cb.value === 'all';
        });
        backToClusters();
      });

      const domainFilters = document.getElementById('domain-filters');
      function updateDomainFilterState() {
        if (!domainFilters) return;
        const disabled = currentMode === 'clusters';
        domainFilters.querySelectorAll('input[type="checkbox"]').forEach(cb => {
          cb.disabled = disabled;
        });
        domainFilters.classList.toggle('disabled', disabled);
      }
      if (domainFilters) {
        domainFilters.addEventListener('change', () => {
          const allCb = domainFilters.querySelector('input[value="all"]');
          const checkboxes = Array.from(domainFilters.querySelectorAll('input[type="checkbox"]'));
          const checked = checkboxes.filter(cb => cb.checked).map(cb => cb.value);

          if (checked.includes('all')) {
            activeDomains.clear();
            checkboxes.filter(cb => cb.value !== 'all').forEach(cb => cb.checked = false);
          } else {
            activeDomains.clear();
            checked.forEach(v => activeDomains.add(v));
            if (allCb) allCb.checked = false;
          }

          if (currentMode === 'full') {
            initGraph(fullGraph, 'full');
          }
        });
      }
      updateDomainFilterState();

      const graphSearch = document.getElementById('graph-search');
      const graphSearchResults = document.getElementById('graph-search-results');
      if (graphSearch) {
        let searchData = { entries: [] };
        // Lightweight names-only index (falls back to the full search index).
        fetch(basePath + '/data/names.json')
          .then(r => { if (!r.ok) throw new Error(); return r.json(); })
          .then(d => { searchData = { entries: d }; })
          .catch(() => {
            fetch(basePath + '/data/search-index.json')
              .then(r => r.json())
              .then(d => { searchData = d; })
              .catch(() => {});
          });

        let graphSearchTimer = null;
        graphSearch.addEventListener('input', () => {
          clearTimeout(graphSearchTimer);
          graphSearchTimer = setTimeout(() => {
            const q = graphSearch.value.trim().toLowerCase();
            if (!q || !graphSearchResults) {
              if (graphSearchResults) graphSearchResults.innerHTML = '';
              return;
            }
            const matches = searchData.entries
              .filter(e => (e.name || '').toLowerCase().includes(q) || e.id.toLowerCase().includes(q) || (e.summary || '').toLowerCase().includes(q))
              .slice(0, 10);
            graphSearchResults.innerHTML = matches.map(e =>
              `<div class="graph-search-result" data-id="${e.id}">${escapeHtml(e.name)}</div>`
            ).join('');
            graphSearchResults.querySelectorAll('.graph-search-result').forEach(el => {
              el.addEventListener('click', () => {
                const id = el.dataset.id;
                let found = false;
                if (currentMode === 'clusters') {
                  const cluster = clusterData.nodes.find(n => (n.data.members || []).includes(id));
                  if (cluster) {
                    showClusterMembers(cluster.data.id);
                    found = true;
                  }
                }
                if (cy) {
                  const node = cy.getElementById(id);
                  if (node.length) {
                    cy.fit(node, 60);
                    node.select();
                    found = true;
                  }
                }
                if (!found) {
                  window.location.href = basePath + '/entry/' + id + '/';
                }
                graphSearchResults.innerHTML = '';
                graphSearch.value = '';
              });
            });
          }, 180);
        });

        document.addEventListener('click', (e) => {
          if (!graphSearch.contains(e.target) && !graphSearchResults.contains(e.target)) {
            graphSearchResults.innerHTML = '';
          }
        });
      }
    });
  }

  function updateActiveButton(id) {
    document.querySelectorAll('.graph-view-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById(id)?.classList.add('active');
  }
})();
