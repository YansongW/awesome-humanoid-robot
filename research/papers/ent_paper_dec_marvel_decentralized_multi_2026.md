---
$id: ent_paper_dec_marvel_decentralized_multi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under
    Budget Constraints'
  zh: 'Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under
    Budget Constraints'
  ko: ''
summary:
  en: "arXiv:2607.09060v1 Announce Type: new \nAbstract: Multi-UAV exploration is\
    \ often constrained by unreliable communication, limited field-of-view sensing\
    \ (e.g., lightweight onboard camera), and finite travel budgets that require each\
    \ robot to reserve enough budget to return to its base. We present Dec-MARVEL,\
    \ a decentralized budget-aware exploration framework for communication-free teams\
    \ with directional sensing. Rather than exchanging maps, goals, or messages, each\
    \ robot coordinates through its incidental observations: any teammate trajectory\
    \ within its field of view serves as a coordination signal. A graph-attention\
    \ actor fuses local frontier geometry, teammate motion, and budget features to\
    \ select return-feasible waypoint-heading actions. The actor is trained with phase-conditioned\
    \ critics, a training-only task-oriented privileged critic, and a mixture-based\
    \ budget curriculum. Across 900 held-out trials spanning three team sizes (2,\
    \ 4, 8 robots) and three travel budgets (720, 800, 1024 meters) against four baselines,\
    \ Dec-MARVEL achieves the highest or tied-highest exploration rate and lowest\
    \ sensing overlap across all nine team-size budget configurations. Under our tightest\
    \ 720m budget, it reaches 53%, 94%, and 100% success for 2, 4, and 8 robots, versus\
    \ 37%, 83%, and 99% for the strongest baseline. Physical-robot experiments demonstrate\
    \ successful sim-to-real transfer and real-world deployment of Dec-MARVEL."
  zh: "arXiv:2607.09060v1 Announce Type: new \nAbstract: Multi-UAV exploration is\
    \ often constrained by unreliable communication, limited field-of-view sensing\
    \ (e.g., lightweight onboard camera), and finite travel budgets that require each\
    \ robot to reserve enough budget to return to its base. We present Dec-MARVEL,\
    \ a decentralized budget-aware exploration framework for communication-free teams\
    \ with directional sensing. Rather than exchanging maps, goals, or messages, each\
    \ robot coordinates through its incidental observations: any teammate trajectory\
    \ within its field of view serves as a coordination signal. A graph-attention\
    \ actor fuses local frontier geometry, teammate motion, and budget features to\
    \ select return-feasible waypoint-heading actions. The actor is trained with phase-conditioned\
    \ critics, a training-only task-oriented privileged critic, and a mixture-based\
    \ budget curriculum. Across 900 held-out trials spanning three team sizes (2,\
    \ 4, 8 robots) and three travel budgets (720, 800, 1024 meters) against four baselines,\
    \ Dec-MARVEL achieves the highest or tied-highest exploration rate and lowest\
    \ sensing overlap across all nine team-size budget configurations. Under our tightest\
    \ 720m budget, it reaches 53%, 94%, and 100% success for 2, 4, and 8 robots, versus\
    \ 37%, 83%, and 99% for the strongest baseline. Physical-robot experiments demonstrate\
    \ successful sim-to-real transfer and real-world deployment of Dec-MARVEL."
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
- humanoid
- robotics
- dec_marvel
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-13'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication
    under Budget Constraints (arXiv)'
  url: https://arxiv.org/abs/2607.09060
  date: '2026'
  accessed_at: '2026-07-13'
---

arXiv:2607.09060v1 Announce Type: new 
Abstract: Multi-UAV exploration is often constrained by unreliable communication, limited field-of-view sensing (e.g., lightweight onboard camera), and finite travel budgets that require each robot to reserve enough budget to return to its base. We present Dec-MARVEL, a decentralized budget-aware exploration framework for communication-free teams with directional sensing. Rather than exchanging maps, goals, or messages, each robot coordinates through its incidental observations: any teammate trajectory within its field of view serves as a coordination signal. A graph-attention actor fuses local frontier geometry, teammate motion, and budget features to select return-feasible waypoint-heading actions. The actor is trained with phase-conditioned critics, a training-only task-oriented privileged critic, and a mixture-based budget curriculum. Across 900 held-out trials spanning three team sizes (2, 4, 8 robots) and three travel budgets (720, 800, 1024 meters) against four baselines, Dec-MARVEL achieves the highest or tied-highest exploration rate and lowest sensing overlap across all nine team-size budget configurations. Under our tightest 720m budget, it reaches 53%, 94%, and 100% success for 2, 4, and 8 robots, versus 37%, 83%, and 99% for the strongest baseline. Physical-robot experiments demonstrate successful sim-to-real transfer and real-world deployment of Dec-MARVEL.
