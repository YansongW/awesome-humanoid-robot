---
$id: ent_paper_learning_humanoid_standing_up_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Standing-up Control across Diverse Postures
  zh: Learning Humanoid Standing-up Control across Diverse Postures
  ko: Learning Humanoid Standing-up Control across Diverse Postures
summary:
  en: Learning Humanoid Standing-up Control across Diverse Postures is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Learning Humanoid Standing-up Control across Diverse Postures is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Learning Humanoid Standing-up Control across Diverse Postures is a 2025 work on loco-manipulation and whole-body-control
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
- learning_humanoid_standing_up
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.08378v2.
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Standing-up Control across Diverse Postures (arXiv)
  url: https://arxiv.org/abs/2502.08378
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Standing-up control is crucial for humanoid robots, with the potential for integration into current locomotion and loco-manipulation systems, such as fall recovery. Existing approaches are either limited to simulations that overlook hardware constraints or rely on predefined ground-specific motion trajectories, failing to enable standing up across postures in real-world scenes. To bridge this gap, we present HoST (Humanoid Standing-up Control), a reinforcement learning framework that learns standing-up control from scratch, enabling robust sim-to-real transfer across diverse postures. HoST effectively learns posture-adaptive motions by leveraging a multi-critic architecture and curriculum-based training on diverse simulated terrains. To ensure successful real-world deployment, we constrain the motion with smoothness regularization and implicit motion speed bound to alleviate oscillatory and violent motions on physical hardware, respectively. After simulation-based training, the learned control policies are directly deployed on the Unitree G1 humanoid robot. Our experimental results demonstrate that the controllers achieve smooth, stable, and robust standing-up motions across a wide range of laboratory and outdoor environments. Videos and code are available at https://taohuang13.github.io/humanoid-standingup.github.io/.

## 核心内容
Standing-up control is crucial for humanoid robots, with the potential for integration into current locomotion and loco-manipulation systems, such as fall recovery. Existing approaches are either limited to simulations that overlook hardware constraints or rely on predefined ground-specific motion trajectories, failing to enable standing up across postures in real-world scenes. To bridge this gap, we present HoST (Humanoid Standing-up Control), a reinforcement learning framework that learns standing-up control from scratch, enabling robust sim-to-real transfer across diverse postures. HoST effectively learns posture-adaptive motions by leveraging a multi-critic architecture and curriculum-based training on diverse simulated terrains. To ensure successful real-world deployment, we constrain the motion with smoothness regularization and implicit motion speed bound to alleviate oscillatory and violent motions on physical hardware, respectively. After simulation-based training, the learned control policies are directly deployed on the Unitree G1 humanoid robot. Our experimental results demonstrate that the controllers achieve smooth, stable, and robust standing-up motions across a wide range of laboratory and outdoor environments. Videos and code are available at https://taohuang13.github.io/humanoid-standingup.github.io/.

## 参考
- http://arxiv.org/abs/2502.08378v2

