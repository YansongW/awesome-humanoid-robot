---
$id: ent_paper_scalable_dexterous_robot_learn_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Scalable Dexterous Robot Learning with AR-based Remote Human-Robot Interactions
  zh: Scalable Dexterous Robot Learning with AR-based Remote Human-Robot Interactions
  ko: Scalable Dexterous Robot Learning with AR-based Remote Human-Robot Interactions
summary:
  en: 'arXiv:2602.07341v2 Announce Type: replace-cross Abstract: This paper focuses on the scalable robot learning for manipulation
    in the dexterous robot arm-hand systems, where the remote human-robot interactions via augmented reality (AR) are established
    to collect the expert demonstration data for improving efficiency. In such a system, we present a novel method to address
    the general manipulation task problem. Specifically, the proposed method consists of two phases: i) In the first phase
    for pretraining, the policy is created in a behavior cloning (BC) manner, through leveraging the learning data from our
    AR-based remote human-robot interaction system; ii) In the second phase, a contrastive learning empowered reinforcement
    learning (RL) method is developed to obtain more efficient and robust policy than the BC, and thus a projection head is
    designed to accelerate the learning progress. An event-driven augmented reward is adopted for enhancing the safety. To
    validate the proposed method, both the physics simulations via PyBullet and real-world experiments are carried out. The
    results demonstrate that compared to the baselines, our method not only significantly speeds up the training process,
    but also achieves much better performance in terms of the success rate for fulfilling the manipulation tasks. By conducting
    the ablation study, it is confirmed that the proposed RL with contrastive learning overcomes policy collapse. Supplementary
    demonstrations are available at https://cyberyyc.github.io/.'
  zh: 本文提出一种基于增强现实（AR）远程人机交互的可扩展机器人学习方法，用于灵巧机械臂-手系统的操作任务。该方法分为两阶段：先通过行为克隆（BC）预训练策略，再采用对比学习增强的强化学习（RL）获得更高效鲁棒的策略，并引入事件驱动增强奖励提升安全性。在PyBullet仿真和真实实验中，该方法显著加速训练过程，操作成功率远超基线，且对比学习有效防止了策略崩溃。
  ko: 'arXiv:2602.07341v2 Announce Type: replace-cross Abstract: This paper focuses on the scalable robot learning for manipulation
    in the dexterous robot arm-hand systems, where the remote human-robot interactions via augmented reality (AR) are established
    to collect the expert demonstration data for improving efficiency. In such a system, we present a novel method to address
    the general manipulation task problem. Specifically, the proposed method consists of two phases: i) In the first phase
    for pretraining, the policy is created in a behavior cloning (BC) manner, through leveraging the learning data from our
    AR-based remote human-robot interaction system; ii) In the second phase, a contrastive learning empowered reinforcement
    learning (RL) method is developed to obtain more efficient and robust policy than the BC, and thus a projection head is
    designed to accelerate the learning progress. An event-driven augmented reward is adopted for enhancing the safety. To
    validate the proposed method, both the physics simulations via PyBullet and real-world experiments are carried out. The
    results demonstrate that compared to the baselines, our method not only significantly speeds up the training process,
    but also achieves much better performance in terms of the success rate for fulfilling the manipulation tasks. By conducting
    the ablation study, it is confirmed that the proposed RL with contrastive learning overcomes policy collapse. Supplementary
    demonstrations are available at https://cyberyyc.github.io/.'
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
- robotics
- scalable_dexterous_robot_learn
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.07341v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (886 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Scalable Dexterous Robot Learning with AR-based Remote Human-Robot Interactions (arXiv)
  url: https://arxiv.org/abs/2602.07341
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
针对灵巧机械臂-手系统的可扩展操作学习问题，本文建立基于增强现实（AR）的远程人机交互系统来高效收集专家演示数据。提出的方法包含两个阶段：第一阶段利用AR交互系统收集的数据，通过行为克隆（BC）方式预训练策略；第二阶段开发对比学习增强的强化学习（RL）方法，并设计投影头加速学习进程，同时采用事件驱动增强奖励提升安全性。在PyBullet物理仿真和真实机器人上的实验表明，该方法相比基线不仅大幅加快训练速度，还显著提高了操作任务的成功率。消融研究证实，对比学习有效克服了策略崩溃问题。

## 核心内容
### 方法架构
本文针对灵巧机械臂-手系统（dexterous robot arm-hand systems）提出两阶段学习框架：
- **第一阶段（预训练）**：通过AR远程人机交互系统（AR-based remote human-robot interaction system）收集专家演示数据，采用行为克隆（BC）方式初始化策略。
- **第二阶段（强化学习）**：开发对比学习增强的强化学习（contrastive learning empowered RL）方法，设计投影头（projection head）加速学习，并引入事件驱动增强奖励（event-driven augmented reward）提升操作安全性。

### 实验设置
- **仿真环境**：使用PyBullet物理引擎进行仿真实验。
- **真实实验**：在真实机器人平台上验证方法有效性。
- **基线对比**：与标准BC、RL等方法进行性能比较。

### 关键结果
- **训练效率**：所提方法相比基线显著加速训练过程。
- **任务成功率**：在操作任务中取得更高的成功率。
- **消融研究**：对比学习有效防止策略崩溃（policy collapse），验证了其必要性。

### 结论
本文提出的AR远程交互与两阶段学习框架，为灵巧机械臂-手系统的可扩展操作学习提供了高效解决方案。补充演示视频见 https://cyberyyc.github.io/。

## Overview
This paper focuses on the scalable robot learning for manipulation in the dexterous robot arm-hand systems, where the remote human-robot interactions via augmented reality (AR) are established to collect the expert demonstration data for improving efficiency. In such a system, we present a novel method to address the general manipulation task problem. Specifically, the proposed method consists of two phases: i) In the first phase for pretraining, the policy is created in a behavior cloning (BC) manner, through leveraging the learning data from our AR-based remote human-robot interaction system; ii) In the second phase, a contrastive learning empowered reinforcement learning (RL) method is developed to obtain more efficient and robust policy than the BC, and thus a projection head is designed to accelerate the learning progress. An event-driven augmented reward is adopted for enhancing the safety. To validate the proposed method, both the physics simulations via PyBullet and real-world experiments are carried out. The results demonstrate that compared to the baselines, our method not only significantly speeds up the training process, but also achieves much better performance in terms of the success rate for fulfilling the manipulation tasks. By conducting the ablation study, it is confirmed that the proposed RL with contrastive learning overcomes policy collapse. Supplementary demonstrations are available at https://cyberyyc.github.io/.

## Overview
This paper focuses on scalable robot learning for manipulation in dexterous robot arm-hand systems, where remote human-robot interactions via augmented reality (AR) are established to collect expert demonstration data for improving efficiency. In such a system, we present a novel method to address the general manipulation task problem. Specifically, the proposed method consists of two phases: i) In the first phase for pretraining, the policy is created in a behavior cloning (BC) manner, by leveraging learning data from our AR-based remote human-robot interaction system; ii) In the second phase, a contrastive learning empowered reinforcement learning (RL) method is developed to obtain a more efficient and robust policy than BC, and thus a projection head is designed to accelerate the learning progress. An event-driven augmented reward is adopted for enhancing safety. To validate the proposed method, both physics simulations via PyBullet and real-world experiments are carried out. The results demonstrate that compared to the baselines, our method not only significantly speeds up the training process but also achieves much better performance in terms of success rate for fulfilling manipulation tasks. By conducting an ablation study, it is confirmed that the proposed RL with contrastive learning overcomes policy collapse. Supplementary demonstrations are available at https://cyberyyc.github.io/.

## Content
This paper focuses on scalable robot learning for manipulation in dexterous robot arm-hand systems, where remote human-robot interactions via augmented reality (AR) are established to collect expert demonstration data for improving efficiency. In such a system, we present a novel method to address the general manipulation task problem. Specifically, the proposed method consists of two phases: i) In the first phase for pretraining, the policy is created in a behavior cloning (BC) manner, by leveraging learning data from our AR-based remote human-robot interaction system; ii) In the second phase, a contrastive learning empowered reinforcement learning (RL) method is developed to obtain a more efficient and robust policy than BC, and thus a projection head is designed to accelerate the learning progress. An event-driven augmented reward is adopted for enhancing safety. To validate the proposed method, both physics simulations via PyBullet and real-world experiments are carried out. The results demonstrate that compared to the baselines, our method not only significantly speeds up the training process but also achieves much better performance in terms of success rate for fulfilling manipulation tasks. By conducting an ablation study, it is confirmed that the proposed RL with contrastive learning overcomes policy collapse. Supplementary demonstrations are available at https://cyberyyc.github.io/.

## 参考
- http://arxiv.org/abs/2602.07341v2

## 개요
정교한 로봇 팔-손 시스템을 위한 확장 가능한 조작 학습 문제를 해결하기 위해, 본 논문은 증강 현실(AR) 기반 원격 인간-로봇 상호작용 시스템을 구축하여 전문가 시연 데이터를 효율적으로 수집한다. 제안된 방법은 두 단계로 구성된다: 첫 번째 단계는 AR 상호작용 시스템에서 수집된 데이터를 활용하여 행동 복제(BC) 방식으로 정책을 사전 학습한다; 두 번째 단계는 대비 학습 강화 강화 학습(RL) 방법을 개발하고, 투영 헤드를 설계하여 학습 과정을 가속화하며, 이벤트 기반 강화 보상을 채택하여 안전성을 향상시킨다. PyBullet 물리 시뮬레이션과 실제 로봇에서의 실험은 이 방법이 기준선에 비해 훈련 속도를 크게 가속화할 뿐만 아니라 조작 작업의 성공률을 현저히 향상시킨다는 것을 보여준다. 절제 연구는 대비 학습이 정책 붕괴 문제를 효과적으로 극복함을 확인한다.

## 핵심 내용
### 방법 아키텍처
본 논문은 정교한 로봇 팔-손 시스템을 위한 두 단계 학습 프레임워크를 제안한다:
- **첫 번째 단계(사전 학습)**: AR 기반 원격 인간-로봇 상호작용 시스템을 통해 전문가 시연 데이터를 수집하고, 행동 복제(BC) 방식으로 정책을 초기화한다.
- **두 번째 단계(강화 학습)**: 대비 학습 강화 강화 학습 방법을 개발하고, 투영 헤드를 설계하여 학습을 가속화하며, 이벤트 기반 강화 보상을 도입하여 조작 안전성을 향상시킨다.

### 실험 설정
- **시뮬레이션 환경**: PyBullet 물리 엔진을 사용하여 시뮬레이션 실험을 수행한다.
- **실제 실험**: 실제 로봇 플랫폼에서 방법의 유효성을 검증한다.
- **기준선 비교**: 표준 BC, RL 등의 방법과 성능을 비교한다.

### 주요 결과
- **훈련 효율성**: 제안된 방법은 기준선에 비해 훈련 과정을 크게 가속화한다.
- **작업 성공률**: 조작 작업에서 더 높은 성공률을 달성한다.
- **절제 연구**: 대비 학습이 정책 붕괴를 효과적으로 방지하여 그 필요성을 검증한다.

### 결론
본 논문에서 제안된 AR 원격 상호작용 및 두 단계 학습 프레임워크는 정교한 로봇 팔-손 시스템의 확장 가능한 조작 학습을 위한 효율적인 솔루션을 제공한다. 추가 시연 비디오는 https://cyberyyc.github.io/ 에서 확인할 수 있다.
