---
$id: ent_paper_kareer_emergence_of_human_to_robot_tr_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Emergence of Human to Robot Transfer in Vision-Language-Action Models
  zh: Emergence of Human to Robot Transfer in Vision-Language-Action Models
  ko: Emergence of Human to Robot Transfer in Vision-Language-Action Models
summary:
  en: Emergence of Human to Robot Transfer in Vision-Language-Action Models (Emergence of Human to Robot Transfer in Vision-Language-Action
    Models), is a 2025 large vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Georgia
    Institute of Technology.
  zh: Physical Intelligence与Georgia Institute of Technology于2025年提出一种视觉-语言-动作模型（VLA），通过简单协同训练方法实现人类视频数据到机器人技能的迁移。研究发现，当模型在足够多样的场景、任务和本体上进行预训练后，人类到机器人的迁移能力会自然涌现，其核心在于多样化预训练产生了跨本体的表征。
  ko: Emergence of Human to Robot Transfer in Vision-Language-Action Models (Emergence of Human to Robot Transfer in Vision-Language-Action
    Models), is a 2025 large vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Georgia
    Institute of Technology.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- emergence_of_human_to_robot_tr
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.22414v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (740 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Emergence of Human to Robot Transfer in Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2512.22414
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Emergence of Human to Robot Transfer in Vision-Language-Action Models source
  url: https://doi.org/10.48550/arXiv.2512.22414
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究探索了如何利用易获取的人类视频数据训练机器人操作模型。传统方法需要人工建立人机映射，而本文受大语言模型启发，提出通过大规模多样化预训练实现迁移能力的涌现。实验表明，当VLA模型在充足场景、任务和机器人本体上预训练后，无需显式对齐即可将人类演示中的技能迁移至机器人。分析显示，这种能力源于预训练过程形成了与具体本体无关的共享表征。在泛化测试中，该方法使仅存在于人类数据中的任务表现提升近一倍。

## 核心内容
### 核心方法
- 提出**协同训练（co-training）**框架：同时使用人类视频数据和机器人数据训练VLA模型
- 预训练阶段需覆盖**足够多样的场景、任务和机器人本体**，这是迁移能力涌现的关键条件

### 关键发现
- **涌现现象**：人类到机器人的迁移能力并非显式编程实现，而是在模型规模和数据多样性达到阈值后自然出现
- **表征分析**：多样化预训练使模型学习到**本体无关（embodiment-agnostic）**的共享表征，人类与机器人数据在隐空间中对齐
- **性能提升**：在仅包含人类数据的泛化场景中，该方法使任务成功率**提升近100%**（相比无人类数据预训练基线）

### 实验设置
- 使用Physical Intelligence的VLA架构，在包含**数百种任务**的混合数据集上预训练
- 评估包括：直接迁移（人类演示→机器人执行）、跨场景泛化、新物体操作等
- 对比实验验证了预训练数据多样性（场景数、任务数、本体类型数）与迁移能力的正相关关系

### 结论
该工作证明：通过规模化多样化预训练，VLA模型可以自动建立人类与机器人之间的技能映射，为利用海量人类视频数据训练机器人提供了可行路径。

## Overview
Vision-language-action (VLA) models can enable broad open world generalization, but require large and diverse datasets. It is appealing to consider whether some of this data can come from human videos, which cover diverse real-world situations and are easy to obtain. However, it is difficult to train VLAs with human videos alone, and establishing a mapping between humans and robots requires manual engineering and presents a major research challenge. Drawing inspiration from advances in large language models, where the ability to learn from diverse supervision emerges with scale, we ask whether a similar phenomenon holds for VLAs that incorporate human video data. We introduce a simple co-training recipe, and find that human-to-robot transfer emerges once the VLA is pre-trained on sufficient scenes, tasks, and embodiments. Our analysis suggests that this emergent capability arises because diverse pretraining produces embodiment-agnostic representations for human and robot data. We validate these findings through a series of experiments probing human to robot skill transfer and find that with sufficiently diverse robot pre-training our method can nearly double the performance on generalization settings seen only in human data.

## 参考
- http://arxiv.org/abs/2512.22414v1

## 개요
이 연구는 쉽게 얻을 수 있는 인간 비디오 데이터를 활용해 로봇 조작 모델을 훈련하는 방법을 탐구한다. 전통적인 방법은 인간-로봇 매핑을 수동으로 구축해야 하지만, 본 논문은 대규모 언어 모델에서 영감을 받아 대규모 다양화 사전 훈련을 통해 전이 능력의 창발을 실현하는 것을 제안한다. 실험 결과, VLA 모델이 충분한 장면, 작업, 로봇 본체에서 사전 훈련되었을 때, 명시적 정렬 없이도 인간 시연의 기술을 로봇으로 전이할 수 있음을 보여준다. 분석에 따르면 이러한 능력은 사전 훈련 과정에서 특정 본체와 무관한 공유 표현이 형성되었기 때문이다. 일반화 테스트에서 이 방법은 인간 데이터에만 존재하는 작업의 성능을 거의 두 배로 향상시켰다.

## 핵심 내용
### 핵심 방법
- **공동 훈련(co-training)** 프레임워크 제안: 인간 비디오 데이터와 로봇 데이터를 동시에 사용하여 VLA 모델 훈련
- 사전 훈련 단계는 **충분히 다양한 장면, 작업, 로봇 본체**를 포함해야 하며, 이는 전이 능력 창발의 핵심 조건

### 주요 발견
- **창발 현상**: 인간에서 로봇으로의 전이 능력은 명시적 프로그래밍으로 구현된 것이 아니라, 모델 규모와 데이터 다양성이 임계값에 도달한 후 자연스럽게 나타남
- **표현 분석**: 다양한 사전 훈련을 통해 모델이 **본체 무관(embodiment-agnostic)** 공유 표현을 학습하며, 인간과 로봇 데이터가 잠재 공간에서 정렬됨
- **성능 향상**: 인간 데이터만 포함된 일반화 장면에서 이 방법은 작업 성공률을 **거의 100% 향상**시킴 (인간 데이터 사전 훈련이 없는 기준선 대비)

### 실험 설정
- Physical Intelligence의 VLA 아키텍처를 사용하여 **수백 가지 작업**을 포함한 혼합 데이터셋에서 사전 훈련
- 평가 항목: 직접 전이(인간 시연→로봇 실행), 교차 장면 일반화, 새로운 객체 조작 등
- 비교 실험을 통해 사전 훈련 데이터 다양성(장면 수, 작업 수, 본체 유형 수)과 전이 능력 간의 양의 상관관계 검증

### 결론
이 연구는 대규모 다양화 사전 훈련을 통해 VLA 모델이 인간과 로봇 간의 기술 매핑을 자동으로 구축할 수 있음을 증명하며, 방대한 인간 비디오 데이터를 활용한 로봇 훈련의 실현 가능한 경로를 제시한다.
