---
$id: ent_paper_one_shot_humanoid_whole_body_m_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: One-shot Humanoid Whole-body Motion Learning
  zh: One-shot Humanoid Whole-body Motion Learning
  ko: One-shot Humanoid Whole-body Motion Learning
summary:
  en: One-shot Humanoid Whole-body Motion Learning is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.
  zh: One-shot Humanoid Whole-body Motion Learning is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.
  ko: One-shot Humanoid Whole-body Motion Learning is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.
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
- loco_manipulation
- one_shot_humanoid_whole_body_m
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.25241v2.
sources:
- id: src_001
  type: paper
  title: One-shot Humanoid Whole-body Motion Learning (arXiv)
  url: https://arxiv.org/abs/2510.25241
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Whole-body humanoid motion represents a fundamental challenge in robotics, requiring balance, coordination, and adaptability to enable human-like behaviors. However, existing methods typically require multiple training samples per motion, rendering the collection of high-quality human motion datasets both labor-intensive and costly. To address this, we propose a data-efficient adaptation approach that learns a new humanoid motion from a single non-walking target sample together with auxiliary walking motions and a walking-trained base model. The core idea lies in leveraging order-preserving optimal transport to compute distances between walking and non-walking sequences, followed by interpolation along geodesics to generate new intermediate pose skeletons, which are then optimized for collision-free configurations and retargeted to the humanoid before integration into a simulated environment for policy adaptation via reinforcement learning. Experimental evaluations on the CMU MoCap dataset demonstrate that our method consistently outperforms baselines, achieving superior performance across metrics. Our code is available at: https://github.com/hhuang-code/One-shot-WBM.

## 核心内容
Whole-body humanoid motion represents a fundamental challenge in robotics, requiring balance, coordination, and adaptability to enable human-like behaviors. However, existing methods typically require multiple training samples per motion, rendering the collection of high-quality human motion datasets both labor-intensive and costly. To address this, we propose a data-efficient adaptation approach that learns a new humanoid motion from a single non-walking target sample together with auxiliary walking motions and a walking-trained base model. The core idea lies in leveraging order-preserving optimal transport to compute distances between walking and non-walking sequences, followed by interpolation along geodesics to generate new intermediate pose skeletons, which are then optimized for collision-free configurations and retargeted to the humanoid before integration into a simulated environment for policy adaptation via reinforcement learning. Experimental evaluations on the CMU MoCap dataset demonstrate that our method consistently outperforms baselines, achieving superior performance across metrics. Our code is available at: https://github.com/hhuang-code/One-shot-WBM.

## 参考
- http://arxiv.org/abs/2510.25241v2

