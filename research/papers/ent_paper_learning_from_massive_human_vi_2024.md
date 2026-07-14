---
$id: ent_paper_learning_from_massive_human_vi_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning from Massive Human Videos for Universal Humanoid Pose Control
  zh: Learning from Massive Human Videos for Universal Humanoid Pose Control
  ko: Learning from Massive Human Videos for Universal Humanoid Pose Control
summary:
  en: Learning from Massive Human Videos for Universal Humanoid Pose Control is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Learning from Massive Human Videos for Universal Humanoid Pose Control is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Learning from Massive Human Videos for Universal Humanoid Pose Control is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
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
- learning_from_massive_human_vi
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.14172v1.
sources:
- id: src_001
  type: paper
  title: Learning from Massive Human Videos for Universal Humanoid Pose Control (arXiv)
  url: https://arxiv.org/abs/2412.14172
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Learning from Massive Human Videos for Universal Humanoid Pose Control project page
  url: https://usc-gvl.github.io/UH-1/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Scalable learning of humanoid robots is crucial for their deployment in real-world applications. While traditional approaches primarily rely on reinforcement learning or teleoperation to achieve whole-body control, they are often limited by the diversity of simulated environments and the high costs of demonstration collection. In contrast, human videos are ubiquitous and present an untapped source of semantic and motion information that could significantly enhance the generalization capabilities of humanoid robots. This paper introduces Humanoid-X, a large-scale dataset of over 20 million humanoid robot poses with corresponding text-based motion descriptions, designed to leverage this abundant data. Humanoid-X is curated through a comprehensive pipeline: data mining from the Internet, video caption generation, motion retargeting of humans to humanoid robots, and policy learning for real-world deployment. With Humanoid-X, we further train a large humanoid model, UH-1, which takes text instructions as input and outputs corresponding actions to control a humanoid robot. Extensive simulated and real-world experiments validate that our scalable training approach leads to superior generalization in text-based humanoid control, marking a significant step toward adaptable, real-world-ready humanoid robots.

## 核心内容
Scalable learning of humanoid robots is crucial for their deployment in real-world applications. While traditional approaches primarily rely on reinforcement learning or teleoperation to achieve whole-body control, they are often limited by the diversity of simulated environments and the high costs of demonstration collection. In contrast, human videos are ubiquitous and present an untapped source of semantic and motion information that could significantly enhance the generalization capabilities of humanoid robots. This paper introduces Humanoid-X, a large-scale dataset of over 20 million humanoid robot poses with corresponding text-based motion descriptions, designed to leverage this abundant data. Humanoid-X is curated through a comprehensive pipeline: data mining from the Internet, video caption generation, motion retargeting of humans to humanoid robots, and policy learning for real-world deployment. With Humanoid-X, we further train a large humanoid model, UH-1, which takes text instructions as input and outputs corresponding actions to control a humanoid robot. Extensive simulated and real-world experiments validate that our scalable training approach leads to superior generalization in text-based humanoid control, marking a significant step toward adaptable, real-world-ready humanoid robots.

## 参考
- http://arxiv.org/abs/2412.14172v1

