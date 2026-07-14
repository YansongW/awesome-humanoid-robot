---
$id: ent_paper_wang_underwatervla_dual_brain_visio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation'
  zh: UnderwaterVLA
  ko: 'UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation'
summary:
  en: 'UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation (UnderwaterVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Westlake University, Zhejiang University,
    Australian National University.'
  zh: 'UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation (UnderwaterVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Westlake University, Zhejiang University,
    Australian National University.'
  ko: 'UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation (UnderwaterVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Westlake University, Zhejiang University,
    Australian National University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- underwatervla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22441v1.
sources:
- id: src_001
  type: paper
  title: 'UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation (arXiv)'
  url: https://arxiv.org/abs/2509.22441
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UnderwaterVLA source
  url: https://doi.org/10.48550/arXiv.2509.22441
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents UnderwaterVLA, a novel framework for autonomous underwater navigation that integrates multimodal foundation models with embodied intelligence systems. Underwater operations remain difficult due to hydrodynamic disturbances, limited communication bandwidth, and degraded sensing in turbid waters. To address these challenges, we introduce three innovations. First, a dual-brain architecture decouples high-level mission reasoning from low-level reactive control, enabling robust operation under communication and computational constraints. Second, we apply Vision-Language-Action(VLA) models to underwater robotics for the first time, incorporating structured chain-of-thought reasoning for interpretable decision-making. Third, a hydrodynamics-informed Model Predictive Control(MPC) scheme compensates for fluid effects in real time without costly task-specific training. Experimental results in field tests show that UnderwaterVLA reduces navigation errors in degraded visual conditions while maintaining higher task completion by 19% to 27% over baseline. By minimizing reliance on underwater-specific training data and improving adaptability across environments, UnderwaterVLA provides a scalable and cost-effective path toward the next generation of intelligent AUVs.

## 核心内容
This paper presents UnderwaterVLA, a novel framework for autonomous underwater navigation that integrates multimodal foundation models with embodied intelligence systems. Underwater operations remain difficult due to hydrodynamic disturbances, limited communication bandwidth, and degraded sensing in turbid waters. To address these challenges, we introduce three innovations. First, a dual-brain architecture decouples high-level mission reasoning from low-level reactive control, enabling robust operation under communication and computational constraints. Second, we apply Vision-Language-Action(VLA) models to underwater robotics for the first time, incorporating structured chain-of-thought reasoning for interpretable decision-making. Third, a hydrodynamics-informed Model Predictive Control(MPC) scheme compensates for fluid effects in real time without costly task-specific training. Experimental results in field tests show that UnderwaterVLA reduces navigation errors in degraded visual conditions while maintaining higher task completion by 19% to 27% over baseline. By minimizing reliance on underwater-specific training data and improving adaptability across environments, UnderwaterVLA provides a scalable and cost-effective path toward the next generation of intelligent AUVs.

## 参考
- http://arxiv.org/abs/2509.22441v1

