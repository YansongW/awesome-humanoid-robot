---
$id: ent_paper_zhang_grape_generalizing_robot_polic_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GRAPE: Generalizing Robot Policy via Preference Alignment'
  zh: GRAPE
  ko: 'GRAPE: Generalizing Robot Policy via Preference Alignment'
summary:
  en: 'GRAPE: Generalizing Robot Policy via Preference Alignment (GRAPE), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by University of Chicago.'
  zh: GRAPE 是芝加哥大学于 2024 年提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于通过偏好对齐在轨迹层面优化策略，并利用成功与失败试次隐式建模奖励，从而显著提升模型对未见任务的泛化能力。实验表明，GRAPE 在域内和未见操作任务上分别将成功率提升
    51.79% 和 58.20%，同时可针对安全、效率等不同目标进行灵活对齐。
  ko: 'GRAPE: Generalizing Robot Policy via Preference Alignment (GRAPE), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by University of Chicago.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- grape
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.19309v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (934 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'GRAPE: Generalizing Robot Policy via Preference Alignment (arXiv)'
  url: https://arxiv.org/abs/2411.19309
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GRAPE source
  url: https://doi.org/10.48550/arXiv.2411.19309
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
GRAPE 针对现有视觉-语言-动作模型仅依赖成功轨迹进行行为克隆、导致泛化性差且难以适应多样化操作目标的问题，提出了一种基于偏好对齐的通用机器人策略。该方法在轨迹层面进行对齐，通过同时利用成功与失败试次隐式学习奖励函数，从而增强模型对多样任务的泛化能力。GRAPE 将复杂操作任务分解为独立阶段，并借助大型视觉-语言模型提出的关键点，通过自定义时空约束自动引导偏好建模。这些约束可灵活定制，以对齐安全、效率或任务成功等不同目标。在真实与仿真环境中的大量实验显示，GRAPE 显著提升了现有最优 VLA 模型的性能，在域内和未见操作任务上成功率分别提高 51.79% 和 58.20%，同时碰撞率降低 37.44%，轨迹步长缩短 11.15%。

## 核心内容
### 方法
- **偏好对齐**：GRAPE 在轨迹层面进行偏好对齐，而非仅依赖成功轨迹。它通过隐式建模奖励函数，同时从成功和失败试次中学习，从而提升对多样任务的泛化能力。
- **任务分解与约束**：复杂操作任务被分解为独立阶段。利用大型视觉-语言模型（如 GPT-4V）提出的关键点，自动生成自定义的时空约束，引导偏好建模。这些约束可灵活调整，以对齐不同目标（如安全、效率、任务成功）。

### 架构
- 基于现有的视觉-语言-动作模型（VLA）架构，通过偏好对齐模块进行扩展。该模块在训练过程中同时考虑成功与失败轨迹，优化策略的泛化性。

### 实验设置
- **环境**：在真实世界和仿真环境中评估，涵盖多种操作任务（如抓取、放置、组装等）。
- **基线**：与当前最优的 VLA 模型（如 RT-2、Octo）进行对比。
- **评估指标**：成功率、碰撞率、轨迹步长。

### 关键数字
- **成功率提升**：在域内任务上提升 51.79%，在未见任务上提升 58.20%。
- **安全对齐**：碰撞率降低 37.44%。
- **效率对齐**：轨迹步长缩短 11.15%。

### 结论
GRAPE 通过偏好对齐有效解决了 VLA 模型泛化性差和难以适应多样化目标的问题。其任务分解与自定义约束机制为机器人策略的灵活对齐提供了新范式。所有代码、模型和数据已开源。

## Overview
Despite the recent advancements of vision-language-action (VLA) models on a variety of robotics tasks, they suffer from critical issues such as poor generalizability to unseen tasks, due to their reliance on behavior cloning exclusively from successful rollouts. Furthermore, they are typically fine-tuned to replicate demonstrations collected by experts under different settings, thus introducing distribution bias and limiting their adaptability to diverse manipulation objectives, such as efficiency, safety, and task completion. To bridge this gap, we introduce GRAPE: Generalizing Robot Policy via Preference Alignment. Specifically, GRAPE aligns VLAs on a trajectory level and implicitly models reward from both successful and failure trials to boost generalizability to diverse tasks. Moreover, GRAPE breaks down complex manipulation tasks to independent stages and automatically guides preference modeling through customized spatiotemporal constraints with keypoints proposed by a large vision-language model. Notably, these constraints are flexible and can be customized to align the model with varying objectives, such as safety, efficiency, or task success. We evaluate GRAPE across a diverse array of tasks in both real-world and simulated environments. Experimental results demonstrate that GRAPE enhances the performance of state-of-the-art VLA models, increasing success rates on in-domain and unseen manipulation tasks by 51.79% and 58.20%, respectively. Additionally, GRAPE can be aligned with various objectives, such as safety and efficiency, reducing collision rates by 37.44% and rollout step-length by 11.15%, respectively. All code, models, and data are available at https://grape-vla.github.io/

## 参考
- http://arxiv.org/abs/2411.19309v2

## 개요
GRAPE는 기존의 비전-언어-행동 모델이 성공 궤적만을 사용한 행동 복제에 의존하여 일반화 성능이 낮고 다양한 조작 목표에 적응하기 어려운 문제를 해결하기 위해, 선호도 정렬 기반의 범용 로봇 정책을 제안한다. 이 방법은 궤적 수준에서 정렬을 수행하며, 성공 및 실패 시도를 동시에 활용하여 보상 함수를 암시적으로 학습함으로써 다양한 작업에 대한 모델의 일반화 능력을 강화한다. GRAPE는 복잡한 조작 작업을 독립적인 단계로 분해하고, 대규모 비전-언어 모델이 제안한 키포인트를 활용하여 사용자 정의 시공간 제약 조건을 통해 선호도 모델링을 자동으로 유도한다. 이러한 제약 조건은 안전, 효율성 또는 작업 성공과 같은 다양한 목표에 맞춰 유연하게 조정할 수 있다. 실제 및 시뮬레이션 환경에서의 광범위한 실험 결과, GRAPE는 기존 최고 수준의 VLA 모델 성능을 크게 향상시켜, 도메인 내 및 미지의 조작 작업에서 성공률을 각각 51.79% 및 58.20% 향상시키고, 충돌률을 37.44% 낮추며, 궤적 길이를 11.15% 단축했다.

## 핵심 내용
### 방법
- **선호도 정렬**: GRAPE는 성공 궤적에만 의존하지 않고 궤적 수준에서 선호도 정렬을 수행한다. 보상 함수를 암시적으로 모델링하여 성공 및 실패 시도에서 동시에 학습함으로써 다양한 작업에 대한 일반화 능력을 향상시킨다.
- **작업 분해 및 제약 조건**: 복잡한 조작 작업은 독립적인 단계로 분해된다. 대규모 비전-언어 모델(예: GPT-4V)이 제안한 키포인트를 활용하여 사용자 정의 시공간 제약 조건을 자동으로 생성하고, 이를 통해 선호도 모델링을 유도한다. 이러한 제약 조건은 안전, 효율성, 작업 성공과 같은 다양한 목표에 맞춰 유연하게 조정할 수 있다.

### 아키텍처
- 기존의 비전-언어-행동 모델(VLA) 아키텍처를 기반으로, 선호도 정렬 모듈을 통해 확장된다. 이 모듈은 훈련 과정에서 성공 및 실패 궤적을 동시에 고려하여 정책의 일반화 성능을 최적화한다.

### 실험 설정
- **환경**: 실제 세계 및 시뮬레이션 환경에서 평가되며, 다양한 조작 작업(예: 집기, 놓기, 조립 등)을 포함한다.
- **기준 모델**: 현재 최고 수준의 VLA 모델(예: RT-2, Octo)과 비교한다.
- **평가 지표**: 성공률, 충돌률, 궤적 길이.

### 주요 수치
- **성공률 향상**: 도메인 내 작업에서 51.79% 향상, 미지의 작업에서 58.20% 향상.
- **안전 정렬**: 충돌률 37.44% 감소.
- **효율성 정렬**: 궤적 길이 11.15% 단축.

### 결론
GRAPE는 선호도 정렬을 통해 VLA 모델의 일반화 성능 저하 및 다양한 목표 적응 문제를 효과적으로 해결한다. 작업 분해 및 사용자 정의 제약 조건 메커니즘은 로봇 정책의 유연한 정렬을 위한 새로운 패러다임을 제시한다. 모든 코드, 모델 및 데이터는 오픈소스로 공개되었다.
