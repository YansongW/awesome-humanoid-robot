---
$id: ent_paper_occluding_the_solution_space_p_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Occluding the Solution Space: Planner-Agnostic Adversarial Attacks on Tolerance-Aware
    Manipulation'
  zh: 'Occluding the Solution Space: Planner-Agnostic Adversarial Attacks on Tolerance-Aware
    Manipulation'
  ko: ''
summary:
  en: "arXiv:2607.03758v1 Announce Type: new \nAbstract: Adversarial attacks on motion\
    \ planning are crucial for evaluating and quantifying the intrinsic robustness\
    \ of robotic manipulation. However, existing approaches are typically limited\
    \ by restrictive exact-pose objectives and their reliance on planner-in-the-loop\
    \ queries. To address these limitations, we propose a planner-agnostic attack\
    \ framework for tolerance-aware manipulation. Our approach shifts the evaluation\
    \ paradigm to task-level feasibility over goal regions, efficiently inserting\
    \ adversarial obstacles without requiring oracle access to the victim system.\
    \ Offline, we characterize the robot's intrinsic workspace capabilities via a\
    \ kinematic occupancy heatmap, which encodes the density of feasible trajectories\
    \ and robustness priors without invoking a specific planner. Online, we formulate\
    \ the attack as a budgeted maximum-coverage optimization, strategically deploying\
    \ obstacles subject to explicit geometric constraints to occlude the solution\
    \ space. Extensive experiments across simulation and real-world scenarios demonstrate\
    \ that our method reliably induces planning failures, significantly outperforming\
    \ planner-in-the-loop baselines in both computational efficiency and attack efficacy."
  zh: "arXiv:2607.03758v1 Announce Type: new \nAbstract: Adversarial attacks on motion\
    \ planning are crucial for evaluating and quantifying the intrinsic robustness\
    \ of robotic manipulation. However, existing approaches are typically limited\
    \ by restrictive exact-pose objectives and their reliance on planner-in-the-loop\
    \ queries. To address these limitations, we propose a planner-agnostic attack\
    \ framework for tolerance-aware manipulation. Our approach shifts the evaluation\
    \ paradigm to task-level feasibility over goal regions, efficiently inserting\
    \ adversarial obstacles without requiring oracle access to the victim system.\
    \ Offline, we characterize the robot's intrinsic workspace capabilities via a\
    \ kinematic occupancy heatmap, which encodes the density of feasible trajectories\
    \ and robustness priors without invoking a specific planner. Online, we formulate\
    \ the attack as a budgeted maximum-coverage optimization, strategically deploying\
    \ obstacles subject to explicit geometric constraints to occlude the solution\
    \ space. Extensive experiments across simulation and real-world scenarios demonstrate\
    \ that our method reliably induces planning failures, significantly outperforming\
    \ planner-in-the-loop baselines in both computational efficiency and attack efficacy."
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
- occluding_the_solution_space
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'Occluding the Solution Space: Planner-Agnostic Adversarial Attacks on Tolerance-Aware
    Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.03758
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2607.03758v1 Announce Type: new 
Abstract: Adversarial attacks on motion planning are crucial for evaluating and quantifying the intrinsic robustness of robotic manipulation. However, existing approaches are typically limited by restrictive exact-pose objectives and their reliance on planner-in-the-loop queries. To address these limitations, we propose a planner-agnostic attack framework for tolerance-aware manipulation. Our approach shifts the evaluation paradigm to task-level feasibility over goal regions, efficiently inserting adversarial obstacles without requiring oracle access to the victim system. Offline, we characterize the robot's intrinsic workspace capabilities via a kinematic occupancy heatmap, which encodes the density of feasible trajectories and robustness priors without invoking a specific planner. Online, we formulate the attack as a budgeted maximum-coverage optimization, strategically deploying obstacles subject to explicit geometric constraints to occlude the solution space. Extensive experiments across simulation and real-world scenarios demonstrate that our method reliably induces planning failures, significantly outperforming planner-in-the-loop baselines in both computational efficiency and attack efficacy.
