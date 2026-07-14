---
$id: ent_paper_ace_a_cross_platform_visual_ex_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation'
  zh: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation'
  ko: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation'
summary:
  en: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation is a 2024 work on manipulation
    for humanoid robots, with open-source code available.'
  zh: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation is a 2024 work on manipulation
    for humanoid robots, with open-source code available.'
  ko: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation is a 2024 work on manipulation
    for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ace
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.11805v1.
sources:
- id: src_001
  type: paper
  title: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation (arXiv)'
  url: https://arxiv.org/abs/2408.11805
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ACE: A Cross-Platform Visual-Exoskeletons System for Low-Cost Dexterous Teleoperation project page'
  url: https://ace-teleop.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Learning from demonstrations has shown to be an effective approach to robotic manipulation, especially with the recently collected large-scale robot data with teleoperation systems. Building an efficient teleoperation system across diverse robot platforms has become more crucial than ever. However, there is a notable lack of cost-effective and user-friendly teleoperation systems for different end-effectors, e.g., anthropomorphic robot hands and grippers, that can operate across multiple platforms. To address this issue, we develop ACE, a cross-platform visual-exoskeleton system for low-cost dexterous teleoperation. Our system utilizes a hand-facing camera to capture 3D hand poses and an exoskeleton mounted on a portable base, enabling accurate real-time capture of both finger and wrist poses. Compared to previous systems, which often require hardware customization according to different robots, our single system can generalize to humanoid hands, arm-hands, arm-gripper, and quadruped-gripper systems with high-precision teleoperation. This enables imitation learning for complex manipulation tasks on diverse platforms.

## 核心内容
Learning from demonstrations has shown to be an effective approach to robotic manipulation, especially with the recently collected large-scale robot data with teleoperation systems. Building an efficient teleoperation system across diverse robot platforms has become more crucial than ever. However, there is a notable lack of cost-effective and user-friendly teleoperation systems for different end-effectors, e.g., anthropomorphic robot hands and grippers, that can operate across multiple platforms. To address this issue, we develop ACE, a cross-platform visual-exoskeleton system for low-cost dexterous teleoperation. Our system utilizes a hand-facing camera to capture 3D hand poses and an exoskeleton mounted on a portable base, enabling accurate real-time capture of both finger and wrist poses. Compared to previous systems, which often require hardware customization according to different robots, our single system can generalize to humanoid hands, arm-hands, arm-gripper, and quadruped-gripper systems with high-precision teleoperation. This enables imitation learning for complex manipulation tasks on diverse platforms.

## 参考
- http://arxiv.org/abs/2408.11805v1

