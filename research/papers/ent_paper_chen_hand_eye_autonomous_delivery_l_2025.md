---
$id: ent_paper_chen_hand_eye_autonomous_delivery_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and
    Reaching'
  zh: 手眼自主递送：学习人形机器人导航、移动与伸取
  ko: '손-눈 자율 배달: 휴머노이드 내비게이션, 보행 및 닿기 학습'
summary:
  en: Proposes Hand-Eye Autonomous Delivery (HEAD), a modular framework that decouples
    egocentric vision-based planning of head and hand targets from a low-level whole-body
    controller trained with GAN-like imitation reinforcement learning on large-scale
    human motion capture data, enabling sim-to-real navigation and reaching on a Unitree
    G1 humanoid.
  zh: 提出了手眼自主递送（HEAD）框架，将基于自我中心视觉的头部与双手目标规划，与通过类GAN模仿强化学习在大规模人体动作捕捉数据上训练的低层全身控制器解耦，并在Unitree
    G1人形机器人上实现了从仿真到现实的导航与伸取。
  ko: 손-눈 자율 배달(HEAD) 프레임워크를 제안한다. 자아중심 시각에 기반한 머리와 손 목표 계획을, 대규모 인체 동작 캡처 데이터로 GAN과
    유사한 모방 강화학습을 통해 학습된 저수준 전신 제어기와 분리하여, Unitree G1 휴머노이드에서 시뮬레이션-투-리얼 내비게이션과 닿기를
    실현한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the arXiv full text (v1/v2, 2025); factual claims and citations
    should be reviewed by a human before promotion to verified.
sources:
- id: src_001
  type: paper
  title: 'Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and
    Reaching'
  url: https://arxiv.org/abs/2508.03068
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

Hand-Eye Autonomous Delivery (HEAD) is a modular learning framework for humanoid robots that combines navigation, locomotion, and reaching. The system is built around a high-level policy that predicts 6D target poses for the robot's eyes and hands from egocentric vision, and a low-level whole-body controller that executes the corresponding full-body motions through PD servos. The high-level policy is divided into a navigation module and a reaching module: the navigation module guides the robot toward a target specified as a 2D point in the initial RGB image, while the reaching module takes over when the object enters a downward-facing RGB-D camera's view and is within arm's reach.

The low-level controller is trained to track three sparse key points—the eyes, left hand, and right hand—using large-scale human motion capture data. To imitate unstructured human motions while satisfying tracking objectives, the authors formulate a GAN-like reinforcement-learning framework with two separate discriminators for the upper and lower body. The observation space is restricted to onboard sensor data in the robot's local frame, avoiding reliance on privileged world-coordinate information such as root position and velocity. The navigation module is trained on a mixture of Aria Glasses recordings, the large-scale Aria Digital Twin dataset, and a small amount of robot-specific motion-capture data to mitigate domain shift due to both perception and embodiment gaps.

The complete system is deployed on a Unitree G1 robot equipped with a wide-angle USB webcam for navigation and an Intel RealSense D435 RGB-D camera for reaching, with all modules running on a PC with an RTX4090 GPU and an i9-14900K CPU. Experiments are conducted in a lab room and a kitchen room with unseen layouts and objects, achieving a 71% success rate in reaching objects placed at different locations and heights.

## Key Contributions

- A modular hand-eye autonomous delivery framework that decouples egocentric perception from physical whole-body control.
- A low-level whole-body controller trained with GAN-like imitation reinforcement learning to track sparse head and hand targets from unstructured human motion data.
- A navigation module that combines large-scale human data (Aria Digital Twin), in-environment human demonstrations collected with Aria Glasses, and small-scale robot data to mitigate domain shift.
- A complete sim-to-real system deployed on a Unitree G1 humanoid demonstrating navigation and reaching in real indoor environments.

## Relevance to Humanoid Robotics

The paper directly addresses the problem of deploying humanoid robots in human-designed indoor environments, where the robot must coordinate locomotion, navigation, and whole-body reaching to deliver its end-effectors and cameras to target objects. By learning from human motion and vision data and transferring to a real humanoid hardware platform, it provides a concrete, integrated pipeline that bridges perception, planning, and low-level control. This is highly relevant to real-world humanoid applications such as autonomous delivery and service robotics.
