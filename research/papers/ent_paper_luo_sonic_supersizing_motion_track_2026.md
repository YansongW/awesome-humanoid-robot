---
$id: ent_paper_luo_sonic_supersizing_motion_track_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control'
  zh: SONIC：通过超大规模运动跟踪实现自然人形全身控制
  ko: 'SONIC: 자연스러운 휴머노이드 전신 제어를 위한 모션 트래킹 초대규모 확장'
summary:
  en: SONIC trains a scalable physics-based whole-body humanoid controller by scaling
    model size, motion-capture dataset volume, and compute for motion tracking, and
    demonstrates real-world deployment on Unitree G1 via teleoperation, interactive
    kinematic planning, and VLA-driven loco-manipulation.
  zh: SONIC 通过扩大模型规模、动作捕捉数据量和计算资源来训练可扩展的基于物理的人形全身运动跟踪策略，并在 Unitree G1 上验证了远程操作、实时运动学规划与视觉-语言-动作驱动的移动操作。
  ko: SONIC은 모델 크기, 모션 캡처 데이터 규모, 연산량을 확장하여 물리 기반 휴머노이드 전신 모션 트래킹 정책을 학습하고, Unitree
    G1에서 원격 조작, 실시간 운동학 계획 및 VLA 기반 로코 매니퓰레이션을 실증한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 09_data_datasets
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vla
- motion_tracking
- whole_body_control
- ppo
- foundation_model
- sim_to_real
- unitree_g1
- teleoperation
- loco_manipulation
- mocap
- finite_scalar_quantization
- kinematic_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review of
    the full paper before verification.
sources:
- id: src_001
  type: paper
  title: 'SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control'
  url: https://arxiv.org/abs/2511.07820
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
related_entities:
- id: ent_robot_system_unitree_g1
  relationship: uses
  description:
    en: Deploys the learned whole-body control policy on the Unitree G1 humanoid.
    zh: 在 Unitree G1 人形机器人上部署学习到的全身控制策略。
    ko: 학습된 전신 제어 정책을 Unitree G1 휴머노이드에 배포한다.
---

## Overview

SONIC frames large-scale motion tracking as a foundation task for humanoid control and trains a single universal policy by scaling network capacity from 1.2M to 42M parameters, dataset volume to more than 100 million motion frames (derived from over 700 hours of motion capture), and total compute to roughly 21,000 GPU hours. The training objective is pure physics-based motion tracking via proximal policy optimization (PPO), which replaces hand-engineered per-task rewards with dense supervision from diverse motion-capture data. The resulting policy supports whole-body tracking of robot, human, and hybrid motion representations in a shared finite scalar quantization (FSQ) token space. To bridge tracking and downstream tasks, the authors introduce a real-time kinematic motion generator that produces trackable reference motions for navigation and other interactive commands. They further show that the same tokenized policy can be driven by VR teleoperation inputs and by vision-language-action (VLA) models, enabling autonomous whole-body loco-manipulation that coordinates hand and foot placement.

## Key Contributions

- Identifies motion tracking as a scalable foundational task for humanoid control and demonstrates favorable scaling laws with compute and data diversity.
- Scales humanoid control training to 21,000 GPU hours and 100+ million motion frames, achieving a universal whole-body tracking policy.
- Introduces a real-time kinematic motion generator for interactive control and a universal token space with specialized robot, human, and hybrid encoders.
- Demonstrates zero-shot generalization to unseen motions, robust sim-to-real transfer to Unitree G1, and VLA-driven whole-body loco-manipulation.

## Relevance to Humanoid Robotics

SONIC is directly relevant to industrial humanoid deployment because it moves beyond small, behavior-specific controllers toward a single generalist policy capable of natural whole-body movement. Real-world experiments on the Unitree G1, using an onboard Jetson Orin and a PICO VR teleoperation kit, show that the approach can be deployed on existing hardware and interfaced with high-level task specifications via VLA models. The combination of scalable motion tracking, real-time planning, and a unified token interface provides a practical foundation for interactive and autonomous humanoid control in applications such as navigation and loco-manipulation.
