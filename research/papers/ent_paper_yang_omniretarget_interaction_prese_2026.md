---
$id: ent_paper_yang_omniretarget_interaction_prese_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction'
  zh: OmniRetarget：面向人形全身移动操作与场景交互的交互保持型数据生成
  ko: 'OmniRetarget: 휴머노이드 전신 이동 조작 및 장면 상호작용을 위한 상호작용 보존 데이터 생성'
summary:
  en: OmniRetarget is an open-source human-to-humanoid motion retargeting engine that preserves spatial and contact relationships
    between a robot, objects, and terrain via an interaction mesh, and solves a per-frame constrained optimization with a
    sequential SOCP/SQP-style solver to generate kinematically feasible reference trajectories for reinforcement learning.
  zh: OmniRetarget 是一个开源的人到人形机器人动作重定向引擎，通过交互网格保持机器人、物体与地形之间的空间及接触关系，并采用序列 SOCP/SQP 式求解器进行逐帧约束优化，从而为强化学习生成运动学可行的参考轨迹。
  ko: OmniRetarget는 상호작용 메시를 통해 로봇, 물체, 지형 간 공간 및 접촉 관계를 보존하고 순차 SOCP/SQP 스타일 최적화 기반 프레임별 제약 최적화를 해결하여 강화학습을 위한 운동학적으로 가능한
    기준 궤적을 생성하는 오픈소스 인간-휴머노이드 동작 리타기팅 엔진이다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 10_evaluation_benchmarks
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- motion_retargeting
- loco_manipulation
- whole_body_control
- reinforcement_learning
- sim_to_real
- interaction_mesh
- laplacian_deformation
- sequential_socp
- data_augmentation
- parkour
- proprioceptive_policy
- humanoid_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.26633v3.
sources:
- id: src_001
  type: paper
  title: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction'
  url: https://arxiv.org/abs/2509.26633
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration. More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OmniRetarget generates kinematically feasible trajectories. Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations. We comprehensively evaluate OmniRetarget by retargeting motions from OMOMO, LAFAN1, and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

## 核心内容
A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration. More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OmniRetarget generates kinematically feasible trajectories. Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations. We comprehensively evaluate OmniRetarget by retargeting motions from OMOMO, LAFAN1, and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

## 参考
- http://arxiv.org/abs/2509.26633v3

