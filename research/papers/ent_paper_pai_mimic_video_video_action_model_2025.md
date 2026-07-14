---
$id: ent_paper_pai_mimic_video_video_action_model_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs'
  zh: VAM
  ko: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs'
summary:
  en: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (VAM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by mimic robotics, Microsoft Zurich, ETH Zurich, ETH AI Center, UC Berkeley.'
  zh: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (VAM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by mimic robotics, Microsoft Zurich, ETH Zurich, ETH AI Center, UC Berkeley.'
  ko: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (VAM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by mimic robotics, Microsoft Zurich, ETH Zurich, ETH AI Center, UC Berkeley.'
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
- vam
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.15692v2.
sources:
- id: src_001
  type: paper
  title: 'mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (arXiv)'
  url: https://arxiv.org/abs/2512.15692
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VAM source
  url: https://doi.org/10.48550/arXiv.2512.15692
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Prevailing Vision-Language-Action Models (VLAs) for robotic manipulation are built upon vision-language backbones pretrained on large-scale, but disconnected static web data. As a result, despite improved semantic generalization, the policy must implicitly infer complex physical dynamics and temporal dependencies solely from robot trajectories. This reliance creates an unsustainable data burden, necessitating continuous, large-scale expert data collection to compensate for the lack of innate physical understanding. We contend that while vision-language pretraining effectively captures semantic priors, it remains blind to physical causality. A more effective paradigm leverages video to jointly capture semantics and visual dynamics during pretraining, thereby isolating the remaining task of low-level control. To this end, we introduce mimic-video, a novel Video-Action Model (VAM) that pairs a pretrained Internet-scale video model with a flow matching-based action decoder conditioned on its latent representations. The decoder serves as an Inverse Dynamics Model (IDM), generating low-level robot actions from the latent representation of video-space action plans. Our extensive evaluation shows that our approach achieves state-of-the-art performance on simulated and real-world robotic manipulation tasks, improving sample efficiency by 10x and convergence speed by 2x compared to traditional VLA architectures.

## 核心内容
Prevailing Vision-Language-Action Models (VLAs) for robotic manipulation are built upon vision-language backbones pretrained on large-scale, but disconnected static web data. As a result, despite improved semantic generalization, the policy must implicitly infer complex physical dynamics and temporal dependencies solely from robot trajectories. This reliance creates an unsustainable data burden, necessitating continuous, large-scale expert data collection to compensate for the lack of innate physical understanding. We contend that while vision-language pretraining effectively captures semantic priors, it remains blind to physical causality. A more effective paradigm leverages video to jointly capture semantics and visual dynamics during pretraining, thereby isolating the remaining task of low-level control. To this end, we introduce mimic-video, a novel Video-Action Model (VAM) that pairs a pretrained Internet-scale video model with a flow matching-based action decoder conditioned on its latent representations. The decoder serves as an Inverse Dynamics Model (IDM), generating low-level robot actions from the latent representation of video-space action plans. Our extensive evaluation shows that our approach achieves state-of-the-art performance on simulated and real-world robotic manipulation tasks, improving sample efficiency by 10x and convergence speed by 2x compared to traditional VLA architectures.

## 参考
- http://arxiv.org/abs/2512.15692v2

