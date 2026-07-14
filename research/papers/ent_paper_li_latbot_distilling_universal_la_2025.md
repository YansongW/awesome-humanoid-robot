---
$id: ent_paper_li_latbot_distilling_universal_la_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models'
  zh: LatBot
  ko: 'LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models'
summary:
  en: 'LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models (LatBot), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Microelectronics, Chinese Academy of Sciences, University of
    Chinese Academy of Sciences, Microsoft Research.'
  zh: 'LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models (LatBot), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Microelectronics, Chinese Academy of Sciences, University of
    Chinese Academy of Sciences, Microsoft Research.'
  ko: 'LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models (LatBot), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Microelectronics, Chinese Academy of Sciences, University of
    Chinese Academy of Sciences, Microsoft Research.'
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
- latbot
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.23034v1.
sources:
- id: src_001
  type: paper
  title: 'LatBot: Distilling Universal Latent Actions for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.23034
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LatBot source
  url: https://doi.org/10.48550/arXiv.2511.23034
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning transferable latent actions from large-scale object manipulation videos can significantly enhance generalization in downstream robotics tasks, as such representations are agnostic to different robot embodiments. Existing approaches primarily rely on visual reconstruction objectives while neglecting physical priors, leading to sub-optimal performance in learning universal representations. To address these challenges, we propose a Universal Latent Action Learning framework that takes task instructions and multiple frames as inputs, and optimizes both future frame reconstruction and action sequence prediction. Unlike prior works, incorporating action predictions (e.g., gripper or hand trajectories and orientations) allows the model to capture richer physical priors such as real-world distances and orientations, thereby enabling seamless transferability to downstream tasks. We further decompose the latent actions into learnable motion and scene tokens to distinguish the robot's active movements from environmental changes, thus filtering out irrelevant dynamics. By distilling the learned latent actions into the latest VLA models, we achieve strong performance across both simulated (SIMPLER and LIBERO) and real-world robot settings. Notably, with only 10 real-world trajectories per task collected on a Franka robot, our approach successfully completes all five challenging tasks, demonstrating strong few-shot transferability in robotic manipulation.

## 核心内容
Learning transferable latent actions from large-scale object manipulation videos can significantly enhance generalization in downstream robotics tasks, as such representations are agnostic to different robot embodiments. Existing approaches primarily rely on visual reconstruction objectives while neglecting physical priors, leading to sub-optimal performance in learning universal representations. To address these challenges, we propose a Universal Latent Action Learning framework that takes task instructions and multiple frames as inputs, and optimizes both future frame reconstruction and action sequence prediction. Unlike prior works, incorporating action predictions (e.g., gripper or hand trajectories and orientations) allows the model to capture richer physical priors such as real-world distances and orientations, thereby enabling seamless transferability to downstream tasks. We further decompose the latent actions into learnable motion and scene tokens to distinguish the robot's active movements from environmental changes, thus filtering out irrelevant dynamics. By distilling the learned latent actions into the latest VLA models, we achieve strong performance across both simulated (SIMPLER and LIBERO) and real-world robot settings. Notably, with only 10 real-world trajectories per task collected on a Franka robot, our approach successfully completes all five challenging tasks, demonstrating strong few-shot transferability in robotic manipulation.

## 参考
- http://arxiv.org/abs/2511.23034v1

