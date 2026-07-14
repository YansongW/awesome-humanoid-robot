---
$id: ent_paper_sim_to_real_learning_for_human_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Sim-to-Real Learning for Humanoid Box Loco-Manipulation
  zh: Sim-to-Real Learning for Humanoid Box Loco-Manipulation
  ko: Sim-to-Real Learning for Humanoid Box Loco-Manipulation
summary:
  en: Sim-to-Real Learning for Humanoid Box Loco-Manipulation is a 2023 work on loco-manipulation and whole-body-control for
    humanoid robots.
  zh: Sim-to-Real Learning for Humanoid Box Loco-Manipulation is a 2023 work on loco-manipulation and whole-body-control for
    humanoid robots.
  ko: Sim-to-Real Learning for Humanoid Box Loco-Manipulation is a 2023 work on loco-manipulation and whole-body-control for
    humanoid robots.
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
- sim_to_real_learning_for_human
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2310.03191v1.
sources:
- id: src_001
  type: paper
  title: Sim-to-Real Learning for Humanoid Box Loco-Manipulation (arXiv)
  url: https://arxiv.org/abs/2310.03191
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
In this work we propose a learning-based approach to box loco-manipulation for a humanoid robot. This is a particularly challenging problem due to the need for whole-body coordination in order to lift boxes of varying weight, position, and orientation while maintaining balance. To address this challenge, we present a sim-to-real reinforcement learning approach for training general box pickup and carrying skills for the bipedal robot Digit. Our reward functions are designed to produce the desired interactions with the box while also valuing balance and gait quality. We combine the learned skills into a full system for box loco-manipulation to achieve the task of moving boxes from one table to another with a variety of sizes, weights, and initial configurations. In addition to quantitative simulation results, we demonstrate successful sim-to-real transfer on the humanoid r

## 核心内容
In this work we propose a learning-based approach to box loco-manipulation for a humanoid robot. This is a particularly challenging problem due to the need for whole-body coordination in order to lift boxes of varying weight, position, and orientation while maintaining balance. To address this challenge, we present a sim-to-real reinforcement learning approach for training general box pickup and carrying skills for the bipedal robot Digit. Our reward functions are designed to produce the desired interactions with the box while also valuing balance and gait quality. We combine the learned skills into a full system for box loco-manipulation to achieve the task of moving boxes from one table to another with a variety of sizes, weights, and initial configurations. In addition to quantitative simulation results, we demonstrate successful sim-to-real transfer on the humanoid r

## 参考
- http://arxiv.org/abs/2310.03191v1

