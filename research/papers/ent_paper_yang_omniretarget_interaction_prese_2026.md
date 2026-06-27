---
$id: ent_paper_yang_omniretarget_interaction_prese_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body
    Loco-Manipulation and Scene Interaction'
  zh: OmniRetarget：面向人形全身移动操作与场景交互的交互保持型数据生成
  ko: 'OmniRetarget: 휴머노이드 전신 이동 조작 및 장면 상호작용을 위한 상호작용 보존 데이터 생성'
summary:
  en: OmniRetarget is an open-source human-to-humanoid motion retargeting engine that
    preserves spatial and contact relationships between a robot, objects, and terrain
    via an interaction mesh, and solves a per-frame constrained optimization with
    a sequential SOCP/SQP-style solver to generate kinematically feasible reference
    trajectories for reinforcement learning.
  zh: OmniRetarget 是一个开源的人到人形机器人动作重定向引擎，通过交互网格保持机器人、物体与地形之间的空间及接触关系，并采用序列 SOCP/SQP
    式求解器进行逐帧约束优化，从而为强化学习生成运动学可行的参考轨迹。
  ko: OmniRetarget는 상호작용 메시를 통해 로봇, 물체, 지형 간 공간 및 접촉 관계를 보존하고 순차 SOCP/SQP 스타일 최적화
    기반 프레임별 제약 최적화를 해결하여 강화학습을 위한 운동학적으로 가능한 기준 궤적을 생성하는 오픈소스 인간-휴머노이드 동작 리타기팅 엔진이다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from arXiv full text (v3, 2509.26633); requires human review
    before verification.
sources:
- id: src_001
  type: paper
  title: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body
    Loco-Manipulation and Scene Interaction'
  url: https://arxiv.org/abs/2509.26633
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

OmniRetarget is a data-generation engine that converts human demonstrations into diverse, kinematically feasible reference trajectories for humanoid whole-body control. It explicitly models spatial and contact relationships between the robot body, manipulated objects, and terrain using an interaction mesh constructed via Delaunay tetrahedralization over key joints and sampled object/environment points. The retargeting objective minimizes the Laplacian deformation energy between the source human mesh and the target robot mesh, while hard kinematic constraints—collision avoidance, joint and velocity limits, and foot-skating prevention—are enforced through a sequential Second-Order Cone Program (SOCP) / SQP-style solver that is warm-started from the previous frame to improve temporal consistency.

A key feature of the framework is systematic data augmentation: a single human demonstration can be expanded into many variations by perturbing object pose, shape, and terrain geometry, and by retargeting to different robot embodiments. The paper demonstrates this cross-embodiment capability on Unitree G1, H1, and Booster T1, and supports robot-object interactions from OMOMO, robot-terrain interactions from an in-house MoCap dataset, and robot-only motions from LAFAN1. The resulting high-quality references enable a minimal downstream RL formulation with only five reward terms, four robot domain-randomization terms, and a purely proprioceptive observation space, all shared across tasks without task-specific reward tuning or learning curricula.

The authors comprehensively evaluate OmniRetarget against PHC, GMR, VideoMimic, the Unitree LAFAN1 Retargeting Dataset, and IMMA, measuring penetration, foot skating, contact preservation, and downstream RL success rates. The generated dataset totals over eight hours of retargeted motion (2.78 hours from OMOMO, one hour from in-house MoCap, and 4.6 hours from LAFAN1) and is planned for open-source release.

## Key Contributions

- First interaction-preserving humanoid retargeting framework that jointly handles robot-object-terrain interactions while enforcing hard physical constraints such as foot sticking, non-penetration, and joint/velocity limits.
- Systematic augmentation pipeline that transforms one human demonstration into diverse, high-quality kinematic trajectories across different object configurations, terrain shapes, and robot embodiments.
- Large-scale, open-source dataset of retargeted, kinematically feasible loco-manipulation trajectories derived from OMOMO, LAFAN1, and an in-house MoCap dataset.
- Zero-shot sim-to-real transfer of proprioceptive RL policies on a physical Unitree G1 humanoid for agile scene-interaction tasks including box carrying, platform climbing, slope crawling, and a 30-second parkour sequence.

## Relevance to Humanoid Robotics

OmniRetarget directly addresses the data bottleneck that constrains mass production and deployment of capable humanoid robots. By generating clean, interaction-aware kinematic references from existing human motion data, it reduces the need for expensive teleoperation or tedious per-task reward engineering. The minimal RL formulation trains solely on proprioceptive state and a small, shared reward set, yet achieves long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a real Unitree G1, demonstrating a practical path from human demonstration to real-world agile humanoid behavior.
