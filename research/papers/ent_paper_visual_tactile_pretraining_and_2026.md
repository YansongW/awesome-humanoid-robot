---
$id: ent_paper_visual_tactile_pretraining_and_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Visual-tactile pretraining and online multitask learning for humanlike manipulation dexterity
  zh: Visual-tactile pretraining and online multitask learning for humanlike manipulation dexterity
  ko: Visual-tactile pretraining and online multitask learning for humanlike manipulation dexterity
summary:
  en: Visual-tactile pretraining and online multitask learning for humanlike manipulation dexterity is a 2026 work on manipulation
    for humanoid robots.
  zh: 这是一项2026年关于人形机器人灵巧操作的研究，由研究团队提出。核心贡献在于通过自监督学习从人类演示中提取视觉-触觉表征，并利用强化学习与在线模仿学习训练统一多任务策略，使多指机械手仅凭单目图像和简单二进制触觉信号即可完成复杂操作任务。
  ko: Visual-tactile pretraining and online multitask learning for humanlike manipulation dexterity is a 2026 work on manipulation
    for humanoid robots.
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
- visual_tactile_pretraining_and
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: Visual-tactile pretraining
    and online multitask learning for humanlike manipulation dexterity. [2026-07-29] zh content backfilled from English abstract
    via scripts/sinicize_english_cards.py'
sources:
- id: src_001
  type: website
  title: Visual-tactile pretraining and online multitask learning for humanlike manipulation dexterity project page
  url: https://www.science.org/doi/10.1126/scirobotics.ady2869
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该工作受人类“观察-实践”学习范式启发，提出两阶段学习框架。第一阶段通过自监督学习从人类演示中学习视觉-触觉联合表征，第二阶段利用强化学习与在线模仿学习训练统一多任务策略。这种解耦学习方式使机器人仅使用低成本传感（单目图像+二进制触觉信号）即可获得可泛化的操作技能。基于统一策略构建的多指手操作系统在5项复杂任务、25个物体上达到85%成功率，并能泛化至3个与训练任务共享手-物协调模式的未见任务。

## 核心内容
### 方法架构
- **两阶段学习框架**：第一阶段通过自监督学习从人类演示中提取视觉-触觉联合表征，第二阶段利用强化学习与在线模仿学习训练统一多任务策略
- **解耦学习设计**：将表征学习与策略学习分离，使机器人能仅依赖低成本传感（单目图像+二进制触觉信号）获得可泛化操作技能

### 实验设置
- **硬件平台**：多指机械手系统，配备单目摄像头和二进制触觉传感器
- **任务与物体**：5项复杂操作任务，涉及25种不同物体
- **泛化测试**：3个与训练任务共享手-物协调模式的未见任务

### 关键结果
- **成功率**：在5项复杂任务、25个物体上达到85%平均成功率
- **泛化能力**：成功泛化至3个未见任务，这些任务与训练任务具有相似的手-物协调模式
- **传感成本**：仅使用单目图像和简单二进制触觉信号，显著降低传感系统复杂度

### 结论
该工作证明了解耦学习视觉-触觉表征与策略训练的有效性，为低成本、高泛化能力的灵巧操作系统提供了可行方案。

## Overview
Achieving humanlike dexterity with anthropomorphic multifingered robotic hands requires precise finger coordination. However, dexterous manipulation remains highly challenging because of high-dimensional action-observation spaces, complex hand-object contact dynamics, and frequent occlusions. To address this, we drew inspiration from the human learning paradigm of observation and practice and propose a two-stage learning framework by learning visual-tactile integration representations via self-supervised learning from human demonstrations. We trained a unified multitask policy through reinforcement learning and online imitation learning. This decoupled learning enabled the robot to acquire generalizable manipulation skills using only monocular images and simple binary tactile signals. With the unified policy, we built a multifingered hand manipulation system that performs multiple complicated tasks with low-cost sensing. It achieved an 85% success rate across five complex tasks and 25 objects and further generalized to three unseen tasks that share similar hand-object coordination patterns with the training tasks.

## 개요
인간형 다지 로봇 손으로 인간과 같은 손재주를 달성하려면 정밀한 손가락 협응이 필요합니다. 그러나 고차원의 행동-관찰 공간, 복잡한 손-물체 접촉 역학, 빈번한 폐색으로 인해 정교한 조작은 여전히 매우 어려운 과제입니다. 이를 해결하기 위해 우리는 관찰과 연습이라는 인간 학습 패러다임에서 영감을 얻어, 인간 시연으로부터 자기 지도 학습을 통해 시각-촉각 통합 표현을 학습하는 2단계 학습 프레임워크를 제안합니다. 강화 학습과 온라인 모방 학습을 통해 통합된 멀티태스크 정책을 훈련했습니다. 이 분리 학습을 통해 로봇은 단안 이미지와 단순한 이진 촉각 신호만으로 일반화 가능한 조작 기술을 습득할 수 있었습니다. 통합 정책을 바탕으로 저비용 센싱으로 여러 복잡한 작업을 수행하는 다지 손 조작 시스템을 구축했습니다. 이 시스템은 5가지 복잡한 작업과 25개 물체에 대해 85%의 성공률을 달성했으며, 훈련 작업과 유사한 손-물체 협응 패턴을 공유하는 3가지 미지의 작업으로 추가 일반화되었습니다.

## 핵심 내용
인간형 다지 로봇 손으로 인간과 같은 손재주를 달성하려면 정밀한 손가락 협응이 필요합니다. 그러나 고차원의 행동-관찰 공간, 복잡한 손-물체 접촉 역학, 빈번한 폐색으로 인해 정교한 조작은 여전히 매우 어려운 과제입니다. 이를 해결하기 위해 우리는 관찰과 연습이라는 인간 학습 패러다임에서 영감을 얻어, 인간 시연으로부터 자기 지도 학습을 통해 시각-촉각 통합 표현을 학습하는 2단계 학습 프레임워크를 제안합니다. 강화 학습과 온라인 모방 학습을 통해 통합된 멀티태스크 정책을 훈련했습니다. 이 분리 학습을 통해 로봇은 단안 이미지와 단순한 이진 촉각 신호만으로 일반화 가능한 조작 기술을 습득할 수 있었습니다. 통합 정책을 바탕으로 저비용 센싱으로 여러 복잡한 작업을 수행하는 다지 손 조작 시스템을 구축했습니다. 이 시스템은 5가지 복잡한 작업과 25개 물체에 대해 85%의 성공률을 달성했으며, 훈련 작업과 유사한 손-물체 협응 패턴을 공유하는 3가지 미지의 작업으로 추가 일반화되었습니다.

## 参考
- Semantic Scholar search: Visual-tactile pretraining and online multitask learning for humanlike manipulation dexterity
