---
$id: ent_paper_physv2a_reachability_gated_and_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhysV2A: Reachability-Gated and Semantic-Mask-Constrained Feasibility Completion
    for Video-to-Robot Manipulation'
  zh: 'PhysV2A: Reachability-Gated and Semantic-Mask-Constrained Feasibility Completion
    for Video-to-Robot Manipulation'
  ko: 'PhysV2A: Reachability-Gated and Semantic-Mask-Constrained Feasibility Completion
    for Video-to-Robot Manipulation'
summary:
  en: "arXiv:2607.09365v1 Announce Type: new \nAbstract: Video-based manipulation\
    \ provides object-centric motion priors from human demonstrations, generated videos,\
    \ or RGB-D observations, but such priors are typically embodiment-agnostic and\
    \ cannot be directly executed by a specific robot. This paper presents \\textbf{PhysV2A},\
    \ a reachability-gated and semantic-mask-constrained feasibility-completion framework\
    \ for converting video-derived 6D object motion into robot-executable manipulation\
    \ trajectories. The key idea is to treat grasp feasibility as trajectory-conditioned\
    \ rather than local: each RGB-D-generated 6-DoF grasp candidate is rigidly coupled\
    \ with the recovered object motion to form a grasp-conditioned TCP trajectory\
    \ hypothesis. PhysV2A then performs hierarchical reachability-gated selection,\
    \ where infeasible grasp--trajectory pairs are rejected by robot-centric kinematic\
    \ checks and surviving candidates are ranked by downstream execution suitability.\
    \ For the selected reachable trajectory, a VLM-assisted and rule-validated S-Mask\
    \ identifies task-critical and relaxable Cartesian components, enabling semantic-mask-constrained\
    \ manipulability refinement through redundancy-first optimization and bounded\
    \ Cartesian relaxation. Real-robot experiments on four tabletop manipulation tasks\
    \ show that PhysV2A improves task success over representative video-prior and\
    \ IK-only baselines, reduces kinematic-feasibility failures, and produces better-conditioned\
    \ trajectories with bounded semantic deviations."
  zh: "arXiv:2607.09365v1 Announce Type: new \nAbstract: Video-based manipulation\
    \ provides object-centric motion priors from human demonstrations, generated videos,\
    \ or RGB-D observations, but such priors are typically embodiment-agnostic and\
    \ cannot be directly executed by a specific robot. This paper presents \\textbf{PhysV2A},\
    \ a reachability-gated and semantic-mask-constrained feasibility-completion framework\
    \ for converting video-derived 6D object motion into robot-executable manipulation\
    \ trajectories. The key idea is to treat grasp feasibility as trajectory-conditioned\
    \ rather than local: each RGB-D-generated 6-DoF grasp candidate is rigidly coupled\
    \ with the recovered object motion to form a grasp-conditioned TCP trajectory\
    \ hypothesis. PhysV2A then performs hierarchical reachability-gated selection,\
    \ where infeasible grasp--trajectory pairs are rejected by robot-centric kinematic\
    \ checks and surviving candidates are ranked by downstream execution suitability.\
    \ For the selected reachable trajectory, a VLM-assisted and rule-validated S-Mask\
    \ identifies task-critical and relaxable Cartesian components, enabling semantic-mask-constrained\
    \ manipulability refinement through redundancy-first optimization and bounded\
    \ Cartesian relaxation. Real-robot experiments on four tabletop manipulation tasks\
    \ show that PhysV2A improves task success over representative video-prior and\
    \ IK-only baselines, reduces kinematic-feasibility failures, and produces better-conditioned\
    \ trajectories with bounded semantic deviations."
  ko: "arXiv:2607.09365v1 Announce Type: new \nAbstract: Video-based manipulation\
    \ provides object-centric motion priors from human demonstrations, generated videos,\
    \ or RGB-D observations, but such priors are typically embodiment-agnostic and\
    \ cannot be directly executed by a specific robot. This paper presents \\textbf{PhysV2A},\
    \ a reachability-gated and semantic-mask-constrained feasibility-completion framework\
    \ for converting video-derived 6D object motion into robot-executable manipulation\
    \ trajectories. The key idea is to treat grasp feasibility as trajectory-conditioned\
    \ rather than local: each RGB-D-generated 6-DoF grasp candidate is rigidly coupled\
    \ with the recovered object motion to form a grasp-conditioned TCP trajectory\
    \ hypothesis. PhysV2A then performs hierarchical reachability-gated selection,\
    \ where infeasible grasp--trajectory pairs are rejected by robot-centric kinematic\
    \ checks and surviving candidates are ranked by downstream execution suitability.\
    \ For the selected reachable trajectory, a VLM-assisted and rule-validated S-Mask\
    \ identifies task-critical and relaxable Cartesian components, enabling semantic-mask-constrained\
    \ manipulability refinement through redundancy-first optimization and bounded\
    \ Cartesian relaxation. Real-robot experiments on four tabletop manipulation tasks\
    \ show that PhysV2A improves task success over representative video-prior and\
    \ IK-only baselines, reduces kinematic-feasibility failures, and produces better-conditioned\
    \ trajectories with bounded semantic deviations."
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
- physv2a
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
  title: 'PhysV2A: Reachability-Gated and Semantic-Mask-Constrained Feasibility Completion
    for Video-to-Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.09365
  date: '2026'
  accessed_at: '2026-07-14'
---

## 概述
arXiv:2607.09365v1 Announce Type: new 
Abstract: Video-based manipulation provides object-centric motion priors from human demonstrations, generated videos, or RGB-D observations, but such priors are typically embodiment-agnostic and cannot be directly executed by a specific robot. This paper presents \textbf{PhysV2A}, a reachability-gated and semantic-mask-constrained feasibility-completion framework for converting video-derived 6D object motion into robot-executable manipulation trajectories. The key idea is to treat grasp feasibility as trajectory-conditioned rather than local: each RGB-D-generated 6-DoF grasp candidate is rigidly coupled with the recovered object motion to form a grasp-conditioned TCP trajectory hypothesis. PhysV2A then performs hierarchical reachability-gated selection, where infeasible grasp--trajectory pairs are rejected by robot-centric kinematic checks and surviving candidates are ranked by downstream execution suitability. For the selected reachable trajectory, a VLM-assisted and rule-validated S-Mask identifies task-critical and relaxable Cartesian components, enabling semantic-mask-constrained manipulability refinement through redundancy-first optimization and bounded Cartesian relaxation. Real-robot experiments on four tabletop manipulation tasks show that PhysV2A improves task success over representative video-prior and IK-only baselines, reduces kinematic-feasibility failures, and produces better-conditioned trajectories with bounded semantic deviations.

## Overview
arXiv:2607.09365v1 Announce Type: new 
Abstract: Video-based manipulation provides object-centric motion priors from human demonstrations, generated videos, or RGB-D observations, but such priors are typically embodiment-agnostic and cannot be directly executed by a specific robot. This paper presents \textbf{PhysV2A}, a reachability-gated and semantic-mask-constrained feasibility-completion framework for converting video-derived 6D object motion into robot-executable manipulation trajectories. The key idea is to treat grasp feasibility as trajectory-conditioned rather than local: each RGB-D-generated 6-DoF grasp candidate is rigidly coupled with the recovered object motion to form a grasp-conditioned TCP trajectory hypothesis. PhysV2A then performs hierarchical reachability-gated selection, where infeasible grasp--trajectory pairs are rejected by robot-centric kinematic checks and surviving candidates are ranked by downstream execution suitability. For the selected reachable trajectory, a VLM-assisted and rule-validated S-Mask identifies task-critical and relaxable Cartesian components, enabling semantic-mask-constrained manipulability refinement through redundancy-first optimization and bounded Cartesian relaxation. Real-robot experiments on four tabletop manipulation tasks show that PhysV2A improves task success over representative video-prior and IK-only baselines, reduces kinematic-feasibility failures, and produces better-conditioned trajectories with bounded semantic deviations.

## 개요
arXiv:2607.09365v1 Announce Type: new 
Abstract: Video-based manipulation provides object-centric motion priors from human demonstrations, generated videos, or RGB-D observations, but such priors are typically embodiment-agnostic and cannot be directly executed by a specific robot. This paper presents \textbf{PhysV2A}, a reachability-gated and semantic-mask-constrained feasibility-completion framework for converting video-derived 6D object motion into robot-executable manipulation trajectories. The key idea is to treat grasp feasibility as trajectory-conditioned rather than local: each RGB-D-generated 6-DoF grasp candidate is rigidly coupled with the recovered object motion to form a grasp-conditioned TCP trajectory hypothesis. PhysV2A then performs hierarchical reachability-gated selection, where infeasible grasp--trajectory pairs are rejected by robot-centric kinematic checks and surviving candidates are ranked by downstream execution suitability. For the selected reachable trajectory, a VLM-assisted and rule-validated S-Mask identifies task-critical and relaxable Cartesian components, enabling semantic-mask-constrained manipulability refinement through redundancy-first optimization and bounded Cartesian relaxation. Real-robot experiments on four tabletop manipulation tasks show that PhysV2A improves task success over representative video-prior and IK-only baselines, reduces kinematic-feasibility failures, and produces better-conditioned trajectories with bounded semantic deviations.
