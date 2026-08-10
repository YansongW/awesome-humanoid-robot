---
$id: ent_paper_sridhar_ricl_adding_in_context_adaptab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models'
  zh: RICL
  ko: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models'
summary:
  en: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models (RICL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Pennsylvania, and published at CoRL25.'
  zh: RICL 是由宾夕法尼亚大学在 CoRL25 上提出的方法，旨在为预训练的视觉-语言-动作模型（VLA）注入上下文学习能力。其核心贡献是仅需 10-20 条新任务演示，无需参数微调即可提升机器人操作性能，并进一步支持参数更新以增强效果。
  ko: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models (RICL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Pennsylvania, and published at CoRL25.'
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
- ricl
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.02062v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (826 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2508.02062
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RICL source
  url: https://doi.org/10.48550/arXiv.2508.02062
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
多任务 VLA 模型作为机器人通用基础模型已展现出潜力，但用户难以轻松教会它们改进。RICL 通过后训练微调策略，利用小型机器人演示数据集，使 VLA 模型获得上下文学习能力。用户提供少量新任务演示后，RICL 自动提取最相关部分嵌入模型上下文，从而执行新任务并提升性能。该方法应用于 π₀-FAST VLA 模型，在多种操作任务中仅用 20 条演示即实现显著改进，且无需参数更新；若允许参数更新，性能进一步提升。

## 核心内容
### 方法
- **问题背景**：预训练的 VLA 模型（如 π₀-FAST）虽能零样本执行新任务，但缺乏上下文学习能力，用户难以高效指导其改进。
- **核心思路**：通过后训练微调（RICL）注入上下文适应性，无需从头训练。微调使用小型机器人演示数据集，使模型学会从上下文中的演示片段提取任务信息。
- **工作流程**：用户提供 10-20 条新任务演示 → RICL 检索最相关部分嵌入 VLA 上下文 → 模型利用 ICL 执行任务，无需参数更新。

### 实验设置
- **基础模型**：π₀-FAST VLA，一个多任务视觉-语言-动作模型。
- **数据集**：小型机器人演示数据集，用于后训练微调。
- **任务**：多种新操作任务，每任务仅 20 条演示。
- **评估指标**：任务成功率。

### 关键结果
- **无参数更新**：RICL 使 π₀-FAST 在新任务上实现大幅性能提升，仅需 20 条演示。
- **有参数更新**：若允许对目标任务演示进行参数微调，RICL 进一步显著提升性能。
- **代码与模型**：论文发布 RICL-π₀-FAST 的代码和模型权重，首次为机器人操作任务提供简单上下文学习接口。

### 结论
RICL 证明了通过后训练微调，可向预训练 VLA 模型注入上下文学习能力，使用户仅凭少量演示即可高效指导模型改进，无需复杂参数调整。

## Overview
Multi-task ``vision-language-action'' (VLA) models have recently demonstrated increasing promise as generalist foundation models for robotics, achieving non-trivial performance out of the box on new tasks in new environments. However, for such models to be truly useful, an end user must have easy means to teach them to improve. For language and vision models, the emergent ability to perform in-context learning (ICL) has proven to be a versatile and highly useful interface to easily teach new tasks with no parameter finetuning. Unfortunately, VLAs pre-trained with imitation learning objectives do not naturally acquire ICL abilities. In this paper, we demonstrate that, with the right finetuning recipe and a small robot demonstration dataset, it is possible to inject in-context adaptability post hoc into such a VLA. After retraining for in-context learning (RICL), our system permits an end user to provide a small number (10-20) of demonstrations for a new task. RICL then fetches the most relevant portions of those demonstrations into the VLA context to exploit ICL, performing the new task and boosting task performance. We apply RICL to inject ICL into the $π_{0}$-FAST VLA, and show that it permits large in-context improvements for a variety of new manipulation tasks with only 20 demonstrations per task, without any parameter updates. When parameter updates on the target task demonstrations is possible, RICL finetuning further boosts performance. We release code and model weights for RICL-$π_{0}$-FAST alongside the paper to enable, for the first time, a simple in-context learning interface for new manipulation tasks. Website: https://ricl-vla.github.io.

## 参考
- http://arxiv.org/abs/2508.02062v1

## 개요
멀티태스크 VLA 모델은 로봇 범용 기반 모델로서 잠재력을 보여주었지만, 사용자가 이를 쉽게 개선하도록 가르치기는 어렵습니다. RICL은 후훈련 미세 조정 전략을 통해 소형 로봇 시연 데이터셋을 활용하여 VLA 모델에 문맥 학습 능력을 부여합니다. 사용자가 소량의 새로운 작업 시연을 제공하면 RICL이 가장 관련성 높은 부분을 자동으로 추출하여 모델 문맥에 내장함으로써 새로운 작업을 수행하고 성능을 향상시킵니다. 이 방법은 π₀-FAST VLA 모델에 적용되어 다양한 조작 작업에서 단 20개의 시연만으로도 상당한 개선을 달성하며, 매개변수 업데이트가 필요 없습니다. 매개변수 업데이트를 허용하면 성능이 더욱 향상됩니다.

## 핵심 내용
### 방법
- **문제 배경**: 사전 훈련된 VLA 모델(예: π₀-FAST)은 제로샷으로 새로운 작업을 수행할 수 있지만 문맥 학습 능력이 부족하여 사용자가 효율적으로 개선을 지도하기 어렵습니다.
- **핵심 아이디어**: 후훈련 미세 조정(RICL)을 통해 처음부터 훈련하지 않고 문맥 적응성을 주입합니다. 미세 조정은 소형 로봇 시연 데이터셋을 사용하여 모델이 문맥 속 시연 조각에서 작업 정보를 추출하도록 학습시킵니다.
- **작동 흐름**: 사용자가 10-20개의 새로운 작업 시연을 제공 → RICL이 가장 관련성 높은 부분을 검색하여 VLA 문맥에 내장 → 모델이 ICL을 활용하여 매개변수 업데이트 없이 작업을 수행합니다.

### 실험 설정
- **기반 모델**: π₀-FAST VLA, 멀티태스크 비전-언어-행동 모델.
- **데이터셋**: 후훈련 미세 조정에 사용되는 소형 로봇 시연 데이터셋.
- **작업**: 다양한 새로운 조작 작업, 각 작업당 20개의 시연만 사용.
- **평가 지표**: 작업 성공률.

### 주요 결과
- **매개변수 업데이트 없음**: RICL은 π₀-FAST가 새로운 작업에서 단 20개의 시연만으로도 큰 성능 향상을 달성하게 합니다.
- **매개변수 업데이트 있음**: 목표 작업 시연에 대한 매개변수 미세 조정을 허용하면 RICL이 성능을 더욱 크게 향상시킵니다.
- **코드 및 모델**: 논문은 RICL-π₀-FAST의 코드와 모델 가중치를 공개하여 로봇 조작 작업에 처음으로 간단한 문맥 학습 인터페이스를 제공합니다.

### 결론
RICL은 후훈련 미세 조정을 통해 사전 훈련된 VLA 모델에 문맥 학습 능력을 주입할 수 있음을 입증하며, 사용자가 복잡한 매개변수 조정 없이 소량의 시연만으로 모델 개선을 효율적으로 지도할 수 있게 합니다.
