---
$id: ent_paper_chen_hand_eye_autonomous_delivery_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and Reaching'
  zh: 手眼自主递送：学习人形机器人导航、移动与伸取
  ko: '손-눈 자율 배달: 휴머노이드 내비게이션, 보행 및 닿기 학습'
summary:
  en: Proposes Hand-Eye Autonomous Delivery (HEAD), a modular framework that decouples egocentric vision-based planning of
    head and hand targets from a low-level whole-body controller trained with GAN-like imitation reinforcement learning on
    large-scale human motion capture data, enabling sim-to-real navigation and reaching on a Unitree G1 humanoid.
  zh: 提出了手眼自主递送（HEAD）框架，将基于自我中心视觉的头部与双手目标规划，与通过类GAN模仿强化学习在大规模人体动作捕捉数据上训练的低层全身控制器解耦，并在Unitree G1人形机器人上实现了从仿真到现实的导航与伸取。
  ko: 손-눈 자율 배달(HEAD) 프레임워크를 제안한다. 자아중심 시각에 기반한 머리와 손 목표 계획을, 대규모 인체 동작 캡처 데이터로 GAN과 유사한 모방 강화학습을 통해 학습된 저수준 전신 제어기와 분리하여,
    Unitree G1 휴머노이드에서 시뮬레이션-투-리얼 내비게이션과 닿기를 실현한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 08_software_middleware
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- hand_eye_delivery
- modular_policy
- whole_body_control
- imitation_learning
- gan_based_rl
- sim_to_real
- navigation_and_reaching
- egocentric_vision
- unitree_g1
- aria_glasses
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.03068v2.
sources:
- id: src_001
  type: paper
  title: 'Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and Reaching'
  url: https://arxiv.org/abs/2508.03068
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
We propose Hand-Eye Autonomous Delivery (HEAD), a framework that learns navigation, locomotion, and reaching skills for humanoids, directly from human motion and vision perception data. We take a modular approach where the high-level planner commands the target position and orientation of the hands and eyes of the humanoid, delivered by the low-level policy that controls the whole-body movements. Specifically, the low-level whole-body controller learns to track the three points (eyes, left hand, and right hand) from existing large-scale human motion capture data while high-level policy learns from human data collected by Aria glasses. Our modular approach decouples the ego-centric vision perception from physical actions, promoting efficient learning and scalability to novel scenes. We evaluate our method both in simulation and in the real-world, demonstrating humanoid's capabilities to navigate and reach in complex environments designed for humans.

## 核心内容
We propose Hand-Eye Autonomous Delivery (HEAD), a framework that learns navigation, locomotion, and reaching skills for humanoids, directly from human motion and vision perception data. We take a modular approach where the high-level planner commands the target position and orientation of the hands and eyes of the humanoid, delivered by the low-level policy that controls the whole-body movements. Specifically, the low-level whole-body controller learns to track the three points (eyes, left hand, and right hand) from existing large-scale human motion capture data while high-level policy learns from human data collected by Aria glasses. Our modular approach decouples the ego-centric vision perception from physical actions, promoting efficient learning and scalability to novel scenes. We evaluate our method both in simulation and in the real-world, demonstrating humanoid's capabilities to navigate and reach in complex environments designed for humans.

## 参考
- http://arxiv.org/abs/2508.03068v2

