---
$id: ent_paper_chen_see_once_then_act_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations'
  zh: ViVLA
  ko: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations'
summary:
  en: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations (ViVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Beijing Institute of Technology, LimX
    Dynamics.'
  zh: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations (ViVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Beijing Institute of Technology, LimX
    Dynamics.'
  ko: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations (ViVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Beijing Institute of Technology, LimX
    Dynamics.'
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
- vision_language_action
- vivla
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.07582v1.
sources:
- id: src_001
  type: paper
  title: 'See Once, Then Act: Vision-Language-Action Model with Task Learning from One-Shot Video Demonstrations (arXiv)'
  url: https://arxiv.org/abs/2512.07582
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ViVLA source
  url: https://doi.org/10.48550/arXiv.2512.07582
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Developing robust and general-purpose manipulation policies represents a fundamental objective in robotics research. While Vision-Language-Action (VLA) models have demonstrated promising capabilities for end-to-end robot control, existing approaches still exhibit limited generalization to tasks beyond their training distributions. In contrast, humans possess remarkable proficiency in acquiring novel skills by simply observing others performing them once. Inspired by this capability, we propose ViVLA, a generalist robotic manipulation policy that achieves efficient task learning from a single expert demonstration video at test time. Our approach jointly processes an expert demonstration video alongside the robot's visual observations to predict both the demonstrated action sequences and subsequent robot actions, effectively distilling fine-grained manipulation knowledge from expert behavior and transferring it seamlessly to the agent. To enhance the performance of ViVLA, we develop a scalable expert-agent pair data generation pipeline capable of synthesizing paired trajectories from easily accessible human videos, further augmented by curated pairs from publicly available datasets. This pipeline produces a total of 892,911 expert-agent samples for training ViVLA. Experimental results demonstrate that our ViVLA is able to acquire novel manipulation skills from only a single expert demonstration video at test time. Our approach achieves over 30% improvement on unseen LIBERO tasks and maintains above 35% gains with cross-embodiment videos. Real-world experiments demonstrate effective learning from human videos, yielding more than 38% improvement on unseen tasks.

## 核心内容
Developing robust and general-purpose manipulation policies represents a fundamental objective in robotics research. While Vision-Language-Action (VLA) models have demonstrated promising capabilities for end-to-end robot control, existing approaches still exhibit limited generalization to tasks beyond their training distributions. In contrast, humans possess remarkable proficiency in acquiring novel skills by simply observing others performing them once. Inspired by this capability, we propose ViVLA, a generalist robotic manipulation policy that achieves efficient task learning from a single expert demonstration video at test time. Our approach jointly processes an expert demonstration video alongside the robot's visual observations to predict both the demonstrated action sequences and subsequent robot actions, effectively distilling fine-grained manipulation knowledge from expert behavior and transferring it seamlessly to the agent. To enhance the performance of ViVLA, we develop a scalable expert-agent pair data generation pipeline capable of synthesizing paired trajectories from easily accessible human videos, further augmented by curated pairs from publicly available datasets. This pipeline produces a total of 892,911 expert-agent samples for training ViVLA. Experimental results demonstrate that our ViVLA is able to acquire novel manipulation skills from only a single expert demonstration video at test time. Our approach achieves over 30% improvement on unseen LIBERO tasks and maintains above 35% gains with cross-embodiment videos. Real-world experiments demonstrate effective learning from human videos, yielding more than 38% improvement on unseen tasks.

## 参考
- http://arxiv.org/abs/2512.07582v1

