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
  en: SONIC trains a scalable physics-based whole-body humanoid controller by scaling model size, motion-capture dataset volume,
    and compute for motion tracking, and demonstrates real-world deployment on Unitree G1 via teleoperation, interactive kinematic
    planning, and VLA-driven loco-manipulation.
  zh: SONIC 通过扩大模型规模、动作捕捉数据量和计算资源来训练可扩展的基于物理的人形全身运动跟踪策略，并在 Unitree G1 上验证了远程操作、实时运动学规划与视觉-语言-动作驱动的移动操作。
  ko: SONIC은 모델 크기, 모션 캡처 데이터 규모, 연산량을 확장하여 물리 기반 휴머노이드 전신 모션 트래킹 정책을 학습하고, Unitree G1에서 원격 조작, 실시간 운동학 계획 및 VLA 기반 로코 매니퓰레이션을
    실증한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.07820v3.
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
## 概述
Despite the rise of billion-parameter foundation models trained across thousands of GPUs, similar scaling gains have not been shown for humanoid control. Current neural controllers for humanoids remain modest in size, target a limited set of behaviors, and are trained on a handful of GPUs. We show that scaling model capacity, data, and compute yields a generalist humanoid controller capable of natural, robust whole-body movements. We position motion tracking as a scalable task for humanoid control, leveraging dense supervision from diverse motion-capture data to acquire human motion priors without manual reward engineering. We build a foundation model for motion tracking by scaling along three axes: network size (1.2M to 42M parameters), dataset volume (100M+ frames from 700 hours of motion capture), and compute (21k GPU hours). Beyond demonstrating the benefits of scale, we further show downstream utility through: (1) a real-time kinematic planner bridging motion tracking to tasks such as navigation, enabling natural and interactive control, and (2) a unified token space supporting VR teleoperation and vision-language-action (VLA) models with a single policy. Through this interface, we demonstrate autonomous VLA-driven whole-body loco-manipulation requiring coordinated hand and foot placement. Scaling motion tracking exhibits favorable properties: performance improves steadily with compute and data diversity, and learned policies generalize to unseen motions, establishing motion tracking at scale as a practical foundation for humanoid control.

## 核心内容
Despite the rise of billion-parameter foundation models trained across thousands of GPUs, similar scaling gains have not been shown for humanoid control. Current neural controllers for humanoids remain modest in size, target a limited set of behaviors, and are trained on a handful of GPUs. We show that scaling model capacity, data, and compute yields a generalist humanoid controller capable of natural, robust whole-body movements. We position motion tracking as a scalable task for humanoid control, leveraging dense supervision from diverse motion-capture data to acquire human motion priors without manual reward engineering. We build a foundation model for motion tracking by scaling along three axes: network size (1.2M to 42M parameters), dataset volume (100M+ frames from 700 hours of motion capture), and compute (21k GPU hours). Beyond demonstrating the benefits of scale, we further show downstream utility through: (1) a real-time kinematic planner bridging motion tracking to tasks such as navigation, enabling natural and interactive control, and (2) a unified token space supporting VR teleoperation and vision-language-action (VLA) models with a single policy. Through this interface, we demonstrate autonomous VLA-driven whole-body loco-manipulation requiring coordinated hand and foot placement. Scaling motion tracking exhibits favorable properties: performance improves steadily with compute and data diversity, and learned policies generalize to unseen motions, establishing motion tracking at scale as a practical foundation for humanoid control.

## 参考
- http://arxiv.org/abs/2511.07820v3

