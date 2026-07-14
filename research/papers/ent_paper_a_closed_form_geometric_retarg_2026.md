---
$id: ent_paper_a_closed_form_geometric_retarg_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation
  zh: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation
  ko: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation
summary:
  en: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation is a 2026 work on teleoperation
    for humanoid robots.
  zh: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation is a 2026 work on teleoperation
    for humanoid robots.
  ko: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation is a 2026 work on teleoperation
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
- a_closed_form_geometric_retarg
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.01632v1.
sources:
- id: src_001
  type: paper
  title: A Closed-Form Geometric Retargeting Solver for Upper Body Humanoid Robot Teleoperation (arXiv)
  url: https://arxiv.org/abs/2602.01632
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Retargeting human motion to robot poses is a practical approach for teleoperating bimanual humanoid robot arms, but existing methods can be suboptimal and slow, often causing undesirable motion or latency. This is due to optimizing to match robot end-effector to human hand position and orientation, which can also limit the robot's workspace to that of the human. Instead, this paper reframes retargeting as an orientation alignment problem, enabling a closed-form, geometric solution algorithm with an optimality guarantee. The key idea is to align a robot arm to a human's upper and lower arm orientations, as identified from shoulder, elbow, and wrist (SEW) keypoints; hence, the method is called SEW-Mimic. The method has fast inference (3 kHz) on standard commercial CPUs, leaving computational overhead for downstream applications; an example in this paper is a safety filter to avoid bimanual self-collision. The method suits most 7-degree-of-freedom robot arms and humanoids, and is agnostic to input keypoint source. Experiments show that SEW-Mimic outperforms other retargeting methods in computation time and accuracy. A pilot user study suggests that the method improves teleoperation task success. Preliminary analysis indicates that data collected with SEW-Mimic improves policy learning due to being smoother. SEW-Mimic is also shown to be a drop-in way to accelerate full-body humanoid retargeting. Finally, hardware demonstrations illustrate SEW-Mimic's practicality. The results emphasize the utility of SEW-Mimic as a fundamental building block for bimanual robot manipulation and humanoid robot teleoperation.

## 核心内容
Retargeting human motion to robot poses is a practical approach for teleoperating bimanual humanoid robot arms, but existing methods can be suboptimal and slow, often causing undesirable motion or latency. This is due to optimizing to match robot end-effector to human hand position and orientation, which can also limit the robot's workspace to that of the human. Instead, this paper reframes retargeting as an orientation alignment problem, enabling a closed-form, geometric solution algorithm with an optimality guarantee. The key idea is to align a robot arm to a human's upper and lower arm orientations, as identified from shoulder, elbow, and wrist (SEW) keypoints; hence, the method is called SEW-Mimic. The method has fast inference (3 kHz) on standard commercial CPUs, leaving computational overhead for downstream applications; an example in this paper is a safety filter to avoid bimanual self-collision. The method suits most 7-degree-of-freedom robot arms and humanoids, and is agnostic to input keypoint source. Experiments show that SEW-Mimic outperforms other retargeting methods in computation time and accuracy. A pilot user study suggests that the method improves teleoperation task success. Preliminary analysis indicates that data collected with SEW-Mimic improves policy learning due to being smoother. SEW-Mimic is also shown to be a drop-in way to accelerate full-body humanoid retargeting. Finally, hardware demonstrations illustrate SEW-Mimic's practicality. The results emphasize the utility of SEW-Mimic as a fundamental building block for bimanual robot manipulation and humanoid robot teleoperation.

## 参考
- http://arxiv.org/abs/2602.01632v1

