---
$id: ent_paper_emp_executable_motion_prior_fo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation'
  zh: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation'
  ko: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation'
summary:
  en: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation is a 2025 work on loco-manipulation
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
- emp
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.15649v1.
sources:
- id: src_001
  type: paper
  title: 'EMP: Executable Motion Prior for Humanoid Robot Standing Upper-body Motion Imitation (arXiv)'
  url: https://arxiv.org/abs/2507.15649
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
To support humanoid robots in performing manipulation tasks, it is essential to study stable standing while accommodating upper-body motions. However, the limited controllable range of humanoid robots in a standing position affects the stability of the entire body. Thus we introduce a reinforcement learning based framework for humanoid robots to imitate human upper-body motions while maintaining overall stability. Our approach begins with designing a retargeting network that generates a large-scale upper-body motion dataset for training the reinforcement learning (RL) policy, which enables the humanoid robot to track upper-body motion targets, employing domain randomization for enhanced robustness. To avoid exceeding the robot's execution capability and ensure safety and stability, we propose an Executable Motion Prior (EMP) module, which adjusts the input target movements based on the robot's current state. This adjustment improves standing stability while minimizing changes to motion amplitude. We evaluate our framework through simulation and real-world tests, demonstrating its practical applicability.

## 核心内容
To support humanoid robots in performing manipulation tasks, it is essential to study stable standing while accommodating upper-body motions. However, the limited controllable range of humanoid robots in a standing position affects the stability of the entire body. Thus we introduce a reinforcement learning based framework for humanoid robots to imitate human upper-body motions while maintaining overall stability. Our approach begins with designing a retargeting network that generates a large-scale upper-body motion dataset for training the reinforcement learning (RL) policy, which enables the humanoid robot to track upper-body motion targets, employing domain randomization for enhanced robustness. To avoid exceeding the robot's execution capability and ensure safety and stability, we propose an Executable Motion Prior (EMP) module, which adjusts the input target movements based on the robot's current state. This adjustment improves standing stability while minimizing changes to motion amplitude. We evaluate our framework through simulation and real-world tests, demonstrating its practical applicability.

## 参考
- http://arxiv.org/abs/2507.15649v1

