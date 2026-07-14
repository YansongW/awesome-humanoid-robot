---
$id: ent_paper_zhang_ego_centric_predictive_model_c_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Ego-centric Predictive Model Conditioned on Hand Trajectories
  zh: Ego-PM
  ko: Ego-centric Predictive Model Conditioned on Hand Trajectories
summary:
  en: Ego-centric Predictive Model Conditioned on Hand Trajectories (Ego-PM), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Show Lab, National University of Singapore.
  zh: Ego-centric Predictive Model Conditioned on Hand Trajectories (Ego-PM), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Show Lab, National University of Singapore.
  ko: Ego-centric Predictive Model Conditioned on Hand Trajectories (Ego-PM), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Show Lab, National University of Singapore.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ego_pm
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.19852v2.
sources:
- id: src_001
  type: paper
  title: Ego-centric Predictive Model Conditioned on Hand Trajectories (arXiv)
  url: https://arxiv.org/abs/2508.19852
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Ego-PM source
  url: https://doi.org/10.48550/arXiv.2508.19852
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In egocentric scenarios, anticipating both the next action and its visual outcome is essential for understanding human-object interactions and for enabling robotic planning. However, existing paradigms fall short of jointly modeling these aspects. Vision-Language-Action (VLA) models focus on action prediction but lack explicit modeling of how actions influence the visual scene, while video prediction models generate future frames without conditioning on specific actions, often resulting in implausible or contextually inconsistent outcomes. To bridge this gap, we propose a unified two-stage predictive framework that jointly models action and visual future in egocentric scenarios, conditioned on hand trajectories. In the first stage, we perform consecutive state modeling to process heterogeneous inputs (visual observations, language, and action history) and explicitly predict future hand trajectories. In the second stage, we introduce causal cross-attention to fuse multi-modal cues, leveraging inferred action signals to guide an image-based Latent Diffusion Model (LDM) for frame-by-frame future video generation. Our approach is the first unified model designed to handle both egocentric human activity understanding and robotic manipulation tasks, providing explicit predictions of both upcoming actions and their visual consequences. Extensive experiments on Ego4D, BridgeData, and RLBench demonstrate that our method outperforms state-of-the-art baselines in both action prediction and future video synthesis.

## 核心内容
In egocentric scenarios, anticipating both the next action and its visual outcome is essential for understanding human-object interactions and for enabling robotic planning. However, existing paradigms fall short of jointly modeling these aspects. Vision-Language-Action (VLA) models focus on action prediction but lack explicit modeling of how actions influence the visual scene, while video prediction models generate future frames without conditioning on specific actions, often resulting in implausible or contextually inconsistent outcomes. To bridge this gap, we propose a unified two-stage predictive framework that jointly models action and visual future in egocentric scenarios, conditioned on hand trajectories. In the first stage, we perform consecutive state modeling to process heterogeneous inputs (visual observations, language, and action history) and explicitly predict future hand trajectories. In the second stage, we introduce causal cross-attention to fuse multi-modal cues, leveraging inferred action signals to guide an image-based Latent Diffusion Model (LDM) for frame-by-frame future video generation. Our approach is the first unified model designed to handle both egocentric human activity understanding and robotic manipulation tasks, providing explicit predictions of both upcoming actions and their visual consequences. Extensive experiments on Ego4D, BridgeData, and RLBench demonstrate that our method outperforms state-of-the-art baselines in both action prediction and future video synthesis.

## 参考
- http://arxiv.org/abs/2508.19852v2

