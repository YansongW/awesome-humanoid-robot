---
$id: ent_paper_shafiee_online_dcm_trajectory_generati_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Online DCM Trajectory Generation for Push Recovery of Torque-Controlled Humanoid Robots
  zh: 扭矩控制人形机器人_push_recovery_的在线_DCM_轨迹生成
  ko: 토크 제어 휴머노이드 로봇의 푸시 복구를 위한 온라인 DCM 궤적 생성
summary:
  en: This paper presents an online step adapter for push recovery in bipedal walking that modifies the next footstep position
    and timing by enforcing initial and final DCM boundary values through exponential ZMP interpolation, validated on the
    torque-controlled iCub humanoid in simulation.
  zh: 本文提出一种用于双足行走推扰恢复的在线步态适配器，通过指数ZMP插值强制设定DCM边界值来调整下一步位置与时机，并在力矩控制的iCub人形机器人仿真中验证了有效性。
  ko: 본 논문은 지수적 ZMP 보간을 통해 초기 및 최종 DCM 경계값을 강제함으로써 다음 보폭 위치와 타이밍을 수정하는 이족 보행 푸시 복구를 위한 온라인 스텝 어댑터를 제안하고, 토크 제어 iCub 휴머노이드
    로봇 시뮬레이션에서 검증하였다.
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
- push_recovery
- dcm_trajectory
- bipedal_locomotion
- torque_control
- online_qp
- zmp_interpolation
- icub
- humanoid_walking
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1909.10403v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (563 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Online DCM Trajectory Generation for Push Recovery of Torque-Controlled Humanoid Robots
  url: https://arxiv.org/abs/1909.10403
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
该研究针对双足行走中的推扰恢复问题，提出一种计算高效的在线步态规划方法。方法假设机器人处于单支撑状态，通过步态适配器动态调整下一步的位置与时机，同时力矩控制架构也考虑了双支撑阶段。核心创新在于利用时变ZMP轨迹的指数插值，同时约束DCM的初始与最终边界值，将推扰恢复转化为可在线求解的二次规划问题。在33公斤的iCub人形机器人仿真中，该方法使机器人以0.28米/秒行走时，能抵抗持续0.05秒、高达150牛顿的外部推力而不摔倒。

## 核心内容
### 方法概述
- 提出一种计算高效的在线双足行走轨迹规划方法，专门针对推扰恢复场景。
- 方法适用于预先规划DCM的控制架构，通过添加步态适配器调整预规划轨迹以实现推扰恢复。
- 步态适配器仅在单支撑阶段激活，但整体力矩控制架构同时覆盖双支撑阶段。

### 核心设计
- 步态适配器的关键设计在于：通过时变ZMP轨迹的指数插值，同时施加DCM的初始与最终边界值。
- 该方法将推扰恢复问题转化为二次规划问题，可利用现代优化器在线求解。

### 实验验证
- 在力矩控制的33公斤iCub人形机器人仿真中验证。
- 实验参数：行走速度0.28米/秒，施加持续0.05秒、最大150牛顿的外部推力。
- 结果证明：该策略能有效防止机器人摔倒，成功实现推扰恢复。

## Overview
We present a computationally efficient method for online planning of bipedal walking trajectories with push recovery. In particular, the proposed methodology fits control architectures where the Divergent-Component-of-Motion (DCM) is planned beforehand, and adds a step adapter to adjust the planned trajectories and achieve push recovery. Assuming that the robot is in a single support state, the step adapter generates new positions and timings for the next step. The step adapter is active in single support phases only, but the proposed torque-control architecture considers double support phases too. The key idea for the design of the step adapter is to impose both initial and final DCM step values using an exponential interpolation of the time varying ZMP trajectory.This allows us to cast the push recovery problem as a Quadratic Programming (QP) one, and to solve it online with state-of-the-art optimisers. The overall approach is validated with simulations of the torque-controlled 33 kg humanoid robot iCub. Results show that the proposed strategy prevents the humanoid robot from falling while walking at 0.28 m/s and pushed with external forces up to 150 Newton for 0.05 seconds.

## Overview
We present a computationally efficient method for online planning of bipedal walking trajectories with push recovery. In particular, the proposed methodology fits control architectures where the Divergent-Component-of-Motion (DCM) is planned beforehand, and adds a step adapter to adjust the planned trajectories and achieve push recovery. Assuming that the robot is in a single support state, the step adapter generates new positions and timings for the next step. The step adapter is active in single support phases only, but the proposed torque-control architecture considers double support phases too. The key idea for the design of the step adapter is to impose both initial and final DCM step values using an exponential interpolation of the time varying ZMP trajectory. This allows us to cast the push recovery problem as a Quadratic Programming (QP) one, and to solve it online with state-of-the-art optimisers. The overall approach is validated with simulations of the torque-controlled 33 kg humanoid robot iCub. Results show that the proposed strategy prevents the humanoid robot from falling while walking at 0.28 m/s and pushed with external forces up to 150 Newton for 0.05 seconds.

## Content
We present a computationally efficient method for online planning of bipedal walking trajectories with push recovery. In particular, the proposed methodology fits control architectures where the Divergent-Component-of-Motion (DCM) is planned beforehand, and adds a step adapter to adjust the planned trajectories and achieve push recovery. Assuming that the robot is in a single support state, the step adapter generates new positions and timings for the next step. The step adapter is active in single support phases only, but the proposed torque-control architecture considers double support phases too. The key idea for the design of the step adapter is to impose both initial and final DCM step values using an exponential interpolation of the time varying ZMP trajectory. This allows us to cast the push recovery problem as a Quadratic Programming (QP) one, and to solve it online with state-of-the-art optimisers. The overall approach is validated with simulations of the torque-controlled 33 kg humanoid robot iCub. Results show that the proposed strategy prevents the humanoid robot from falling while walking at 0.28 m/s and pushed with external forces up to 150 Newton for 0.05 seconds.

## 参考
- http://arxiv.org/abs/1909.10403v2

## 개요
이 연구는 이족 보행 중 밀림 외란 회복 문제를 대상으로, 계산 효율이 높은 온라인 보행 계획 방법을 제안한다. 이 방법은 로봇이 단일 지지 상태에 있다고 가정하고, 보행 어댑터를 통해 다음 단계의 위치와 시점을 동적으로 조정하며, 토크 제어 아키텍처는 이중 지지 단계도 고려한다. 핵심 혁신은 시간에 따라 변하는 ZMP 궤적의 지수 보간을 활용하고, DCM의 초기 및 최종 경계 값을 동시에 제약하여 밀림 외란 회복을 온라인으로 풀 수 있는 2차 계획 문제로 변환하는 것이다. 33kg의 iCub 휴머노이드 로봇 시뮬레이션에서, 이 방법은 로봇이 0.28m/s로 보행할 때 0.05초 동안 지속되는 최대 150N의 외부 밀림에도 넘어지지 않고 저항할 수 있음을 보여준다.

## 핵심 내용
### 방법 개요
- 밀림 외란 회복 시나리오를 대상으로 한 계산 효율이 높은 온라인 이족 보행 궤적 계획 방법을 제안한다.
- 이 방법은 사전 계획된 DCM을 사용하는 제어 아키텍처에 적용되며, 보행 어댑터를 추가하여 사전 계획된 궤적을 조정함으로써 밀림 외란 회복을 구현한다.
- 보행 어댑터는 단일 지지 단계에서만 활성화되지만, 전체 토크 제어 아키텍처는 이중 지지 단계도 동시에 포함한다.

### 핵심 설계
- 보행 어댑터의 핵심 설계는 시간에 따라 변하는 ZMP 궤적의 지수 보간을 통해 DCM의 초기 및 최종 경계 값을 동시에 적용하는 것이다.
- 이 방법은 밀림 외란 회복 문제를 2차 계획 문제로 변환하며, 현대 최적화 도구를 사용하여 온라인으로 풀 수 있다.

### 실험 검증
- 토크 제어 방식의 33kg iCub 휴머노이드 로봇 시뮬레이션에서 검증되었다.
- 실험 매개변수: 보행 속도 0.28m/s, 0.05초 동안 지속되는 최대 150N의 외부 밀림 적용.
- 결과는 이 전략이 로봇이 넘어지는 것을 효과적으로 방지하고 밀림 외란 회복을 성공적으로 구현함을 증명한다.
