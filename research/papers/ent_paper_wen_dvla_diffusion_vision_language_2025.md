---
$id: ent_paper_wen_dvla_diffusion_vision_language_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought'
  zh: dVLA
  ko: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought'
summary:
  en: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought (dVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Shanghai Jiaotong University.'
  zh: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought (dVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Shanghai Jiaotong University.'
  ko: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought (dVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Shanghai Jiaotong University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.25681v1.
sources:
- id: src_001
  type: paper
  title: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought (arXiv)'
  url: https://arxiv.org/abs/2509.25681
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: dVLA source
  url: https://doi.org/10.48550/arXiv.2509.25681
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models are emerging as a next-generation paradigm for robotics. We introduce dVLA, a diffusion-based VLA that leverages a multimodal chain-of-thought to unify visual perception, language reasoning, and robotic control in a single system. dVLA jointly optimizes perception, language understanding, and action under a single diffusion objective, enabling stronger cross-modal reasoning and better generalization to novel instructions and objects. For practical deployment, we mitigate inference latency by incorporating two acceleration strategies, a prefix attention mask and KV caching, yielding up to around times speedup at test-time inference. We evaluate dVLA in both simulation and the real world: on the LIBERO benchmark, it achieves state-of-the-art performance with a 96.4% average success rate, consistently surpassing both discrete and continuous action policies; on a real Franka robot, it succeeds across a diverse task suite, including a challenging bin-picking task that requires multi-step planning, demonstrating robust real-world performance. Together, these results underscore the promise of unified diffusion frameworks for practical, high-performance VLA robotics.

## 核心内容
Vision-Language-Action (VLA) models are emerging as a next-generation paradigm for robotics. We introduce dVLA, a diffusion-based VLA that leverages a multimodal chain-of-thought to unify visual perception, language reasoning, and robotic control in a single system. dVLA jointly optimizes perception, language understanding, and action under a single diffusion objective, enabling stronger cross-modal reasoning and better generalization to novel instructions and objects. For practical deployment, we mitigate inference latency by incorporating two acceleration strategies, a prefix attention mask and KV caching, yielding up to around times speedup at test-time inference. We evaluate dVLA in both simulation and the real world: on the LIBERO benchmark, it achieves state-of-the-art performance with a 96.4% average success rate, consistently surpassing both discrete and continuous action policies; on a real Franka robot, it succeeds across a diverse task suite, including a challenging bin-picking task that requires multi-step planning, demonstrating robust real-world performance. Together, these results underscore the promise of unified diffusion frameworks for practical, high-performance VLA robotics.

## 参考
- http://arxiv.org/abs/2509.25681v1

