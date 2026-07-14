---
$id: ent_paper_fan_xr_1_towards_versatile_vision_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations'
  zh: XR-1
  ko: 'XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations'
summary:
  en: 'XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations (XR-1), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Beijing Innovation Center of Humanoid
    Robotics, Beihang University, State Key Laboratory of Virtual Reality Technology and Systems, State Key Laboratory of
    Multimedia Information Processing, Peking University.'
  zh: 'XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations (XR-1), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Beijing Innovation Center of Humanoid
    Robotics, Beihang University, State Key Laboratory of Virtual Reality Technology and Systems, State Key Laboratory of
    Multimedia Information Processing, Peking University.'
  ko: 'XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations (XR-1), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Beijing Innovation Center of Humanoid
    Robotics, Beihang University, State Key Laboratory of Virtual Reality Technology and Systems, State Key Laboratory of
    Multimedia Information Processing, Peking University.'
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
- xr_1
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.02776v3.
sources:
- id: src_001
  type: paper
  title: 'XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations (arXiv)'
  url: https://arxiv.org/abs/2511.02776
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: XR-1 source
  url: https://doi.org/10.48550/arXiv.2511.02776
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent progress in large-scale robotic datasets and vision-language models (VLMs) has advanced research on vision-language-action (VLA) models. However, existing VLA models still face two fundamental challenges: (i) producing precise low-level actions from high-dimensional observations, (ii) bridging domain gaps across heterogeneous data sources, including diverse robot embodiments and human demonstrations. Existing methods often encode latent variables from either visual dynamics or robotic actions to guide policy learning, but they fail to fully exploit the complementary multi-modal knowledge present in large-scale, heterogeneous datasets. In this work, we present X Robotic Model 1 (XR-1), a novel framework for versatile and scalable VLA learning across diverse robots, tasks, and environments. XR-1 introduces the \emph{Unified Vision-Motion Codes (UVMC)}, a discrete latent representation learned via a dual-branch VQ-VAE that jointly encodes visual dynamics and robotic motion. UVMC addresses these challenges by (i) serving as an intermediate representation between the observations and actions, and (ii) aligning multimodal dynamic information from heterogeneous data sources to capture complementary knowledge. To effectively exploit UVMC, we propose a three-stage training paradigm: (i) self-supervised UVMC learning, (ii) UVMC-guided pretraining on large-scale cross-embodiment robotic datasets, and (iii) task-specific post-training. We validate XR-1 through extensive real-world experiments with more than 14,000 rollouts on six different robot embodiments, spanning over 120 diverse manipulation tasks. XR-1 consistently outperforms state-of-the-art baselines such as $π_{0.5}$, $π_0$, RDT, UniVLA, and GR00T-N1.5 while demonstrating strong generalization to novel objects, background variations, distractors, and illumination changes. Our project is at https://xr-1-vla.github.io/.

## 核心内容
Recent progress in large-scale robotic datasets and vision-language models (VLMs) has advanced research on vision-language-action (VLA) models. However, existing VLA models still face two fundamental challenges: (i) producing precise low-level actions from high-dimensional observations, (ii) bridging domain gaps across heterogeneous data sources, including diverse robot embodiments and human demonstrations. Existing methods often encode latent variables from either visual dynamics or robotic actions to guide policy learning, but they fail to fully exploit the complementary multi-modal knowledge present in large-scale, heterogeneous datasets. In this work, we present X Robotic Model 1 (XR-1), a novel framework for versatile and scalable VLA learning across diverse robots, tasks, and environments. XR-1 introduces the \emph{Unified Vision-Motion Codes (UVMC)}, a discrete latent representation learned via a dual-branch VQ-VAE that jointly encodes visual dynamics and robotic motion. UVMC addresses these challenges by (i) serving as an intermediate representation between the observations and actions, and (ii) aligning multimodal dynamic information from heterogeneous data sources to capture complementary knowledge. To effectively exploit UVMC, we propose a three-stage training paradigm: (i) self-supervised UVMC learning, (ii) UVMC-guided pretraining on large-scale cross-embodiment robotic datasets, and (iii) task-specific post-training. We validate XR-1 through extensive real-world experiments with more than 14,000 rollouts on six different robot embodiments, spanning over 120 diverse manipulation tasks. XR-1 consistently outperforms state-of-the-art baselines such as $π_{0.5}$, $π_0$, RDT, UniVLA, and GR00T-N1.5 while demonstrating strong generalization to novel objects, background variations, distractors, and illumination changes. Our project is at https://xr-1-vla.github.io/.

## 参考
- http://arxiv.org/abs/2511.02776v3

