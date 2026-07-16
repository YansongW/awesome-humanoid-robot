---
$id: ent_paper_ghansah_hierarchical_reduced_order_mod_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots
  zh: 面向人形机器人稳健运动的层级化降阶模型预测控制
  ko: 인간형 로봇의 견고한 보행을 위한 계층적 차수 축소 모델 예측 제어
summary:
  en: Presents a hierarchical reduced-order model predictive control framework for humanoid locomotion, combining a 40 Hz
    nonlinear step planner based on ALIP step-to-step dynamics with a 500 Hz linear MPC that incorporates arm and torso dynamics,
    validated in simulation and hardware on the Unitree G1.
  zh: 提出了一种面向人形机器人行走的层级化降阶模型预测控制框架，将基于ALIP步间动力学的40 Hz非线性步态规划器与包含手臂和躯干动态的500 Hz线性MPC相结合，并在Unitree G1的仿真和硬件实验中进行了验证。
  ko: ALIP 보행 간 동역학에 기반한 40Hz 비선형 보행 계획기와 팔 및 몸통 동역학을 포함하는 500Hz 선형 MPC를 결합한 인간형 로봇 보행을 위한 계층적 차수 축소 MPC 프레임워크를 제시하고, Unitree
    G1에서 시뮬레이션 및 하드웨어 실험으로 검증한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- model_predictive_control
- humanoid_locomotion
- alip
- srb_mpc
- unitree_g1
- push_recovery
- step_planning
- onboard_control
- bipedal_walking
- disturbance_rejection
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.04722v1.
sources:
- id: src_001
  type: paper
  title: Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots
  url: https://arxiv.org/abs/2509.04722
  date: '2025'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_robot_system_unitree_g1
  relationship: evaluates_on
  description:
    en: The proposed hierarchical MPC framework is validated through simulation and hardware experiments on the Unitree G1
      humanoid robot.
    zh: 所提出的层级化MPC框架在Unitree G1人形机器人上通过仿真和硬件实验进行了验证。
    ko: 제안된 계층적 MPC 프레임워크는 Unitree G1 인간형 로봇에서 시뮬레이션 및 하드웨어 실험을 통해 검증되었다.
- id: ent_oem_unitree_robotics
  relationship: uses
  description:
    en: The hardware experiments use the Unitree G1 humanoid robot produced by Unitree.
    zh: 硬件实验使用了由宇树科技生产的Unitree G1人形机器人。
    ko: 하드웨어 실험에는 Unitree가 제조한 Unitree G1 인간형 로봇이 사용되었다.
theoretical_depth:
- system
---
## 概述
As humanoid robots enter real-world environments, ensuring robust locomotion across diverse environments is crucial. This paper presents a computationally efficient hierarchical control framework for humanoid robot locomotion based on reduced-order models -- enabling versatile step planning and incorporating arm and torso dynamics to better stabilize the walking. At the high level, we use the step-to-step dynamics of the ALIP model to simultaneously optimize over step periods, step lengths, and ankle torques via nonlinear MPC. The ALIP trajectories are used as references to a linear MPC framework that extends the standard SRB-MPC to also include simplified arm and torso dynamics. We validate the performance of our approach through simulation and hardware experiments on the Unitree G1 humanoid robot. In the proposed framework the high-level step planner runs at 40 Hz and the mid-level MPC at 500 Hz using the onboard mini-PC. Adaptive step timing increased the push recovery success rate by 36%, and the upper body control improved the yaw disturbance rejection. We also demonstrate robust locomotion across diverse indoor and outdoor terrains, including grass, stone pavement, and uneven gym mats.

## 核心内容
As humanoid robots enter real-world environments, ensuring robust locomotion across diverse environments is crucial. This paper presents a computationally efficient hierarchical control framework for humanoid robot locomotion based on reduced-order models -- enabling versatile step planning and incorporating arm and torso dynamics to better stabilize the walking. At the high level, we use the step-to-step dynamics of the ALIP model to simultaneously optimize over step periods, step lengths, and ankle torques via nonlinear MPC. The ALIP trajectories are used as references to a linear MPC framework that extends the standard SRB-MPC to also include simplified arm and torso dynamics. We validate the performance of our approach through simulation and hardware experiments on the Unitree G1 humanoid robot. In the proposed framework the high-level step planner runs at 40 Hz and the mid-level MPC at 500 Hz using the onboard mini-PC. Adaptive step timing increased the push recovery success rate by 36%, and the upper body control improved the yaw disturbance rejection. We also demonstrate robust locomotion across diverse indoor and outdoor terrains, including grass, stone pavement, and uneven gym mats.

## 参考
- http://arxiv.org/abs/2509.04722v1

## Overview
As humanoid robots enter real-world environments, ensuring robust locomotion across diverse environments is crucial. This paper presents a computationally efficient hierarchical control framework for humanoid robot locomotion based on reduced-order models -- enabling versatile step planning and incorporating arm and torso dynamics to better stabilize the walking. At the high level, we use the step-to-step dynamics of the ALIP model to simultaneously optimize over step periods, step lengths, and ankle torques via nonlinear MPC. The ALIP trajectories are used as references to a linear MPC framework that extends the standard SRB-MPC to also include simplified arm and torso dynamics. We validate the performance of our approach through simulation and hardware experiments on the Unitree G1 humanoid robot. In the proposed framework the high-level step planner runs at 40 Hz and the mid-level MPC at 500 Hz using the onboard mini-PC. Adaptive step timing increased the push recovery success rate by 36%, and the upper body control improved the yaw disturbance rejection. We also demonstrate robust locomotion across diverse indoor and outdoor terrains, including grass, stone pavement, and uneven gym mats.

## Content
As humanoid robots enter real-world environments, ensuring robust locomotion across diverse environments is crucial. This paper presents a computationally efficient hierarchical control framework for humanoid robot locomotion based on reduced-order models -- enabling versatile step planning and incorporating arm and torso dynamics to better stabilize the walking. At the high level, we use the step-to-step dynamics of the ALIP model to simultaneously optimize over step periods, step lengths, and ankle torques via nonlinear MPC. The ALIP trajectories are used as references to a linear MPC framework that extends the standard SRB-MPC to also include simplified arm and torso dynamics. We validate the performance of our approach through simulation and hardware experiments on the Unitree G1 humanoid robot. In the proposed framework the high-level step planner runs at 40 Hz and the mid-level MPC at 500 Hz using the onboard mini-PC. Adaptive step timing increased the push recovery success rate by 36%, and the upper body control improved the yaw disturbance rejection. We also demonstrate robust locomotion across diverse indoor and outdoor terrains, including grass, stone pavement, and uneven gym mats.

## 개요
휴머노이드 로봇이 실제 환경에 진입함에 따라 다양한 환경에서 강건한 보행을 보장하는 것이 중요해졌습니다. 본 논문은 축소 차수 모델을 기반으로 한 계산 효율적인 계층적 제어 프레임워크를 제시합니다. 이는 다양한 보폭 계획을 가능하게 하고, 보행 안정성을 높이기 위해 팔과 몸통 동역학을 통합합니다. 상위 수준에서는 ALIP 모델의 단계별 동역학을 사용하여 비선형 MPC를 통해 보폭 주기, 보폭 길이 및 발목 토크를 동시에 최적화합니다. ALIP 궤적은 표준 SRB-MPC를 확장하여 단순화된 팔과 몸통 동역학을 포함하는 선형 MPC 프레임워크의 참조로 사용됩니다. 우리는 Unitree G1 휴머노이드 로봇을 대상으로 시뮬레이션 및 하드웨어 실험을 통해 접근 방식의 성능을 검증합니다. 제안된 프레임워크에서 상위 수준 보폭 계획기는 40Hz로, 중간 수준 MPC는 온보드 미니 PC를 사용하여 500Hz로 작동합니다. 적응형 보폭 타이밍은 푸시 회복 성공률을 36% 향상시켰으며, 상체 제어는 요 방해 억제를 개선했습니다. 또한 잔디, 돌 포장 도로, 고르지 않은 체육관 매트 등 다양한 실내외 지형에서 강건한 보행을 입증했습니다.

## 핵심 내용
휴머노이드 로봇이 실제 환경에 진입함에 따라 다양한 환경에서 강건한 보행을 보장하는 것이 중요해졌습니다. 본 논문은 축소 차수 모델을 기반으로 한 계산 효율적인 계층적 제어 프레임워크를 제시합니다. 이는 다양한 보폭 계획을 가능하게 하고, 보행 안정성을 높이기 위해 팔과 몸통 동역학을 통합합니다. 상위 수준에서는 ALIP 모델의 단계별 동역학을 사용하여 비선형 MPC를 통해 보폭 주기, 보폭 길이 및 발목 토크를 동시에 최적화합니다. ALIP 궤적은 표준 SRB-MPC를 확장하여 단순화된 팔과 몸통 동역학을 포함하는 선형 MPC 프레임워크의 참조로 사용됩니다. 우리는 Unitree G1 휴머노이드 로봇을 대상으로 시뮬레이션 및 하드웨어 실험을 통해 접근 방식의 성능을 검증합니다. 제안된 프레임워크에서 상위 수준 보폭 계획기는 40Hz로, 중간 수준 MPC는 온보드 미니 PC를 사용하여 500Hz로 작동합니다. 적응형 보폭 타이밍은 푸시 회복 성공률을 36% 향상시켰으며, 상체 제어는 요 방해 억제를 개선했습니다. 또한 잔디, 돌 포장 도로, 고르지 않은 체육관 매트 등 다양한 실내외 지형에서 강건한 보행을 입증했습니다.
