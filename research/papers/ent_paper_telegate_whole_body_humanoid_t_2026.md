---
$id: ent_paper_telegate_whole_body_humanoid_t_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior'
  zh: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior'
  ko: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior'
summary:
  en: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior is a 2026 work on teleoperation
    for humanoid robots.'
  zh: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior is a 2026 work on teleoperation
    for humanoid robots.'
  ko: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior is a 2026 work on teleoperation
    for humanoid robots.'
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
- telegate
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.09628v2.
sources:
- id: src_001
  type: paper
  title: 'TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior (arXiv)'
  url: https://arxiv.org/abs/2602.09628
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Real-time whole-body teleoperation is a critical method for humanoid robots to perform complex tasks in unstructured environments. However, developing a unified controller that robustly supports diverse human motions remains a significant challenge. Existing methods typically distill multiple expert policies into a single general policy, which often inevitably leads to performance degradation, particularly on highly dynamic motions. This paper presents TeleGate, a unified whole-body teleoperation framework for humanoid robots that achieves high-precision tracking across various motions while avoiding the performance loss inherent in knowledge distillation. Our key idea is to preserve the full capability of domain-specific expert policies by training a lightweight gating network, which dynamically activates experts in real-time based on proprioceptive states and reference trajectories. Furthermore, to compensate for the absence of future reference trajectories in real-time teleoperation, we introduce a VAE-based motion prior module that extracts implicit future motion intent from historical observations, enabling anticipatory control for motions requiring prediction such as jumping and standing up. We conducted empirical evaluations in simulation and also deployed our technique on the Unitree G1 humanoid robot. Using only 2.5 hours of motion capture data for training, our TeleGate achieves high-precision real-time teleoperation across diverse dynamic motions (e.g., running, fall recovery, and jumping), significantly outperforming the baseline methods in both tracking accuracy and success rate.

## 核心内容
Real-time whole-body teleoperation is a critical method for humanoid robots to perform complex tasks in unstructured environments. However, developing a unified controller that robustly supports diverse human motions remains a significant challenge. Existing methods typically distill multiple expert policies into a single general policy, which often inevitably leads to performance degradation, particularly on highly dynamic motions. This paper presents TeleGate, a unified whole-body teleoperation framework for humanoid robots that achieves high-precision tracking across various motions while avoiding the performance loss inherent in knowledge distillation. Our key idea is to preserve the full capability of domain-specific expert policies by training a lightweight gating network, which dynamically activates experts in real-time based on proprioceptive states and reference trajectories. Furthermore, to compensate for the absence of future reference trajectories in real-time teleoperation, we introduce a VAE-based motion prior module that extracts implicit future motion intent from historical observations, enabling anticipatory control for motions requiring prediction such as jumping and standing up. We conducted empirical evaluations in simulation and also deployed our technique on the Unitree G1 humanoid robot. Using only 2.5 hours of motion capture data for training, our TeleGate achieves high-precision real-time teleoperation across diverse dynamic motions (e.g., running, fall recovery, and jumping), significantly outperforming the baseline methods in both tracking accuracy and success rate.

## 参考
- http://arxiv.org/abs/2602.09628v2

