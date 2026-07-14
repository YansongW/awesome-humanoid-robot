---
$id: ent_paper_embracing_bulky_objects_with_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning'
  zh: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning'
  ko: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning'
summary:
  en: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embracing_bulky_objects_with_h
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.13534v1.
sources:
- id: src_001
  type: paper
  title: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2509.13534
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Whole-body manipulation (WBM) for humanoid robots presents a promising approach for executing embracing tasks involving bulky objects, where traditional grasping relying on end-effectors only remains limited in such scenarios due to inherent stability and payload constraints. This paper introduces a reinforcement learning framework that integrates a pre-trained human motion prior with a neural signed distance field (NSDF) representation to achieve robust whole-body embracing. Our method leverages a teacher-student architecture to distill large-scale human motion data, generating kinematically natural and physically feasible whole-body motion patterns. This facilitates coordinated control across the arms and torso, enabling stable multi-contact interactions that enhance the robustness in manipulation and also the load capacity. The embedded NSDF further provides accurate and continuous geometric perception, improving contact awareness throughout long-horizon tasks. We thoroughly evaluate the approach through comprehensive simulations and real-world experiments. The results demonstrate improved adaptability to diverse shapes and sizes of objects and also successful sim-to-real transfer. These indicate that the proposed framework offers an effective and practical solution for multi-contact and long-horizon WBM tasks of humanoid robots.

## 核心内容
Whole-body manipulation (WBM) for humanoid robots presents a promising approach for executing embracing tasks involving bulky objects, where traditional grasping relying on end-effectors only remains limited in such scenarios due to inherent stability and payload constraints. This paper introduces a reinforcement learning framework that integrates a pre-trained human motion prior with a neural signed distance field (NSDF) representation to achieve robust whole-body embracing. Our method leverages a teacher-student architecture to distill large-scale human motion data, generating kinematically natural and physically feasible whole-body motion patterns. This facilitates coordinated control across the arms and torso, enabling stable multi-contact interactions that enhance the robustness in manipulation and also the load capacity. The embedded NSDF further provides accurate and continuous geometric perception, improving contact awareness throughout long-horizon tasks. We thoroughly evaluate the approach through comprehensive simulations and real-world experiments. The results demonstrate improved adaptability to diverse shapes and sizes of objects and also successful sim-to-real transfer. These indicate that the proposed framework offers an effective and practical solution for multi-contact and long-horizon WBM tasks of humanoid robots.

## 参考
- http://arxiv.org/abs/2509.13534v1

