---
$id: ent_paper_towards_adaptive_humanoid_cont_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning
  zh: 多行为蒸馏不是简单拼策略
  ko: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning
summary:
  en: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning is a knowledge node related
    to paper in the humanoid robot value chain.
  zh: Humanoid robots are promising to learn a diverse set of human-like locomotion behaviors, including standing up, walking,
    running, and jumping. However, existing methods predominantly require training independent policies for each skill, yielding
    behavior-specific controllers that exhibit limited generalization and brittle performance when deployed on irregular terrains
    and in diverse situations. To address this challenge, we propose Adaptive Humanoid Control (AHC) that adopts a two-stage
    framework to learn an adaptive humanoid locomotion controller across different skills and terrains. Specifically, we first
    train several primary locomotion policies and perform a multi-behavior distillation process to obtain a basic multi-behavior
    controller, facilitating adaptive behavior switching based
  ko: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning is a knowledge node related
    to paper in the humanoid robot value chain.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.06371v3.
sources:
- id: src_001
  type: paper
  title: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning (arXiv)
  url: https://arxiv.org/abs/2511.06371
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 多行为蒸馏不是简单拼策略 project page
  url: https://ahc-humanoid.github.io
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Humanoid robots are promising to learn a diverse set of human-like locomotion behaviors, including standing up, walking, running, and jumping. However, existing methods predominantly require training independent policies for each skill, yielding behavior-specific controllers that exhibit limited generalization and brittle performance when deployed on irregular terrains and in diverse situations. To address this challenge, we propose Adaptive Humanoid Control (AHC) that adopts a two-stage framework to learn an adaptive humanoid locomotion controller across different skills and terrains. Specifically, we first train several primary locomotion policies and perform a multi-behavior distillation process to obtain a basic multi-behavior controller, facilitating adaptive behavior switching based on the environment. Then, we perform reinforced fine-tuning by collecting online feedback in performing adaptive behaviors on more diverse terrains, enhancing terrain adaptability for the controller. We conduct experiments in both simulation and real-world experiments in Unitree G1 robots. The results show that our method exhibits strong adaptability across various situations and terrains. Project website: https://ahc-humanoid.github.io.

## 核心内容
Humanoid robots are promising to learn a diverse set of human-like locomotion behaviors, including standing up, walking, running, and jumping. However, existing methods predominantly require training independent policies for each skill, yielding behavior-specific controllers that exhibit limited generalization and brittle performance when deployed on irregular terrains and in diverse situations. To address this challenge, we propose Adaptive Humanoid Control (AHC) that adopts a two-stage framework to learn an adaptive humanoid locomotion controller across different skills and terrains. Specifically, we first train several primary locomotion policies and perform a multi-behavior distillation process to obtain a basic multi-behavior controller, facilitating adaptive behavior switching based on the environment. Then, we perform reinforced fine-tuning by collecting online feedback in performing adaptive behaviors on more diverse terrains, enhancing terrain adaptability for the controller. We conduct experiments in both simulation and real-world experiments in Unitree G1 robots. The results show that our method exhibits strong adaptability across various situations and terrains. Project website: https://ahc-humanoid.github.io.

## 参考
- http://arxiv.org/abs/2511.06371v3

