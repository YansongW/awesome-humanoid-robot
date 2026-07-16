---
$id: ent_paper_dai_rover_robot_reward_model_as_te_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model'
  zh: RoVer
  ko: 'RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model'
summary:
  en: 'RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model (RoVer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences,
    Peng Cheng Laboratory, School of Computer Science and Engineering, Sun Yat-sen University, College of Computing and Data
    Science, Nanyang Technological University, Shanghai AI Laboratory, University of Chinese Academy of Sciences, X-Era AI
    Lab.'
  zh: 'RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model (RoVer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences,
    Peng Cheng Laboratory, School of Computer Science and Engineering, Sun Yat-sen University, College of Computing and Data
    Science, Nanyang Technological University, Shanghai AI Laboratory, University of Chinese Academy of Sciences, X-Era AI
    Lab.'
  ko: 'RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model (RoVer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences,
    Peng Cheng Laboratory, School of Computer Science and Engineering, Sun Yat-sen University, College of Computing and Data
    Science, Nanyang Technological University, Shanghai AI Laboratory, University of Chinese Academy of Sciences, X-Era AI
    Lab.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- rover
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10975v2.
sources:
- id: src_001
  type: paper
  title: 'RoVer: Robot Reward Model as Test-Time Verifier for Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2510.10975
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoVer source
  url: https://doi.org/10.48550/arXiv.2510.10975
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have become a prominent paradigm for embodied intelligence, yet further performance improvements typically rely on scaling up training data and model size -- an approach that is prohibitively expensive for robotics and fundamentally limited by data collection costs. We address this limitation with $\mathbf{RoVer}$, an embodied test-time scaling framework that uses a $\mathbf{Ro}$bot Process Reward Model (PRM) as a Test-Time $\mathbf{Ver}$ifier to enhance the capabilities of existing VLA models without modifying their architectures or weights. Specifically, RoVer (i) assigns scalar-based process rewards to evaluate the reliability of candidate actions, and (ii) predicts an action-space direction for candidate expansion/refinement. During inference, RoVer generates multiple candidate actions concurrently from the base policy, expands them along PRM-predicted directions, and then scores all candidates with PRM to select the optimal action for execution. Notably, by caching shared perception features, it can amortize perception cost and evaluate more candidates under the same test-time computational budget. Essentially, our approach effectively transforms available computing resources into better action decision-making, realizing the benefits of test-time scaling without extra training overhead. Our contributions are threefold: (1) a general, plug-and-play test-time scaling framework for VLAs; (2) a PRM that jointly provides scalar process rewards and an action-space direction to guide exploration; and (3) an efficient direction-guided sampling strategy that leverages a shared perception cache to enable scalable candidate generation and selection during inference.

## 核心内容
Vision-Language-Action (VLA) models have become a prominent paradigm for embodied intelligence, yet further performance improvements typically rely on scaling up training data and model size -- an approach that is prohibitively expensive for robotics and fundamentally limited by data collection costs. We address this limitation with $\mathbf{RoVer}$, an embodied test-time scaling framework that uses a $\mathbf{Ro}$bot Process Reward Model (PRM) as a Test-Time $\mathbf{Ver}$ifier to enhance the capabilities of existing VLA models without modifying their architectures or weights. Specifically, RoVer (i) assigns scalar-based process rewards to evaluate the reliability of candidate actions, and (ii) predicts an action-space direction for candidate expansion/refinement. During inference, RoVer generates multiple candidate actions concurrently from the base policy, expands them along PRM-predicted directions, and then scores all candidates with PRM to select the optimal action for execution. Notably, by caching shared perception features, it can amortize perception cost and evaluate more candidates under the same test-time computational budget. Essentially, our approach effectively transforms available computing resources into better action decision-making, realizing the benefits of test-time scaling without extra training overhead. Our contributions are threefold: (1) a general, plug-and-play test-time scaling framework for VLAs; (2) a PRM that jointly provides scalar process rewards and an action-space direction to guide exploration; and (3) an efficient direction-guided sampling strategy that leverages a shared perception cache to enable scalable candidate generation and selection during inference.

## 参考
- http://arxiv.org/abs/2510.10975v2

## Overview
Vision-Language-Action (VLA) models have become a prominent paradigm for embodied intelligence, yet further performance improvements typically rely on scaling up training data and model size -- an approach that is prohibitively expensive for robotics and fundamentally limited by data collection costs. We address this limitation with $\mathbf{RoVer}$, an embodied test-time scaling framework that uses a $\mathbf{Ro}$bot Process Reward Model (PRM) as a Test-Time $\mathbf{Ver}$ifier to enhance the capabilities of existing VLA models without modifying their architectures or weights. Specifically, RoVer (i) assigns scalar-based process rewards to evaluate the reliability of candidate actions, and (ii) predicts an action-space direction for candidate expansion/refinement. During inference, RoVer generates multiple candidate actions concurrently from the base policy, expands them along PRM-predicted directions, and then scores all candidates with PRM to select the optimal action for execution. Notably, by caching shared perception features, it can amortize perception cost and evaluate more candidates under the same test-time computational budget. Essentially, our approach effectively transforms available computing resources into better action decision-making, realizing the benefits of test-time scaling without extra training overhead. Our contributions are threefold: (1) a general, plug-and-play test-time scaling framework for VLAs; (2) a PRM that jointly provides scalar process rewards and an action-space direction to guide exploration; and (3) an efficient direction-guided sampling strategy that leverages a shared perception cache to enable scalable candidate generation and selection during inference.

## Content
Vision-Language-Action (VLA) models have become a prominent paradigm for embodied intelligence, yet further performance improvements typically rely on scaling up training data and model size -- an approach that is prohibitively expensive for robotics and fundamentally limited by data collection costs. We address this limitation with $\mathbf{RoVer}$, an embodied test-time scaling framework that uses a $\mathbf{Ro}$bot Process Reward Model (PRM) as a Test-Time $\mathbf{Ver}$ifier to enhance the capabilities of existing VLA models without modifying their architectures or weights. Specifically, RoVer (i) assigns scalar-based process rewards to evaluate the reliability of candidate actions, and (ii) predicts an action-space direction for candidate expansion/refinement. During inference, RoVer generates multiple candidate actions concurrently from the base policy, expands them along PRM-predicted directions, and then scores all candidates with PRM to select the optimal action for execution. Notably, by caching shared perception features, it can amortize perception cost and evaluate more candidates under the same test-time computational budget. Essentially, our approach effectively transforms available computing resources into better action decision-making, realizing the benefits of test-time scaling without extra training overhead. Our contributions are threefold: (1) a general, plug-and-play test-time scaling framework for VLAs; (2) a PRM that jointly provides scalar process rewards and an action-space direction to guide exploration; and (3) an efficient direction-guided sampling strategy that leverages a shared perception cache to enable scalable candidate generation and selection during inference.

## 개요
Vision-Language-Action (VLA) 모델은 구현된 지능을 위한 대표적인 패러다임이 되었지만, 추가적인 성능 향상은 일반적으로 훈련 데이터와 모델 크기의 확장에 의존합니다. 이는 로봇 공학에 엄청난 비용이 들고 데이터 수집 비용에 의해 근본적으로 제한되는 접근 방식입니다. 우리는 이러한 한계를 $\mathbf{RoVer}$로 해결합니다. 이는 구현된 테스트 시간 확장 프레임워크로, $\mathbf{Ro}$bot Process Reward Model (PRM)을 Test-Time $\mathbf{Ver}$ifier로 사용하여 기존 VLA 모델의 아키텍처나 가중치를 수정하지 않고도 성능을 향상시킵니다. 구체적으로, RoVer는 (i) 스칼라 기반 프로세스 보상을 할당하여 후보 행동의 신뢰성을 평가하고, (ii) 후보 확장/정제를 위한 행동 공간 방향을 예측합니다. 추론 중에 RoVer는 기본 정책에서 여러 후보 행동을 동시에 생성하고, PRM이 예측한 방향으로 확장한 후, PRM으로 모든 후보를 평가하여 실행할 최적의 행동을 선택합니다. 특히, 공유된 인식 특징을 캐싱함으로써 인식 비용을 분산시키고 동일한 테스트 시간 계산 예산 내에서 더 많은 후보를 평가할 수 있습니다. 본질적으로, 우리의 접근 방식은 사용 가능한 컴퓨팅 리소스를 더 나은 행동 결정으로 효과적으로 변환하여 추가 훈련 오버헤드 없이 테스트 시간 확장의 이점을 실현합니다. 우리의 기여는 세 가지입니다: (1) VLA를 위한 일반적이고 플러그 앤 플레이 방식의 테스트 시간 확장 프레임워크; (2) 스칼라 프로세스 보상과 탐색을 안내하는 행동 공간 방향을 함께 제공하는 PRM; (3) 공유된 인식 캐시를 활용하여 추론 중 확장 가능한 후보 생성 및 선택을 가능하게 하는 효율적인 방향 안내 샘플링 전략.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 구현된 지능을 위한 대표적인 패러다임이 되었지만, 추가적인 성능 향상은 일반적으로 훈련 데이터와 모델 크기의 확장에 의존합니다. 이는 로봇 공학에 엄청난 비용이 들고 데이터 수집 비용에 의해 근본적으로 제한되는 접근 방식입니다. 우리는 이러한 한계를 $\mathbf{RoVer}$로 해결합니다. 이는 구현된 테스트 시간 확장 프레임워크로, $\mathbf{Ro}$bot Process Reward Model (PRM)을 Test-Time $\mathbf{Ver}$ifier로 사용하여 기존 VLA 모델의 아키텍처나 가중치를 수정하지 않고도 성능을 향상시킵니다. 구체적으로, RoVer는 (i) 스칼라 기반 프로세스 보상을 할당하여 후보 행동의 신뢰성을 평가하고, (ii) 후보 확장/정제를 위한 행동 공간 방향을 예측합니다. 추론 중에 RoVer는 기본 정책에서 여러 후보 행동을 동시에 생성하고, PRM이 예측한 방향으로 확장한 후, PRM으로 모든 후보를 평가하여 실행할 최적의 행동을 선택합니다. 특히, 공유된 인식 특징을 캐싱함으로써 인식 비용을 분산시키고 동일한 테스트 시간 계산 예산 내에서 더 많은 후보를 평가할 수 있습니다. 본질적으로, 우리의 접근 방식은 사용 가능한 컴퓨팅 리소스를 더 나은 행동 결정으로 효과적으로 변환하여 추가 훈련 오버헤드 없이 테스트 시간 확장의 이점을 실현합니다. 우리의 기여는 세 가지입니다: (1) VLA를 위한 일반적이고 플러그 앤 플레이 방식의 테스트 시간 확장 프레임워크; (2) 스칼라 프로세스 보상과 탐색을 안내하는 행동 공간 방향을 함께 제공하는 PRM; (3) 공유된 인식 캐시를 활용하여 추론 중 확장 가능한 후보 생성 및 선택을 가능하게 하는 효율적인 방향 안내 샘플링 전략.
