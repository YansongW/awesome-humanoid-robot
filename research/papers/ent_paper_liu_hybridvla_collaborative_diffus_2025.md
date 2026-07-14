---
$id: ent_paper_liu_hybridvla_collaborative_diffus_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model'
  zh: HybridVLA
  ko: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model'
summary:
  en: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model (HybridVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Peking University, Beijing Academy of Artificial
    Intelligence (BAAI), CUHK.'
  zh: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model (HybridVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Peking University, Beijing Academy of Artificial
    Intelligence (BAAI), CUHK.'
  ko: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model (HybridVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Peking University, Beijing Academy of Artificial
    Intelligence (BAAI), CUHK.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hybridvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.10631v3.
sources:
- id: src_001
  type: paper
  title: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2503.10631
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: HybridVLA source
  url: https://doi.org/10.48550/arXiv.2503.10631
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
A fundamental objective of manipulation policy design is to endow robots to comprehend human instructions, reason about scene cues, and execute generalized actions in dynamic environments. Recent autoregressive vision-language-action (VLA) methods inherit common-sense reasoning capabilities from vision-language models (VLMs) for next action-token prediction. However, these methods quantize actions into discrete bins, which disrupts the continuity required for precise control. In contrast, existing diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions solely conditioned on feature representations extracted by the VLM, without fully leveraging the VLM's pretrained reasoning capabilities through token-level generation. To address these limitations, we introduce HybridVLA, a unified framework that absorbs the continuous nature of diffusion-based actions and the contextual reasoning of autoregression within a single large language model. To mitigate interference between the two generation paradigms, we propose a collaborative training recipe that seamlessly incorporates diffusion denoising into the next-token prediction process. With this recipe, we find these two action prediction methods not only reinforce each other but also exhibit varying strength across different tasks. Therefore, we design a collaborative action ensemble mechanism that adaptively fuses both predictions, leading to more robust control. HybridVLA outperforms previous state-of-the-art VLA methods by 14\% and 19\% in mean success rate on simulation and real-world tasks, respectively, while demonstrating stable manipulation in unseen configurations.

## 核心内容
A fundamental objective of manipulation policy design is to endow robots to comprehend human instructions, reason about scene cues, and execute generalized actions in dynamic environments. Recent autoregressive vision-language-action (VLA) methods inherit common-sense reasoning capabilities from vision-language models (VLMs) for next action-token prediction. However, these methods quantize actions into discrete bins, which disrupts the continuity required for precise control. In contrast, existing diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions solely conditioned on feature representations extracted by the VLM, without fully leveraging the VLM's pretrained reasoning capabilities through token-level generation. To address these limitations, we introduce HybridVLA, a unified framework that absorbs the continuous nature of diffusion-based actions and the contextual reasoning of autoregression within a single large language model. To mitigate interference between the two generation paradigms, we propose a collaborative training recipe that seamlessly incorporates diffusion denoising into the next-token prediction process. With this recipe, we find these two action prediction methods not only reinforce each other but also exhibit varying strength across different tasks. Therefore, we design a collaborative action ensemble mechanism that adaptively fuses both predictions, leading to more robust control. HybridVLA outperforms previous state-of-the-art VLA methods by 14\% and 19\% in mean success rate on simulation and real-world tasks, respectively, while demonstrating stable manipulation in unseen configurations.

## 参考
- http://arxiv.org/abs/2503.10631v3

