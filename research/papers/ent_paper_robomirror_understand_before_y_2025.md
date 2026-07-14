---
$id: ent_paper_robomirror_understand_before_y_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion'
  zh: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion'
  ko: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion'
summary:
  en: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion is a 2025 work on locomotion for humanoid
    robots.'
  zh: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion is a 2025 work on locomotion for humanoid
    robots.'
  ko: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion is a 2025 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- robomirror
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.23649v3.
sources:
- id: src_001
  type: paper
  title: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2512.23649
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humans learn locomotion through visual observation, interpreting visual content first before imitating actions. However, state-of-the-art humanoid locomotion systems rely on either curated motion capture trajectories or sparse text commands, leaving a critical gap between visual understanding and control. Text-to-motion methods suffer from semantic sparsity and staged pipeline errors, while video-based approaches only perform mechanical pose mimicry without genuine visual understanding. We propose RoboMirror, the first retargeting-free video-to-locomotion framework embodying "understand before you imitate". Leveraging VLMs, it distills raw egocentric/third-person videos into visual motion intents, which directly condition a diffusion-based policy to generate physically plausible, semantically aligned locomotion without explicit pose reconstruction or retargeting. Extensive experiments validate the effectiveness of RoboMirror, it enables telepresence via egocentric videos, drastically reduces third-person control latency by 80%, and achieves a 3.7% higher task success rate than baselines. By reframing humanoid control around video understanding, we bridge the visual understanding and action gap.

## 核心内容
Humans learn locomotion through visual observation, interpreting visual content first before imitating actions. However, state-of-the-art humanoid locomotion systems rely on either curated motion capture trajectories or sparse text commands, leaving a critical gap between visual understanding and control. Text-to-motion methods suffer from semantic sparsity and staged pipeline errors, while video-based approaches only perform mechanical pose mimicry without genuine visual understanding. We propose RoboMirror, the first retargeting-free video-to-locomotion framework embodying "understand before you imitate". Leveraging VLMs, it distills raw egocentric/third-person videos into visual motion intents, which directly condition a diffusion-based policy to generate physically plausible, semantically aligned locomotion without explicit pose reconstruction or retargeting. Extensive experiments validate the effectiveness of RoboMirror, it enables telepresence via egocentric videos, drastically reduces third-person control latency by 80%, and achieves a 3.7% higher task success rate than baselines. By reframing humanoid control around video understanding, we bridge the visual understanding and action gap.

## 参考
- http://arxiv.org/abs/2512.23649v3

