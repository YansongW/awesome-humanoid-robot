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
    via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (658
    chars, DeepSeek).'
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

## 参考
- Semantic Scholar search: Visual-tactile pretraining and online multitask learning for humanlike manipulation dexterity

## 개요
이 연구는 인간의 "관찰-실천" 학습 패러다임에서 영감을 받아 2단계 학습 프레임워크를 제안한다. 첫 번째 단계에서는 자기 지도 학습을 통해 인간 시연에서 시각-촉각 결합 표현을 학습하고, 두 번째 단계에서는 강화 학습과 온라인 모방 학습을 사용하여 통합 다작업 정책을 훈련한다. 이러한 분리 학습 설계는 로봇이 저비용 센싱(단안 이미지 + 이진 촉각 신호)만으로 일반화 가능한 조작 기술을 획득할 수 있게 한다. 통합 정책 기반의 다지 손 조작 시스템은 5가지 복잡한 작업, 25개 물체에서 85% 성공률을 달성하고, 훈련 작업과 손-물체 협응 패턴을 공유하는 3가지 미지의 작업으로 일반화할 수 있다.

## 핵심 내용
### 방법 아키텍처
- **2단계 학습 프레임워크**: 첫 번째 단계에서는 자기 지도 학습을 통해 인간 시연에서 시각-촉각 결합 표현을 추출하고, 두 번째 단계에서는 강화 학습과 온라인 모방 학습을 사용하여 통합 다작업 정책을 훈련
- **분리 학습 설계**: 표현 학습과 정책 학습을 분리하여 로봇이 저비용 센싱(단안 이미지 + 이진 촉각 신호)만으로 일반화 가능한 조작 기술을 획득할 수 있게 함

### 실험 설정
- **하드웨어 플랫폼**: 다지 손 로봇 시스템, 단안 카메라 및 이진 촉각 센서 장착
- **작업 및 물체**: 5가지 복잡한 조작 작업, 25가지 다양한 물체 포함
- **일반화 테스트**: 훈련 작업과 손-물체 협응 패턴을 공유하는 3가지 미지의 작업

### 주요 결과
- **성공률**: 5가지 복잡한 작업, 25개 물체에서 85% 평균 성공률 달성
- **일반화 능력**: 훈련 작업과 유사한 손-물체 협응 패턴을 가진 3가지 미지의 작업으로 성공적으로 일반화
- **센싱 비용**: 단안 이미지와 단순 이진 촉각 신호만 사용하여 센싱 시스템 복잡성을 크게 줄임

### 결론
이 연구는 시각-촉각 표현 학습과 정책 훈련을 분리하는 것의 효과성을 입증하며, 저비용 및 높은 일반화 능력을 갖춘 손재주 조작 시스템을 위한 실현 가능한 솔루션을 제공한다.
