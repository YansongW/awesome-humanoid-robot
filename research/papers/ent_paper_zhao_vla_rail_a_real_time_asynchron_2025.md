---
$id: ent_paper_zhao_vla_rail_a_real_time_asynchron_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots'
  zh: VLA-RAIL
  ko: 'VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots'
summary:
  en: 'VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots (VLA-RAIL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by China Mobile (Hangzhou) Information Technology Co., Ltd.,.'
  zh: 'VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots (VLA-RAIL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by China Mobile (Hangzhou) Information Technology Co., Ltd.,.'
  ko: 'VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots (VLA-RAIL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by China Mobile (Hangzhou) Information Technology Co., Ltd.,.'
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
- vision_language_action
- vla
- vla_rail
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.24673v1.
sources:
- id: src_001
  type: paper
  title: 'VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots (arXiv)'
  url: https://arxiv.org/abs/2512.24673
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-RAIL source
  url: https://doi.org/10.48550/arXiv.2512.24673
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have achieved remarkable breakthroughs in robotics, with the action chunk playing a dominant role in these advances. Given the real-time and continuous nature of robotic motion control, the strategies for fusing a queue of successive action chunks have a profound impact on the overall performance of VLA models. Existing methods suffer from jitter, stalling, or even pauses in robotic action execution, which not only limits the achievable execution speed but also reduces the overall success rate of task completion. This paper introduces VLA-RAIL (A Real-Time Asynchronous Inference Linker), a novel framework designed to address these issues by conducting model inference and robot motion control asynchronously and guaranteeing smooth, continuous, and high-speed action execution. The core contributions of the paper are two fold: a Trajectory Smoother that effectively filters out the noise and jitter in the trajectory of one action chunk using polynomial fitting and a Chunk Fuser that seamlessly align the current executing trajectory and the newly arrived chunk, ensuring position, velocity, and acceleration continuity between two successive action chunks. We validate the effectiveness of VLA-RAIL on a benchmark of dynamic simulation tasks and several real-world manipulation tasks. Experimental results demonstrate that VLA-RAIL significantly reduces motion jitter, enhances execution speed, and improves task success rates, which will become a key infrastructure for the large-scale deployment of VLA models.

## 核心内容
Vision-Language-Action (VLA) models have achieved remarkable breakthroughs in robotics, with the action chunk playing a dominant role in these advances. Given the real-time and continuous nature of robotic motion control, the strategies for fusing a queue of successive action chunks have a profound impact on the overall performance of VLA models. Existing methods suffer from jitter, stalling, or even pauses in robotic action execution, which not only limits the achievable execution speed but also reduces the overall success rate of task completion. This paper introduces VLA-RAIL (A Real-Time Asynchronous Inference Linker), a novel framework designed to address these issues by conducting model inference and robot motion control asynchronously and guaranteeing smooth, continuous, and high-speed action execution. The core contributions of the paper are two fold: a Trajectory Smoother that effectively filters out the noise and jitter in the trajectory of one action chunk using polynomial fitting and a Chunk Fuser that seamlessly align the current executing trajectory and the newly arrived chunk, ensuring position, velocity, and acceleration continuity between two successive action chunks. We validate the effectiveness of VLA-RAIL on a benchmark of dynamic simulation tasks and several real-world manipulation tasks. Experimental results demonstrate that VLA-RAIL significantly reduces motion jitter, enhances execution speed, and improves task success rates, which will become a key infrastructure for the large-scale deployment of VLA models.

## 参考
- http://arxiv.org/abs/2512.24673v1

