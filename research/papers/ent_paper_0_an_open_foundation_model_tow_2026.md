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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.12263v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
우리는 $Ψ_0$ (Psi-Zero)를 소개합니다. 이는 까다로운 휴머노이드 로코-조작(loco-manipulation) 작업을 해결하기 위한 오픈 파운데이션 모델입니다. 기존 접근법은 종종 대규모의 다양한 인간 및 휴머노이드 데이터를 공동 학습(co-training)하여 이 근본적인 문제를 해결하려고 시도하지만, 우리는 인간과 휴머노이드 로봇 간의 근본적인 운동학적 및 동작 차이로 인해 이 전략이 최적이 아니라고 주장합니다. 따라서 상당한 데이터 양에도 불구하고 데이터 효율성과 모델 성능은 여전히 만족스럽지 않습니다. 이 문제를 해결하기 위해, \ours\는 학습 과정을 분리하여 이질적인 데이터 소스의 유용성을 극대화합니다. 구체적으로, 우리는 서로 다른 학습 목표를 가진 단계적 학습 패러다임을 제안합니다: 첫째, 대규모 자기중심적 인간 비디오에서 VLM 백본을 자기회귀적으로 사전 학습하여 일반화 가능한 시각-행동 표현을 획득합니다. 그런 다음, 고품질 휴머노이드 로봇 데이터에서 흐름 기반 행동 전문가(flow-based action expert)를 사후 학습하여 정밀한 로봇 관절 제어를 학습합니다. 우리의 연구는 또한 중요하지만 종종 간과되는 데이터 레시피를 식별합니다: 잡음이 많은 인터넷 클립이나 이질적인 교차 체현 로봇 데이터셋으로 확장하는 접근법과 달리, 고품질 자기중심적 인간 조작 데이터로 사전 학습한 후 도메인 특화 실제 휴머노이드 궤적으로 사후 학습하는 것이 우수한 성능을 제공한다는 것을 입증합니다. 광범위한 실제 실험을 통해 \ours\는 약 800시간의 인간 비디오 데이터와 30시간의 실제 로봇 데이터만 사용하여 최고의 성능을 달성하며, 10배 이상 많은 데이터로 사전 학습된 기준선보다 여러 작업에서 전체 성공률이 40% 이상 향상됨을 보여줍니다. 우리는 데이터 처리 및 학습 파이프라인, 휴머노이드 파운데이션 모델, 실시간 행동 추론 엔진을 포함한 전체 생태계를 커뮤니티에 오픈소스로 공개할 예정입니다.

## 핵심 내용
우리는 $Ψ_0$ (Psi-Zero)를 소개합니다. 이는 까다로운 휴머노이드 로코-조작(loco-manipulation) 작업을 해결하기 위한 오픈 파운데이션 모델입니다. 기존 접근법은 종종 대규모의 다양한 인간 및 휴머노이드 데이터를 공동 학습(co-training)하여 이 근본적인 문제를 해결하려고 시도하지만, 우리는 인간과 휴머노이드 로봇 간의 근본적인 운동학적 및 동작 차이로 인해 이 전략이 최적이 아니라고 주장합니다. 따라서 상당한 데이터 양에도 불구하고 데이터 효율성과 모델 성능은 여전히 만족스럽지 않습니다. 이 문제를 해결하기 위해, \ours\는 학습 과정을 분리하여 이질적인 데이터 소스의 유용성을 극대화합니다. 구체적으로, 우리는 서로 다른 학습 목표를 가진 단계적 학습 패러다임을 제안합니다: 첫째, 대규모 자기중심적 인간 비디오에서 VLM 백본을 자기회귀적으로 사전 학습하여 일반화 가능한 시각-행동 표현을 획득합니다. 그런 다음, 고품질 휴머노이드 로봇 데이터에서 흐름 기반 행동 전문가(flow-based action expert)를 사후 학습하여 정밀한 로봇 관절 제어를 학습합니다. 우리의 연구는 또한 중요하지만 종종 간과되는 데이터 레시피를 식별합니다: 잡음이 많은 인터넷 클립이나 이질적인 교차 체현 로봇 데이터셋으로 확장하는 접근법과 달리, 고품질 자기중심적 인간 조작 데이터로 사전 학습한 후 도메인 특화 실제 휴머노이드 궤적으로 사후 학습하는 것이 우수한 성능을 제공한다는 것을 입증합니다. 광범위한 실제 실험을 통해 \ours\는 약 800시간의 인간 비디오 데이터와 30시간의 실제 로봇 데이터만 사용하여 최고의 성능을 달성하며, 10배 이상 많은 데이터로 사전 학습된 기준선보다 여러 작업에서 전체 성공률이 40% 이상 향상됨을 보여줍니다. 우리는 데이터 처리 및 학습 파이프라인, 휴머노이드 파운데이션 모델, 실시간 행동 추론 엔진을 포함한 전체 생태계를 커뮤니티에 오픈소스로 공개할 예정입니다.

## 参考
- http://arxiv.org/abs/2603.12263v1
