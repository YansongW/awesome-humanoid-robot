---
$id: ent_paper_benchmarking_humanoid_imitatio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Benchmarking Humanoid Imitation Learning with Motion Difficulty
  zh: Benchmarking Humanoid Imitation Learning with Motion Difficulty
  ko: Benchmarking Humanoid Imitation Learning with Motion Difficulty
summary:
  en: Benchmarking Humanoid Imitation Learning with Motion Difficulty is a 2025 work on simulation benchmark for humanoid
    robots.
  zh: Benchmarking Humanoid Imitation Learning with Motion Difficulty is a 2025 work on simulation benchmark for humanoid
    robots.
  ko: Benchmarking Humanoid Imitation Learning with Motion Difficulty is a 2025 work on simulation benchmark for humanoid
    robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- benchmarking_humanoid_imitatio
- humanoid
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.07248v2.
sources:
- id: src_001
  type: paper
  title: Benchmarking Humanoid Imitation Learning with Motion Difficulty (arXiv)
  url: https://arxiv.org/abs/2512.07248
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Physics-based motion imitation is central to humanoid control, yet current evaluation metrics (e.g., MPJPE) only quantify imitation outcomes, not their underlying causes. This conflation obscures a critical diagnostic question: when imitation error occurs, does it stem from policy limitations or the intrinsic learning difficulty of the target motion? To resolve this ambiguity, we propose the Torque Variation Score (TVS), a physics-grounded metric that quantifies the inherent learning difficulty of a motion independently of any policy's performance. TVS measures the magnitude of torque variation required to correct small pose perturbations, directly capturing how dynamical properties shape the reinforcement learning landscape. We establish that high-TV motions induce flat reward landscapes and vanishing policy gradients, explaining persistent imitation failures. Extensive experiments with state-of-the-art methods (UHC, PHC+) confirm TVS strongly correlates with imitation error and enables principled error attribution: high error on low-TV motions indicates policy deficiency, while high error on high-TV motions reflects fundamental learning constraints. Beyond error diagnosis, TVS facilitates three practical applications: Maximum Imitable Difficulty (MID) for policy capability assessment, Difficulty-Stratified Joint Error (DSJE) for granular performance profiling, and Flawed Motion Detection for identifying segments with abnormally high learning difficulty to support mocap data curation and quality control. TVS provides a rigorous lens to distinguish policy-induced errors from motion-inherent challenges and enhances motion dataset reliability.

## 核心内容
Physics-based motion imitation is central to humanoid control, yet current evaluation metrics (e.g., MPJPE) only quantify imitation outcomes, not their underlying causes. This conflation obscures a critical diagnostic question: when imitation error occurs, does it stem from policy limitations or the intrinsic learning difficulty of the target motion? To resolve this ambiguity, we propose the Torque Variation Score (TVS), a physics-grounded metric that quantifies the inherent learning difficulty of a motion independently of any policy's performance. TVS measures the magnitude of torque variation required to correct small pose perturbations, directly capturing how dynamical properties shape the reinforcement learning landscape. We establish that high-TV motions induce flat reward landscapes and vanishing policy gradients, explaining persistent imitation failures. Extensive experiments with state-of-the-art methods (UHC, PHC+) confirm TVS strongly correlates with imitation error and enables principled error attribution: high error on low-TV motions indicates policy deficiency, while high error on high-TV motions reflects fundamental learning constraints. Beyond error diagnosis, TVS facilitates three practical applications: Maximum Imitable Difficulty (MID) for policy capability assessment, Difficulty-Stratified Joint Error (DSJE) for granular performance profiling, and Flawed Motion Detection for identifying segments with abnormally high learning difficulty to support mocap data curation and quality control. TVS provides a rigorous lens to distinguish policy-induced errors from motion-inherent challenges and enhances motion dataset reliability.

## 参考
- http://arxiv.org/abs/2512.07248v2

