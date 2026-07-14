---
$id: ent_paper_hafo_a_force_adaptive_control_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments'
  zh: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments'
  ko: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments'
summary:
  en: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hafo
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.20275v4.
sources:
- id: src_001
  type: paper
  title: 'HAFO: A Force-Adaptive Control Framework for Humanoid Robots in Intense Interaction Environments (arXiv)'
  url: https://arxiv.org/abs/2511.20275
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning (RL) controllers have made impressive progress in humanoid locomotion and light-weight object manipulation. However, achieving robust and precise motion control with intense force interaction remains a significant challenge. To address these limitations, this paper proposes HAFO, a dual-agent reinforcement learning framework that concurrently optimizes both a robust locomotion strategy and a precise upper-body manipulation strategy via coupled training. We employ a constrained residual action space to improve dual-agent training stability and sample efficiency. The external tension disturbances are explicitly modeled using a spring-damper system, allowing for fine-grained force control through manipulation of the virtual spring. In this process, the reinforcement learning policy autonomously generates a disturbance-rejection response by utilizing environmental feedback. The experimental results demonstrate that HAFO achieves whole-body control for humanoid robots across diverse force-interaction environments using a single dual-agent policy, delivering outstanding performance under load-bearing and thrust-disturbance conditions, while maintaining stable operation even under rope suspension state.

## 核心内容
Reinforcement learning (RL) controllers have made impressive progress in humanoid locomotion and light-weight object manipulation. However, achieving robust and precise motion control with intense force interaction remains a significant challenge. To address these limitations, this paper proposes HAFO, a dual-agent reinforcement learning framework that concurrently optimizes both a robust locomotion strategy and a precise upper-body manipulation strategy via coupled training. We employ a constrained residual action space to improve dual-agent training stability and sample efficiency. The external tension disturbances are explicitly modeled using a spring-damper system, allowing for fine-grained force control through manipulation of the virtual spring. In this process, the reinforcement learning policy autonomously generates a disturbance-rejection response by utilizing environmental feedback. The experimental results demonstrate that HAFO achieves whole-body control for humanoid robots across diverse force-interaction environments using a single dual-agent policy, delivering outstanding performance under load-bearing and thrust-disturbance conditions, while maintaining stable operation even under rope suspension state.

## 参考
- http://arxiv.org/abs/2511.20275v4

