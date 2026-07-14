---
$id: ent_paper_zhang_reinforcing_action_policies_by_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcing Action Policies by Prophesying
  zh: Prophet
  ko: Reinforcing Action Policies by Prophesying
summary:
  en: Reinforcing Action Policies by Prophesying (Prophet), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Fudan University, Shanghai Innovation Institute, Logos Robotics.
  zh: Reinforcing Action Policies by Prophesying (Prophet), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Fudan University, Shanghai Innovation Institute, Logos Robotics.
  ko: Reinforcing Action Policies by Prophesying (Prophet), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Fudan University, Shanghai Innovation Institute, Logos Robotics.
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
- prophet
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.20633v1.
sources:
- id: src_001
  type: paper
  title: Reinforcing Action Policies by Prophesying (arXiv)
  url: https://arxiv.org/abs/2511.20633
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Prophet source
  url: https://doi.org/10.48550/arXiv.2511.20633
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) policies excel in aligning language, perception, and robot control. However, most VLAs are trained purely by imitation, which overfits to demonstrations, and is brittle under distribution shift. Reinforcement learning (RL) directly optimizes task reward and thus addresses this misalignment, but real-robot interaction is expensive and conventional simulators are hard to engineer and transfer. We address both data efficiency and optimization stability in VLA post-training via a learned world model and an RL procedure tailored to flow-based action heads. Specifically, we introduce Prophet, a unified action-to-video robot actuation pretrained across large-scale, heterogeneous robot data to learn reusable action-outcome dynamics. It is able to few-shot adapt to new robots, objects, and environments, yielding a rollout-ready simulator. Upon Prophet, we reinforce action policies with Flow-action-GRPO (FA-GRPO), which adapts Flow-GRPO to operate on VLA actions, and with FlowScale, a stepwise reweighting that rescales per-step gradients in the flow head. Together, Prophet, FA-GRPO, and FlowScale constitute ProphRL, a practical, data- and compute-efficient path to VLA post-training. Experiments show 5-17% success gains on public benchmarks and 24-30% gains on real robots across different VLA variants.

## 核心内容
Vision-Language-Action (VLA) policies excel in aligning language, perception, and robot control. However, most VLAs are trained purely by imitation, which overfits to demonstrations, and is brittle under distribution shift. Reinforcement learning (RL) directly optimizes task reward and thus addresses this misalignment, but real-robot interaction is expensive and conventional simulators are hard to engineer and transfer. We address both data efficiency and optimization stability in VLA post-training via a learned world model and an RL procedure tailored to flow-based action heads. Specifically, we introduce Prophet, a unified action-to-video robot actuation pretrained across large-scale, heterogeneous robot data to learn reusable action-outcome dynamics. It is able to few-shot adapt to new robots, objects, and environments, yielding a rollout-ready simulator. Upon Prophet, we reinforce action policies with Flow-action-GRPO (FA-GRPO), which adapts Flow-GRPO to operate on VLA actions, and with FlowScale, a stepwise reweighting that rescales per-step gradients in the flow head. Together, Prophet, FA-GRPO, and FlowScale constitute ProphRL, a practical, data- and compute-efficient path to VLA post-training. Experiments show 5-17% success gains on public benchmarks and 24-30% gains on real robots across different VLA variants.

## 参考
- http://arxiv.org/abs/2511.20633v1

