---
$id: ent_paper_benchmarking_potential_based_r_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion
  zh: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion
  ko: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion
summary:
  en: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion is a 2023 work on locomotion for humanoid robots.
  zh: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion is a 2023 work on locomotion for humanoid robots.
  ko: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion is a 2023 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmarking_potential_based_r
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.10142v1.
sources:
- id: src_001
  type: paper
  title: Benchmarking Potential Based Rewards for Learning Humanoid Locomotion (arXiv)
  url: https://arxiv.org/abs/2307.10142
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
The main challenge in developing effective reinforcement learning (RL) pipelines is often the design and tuning the reward functions. Well-designed shaping reward can lead to significantly faster learning. Naively formulated rewards, however, can conflict with the desired behavior and result in overfitting or even erratic performance if not properly tuned. In theory, the broad class of potential based reward shaping (PBRS) can help guide the learning process without affecting the optimal policy. Although several studies have explored the use of potential based reward shaping to accelerate learning convergence, most have been limited to grid-worlds and low-dimensional systems, and RL in robotics has predominantly relied on standard forms of reward shaping. In this paper, we benchmark standard forms of shaping with PBRS for a humanoid robot. We find that in this high-dimensional system, PBRS has only marginal benefits in convergence speed. However, the PBRS reward terms are significantly more robust to scaling than typical reward shaping approaches, and thus easier to tune.

## 核心内容
The main challenge in developing effective reinforcement learning (RL) pipelines is often the design and tuning the reward functions. Well-designed shaping reward can lead to significantly faster learning. Naively formulated rewards, however, can conflict with the desired behavior and result in overfitting or even erratic performance if not properly tuned. In theory, the broad class of potential based reward shaping (PBRS) can help guide the learning process without affecting the optimal policy. Although several studies have explored the use of potential based reward shaping to accelerate learning convergence, most have been limited to grid-worlds and low-dimensional systems, and RL in robotics has predominantly relied on standard forms of reward shaping. In this paper, we benchmark standard forms of shaping with PBRS for a humanoid robot. We find that in this high-dimensional system, PBRS has only marginal benefits in convergence speed. However, the PBRS reward terms are significantly more robust to scaling than typical reward shaping approaches, and thus easier to tune.

## 参考
- http://arxiv.org/abs/2307.10142v1

## Overview
The main challenge in developing effective reinforcement learning (RL) pipelines is often the design and tuning of reward functions. Well-designed shaping rewards can lead to significantly faster learning. Naively formulated rewards, however, can conflict with the desired behavior and result in overfitting or even erratic performance if not properly tuned. In theory, the broad class of potential-based reward shaping (PBRS) can help guide the learning process without affecting the optimal policy. Although several studies have explored the use of potential-based reward shaping to accelerate learning convergence, most have been limited to grid-worlds and low-dimensional systems, and RL in robotics has predominantly relied on standard forms of reward shaping. In this paper, we benchmark standard forms of shaping with PBRS for a humanoid robot. We find that in this high-dimensional system, PBRS has only marginal benefits in convergence speed. However, the PBRS reward terms are significantly more robust to scaling than typical reward shaping approaches, and thus easier to tune.

## Content
The main challenge in developing effective reinforcement learning (RL) pipelines is often the design and tuning of reward functions. Well-designed shaping rewards can lead to significantly faster learning. Naively formulated rewards, however, can conflict with the desired behavior and result in overfitting or even erratic performance if not properly tuned. In theory, the broad class of potential-based reward shaping (PBRS) can help guide the learning process without affecting the optimal policy. Although several studies have explored the use of potential-based reward shaping to accelerate learning convergence, most have been limited to grid-worlds and low-dimensional systems, and RL in robotics has predominantly relied on standard forms of reward shaping. In this paper, we benchmark standard forms of shaping with PBRS for a humanoid robot. We find that in this high-dimensional system, PBRS has only marginal benefits in convergence speed. However, the PBRS reward terms are significantly more robust to scaling than typical reward shaping approaches, and thus easier to tune.

## 개요
효과적인 강화 학습(RL) 파이프라인을 개발하는 데 있어 주요 과제는 종종 보상 함수의 설계와 조정입니다. 잘 설계된 형상 보상은 학습 속도를 크게 향상시킬 수 있습니다. 그러나 순진하게 구성된 보상은 원하는 행동과 충돌하여 과적합을 초래하거나, 적절히 조정되지 않으면 불규칙한 성능을 보일 수 있습니다. 이론적으로, 잠재 기반 보상 형성(PBRS)의 광범위한 클래스는 최적 정책에 영향을 주지 않고 학습 과정을 안내하는 데 도움을 줄 수 있습니다. 여러 연구에서 학습 수렴을 가속화하기 위해 잠재 기반 보상 형성을 사용하는 방법을 탐구했지만, 대부분은 그리드 월드와 저차원 시스템에 국한되었으며, 로봇 공학에서의 RL은 주로 표준 형태의 보상 형성에 의존해 왔습니다. 본 논문에서는 인간형 로봇을 대상으로 PBRS와 함께 표준 형태의 형성 방법을 벤치마킹합니다. 이 고차원 시스템에서 PBRS는 수렴 속도에 미미한 이점만을 제공한다는 것을 발견했습니다. 그러나 PBRS 보상 항은 일반적인 보상 형성 접근법보다 스케일링에 훨씬 더 강건하여 조정이 더 쉽습니다.

## 핵심 내용
효과적인 강화 학습(RL) 파이프라인을 개발하는 데 있어 주요 과제는 종종 보상 함수의 설계와 조정입니다. 잘 설계된 형상 보상은 학습 속도를 크게 향상시킬 수 있습니다. 그러나 순진하게 구성된 보상은 원하는 행동과 충돌하여 과적합을 초래하거나, 적절히 조정되지 않으면 불규칙한 성능을 보일 수 있습니다. 이론적으로, 잠재 기반 보상 형성(PBRS)의 광범위한 클래스는 최적 정책에 영향을 주지 않고 학습 과정을 안내하는 데 도움을 줄 수 있습니다. 여러 연구에서 학습 수렴을 가속화하기 위해 잠재 기반 보상 형성을 사용하는 방법을 탐구했지만, 대부분은 그리드 월드와 저차원 시스템에 국한되었으며, 로봇 공학에서의 RL은 주로 표준 형태의 보상 형성에 의존해 왔습니다. 본 논문에서는 인간형 로봇을 대상으로 PBRS와 함께 표준 형태의 형성 방법을 벤치마킹합니다. 이 고차원 시스템에서 PBRS는 수렴 속도에 미미한 이점만을 제공한다는 것을 발견했습니다. 그러나 PBRS 보상 항은 일반적인 보상 형성 접근법보다 스케일링에 훨씬 더 강건하여 조정이 더 쉽습니다.
