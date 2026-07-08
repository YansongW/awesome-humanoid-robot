---
$id: ent_paper_ldhp_library_driven_hierarchic_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LDHP: Library-Driven Hierarchical Planning for Non-prehensile Dexterous Manipulation'
  zh: 'LDHP: Library-Driven Hierarchical Planning for Non-prehensile Dexterous Manipulation'
  ko: ''
summary:
  en: "arXiv:2603.13844v2 Announce Type: replace \nAbstract: Non-prehensile manipulation\
    \ is essential for handling thin, large, or otherwise ungraspable objects in unstructured\
    \ settings. Prior planning and search-based methods often rely on ad-hoc manual\
    \ designs or generate physically unrealizable motions by ignoring critical gripper\
    \ properties, while training-based approaches are data-intensive and struggle\
    \ to generalize to novel, out-of-distribution tasks. We propose a library-driven\
    \ hierarchical planner (LDHP) that makes executability a first-class design goal:\
    \ a top-tier contact-state planner proposes object-pose paths using MoveObject\
    \ primitives, and a bottom-tier grasp planner synthesizes feasible grasp sequences\
    \ with AdjustGrasp primitives; feasibility is certified by collision checks and\
    \ quasi-static mechanics, and contact-sensitive segments are recovered via a bounded\
    \ dichotomy refinement. This gripper-aware decomposition decouples object motion\
    \ from grasp realizability, yields a task-agnostic pipeline that transfers across\
    \ manipulation tasks and geometric variations without re-design, and exposes clean\
    \ hooks for optional learned priors. Real-robot studies on zero-mobility lifting\
    \ and slot insertion demonstrate consistent execution and robustness to shape\
    \ and environment changes."
  zh: "arXiv:2603.13844v2 Announce Type: replace \nAbstract: Non-prehensile manipulation\
    \ is essential for handling thin, large, or otherwise ungraspable objects in unstructured\
    \ settings. Prior planning and search-based methods often rely on ad-hoc manual\
    \ designs or generate physically unrealizable motions by ignoring critical gripper\
    \ properties, while training-based approaches are data-intensive and struggle\
    \ to generalize to novel, out-of-distribution tasks. We propose a library-driven\
    \ hierarchical planner (LDHP) that makes executability a first-class design goal:\
    \ a top-tier contact-state planner proposes object-pose paths using MoveObject\
    \ primitives, and a bottom-tier grasp planner synthesizes feasible grasp sequences\
    \ with AdjustGrasp primitives; feasibility is certified by collision checks and\
    \ quasi-static mechanics, and contact-sensitive segments are recovered via a bounded\
    \ dichotomy refinement. This gripper-aware decomposition decouples object motion\
    \ from grasp realizability, yields a task-agnostic pipeline that transfers across\
    \ manipulation tasks and geometric variations without re-design, and exposes clean\
    \ hooks for optional learned priors. Real-robot studies on zero-mobility lifting\
    \ and slot insertion demonstrate consistent execution and robustness to shape\
    \ and environment changes."
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
- ldhp
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
  title: 'LDHP: Library-Driven Hierarchical Planning for Non-prehensile Dexterous
    Manipulation'
  url: https://arxiv.org/abs/2603.13844
  date: '2026'
  accessed_at: '2026-07-01'
---

arXiv:2603.13844v2 Announce Type: replace 
Abstract: Non-prehensile manipulation is essential for handling thin, large, or otherwise ungraspable objects in unstructured settings. Prior planning and search-based methods often rely on ad-hoc manual designs or generate physically unrealizable motions by ignoring critical gripper properties, while training-based approaches are data-intensive and struggle to generalize to novel, out-of-distribution tasks. We propose a library-driven hierarchical planner (LDHP) that makes executability a first-class design goal: a top-tier contact-state planner proposes object-pose paths using MoveObject primitives, and a bottom-tier grasp planner synthesizes feasible grasp sequences with AdjustGrasp primitives; feasibility is certified by collision checks and quasi-static mechanics, and contact-sensitive segments are recovered via a bounded dichotomy refinement. This gripper-aware decomposition decouples object motion from grasp realizability, yields a task-agnostic pipeline that transfers across manipulation tasks and geometric variations without re-design, and exposes clean hooks for optional learned priors. Real-robot studies on zero-mobility lifting and slot insertion demonstrate consistent execution and robustness to shape and environment changes.
