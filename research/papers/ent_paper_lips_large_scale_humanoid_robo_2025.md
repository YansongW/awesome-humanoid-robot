---
$id: ent_paper_lips_large_scale_humanoid_robo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures'
  zh: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures'
  ko: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures'
summary:
  en: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures is a 2025 work on locomotion for humanoid robots.'
  zh: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures is a 2025 work on locomotion for humanoid robots.'
  ko: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- lips
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.08349v1.
sources:
- id: src_001
  type: paper
  title: 'LiPS: Large-Scale Humanoid Robot RL with Parallel-Series Structures (arXiv)'
  url: https://arxiv.org/abs/2503.08349
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In recent years, research on humanoid robots has garnered significant attention, particularly in reinforcement learning based control algorithms, which have achieved major breakthroughs. Compared to traditional model-based control algorithms, reinforcement learning based algorithms demonstrate substantial advantages in handling complex tasks. Leveraging the large-scale parallel computing capabilities of GPUs, contemporary humanoid robots can undergo extensive parallel training in simulated environments. A physical simulation platform capable of large-scale parallel training is crucial for the development of humanoid robots. As one of the most complex robot forms, humanoid robots typically possess intricate mechanical structures, encompassing numerous series and parallel mechanisms. However, many reinforcement learning based humanoid robot control algorithms currently employ open-loop topologies during training, deferring the conversion to series-parallel structures until the sim2real phase. This approach is primarily due to the limitations of physics engines, as current GPU-based physics engines often only support open-loop topologies or have limited capabilities in simulating multi-rigid-body closed-loop topologies. For enabling reinforcement learning-based humanoid robot control algorithms to train in large-scale parallel environments, we propose a novel training method LiPS. By incorporating multi-rigid-body dynamics modeling in the simulation environment, we significantly reduce the sim2real gap and the difficulty of converting to parallel structures during model deployment, thereby robustly supporting large-scale reinforcement learning for humanoid robots.

## 核心内容
In recent years, research on humanoid robots has garnered significant attention, particularly in reinforcement learning based control algorithms, which have achieved major breakthroughs. Compared to traditional model-based control algorithms, reinforcement learning based algorithms demonstrate substantial advantages in handling complex tasks. Leveraging the large-scale parallel computing capabilities of GPUs, contemporary humanoid robots can undergo extensive parallel training in simulated environments. A physical simulation platform capable of large-scale parallel training is crucial for the development of humanoid robots. As one of the most complex robot forms, humanoid robots typically possess intricate mechanical structures, encompassing numerous series and parallel mechanisms. However, many reinforcement learning based humanoid robot control algorithms currently employ open-loop topologies during training, deferring the conversion to series-parallel structures until the sim2real phase. This approach is primarily due to the limitations of physics engines, as current GPU-based physics engines often only support open-loop topologies or have limited capabilities in simulating multi-rigid-body closed-loop topologies. For enabling reinforcement learning-based humanoid robot control algorithms to train in large-scale parallel environments, we propose a novel training method LiPS. By incorporating multi-rigid-body dynamics modeling in the simulation environment, we significantly reduce the sim2real gap and the difficulty of converting to parallel structures during model deployment, thereby robustly supporting large-scale reinforcement learning for humanoid robots.

## 参考
- http://arxiv.org/abs/2503.08349v1

## Overview
In recent years, research on humanoid robots has garnered significant attention, particularly in reinforcement learning based control algorithms, which have achieved major breakthroughs. Compared to traditional model-based control algorithms, reinforcement learning based algorithms demonstrate substantial advantages in handling complex tasks. Leveraging the large-scale parallel computing capabilities of GPUs, contemporary humanoid robots can undergo extensive parallel training in simulated environments. A physical simulation platform capable of large-scale parallel training is crucial for the development of humanoid robots. As one of the most complex robot forms, humanoid robots typically possess intricate mechanical structures, encompassing numerous series and parallel mechanisms. However, many reinforcement learning based humanoid robot control algorithms currently employ open-loop topologies during training, deferring the conversion to series-parallel structures until the sim2real phase. This approach is primarily due to the limitations of physics engines, as current GPU-based physics engines often only support open-loop topologies or have limited capabilities in simulating multi-rigid-body closed-loop topologies. For enabling reinforcement learning-based humanoid robot control algorithms to train in large-scale parallel environments, we propose a novel training method LiPS. By incorporating multi-rigid-body dynamics modeling in the simulation environment, we significantly reduce the sim2real gap and the difficulty of converting to parallel structures during model deployment, thereby robustly supporting large-scale reinforcement learning for humanoid robots.

## Content
In recent years, research on humanoid robots has garnered significant attention, particularly in reinforcement learning based control algorithms, which have achieved major breakthroughs. Compared to traditional model-based control algorithms, reinforcement learning based algorithms demonstrate substantial advantages in handling complex tasks. Leveraging the large-scale parallel computing capabilities of GPUs, contemporary humanoid robots can undergo extensive parallel training in simulated environments. A physical simulation platform capable of large-scale parallel training is crucial for the development of humanoid robots. As one of the most complex robot forms, humanoid robots typically possess intricate mechanical structures, encompassing numerous series and parallel mechanisms. However, many reinforcement learning based humanoid robot control algorithms currently employ open-loop topologies during training, deferring the conversion to series-parallel structures until the sim2real phase. This approach is primarily due to the limitations of physics engines, as current GPU-based physics engines often only support open-loop topologies or have limited capabilities in simulating multi-rigid-body closed-loop topologies. For enabling reinforcement learning-based humanoid robot control algorithms to train in large-scale parallel environments, we propose a novel training method LiPS. By incorporating multi-rigid-body dynamics modeling in the simulation environment, we significantly reduce the sim2real gap and the difficulty of converting to parallel structures during model deployment, thereby robustly supporting large-scale reinforcement learning for humanoid robots.

## 개요
최근 몇 년간 인간형 로봇에 대한 연구가 큰 주목을 받고 있으며, 특히 강화 학습 기반 제어 알고리즘에서 중요한 돌파구가 마련되었습니다. 전통적인 모델 기반 제어 알고리즘과 비교하여 강화 학습 기반 알고리즘은 복잡한 작업을 처리하는 데 있어 상당한 이점을 보여줍니다. GPU의 대규모 병렬 컴퓨팅 능력을 활용하여 현대의 인간형 로봇은 시뮬레이션 환경에서 광범위한 병렬 훈련을 수행할 수 있습니다. 대규모 병렬 훈련이 가능한 물리 시뮬레이션 플랫폼은 인간형 로봇 개발에 매우 중요합니다. 가장 복잡한 로봇 형태 중 하나인 인간형 로봇은 일반적으로 정교한 기계 구조를 가지며, 많은 직렬 및 병렬 메커니즘을 포함합니다. 그러나 현재 많은 강화 학습 기반 인간형 로봇 제어 알고리즘은 훈련 중 개루프 토폴로지를 사용하고, sim2real 단계에서 직렬-병렬 구조로의 변환을 미룹니다. 이러한 접근 방식은 주로 물리 엔진의 한계 때문이며, 현재 GPU 기반 물리 엔진은 종종 개루프 토폴로지만 지원하거나 다중 강체 폐루프 토폴로지 시뮬레이션 능력이 제한적입니다. 강화 학습 기반 인간형 로봇 제어 알고리즘이 대규모 병렬 환경에서 훈련할 수 있도록 하기 위해, 우리는 새로운 훈련 방법인 LiPS를 제안합니다. 시뮬레이션 환경에 다중 강체 동역학 모델링을 통합함으로써 sim2real 격차와 모델 배포 시 병렬 구조로의 변환 어려움을 크게 줄여, 인간형 로봇의 대규모 강화 학습을 강력하게 지원합니다.

## 핵심 내용
최근 몇 년간 인간형 로봇에 대한 연구가 큰 주목을 받고 있으며, 특히 강화 학습 기반 제어 알고리즘에서 중요한 돌파구가 마련되었습니다. 전통적인 모델 기반 제어 알고리즘과 비교하여 강화 학습 기반 알고리즘은 복잡한 작업을 처리하는 데 있어 상당한 이점을 보여줍니다. GPU의 대규모 병렬 컴퓨팅 능력을 활용하여 현대의 인간형 로봇은 시뮬레이션 환경에서 광범위한 병렬 훈련을 수행할 수 있습니다. 대규모 병렬 훈련이 가능한 물리 시뮬레이션 플랫폼은 인간형 로봇 개발에 매우 중요합니다. 가장 복잡한 로봇 형태 중 하나인 인간형 로봇은 일반적으로 정교한 기계 구조를 가지며, 많은 직렬 및 병렬 메커니즘을 포함합니다. 그러나 현재 많은 강화 학습 기반 인간형 로봇 제어 알고리즘은 훈련 중 개루프 토폴로지를 사용하고, sim2real 단계에서 직렬-병렬 구조로의 변환을 미룹니다. 이러한 접근 방식은 주로 물리 엔진의 한계 때문이며, 현재 GPU 기반 물리 엔진은 종종 개루프 토폴로지만 지원하거나 다중 강체 폐루프 토폴로지 시뮬레이션 능력이 제한적입니다. 강화 학습 기반 인간형 로봇 제어 알고리즘이 대규모 병렬 환경에서 훈련할 수 있도록 하기 위해, 우리는 새로운 훈련 방법인 LiPS를 제안합니다. 시뮬레이션 환경에 다중 강체 동역학 모델링을 통합함으로써 sim2real 격차와 모델 배포 시 병렬 구조로의 변환 어려움을 크게 줄여, 인간형 로봇의 대규모 강화 학습을 강력하게 지원합니다.
