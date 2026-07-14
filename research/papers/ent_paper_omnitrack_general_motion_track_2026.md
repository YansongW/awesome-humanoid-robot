---
$id: ent_paper_omnitrack_general_motion_track_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniTrack: General Motion Tracking via Physics-Consistent Reference'
  zh: 不要让控制器追踪错误参考
  ko: 'OmniTrack: General Motion Tracking via Physics-Consistent Reference'
summary:
  en: 'OmniTrack: General Motion Tracking via Physics-Consistent Reference is a knowledge node related to paper in the humanoid
    robot value chain.'
  zh: Learning motion tracking from rich human motion data is a foundational task for achieving general control in humanoid
    robots, enabling them to perform diverse behaviors. However, discrepancies in morphology and dynamics between humans and
    robots, combined with data noise, introduce physically infeasible artifacts in reference motions, such as floating and
    penetration. During both training and execution, these artifacts create a conflict between following inaccurate reference
    motions and maintaining the robot's stability, hindering the development of a generalizable motion tracking policy. To
    address these challenges, we introduce OmniTrack, a general tracking framework that explicitly decouples physical feasibility
    from general motion tracking. In the first stage, a privileged generalist p
  ko: 'OmniTrack: General Motion Tracking via Physics-Consistent Reference is a knowledge node related to paper in the humanoid
    robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- behavioral_foundation_model
- imitation_learning
- motion_tracker
- motion_tracking
- physics_based_control
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.23832v1.
sources:
- id: src_001
  type: paper
  title: 'OmniTrack: General Motion Tracking via Physics-Consistent Reference (arXiv)'
  url: https://arxiv.org/abs/2602.23832
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 不要让控制器追踪错误参考 project page
  url: https://omnitrack-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Learning motion tracking from rich human motion data is a foundational task for achieving general control in humanoid robots, enabling them to perform diverse behaviors. However, discrepancies in morphology and dynamics between humans and robots, combined with data noise, introduce physically infeasible artifacts in reference motions, such as floating and penetration. During both training and execution, these artifacts create a conflict between following inaccurate reference motions and maintaining the robot's stability, hindering the development of a generalizable motion tracking policy. To address these challenges, we introduce OmniTrack, a general tracking framework that explicitly decouples physical feasibility from general motion tracking. In the first stage, a privileged generalist policy generates physically plausible motions that strictly adhere to the robot's dynamics via trajectory rollout in simulation. In the second stage, the general control policy is trained to track these physically feasible motions, ensuring stable and coherent control transfer to the real robot. Experiments show that OmniTrack improves tracking accuracy and demonstrates strong generalization to unseen motions. In real-world tests, OmniTrack achieves hour-long, consistent, and stable tracking, including complex acrobatic motions such as flips and cartwheels. Additionally, we show that OmniTrack supports human-style stable and dynamic online teleoperation, highlighting its robustness and adaptability to varying user inputs.

## 核心内容
Learning motion tracking from rich human motion data is a foundational task for achieving general control in humanoid robots, enabling them to perform diverse behaviors. However, discrepancies in morphology and dynamics between humans and robots, combined with data noise, introduce physically infeasible artifacts in reference motions, such as floating and penetration. During both training and execution, these artifacts create a conflict between following inaccurate reference motions and maintaining the robot's stability, hindering the development of a generalizable motion tracking policy. To address these challenges, we introduce OmniTrack, a general tracking framework that explicitly decouples physical feasibility from general motion tracking. In the first stage, a privileged generalist policy generates physically plausible motions that strictly adhere to the robot's dynamics via trajectory rollout in simulation. In the second stage, the general control policy is trained to track these physically feasible motions, ensuring stable and coherent control transfer to the real robot. Experiments show that OmniTrack improves tracking accuracy and demonstrates strong generalization to unseen motions. In real-world tests, OmniTrack achieves hour-long, consistent, and stable tracking, including complex acrobatic motions such as flips and cartwheels. Additionally, we show that OmniTrack supports human-style stable and dynamic online teleoperation, highlighting its robustness and adaptability to varying user inputs.

## 参考
- http://arxiv.org/abs/2602.23832v1

