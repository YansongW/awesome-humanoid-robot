---
$id: ent_paper_unified_video_action_model_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Video Action Model
  zh: Unified Video Action Model
  ko: Unified Video Action Model
summary:
  en: Unified Video Action Model is a 2025 work on manipulation for humanoid robots.
  zh: A unified video and action model holds significant promise for robotics, where videos provide rich scene information
    for action prediction, and actions provide dynamics information for video prediction. However, effectively combining video
    generation and action prediction remains challenging, and current video generation-based methods struggle to match the
    performance of direct policy learning in action accuracy and inference speed. To bridge this gap, we introduce the Unified
    Video Action model (UVA), which jointly optimizes video and action predictions to achieve both high accuracy and effic
  ko: Unified Video Action Model is a 2025 work on manipulation for humanoid robots.
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
- manipulation
- unified_video_action_model
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.00200v3.
sources:
- id: src_001
  type: paper
  title: Unified Video Action Model (arXiv)
  url: https://arxiv.org/abs/2503.00200
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Unified Video Action Model project page
  url: https://unified-video-action-model.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---

## 概述
A unified video and action model holds significant promise for robotics, where videos provide rich scene information for action prediction, and actions provide dynamics information for video prediction. However, effectively combining video generation and action prediction remains challenging, and current video generation-based methods struggle to match the performance of direct policy learning in action accuracy and inference speed. To bridge this gap, we introduce the Unified Video Action model (UVA), which jointly optimizes video and action predictions to achieve both high accuracy and efficient action inference. The key lies in learning a joint video-action latent representation and decoupling video-action decoding. The joint latent representation bridges the visual and action domains, effectively modeling the relationship between video and action sequences. Meanwhile, the decoupled decoding, powered by two lightweight diffusion heads, enables high-speed action inference by bypassing video generation during inference. Such a unified framework further enables versatile functionality through masked input training. By selectively masking actions or videos, a single model can tackle diverse tasks beyond policy learning, such as forward and inverse dynamics modeling and video generation. Via an extensive set of experiments, we demonstrate that UVA can serve as a general-purpose solution for a wide range of robotics tasks, such as policy learning, forward/inverse dynamics and video observation prediction, without compromising performance compared to methods tailored for specific applications. Results are best viewed on https://unified-video-action-model.github.io/.

## 核心内容
A unified video and action model holds significant promise for robotics, where videos provide rich scene information for action prediction, and actions provide dynamics information for video prediction. However, effectively combining video generation and action prediction remains challenging, and current video generation-based methods struggle to match the performance of direct policy learning in action accuracy and inference speed. To bridge this gap, we introduce the Unified Video Action model (UVA), which jointly optimizes video and action predictions to achieve both high accuracy and efficient action inference. The key lies in learning a joint video-action latent representation and decoupling video-action decoding. The joint latent representation bridges the visual and action domains, effectively modeling the relationship between video and action sequences. Meanwhile, the decoupled decoding, powered by two lightweight diffusion heads, enables high-speed action inference by bypassing video generation during inference. Such a unified framework further enables versatile functionality through masked input training. By selectively masking actions or videos, a single model can tackle diverse tasks beyond policy learning, such as forward and inverse dynamics modeling and video generation. Via an extensive set of experiments, we demonstrate that UVA can serve as a general-purpose solution for a wide range of robotics tasks, such as policy learning, forward/inverse dynamics and video observation prediction, without compromising performance compared to methods tailored for specific applications. Results are best viewed on https://unified-video-action-model.github.io/.

## 参考
- http://arxiv.org/abs/2503.00200v3


