---
$id: ent_paper_an_robotic_assistant_completing_c_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models'
  zh: Robotic Assistant
  ko: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models'
summary:
  en: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models (Robotic Assistant),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by ETH Zurich, MIT, Stanford University.'
  zh: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models (Robotic Assistant),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by ETH Zurich, MIT, Stanford University.'
  ko: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models (Robotic Assistant),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by ETH Zurich, MIT, Stanford University.'
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
- robotic_assistant
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.25713v1.
sources:
- id: src_001
  type: paper
  title: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2510.25713
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Robotic Assistant source
  url: https://doi.org/10.48550/arXiv.2510.25713
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We adapt a pre-trained Vision-Language-Action (VLA) model (Open-VLA) for dexterous human-robot collaboration with minimal language prompting. Our approach adds (i) FiLM conditioning to visual backbones for task-aware perception, (ii) an auxiliary intent head that predicts collaborator hand pose and target cues, and (iii) action-space post-processing that predicts compact deltas (position/rotation) and PCA-reduced finger joints before mapping to full commands. Using a multi-view, teleoperated Franka and Mimic-hand dataset augmented with MediaPipe hand poses, we demonstrate that delta actions are well-behaved and that four principal components explain ~96% of hand-joint variance. Ablations identify action post-processing as the primary performance driver; auxiliary intent helps, FiLM is mixed, and a directional motion loss is detrimental. A real-time stack (~0.3 s latency on one RTX 4090) composes "pick-up" and "pass" into a long-horizon behavior. We surface "trainer overfitting" to specific demonstrators as the key limitation.

## 核心内容
We adapt a pre-trained Vision-Language-Action (VLA) model (Open-VLA) for dexterous human-robot collaboration with minimal language prompting. Our approach adds (i) FiLM conditioning to visual backbones for task-aware perception, (ii) an auxiliary intent head that predicts collaborator hand pose and target cues, and (iii) action-space post-processing that predicts compact deltas (position/rotation) and PCA-reduced finger joints before mapping to full commands. Using a multi-view, teleoperated Franka and Mimic-hand dataset augmented with MediaPipe hand poses, we demonstrate that delta actions are well-behaved and that four principal components explain ~96% of hand-joint variance. Ablations identify action post-processing as the primary performance driver; auxiliary intent helps, FiLM is mixed, and a directional motion loss is detrimental. A real-time stack (~0.3 s latency on one RTX 4090) composes "pick-up" and "pass" into a long-horizon behavior. We surface "trainer overfitting" to specific demonstrators as the key limitation.

## 参考
- http://arxiv.org/abs/2510.25713v1

