/* Cytoscape.js graph visualization for the knowledge graph */

(function () {
  'use strict';

  const COLORS = {
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
    default: '#6b7280',
  };

  const CLUSTER_SIZE_SCALE = 6;
  const CLUSTER_FONT_SIZE = 14;
  const NODE_SIZE = 18;
  const NODE_FONT_SIZE = 10;

  let cy = null;
  let currentMode = 'clusters'; // 'clusters' | 'domain' | 'full'
  let fullGraphData = null;
  let clusterData = null;

  function getBasePath() {
    const path = window.location.pathname;
    const m = path.match(/^\/(en|ko)(?=\/)/);
    return m ? '/' + m[1] : '';
  }
  const basePath = getBasePath();

  function getDomainColor(domain) {
    return COLORS[domain] || COLORS.default;
  }

  function getPrimaryDomain(node) {
    const domains = node.data('domains') || [];
    return domains[0] || 'unknown';
  }

  async function loadData() {
    try {
      const [relationsRes, clustersRes] = await Promise.all([
        fetch('/data/relations.json'),
        fetch('/data/clusters.json'),
      ]);
      if (!relationsRes.ok || !clustersRes.ok) throw new Error('Failed to load graph data');
      fullGraphData = await relationsRes.json();
      clusterData = await clustersRes.json();
      // Translate cluster labels if a language map is provided by the page.
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
    return [
      {
        selector: 'node',
        style: {
          'background-color': ele => getDomainColor(getPrimaryDomain(ele)),
          'label': 'data(name)',
          'font-size': NODE_FONT_SIZE,
          'color': 'var(--color-text)',
          'text-valign': 'bottom',
          'text-halign': 'center',
          'text-margin-y': 4,
          'text-wrap': 'wrap',
          'text-max-width': 100,
          'text-background-color': 'var(--color-bg)',
          'text-background-opacity': 0.85,
          'text-background-shape': 'roundrectangle',
          'text-background-padding': 2,
        },
      },
      {
        selector: 'node[isCluster]',
        style: {
          'width': ele => Math.min(80, 30 + Math.sqrt(ele.data('count')) * CLUSTER_SIZE_SCALE),
          'height': ele => Math.min(80, 30 + Math.sqrt(ele.data('count')) * CLUSTER_SIZE_SCALE),
          'font-size': CLUSTER_FONT_SIZE,
          'font-weight': 'bold',
          'text-valign': 'center',
          'text-halign': 'center',
          'text-margin-y': 0,
          'border-width': 3,
          'border-color': 'var(--color-border)',
          'background-opacity': 0.9,
        },
      },
      {
        selector: 'node[!isCluster]',
        style: {
          'width': NODE_SIZE,
          'height': NODE_SIZE,
        },
      },
      {
        selector: 'edge',
        style: {
          'width': 1.2,
          'line-color': 'var(--color-border)',
          'target-arrow-color': 'var(--color-border)',
          'target-arrow-shape': 'triangle',
          'curve-style': 'bezier',
          'arrow-scale': 0.7,
        },
      },
      {
        selector: 'edge[isClusterEdge]',
        style: {
          'width': ele => Math.min(8, 1 + Math.log(ele.data('weight') || 1) * 1.5),
          'line-color': '#94a3b8',
          'target-arrow-color': '#94a3b8',
        },
      },
      {
        selector: ':selected',
        style: {
          'border-width': 4,
          'border-color': 'var(--color-accent)',
          'border-opacity': 1,
        },
      },
      {
        selector: '.highlighted',
        style: {
          'border-width': 4,
          'border-color': 'var(--color-accent)',
        },
      },
      {
        selector: '.dimmed',
        style: {
          'opacity': 0.15,
        },
      },
    ];
  }

  function runLayout(name) {
    if (!cy) return;
    const opts = { animate: true, animationDuration: 600, padding: 24, fit: true };
    let layout;
    if (name === 'cose') {
      layout = cy.layout({
        name: 'cose',
        ...opts,
        nodeRepulsion: 5000,
        idealEdgeLength: 100,
        componentSpacing: 80,
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
      minZoom: 0.1,
      maxZoom: 4,
      wheelSensitivity: 0.25,
    });

    // Interactions
    cy.on('tap', 'node[isCluster]', evt => {
      const clusterId = evt.target.id();
      showClusterMembers(clusterId);
    });

    cy.on('tap', 'node[!isCluster]', evt => {
      const id = evt.target.id();
      window.location.href = basePath + '/entry/' + id + '/';
    });

    cy.on('mouseover', 'node', evt => {
      evt.target.addClass('highlighted');
    });

    cy.on('mouseout', 'node', evt => {
      evt.target.removeClass('highlighted');
    });

    runLayout('cose');
  }

  function showClusterMembers(clusterId) {
    const cluster = clusterData.nodes.find(n => n.data.id === clusterId);
    if (!cluster) return;
    const members = new Set(cluster.data.members || []);

    // Filter full graph to only cluster members + their relationships
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
      minZoom: 0.2,
      maxZoom: 4,
      wheelSensitivity: 0.25,
    });

    cy.on('tap', 'node', evt => {
      window.location.href = basePath + '/entry/' + evt.target.id() + '/';
    });

    runLayout('cose');

    // Show breadcrumb/title
    const titleEl = document.getElementById('graph-current-view');
    if (titleEl) {
      titleEl.textContent = `${cluster.data.name}（${cluster.data.count}）`;
      titleEl.classList.remove('hidden');
    }
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
      cy.layout({ name: 'cose', padding: 20, nodeRepulsion: 4000, idealEdgeLength: 70, animate: true }).run();
      setTimeout(() => {
        const centerNode = cy.getElementById(centerId);
        if (centerNode.length) {
          centerNode.style({ 'width': 30, 'height': 30 });
          cy.fit(centerNode.closedNeighborhood(), 60);
        }
      }, 650);
    });
  }

  // Full graph page
  const fullGraph = document.getElementById('full-graph');
  if (fullGraph && typeof cytoscape !== 'undefined') {
    loadData().then(() => {
      initGraph(fullGraph, 'clusters');

      // View toggles
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

      // Fit / reset
      document.getElementById('fit-graph')?.addEventListener('click', () => cy && cy.fit());
      document.getElementById('reset-graph')?.addEventListener('click', () => {
        initGraph(fullGraph, 'clusters');
        updateActiveButton('view-clusters');
      });

      // Graph search
      const graphSearch = document.getElementById('graph-search');
      const graphSearchResults = document.getElementById('graph-search-results');
      if (graphSearch) {
        let searchData = { entries: [] };
        fetch('/data/search-index.json')
          .then(r => r.json())
          .then(d => { searchData = d; })
          .catch(() => {});

        graphSearch.addEventListener('input', () => {
          const q = graphSearch.value.trim().toLowerCase();
          if (!q || !graphSearchResults) return;
          const matches = searchData.entries
            .filter(e => (e.name || '').toLowerCase().includes(q) || e.id.toLowerCase().includes(q))
            .slice(0, 10);
          graphSearchResults.innerHTML = matches.map(e =>
            `<div class="graph-search-result" data-id="${e.id}">${e.name}</div>`
          ).join('');
          graphSearchResults.querySelectorAll('.graph-search-result').forEach(el => {
            el.addEventListener('click', () => {
              const id = el.dataset.id;
              if (currentMode === 'clusters') {
                // Find which cluster contains this entity and expand it
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
            });
          });
        });
      }
    });
  }

  function updateActiveButton(id) {
    document.querySelectorAll('.graph-view-btn').forEach(btn => btn.classList.remove('active'));
    document.getElementById(id)?.classList.add('active');
  }
})();
