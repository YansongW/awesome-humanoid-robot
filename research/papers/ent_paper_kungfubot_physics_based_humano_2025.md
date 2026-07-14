---
$id: ent_paper_kungfubot_physics_based_humano_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills'
  zh: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills'
  ko: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills'
summary:
  en: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- kungfubot
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.12851v3.
sources:
- id: src_001
  type: paper
  title: 'KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills (arXiv)'
  url: https://arxiv.org/abs/2506.12851
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots are promising to acquire various skills by imitating human behaviors. However, existing algorithms are only capable of tracking smooth, low-speed human motions, even with delicate reward and curriculum design. This paper presents a physics-based humanoid control framework, aiming to master highly-dynamic human behaviors such as Kungfu and dancing through multi-steps motion processing and adaptive motion tracking. For motion processing, we design a pipeline to extract, filter out, correct, and retarget motions, while ensuring compliance with physical constraints to the maximum extent. For motion imitation, we formulate a bi-level optimization problem to dynamically adjust the tracking accuracy tolerance based on the current tracking error, creating an adaptive curriculum mechanism. We further construct an asymmetric actor-critic framework for policy training. In experiments, we train whole-body control policies to imitate a set of highly-dynamic motions. Our method achieves significantly lower tracking errors than existing approaches and is successfully deployed on the Unitree G1 robot, demonstrating stable and expressive behaviors. The project page is https://kungfubot.github.io.

## 核心内容
Humanoid robots are promising to acquire various skills by imitating human behaviors. However, existing algorithms are only capable of tracking smooth, low-speed human motions, even with delicate reward and curriculum design. This paper presents a physics-based humanoid control framework, aiming to master highly-dynamic human behaviors such as Kungfu and dancing through multi-steps motion processing and adaptive motion tracking. For motion processing, we design a pipeline to extract, filter out, correct, and retarget motions, while ensuring compliance with physical constraints to the maximum extent. For motion imitation, we formulate a bi-level optimization problem to dynamically adjust the tracking accuracy tolerance based on the current tracking error, creating an adaptive curriculum mechanism. We further construct an asymmetric actor-critic framework for policy training. In experiments, we train whole-body control policies to imitate a set of highly-dynamic motions. Our method achieves significantly lower tracking errors than existing approaches and is successfully deployed on the Unitree G1 robot, demonstrating stable and expressive behaviors. The project page is https://kungfubot.github.io.

## 参考
- http://arxiv.org/abs/2506.12851v3

