---
$id: ent_paper_gbc_generalized_behavior_cloni_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GBC: Generalized Behavior-Cloning Framework for Whole-Body Humanoid Imitation'
  zh: 'GBC: Generalized Behavior-Cloning Framework for Whole-Body Humanoid Imitation'
  ko: 'GBC: Generalized Behavior-Cloning Framework for Whole-Body Humanoid Imitation'
summary:
  en: 'GBC: Generalized Behavior-Cloning Framework for Whole-Body Humanoid Imitation is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.'
  zh: 'GBC: Generalized Behavior-Cloning Framework for Whole-Body Humanoid Imitation is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.'
  ko: 'GBC: Generalized Behavior-Cloning Framework for Whole-Body Humanoid Imitation is a 2025 work on loco-manipulation and
    whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gbc
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.09960v1.
sources:
- id: src_001
  type: paper
  title: 'GBC: Generalized Behavior-Cloning Framework for Whole-Body Humanoid Imitation (arXiv)'
  url: https://arxiv.org/abs/2508.09960
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The creation of human-like humanoid robots is hindered by a fundamental fragmentation: data processing and learning algorithms are rarely universal across different robot morphologies. This paper introduces the Generalized Behavior Cloning (GBC) framework, a comprehensive and unified solution designed to solve this end-to-end challenge. GBC establishes a complete pathway from human motion to robot action through three synergistic innovations. First, an adaptive data pipeline leverages a differentiable IK network to automatically retarget any human MoCap data to any humanoid. Building on this foundation, our novel DAgger-MMPPO algorithm with its MMTransformer architecture learns robust, high-fidelity imitation policies. To complete the ecosystem, the entire framework is delivered as an efficient, open-source platform based on Isaac Lab, empowering the community to deploy the full workflow via simple configuration scripts. We validate the power and generality of GBC by training policies on multiple heterogeneous humanoids, demonstrating excellent performance and transfer to novel motions. This work establishes the first practical and unified pathway for creating truly generalized humanoid controllers.

## 核心内容
The creation of human-like humanoid robots is hindered by a fundamental fragmentation: data processing and learning algorithms are rarely universal across different robot morphologies. This paper introduces the Generalized Behavior Cloning (GBC) framework, a comprehensive and unified solution designed to solve this end-to-end challenge. GBC establishes a complete pathway from human motion to robot action through three synergistic innovations. First, an adaptive data pipeline leverages a differentiable IK network to automatically retarget any human MoCap data to any humanoid. Building on this foundation, our novel DAgger-MMPPO algorithm with its MMTransformer architecture learns robust, high-fidelity imitation policies. To complete the ecosystem, the entire framework is delivered as an efficient, open-source platform based on Isaac Lab, empowering the community to deploy the full workflow via simple configuration scripts. We validate the power and generality of GBC by training policies on multiple heterogeneous humanoids, demonstrating excellent performance and transfer to novel motions. This work establishes the first practical and unified pathway for creating truly generalized humanoid controllers.

## 参考
- http://arxiv.org/abs/2508.09960v1

