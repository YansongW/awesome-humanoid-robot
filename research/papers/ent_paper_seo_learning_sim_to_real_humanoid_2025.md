---
$id: ent_paper_seo_learning_sim_to_real_humanoid_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Sim-to-Real Humanoid Locomotion in 15 Minutes
  zh: 在15分钟内学习从仿真到现实的人形机器人运动
  ko: 15분 만에 학습하는 시뮬레이션-현실 간 휴머노이드 보행
summary:
  en: This paper presents a practical recipe using FastSAC and FastTD3 with massively parallel simulation to train robust
    full-body humanoid locomotion policies on a single RTX 4090 GPU in 15 minutes, and demonstrates sim-to-real deployment
    on Unitree G1 and Booster T1 robots.
  zh: 本文提出了一种基于 FastSAC 和 FastTD3 的实用方案，结合大规模并行仿真，在单张 RTX 4090 GPU 上仅用 15 分钟即可训练出鲁棒的全尺寸人形机器人运动策略，并在 Unitree G1 与 Booster T1
    机器人上实现了 sim-to-real 部署。
  ko: 본 논문은 대규모 병렬 시뮬레이션과 FastSAC 및 FastTD3를 활용한 실용적인 방법론을 제안하여 단일 RTX 4090 GPU에서 15분 만에 강건한 전신 휴머노이드 보행 정책을 학습하고, Unitree
    G1과 Booster T1 로봇에서 sim-to-real 전개를 입증한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 06_design_engineering
layers:
- intelligence
- midstream
- upstream
functional_roles:
- intelligence
- knowledge
tags:
- sim_to_real
- reinforcement_learning
- off_policy_rl
- fastsac
- fasttd3
- humanoid_locomotion
- whole_body_motion_tracking
- domain_randomization
- unitree_g1
- booster_t1
- rtx_4090
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.01996v1.
sources:
- id: src_001
  type: paper
  title: Learning Sim-to-Real Humanoid Locomotion in 15 Minutes
  url: https://arxiv.org/abs/2512.01996
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Massively parallel simulation has reduced reinforcement learning (RL) training time for robots from days to minutes. However, achieving fast and reliable sim-to-real RL for humanoid control remains difficult due to the challenges introduced by factors such as high dimensionality and domain randomization. In this work, we introduce a simple and practical recipe based on off-policy RL algorithms, i.e., FastSAC and FastTD3, that enables rapid training of humanoid locomotion policies in just 15 minutes with a single RTX 4090 GPU. Our simple recipe stabilizes off-policy RL algorithms at massive scale with thousands of parallel environments through carefully tuned design choices and minimalist reward functions. We demonstrate rapid end-to-end learning of humanoid locomotion controllers on Unitree G1 and Booster T1 robots under strong domain randomization, e.g., randomized dynamics, rough terrain, and push perturbations, as well as fast training of whole-body human-motion tracking policies. We provide videos and open-source implementation at: https://younggyo.me/fastsac-humanoid.

## 核心内容
Massively parallel simulation has reduced reinforcement learning (RL) training time for robots from days to minutes. However, achieving fast and reliable sim-to-real RL for humanoid control remains difficult due to the challenges introduced by factors such as high dimensionality and domain randomization. In this work, we introduce a simple and practical recipe based on off-policy RL algorithms, i.e., FastSAC and FastTD3, that enables rapid training of humanoid locomotion policies in just 15 minutes with a single RTX 4090 GPU. Our simple recipe stabilizes off-policy RL algorithms at massive scale with thousands of parallel environments through carefully tuned design choices and minimalist reward functions. We demonstrate rapid end-to-end learning of humanoid locomotion controllers on Unitree G1 and Booster T1 robots under strong domain randomization, e.g., randomized dynamics, rough terrain, and push perturbations, as well as fast training of whole-body human-motion tracking policies. We provide videos and open-source implementation at: https://younggyo.me/fastsac-humanoid.

## 参考
- http://arxiv.org/abs/2512.01996v1

## Overview
Massively parallel simulation has reduced reinforcement learning (RL) training time for robots from days to minutes. However, achieving fast and reliable sim-to-real RL for humanoid control remains difficult due to the challenges introduced by factors such as high dimensionality and domain randomization. In this work, we introduce a simple and practical recipe based on off-policy RL algorithms, i.e., FastSAC and FastTD3, that enables rapid training of humanoid locomotion policies in just 15 minutes with a single RTX 4090 GPU. Our simple recipe stabilizes off-policy RL algorithms at massive scale with thousands of parallel environments through carefully tuned design choices and minimalist reward functions. We demonstrate rapid end-to-end learning of humanoid locomotion controllers on Unitree G1 and Booster T1 robots under strong domain randomization, e.g., randomized dynamics, rough terrain, and push perturbations, as well as fast training of whole-body human-motion tracking policies. We provide videos and open-source implementation at: https://younggyo.me/fastsac-humanoid.

## Content
Massively parallel simulation has reduced reinforcement learning (RL) training time for robots from days to minutes. However, achieving fast and reliable sim-to-real RL for humanoid control remains difficult due to the challenges introduced by factors such as high dimensionality and domain randomization. In this work, we introduce a simple and practical recipe based on off-policy RL algorithms, i.e., FastSAC and FastTD3, that enables rapid training of humanoid locomotion policies in just 15 minutes with a single RTX 4090 GPU. Our simple recipe stabilizes off-policy RL algorithms at massive scale with thousands of parallel environments through carefully tuned design choices and minimalist reward functions. We demonstrate rapid end-to-end learning of humanoid locomotion controllers on Unitree G1 and Booster T1 robots under strong domain randomization, e.g., randomized dynamics, rough terrain, and push perturbations, as well as fast training of whole-body human-motion tracking policies. We provide videos and open-source implementation at: https://younggyo.me/fastsac-humanoid.

## 개요
대규모 병렬 시뮬레이션은 로봇의 강화 학습(RL) 훈련 시간을 며칠에서 몇 분으로 단축시켰습니다. 그러나 휴머노이드 제어를 위한 빠르고 신뢰할 수 있는 sim-to-real RL을 달성하는 것은 고차원성 및 도메인 무작위화와 같은 요인으로 인해 여전히 어렵습니다. 본 연구에서는 오프폴리시 RL 알고리즘인 FastSAC과 FastTD3를 기반으로 한 간단하고 실용적인 방법을 소개합니다. 이 방법은 단일 RTX 4090 GPU로 단 15분 만에 휴머노이드 보행 정책을 빠르게 훈련할 수 있게 해줍니다. 우리의 간단한 방법은 세심하게 조정된 설계 선택과 최소한의 보상 함수를 통해 수천 개의 병렬 환경에서 대규모로 오프폴리시 RL 알고리즘을 안정화합니다. 우리는 Unitree G1 및 Booster T1 로봇에서 강력한 도메인 무작위화(예: 무작위 동역학, 거친 지형, 밀기 교란) 하에 휴머노이드 보행 제어기의 빠른 종단간 학습과 전신 인간 동작 추적 정책의 빠른 훈련을 시연합니다. 비디오와 오픈소스 구현은 https://younggyo.me/fastsac-humanoid 에서 제공합니다.

## 핵심 내용
대규모 병렬 시뮬레이션은 로봇의 강화 학습(RL) 훈련 시간을 며칠에서 몇 분으로 단축시켰습니다. 그러나 휴머노이드 제어를 위한 빠르고 신뢰할 수 있는 sim-to-real RL을 달성하는 것은 고차원성 및 도메인 무작위화와 같은 요인으로 인해 여전히 어렵습니다. 본 연구에서는 오프폴리시 RL 알고리즘인 FastSAC과 FastTD3를 기반으로 한 간단하고 실용적인 방법을 소개합니다. 이 방법은 단일 RTX 4090 GPU로 단 15분 만에 휴머노이드 보행 정책을 빠르게 훈련할 수 있게 해줍니다. 우리의 간단한 방법은 세심하게 조정된 설계 선택과 최소한의 보상 함수를 통해 수천 개의 병렬 환경에서 대규모로 오프폴리시 RL 알고리즘을 안정화합니다. 우리는 Unitree G1 및 Booster T1 로봇에서 강력한 도메인 무작위화(예: 무작위 동역학, 거친 지형, 밀기 교란) 하에 휴머노이드 보행 제어기의 빠른 종단간 학습과 전신 인간 동작 추적 정책의 빠른 훈련을 시연합니다. 비디오와 오픈소스 구현은 https://younggyo.me/fastsac-humanoid 에서 제공합니다.
