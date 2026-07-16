---
$id: ent_paper_mimicdroid_in_context_learning_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos'
  zh: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos'
  ko: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos'
summary:
  en: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos is a 2025 work on manipulation
    for humanoid robots.'
  zh: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos is a 2025 work on manipulation
    for humanoid robots.'
  ko: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos is a 2025 work on manipulation
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
- manipulation
- mimicdroid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09769v1.
sources:
- id: src_001
  type: paper
  title: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos (arXiv)'
  url: https://arxiv.org/abs/2509.09769
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We aim to enable humanoid robots to efficiently solve new manipulation tasks from a few video examples. In-context learning (ICL) is a promising framework for achieving this goal due to its test-time data efficiency and rapid adaptability. However, current ICL methods rely on labor-intensive teleoperated data for training, which restricts scalability. We propose using human play videos -- continuous, unlabeled videos of people interacting freely with their environment -- as a scalable and diverse training data source. We introduce MimicDroid, which enables humanoids to perform ICL using human play videos as the only training data. MimicDroid extracts trajectory pairs with similar manipulation behaviors and trains the policy to predict the actions of one trajectory conditioned on the other. Through this process, the model acquired ICL capabilities for adapting to novel objects and environments at test time. To bridge the embodiment gap, MimicDroid first retargets human wrist poses estimated from RGB videos to the humanoid, leveraging kinematic similarity. It also applies random patch masking during training to reduce overfitting to human-specific cues and improve robustness to visual differences. To evaluate few-shot learning for humanoids, we introduce an open-source simulation benchmark with increasing levels of generalization difficulty. MimicDroid outperformed state-of-the-art methods and achieved nearly twofold higher success rates in the real world. Additional materials can be found on: ut-austin-rpl.github.io/MimicDroid

## 核心内容
We aim to enable humanoid robots to efficiently solve new manipulation tasks from a few video examples. In-context learning (ICL) is a promising framework for achieving this goal due to its test-time data efficiency and rapid adaptability. However, current ICL methods rely on labor-intensive teleoperated data for training, which restricts scalability. We propose using human play videos -- continuous, unlabeled videos of people interacting freely with their environment -- as a scalable and diverse training data source. We introduce MimicDroid, which enables humanoids to perform ICL using human play videos as the only training data. MimicDroid extracts trajectory pairs with similar manipulation behaviors and trains the policy to predict the actions of one trajectory conditioned on the other. Through this process, the model acquired ICL capabilities for adapting to novel objects and environments at test time. To bridge the embodiment gap, MimicDroid first retargets human wrist poses estimated from RGB videos to the humanoid, leveraging kinematic similarity. It also applies random patch masking during training to reduce overfitting to human-specific cues and improve robustness to visual differences. To evaluate few-shot learning for humanoids, we introduce an open-source simulation benchmark with increasing levels of generalization difficulty. MimicDroid outperformed state-of-the-art methods and achieved nearly twofold higher success rates in the real world. Additional materials can be found on: ut-austin-rpl.github.io/MimicDroid

## 参考
- http://arxiv.org/abs/2509.09769v1

## Overview
We aim to enable humanoid robots to efficiently solve new manipulation tasks from a few video examples. In-context learning (ICL) is a promising framework for achieving this goal due to its test-time data efficiency and rapid adaptability. However, current ICL methods rely on labor-intensive teleoperated data for training, which restricts scalability. We propose using human play videos -- continuous, unlabeled videos of people interacting freely with their environment -- as a scalable and diverse training data source. We introduce MimicDroid, which enables humanoids to perform ICL using human play videos as the only training data. MimicDroid extracts trajectory pairs with similar manipulation behaviors and trains the policy to predict the actions of one trajectory conditioned on the other. Through this process, the model acquired ICL capabilities for adapting to novel objects and environments at test time. To bridge the embodiment gap, MimicDroid first retargets human wrist poses estimated from RGB videos to the humanoid, leveraging kinematic similarity. It also applies random patch masking during training to reduce overfitting to human-specific cues and improve robustness to visual differences. To evaluate few-shot learning for humanoids, we introduce an open-source simulation benchmark with increasing levels of generalization difficulty. MimicDroid outperformed state-of-the-art methods and achieved nearly twofold higher success rates in the real world. Additional materials can be found on: ut-austin-rpl.github.io/MimicDroid

## Content
We aim to enable humanoid robots to efficiently solve new manipulation tasks from a few video examples. In-context learning (ICL) is a promising framework for achieving this goal due to its test-time data efficiency and rapid adaptability. However, current ICL methods rely on labor-intensive teleoperated data for training, which restricts scalability. We propose using human play videos -- continuous, unlabeled videos of people interacting freely with their environment -- as a scalable and diverse training data source. We introduce MimicDroid, which enables humanoids to perform ICL using human play videos as the only training data. MimicDroid extracts trajectory pairs with similar manipulation behaviors and trains the policy to predict the actions of one trajectory conditioned on the other. Through this process, the model acquired ICL capabilities for adapting to novel objects and environments at test time. To bridge the embodiment gap, MimicDroid first retargets human wrist poses estimated from RGB videos to the humanoid, leveraging kinematic similarity. It also applies random patch masking during training to reduce overfitting to human-specific cues and improve robustness to visual differences. To evaluate few-shot learning for humanoids, we introduce an open-source simulation benchmark with increasing levels of generalization difficulty. MimicDroid outperformed state-of-the-art methods and achieved nearly twofold higher success rates in the real world. Additional materials can be found on: ut-austin-rpl.github.io/MimicDroid

## 개요
우리는 인간형 로봇이 몇 가지 비디오 예제만으로 새로운 조작 작업을 효율적으로 해결할 수 있도록 하는 것을 목표로 합니다. 인컨텍스트 학습(ICL)은 테스트 시 데이터 효율성과 빠른 적응성 덕분에 이 목표를 달성하기 위한 유망한 프레임워크입니다. 그러나 현재의 ICL 방법은 훈련을 위해 노동 집약적인 원격 조작 데이터에 의존하여 확장성을 제한합니다. 우리는 인간의 놀이 비디오(사람들이 환경과 자유롭게 상호작용하는 연속적이고 레이블이 없는 비디오)를 확장 가능하고 다양한 훈련 데이터 소스로 사용할 것을 제안합니다. 우리는 MimicDroid를 소개합니다. 이는 인간형 로봇이 인간의 놀이 비디오만을 훈련 데이터로 사용하여 ICL을 수행할 수 있게 합니다. MimicDroid는 유사한 조작 행동을 가진 궤적 쌍을 추출하고, 하나의 궤적의 행동을 다른 궤적에 조건부로 예측하도록 정책을 훈련합니다. 이 과정을 통해 모델은 테스트 시 새로운 물체와 환경에 적응하기 위한 ICL 능력을 획득합니다. 구현 차이를 극복하기 위해 MimicDroid는 먼저 RGB 비디오에서 추정된 인간 손목 자세를 인간형 로봇에 재타겟팅하여 운동학적 유사성을 활용합니다. 또한 훈련 중 무작위 패치 마스킹을 적용하여 인간 특정 단서에 대한 과적합을 줄이고 시각적 차이에 대한 강건성을 향상시킵니다. 인간형 로봇의 퓨샷 학습을 평가하기 위해 일반화 난이도가 증가하는 오픈소스 시뮬레이션 벤치마크를 도입합니다. MimicDroid는 최첨단 방법을 능가하며 실제 환경에서 거의 두 배 높은 성공률을 달성했습니다. 추가 자료는 다음에서 확인할 수 있습니다: ut-austin-rpl.github.io/MimicDroid

## 핵심 내용
우리는 인간형 로봇이 몇 가지 비디오 예제만으로 새로운 조작 작업을 효율적으로 해결할 수 있도록 하는 것을 목표로 합니다. 인컨텍스트 학습(ICL)은 테스트 시 데이터 효율성과 빠른 적응성 덕분에 이 목표를 달성하기 위한 유망한 프레임워크입니다. 그러나 현재의 ICL 방법은 훈련을 위해 노동 집약적인 원격 조작 데이터에 의존하여 확장성을 제한합니다. 우리는 인간의 놀이 비디오(사람들이 환경과 자유롭게 상호작용하는 연속적이고 레이블이 없는 비디오)를 확장 가능하고 다양한 훈련 데이터 소스로 사용할 것을 제안합니다. 우리는 MimicDroid를 소개합니다. 이는 인간형 로봇이 인간의 놀이 비디오만을 훈련 데이터로 사용하여 ICL을 수행할 수 있게 합니다. MimicDroid는 유사한 조작 행동을 가진 궤적 쌍을 추출하고, 하나의 궤적의 행동을 다른 궤적에 조건부로 예측하도록 정책을 훈련합니다. 이 과정을 통해 모델은 테스트 시 새로운 물체와 환경에 적응하기 위한 ICL 능력을 획득합니다. 구현 차이를 극복하기 위해 MimicDroid는 먼저 RGB 비디오에서 추정된 인간 손목 자세를 인간형 로봇에 재타겟팅하여 운동학적 유사성을 활용합니다. 또한 훈련 중 무작위 패치 마스킹을 적용하여 인간 특정 단서에 대한 과적합을 줄이고 시각적 차이에 대한 강건성을 향상시킵니다. 인간형 로봇의 퓨샷 학습을 평가하기 위해 일반화 난이도가 증가하는 오픈소스 시뮬레이션 벤치마크를 도입합니다. MimicDroid는 최첨단 방법을 능가하며 실제 환경에서 거의 두 배 높은 성공률을 달성했습니다. 추가 자료는 다음에서 확인할 수 있습니다: ut-austin-rpl.github.io/MimicDroid
