---
$id: ent_paper_yang_x_humanoid_robotize_human_vide_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale'
  zh: X-Humanoid
  ko: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale'
summary:
  en: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale (X-Humanoid), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NUS.'
  zh: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale (X-Humanoid), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NUS.'
  ko: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale (X-Humanoid), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NUS.'
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
- x_humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.04537v1.
sources:
- id: src_001
  type: paper
  title: 'X-Humanoid: Robotize Human Videos to Generate Humanoid Videos at Scale (arXiv)'
  url: https://arxiv.org/abs/2512.04537
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: X-Humanoid source
  url: https://doi.org/10.48550/arXiv.2512.04537
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The advancement of embodied AI has unlocked significant potential for intelligent humanoid robots. However, progress in both Vision-Language-Action (VLA) models and world models is severely hampered by the scarcity of large-scale, diverse training data. A promising solution is to "robotize" web-scale human videos, which has been proven effective for policy training. However, these solutions mainly "overlay" robot arms to egocentric videos, which cannot handle complex full-body motions and scene occlusions in third-person videos, making them unsuitable for robotizing humans. To bridge this gap, we introduce X-Humanoid, a generative video editing approach that adapts the powerful Wan 2.2 model into a video-to-video structure and finetunes it for the human-to-humanoid translation task. This finetuning requires paired human-humanoid videos, so we designed a scalable data creation pipeline, turning community assets into 17+ hours of paired synthetic videos using Unreal Engine. We then apply our trained model to 60 hours of the Ego-Exo4D videos, generating and releasing a new large-scale dataset of over 3.6 million "robotized" humanoid video frames. Quantitative analysis and user studies confirm our method's superiority over existing baselines: 69% of users rated it best for motion consistency, and 62.1% for embodiment correctness.

## 核心内容
The advancement of embodied AI has unlocked significant potential for intelligent humanoid robots. However, progress in both Vision-Language-Action (VLA) models and world models is severely hampered by the scarcity of large-scale, diverse training data. A promising solution is to "robotize" web-scale human videos, which has been proven effective for policy training. However, these solutions mainly "overlay" robot arms to egocentric videos, which cannot handle complex full-body motions and scene occlusions in third-person videos, making them unsuitable for robotizing humans. To bridge this gap, we introduce X-Humanoid, a generative video editing approach that adapts the powerful Wan 2.2 model into a video-to-video structure and finetunes it for the human-to-humanoid translation task. This finetuning requires paired human-humanoid videos, so we designed a scalable data creation pipeline, turning community assets into 17+ hours of paired synthetic videos using Unreal Engine. We then apply our trained model to 60 hours of the Ego-Exo4D videos, generating and releasing a new large-scale dataset of over 3.6 million "robotized" humanoid video frames. Quantitative analysis and user studies confirm our method's superiority over existing baselines: 69% of users rated it best for motion consistency, and 62.1% for embodiment correctness.

## 参考
- http://arxiv.org/abs/2512.04537v1

