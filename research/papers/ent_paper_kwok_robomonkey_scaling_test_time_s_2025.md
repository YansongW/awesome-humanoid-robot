---
$id: ent_paper_kwok_robomonkey_scaling_test_time_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models'
  zh: RoboMonkey
  ko: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models'
summary:
  en: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models (RoboMonkey), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Stanford University, UC Berkeley, NVIDIA Research,
    and published at CoRL25.'
  zh: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models (RoboMonkey), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Stanford University, UC Berkeley, NVIDIA Research,
    and published at CoRL25.'
  ko: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models (RoboMonkey), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Stanford University, UC Berkeley, NVIDIA Research,
    and published at CoRL25.'
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
- robomonkey
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.17811v2.
sources:
- id: src_001
  type: paper
  title: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2506.17811
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboMonkey source
  url: https://doi.org/10.48550/arXiv.2506.17811
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in visuomotor control, yet ensuring their robustness in unstructured real-world environments remains a persistent challenge. In this paper, we investigate test-time scaling through the lens of sampling and verification as means to enhance the robustness and generalization of VLAs. We first demonstrate that the relationship between action error and the number of generated samples follows an exponentiated power law across a range of VLAs, indicating the existence of inference-time scaling laws. Building on these insights, we introduce RoboMonkey, a test-time scaling framework for VLAs. At deployment, RoboMonkey samples a small set of actions from a VLA, applies Gaussian perturbation and majority voting to construct an action proposal distribution, and then uses a Vision Language Model (VLM)-based verifier to select the optimal action. We propose a synthetic data generation pipeline for training such VLM-based action verifiers, and demonstrate that scaling the synthetic dataset consistently improves verification and downstream accuracy. Through extensive simulated and hardware experiments, we show that pairing existing VLAs with RoboMonkey yields significant performance gains, achieving a 25% absolute improvement on out-of-distribution tasks and 9% on in-distribution tasks. Additionally, when adapting to new robot setups, we show that fine-tuning both VLAs and action verifiers yields a 7% performance increase compared to fine-tuning VLAs alone.

## 核心内容
Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in visuomotor control, yet ensuring their robustness in unstructured real-world environments remains a persistent challenge. In this paper, we investigate test-time scaling through the lens of sampling and verification as means to enhance the robustness and generalization of VLAs. We first demonstrate that the relationship between action error and the number of generated samples follows an exponentiated power law across a range of VLAs, indicating the existence of inference-time scaling laws. Building on these insights, we introduce RoboMonkey, a test-time scaling framework for VLAs. At deployment, RoboMonkey samples a small set of actions from a VLA, applies Gaussian perturbation and majority voting to construct an action proposal distribution, and then uses a Vision Language Model (VLM)-based verifier to select the optimal action. We propose a synthetic data generation pipeline for training such VLM-based action verifiers, and demonstrate that scaling the synthetic dataset consistently improves verification and downstream accuracy. Through extensive simulated and hardware experiments, we show that pairing existing VLAs with RoboMonkey yields significant performance gains, achieving a 25% absolute improvement on out-of-distribution tasks and 9% on in-distribution tasks. Additionally, when adapting to new robot setups, we show that fine-tuning both VLAs and action verifiers yields a 7% performance increase compared to fine-tuning VLAs alone.

## 参考
- http://arxiv.org/abs/2506.17811v2

