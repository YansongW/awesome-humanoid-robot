---
$id: ent_paper_steadytray_learning_object_bal_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning'
  zh: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning'
  ko: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning'
summary:
  en: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning is a 2026
    work on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning is a 2026
    work on loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning is a 2026
    work on loco-manipulation and whole-body-control for humanoid robots.'
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
- loco_manipulation
- steadytray
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.10306v1.
sources:
- id: src_001
  type: paper
  title: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2603.10306
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'SteadyTray: Learning Object Balancing Tasks in Humanoid Tray Transport via Residual Reinforcement Learning project
    page'
  url: https://steadytray.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Stabilizing unsecured payloads against the inherent oscillations of dynamic bipedal locomotion remains a critical engineering bottleneck for humanoids in unstructured environments. To solve this, we introduce ReST-RL, a hierarchical reinforcement learning architecture that explicitly decouples locomotion from payload stabilization, evaluated via the SteadyTray benchmark. Rather than relying on monolithic end-to-end learning, our framework integrates a robust base locomotion policy with a dynamic residual module engineered to actively cancel gait-induced perturbations at the end-effector. This architectural separation ensures steady tray transport without degrading the underlying bipedal stability. In simulation, the residual design significantly outperforms end-to-end baselines in gait smoothness and orientation accuracy, achieving a 96.9% success rate in variable velocity tracking and 74.5% robustness against external force disturbances. Successfully deployed on the Unitree G1 humanoid hardware, this modular approach demonstrates highly reliable zero-shot sim-to-real generalization across various objects and external force disturbances.

## 核心内容
Stabilizing unsecured payloads against the inherent oscillations of dynamic bipedal locomotion remains a critical engineering bottleneck for humanoids in unstructured environments. To solve this, we introduce ReST-RL, a hierarchical reinforcement learning architecture that explicitly decouples locomotion from payload stabilization, evaluated via the SteadyTray benchmark. Rather than relying on monolithic end-to-end learning, our framework integrates a robust base locomotion policy with a dynamic residual module engineered to actively cancel gait-induced perturbations at the end-effector. This architectural separation ensures steady tray transport without degrading the underlying bipedal stability. In simulation, the residual design significantly outperforms end-to-end baselines in gait smoothness and orientation accuracy, achieving a 96.9% success rate in variable velocity tracking and 74.5% robustness against external force disturbances. Successfully deployed on the Unitree G1 humanoid hardware, this modular approach demonstrates highly reliable zero-shot sim-to-real generalization across various objects and external force disturbances.

## 参考
- http://arxiv.org/abs/2603.10306v1

