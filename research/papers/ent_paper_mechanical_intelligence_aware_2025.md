---
$id: ent_paper_mechanical_intelligence_aware_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation
  zh: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation
  ko: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation
summary:
  en: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation is a 2025 work on locomotion for humanoid
    robots.
  zh: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation is a 2025 work on locomotion for humanoid
    robots.
  ko: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation is a 2025 work on locomotion for humanoid
    robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- mechanical_intelligence_aware
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.00273v3.
sources:
- id: src_001
  type: paper
  title: Mechanical Intelligence-Aware Curriculum RL for Humanoids with Parallel Actuation (arXiv)
  url: https://arxiv.org/abs/2507.00273
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning (RL) has enabled advances in humanoid robot locomotion, yet most learning frameworks do not account for mechanical intelligence embedded in parallel actuation mechanisms due to limitations in simulator support for closed kinematic chains. This omission can lead to inaccurate motion modeling and suboptimal policies, particularly for robots with high actuation complexity. This paper presents general formulations and simulation methods for three types of parallel mechanisms: a differential pulley, a five-bar linkage, and a four-bar linkage, and trains a parallel-mechanism aware policy through an end-to-end curriculum RL framework for BRUCE, a kid-sized humanoid robot. Unlike prior approaches that rely on simplified serial approximations, we simulate all closed-chain constraints natively using GPU-accelerated MuJoCo (MJX), preserving the hardware's mechanical nonlinear properties during training. We benchmark our RL approach against a model predictive controller (MPC), demonstrating better surface generalization and performance in real-world zero-shot deployment. This work highlights the computational approaches and performance benefits of fully simulating parallel mechanisms in end-to-end learning pipelines for legged humanoids. Project codes with parallel mechanisms: https://github.com/alvister88/og_bruce

## 核心内容
Reinforcement learning (RL) has enabled advances in humanoid robot locomotion, yet most learning frameworks do not account for mechanical intelligence embedded in parallel actuation mechanisms due to limitations in simulator support for closed kinematic chains. This omission can lead to inaccurate motion modeling and suboptimal policies, particularly for robots with high actuation complexity. This paper presents general formulations and simulation methods for three types of parallel mechanisms: a differential pulley, a five-bar linkage, and a four-bar linkage, and trains a parallel-mechanism aware policy through an end-to-end curriculum RL framework for BRUCE, a kid-sized humanoid robot. Unlike prior approaches that rely on simplified serial approximations, we simulate all closed-chain constraints natively using GPU-accelerated MuJoCo (MJX), preserving the hardware's mechanical nonlinear properties during training. We benchmark our RL approach against a model predictive controller (MPC), demonstrating better surface generalization and performance in real-world zero-shot deployment. This work highlights the computational approaches and performance benefits of fully simulating parallel mechanisms in end-to-end learning pipelines for legged humanoids. Project codes with parallel mechanisms: https://github.com/alvister88/og_bruce

## 参考
- http://arxiv.org/abs/2507.00273v3

## Overview
Reinforcement learning (RL) has enabled advances in humanoid robot locomotion, yet most learning frameworks do not account for mechanical intelligence embedded in parallel actuation mechanisms due to limitations in simulator support for closed kinematic chains. This omission can lead to inaccurate motion modeling and suboptimal policies, particularly for robots with high actuation complexity. This paper presents general formulations and simulation methods for three types of parallel mechanisms: a differential pulley, a five-bar linkage, and a four-bar linkage, and trains a parallel-mechanism aware policy through an end-to-end curriculum RL framework for BRUCE, a kid-sized humanoid robot. Unlike prior approaches that rely on simplified serial approximations, we simulate all closed-chain constraints natively using GPU-accelerated MuJoCo (MJX), preserving the hardware's mechanical nonlinear properties during training. We benchmark our RL approach against a model predictive controller (MPC), demonstrating better surface generalization and performance in real-world zero-shot deployment. This work highlights the computational approaches and performance benefits of fully simulating parallel mechanisms in end-to-end learning pipelines for legged humanoids. Project codes with parallel mechanisms: https://github.com/alvister88/og_bruce

## Content
Reinforcement learning (RL) has enabled advances in humanoid robot locomotion, yet most learning frameworks do not account for mechanical intelligence embedded in parallel actuation mechanisms due to limitations in simulator support for closed kinematic chains. This omission can lead to inaccurate motion modeling and suboptimal policies, particularly for robots with high actuation complexity. This paper presents general formulations and simulation methods for three types of parallel mechanisms: a differential pulley, a five-bar linkage, and a four-bar linkage, and trains a parallel-mechanism aware policy through an end-to-end curriculum RL framework for BRUCE, a kid-sized humanoid robot. Unlike prior approaches that rely on simplified serial approximations, we simulate all closed-chain constraints natively using GPU-accelerated MuJoCo (MJX), preserving the hardware's mechanical nonlinear properties during training. We benchmark our RL approach against a model predictive controller (MPC), demonstrating better surface generalization and performance in real-world zero-shot deployment. This work highlights the computational approaches and performance benefits of fully simulating parallel mechanisms in end-to-end learning pipelines for legged humanoids. Project codes with parallel mechanisms: https://github.com/alvister88/og_bruce

## 개요
강화 학습(RL)은 인간형 로봇의 보행 기술 발전을 가능하게 했지만, 대부분의 학습 프레임워크는 폐쇄 운동 사슬에 대한 시뮬레이터 지원 부족으로 인해 병렬 구동 메커니즘에 내장된 기계적 지능을 고려하지 않습니다. 이러한 생략은 특히 구동 복잡성이 높은 로봇에서 부정확한 동작 모델링과 최적이 아닌 정책으로 이어질 수 있습니다. 본 논문은 차동 도르래, 5절 링크, 4절 링크의 세 가지 병렬 메커니즘에 대한 일반적인 공식과 시뮬레이션 방법을 제시하고, 어린이 크기 인간형 로봇 BRUCE를 위한 종단 간 커리큘럼 RL 프레임워크를 통해 병렬 메커니즘을 인식하는 정책을 훈련합니다. 단순화된 직렬 근사에 의존하는 이전 접근 방식과 달리, 우리는 GPU 가속 MuJoCo(MJX)를 사용하여 모든 폐쇄 사슬 제약 조건을 기본적으로 시뮬레이션하여 훈련 중 하드웨어의 기계적 비선형 특성을 보존합니다. 우리는 RL 접근 방식을 모델 예측 제어기(MPC)와 비교 평가하여 실제 환경 제로샷 배포에서 더 나은 표면 일반화와 성능을 입증합니다. 이 연구는 보행 인간형 로봇을 위한 종단 간 학습 파이프라인에서 병렬 메커니즘을 완전히 시뮬레이션하는 계산적 접근 방식과 성능 이점을 강조합니다. 병렬 메커니즘을 포함한 프로젝트 코드: https://github.com/alvister88/og_bruce

## 핵심 내용
강화 학습(RL)은 인간형 로봇의 보행 기술 발전을 가능하게 했지만, 대부분의 학습 프레임워크는 폐쇄 운동 사슬에 대한 시뮬레이터 지원 부족으로 인해 병렬 구동 메커니즘에 내장된 기계적 지능을 고려하지 않습니다. 이러한 생략은 특히 구동 복잡성이 높은 로봇에서 부정확한 동작 모델링과 최적이 아닌 정책으로 이어질 수 있습니다. 본 논문은 차동 도르래, 5절 링크, 4절 링크의 세 가지 병렬 메커니즘에 대한 일반적인 공식과 시뮬레이션 방법을 제시하고, 어린이 크기 인간형 로봇 BRUCE를 위한 종단 간 커리큘럼 RL 프레임워크를 통해 병렬 메커니즘을 인식하는 정책을 훈련합니다. 단순화된 직렬 근사에 의존하는 이전 접근 방식과 달리, 우리는 GPU 가속 MuJoCo(MJX)를 사용하여 모든 폐쇄 사슬 제약 조건을 기본적으로 시뮬레이션하여 훈련 중 하드웨어의 기계적 비선형 특성을 보존합니다. 우리는 RL 접근 방식을 모델 예측 제어기(MPC)와 비교 평가하여 실제 환경 제로샷 배포에서 더 나은 표면 일반화와 성능을 입증합니다. 이 연구는 보행 인간형 로봇을 위한 종단 간 학습 파이프라인에서 병렬 메커니즘을 완전히 시뮬레이션하는 계산적 접근 방식과 성능 이점을 강조합니다. 병렬 메커니즘을 포함한 프로젝트 코드: https://github.com/alvister88/og_bruce
