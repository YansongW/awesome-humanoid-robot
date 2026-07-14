---
$id: ent_paper_li_urbanvla_a_vision_language_act_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility'
  zh: UrbanVLA
  ko: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility'
summary:
  en: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility (UrbanVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Galbot, USTC, BAAI.'
  zh: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility (UrbanVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Galbot, USTC, BAAI.'
  ko: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility (UrbanVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Galbot, USTC, BAAI.'
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
- robotic_manipulation
- urbanvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.23576v1.
sources:
- id: src_001
  type: paper
  title: 'UrbanVLA: A Vision-Language-Action Model for Urban Micromobility (arXiv)'
  url: https://arxiv.org/abs/2510.23576
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UrbanVLA source
  url: https://doi.org/10.48550/arXiv.2510.23576
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Urban micromobility applications, such as delivery robots, demand reliable navigation across large-scale urban environments while following long-horizon route instructions. This task is particularly challenging due to the dynamic and unstructured nature of real-world city areas, yet most existing navigation methods remain tailored to short-scale and controllable scenarios. Effective urban micromobility requires two complementary levels of navigation skills: low-level capabilities such as point-goal reaching and obstacle avoidance, and high-level capabilities, such as route-visual alignment. To this end, we propose UrbanVLA, a route-conditioned Vision-Language-Action (VLA) framework designed for scalable urban navigation. Our method explicitly aligns noisy route waypoints with visual observations during execution, and subsequently plans trajectories to drive the robot. To enable UrbanVLA to master both levels of navigation, we employ a two-stage training pipeline. The process begins with Supervised Fine-Tuning (SFT) using simulated environments and trajectories parsed from web videos. This is followed by Reinforcement Fine-Tuning (RFT) on a mixture of simulation and real-world data, which enhances the model's safety and adaptability in real-world settings. Experiments demonstrate that UrbanVLA surpasses strong baselines by more than 55% in the SocialNav task on MetaUrban. Furthermore, UrbanVLA achieves reliable real-world navigation, showcasing both scalability to large-scale urban environments and robustness against real-world uncertainties.

## 核心内容
Urban micromobility applications, such as delivery robots, demand reliable navigation across large-scale urban environments while following long-horizon route instructions. This task is particularly challenging due to the dynamic and unstructured nature of real-world city areas, yet most existing navigation methods remain tailored to short-scale and controllable scenarios. Effective urban micromobility requires two complementary levels of navigation skills: low-level capabilities such as point-goal reaching and obstacle avoidance, and high-level capabilities, such as route-visual alignment. To this end, we propose UrbanVLA, a route-conditioned Vision-Language-Action (VLA) framework designed for scalable urban navigation. Our method explicitly aligns noisy route waypoints with visual observations during execution, and subsequently plans trajectories to drive the robot. To enable UrbanVLA to master both levels of navigation, we employ a two-stage training pipeline. The process begins with Supervised Fine-Tuning (SFT) using simulated environments and trajectories parsed from web videos. This is followed by Reinforcement Fine-Tuning (RFT) on a mixture of simulation and real-world data, which enhances the model's safety and adaptability in real-world settings. Experiments demonstrate that UrbanVLA surpasses strong baselines by more than 55% in the SocialNav task on MetaUrban. Furthermore, UrbanVLA achieves reliable real-world navigation, showcasing both scalability to large-scale urban environments and robustness against real-world uncertainties.

## 参考
- http://arxiv.org/abs/2510.23576v1

