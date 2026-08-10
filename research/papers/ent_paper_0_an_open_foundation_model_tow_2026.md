---
$id: ent_paper_0_an_open_foundation_model_tow_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation'
  zh: 'Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation'
  ko: 'Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation'
summary:
  en: 'Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: Ψ₀（Psi-Zero）是一个面向人形机器人全身控制与操作任务的开源基础模型，由研究团队于2026年提出。其核心贡献在于提出分阶段训练范式，通过解耦人类与人形机器人的运动差异，仅用约800小时人类视频和30小时机器人数据，即在多项任务上超越使用10倍以上数据训练的基线模型，成功率提升超40%。
  ko: 'Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation is a 2026 work on loco-manipulation and whole-body-control
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
- '0'
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.12263v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (847 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Ψ₀: An Open Foundation Model Towards Universal Humanoid Loco-Manipulation (arXiv)'
  url: https://arxiv.org/abs/2603.12263
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有方法通常依赖大规模人类与人形机器人数据的联合训练，但因两者运动学与动作模式存在根本差异，导致数据效率与模型性能受限。Ψ₀通过分阶段学习策略解决这一问题：首先在人类第一人称视频上自回归预训练VLM骨干网络，获取泛化的视觉-动作表征；随后基于高质量人形机器人轨迹数据，后训练一个基于流的动作专家模型，实现精准的关节控制。研究还发现，相比使用嘈杂网络视频或异构机器人数据集，预训练高质量人类操作数据、后训练领域特定真实机器人轨迹的数据配方更为关键。在真实世界实验中，Ψ₀仅需约800小时人类视频与30小时机器人数据，即在多项操作任务上显著优于使用10倍以上数据训练的基线模型。

## 核心内容
### 方法架构
- **分阶段训练范式**：将学习过程解耦为两个阶段，最大化异构数据源的利用效率。
  - **阶段一：VLM骨干预训练**：在大规模第一人称人类视频上，通过自回归方式预训练视觉-语言模型（VLM）骨干，学习可泛化的视觉-动作表征。
  - **阶段二：动作专家后训练**：基于高质量人形机器人轨迹数据，训练基于流的动作专家模型，学习精确的机器人关节控制。

### 关键发现：数据配方
- 与依赖大规模噪声网络视频或跨形态机器人数据集的方法不同，Ψ₀证明以下数据配方更优：
  - **预训练数据**：高质量第一人称人类操作视频（约800小时）。
  - **后训练数据**：领域特定的真实世界人形机器人轨迹（约30小时）。
- 该配方显著提升数据效率与模型性能。

### 实验设置与结果
- **真实世界实验**：在多项人形机器人操作任务上评估。
- **性能对比**：
  - Ψ₀在总体成功率上，超越使用10倍以上数据训练的基线模型超过40%。
  - 仅使用约800小时人类视频与30小时机器人数据，即达到最优性能。

### 开源生态
- 将开源完整生态系统，包括：
  - 数据处理与训练流水线。
  - 人形机器人基础模型。
  - 实时动作推理引擎。

## Overview
We introduce $Ψ_0$ (Psi-Zero), an open foundation model to address challenging humanoid loco-manipulation tasks. While existing approaches often attempt to address this fundamental problem by co-training on large and diverse human and humanoid data, we argue that this strategy is suboptimal due to the fundamental kinematic and motion disparities between humans and humanoid robots. Therefore, data efficiency and model performance remain unsatisfactory despite the considerable data volume. To address this challenge, \ours\;decouples the learning process to maximize the utility of heterogeneous data sources. Specifically, we propose a staged training paradigm with different learning objectives: First, we autoregressively pre-train a VLM backbone on large-scale egocentric human videos to acquire generalizable visual-action representations. Then, we post-train a flow-based action expert on high-quality humanoid robot data to learn precise robot joint control. Our research further identifies a critical yet often overlooked data recipe: in contrast to approaches that scale with noisy Internet clips or heterogeneous cross-embodiment robot datasets, we demonstrate that pre-training on high-quality egocentric human manipulation data followed by post-training on domain-specific real-world humanoid trajectories yields superior performance. Extensive real-world experiments demonstrate that \ours\ achieves the best performance using only about 800 hours of human video data and 30 hours of real-world robot data, outperforming baselines pre-trained on more than 10$\times$ as much data by over 40\% in overall success rate across multiple tasks. We will open-source the entire ecosystem to the community, including a data processing and training pipeline, a humanoid foundation model, and a real-time action inference engine.

## 参考
- http://arxiv.org/abs/2603.12263v1

## 개요
기존 방법들은 일반적으로 대규모 인간 및 휴머노이드 로봇 데이터의 결합 훈련에 의존하지만, 두 데이터의 운동학 및 동작 패턴에 근본적인 차이가 있어 데이터 효율성과 모델 성능이 제한됩니다. Ψ₀는 단계적 학습 전략을 통해 이 문제를 해결합니다: 먼저 인간의 1인칭 비디오에서 자기회귀적으로 VLM 백본 네트워크를 사전 훈련하여 일반화된 시각-동작 표현을 획득하고, 이후 고품질 휴머노이드 로봇 궤적 데이터를 기반으로 플로우 기반 동작 전문가 모델을 후훈련하여 정밀한 관절 제어를 구현합니다. 연구는 또한 노이즈가 많은 네트워크 비디오나 이종 로봇 데이터셋을 사용하는 것보다, 고품질 인간 조작 데이터를 사전 훈련하고 도메인 특정 실제 로봇 궤적을 후훈련하는 데이터 레시피가 더 중요하다는 것을 발견했습니다. 실제 세계 실험에서 Ψ₀는 약 800시간의 인간 비디오와 30시간의 로봇 데이터만으로 여러 조작 작업에서 10배 이상의 데이터로 훈련된 기준 모델을 크게 능가했습니다.

## 핵심 내용
### 방법 아키텍처
- **단계적 훈련 패러다임**: 학습 과정을 두 단계로 분리하여 이종 데이터 소스의 활용 효율을 극대화합니다.
  - **1단계: VLM 백본 사전 훈련**: 대규모 1인칭 인간 비디오에서 자기회귀 방식으로 시각-언어 모델(VLM) 백본을 사전 훈련하여 일반화 가능한 시각-동작 표현을 학습합니다.
  - **2단계: 동작 전문가 후훈련**: 고품질 휴머노이드 로봇 궤적 데이터를 기반으로 플로우 기반 동작 전문가 모델을 훈련하여 정밀한 로봇 관절 제어를 학습합니다.

### 핵심 발견: 데이터 레시피
- 대규모 노이즈 네트워크 비디오나 교차 형태 로봇 데이터셋에 의존하는 방법과 달리, Ψ₀는 다음 데이터 레시피가 더 우수함을 입증합니다:
  - **사전 훈련 데이터**: 고품질 1인칭 인간 조작 비디오(약 800시간).
  - **후훈련 데이터**: 도메인 특정 실제 세계 휴머노이드 로봇 궤적(약 30시간).
- 이 레시피는 데이터 효율성과 모델 성능을 크게 향상시킵니다.

### 실험 설정 및 결과
- **실제 세계 실험**: 여러 휴머노이드 로봇 조작 작업에서 평가.
- **성능 비교**:
  - Ψ₀는 전체 성공률에서 10배 이상의 데이터로 훈련된 기준 모델을 40% 이상 능가합니다.
  - 약 800시간의 인간 비디오와 30시간의 로봇 데이터만으로 최적 성능에 도달합니다.

### 오픈 소스 생태계
- 완전한 생태계를 오픈 소스로 공개할 예정이며, 다음을 포함합니다:
  - 데이터 처리 및 훈련 파이프라인.
  - 휴머노이드 로봇 기반 모델.
  - 실시간 동작 추론 엔진.
