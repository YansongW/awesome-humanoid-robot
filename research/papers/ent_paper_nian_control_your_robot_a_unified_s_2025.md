---
$id: ent_paper_nian_control_your_robot_a_unified_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Control Your Robot: A Unified System for Robot Control and Policy Deployment'
  zh: Control Your Robot
  ko: 'Control Your Robot: A Unified System for Robot Control and Policy Deployment'
summary:
  en: 'Control Your Robot: A Unified System for Robot Control and Policy Deployment (Control Your Robot), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by ScaleLab, Shanghai Jiao Tong University, University
    of Shanghai for Science and Technology, Lumina Group.'
  zh: 'Control Your Robot: A Unified System for Robot Control and Policy Deployment (Control Your Robot), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by ScaleLab, Shanghai Jiao Tong University, University
    of Shanghai for Science and Technology, Lumina Group.'
  ko: 'Control Your Robot: A Unified System for Robot Control and Policy Deployment (Control Your Robot), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by ScaleLab, Shanghai Jiao Tong University, University
    of Shanghai for Science and Technology, Lumina Group.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- control_your_robot
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.23823v2.
sources:
- id: src_001
  type: paper
  title: 'Control Your Robot: A Unified System for Robot Control and Policy Deployment (arXiv)'
  url: https://arxiv.org/abs/2509.23823
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Control Your Robot source
  url: https://doi.org/10.48550/arXiv.2509.23823
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Cross-platform robot control remains difficult because hardware interfaces, data formats, and control paradigms vary widely, which fragments toolchains and slows deployment. To address this, we present Control Your Robot, a modular, general-purpose framework that unifies data collection and policy deployment across diverse platforms. The system reduces fragmentation through a standardized workflow with modular design, unified APIs, and a closed-loop architecture. It supports flexible robot registration, dual-mode control with teleoperation and trajectory playback, and seamless integration from multimodal data acquisition to inference. Experiments on single-arm and dual-arm systems show efficient, low-latency data collection and effective support for policy learning with imitation learning and vision-language-action models. Policies trained on data gathered by Control Your Robot match expert demonstrations closely, indicating that the framework enables scalable and reproducible robot learning across platforms.

## 核心内容
Cross-platform robot control remains difficult because hardware interfaces, data formats, and control paradigms vary widely, which fragments toolchains and slows deployment. To address this, we present Control Your Robot, a modular, general-purpose framework that unifies data collection and policy deployment across diverse platforms. The system reduces fragmentation through a standardized workflow with modular design, unified APIs, and a closed-loop architecture. It supports flexible robot registration, dual-mode control with teleoperation and trajectory playback, and seamless integration from multimodal data acquisition to inference. Experiments on single-arm and dual-arm systems show efficient, low-latency data collection and effective support for policy learning with imitation learning and vision-language-action models. Policies trained on data gathered by Control Your Robot match expert demonstrations closely, indicating that the framework enables scalable and reproducible robot learning across platforms.

## 参考
- http://arxiv.org/abs/2509.23823v2

