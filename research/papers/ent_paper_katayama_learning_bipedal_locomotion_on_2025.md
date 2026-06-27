---
$id: ent_paper_katayama_learning_bipedal_locomotion_on_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Bipedal Locomotion on Gear-Driven Humanoid Robot Using Foot-Mounted
    IMUs
  zh: 使用足部惯性测量单元在齿轮驱动人形机器人上学习双足行走
  ko: 발에 장착된 IMU를 활용한 기어 구동 인간형 로봇의 이족 보행 학습
summary:
  en: This paper proposes a reinforcement learning framework that uses foot-mounted
    inertial measurement units (IMUs) together with a base-mounted IMU to achieve
    robust sim-to-real bipedal locomotion on a high-gear-ratio, torque-sensorless
    miniature humanoid robot (EVAL-03). It introduces symmetric data augmentation
    and random network distillation to improve rapid stabilization over rough and
    non-rigid terrains, validated through hardware experiments.
  zh: 该论文提出了一种强化学习框架，通过足部惯性测量单元（IMU）与躯干IMU相结合，在采用高减速比执行器且无扭矩传感器的微型人形机器人EVAL-03上实现稳健的仿真到现实双足行走。论文引入了针对观测空间的对称数据增强和随机网络蒸馏技术，以提升在粗糙和非刚性地形上的快速稳定能力，并通过硬件实验进行了验证。
  ko: 본 논문은 발에 장착된 관성 측정 장치(IMU)와 기반 IMU를 함께 사용하여 고감속비 액추에이터와 토크 센서가 없는 소형 인간형 로봇
    EVAL-03에서 시뮬레이션에서 현실로 이어지는 견고한 이족 보행을 달성하는 강화학습 프레임워크를 제안한다. 거친 지형과 비강성 지형에서의
    급격한 안정화 능력을 향상시키기 위해 대칭 데이터 증강과 랜덤 네트워크 증류를 도입하고 하드웨어 실험으로 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 05_mass_production
- 11_applications_markets
layers:
- intelligence
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- sim_to_real
- reinforcement_learning
- bipedal_locomotion
- foot_mounted_imu
- gear_driven_humanoid
- torque_sensorless
- blind_locomotion
- eval_03
- miniature_humanoid
- ppo
- isaac_gym
- legged_gym
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; requires human review against
    the full arXiv text before verification.
sources:
- id: src_001
  type: paper
  title: Learning Bipedal Locomotion on Gear-Driven Humanoid Robot Using Foot-Mounted
    IMUs
  url: https://arxiv.org/abs/2504.00614
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This work addresses sim-to-real reinforcement learning (RL) for miniature humanoid robots that use high-gear-ratio actuators and lack torque sensors. Accurate actuator modeling and system identification are difficult in such systems because of complex nonlinear dynamics, friction, and backlash. The authors sidestep detailed actuator modeling by relying instead on additional sensing: linear acceleration and angular velocity measurements from foot-mounted IMUs, combined with a base-mounted IMU, are used as observations for a blind locomotion policy.

The policy is trained with proximal policy optimization (PPO) in simulation using Isaac Gym/Legged Gym and then transferred to the real EVAL-03 robot. To improve learning, the authors propose symmetric data augmentation tailored to the new observation space, including coordinate transforms for the foot-mounted IMUs, and random network distillation (RND) to encourage diverse foot placements on rough terrain. The resulting controller is evaluated on hardware over non-rigid surfaces, steps, and payload conditions.

## Key Contributions

- An RL framework that incorporates foot-mounted IMU observations for sim-to-real bipedal locomotion on high-gear-ratio, torque-sensorless humanoids.
- Symmetric data augmentation designed for the proposed observation space, including foot-IMU coordinate transforms.
- Random network distillation to encourage exploration of diverse foot placements on rough terrain.
- Hardware experiments on the EVAL-03 robot across non-rigid terrains, steps, and payload conditions.

## Relevance to Humanoid Robotics

The paper is directly relevant to affordable, mass-producible humanoid systems because it shows a low-cost sensing route—adding foot-mounted IMUs rather than torque sensors or elaborate actuator models—to robust sim-to-real locomotion on gear-driven miniature humanoids. If the approach transfers to larger platforms, it could lower the sensor and modeling cost barriers that currently limit reliable bipedal control in low-cost humanoid designs.
