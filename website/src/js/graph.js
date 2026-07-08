/* Cytoscape.js graph visualization for the knowledge graph */

(function () {
  'use strict';

  const COLORS = {
    company: '#3498db',
    component_manufacturer: '#2ecc71',
    tier1_supplier: '#2ecc71',
    oem: '#3498db',
    component: '#2ecc71',
    technology: '#e74c3c',
    method: '#e74c3c',
    paper: '#9b59b6',
    dataset: '#9b59b6',
    benchmark: '#f39c12',
    report: '#f39c12',
    material: '#1abc9c',
    foundation: '#95a5a6',
    default: '#64748b',
  };

  const TYPE_MAP = {
    'component_manufacturer': 'company',
    'tier1_supplier': 'company',
    'oem': 'company',
    'robot_system': 'oem',
  };

  function getColor(type) {
    const mapped = TYPE_MAP[type] || type;
    return COLORS[mapped] || COLORS.default;
  }

  async function loadGraphData() {
    try {
      const res = await fetch('/data/relations.json');
      if (!res.ok) throw new Error('Failed to load graph data');
      return await res.json();
    } catch (err) {
      console.error(err);
      return { nodes: [], edges: [] };
    }
  }

  function initGraph(container, options) {
    const { centerId, filterDomains } = options || {};

    loadGraphData().then(data => {
      let nodes = data.nodes || [];
      let edges = data.edges || [];

      if (centerId) {
        const relatedEdgeIds = new Set();
        const relatedNodeIds = new Set([centerId]);
        for (const edge of edges) {
          if (edge.data.source === centerId || edge.data.target === centerId) {
            relatedEdgeIds.add(edge.data.id);
            relatedNodeIds.add(edge.data.source);
            relatedNodeIds.add(edge.data.target);
          }
        }
        nodes = nodes.filter(n => relatedNodeIds.has(n.data.id));
        edges = edges.filter(e => relatedEdgeIds.has(e.data.id));
      }

      if (filterDomains && filterDomains.length > 0 && !filterDomains.includes('all')) {
        const allowedIds = new Set(
          nodes
            .filter(n => n.data.domains && n.data.domains.some(d => filterDomains.includes(d)))
            .map(n => n.data.id)
        );
        nodes = nodes.filter(n => allowedIds.has(n.data.id));
        edges = edges.filter(e => allowedIds.has(e.data.source) && allowedIds.has(e.data.target));
      }

      if (nodes.length === 0) {
        container.innerHTML = '<div class="empty-state">没有可显示的关系数据。</div>';
        return;
      }

      const cy = cytoscape({
        container: container,
        elements: [...nodes, ...edges],
        style: [
          {
            selector: 'node',
            style: {
              'background-color': ele => getColor(ele.data('type')),
              'label': ele => {
                const name = ele.data('name') || ele.data('id');
                return name.length > 18 ? name.slice(0, 16) + '…' : name;
              },
              'width': 24,
              'height': 24,
              'font-size': 10,
              'color': 'var(--color-text)',
              'text-valign': 'bottom',
              'text-halign': 'center',
              'text-margin-y': 4,
              'text-wrap': 'wrap',
              'text-max-width': 90,
            },
          },
          {
            selector: 'edge',
            style: {
              'width': 1.5,
              'line-color': 'var(--color-border)',
              'target-arrow-color': 'var(--color-border)',
              'target-arrow-shape': 'triangle',
              'curve-style': 'bezier',
              'arrow-scale': 0.8,
            },
          },
          {
            selector: ':selected',
            style: {
              'border-width': 3,
              'border-color': 'var(--color-accent)',
              'border-opacity': 1,
            },
          },
        ],
        layout: {
          name: 'cose',
          padding: 20,
          nodeRepulsion: 8000,
          idealEdgeLength: 80,
          animate: true,
          animationDuration: 500,
          fit: true,
        },
        minZoom: 0.2,
        maxZoom: 3,
        wheelSensitivity: 0.3,
      });

      cy.on('tap', 'node', evt => {
        const id = evt.target.id();
        window.location.href = '/entry/' + id + '/';
      });

      cy.on('mouseover', 'node', evt => {
        evt.target.animate({
          style: { 'width': 30, 'height': 30 },
        }, { duration: 150 });
      });

      cy.on('mouseout', 'node', evt => {
        evt.target.animate({
          style: { 'width': 24, 'height': 24 },
        }, { duration: 150 });
      });

      if (centerId) {
        const centerNode = cy.getElementById(centerId);
        if (centerNode.length) {
          centerNode.style({ 'width': 36, 'height': 36 });
          setTimeout(() => cy.fit(centerNode.closedNeighborhood(), 60), 600);
        }
      }

      window._cy = cy;
    });
  }

  // Entry page subgraph
  const entryGraph = document.getElementById('entry-graph');
  if (entryGraph && typeof cytoscape !== 'undefined') {
    const centerId = entryGraph.dataset.centerId;
    initGraph(entryGraph, { centerId });
  }

  // Full graph page
  const fullGraph = document.getElementById('full-graph');
  if (fullGraph && typeof cytoscape !== 'undefined') {
    initGraph(fullGraph, {});

    // Domain filters
    const domainFilters = document.querySelectorAll('#domain-filters input[type="checkbox"]');
    domainFilters.forEach(cb => {
      cb.addEventListener('change', () => {
        const allCb = document.querySelector('#domain-filters input[value="all"]');
        let selected;
        if (cb.value === 'all' && cb.checked) {
          domainFilters.forEach(c => { if (c.value !== 'all') c.checked = false; });
          selected = ['all'];
        } else {
          if (allCb) allCb.checked = false;
          selected = Array.from(domainFilters)
            .filter(c => c.checked)
            .map(c => c.value);
          if (selected.length === 0) {
            if (allCb) allCb.checked = true;
            selected = ['all'];
          }
        }
        initGraph(fullGraph, { filterDomains: selected });
      });
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
            if (window._cy) {
              const node = window._cy.getElementById(id);
              if (node.length) {
                window._cy.fit(node, 60);
                node.select();
              }
            }
            graphSearchResults.innerHTML = '';
          });
        });
      });
    }

    // Reset / fit buttons
    const resetBtn = document.getElementById('reset-graph');
    const fitBtn = document.getElementById('fit-graph');
    if (resetBtn) resetBtn.addEventListener('click', () => initGraph(fullGraph, {}));
    if (fitBtn && window._cy) fitBtn.addEventListener('click', () => window._cy.fit());
  }
})();
