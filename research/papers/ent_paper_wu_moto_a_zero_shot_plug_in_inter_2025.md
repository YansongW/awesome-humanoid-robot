---
$id: ent_paper_wu_moto_a_zero_shot_plug_in_inter_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation'
  zh: MoTo
  ko: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation'
summary:
  en: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation (MoTo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Key Laboratory of Embodied Intelligence Systems, Beijing National
    Research Center for Information Science and Technology, School of Electrical and Electronic Engineering, Nanyang Technological
    University, School of IEA, Beijing University of Posts and Telecommunications, Department of Automation, Tsinghua University,
    and published at CoRL25.'
  zh: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation (MoTo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Key Laboratory of Embodied Intelligence Systems, Beijing National
    Research Center for Information Science and Technology, School of Electrical and Electronic Engineering, Nanyang Technological
    University, School of IEA, Beijing University of Posts and Telecommunications, Department of Automation, Tsinghua University,
    and published at CoRL25.'
  ko: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation (MoTo), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing Key Laboratory of Embodied Intelligence Systems, Beijing National
    Research Center for Information Science and Technology, School of Electrical and Electronic Engineering, Nanyang Technological
    University, School of IEA, Beijing University of Posts and Telecommunications, Department of Automation, Tsinghua University,
    and published at CoRL25.'
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
- moto
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.01658v1.
sources:
- id: src_001
  type: paper
  title: 'MoTo: A Zero-shot Plug-in Interaction-aware Navigation for General Mobile Manipulation (arXiv)'
  url: https://arxiv.org/abs/2509.01658
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MoTo source
  url: https://doi.org/10.48550/arXiv.2509.01658
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Mobile manipulation stands as a core challenge in robotics, enabling robots to assist humans across varied tasks and dynamic daily environments. Conventional mobile manipulation approaches often struggle to generalize across different tasks and environments due to the lack of large-scale training. However, recent advances in manipulation foundation models demonstrate impressive generalization capability on a wide range of fixed-base manipulation tasks, which are still limited to a fixed setting. Therefore, we devise a plug-in module named MoTo, which can be combined with any off-the-shelf manipulation foundation model to empower them with mobile manipulation ability. Specifically, we propose an interaction-aware navigation policy to generate robot docking points for generalized mobile manipulation. To enable zero-shot ability, we propose an interaction keypoints framework via vision-language models (VLM) under multi-view consistency for both target object and robotic arm following instructions, where fixed-base manipulation foundation models can be employed. We further propose motion planning objectives for the mobile base and robot arm, which minimize the distance between the two keypoints and maintain the physical feasibility of trajectories. In this way, MoTo guides the robot to move to the docking points where fixed-base manipulation can be successfully performed, and leverages VLM generation and trajectory optimization to achieve mobile manipulation in a zero-shot manner, without any requirement on mobile manipulation expert data. Extensive experimental results on OVMM and real-world demonstrate that MoTo achieves success rates of 2.68% and 16.67% higher than the state-of-the-art mobile manipulation methods, respectively, without requiring additional training data.

## 核心内容
Mobile manipulation stands as a core challenge in robotics, enabling robots to assist humans across varied tasks and dynamic daily environments. Conventional mobile manipulation approaches often struggle to generalize across different tasks and environments due to the lack of large-scale training. However, recent advances in manipulation foundation models demonstrate impressive generalization capability on a wide range of fixed-base manipulation tasks, which are still limited to a fixed setting. Therefore, we devise a plug-in module named MoTo, which can be combined with any off-the-shelf manipulation foundation model to empower them with mobile manipulation ability. Specifically, we propose an interaction-aware navigation policy to generate robot docking points for generalized mobile manipulation. To enable zero-shot ability, we propose an interaction keypoints framework via vision-language models (VLM) under multi-view consistency for both target object and robotic arm following instructions, where fixed-base manipulation foundation models can be employed. We further propose motion planning objectives for the mobile base and robot arm, which minimize the distance between the two keypoints and maintain the physical feasibility of trajectories. In this way, MoTo guides the robot to move to the docking points where fixed-base manipulation can be successfully performed, and leverages VLM generation and trajectory optimization to achieve mobile manipulation in a zero-shot manner, without any requirement on mobile manipulation expert data. Extensive experimental results on OVMM and real-world demonstrate that MoTo achieves success rates of 2.68% and 16.67% higher than the state-of-the-art mobile manipulation methods, respectively, without requiring additional training data.

## 参考
- http://arxiv.org/abs/2509.01658v1

