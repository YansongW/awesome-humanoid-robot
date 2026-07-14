---
$id: ent_paper_tan_latent_chain_of_thought_world_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Latent Chain-of-Thought World Modeling for End-to-End Driving
  zh: LCDrive
  ko: Latent Chain-of-Thought World Modeling for End-to-End Driving
summary:
  en: Latent Chain-of-Thought World Modeling for End-to-End Driving (LCDrive), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Tübingen.
  zh: Latent Chain-of-Thought World Modeling for End-to-End Driving (LCDrive), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Tübingen.
  ko: Latent Chain-of-Thought World Modeling for End-to-End Driving (LCDrive), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by University of Tübingen.
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
- lcdrive
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.10226v2.
sources:
- id: src_001
  type: paper
  title: Latent Chain-of-Thought World Modeling for End-to-End Driving (arXiv)
  url: https://arxiv.org/abs/2512.10226
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LCDrive source
  url: https://doi.org/10.48550/arXiv.2512.10226
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent Vision-Language-Action (VLA) models for autonomous driving explore inference-time reasoning as a way to improve driving performance and safety in challenging scenarios. Most prior work uses natural language to express chain-of-thought (CoT) reasoning before producing driving actions. However, text may not be the most efficient representation for reasoning. In this work, we present Latent-CoT-Drive (LCDrive): a model that expresses CoT in a latent language that captures possible outcomes of the driving actions being considered. Our approach unifies CoT reasoning and decision making by representing both in an action-aligned latent space. Instead of natural language, the model reasons by interleaving (1) action-proposal tokens, which use the same vocabulary as the model's output actions; and (2) world model tokens, which are grounded in a learned latent world model and express future outcomes of these actions. We cold start latent CoT by supervising the model's action proposals and world model tokens based on ground-truth future rollouts of the scene. We then post-train with closed-loop reinforcement learning to strengthen reasoning capabilities. On a large-scale end-to-end driving benchmark, LCDrive achieves faster inference, better trajectory quality, and larger improvements from interactive reinforcement learning compared to both non-reasoning and text-reasoning baselines.

## 核心内容
Recent Vision-Language-Action (VLA) models for autonomous driving explore inference-time reasoning as a way to improve driving performance and safety in challenging scenarios. Most prior work uses natural language to express chain-of-thought (CoT) reasoning before producing driving actions. However, text may not be the most efficient representation for reasoning. In this work, we present Latent-CoT-Drive (LCDrive): a model that expresses CoT in a latent language that captures possible outcomes of the driving actions being considered. Our approach unifies CoT reasoning and decision making by representing both in an action-aligned latent space. Instead of natural language, the model reasons by interleaving (1) action-proposal tokens, which use the same vocabulary as the model's output actions; and (2) world model tokens, which are grounded in a learned latent world model and express future outcomes of these actions. We cold start latent CoT by supervising the model's action proposals and world model tokens based on ground-truth future rollouts of the scene. We then post-train with closed-loop reinforcement learning to strengthen reasoning capabilities. On a large-scale end-to-end driving benchmark, LCDrive achieves faster inference, better trajectory quality, and larger improvements from interactive reinforcement learning compared to both non-reasoning and text-reasoning baselines.

## 参考
- http://arxiv.org/abs/2512.10226v2

