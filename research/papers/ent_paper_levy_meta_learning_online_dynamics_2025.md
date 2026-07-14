---
$id: ent_paper_levy_meta_learning_online_dynamics_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving
  zh: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving
  ko: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving
summary:
  en: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving (Meta-Learning Online Dynamics Model Adaptation
    in Off-Road Autonomous Driving), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Jet Propulsion Laboratory, California Institute of Technology, University of Texas at Austin, Georgia Institute of Technology,
    and published at RSS25.
  zh: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving (Meta-Learning Online Dynamics Model Adaptation
    in Off-Road Autonomous Driving), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Jet Propulsion Laboratory, California Institute of Technology, University of Texas at Austin, Georgia Institute of Technology,
    and published at RSS25.
  ko: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving (Meta-Learning Online Dynamics Model Adaptation
    in Off-Road Autonomous Driving), is a 2025 large vision-language-action model for robotic manipulation, introduced by
    Jet Propulsion Laboratory, California Institute of Technology, University of Texas at Austin, Georgia Institute of Technology,
    and published at RSS25.
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
- meta_learning_online_dynamics
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.16923v1.
sources:
- id: src_001
  type: paper
  title: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving (arXiv)
  url: https://arxiv.org/abs/2504.16923
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Meta-Learning Online Dynamics Model Adaptation in Off-Road Autonomous Driving source
  url: https://doi.org/10.48550/arXiv.2504.16923
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
High-speed off-road autonomous driving presents unique challenges due to complex, evolving terrain characteristics and the difficulty of accurately modeling terrain-vehicle interactions. While dynamics models used in model-based control can be learned from real-world data, they often struggle to generalize to unseen terrain, making real-time adaptation essential. We propose a novel framework that combines a Kalman filter-based online adaptation scheme with meta-learned parameters to address these challenges. Offline meta-learning optimizes the basis functions along which adaptation occurs, as well as the adaptation parameters, while online adaptation dynamically adjusts the onboard dynamics model in real time for model-based control. We validate our approach through extensive experiments, including real-world testing on a full-scale autonomous off-road vehicle, demonstrating that our method outperforms baseline approaches in prediction accuracy, performance, and safety metrics, particularly in safety-critical scenarios. Our results underscore the effectiveness of meta-learned dynamics model adaptation, advancing the development of reliable autonomous systems capable of navigating diverse and unseen environments. Video is available at: https://youtu.be/cCKHHrDRQEA

## 核心内容
High-speed off-road autonomous driving presents unique challenges due to complex, evolving terrain characteristics and the difficulty of accurately modeling terrain-vehicle interactions. While dynamics models used in model-based control can be learned from real-world data, they often struggle to generalize to unseen terrain, making real-time adaptation essential. We propose a novel framework that combines a Kalman filter-based online adaptation scheme with meta-learned parameters to address these challenges. Offline meta-learning optimizes the basis functions along which adaptation occurs, as well as the adaptation parameters, while online adaptation dynamically adjusts the onboard dynamics model in real time for model-based control. We validate our approach through extensive experiments, including real-world testing on a full-scale autonomous off-road vehicle, demonstrating that our method outperforms baseline approaches in prediction accuracy, performance, and safety metrics, particularly in safety-critical scenarios. Our results underscore the effectiveness of meta-learned dynamics model adaptation, advancing the development of reliable autonomous systems capable of navigating diverse and unseen environments. Video is available at: https://youtu.be/cCKHHrDRQEA

## 参考
- http://arxiv.org/abs/2504.16923v1

