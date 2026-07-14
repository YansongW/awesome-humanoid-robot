---
$id: ent_paper_human_humanoid_robots_cross_em_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
  zh: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
  ko: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
summary:
  en: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
    is a 2024 work on loco-manipulation and whole-body-control for humanoid robots.
  zh: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
    is a 2024 work on loco-manipulation and whole-body-control for humanoid robots.
  ko: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
    is a 2024 work on loco-manipulation and whole-body-control for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- human_humanoid_robots_cross_em
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.15166v1.
sources:
- id: src_001
  type: paper
  title: Human-Humanoid Robots Cross-Embodiment Behavior-Skill Transfer Using Decomposed Adversarial Learning from Demonstration
    (arXiv)
  url: https://arxiv.org/abs/2412.15166
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots are envisioned as embodied intelligent agents capable of performing a wide range of human-level loco-manipulation tasks, particularly in scenarios requiring strenuous and repetitive labor. However, learning these skills is challenging due to the high degrees of freedom of humanoid robots, and collecting sufficient training data for humanoid is a laborious process. Given the rapid introduction of new humanoid platforms, a cross-embodiment framework that allows generalizable skill transfer is becoming increasingly critical. To address this, we propose a transferable framework that reduces the data bottleneck by using a unified digital human model as a common prototype and bypassing the need for re-training on every new robot platform. The model learns behavior primitives from human demonstrations through adversarial imitation, and the complex robot structures are decomposed into functional components, each trained independently and dynamically coordinated. Task generalization is achieved through a human-object interaction graph, and skills are transferred to different robots via embodiment-specific kinematic motion retargeting and dynamic fine-tuning. Our framework is validated on five humanoid robots with diverse configurations, demonstrating stable loco-manipulation and highlighting its effectiveness in reducing data requirements and increasing the efficiency of skill transfer across platforms.

## 核心内容
Humanoid robots are envisioned as embodied intelligent agents capable of performing a wide range of human-level loco-manipulation tasks, particularly in scenarios requiring strenuous and repetitive labor. However, learning these skills is challenging due to the high degrees of freedom of humanoid robots, and collecting sufficient training data for humanoid is a laborious process. Given the rapid introduction of new humanoid platforms, a cross-embodiment framework that allows generalizable skill transfer is becoming increasingly critical. To address this, we propose a transferable framework that reduces the data bottleneck by using a unified digital human model as a common prototype and bypassing the need for re-training on every new robot platform. The model learns behavior primitives from human demonstrations through adversarial imitation, and the complex robot structures are decomposed into functional components, each trained independently and dynamically coordinated. Task generalization is achieved through a human-object interaction graph, and skills are transferred to different robots via embodiment-specific kinematic motion retargeting and dynamic fine-tuning. Our framework is validated on five humanoid robots with diverse configurations, demonstrating stable loco-manipulation and highlighting its effectiveness in reducing data requirements and increasing the efficiency of skill transfer across platforms.

## 参考
- http://arxiv.org/abs/2412.15166v1

