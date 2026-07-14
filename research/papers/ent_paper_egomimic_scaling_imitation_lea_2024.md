---
$id: ent_paper_egomimic_scaling_imitation_lea_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoMimic: Scaling Imitation Learning via Egocentric Video'
  zh: 'EgoMimic: Scaling Imitation Learning via Egocentric Video'
  ko: 'EgoMimic: Scaling Imitation Learning via Egocentric Video'
summary:
  en: 'EgoMimic: Scaling Imitation Learning via Egocentric Video is a 2024 work on manipulation for humanoid robots, with
    open-source code available.'
  zh: 'EgoMimic: Scaling Imitation Learning via Egocentric Video is a 2024 work on manipulation for humanoid robots, with
    open-source code available.'
  ko: 'EgoMimic: Scaling Imitation Learning via Egocentric Video is a 2024 work on manipulation for humanoid robots, with
    open-source code available.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egomimic
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.24221v1.
sources:
- id: src_001
  type: paper
  title: 'EgoMimic: Scaling Imitation Learning via Egocentric Video (arXiv)'
  url: https://arxiv.org/abs/2410.24221
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'EgoMimic: Scaling Imitation Learning via Egocentric Video project page'
  url: https://egomimic.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
The scale and diversity of demonstration data required for imitation learning is a significant challenge. We present EgoMimic, a full-stack framework which scales manipulation via human embodiment data, specifically egocentric human videos paired with 3D hand tracking. EgoMimic achieves this through: (1) a system to capture human embodiment data using the ergonomic Project Aria glasses, (2) a low-cost bimanual manipulator that minimizes the kinematic gap to human data, (3) cross-domain data alignment techniques, and (4) an imitation learning architecture that co-trains on human and robot data. Compared to prior works that only extract high-level intent from human videos, our approach treats human and robot data equally as embodied demonstration data and learns a unified policy from both data sources. EgoMimic achieves significant improvement on a diverse set of long-horizon, single-arm and bimanual manipulation tasks over state-of-the-art imitation learning methods and enables generalization to entirely new scenes. Finally, we show a favorable scaling trend for EgoMimic, where adding 1 hour of additional hand data is significantly more valuable than 1 hour of additional robot data. Videos and additional information can be found at https://egomimic.github.io/

## 核心内容
The scale and diversity of demonstration data required for imitation learning is a significant challenge. We present EgoMimic, a full-stack framework which scales manipulation via human embodiment data, specifically egocentric human videos paired with 3D hand tracking. EgoMimic achieves this through: (1) a system to capture human embodiment data using the ergonomic Project Aria glasses, (2) a low-cost bimanual manipulator that minimizes the kinematic gap to human data, (3) cross-domain data alignment techniques, and (4) an imitation learning architecture that co-trains on human and robot data. Compared to prior works that only extract high-level intent from human videos, our approach treats human and robot data equally as embodied demonstration data and learns a unified policy from both data sources. EgoMimic achieves significant improvement on a diverse set of long-horizon, single-arm and bimanual manipulation tasks over state-of-the-art imitation learning methods and enables generalization to entirely new scenes. Finally, we show a favorable scaling trend for EgoMimic, where adding 1 hour of additional hand data is significantly more valuable than 1 hour of additional robot data. Videos and additional information can be found at https://egomimic.github.io/

## 参考
- http://arxiv.org/abs/2410.24221v1

