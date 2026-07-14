---
$id: ent_paper_a_hierarchical_framework_for_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs
  zh: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs
  ko: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs
summary:
  en: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs is a 2025 work on locomotion for humanoid
    robots.
  zh: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs is a 2025 work on locomotion for humanoid
    robots.
  ko: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs is a 2025 work on locomotion for humanoid
    robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_hierarchical_framework_for_h
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00077v1.
sources:
- id: src_001
  type: paper
  title: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs (arXiv)
  url: https://arxiv.org/abs/2512.00077
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The integration of Supernumerary Limbs (SLs) on humanoid robots poses a significant stability challenge due to the dynamic perturbations they introduce. This thesis addresses this issue by designing a novel hierarchical control architecture to improve humanoid locomotion stability with SLs. The core of this framework is a decoupled strategy that combines learning-based locomotion with model-based balancing. The low-level component consists of a walking gait for a Unitree H1 humanoid through imitation learning and curriculum learning. The high-level component actively utilizes the SLs for dynamic balancing. The effectiveness of the system is evaluated in a physics-based simulation under three conditions: baseline gait for an unladen humanoid (baseline walking), walking with a static SL payload (static payload), and walking with the active dynamic balancing controller (dynamic balancing). Our evaluation shows that the dynamic balancing controller improves stability. Compared to the static payload condition, the balancing strategy yields a gait pattern closer to the baseline and decreases the Dynamic Time Warping (DTW) distance of the CoM trajectory by 47\%. The balancing controller also improves the re-stabilization within gait cycles and achieves a more coordinated anti-phase pattern of Ground Reaction Forces (GRF). The results demonstrate that a decoupled, hierarchical design can effectively mitigate the internal dynamic disturbances arising from the mass and movement of the SLs, enabling stable locomotion for humanoids equipped with functional limbs. Code and videos are available here: https://github.com/heyzbw/HuSLs.

## 核心内容
The integration of Supernumerary Limbs (SLs) on humanoid robots poses a significant stability challenge due to the dynamic perturbations they introduce. This thesis addresses this issue by designing a novel hierarchical control architecture to improve humanoid locomotion stability with SLs. The core of this framework is a decoupled strategy that combines learning-based locomotion with model-based balancing. The low-level component consists of a walking gait for a Unitree H1 humanoid through imitation learning and curriculum learning. The high-level component actively utilizes the SLs for dynamic balancing. The effectiveness of the system is evaluated in a physics-based simulation under three conditions: baseline gait for an unladen humanoid (baseline walking), walking with a static SL payload (static payload), and walking with the active dynamic balancing controller (dynamic balancing). Our evaluation shows that the dynamic balancing controller improves stability. Compared to the static payload condition, the balancing strategy yields a gait pattern closer to the baseline and decreases the Dynamic Time Warping (DTW) distance of the CoM trajectory by 47\%. The balancing controller also improves the re-stabilization within gait cycles and achieves a more coordinated anti-phase pattern of Ground Reaction Forces (GRF). The results demonstrate that a decoupled, hierarchical design can effectively mitigate the internal dynamic disturbances arising from the mass and movement of the SLs, enabling stable locomotion for humanoids equipped with functional limbs. Code and videos are available here: https://github.com/heyzbw/HuSLs.

## 参考
- http://arxiv.org/abs/2512.00077v1

