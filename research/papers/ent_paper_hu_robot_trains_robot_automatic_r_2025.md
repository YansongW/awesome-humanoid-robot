---
$id: ent_paper_hu_robot_trains_robot_automatic_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for
    Humanoids'
  zh: 机器人训练机器人：人形机器人的自动现实世界策略适应与学习
  ko: '로봇이 로봇을 훈련시킨다: 휴머노이드를 위한 자동 실제 세계 정책 적응 및 학습'
summary:
  en: This paper proposes Robot-Trains-Robot (RTR), a framework in which a robot-arm
    teacher supports and guides a humanoid student through compliant contact, curriculum
    scheduling, perturbations, failure detection, and automatic resets, enabling efficient
    real-world reinforcement learning with minimal human intervention. The authors
    also introduce a dynamics-aware latent-optimization pipeline using FiLM layers
    and domain randomization to stabilize sim-to-real transfer, and demonstrate it
    on a ToddlerBot humanoid for walking-speed tracking fine-tuning and swing-up learning
    from scratch.
  zh: 本文提出了机器人训练机器人（RTR）框架，其中一个机器臂教师通过柔顺接触、课程调度、扰动、故障检测和自动重置来支持和引导人形学生，从而实现最少人工干预的高效现实世界强化学习。作者还介绍了使用
    FiLM 层和域随机化的动态感知潜变量优化流程以稳定仿真到现实的迁移，并在 ToddlerBot 人形机器人上展示了行走速度跟踪微调和从零开始的起身摆动学习。
  ko: 본 논문은 로봇 팔 교사가 순응적 접촉, 커리큘럼 스케줄링, 섭동, 실패 감지 및 자동 리셋을 통해 휴머노이드 학생을 지지하고 안내하여
    최소한의 인간 개입으로 효율적인 실제 세계 강화 학습을 가능하게 하는 Robot-Trains-Robot(RTR) 프레임워크를 제안한다. 저자들은
    또한 FiLM 레이어와 도메인 랜덤화를 사용하여 시뮬레이션에서 실제로의 전이를 안정화하는 동역학 인식 잠재 변수 최적화 파이프라인을 소개하고,
    ToddlerBot 휴머노이드에서 보행 속도 추적 미세 조정 및 처음부터의 스윙업 학습을 입증한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- reinforcement_learning
- sim_to_real
- humanoid_locomotion
- real_world_rl
- robot_teacher
- curriculum_learning
- automatic_reset
- ppo
- film_layer
- domain_randomization
- toddlerbot
- ur5
- force_torque_sensor
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full paper was not independently
    retrieved. Requires human review before verification.
sources:
- id: src_001
  type: paper
  title: 'Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning
    for Humanoids'
  url: https://arxiv.org/abs/2508.12252
  date: '2025'
  accessed_at: '2026-06-26'
---


## Overview

Robot-Trains-Robot (RTR) is a hardware-software framework designed to make real-world reinforcement learning on humanoid robots practical and safe. A UR5 robotic arm equipped with an ATI mini45 force-torque sensor acts as a teacher that physically supports and guides a ToddlerBot humanoid student. The arm provides protective support, applies scheduled curriculum transitions, supplies reward-proxies such as speed tracking error and swing-up height, injects perturbations, detects failures, and triggers automatic resets so that the humanoid can train for long periods with little human supervision.

The policy itself is trained in simulation with domain randomization and uses Feature-wise Linear Modulation (FiLM) layers to condition behavior on a low-dimensional latent variable that encodes dynamics. During real-world adaptation, only that single latent vector is optimized with PPO, keeping the base policy weights frozen. This dramatically reduces the number of real-world samples needed and improves stability when transferring from simulation to hardware.

The authors evaluate RTR on two challenging tasks. The first fine-tunes a pretrained walking policy so the robot accurately tracks commanded walking speeds on a programmable treadmill. The second learns a swing-up task from scratch, where the robot starts lying on the ground and must stand up using the arm for assistance. Both tasks are performed autonomously in the real world with automatic resets.

## Key Contributions

- A complete Robot-Trains-Robot (RTR) system that provides protection, curriculum, reward proxy, perturbation, failure detection, and automatic resets for real-world humanoid training.
- A dynamics-aware latent-optimization pipeline using FiLM layers, domain randomization, and PPO for rapid and stable sim-to-real policy adaptation.
- Empirical validation on two challenging real-world tasks: walking speed-tracking fine-tuning and humanoid swing-up learning from scratch.

## Relevance to Humanoid Robotics

RTR is directly relevant to humanoid robotics because it addresses the central barrier of safely learning and adapting policies on real humanoid hardware. By automating protection, reward estimation, and reset, it reduces the manual labor and risk that have historically made real-world RL on humanoids impractical. The ability to fine-tune sim-trained policies with a single optimized latent variable also offers a scalable path for closing the sim-to-real gap without extensive retraining on hardware.

The work is classified as an AI/models/algorithms contribution with secondary relevance to applications and markets, because the framework is a learning methodology rather than a mass-production or commercial-deployment system. However, its emphasis on autonomous, long-duration real-world skill acquisition positions it as an enabling technology for future deployable humanoid robots.
