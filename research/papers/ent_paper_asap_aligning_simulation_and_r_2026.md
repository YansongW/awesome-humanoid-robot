---
$id: ent_paper_asap_aligning_simulation_and_r_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills'
  zh: sim-to-real 对齐不是调参数那么简单
  ko: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills'
summary:
  en: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills is a knowledge node
    related to paper in the humanoid robot value chain.'
  zh: Humanoid robots hold the potential for unparalleled versatility in performing human-like, whole-body skills. However,
    achieving agile and coordinated whole-body motions remains a significant challenge due to the dynamics mismatch between
    simulation and the real world. Existing approaches, such as system identification (SysID) and domain randomization (DR)
    methods, often rely on labor-intensive parameter tuning or result in overly conservative policies that sacrifice agility.
    In this paper, we present ASAP (Aligning Simulation and Real-World Physics), a two-stage framework designed to tackle
    the dynamics mismatch and enable agile humanoid whole-body skills. In the first stage, we pre-train motion tracking policies
    in simulation using retargeted human motion data. In the second stage, we dep
  ko: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills is a knowledge node
    related to paper in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- sim_to_real
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.01143v3.
sources:
- id: src_001
  type: paper
  title: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills (arXiv)'
  url: https://arxiv.org/abs/2502.01143
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: sim-to-real 对齐不是调参数那么简单 project page
  url: https://agile.human2humanoid.com
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Humanoid robots hold the potential for unparalleled versatility in performing human-like, whole-body skills. However, achieving agile and coordinated whole-body motions remains a significant challenge due to the dynamics mismatch between simulation and the real world. Existing approaches, such as system identification (SysID) and domain randomization (DR) methods, often rely on labor-intensive parameter tuning or result in overly conservative policies that sacrifice agility. In this paper, we present ASAP (Aligning Simulation and Real-World Physics), a two-stage framework designed to tackle the dynamics mismatch and enable agile humanoid whole-body skills. In the first stage, we pre-train motion tracking policies in simulation using retargeted human motion data. In the second stage, we deploy the policies in the real world and collect real-world data to train a delta (residual) action model that compensates for the dynamics mismatch. Then, ASAP fine-tunes pre-trained policies with the delta action model integrated into the simulator to align effectively with real-world dynamics. We evaluate ASAP across three transfer scenarios: IsaacGym to IsaacSim, IsaacGym to Genesis, and IsaacGym to the real-world Unitree G1 humanoid robot. Our approach significantly improves agility and whole-body coordination across various dynamic motions, reducing tracking error compared to SysID, DR, and delta dynamics learning baselines. ASAP enables highly agile motions that were previously difficult to achieve, demonstrating the potential of delta action learning in bridging simulation and real-world dynamics. These results suggest a promising sim-to-real direction for developing more expressive and agile humanoids.

## 核心内容
Humanoid robots hold the potential for unparalleled versatility in performing human-like, whole-body skills. However, achieving agile and coordinated whole-body motions remains a significant challenge due to the dynamics mismatch between simulation and the real world. Existing approaches, such as system identification (SysID) and domain randomization (DR) methods, often rely on labor-intensive parameter tuning or result in overly conservative policies that sacrifice agility. In this paper, we present ASAP (Aligning Simulation and Real-World Physics), a two-stage framework designed to tackle the dynamics mismatch and enable agile humanoid whole-body skills. In the first stage, we pre-train motion tracking policies in simulation using retargeted human motion data. In the second stage, we deploy the policies in the real world and collect real-world data to train a delta (residual) action model that compensates for the dynamics mismatch. Then, ASAP fine-tunes pre-trained policies with the delta action model integrated into the simulator to align effectively with real-world dynamics. We evaluate ASAP across three transfer scenarios: IsaacGym to IsaacSim, IsaacGym to Genesis, and IsaacGym to the real-world Unitree G1 humanoid robot. Our approach significantly improves agility and whole-body coordination across various dynamic motions, reducing tracking error compared to SysID, DR, and delta dynamics learning baselines. ASAP enables highly agile motions that were previously difficult to achieve, demonstrating the potential of delta action learning in bridging simulation and real-world dynamics. These results suggest a promising sim-to-real direction for developing more expressive and agile humanoids.

## 参考
- http://arxiv.org/abs/2502.01143v3

## Overview
Humanoid robots hold the potential for unparalleled versatility in performing human-like, whole-body skills. However, achieving agile and coordinated whole-body motions remains a significant challenge due to the dynamics mismatch between simulation and the real world. Existing approaches, such as system identification (SysID) and domain randomization (DR) methods, often rely on labor-intensive parameter tuning or result in overly conservative policies that sacrifice agility. In this paper, we present ASAP (Aligning Simulation and Real-World Physics), a two-stage framework designed to tackle the dynamics mismatch and enable agile humanoid whole-body skills. In the first stage, we pre-train motion tracking policies in simulation using retargeted human motion data. In the second stage, we deploy the policies in the real world and collect real-world data to train a delta (residual) action model that compensates for the dynamics mismatch. Then, ASAP fine-tunes pre-trained policies with the delta action model integrated into the simulator to align effectively with real-world dynamics. We evaluate ASAP across three transfer scenarios: IsaacGym to IsaacSim, IsaacGym to Genesis, and IsaacGym to the real-world Unitree G1 humanoid robot. Our approach significantly improves agility and whole-body coordination across various dynamic motions, reducing tracking error compared to SysID, DR, and delta dynamics learning baselines. ASAP enables highly agile motions that were previously difficult to achieve, demonstrating the potential of delta action learning in bridging simulation and real-world dynamics. These results suggest a promising sim-to-real direction for developing more expressive and agile humanoids.

## Content
Humanoid robots hold the potential for unparalleled versatility in performing human-like, whole-body skills. However, achieving agile and coordinated whole-body motions remains a significant challenge due to the dynamics mismatch between simulation and the real world. Existing approaches, such as system identification (SysID) and domain randomization (DR) methods, often rely on labor-intensive parameter tuning or result in overly conservative policies that sacrifice agility. In this paper, we present ASAP (Aligning Simulation and Real-World Physics), a two-stage framework designed to tackle the dynamics mismatch and enable agile humanoid whole-body skills. In the first stage, we pre-train motion tracking policies in simulation using retargeted human motion data. In the second stage, we deploy the policies in the real world and collect real-world data to train a delta (residual) action model that compensates for the dynamics mismatch. Then, ASAP fine-tunes pre-trained policies with the delta action model integrated into the simulator to align effectively with real-world dynamics. We evaluate ASAP across three transfer scenarios: IsaacGym to IsaacSim, IsaacGym to Genesis, and IsaacGym to the real-world Unitree G1 humanoid robot. Our approach significantly improves agility and whole-body coordination across various dynamic motions, reducing tracking error compared to SysID, DR, and delta dynamics learning baselines. ASAP enables highly agile motions that were previously difficult to achieve, demonstrating the potential of delta action learning in bridging simulation and real-world dynamics. These results suggest a promising sim-to-real direction for developing more expressive and agile humanoids.

## 개요
휴머노이드 로봇은 인간과 유사한 전신 기술을 수행하는 데 있어 비교할 수 없는 다재다능함을 지니고 있습니다. 그러나 시뮬레이션과 실제 세계 간의 동역학 불일치로 인해 민첩하고 조화로운 전신 움직임을 달성하는 것은 여전히 큰 도전 과제입니다. 시스템 식별(SysID) 및 도메인 무작위화(DR) 방법과 같은 기존 접근 방식은 노동 집약적인 매개변수 튜닝에 의존하거나 민첩성을 희생하는 지나치게 보수적인 정책을 초래하는 경우가 많습니다. 본 논문에서는 동역학 불일치를 해결하고 민첩한 휴머노이드 전신 기술을 가능하게 하기 위해 설계된 2단계 프레임워크인 ASAP(Aligning Simulation and Real-World Physics)를 제시합니다. 첫 번째 단계에서는 리타겟팅된 인간 모션 데이터를 사용하여 시뮬레이션에서 모션 추적 정책을 사전 훈련합니다. 두 번째 단계에서는 정책을 실제 세계에 배포하고 실제 데이터를 수집하여 동역학 불일치를 보상하는 델타(잔차) 액션 모델을 훈련합니다. 그런 다음 ASAP는 델타 액션 모델을 시뮬레이터에 통합하여 사전 훈련된 정책을 미세 조정함으로써 실제 동역학과 효과적으로 정렬합니다. 우리는 IsaacGym에서 IsaacSim으로, IsaacGym에서 Genesis로, IsaacGym에서 실제 Unitree G1 휴머노이드 로봇으로의 세 가지 전이 시나리오에서 ASAP를 평가합니다. 우리의 접근 방식은 다양한 동적 움직임에서 민첩성과 전신 조정을 크게 개선하여 SysID, DR 및 델타 동역학 학습 기준선과 비교하여 추적 오차를 줄입니다. ASAP는 이전에 달성하기 어려웠던 매우 민첩한 움직임을 가능하게 하여 시뮬레이션과 실제 동역학을 연결하는 델타 액션 학습의 잠재력을 보여줍니다. 이러한 결과는 더 표현력 있고 민첩한 휴머노이드를 개발하기 위한 유망한 sim-to-real 방향을 시사합니다.

## 핵심 내용
휴머노이드 로봇은 인간과 유사한 전신 기술을 수행하는 데 있어 비교할 수 없는 다재다능함을 지니고 있습니다. 그러나 시뮬레이션과 실제 세계 간의 동역학 불일치로 인해 민첩하고 조화로운 전신 움직임을 달성하는 것은 여전히 큰 도전 과제입니다. 시스템 식별(SysID) 및 도메인 무작위화(DR) 방법과 같은 기존 접근 방식은 노동 집약적인 매개변수 튜닝에 의존하거나 민첩성을 희생하는 지나치게 보수적인 정책을 초래하는 경우가 많습니다. 본 논문에서는 동역학 불일치를 해결하고 민첩한 휴머노이드 전신 기술을 가능하게 하기 위해 설계된 2단계 프레임워크인 ASAP(Aligning Simulation and Real-World Physics)를 제시합니다. 첫 번째 단계에서는 리타겟팅된 인간 모션 데이터를 사용하여 시뮬레이션에서 모션 추적 정책을 사전 훈련합니다. 두 번째 단계에서는 정책을 실제 세계에 배포하고 실제 데이터를 수집하여 동역학 불일치를 보상하는 델타(잔차) 액션 모델을 훈련합니다. 그런 다음 ASAP는 델타 액션 모델을 시뮬레이터에 통합하여 사전 훈련된 정책을 미세 조정함으로써 실제 동역학과 효과적으로 정렬합니다. 우리는 IsaacGym에서 IsaacSim으로, IsaacGym에서 Genesis로, IsaacGym에서 실제 Unitree G1 휴머노이드 로봇으로의 세 가지 전이 시나리오에서 ASAP를 평가합니다. 우리의 접근 방식은 다양한 동적 움직임에서 민첩성과 전신 조정을 크게 개선하여 SysID, DR 및 델타 동역학 학습 기준선과 비교하여 추적 오차를 줄입니다. ASAP는 이전에 달성하기 어려웠던 매우 민첩한 움직임을 가능하게 하여 시뮬레이션과 실제 동역학을 연결하는 델타 액션 학습의 잠재력을 보여줍니다. 이러한 결과는 더 표현력 있고 민첩한 휴머노이드를 개발하기 위한 유망한 sim-to-real 방향을 시사합니다.
