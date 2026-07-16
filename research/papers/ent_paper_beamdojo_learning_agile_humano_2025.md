---
$id: ent_paper_beamdojo_learning_agile_humano_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds'
  zh: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds'
  ko: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds'
summary:
  en: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds is a 2025 work on locomotion for humanoid robots.'
  zh: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds is a 2025 work on locomotion for humanoid robots.'
  ko: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- beamdojo
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.10363v3.
sources:
- id: src_001
  type: paper
  title: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds (arXiv)'
  url: https://arxiv.org/abs/2502.10363
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds project page'
  url: https://why618188.github.io/beamdojo/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Traversing risky terrains with sparse footholds poses a significant challenge for humanoid robots, requiring precise foot placements and stable locomotion. Existing learning-based approaches often struggle on such complex terrains due to sparse foothold rewards and inefficient learning processes. To address these challenges, we introduce BeamDojo, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds. BeamDojo begins by introducing a sampling-based foothold reward tailored for polygonal feet, along with a double critic to balancing the learning process between dense locomotion rewards and sparse foothold rewards. To encourage sufficient trial-and-error exploration, BeamDojo incorporates a two-stage RL approach: the first stage relaxes the terrain dynamics by training the humanoid on flat terrain while providing it with task-terrain perceptive observations, and the second stage fine-tunes the policy on the actual task terrain. Moreover, we implement a onboard LiDAR-based elevation map to enable real-world deployment. Extensive simulation and real-world experiments demonstrate that BeamDojo achieves efficient learning in simulation and enables agile locomotion with precise foot placement on sparse footholds in the real world, maintaining a high success rate even under significant external disturbances.

## 核心内容
Traversing risky terrains with sparse footholds poses a significant challenge for humanoid robots, requiring precise foot placements and stable locomotion. Existing learning-based approaches often struggle on such complex terrains due to sparse foothold rewards and inefficient learning processes. To address these challenges, we introduce BeamDojo, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds. BeamDojo begins by introducing a sampling-based foothold reward tailored for polygonal feet, along with a double critic to balancing the learning process between dense locomotion rewards and sparse foothold rewards. To encourage sufficient trial-and-error exploration, BeamDojo incorporates a two-stage RL approach: the first stage relaxes the terrain dynamics by training the humanoid on flat terrain while providing it with task-terrain perceptive observations, and the second stage fine-tunes the policy on the actual task terrain. Moreover, we implement a onboard LiDAR-based elevation map to enable real-world deployment. Extensive simulation and real-world experiments demonstrate that BeamDojo achieves efficient learning in simulation and enables agile locomotion with precise foot placement on sparse footholds in the real world, maintaining a high success rate even under significant external disturbances.

## 参考
- http://arxiv.org/abs/2502.10363v3

## Overview
Traversing risky terrains with sparse footholds poses a significant challenge for humanoid robots, requiring precise foot placements and stable locomotion. Existing learning-based approaches often struggle on such complex terrains due to sparse foothold rewards and inefficient learning processes. To address these challenges, we introduce BeamDojo, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds. BeamDojo begins by introducing a sampling-based foothold reward tailored for polygonal feet, along with a double critic to balancing the learning process between dense locomotion rewards and sparse foothold rewards. To encourage sufficient trial-and-error exploration, BeamDojo incorporates a two-stage RL approach: the first stage relaxes the terrain dynamics by training the humanoid on flat terrain while providing it with task-terrain perceptive observations, and the second stage fine-tunes the policy on the actual task terrain. Moreover, we implement a onboard LiDAR-based elevation map to enable real-world deployment. Extensive simulation and real-world experiments demonstrate that BeamDojo achieves efficient learning in simulation and enables agile locomotion with precise foot placement on sparse footholds in the real world, maintaining a high success rate even under significant external disturbances.

## Content
Traversing risky terrains with sparse footholds poses a significant challenge for humanoid robots, requiring precise foot placements and stable locomotion. Existing learning-based approaches often struggle on such complex terrains due to sparse foothold rewards and inefficient learning processes. To address these challenges, we introduce BeamDojo, a reinforcement learning (RL) framework designed for enabling agile humanoid locomotion on sparse footholds. BeamDojo begins by introducing a sampling-based foothold reward tailored for polygonal feet, along with a double critic to balancing the learning process between dense locomotion rewards and sparse foothold rewards. To encourage sufficient trial-and-error exploration, BeamDojo incorporates a two-stage RL approach: the first stage relaxes the terrain dynamics by training the humanoid on flat terrain while providing it with task-terrain perceptive observations, and the second stage fine-tunes the policy on the actual task terrain. Moreover, we implement a onboard LiDAR-based elevation map to enable real-world deployment. Extensive simulation and real-world experiments demonstrate that BeamDojo achieves efficient learning in simulation and enables agile locomotion with precise foot placement on sparse footholds in the real world, maintaining a high success rate even under significant external disturbances.

## 개요
드문 발판이 있는 위험한 지형을 횡단하는 것은 인간형 로봇에게 정확한 발 위치와 안정적인 보행을 요구하는 중요한 도전 과제입니다. 기존의 학습 기반 접근 방식은 드문 발판 보상과 비효율적인 학습 과정으로 인해 이러한 복잡한 지형에서 종종 어려움을 겪습니다. 이러한 문제를 해결하기 위해, 우리는 드문 발판에서 민첩한 인간형 로봇 보행을 가능하게 하도록 설계된 강화 학습(RL) 프레임워크인 BeamDojo를 소개합니다. BeamDojo는 먼저 다각형 발에 맞춤화된 샘플링 기반 발판 보상과 함께, 조밀한 보행 보상과 드문 발판 보상 간의 학습 과정을 균형 맞추기 위한 이중 비평가(double critic)를 도입합니다. 충분한 시행착오 탐험을 장려하기 위해, BeamDojo는 2단계 RL 접근 방식을 통합합니다. 첫 번째 단계는 인간형 로봇에게 작업 지형 인식 관측을 제공하면서 평평한 지형에서 훈련시켜 지형 역학을 완화하고, 두 번째 단계는 실제 작업 지형에서 정책을 미세 조정합니다. 또한, 실제 환경 배치를 가능하게 하기 위해 온보드 LiDAR 기반 고도 지도를 구현합니다. 광범위한 시뮬레이션 및 실제 실험을 통해 BeamDojo가 시뮬레이션에서 효율적인 학습을 달성하고, 실제 세계의 드문 발판에서 정확한 발 위치로 민첩한 보행을 가능하게 하며, 상당한 외부 교란 하에서도 높은 성공률을 유지함을 입증합니다.

## 핵심 내용
드문 발판이 있는 위험한 지형을 횡단하는 것은 인간형 로봇에게 정확한 발 위치와 안정적인 보행을 요구하는 중요한 도전 과제입니다. 기존의 학습 기반 접근 방식은 드문 발판 보상과 비효율적인 학습 과정으로 인해 이러한 복잡한 지형에서 종종 어려움을 겪습니다. 이러한 문제를 해결하기 위해, 우리는 드문 발판에서 민첩한 인간형 로봇 보행을 가능하게 하도록 설계된 강화 학습(RL) 프레임워크인 BeamDojo를 소개합니다. BeamDojo는 먼저 다각형 발에 맞춤화된 샘플링 기반 발판 보상과 함께, 조밀한 보행 보상과 드문 발판 보상 간의 학습 과정을 균형 맞추기 위한 이중 비평가(double critic)를 도입합니다. 충분한 시행착오 탐험을 장려하기 위해, BeamDojo는 2단계 RL 접근 방식을 통합합니다. 첫 번째 단계는 인간형 로봇에게 작업 지형 인식 관측을 제공하면서 평평한 지형에서 훈련시켜 지형 역학을 완화하고, 두 번째 단계는 실제 작업 지형에서 정책을 미세 조정합니다. 또한, 실제 환경 배치를 가능하게 하기 위해 온보드 LiDAR 기반 고도 지도를 구현합니다. 광범위한 시뮬레이션 및 실제 실험을 통해 BeamDojo가 시뮬레이션에서 효율적인 학습을 달성하고, 실제 세계의 드문 발판에서 정확한 발 위치로 민첩한 보행을 가능하게 하며, 상당한 외부 교란 하에서도 높은 성공률을 유지함을 입증합니다.
