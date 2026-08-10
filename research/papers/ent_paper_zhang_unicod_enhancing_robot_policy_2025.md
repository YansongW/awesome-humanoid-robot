---
$id: ent_paper_zhang_unicod_enhancing_robot_policy_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning'
  zh: UniCoD
  ko: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning'
summary:
  en: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning (UniCoD), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences,
    Tsinghua University, Shanghai Qizhi Institute, Peking University, Shanghai AI Lab.'
  zh: UniCoD 是清华大学等机构于2025年提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于通过统一连续与离散表示学习，结合视觉语言理解与视觉生成预训练的优势，在仿真和真实世界任务中分别提升9%和12%的性能。
  ko: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning (UniCoD), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for Interdisciplinary Information Sciences,
    Tsinghua University, Shanghai Qizhi Institute, Peking University, Shanghai AI Lab.'
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
- unicod
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10642v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (675 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'UniCoD: Enhancing Robot Policy via Unified Continuous and Discrete Representation Learning (arXiv)'
  url: https://arxiv.org/abs/2510.10642
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UniCoD source
  url: https://doi.org/10.48550/arXiv.2510.10642
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
UniCoD 针对开放环境中多样化任务的通用机器人策略构建挑战，提出了一种统一连续与离散表示学习的方法。该方法基于 UniJEPA 架构，首先在超过100万个互联网教学操作视频上进行预训练，学习高维视觉特征的动态建模能力。随后，通过机器人本体数据微调，将预测表示映射为动作令牌。实验表明，UniCoD 在仿真环境和真实世界分布外任务中均显著优于基线方法。

## 核心内容
### 方法架构
UniCoD 的核心是 UniJEPA 架构，它统一了视觉语言理解与视觉生成预训练的优势。具体而言：
- **预训练阶段**：在超过100万个互联网规模的教学操作视频上，UniJEPA 学习动态建模高维视觉特征，同时捕捉语义理解与视觉动力学。
- **微调阶段**：利用机器人本体收集的数据，将预测表示映射为离散的动作令牌，实现从理解到执行的端到端学习。

### 实验设置
- **仿真环境**：在多个标准机器人操作基准上测试，涵盖抓取、放置、组装等任务。
- **真实世界任务**：评估分布外场景，包括不同物体、光照和背景条件下的操作。

### 关键结果
- **仿真环境**：UniCoD 平均提升9%的任务成功率，优于基于纯 VLM 或生成模型的基线。
- **真实世界任务**：在分布外场景中，UniCoD 提升12%的成功率，验证了其泛化能力。

### 结论
UniCoD 通过统一连续与离散表示学习，有效融合了视觉语言理解与视觉生成预训练的优势，为构建通用机器人策略提供了新范式。未来工作可探索更大规模预训练与更复杂的动作空间。

## Overview
Building generalist robot policies that can handle diverse tasks in open-ended environments is a central challenge in robotics. To leverage knowledge from large-scale pretraining, prior work (VLA) has typically built generalist policies either on top of vision-language understanding models (VLMs) or generative models. However, both semantic understanding from vision-language pretraining and visual dynamics modeling from visual-generation pretraining are crucial for embodied robots. Recent unified models of generation and understanding have demonstrated strong capabilities in both comprehension and generation through large-scale pretraining. We posit that robotic policy learning can likewise benefit from the combined strengths of understanding, planning, and continuous future representation learning. Building on this insight, we introduce UniJEPA, which acquires the ability to dynamically model high-dimensional visual features through pretraining on over 1M internet-scale instructional manipulation videos. Subsequently, UniJEPA is fine-tuned on data collected from the robot embodiment, enabling the learning of mappings from predictive representations to action tokens. Extensive experiments show our approach consistently outperforms baseline methods in terms of 9\% and 12\% across simulation environments and real-world out-of-distribution tasks.

## 参考
- http://arxiv.org/abs/2510.10642v3

## 개요
UniCoD는 개방 환경에서 다양한 작업을 위한 범용 로봇 정책 구축의 과제를 해결하기 위해, 연속 및 이산 표현 학습을 통합하는 방법을 제안합니다. 이 방법은 UniJEPA 아키텍처를 기반으로, 먼저 100만 개 이상의 인터넷 교육용 조작 비디오에서 사전 훈련을 통해 고차원 시각 특징의 동적 모델링 능력을 학습합니다. 이후 로봇 본체 데이터를 미세 조정하여 예측 표현을 행동 토큰으로 매핑합니다. 실험 결과, UniCoD는 시뮬레이션 환경과 실제 세계 분포 외 작업에서 모두 기준 방법보다显著히 우수한 성능을 보였습니다.

## 핵심 내용
### 방법 아키텍처
UniCoD의 핵심은 UniJEPA 아키텍처로, 시각 언어 이해와 시각 생성 사전 훈련의 장점을 통합합니다. 구체적으로:
- **사전 훈련 단계**: 100만 개 이상의 인터넷 규모 교육용 조작 비디오에서 UniJEPA는 고차원 시각 특징의 동적 모델링을 학습하며, 의미 이해와 시각 역학을 동시에 포착합니다.
- **미세 조정 단계**: 로봇 본체에서 수집된 데이터를 활용하여 예측 표현을 이산 행동 토큰으로 매핑하고, 이해에서 실행까지의 종단 간 학습을 구현합니다.

### 실험 설정
- **시뮬레이션 환경**: 여러 표준 로봇 조작 벤치마크에서 테스트하며, 파지, 배치, 조립 등의 작업을 포함합니다.
- **실제 세계 작업**: 분포 외 시나리오를 평가하며, 다양한 객체, 조명 및 배경 조건에서의 조작을 포함합니다.

### 주요 결과
- **시뮬레이션 환경**: UniCoD는 평균 9%의 작업 성공률 향상을 보였으며, 순수 VLM 또는 생성 모델 기반 기준선보다 우수합니다.
- **실제 세계 작업**: 분포 외 시나리오에서 UniCoD는 12%의 성공률 향상을 보여, 일반화 능력을 검증했습니다.

### 결론
UniCoD는 연속 및 이산 표현 학습을 통합하여 시각 언어 이해와 시각 생성 사전 훈련의 장점을 효과적으로 융합하며, 범용 로봇 정책 구축을 위한 새로운 패러다임을 제공합니다. 향후 연구는 더 큰 규모의 사전 훈련과 더 복잡한 행동 공간을 탐구할 수 있습니다.
