---
$id: ent_paper_humanoid_policy_human_policy_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Policy ~ Human Policy
  zh: Humanoid Policy ~ Human Policy
  ko: Humanoid Policy ~ Human Policy
summary:
  en: Humanoid Policy ~ Human Policy is a 2025 work on manipulation for humanoid robots.
  zh: Humanoid Policy ~ Human Policy 是2025年关于人形机器人操作的研究工作。该工作提出利用第一人称人类演示数据作为跨本体训练数据，通过构建 Human Action Transformer (HAT) 模型来弥合人类与人形机器人之间的本体差异。核心贡献在于使用更易扩展的人类数据显著提升了机器人策略的泛化能力和鲁棒性。
  ko: Humanoid Policy ~ Human Policy is a 2025 work on manipulation for humanoid robots.
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
- humanoid_policy_human_policy
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.13441v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (647 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Humanoid Policy ~ Human Policy (arXiv)
  url: https://arxiv.org/abs/2503.13441
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Humanoid Policy ~ Human Policy project page
  url: https://human-as-robot.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对人形机器人操作策略训练中数据采集成本高、难以规模化的问题，探索了利用第一人称人类演示数据作为跨本体训练数据的新方法。研究者从数据和建模两个角度着手，首先收集了与机器人操作任务直接对齐的第一人称任务导向数据集 PH2D，然后训练了 Human Action Transformer (HAT) 模型。HAT 模型统一了人类和人形机器人的状态-动作空间，能够通过可微分的重定向将人类动作映射到机器人动作。实验表明，结合少量机器人数据共同训练，人类数据能显著提升策略的泛化能力和鲁棒性，同时大幅提高数据采集效率。

## 核心内容
### 方法概述
- **数据层面**：收集了第一人称任务导向数据集 PH2D，该数据集直接与人形机器人操作演示对齐，解决了人类与人形机器人之间的本体差异问题。
- **模型层面**：训练了 Human Action Transformer (HAT) 模型，其状态-动作空间对人类和人形机器人是统一的，能够通过可微分重定向将人类动作映射到机器人动作。

### 核心架构
- HAT 模型直接建模人类和人形机器人为不同本体，无需额外监督信号。
- 模型与较小规模的机器人数据共同训练，实现跨本体学习。

### 实验设置与结果
- 实验验证了人类数据对策略泛化能力和鲁棒性的提升效果。
- 与仅使用机器人数据的方法相比，HAT 在数据采集效率上显著更优。
- 代码和数据已开源：https://human-as-robot.github.io/

## Overview
Training manipulation policies for humanoid robots with diverse data enhances their robustness and generalization across tasks and platforms. However, learning solely from robot demonstrations is labor-intensive, requiring expensive tele-operated data collection which is difficult to scale. This paper investigates a more scalable data source, egocentric human demonstrations, to serve as cross-embodiment training data for robot learning. We mitigate the embodiment gap between humanoids and humans from both the data and modeling perspectives. We collect an egocentric task-oriented dataset (PH2D) that is directly aligned with humanoid manipulation demonstrations. We then train a human-humanoid behavior policy, which we term Human Action Transformer (HAT). The state-action space of HAT is unified for both humans and humanoid robots and can be differentiably retargeted to robot actions. Co-trained with smaller-scale robot data, HAT directly models humanoid robots and humans as different embodiments without additional supervision. We show that human data improves both generalization and robustness of HAT with significantly better data collection efficiency. Code and data: https://human-as-robot.github.io/

## 参考
- http://arxiv.org/abs/2503.13441v3

## 개요
이 연구는 휴머노이드 로봇 조작 정책 훈련에서 데이터 수집 비용이 높고 확장이 어려운 문제를 해결하기 위해, 1인칭 인간 시연 데이터를 교차 본체 훈련 데이터로 활용하는 새로운 방법을 탐구한다. 연구진은 데이터와 모델링 두 측면에서 접근하여, 먼저 로봇 조작 작업과 직접적으로 정렬된 1인칭 작업 지향 데이터셋 PH2D를 수집하고, 이후 Human Action Transformer (HAT) 모델을 훈련했다. HAT 모델은 인간과 휴머노이드 로봇의 상태-행동 공간을 통합하며, 미분 가능한 리타게팅을 통해 인간의 행동을 로봇의 행동으로 매핑할 수 있다. 실험 결과, 소량의 로봇 데이터와 함께 공동 훈련할 때 인간 데이터가 정책의 일반화 능력과 견고성을 크게 향상시키고, 데이터 수집 효율을 대폭 높이는 것으로 나타났다.

## 핵심 내용
### 방법 개요
- **데이터 측면**: 휴머노이드 로봇 조작 시연과 직접적으로 정렬된 1인칭 작업 지향 데이터셋 PH2D를 수집하여, 인간과 휴머노이드 로봇 간의 본체 차이 문제를 해결했다.
- **모델 측면**: Human Action Transformer (HAT) 모델을 훈련했으며, 이 모델의 상태-행동 공간은 인간과 휴머노이드 로봇에 대해 통합되어 있고, 미분 가능한 리타게팅을 통해 인간의 행동을 로봇의 행동으로 매핑할 수 있다.

### 핵심 아키텍처
- HAT 모델은 인간과 휴머노이드 로봇을 서로 다른 본체로 직접 모델링하며, 추가적인 감독 신호가 필요 없다.
- 모델은 소규모 로봇 데이터와 공동 훈련하여 교차 본체 학습을 구현한다.

### 실험 설정 및 결과
- 실험을 통해 인간 데이터가 정책의 일반화 능력과 견고성 향상에 미치는 효과를 검증했다.
- 로봇 데이터만 사용하는 방법과 비교하여, HAT는 데이터 수집 효율에서 현저히 우수하다.
- 코드와 데이터는 오픈소스로 공개되었다: https://human-as-robot.github.io/
