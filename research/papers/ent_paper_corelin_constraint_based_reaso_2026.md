---
$id: ent_paper_corelin_constraint_based_reaso_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoReLIN: Constraint-based Reasoning for Zero-shot Lifelong Interactive Navigation'
  zh: 'CoReLIN: Constraint-based Reasoning for Zero-shot Lifelong Interactive Navigation'
  ko: ''
summary:
  en: "arXiv:2602.20055v2 Announce Type: replace \nAbstract: Robot navigation typically\
    \ assumes an obstacle-free path exists between start and goal. In real environments,\
    \ however, clutter may block all routes. We introduce Lifelong Interactive Navigation,\
    \ where a mobile robot with manipulation capabilities must move objects to forge\
    \ paths and complete sequential object-placement tasks. Because environment modifications\
    \ persist, decisions impact future navigability and task difficulty. We propose\
    \ CoReLIN, an LLM-driven constraint-based reasoning framework with active perception.\
    \ CoReLIN reasons over a structured scene graph to decide which objects to relocate,\
    \ where to place them, and where to explore next. A standard motion planner executes\
    \ reliable navigation and manipulation primitives. To evaluate long-horizon behavior,\
    \ we introduce 2 new metrics - Long-term Efficiency Score (LES), a unified metric\
    \ capturing success, execution efficiency, environment optimality, captured by\
    \ Price of Clutter. In ProcTHOR-10k, CoReLIN outperforms best baseline by 16%\
    \ under standard metrics and LES, and transfers to real-world hardware."
  zh: "arXiv:2602.20055v2 Announce Type: replace \nAbstract: Robot navigation typically\
    \ assumes an obstacle-free path exists between start and goal. In real environments,\
    \ however, clutter may block all routes. We introduce Lifelong Interactive Navigation,\
    \ where a mobile robot with manipulation capabilities must move objects to forge\
    \ paths and complete sequential object-placement tasks. Because environment modifications\
    \ persist, decisions impact future navigability and task difficulty. We propose\
    \ CoReLIN, an LLM-driven constraint-based reasoning framework with active perception.\
    \ CoReLIN reasons over a structured scene graph to decide which objects to relocate,\
    \ where to place them, and where to explore next. A standard motion planner executes\
    \ reliable navigation and manipulation primitives. To evaluate long-horizon behavior,\
    \ we introduce 2 new metrics - Long-term Efficiency Score (LES), a unified metric\
    \ capturing success, execution efficiency, environment optimality, captured by\
    \ Price of Clutter. In ProcTHOR-10k, CoReLIN outperforms best baseline by 16%\
    \ under standard metrics and LES, and transfers to real-world hardware."
  ko: ''
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- corelin
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported from arXiv cs.RO RSS feed.
sources:
- id: src_001
  type: paper
  title: 'CoReLIN: Constraint-based Reasoning for Zero-shot Lifelong Interactive Navigation'
  url: https://arxiv.org/abs/2602.20055
  date: '2026'
  accessed_at: '2026-07-01'
---

arXiv:2602.20055v2 Announce Type: replace 
Abstract: Robot navigation typically assumes an obstacle-free path exists between start and goal. In real environments, however, clutter may block all routes. We introduce Lifelong Interactive Navigation, where a mobile robot with manipulation capabilities must move objects to forge paths and complete sequential object-placement tasks. Because environment modifications persist, decisions impact future navigability and task difficulty. We propose CoReLIN, an LLM-driven constraint-based reasoning framework with active perception. CoReLIN reasons over a structured scene graph to decide which objects to relocate, where to place them, and where to explore next. A standard motion planner executes reliable navigation and manipulation primitives. To evaluate long-horizon behavior, we introduce 2 new metrics - Long-term Efficiency Score (LES), a unified metric capturing success, execution efficiency, environment optimality, captured by Price of Clutter. In ProcTHOR-10k, CoReLIN outperforms best baseline by 16% under standard metrics and LES, and transfers to real-world hardware.
