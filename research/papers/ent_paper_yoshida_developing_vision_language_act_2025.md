---
$id: ent_paper_yoshida_developing_vision_language_act_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Developing Vision-Language-Action Model from Egocentric Videos
  zh: Developing Vision-Language-Action Model from Egocentric Videos
  ko: Developing Vision-Language-Action Model from Egocentric Videos
summary:
  en: Developing Vision-Language-Action Model from Egocentric Videos (Developing Vision-Language-Action Model from Egocentric
    Videos), is a 2025 large vision-language-action model for robotic manipulation, introduced by Institute of Science Tokyo,
    NII LLMC, Sony Interactive Entertainment.
  zh: Developing Vision-Language-Action Model from Egocentric Videos (Developing Vision-Language-Action Model from Egocentric
    Videos), is a 2025 large vision-language-action model for robotic manipulation, introduced by Institute of Science Tokyo,
    NII LLMC, Sony Interactive Entertainment.
  ko: Developing Vision-Language-Action Model from Egocentric Videos (Developing Vision-Language-Action Model from Egocentric
    Videos), is a 2025 large vision-language-action model for robotic manipulation, introduced by Institute of Science Tokyo,
    NII LLMC, Sony Interactive Entertainment.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- developing_vision_language_act
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21986v1.
sources:
- id: src_001
  type: paper
  title: Developing Vision-Language-Action Model from Egocentric Videos (arXiv)
  url: https://arxiv.org/abs/2509.21986
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Developing Vision-Language-Action Model from Egocentric Videos source
  url: https://doi.org/10.48550/arXiv.2509.21986
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Egocentric videos capture how humans manipulate objects and tools, providing diverse motion cues for learning object manipulation. Unlike the costly, expert-driven manual teleoperation commonly used in training Vision-Language-Action models (VLAs), egocentric videos offer a scalable alternative. However, prior studies that leverage such videos for training robot policies typically rely on auxiliary annotations, such as detailed hand-pose recordings. Consequently, it remains unclear whether VLAs can be trained directly from raw egocentric videos. In this work, we address this challenge by leveraging EgoScaler, a framework that extracts 6DoF object manipulation trajectories from egocentric videos without requiring auxiliary recordings. We apply EgoScaler to four large-scale egocentric video datasets and automatically refine noisy or incomplete trajectories, thereby constructing a new large-scale dataset for VLA pre-training. Our experiments with a state-of-the-art $π_0$ architecture in both simulated and real-robot environments yield three key findings: (i) pre-training on our dataset improves task success rates by over 20\% compared to training from scratch, (ii) the performance is competitive with that achieved using real-robot datasets, and (iii) combining our dataset with real-robot data yields further improvements. These results demonstrate that egocentric videos constitute a promising and scalable resource for advancing VLA research.

## 核心内容
Egocentric videos capture how humans manipulate objects and tools, providing diverse motion cues for learning object manipulation. Unlike the costly, expert-driven manual teleoperation commonly used in training Vision-Language-Action models (VLAs), egocentric videos offer a scalable alternative. However, prior studies that leverage such videos for training robot policies typically rely on auxiliary annotations, such as detailed hand-pose recordings. Consequently, it remains unclear whether VLAs can be trained directly from raw egocentric videos. In this work, we address this challenge by leveraging EgoScaler, a framework that extracts 6DoF object manipulation trajectories from egocentric videos without requiring auxiliary recordings. We apply EgoScaler to four large-scale egocentric video datasets and automatically refine noisy or incomplete trajectories, thereby constructing a new large-scale dataset for VLA pre-training. Our experiments with a state-of-the-art $π_0$ architecture in both simulated and real-robot environments yield three key findings: (i) pre-training on our dataset improves task success rates by over 20\% compared to training from scratch, (ii) the performance is competitive with that achieved using real-robot datasets, and (iii) combining our dataset with real-robot data yields further improvements. These results demonstrate that egocentric videos constitute a promising and scalable resource for advancing VLA research.

## 参考
- http://arxiv.org/abs/2509.21986v1

