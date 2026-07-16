---
$id: ent_paper_predictive_sampling_real_time_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo'
  zh: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo'
  ko: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo'
summary:
  en: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo is a 2022 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo is a 2022 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo is a 2022 work on loco-manipulation and whole-body-control
    for humanoid robots.'
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
- predictive_sampling
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.00541v2.
sources:
- id: src_001
  type: paper
  title: 'Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo (arXiv)'
  url: https://arxiv.org/abs/2212.00541
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
We introduce MuJoCo MPC (MJPC), an open-source, interactive application and software framework for real-time predictive control, based on MuJoCo physics. MJPC allows the user to easily author and solve complex robotics tasks, and currently supports three shooting-based planners: derivative-based iLQG and Gradient Descent, and a simple derivative-free method we call Predictive Sampling. Predictive Sampling was designed as an elementary baseline, mostly for its pedagogical value, but turned out to be surprisingly competitive with the more established algorithms. This work does not present algorithmic advances, and instead, prioritises performant algorithms, simple code, and accessibility of model-based methods via intuitive and interactive software. MJPC is available at: github.com/deepmind/mujoco_mpc, a video summary can be viewed at: dpmd.ai/mjpc.

## 核心内容
We introduce MuJoCo MPC (MJPC), an open-source, interactive application and software framework for real-time predictive control, based on MuJoCo physics. MJPC allows the user to easily author and solve complex robotics tasks, and currently supports three shooting-based planners: derivative-based iLQG and Gradient Descent, and a simple derivative-free method we call Predictive Sampling. Predictive Sampling was designed as an elementary baseline, mostly for its pedagogical value, but turned out to be surprisingly competitive with the more established algorithms. This work does not present algorithmic advances, and instead, prioritises performant algorithms, simple code, and accessibility of model-based methods via intuitive and interactive software. MJPC is available at: github.com/deepmind/mujoco_mpc, a video summary can be viewed at: dpmd.ai/mjpc.

## 参考
- http://arxiv.org/abs/2212.00541v2

## Overview
We introduce MuJoCo MPC (MJPC), an open-source, interactive application and software framework for real-time predictive control, based on MuJoCo physics. MJPC allows the user to easily author and solve complex robotics tasks, and currently supports three shooting-based planners: derivative-based iLQG and Gradient Descent, and a simple derivative-free method we call Predictive Sampling. Predictive Sampling was designed as an elementary baseline, mostly for its pedagogical value, but turned out to be surprisingly competitive with the more established algorithms. This work does not present algorithmic advances, and instead, prioritises performant algorithms, simple code, and accessibility of model-based methods via intuitive and interactive software. MJPC is available at: github.com/deepmind/mujoco_mpc, a video summary can be viewed at: dpmd.ai/mjpc.

## Content
We introduce MuJoCo MPC (MJPC), an open-source, interactive application and software framework for real-time predictive control, based on MuJoCo physics. MJPC allows the user to easily author and solve complex robotics tasks, and currently supports three shooting-based planners: derivative-based iLQG and Gradient Descent, and a simple derivative-free method we call Predictive Sampling. Predictive Sampling was designed as an elementary baseline, mostly for its pedagogical value, but turned out to be surprisingly competitive with the more established algorithms. This work does not present algorithmic advances, and instead, prioritises performant algorithms, simple code, and accessibility of model-based methods via intuitive and interactive software. MJPC is available at: github.com/deepmind/mujoco_mpc, a video summary can be viewed at: dpmd.ai/mjpc.

## 개요
MuJoCo MPC(MJPC)를 소개합니다. 이는 MuJoCo 물리 엔진을 기반으로 한 오픈소스 대화형 애플리케이션이자 소프트웨어 프레임워크로, 실시간 예측 제어를 지원합니다. MJPC를 통해 사용자는 복잡한 로봇공학 작업을 쉽게 작성하고 해결할 수 있으며, 현재 세 가지 슈팅 기반 계획기를 지원합니다: 미분 기반 iLQG와 경사 하강법, 그리고 Predictive Sampling이라 불리는 간단한 미분 없는 방법입니다. Predictive Sampling은 주로 교육적 가치를 위해 기본적인 기준선으로 설계되었으나, 기존 알고리즘과 놀라울 정도로 경쟁력 있는 성능을 보였습니다. 본 연구는 알고리즘적 발전을 제시하기보다는, 직관적이고 대화형 소프트웨어를 통해 성능 좋은 알고리즘, 간결한 코드, 그리고 모델 기반 방법의 접근성을 우선시합니다. MJPC는 다음에서 확인할 수 있습니다: github.com/deepmind/mujoco_mpc, 비디오 요약은 다음에서 시청 가능합니다: dpmd.ai/mjpc.

## 핵심 내용
MuJoCo MPC(MJPC)를 소개합니다. 이는 MuJoCo 물리 엔진을 기반으로 한 오픈소스 대화형 애플리케이션이자 소프트웨어 프레임워크로, 실시간 예측 제어를 지원합니다. MJPC를 통해 사용자는 복잡한 로봇공학 작업을 쉽게 작성하고 해결할 수 있으며, 현재 세 가지 슈팅 기반 계획기를 지원합니다: 미분 기반 iLQG와 경사 하강법, 그리고 Predictive Sampling이라 불리는 간단한 미분 없는 방법입니다. Predictive Sampling은 주로 교육적 가치를 위해 기본적인 기준선으로 설계되었으나, 기존 알고리즘과 놀라울 정도로 경쟁력 있는 성능을 보였습니다. 본 연구는 알고리즘적 발전을 제시하기보다는, 직관적이고 대화형 소프트웨어를 통해 성능 좋은 알고리즘, 간결한 코드, 그리고 모델 기반 방법의 접근성을 우선시합니다. MJPC는 다음에서 확인할 수 있습니다: github.com/deepmind/mujoco_mpc, 비디오 요약은 다음에서 시청 가능합니다: dpmd.ai/mjpc.
