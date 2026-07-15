---
$id: ent_paper_goyal_rvt_robotic_view_transformer_f_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RVT: Robotic View Transformer for 3D Object Manipulation'
  zh: RVT
  ko: 'RVT: Robotic View Transformer for 3D Object Manipulation'
summary:
  en: 'RVT: Robotic View Transformer for 3D Object Manipulation (RVT), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by NVIDIA, and published at CoRL 2023.'
  zh: 'RVT: Robotic View Transformer for 3D Object Manipulation (RVT), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by NVIDIA, and published at CoRL 2023.'
  ko: 'RVT: Robotic View Transformer for 3D Object Manipulation (RVT), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by NVIDIA, and published at CoRL 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- rvt
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.14896v1.
sources:
- id: src_001
  type: paper
  title: RVT source
  url: https://proceedings.mlr.press/v229/goyal23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
For 3D object manipulation, methods that build an explicit 3D representation perform better than those relying only on camera images. But using explicit 3D representations like voxels comes at large computing cost, adversely affecting scalability. In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate. Some key features of RVT are an attention mechanism to aggregate information across views and re-rendering of the camera input from virtual views around the robot workspace. In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations, achieving 26% higher relative success than the existing state-of-the-art method (PerAct). It also trains 36X faster than PerAct for achieving the same performance and achieves 2.3X the inference speed of PerAct. Further, RVT can perform a variety of manipulation tasks in the real world with just a few ($\sim$10) demonstrations per task. Visual results, code, and trained model are provided at https://robotic-view-transformer.github.io/.

## 核心内容
For 3D object manipulation, methods that build an explicit 3D representation perform better than those relying only on camera images. But using explicit 3D representations like voxels comes at large computing cost, adversely affecting scalability. In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate. Some key features of RVT are an attention mechanism to aggregate information across views and re-rendering of the camera input from virtual views around the robot workspace. In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations, achieving 26% higher relative success than the existing state-of-the-art method (PerAct). It also trains 36X faster than PerAct for achieving the same performance and achieves 2.3X the inference speed of PerAct. Further, RVT can perform a variety of manipulation tasks in the real world with just a few ($\sim$10) demonstrations per task. Visual results, code, and trained model are provided at https://robotic-view-transformer.github.io/.

## 参考
- http://arxiv.org/abs/2306.14896v1

