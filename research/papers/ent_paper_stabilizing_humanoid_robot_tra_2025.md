---
$id: ent_paper_stabilizing_humanoid_robot_tra_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning
  zh: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning
  ko: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning
summary:
  en: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning is a 2025 work on locomotion for humanoid
    robots.
  zh: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning is a 2025 work on locomotion for humanoid
    robots.
  ko: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning is a 2025 work on locomotion for humanoid
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
- stabilizing_humanoid_robot_tra
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.24697v1.
sources:
- id: src_001
  type: paper
  title: Stabilizing Humanoid Robot Trajectory Generation via Physics-Informed Learning (arXiv)
  url: https://arxiv.org/abs/2509.24697
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent trends in humanoid robot control have successfully employed imitation learning to enable the learned generation of smooth, human-like trajectories from human data. While these approaches make more realistic motions possible, they are limited by the amount of available motion data, and do not incorporate prior knowledge about the physical laws governing the system and its interactions with the environment. Thus they may violate such laws, leading to divergent trajectories and sliding contacts which limit real-world stability. We address such limitations via a two-pronged learning strategy which leverages the known physics of the system and fundamental control principles. First, we encode physics priors during supervised imitation learning to promote trajectory feasibility. Second, we minimize drift at inference time by applying a proportional-integral controller directly to the generated output state. We validate our method on various locomotion behaviors for the ergoCub humanoid robot, where a physics-informed loss encourages zero contact foot velocity. Our experiments demonstrate that the proposed approach is compatible with multiple controllers on a real robot and significantly improves the accuracy and physical constraint conformity of generated trajectories.

## 核心内容
Recent trends in humanoid robot control have successfully employed imitation learning to enable the learned generation of smooth, human-like trajectories from human data. While these approaches make more realistic motions possible, they are limited by the amount of available motion data, and do not incorporate prior knowledge about the physical laws governing the system and its interactions with the environment. Thus they may violate such laws, leading to divergent trajectories and sliding contacts which limit real-world stability. We address such limitations via a two-pronged learning strategy which leverages the known physics of the system and fundamental control principles. First, we encode physics priors during supervised imitation learning to promote trajectory feasibility. Second, we minimize drift at inference time by applying a proportional-integral controller directly to the generated output state. We validate our method on various locomotion behaviors for the ergoCub humanoid robot, where a physics-informed loss encourages zero contact foot velocity. Our experiments demonstrate that the proposed approach is compatible with multiple controllers on a real robot and significantly improves the accuracy and physical constraint conformity of generated trajectories.

## 参考
- http://arxiv.org/abs/2509.24697v1

## Overview
Recent trends in humanoid robot control have successfully employed imitation learning to enable the learned generation of smooth, human-like trajectories from human data. While these approaches make more realistic motions possible, they are limited by the amount of available motion data, and do not incorporate prior knowledge about the physical laws governing the system and its interactions with the environment. Thus they may violate such laws, leading to divergent trajectories and sliding contacts which limit real-world stability. We address such limitations via a two-pronged learning strategy which leverages the known physics of the system and fundamental control principles. First, we encode physics priors during supervised imitation learning to promote trajectory feasibility. Second, we minimize drift at inference time by applying a proportional-integral controller directly to the generated output state. We validate our method on various locomotion behaviors for the ergoCub humanoid robot, where a physics-informed loss encourages zero contact foot velocity. Our experiments demonstrate that the proposed approach is compatible with multiple controllers on a real robot and significantly improves the accuracy and physical constraint conformity of generated trajectories.

## Content
Recent trends in humanoid robot control have successfully employed imitation learning to enable the learned generation of smooth, human-like trajectories from human data. While these approaches make more realistic motions possible, they are limited by the amount of available motion data, and do not incorporate prior knowledge about the physical laws governing the system and its interactions with the environment. Thus they may violate such laws, leading to divergent trajectories and sliding contacts which limit real-world stability. We address such limitations via a two-pronged learning strategy which leverages the known physics of the system and fundamental control principles. First, we encode physics priors during supervised imitation learning to promote trajectory feasibility. Second, we minimize drift at inference time by applying a proportional-integral controller directly to the generated output state. We validate our method on various locomotion behaviors for the ergoCub humanoid robot, where a physics-informed loss encourages zero contact foot velocity. Our experiments demonstrate that the proposed approach is compatible with multiple controllers on a real robot and significantly improves the accuracy and physical constraint conformity of generated trajectories.

## 개요
최근 인간형 로봇 제어 분야에서는 모방 학습을 성공적으로 활용하여 인간 데이터로부터 부드럽고 인간과 유사한 궤적을 학습 생성하는 방법이 주목받고 있습니다. 이러한 접근 방식은 보다 현실적인 동작을 가능하게 하지만, 사용 가능한 동작 데이터의 양에 제한을 받으며 시스템과 환경 간의 상호작용을 지배하는 물리 법칙에 대한 사전 지식을 통합하지 못합니다. 따라서 이러한 법칙을 위반하여 궤적이 발산하거나 접촉이 미끄러지는 현상이 발생할 수 있으며, 이는 실제 환경에서의 안정성을 저해합니다. 우리는 시스템의 알려진 물리 법칙과 기본 제어 원리를 활용하는 두 가지 학습 전략을 통해 이러한 한계를 해결합니다. 첫째, 지도 모방 학습 과정에서 물리적 사전 지식을 인코딩하여 궤적의 실현 가능성을 높입니다. 둘째, 추론 시점에서 생성된 출력 상태에 비례-적분 제어기를 직접 적용하여 드리프트를 최소화합니다. 우리는 ergoCub 인간형 로봇의 다양한 보행 동작에 대해 이 방법을 검증했으며, 물리 정보 기반 손실 함수가 접촉 발의 속도를 0으로 유도하도록 설계했습니다. 실험 결과, 제안된 접근 방식이 실제 로봇의 여러 제어기와 호환되며 생성된 궤적의 정확성과 물리적 제약 준수도를 크게 향상시킴을 입증했습니다.

## 핵심 내용
최근 인간형 로봇 제어 분야에서는 모방 학습을 성공적으로 활용하여 인간 데이터로부터 부드럽고 인간과 유사한 궤적을 학습 생성하는 방법이 주목받고 있습니다. 이러한 접근 방식은 보다 현실적인 동작을 가능하게 하지만, 사용 가능한 동작 데이터의 양에 제한을 받으며 시스템과 환경 간의 상호작용을 지배하는 물리 법칙에 대한 사전 지식을 통합하지 못합니다. 따라서 이러한 법칙을 위반하여 궤적이 발산하거나 접촉이 미끄러지는 현상이 발생할 수 있으며, 이는 실제 환경에서의 안정성을 저해합니다. 우리는 시스템의 알려진 물리 법칙과 기본 제어 원리를 활용하는 두 가지 학습 전략을 통해 이러한 한계를 해결합니다. 첫째, 지도 모방 학습 과정에서 물리적 사전 지식을 인코딩하여 궤적의 실현 가능성을 높입니다. 둘째, 추론 시점에서 생성된 출력 상태에 비례-적분 제어기를 직접 적용하여 드리프트를 최소화합니다. 우리는 ergoCub 인간형 로봇의 다양한 보행 동작에 대해 이 방법을 검증했으며, 물리 정보 기반 손실 함수가 접촉 발의 속도를 0으로 유도하도록 설계했습니다. 실험 결과, 제안된 접근 방식이 실제 로봇의 여러 제어기와 호환되며 생성된 궤적의 정확성과 물리적 제약 준수도를 크게 향상시킴을 입증했습니다.
