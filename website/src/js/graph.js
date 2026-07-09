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
          'font-size': 13,
          'font-weight': 600,
          'color': t.text,
          'text-valign': 'bottom',
          'text-halign': 'center',
          'text-margin-y': 6,
          'text-wrap': 'wrap',
          'text-max-width': 140,
          'text-background-color': t.bg,
          'text-background-opacity': 0.92,
          'text-background-shape': 'roundrectangle',
          'text-background-padding': 3,
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
          'width': ele => Math.min(110, 42 + Math.sqrt(ele.data('count') || 1) * 8),
          'height': ele => Math.min(110, 42 + Math.sqrt(ele.data('count') || 1) * 8),
          'font-size': 15,
          'font-weight': 700,
          'text-valign': 'center',
          'text-halign': 'center',
          'text-margin-y': 0,
          'text-max-width': 120,
          'border-width': 3,
          'border-color': t.clusterBorder,
          'background-opacity': 0.95,
          'label': ele => `${ele.data('name')}\n${ele.data('count')} 个实体`,
          'text-wrap': 'wrap',
          'color': t.text,
        },
      },
      {
        selector: 'node[!isCluster]',
        style: {
          'width': 22,
          'height': 22,
        },
      },
      {
        selector: 'edge',
        style: {
          'width': 1.5,
          'line-color': t.edge,
          'target-arrow-color': t.edge,
          'target-arrow-shape': 'triangle',
          'curve-style': 'bezier',
          'arrow-scale': 0.8,
        },
      },
      {
        selector: 'edge[isClusterEdge]',
        style: {
          'width': ele => Math.min(10, 1.5 + Math.log(ele.data('weight') || 1) * 1.8),
          'line-color': t.clusterEdge,
          'target-arrow-color': t.clusterEdge,
          'arrow-scale': 1,
        },
      },
      {
        selector: ':selected',
        style: {
          'border-width': 5,
          'border-color': t.accent,
          'border-opacity': 1,
        },
      },
      {
        selector: '.highlighted',
        style: {
          'border-width': 4,
          'border-color': t.accent,
          'width': 28,
          'height': 28,
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

  function runLayout(name) {
    if (!cy) return;
    const opts = { animate: true, animationDuration: 500, padding: 36, fit: true };
    let layout;
    if (name === 'cose') {
      layout = cy.layout({
        name: 'cose',
        ...opts,
        nodeRepulsion: 8000,
        idealEdgeLength: 120,
        componentSpacing: 100,
        nodeOverlap: 20,
        refresh: 20,
        fit: true,
        padding: 36,
        randomize: false,
      });
    } else if (name === 'circle') {
      layout = cy.layout({ name: 'circle', ...opts });
    } else if (name === 'grid') {
      layout = cy.layout({ name: 'grid', ...opts });
    } else {
      layout = cy.layout({ name: 'cose', ...opts });
    }
    layout.run();
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
      elements = [...fullGraphData.nodes, ...fullGraphData.edges];
    }

    if (elements.length === 0) {
      container.innerHTML = '<div class="empty-state">没有可显示的关系数据。</div>';
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
      if (count) html += `<br><span>${count} 个实体</span>`;
      if (type && !count) html += `<br><span>${escapeHtml(type)}${domains ? ' · ' + escapeHtml(domains) : ''}</span>`;
      showTooltip(html, evt.renderedPosition, container);
    });

    cy.on('mouseout', 'node', evt => {
      evt.target.removeClass('highlighted');
      hideTooltip();
    });

    cy.on('tapstart drag', () => hideTooltip());

    runLayout('cose');
  }

  function showClusterMembers(clusterId) {
    const cluster = clusterData.nodes.find(n => n.data.id === clusterId);
    if (!cluster) return;
    const members = new Set(cluster.data.members || []);

    const nodes = fullGraphData.nodes.filter(n => members.has(n.data.id));
    const edges = fullGraphData.edges.filter(
      e => members.has(e.data.source) && members.has(e.data.target)
    );

    if (cy) cy.destroy();
    const container = document.getElementById('full-graph');
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

    runLayout('cose');

    const titleEl = document.getElementById('graph-current-view');
    if (titleEl) {
      titleEl.textContent = `${cluster.data.name}（${cluster.data.count}）`;
      titleEl.classList.remove('hidden');
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
    loadData().then(() => {
      const centerId = entryGraph.dataset.centerId;
      const members = new Set([centerId]);
      const edges = [];
      for (const edge of fullGraphData.edges) {
        if (edge.data.source === centerId || edge.data.target === centerId) {
          edges.push(edge);
          members.add(edge.data.source);
          members.add(edge.data.target);
        }
      }
      const nodes = fullGraphData.nodes.filter(n => members.has(n.data.id));
      if (nodes.length === 0) {
        entryGraph.innerHTML = '<div class="empty-state">暂无关系数据</div>';
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
      cy.layout({ name: 'cose', padding: 24, nodeRepulsion: 6000, idealEdgeLength: 90, animate: true }).run();
      setTimeout(() => {
        const centerNode = cy.getElementById(centerId);
        if (centerNode.length) {
          centerNode.style({ 'width': 34, 'height': 34, 'border-width': 4, 'border-color': themeColors().accent });
          cy.fit(centerNode.closedNeighborhood(), 60);
        }
      }, 650);
    });
  }

  // Full graph page
  const fullGraph = document.getElementById('full-graph');
  if (fullGraph && typeof cytoscape !== 'undefined') {
    tooltipEl = document.getElementById('graph-tooltip');

    loadData().then(() => {
      initGraph(fullGraph, 'clusters');

      document.getElementById('view-clusters')?.addEventListener('click', () => {
        initGraph(fullGraph, 'clusters');
        updateActiveButton('view-clusters');
      });
      document.getElementById('view-full')?.addEventListener('click', () => {
        if (fullGraphData.nodes.length > 1500) {
          if (!confirm(`当前有 ${fullGraphData.nodes.length} 个节点，全图加载可能会卡顿。是否继续？`)) return;
        }
        initGraph(fullGraph, 'full');
        updateActiveButton('view-full');
      });

      document.getElementById('fit-graph')?.addEventListener('click', () => cy && cy.fit());
      document.getElementById('reset-graph')?.addEventListener('click', () => {
        initGraph(fullGraph, 'clusters');
        updateActiveButton('view-clusters');
      });

      const graphSearch = document.getElementById('graph-search');
      const graphSearchResults = document.getElementById('graph-search-results');
      if (graphSearch) {
        let searchData = { entries: [] };
        fetch(basePath + '/data/search-index.json')
          .then(r => r.json())
          .then(d => { searchData = d; })
          .catch(() => {});

        graphSearch.addEventListener('input', () => {
          const q = graphSearch.value.trim().toLowerCase();
          if (!q || !graphSearchResults) {
            graphSearchResults.innerHTML = '';
            return;
          }
          const matches = searchData.entries
            .filter(e => (e.name || '').toLowerCase().includes(q) || e.id.toLowerCase().includes(q))
            .slice(0, 10);
          graphSearchResults.innerHTML = matches.map(e =>
            `<div class="graph-search-result" data-id="${e.id}">${escapeHtml(e.name)}</div>`
          ).join('');
          graphSearchResults.querySelectorAll('.graph-search-result').forEach(el => {
            el.addEventListener('click', () => {
              const id = el.dataset.id;
              if (currentMode === 'clusters') {
                const cluster = clusterData.nodes.find(n => (n.data.members || []).includes(id));
                if (cluster) showClusterMembers(cluster.data.id);
              }
              if (cy) {
                const node = cy.getElementById(id);
                if (node.length) {
                  cy.fit(node, 60);
                  node.select();
                }
              }
              graphSearchResults.innerHTML = '';
              graphSearch.value = '';
            });
          });
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
