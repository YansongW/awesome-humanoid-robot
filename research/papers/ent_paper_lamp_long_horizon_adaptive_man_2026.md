---
$id: ent_paper_lamp_long_horizon_adaptive_man_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LAMP: Long-Horizon Adaptive Manipulation Planning for Multi-Robot Collaboration
    in Cluttered Space'
  zh: 'LAMP: Long-Horizon Adaptive Manipulation Planning for Multi-Robot Collaboration
    in Cluttered Space'
  ko: ''
summary:
  en: "arXiv:2606.29358v2 Announce Type: replace \nAbstract: Multi-robot manipulation\
    \ requires jointly reasoning about contact formations, robot motions under coupled\
    \ dynamics, and collision avoidance. Systematically searching over this large\
    \ space is difficult and becomes increasingly intractable as the number of robots\
    \ grows, the task horizon lengthens, or the scene becomes more densely cluttered.\
    \ Existing approaches therefore either learn to solve the problem end-to-end via\
    \ reinforcement learning or restrict planning to a simpler surrogate problem,\
    \ such as planning object motions while learning short-horizon contact primitives.\
    \ However, neither paradigm scales to the problem instances we target: long-horizon\
    \ multi-robot manipulation in extremely dense environments. In this paper, we\
    \ propose Long-horizon Adaptive Manipulation Planning (LAMP), a framework combining\
    \ a generative model for manipulation with classical planning for long-horizon\
    \ reasoning. We instantiate our framework with two algorithms leveraging insights\
    \ from established planning techniques, A* and lazy search: LAMP-A*, which systematically\
    \ searches over the coupled object-robot space, and LAMP-Lazy, a lazy planner\
    \ that enables real-time replanning through deferred evaluation. Experiments in\
    \ challenging simulated environments demonstrate that our approach solves complex\
    \ long-horizon tasks in highly cluttered environments that prior methods cannot\
    \ handle."
  zh: "arXiv:2606.29358v2 Announce Type: replace \nAbstract: Multi-robot manipulation\
    \ requires jointly reasoning about contact formations, robot motions under coupled\
    \ dynamics, and collision avoidance. Systematically searching over this large\
    \ space is difficult and becomes increasingly intractable as the number of robots\
    \ grows, the task horizon lengthens, or the scene becomes more densely cluttered.\
    \ Existing approaches therefore either learn to solve the problem end-to-end via\
    \ reinforcement learning or restrict planning to a simpler surrogate problem,\
    \ such as planning object motions while learning short-horizon contact primitives.\
    \ However, neither paradigm scales to the problem instances we target: long-horizon\
    \ multi-robot manipulation in extremely dense environments. In this paper, we\
    \ propose Long-horizon Adaptive Manipulation Planning (LAMP), a framework combining\
    \ a generative model for manipulation with classical planning for long-horizon\
    \ reasoning. We instantiate our framework with two algorithms leveraging insights\
    \ from established planning techniques, A* and lazy search: LAMP-A*, which systematically\
    \ searches over the coupled object-robot space, and LAMP-Lazy, a lazy planner\
    \ that enables real-time replanning through deferred evaluation. Experiments in\
    \ challenging simulated environments demonstrate that our approach solves complex\
    \ long-horizon tasks in highly cluttered environments that prior methods cannot\
    \ handle."
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
- lamp
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-10'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'LAMP: Long-Horizon Adaptive Manipulation Planning for Multi-Robot Collaboration
    in Cluttered Space (arXiv)'
  url: https://arxiv.org/abs/2606.29358
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2606.29358v2 Announce Type: replace 
Abstract: Multi-robot manipulation requires jointly reasoning about contact formations, robot motions under coupled dynamics, and collision avoidance. Systematically searching over this large space is difficult and becomes increasingly intractable as the number of robots grows, the task horizon lengthens, or the scene becomes more densely cluttered. Existing approaches therefore either learn to solve the problem end-to-end via reinforcement learning or restrict planning to a simpler surrogate problem, such as planning object motions while learning short-horizon contact primitives. However, neither paradigm scales to the problem instances we target: long-horizon multi-robot manipulation in extremely dense environments. In this paper, we propose Long-horizon Adaptive Manipulation Planning (LAMP), a framework combining a generative model for manipulation with classical planning for long-horizon reasoning. We instantiate our framework with two algorithms leveraging insights from established planning techniques, A* and lazy search: LAMP-A*, which systematically searches over the coupled object-robot space, and LAMP-Lazy, a lazy planner that enables real-time replanning through deferred evaluation. Experiments in challenging simulated environments demonstrate that our approach solves complex long-horizon tasks in highly cluttered environments that prior methods cannot handle.
