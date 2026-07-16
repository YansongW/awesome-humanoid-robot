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
  zh: 本文提出了一种用于双足行走推搡恢复的在线步态适配器，通过指数_ZMP_插值强制_DCM_边界值来修改下一步足位和时长，并在仿真中于扭矩控制的_iCub_人形机器人上进行了验证。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1909.10403v2.
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
We present a computationally efficient method for online planning of bipedal walking trajectories with push recovery. In particular, the proposed methodology fits control architectures where the Divergent-Component-of-Motion (DCM) is planned beforehand, and adds a step adapter to adjust the planned trajectories and achieve push recovery. Assuming that the robot is in a single support state, the step adapter generates new positions and timings for the next step. The step adapter is active in single support phases only, but the proposed torque-control architecture considers double support phases too. The key idea for the design of the step adapter is to impose both initial and final DCM step values using an exponential interpolation of the time varying ZMP trajectory.This allows us to cast the push recovery problem as a Quadratic Programming (QP) one, and to solve it online with state-of-the-art optimisers. The overall approach is validated with simulations of the torque-controlled 33 kg humanoid robot iCub. Results show that the proposed strategy prevents the humanoid robot from falling while walking at 0.28 m/s and pushed with external forces up to 150 Newton for 0.05 seconds.

## 核心内容
We present a computationally efficient method for online planning of bipedal walking trajectories with push recovery. In particular, the proposed methodology fits control architectures where the Divergent-Component-of-Motion (DCM) is planned beforehand, and adds a step adapter to adjust the planned trajectories and achieve push recovery. Assuming that the robot is in a single support state, the step adapter generates new positions and timings for the next step. The step adapter is active in single support phases only, but the proposed torque-control architecture considers double support phases too. The key idea for the design of the step adapter is to impose both initial and final DCM step values using an exponential interpolation of the time varying ZMP trajectory.This allows us to cast the push recovery problem as a Quadratic Programming (QP) one, and to solve it online with state-of-the-art optimisers. The overall approach is validated with simulations of the torque-controlled 33 kg humanoid robot iCub. Results show that the proposed strategy prevents the humanoid robot from falling while walking at 0.28 m/s and pushed with external forces up to 150 Newton for 0.05 seconds.

## 参考
- http://arxiv.org/abs/1909.10403v2

## Overview
We present a computationally efficient method for online planning of bipedal walking trajectories with push recovery. In particular, the proposed methodology fits control architectures where the Divergent-Component-of-Motion (DCM) is planned beforehand, and adds a step adapter to adjust the planned trajectories and achieve push recovery. Assuming that the robot is in a single support state, the step adapter generates new positions and timings for the next step. The step adapter is active in single support phases only, but the proposed torque-control architecture considers double support phases too. The key idea for the design of the step adapter is to impose both initial and final DCM step values using an exponential interpolation of the time varying ZMP trajectory. This allows us to cast the push recovery problem as a Quadratic Programming (QP) one, and to solve it online with state-of-the-art optimisers. The overall approach is validated with simulations of the torque-controlled 33 kg humanoid robot iCub. Results show that the proposed strategy prevents the humanoid robot from falling while walking at 0.28 m/s and pushed with external forces up to 150 Newton for 0.05 seconds.

## Content
We present a computationally efficient method for online planning of bipedal walking trajectories with push recovery. In particular, the proposed methodology fits control architectures where the Divergent-Component-of-Motion (DCM) is planned beforehand, and adds a step adapter to adjust the planned trajectories and achieve push recovery. Assuming that the robot is in a single support state, the step adapter generates new positions and timings for the next step. The step adapter is active in single support phases only, but the proposed torque-control architecture considers double support phases too. The key idea for the design of the step adapter is to impose both initial and final DCM step values using an exponential interpolation of the time varying ZMP trajectory. This allows us to cast the push recovery problem as a Quadratic Programming (QP) one, and to solve it online with state-of-the-art optimisers. The overall approach is validated with simulations of the torque-controlled 33 kg humanoid robot iCub. Results show that the proposed strategy prevents the humanoid robot from falling while walking at 0.28 m/s and pushed with external forces up to 150 Newton for 0.05 seconds.

## 개요
본 논문에서는 푸시 회복이 가능한 이족 보행 궤적의 온라인 계획을 위한 계산 효율적인 방법을 제시합니다. 특히, 제안된 방법론은 사전에 발산 운동 성분(DCM)이 계획된 제어 아키텍처에 적합하며, 계획된 궤적을 조정하고 푸시 회복을 달성하기 위해 스텝 어댑터를 추가합니다. 로봇이 단일 지지 상태에 있다고 가정할 때, 스텝 어댑터는 다음 스텝의 새로운 위치와 타이밍을 생성합니다. 스텝 어댑터는 단일 지지 단계에서만 활성화되지만, 제안된 토크 제어 아키텍처는 이중 지지 단계도 고려합니다. 스텝 어댑터 설계의 핵심 아이디어는 시간에 따라 변하는 ZMP 궤적의 지수 보간을 사용하여 초기 및 최종 DCM 스텝 값을 모두 부과하는 것입니다. 이를 통해 푸시 회복 문제를 2차 계획법(QP) 문제로 변환하고, 최신 최적화 도구를 사용하여 온라인으로 해결할 수 있습니다. 전체 접근 방식은 토크 제어되는 33kg 휴머노이드 로봇 iCub의 시뮬레이션을 통해 검증되었습니다. 결과는 제안된 전략이 0.28m/s로 보행 중 0.05초 동안 최대 150뉴턴의 외력으로 밀릴 때 휴머노이드 로봇의 넘어짐을 방지함을 보여줍니다.

## 핵심 내용
본 논문에서는 푸시 회복이 가능한 이족 보행 궤적의 온라인 계획을 위한 계산 효율적인 방법을 제시합니다. 특히, 제안된 방법론은 사전에 발산 운동 성분(DCM)이 계획된 제어 아키텍처에 적합하며, 계획된 궤적을 조정하고 푸시 회복을 달성하기 위해 스텝 어댑터를 추가합니다. 로봇이 단일 지지 상태에 있다고 가정할 때, 스텝 어댑터는 다음 스텝의 새로운 위치와 타이밍을 생성합니다. 스텝 어댑터는 단일 지지 단계에서만 활성화되지만, 제안된 토크 제어 아키텍처는 이중 지지 단계도 고려합니다. 스텝 어댑터 설계의 핵심 아이디어는 시간에 따라 변하는 ZMP 궤적의 지수 보간을 사용하여 초기 및 최종 DCM 스텝 값을 모두 부과하는 것입니다. 이를 통해 푸시 회복 문제를 2차 계획법(QP) 문제로 변환하고, 최신 최적화 도구를 사용하여 온라인으로 해결할 수 있습니다. 전체 접근 방식은 토크 제어되는 33kg 휴머노이드 로봇 iCub의 시뮬레이션을 통해 검증되었습니다. 결과는 제안된 전략이 0.28m/s로 보행 중 0.05초 동안 최대 150뉴턴의 외력으로 밀릴 때 휴머노이드 로봇의 넘어짐을 방지함을 보여줍니다.
