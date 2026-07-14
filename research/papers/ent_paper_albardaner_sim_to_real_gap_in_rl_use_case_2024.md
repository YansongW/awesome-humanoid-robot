---
$id: ent_paper_albardaner_sim_to_real_gap_in_rl_use_case_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Sim-to-Real gap in RL: Use Case with TIAGo and Isaac Sim/Gym'
  zh: 强化学习中的仿真到现实差距：基于 TIAGo 与 Isaac Sim/Gym 的实例研究
  ko: 'RL의 시뮬레이션-현실 간격: TIAGo 및 Isaac Sim/Gym 활용 사례'
summary:
  en: This 2024 arXiv paper trains reinforcement-learning policies for the TIAGo mobile manipulator in Nvidia Isaac Gym and
    Isaac Sim, then quantifies joint-response differences and accumulated errors against the real robot to demonstrate sim-to-real
    transfer.
  zh: 这篇 2024 年 arXiv 论文在 Nvidia Isaac Gym 和 Isaac Sim 中为 TIAGo 移动操作机器人训练强化学习策略，并通过与真实机器人的关节响应差异和累积误差对比，展示仿真到现实的迁移效果。
  ko: 이 2024년 arXiv 논문은 Nvidia Isaac Gym과 Isaac Sim에서 TIAGo 이동 조작 로봇용 강화학습 정책을 학습한 후, 실제 로봇과의 관절 응답 차이 및 누적 오차를 정량화하여 시뮬레이션-현실
    전이를 입증한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- reinforcement_learning
- isaac_gym
- isaac_sim
- tiago
- mobile_manipulation
- physics_simulation
- control_architecture
- collision_avoidance
- ros
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.07091v2.
sources:
- id: src_001
  type: paper
  title: 'Sim-to-Real gap in RL: Use Case with TIAGo and Isaac Sim/Gym'
  url: https://arxiv.org/abs/2403.07091
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
This paper explores policy-learning approaches in the context of sim-to-real transfer for robotic manipulation using a TIAGo mobile manipulator, focusing on two state-of-art simulators, Isaac Gym and Isaac Sim, both developed by Nvidia. Control architectures are discussed, with a particular emphasis on achieving collision-less movement in both simulation and the real environment. Presented results demonstrate successful sim-to-real transfer, showcasing similar movements executed by an RL-trained model in both simulated and real setups.

## 核心内容
This paper explores policy-learning approaches in the context of sim-to-real transfer for robotic manipulation using a TIAGo mobile manipulator, focusing on two state-of-art simulators, Isaac Gym and Isaac Sim, both developed by Nvidia. Control architectures are discussed, with a particular emphasis on achieving collision-less movement in both simulation and the real environment. Presented results demonstrate successful sim-to-real transfer, showcasing similar movements executed by an RL-trained model in both simulated and real setups.

## 参考
- http://arxiv.org/abs/2403.07091v2

