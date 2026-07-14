---
$id: ent_paper_liu_what_can_rl_bring_to_vla_gener_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: What Can RL Bring to VLA Generalization? An Empirical Study
  zh: What Can RL Bring to VLA Generalization? An Empirical Study
  ko: What Can RL Bring to VLA Generalization? An Empirical Study
summary:
  en: What Can RL Bring to VLA Generalization? An Empirical Study (What Can RL Bring to VLA Generalization? An Empirical Study),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shenzhen International Graduate School,
    Tsinghua University, Institute for Interdisciplinary Information Sciences, Tsinghua University, Department of Electronic
    Engineering, Tsinghua University, and published at NIPS25.
  zh: What Can RL Bring to VLA Generalization? An Empirical Study (What Can RL Bring to VLA Generalization? An Empirical Study),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shenzhen International Graduate School,
    Tsinghua University, Institute for Interdisciplinary Information Sciences, Tsinghua University, Department of Electronic
    Engineering, Tsinghua University, and published at NIPS25.
  ko: What Can RL Bring to VLA Generalization? An Empirical Study (What Can RL Bring to VLA Generalization? An Empirical Study),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shenzhen International Graduate School,
    Tsinghua University, Institute for Interdisciplinary Information Sciences, Tsinghua University, Department of Electronic
    Engineering, Tsinghua University, and published at NIPS25.
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
- what_can_rl_bring_to_vla_gener
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.19789v4.
sources:
- id: src_001
  type: paper
  title: What Can RL Bring to VLA Generalization? An Empirical Study (arXiv)
  url: https://arxiv.org/abs/2505.19789
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: What Can RL Bring to VLA Generalization? An Empirical Study source
  url: https://doi.org/10.48550/arXiv.2505.19789
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Large Vision-Language Action (VLA) models have shown significant potential for embodied AI. However, their predominant training via supervised fine-tuning (SFT) limits generalization due to susceptibility to compounding errors under distribution shifts. Reinforcement learning (RL) offers a path to overcome these limitations by optimizing for task objectives via trial-and-error, yet a systematic understanding of its specific generalization benefits for VLAs compared to SFT is lacking. To address this, our study introduces a comprehensive benchmark for evaluating VLA generalization and systematically investigates the impact of RL fine-tuning across diverse visual, semantic, and execution dimensions. Our extensive experiments reveal that RL fine-tuning, particularly with PPO, significantly enhances generalization in semantic understanding and execution robustness over SFT, while maintaining comparable visual robustness. We identify PPO as a more effective RL algorithm for VLAs than LLM-derived methods like DPO and GRPO. We also develop a simple recipe for efficient PPO training on VLAs, and demonstrate its practical utility for improving VLA generalization. The project page is at https://rlvla.github.io

## 核心内容
Large Vision-Language Action (VLA) models have shown significant potential for embodied AI. However, their predominant training via supervised fine-tuning (SFT) limits generalization due to susceptibility to compounding errors under distribution shifts. Reinforcement learning (RL) offers a path to overcome these limitations by optimizing for task objectives via trial-and-error, yet a systematic understanding of its specific generalization benefits for VLAs compared to SFT is lacking. To address this, our study introduces a comprehensive benchmark for evaluating VLA generalization and systematically investigates the impact of RL fine-tuning across diverse visual, semantic, and execution dimensions. Our extensive experiments reveal that RL fine-tuning, particularly with PPO, significantly enhances generalization in semantic understanding and execution robustness over SFT, while maintaining comparable visual robustness. We identify PPO as a more effective RL algorithm for VLAs than LLM-derived methods like DPO and GRPO. We also develop a simple recipe for efficient PPO training on VLAs, and demonstrate its practical utility for improving VLA generalization. The project page is at https://rlvla.github.io

## 参考
- http://arxiv.org/abs/2505.19789v4

