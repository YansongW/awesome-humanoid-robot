---
$id: ent_paper_greedy_heuristics_for_sampling_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Greedy Heuristics for Sampling-Based Motion Planning in High-Dimensional State
    Spaces
  zh: Greedy Heuristics for Sampling-Based Motion Planning in High-Dimensional State
    Spaces
  ko: ''
summary:
  en: "arXiv:2405.03411v4 Announce Type: replace \nAbstract: Informed sampling techniques\
    \ accelerate the convergence of sampling-based motion planners by biasing sampling\
    \ toward regions of the state space that are most likely to yield better solutions.\
    \ However, when the current solution path contains redundant or tortuous segments,\
    \ the resulting informed subset may remain unnecessarily large, slowing convergence.\
    \ Our prior work addressed this issue by introducing the greedy informed set,\
    \ which reduces the sampling region based on the maximum heuristic cost along\
    \ the current solution path. In this article, we formally characterize the behavior\
    \ of the greedy informed set within Rapidly-exploring Random Tree (RRT*)-like\
    \ planners and analyze how greedy sampling affects exploration and asymptotic\
    \ optimality. We then present Greedy RRT* (G-RRT*), a bi-directional anytime variant\
    \ of RRT* that leverages the greedy informed set to focus sampling in the most\
    \ promising regions of the search space. Experiments on abstract planning benchmarks,\
    \ manipulation tasks from the MotionBenchMaker dataset, and a dual-arm Barrett\
    \ WAM problem demonstrate that G-RRT* rapidly finds initial solutions and converges\
    \ asymptotically to optimal paths, outperforming state-of-the-art sampling-based\
    \ planners."
  zh: "arXiv:2405.03411v4 Announce Type: replace \nAbstract: Informed sampling techniques\
    \ accelerate the convergence of sampling-based motion planners by biasing sampling\
    \ toward regions of the state space that are most likely to yield better solutions.\
    \ However, when the current solution path contains redundant or tortuous segments,\
    \ the resulting informed subset may remain unnecessarily large, slowing convergence.\
    \ Our prior work addressed this issue by introducing the greedy informed set,\
    \ which reduces the sampling region based on the maximum heuristic cost along\
    \ the current solution path. In this article, we formally characterize the behavior\
    \ of the greedy informed set within Rapidly-exploring Random Tree (RRT*)-like\
    \ planners and analyze how greedy sampling affects exploration and asymptotic\
    \ optimality. We then present Greedy RRT* (G-RRT*), a bi-directional anytime variant\
    \ of RRT* that leverages the greedy informed set to focus sampling in the most\
    \ promising regions of the search space. Experiments on abstract planning benchmarks,\
    \ manipulation tasks from the MotionBenchMaker dataset, and a dual-arm Barrett\
    \ WAM problem demonstrate that G-RRT* rapidly finds initial solutions and converges\
    \ asymptotically to optimal paths, outperforming state-of-the-art sampling-based\
    \ planners."
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
- greedy_heuristics_for_sampling
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: Greedy Heuristics for Sampling-Based Motion Planning in High-Dimensional
    State Spaces (arXiv)
  url: https://arxiv.org/abs/2405.03411
  date: '2026'
  accessed_at: '2026-07-14'
---

arXiv:2405.03411v4 Announce Type: replace 
Abstract: Informed sampling techniques accelerate the convergence of sampling-based motion planners by biasing sampling toward regions of the state space that are most likely to yield better solutions. However, when the current solution path contains redundant or tortuous segments, the resulting informed subset may remain unnecessarily large, slowing convergence. Our prior work addressed this issue by introducing the greedy informed set, which reduces the sampling region based on the maximum heuristic cost along the current solution path. In this article, we formally characterize the behavior of the greedy informed set within Rapidly-exploring Random Tree (RRT*)-like planners and analyze how greedy sampling affects exploration and asymptotic optimality. We then present Greedy RRT* (G-RRT*), a bi-directional anytime variant of RRT* that leverages the greedy informed set to focus sampling in the most promising regions of the search space. Experiments on abstract planning benchmarks, manipulation tasks from the MotionBenchMaker dataset, and a dual-arm Barrett WAM problem demonstrate that G-RRT* rapidly finds initial solutions and converges asymptotically to optimal paths, outperforming state-of-the-art sampling-based planners.
