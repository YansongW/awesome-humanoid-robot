---
$id: ent_paper_whole_body_model_predictive_co_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo
  zh: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo
  ko: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo
summary:
  en: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- loco_manipulation
- whole_body_control
- whole_body_model_predictive_co
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.04613v3.
sources:
- id: src_001
  type: paper
  title: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo (arXiv)
  url: https://arxiv.org/abs/2503.04613
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We demonstrate the surprising real-world effectiveness of a very simple approach to whole-body model-predictive control (MPC) of quadruped and humanoid robots: the iterative LQR (iLQR) algorithm with MuJoCo dynamics and finite-difference approximated derivatives. Building upon the previous success of model-based behavior synthesis and control of locomotion and manipulation tasks with MuJoCo in simulation, we show that these policies can easily generalize to the real world with few sim-to-real considerations. Our baseline method achieves real-time whole-body MPC on a variety of hardware experiments, including dynamic quadruped locomotion, quadruped walking on two legs, and full-sized humanoid bipedal locomotion. We hope this easy-to-reproduce hardware baseline lowers the barrier to entry for real-world whole-body MPC research and contributes to accelerating research velocity in the community. Our code and experiment videos will be available online at:https://johnzhang3.github.io/mujoco_ilqr

## 核心内容
We demonstrate the surprising real-world effectiveness of a very simple approach to whole-body model-predictive control (MPC) of quadruped and humanoid robots: the iterative LQR (iLQR) algorithm with MuJoCo dynamics and finite-difference approximated derivatives. Building upon the previous success of model-based behavior synthesis and control of locomotion and manipulation tasks with MuJoCo in simulation, we show that these policies can easily generalize to the real world with few sim-to-real considerations. Our baseline method achieves real-time whole-body MPC on a variety of hardware experiments, including dynamic quadruped locomotion, quadruped walking on two legs, and full-sized humanoid bipedal locomotion. We hope this easy-to-reproduce hardware baseline lowers the barrier to entry for real-world whole-body MPC research and contributes to accelerating research velocity in the community. Our code and experiment videos will be available online at:https://johnzhang3.github.io/mujoco_ilqr

## 参考
- http://arxiv.org/abs/2503.04613v3

## Overview
We demonstrate the surprising real-world effectiveness of a very simple approach to whole-body model-predictive control (MPC) of quadruped and humanoid robots: the iterative LQR (iLQR) algorithm with MuJoCo dynamics and finite-difference approximated derivatives. Building upon the previous success of model-based behavior synthesis and control of locomotion and manipulation tasks with MuJoCo in simulation, we show that these policies can easily generalize to the real world with few sim-to-real considerations. Our baseline method achieves real-time whole-body MPC on a variety of hardware experiments, including dynamic quadruped locomotion, quadruped walking on two legs, and full-sized humanoid bipedal locomotion. We hope this easy-to-reproduce hardware baseline lowers the barrier to entry for real-world whole-body MPC research and contributes to accelerating research velocity in the community. Our code and experiment videos will be available online at: https://johnzhang3.github.io/mujoco_ilqr

## Content
We demonstrate the surprising real-world effectiveness of a very simple approach to whole-body model-predictive control (MPC) of quadruped and humanoid robots: the iterative LQR (iLQR) algorithm with MuJoCo dynamics and finite-difference approximated derivatives. Building upon the previous success of model-based behavior synthesis and control of locomotion and manipulation tasks with MuJoCo in simulation, we show that these policies can easily generalize to the real world with few sim-to-real considerations. Our baseline method achieves real-time whole-body MPC on a variety of hardware experiments, including dynamic quadruped locomotion, quadruped walking on two legs, and full-sized humanoid bipedal locomotion. We hope this easy-to-reproduce hardware baseline lowers the barrier to entry for real-world whole-body MPC research and contributes to accelerating research velocity in the community. Our code and experiment videos will be available online at: https://johnzhang3.github.io/mujoco_ilqr

## 개요
우리는 사족 보행 로봇과 휴머노이드 로봇의 전신 모델 예측 제어(MPC)에 대한 매우 간단한 접근 방식의 놀라운 실제 효과를 입증합니다: MuJoCo 동역학과 유한 차분 근사 도함수를 사용한 반복 LQR(iLQR) 알고리즘입니다. 시뮬레이션에서 MuJoCo를 사용한 보행 및 조작 작업의 모델 기반 행동 합성 및 제어의 이전 성공을 바탕으로, 이러한 정책이 몇 가지 sim-to-real 고려 사항만으로 실제 세계에 쉽게 일반화될 수 있음을 보여줍니다. 우리의 기준 방법은 동적 사족 보행, 두 다리로 걷는 사족 보행, 전신 크기 휴머노이드 이족 보행을 포함한 다양한 하드웨어 실험에서 실시간 전신 MPC를 달성합니다. 이 쉽게 재현 가능한 하드웨어 기준이 실제 세계 전신 MPC 연구의 진입 장벽을 낮추고 커뮤니티의 연구 속도를 가속화하는 데 기여하기를 바랍니다. 우리의 코드와 실험 비디오는 다음에서 온라인으로 제공될 예정입니다: https://johnzhang3.github.io/mujoco_ilqr

## 핵심 내용
우리는 사족 보행 로봇과 휴머노이드 로봇의 전신 모델 예측 제어(MPC)에 대한 매우 간단한 접근 방식의 놀라운 실제 효과를 입증합니다: MuJoCo 동역학과 유한 차분 근사 도함수를 사용한 반복 LQR(iLQR) 알고리즘입니다. 시뮬레이션에서 MuJoCo를 사용한 보행 및 조작 작업의 모델 기반 행동 합성 및 제어의 이전 성공을 바탕으로, 이러한 정책이 몇 가지 sim-to-real 고려 사항만으로 실제 세계에 쉽게 일반화될 수 있음을 보여줍니다. 우리의 기준 방법은 동적 사족 보행, 두 다리로 걷는 사족 보행, 전신 크기 휴머노이드 이족 보행을 포함한 다양한 하드웨어 실험에서 실시간 전신 MPC를 달성합니다. 이 쉽게 재현 가능한 하드웨어 기준이 실제 세계 전신 MPC 연구의 진입 장벽을 낮추고 커뮤니티의 연구 속도를 가속화하는 데 기여하기를 바랍니다. 우리의 코드와 실험 비디오는 다음에서 온라인으로 제공될 예정입니다: https://johnzhang3.github.io/mujoco_ilqr
