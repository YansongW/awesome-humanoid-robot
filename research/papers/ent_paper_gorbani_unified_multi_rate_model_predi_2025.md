---
$id: ent_paper_gorbani_unified_multi_rate_model_predi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Multi-Rate Model Predictive Control for a Jet-Powered Humanoid Robot
  zh: 喷气动力人形机器人的统一多速率模型预测控制
  ko: 제트 동력 휴머노이드 로봇을 위한 통합 다중 속도 모델 예측 제어
summary:
  en: This paper presents a multi-rate Model Predictive Control framework for the jet-powered humanoid iRonCub that jointly
    embeds centroidal momentum dynamics and second-order nonlinear jet-engine dynamics, validated through MuJoCo simulations.
  zh: 本文提出了一种用于喷气动力人形机器人iRonCub的多速率模型预测控制框架，将质心动量动力学与二阶非线性喷气发动机动力学相结合，并通过MuJoCo仿真进行了验证。
  ko: 본 논문은 제트 동력 휴머노이드 iRonCub를 위한 다중 속도 모델 예측 제어 프레임워크를 제안하며, 질량 중심 운동량 역학과 2차 비선형 제트 엔진 역학을 통합하고 MuJoCo 시뮬레이션을 통해 검증하였다.
domains:
- 06_design_engineering
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
- system
tags:
- model_predictive_control
- multi_rate_control
- jet_powered_humanoid
- ironcub
- centroidal_momentum
- flight_control
- lpv_mpc
- jet_dynamics
- mujoco
- osqp
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.16478v2.
sources:
- id: src_001
  type: paper
  title: Unified Multi-Rate Model Predictive Control for a Jet-Powered Humanoid Robot
  url: https://arxiv.org/abs/2505.16478v2
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
We propose a novel Model Predictive Control (MPC) framework for a jet-powered flying humanoid robot. The controller is based on a linearised centroidal momentum model to represent the flight dynamics, augmented with a second-order nonlinear model to explicitly account for the slow and nonlinear dynamics of jet propulsion. A key contribution is the introduction of a multi-rate MPC formulation that handles the different actuation rates of the robot's joints and jet engines while embedding the jet dynamics directly into the predictive model. We validated the framework using the jet-powered humanoid robot iRonCub, performing simulations in Mujoco; the simulation results demonstrate the robot's ability to recover from external disturbances and perform stable, non-abrupt flight manoeuvres, validating the effectiveness of the proposed approach.

## 核心内容
We propose a novel Model Predictive Control (MPC) framework for a jet-powered flying humanoid robot. The controller is based on a linearised centroidal momentum model to represent the flight dynamics, augmented with a second-order nonlinear model to explicitly account for the slow and nonlinear dynamics of jet propulsion. A key contribution is the introduction of a multi-rate MPC formulation that handles the different actuation rates of the robot's joints and jet engines while embedding the jet dynamics directly into the predictive model. We validated the framework using the jet-powered humanoid robot iRonCub, performing simulations in Mujoco; the simulation results demonstrate the robot's ability to recover from external disturbances and perform stable, non-abrupt flight manoeuvres, validating the effectiveness of the proposed approach.

## 参考
- http://arxiv.org/abs/2505.16478v2

## Overview
We propose a novel Model Predictive Control (MPC) framework for a jet-powered flying humanoid robot. The controller is based on a linearised centroidal momentum model to represent the flight dynamics, augmented with a second-order nonlinear model to explicitly account for the slow and nonlinear dynamics of jet propulsion. A key contribution is the introduction of a multi-rate MPC formulation that handles the different actuation rates of the robot's joints and jet engines while embedding the jet dynamics directly into the predictive model. We validated the framework using the jet-powered humanoid robot iRonCub, performing simulations in Mujoco; the simulation results demonstrate the robot's ability to recover from external disturbances and perform stable, non-abrupt flight manoeuvres, validating the effectiveness of the proposed approach.

## Content
We propose a novel Model Predictive Control (MPC) framework for a jet-powered flying humanoid robot. The controller is based on a linearised centroidal momentum model to represent the flight dynamics, augmented with a second-order nonlinear model to explicitly account for the slow and nonlinear dynamics of jet propulsion. A key contribution is the introduction of a multi-rate MPC formulation that handles the different actuation rates of the robot's joints and jet engines while embedding the jet dynamics directly into the predictive model. We validated the framework using the jet-powered humanoid robot iRonCub, performing simulations in Mujoco; the simulation results demonstrate the robot's ability to recover from external disturbances and perform stable, non-abrupt flight manoeuvres, validating the effectiveness of the proposed approach.

## 개요
본 논문은 제트 추진 비행 휴머노이드 로봇을 위한 새로운 모델 예측 제어(MPC) 프레임워크를 제안합니다. 제어기는 비행 동역학을 표현하기 위해 선형화된 중심 운동량 모델을 기반으로 하며, 제트 추진의 느리고 비선형적인 동역학을 명시적으로 고려하기 위해 2차 비선형 모델이 추가되었습니다. 주요 기여는 로봇의 관절과 제트 엔진의 서로 다른 작동 속도를 처리하면서 제트 동역학을 예측 모델에 직접 포함시키는 다중 속도 MPC 공식을 도입한 것입니다. 우리는 제트 추진 휴머노이드 로봇 iRonCub을 사용하여 Mujoco에서 시뮬레이션을 수행함으로써 프레임워크를 검증했습니다. 시뮬레이션 결과는 로봇이 외부 교란으로부터 회복하고 안정적이고 급격하지 않은 비행 기동을 수행할 수 있음을 보여주며, 제안된 접근 방식의 효과성을 입증합니다.

## 핵심 내용
본 논문은 제트 추진 비행 휴머노이드 로봇을 위한 새로운 모델 예측 제어(MPC) 프레임워크를 제안합니다. 제어기는 비행 동역학을 표현하기 위해 선형화된 중심 운동량 모델을 기반으로 하며, 제트 추진의 느리고 비선형적인 동역학을 명시적으로 고려하기 위해 2차 비선형 모델이 추가되었습니다. 주요 기여는 로봇의 관절과 제트 엔진의 서로 다른 작동 속도를 처리하면서 제트 동역학을 예측 모델에 직접 포함시키는 다중 속도 MPC 공식을 도입한 것입니다. 우리는 제트 추진 휴머노이드 로봇 iRonCub을 사용하여 Mujoco에서 시뮬레이션을 수행함으로써 프레임워크를 검증했습니다. 시뮬레이션 결과는 로봇이 외부 교란으로부터 회복하고 안정적이고 급격하지 않은 비행 기동을 수행할 수 있음을 보여주며, 제안된 접근 방식의 효과성을 입증합니다.
