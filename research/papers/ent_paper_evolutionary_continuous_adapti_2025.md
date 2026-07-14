---
$id: ent_paper_evolutionary_continuous_adapti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance
  zh: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance
  ko: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance
summary:
  en: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance is a 2025 work on hardware design
    for humanoid robots.
  zh: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance is a 2025 work on hardware design
    for humanoid robots.
  ko: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance is a 2025 work on hardware design
    for humanoid robots.
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- evolutionary_continuous_adapti
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.26082v1.
sources:
- id: src_001
  type: paper
  title: Evolutionary Continuous Adaptive RL-Powered Co-Design for Humanoid Chin-Up Performance (arXiv)
  url: https://arxiv.org/abs/2509.26082
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have seen significant advancements in both design and control, with a growing emphasis on integrating these aspects to enhance overall performance. Traditionally, robot design has followed a sequential process, where control algorithms are developed after the hardware is finalized. However, this can be myopic and prevent robots to fully exploit their hardware capabilities. Recent approaches advocate for co-design, optimizing both design and control in parallel to maximize robotic capabilities. This paper presents the Evolutionary Continuous Adaptive RL-based Co-Design (EA-CoRL) framework, which combines reinforcement learning (RL) with evolutionary strategies to enable continuous adaptation of the control policy to the hardware. EA-CoRL comprises two key components: Design Evolution, which explores the hardware choices using an evolutionary algorithm to identify efficient configurations, and Policy Continuous Adaptation, which fine-tunes a task-specific control policy across evolving designs to maximize performance rewards. We evaluate EA-CoRL by co-designing the actuators (gear ratios) and control policy of the RH5 humanoid for a highly dynamic chin-up task, previously unfeasible due to actuator limitations. Comparative results against state-of-the-art RL-based co-design methods show that EA-CoRL achieves higher fitness score and broader design space exploration, highlighting the critical role of continuous policy adaptation in robot co-design.

## 核心内容
Humanoid robots have seen significant advancements in both design and control, with a growing emphasis on integrating these aspects to enhance overall performance. Traditionally, robot design has followed a sequential process, where control algorithms are developed after the hardware is finalized. However, this can be myopic and prevent robots to fully exploit their hardware capabilities. Recent approaches advocate for co-design, optimizing both design and control in parallel to maximize robotic capabilities. This paper presents the Evolutionary Continuous Adaptive RL-based Co-Design (EA-CoRL) framework, which combines reinforcement learning (RL) with evolutionary strategies to enable continuous adaptation of the control policy to the hardware. EA-CoRL comprises two key components: Design Evolution, which explores the hardware choices using an evolutionary algorithm to identify efficient configurations, and Policy Continuous Adaptation, which fine-tunes a task-specific control policy across evolving designs to maximize performance rewards. We evaluate EA-CoRL by co-designing the actuators (gear ratios) and control policy of the RH5 humanoid for a highly dynamic chin-up task, previously unfeasible due to actuator limitations. Comparative results against state-of-the-art RL-based co-design methods show that EA-CoRL achieves higher fitness score and broader design space exploration, highlighting the critical role of continuous policy adaptation in robot co-design.

## 参考
- http://arxiv.org/abs/2509.26082v1

