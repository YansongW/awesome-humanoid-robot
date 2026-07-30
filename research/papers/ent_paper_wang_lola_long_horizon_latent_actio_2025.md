---
$id: ent_paper_wang_lola_long_horizon_latent_actio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LoLA: Long Horizon Latent Action Learning for General Robot Manipulation'
  zh: LoLA
  ko: 'LoLA: Long Horizon Latent Action Learning for General Robot Manipulation'
summary:
  en: 'LoLA: Long Horizon Latent Action Learning for General Robot Manipulation (LoLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Microelectronics, Chinese Academy of Sciences, University of
    Chinese Academy of Sciences, Microsoft Research.'
  zh: LoLA（Long Horizon Latent Action Learning）是由中国科学院微电子研究所、中国科学院大学和Microsoft Research联合提出的2025年大型视觉-语言-动作模型，专为机器人操作设计。其核心贡献在于通过状态感知潜在重表示模块，将长期多视角观测与语言指令转化为可操作的机器人运动空间，显著提升了长时域语言引导操作任务的性能。
  ko: 'LoLA: Long Horizon Latent Action Learning for General Robot Manipulation (LoLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Microelectronics, Chinese Academy of Sciences, University of
    Chinese Academy of Sciences, Microsoft Research.'
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
- lola
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.20166v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'LoLA: Long Horizon Latent Action Learning for General Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2512.20166
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LoLA source
  url: https://doi.org/10.48550/arXiv.2512.20166
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
LoLA针对现有视觉-语言-动作模型在处理长时域、语言引导的机器人操作任务时，对历史信息利用和连贯动作序列生成能力不足的问题，提出了一种集成长期多视角观测与机器人本体感知的框架。该框架首先利用视觉-语言模型从历史序列和多视角观测中编码丰富的上下文特征，然后通过核心模块“状态感知潜在重表示”，将视觉输入和语言命令转化为可操作的机器人运动空间。与现有方法简单拼接机器人本体感知（如关节角度）与视觉-语言嵌入不同，该模块利用机器人状态，通过可学习的“具身锚定”潜在空间，将视觉-语言表示显式地锚定在物理尺度上。LoLA在多个机器人预训练数据集上训练，并在SIMPLER和LIBERO仿真基准以及Franka和Bi-Manual Aloha机器人的两个真实世界任务中进行了广泛评估，结果显示其在长时域操作任务上显著优于pi0等先前最先进方法。

## 核心内容
### 方法概述
LoLA框架的核心在于解决长时域、语言引导的机器人操作任务中，对历史信息利用和连贯动作序列生成的需求。现有VLA模型往往忽视这些能力，而LoLA通过以下关键设计实现突破：

- **视觉-语言模型编码**：首先利用VLM从历史序列和多视角观测中编码丰富的上下文特征，为后续动作生成提供基础。
- **状态感知潜在重表示模块**：这是LoLA的核心创新。与现有VLA方法简单地将机器人本体感知（如关节角度）与VL嵌入拼接不同，该模块利用机器人状态，通过一个可学习的“具身锚定”潜在空间，将VL表示显式地锚定在物理尺度上。这使得视觉输入和语言命令能够被转化为可操作的机器人运动空间，从而实现多步推理和动作生成。

### 实验设置与结果
LoLA在多个机器人预训练数据集上进行了训练，并在以下基准和任务上进行了评估：

- **仿真基准**：在SIMPLER和LIBERO基准上进行了评估。
- **真实世界任务**：在Franka和Bi-Manual Aloha机器人上执行了两个真实世界操作任务。

实验结果表明，LoLA在长时域操作任务上显著优于先前最先进的方法（如pi0），特别是在需要长期历史信息和连贯动作序列的任务中表现突出。

## Overview
The capability of performing long-horizon, language-guided robotic manipulation tasks critically relies on leveraging historical information and generating coherent action sequences. However, such capabilities are often overlooked by existing Vision-Language-Action (VLA) models. To solve this challenge, we propose LoLA (Long Horizon Latent Action Learning), a framework designed for robot manipulation that integrates long-term multi-view observations and robot proprioception to enable multi-step reasoning and action generation. We first employ Vision-Language Models to encode rich contextual features from historical sequences and multi-view observations. We further introduces a key module, State-Aware Latent Re-representation, which transforms visual inputs and language commands into actionable robot motion space. Unlike existing VLA approaches that merely concatenate robot proprioception (e.g., joint angles) with VL embeddings, this module leverages such robot states to explicitly ground VL representations in physical scale through a learnable "embodiment-anchored" latent space. We trained LoLA on diverse robotic pre-training datasets and conducted extensive evaluations on simulation benchmarks (SIMPLER and LIBERO), as well as two real-world tasks on Franka and Bi-Manual Aloha robots. Results show that LoLA significantly outperforms prior state-of-the-art methods (e.g., pi0), particularly in long-horizon manipulation tasks.

## Overview
The capability of performing long-horizon, language-guided robotic manipulation tasks critically relies on leveraging historical information and generating coherent action sequences. However, such capabilities are often overlooked by existing Vision-Language-Action (VLA) models. To solve this challenge, we propose LoLA (Long Horizon Latent Action Learning), a framework designed for robot manipulation that integrates long-term multi-view observations and robot proprioception to enable multi-step reasoning and action generation. We first employ Vision-Language Models to encode rich contextual features from historical sequences and multi-view observations. We further introduce a key module, State-Aware Latent Re-representation, which transforms visual inputs and language commands into actionable robot motion space. Unlike existing VLA approaches that merely concatenate robot proprioception (e.g., joint angles) with VL embeddings, this module leverages such robot states to explicitly ground VL representations in physical scale through a learnable "embodiment-anchored" latent space. We trained LoLA on diverse robotic pre-training datasets and conducted extensive evaluations on simulation benchmarks (SIMPLER and LIBERO), as well as two real-world tasks on Franka and Bi-Manual Aloha robots. Results show that LoLA significantly outperforms prior state-of-the-art methods (e.g., pi0), particularly in long-horizon manipulation tasks.

## Content
The capability of performing long-horizon, language-guided robotic manipulation tasks critically relies on leveraging historical information and generating coherent action sequences. However, such capabilities are often overlooked by existing Vision-Language-Action (VLA) models. To solve this challenge, we propose LoLA (Long Horizon Latent Action Learning), a framework designed for robot manipulation that integrates long-term multi-view observations and robot proprioception to enable multi-step reasoning and action generation. We first employ Vision-Language Models to encode rich contextual features from historical sequences and multi-view observations. We further introduce a key module, State-Aware Latent Re-representation, which transforms visual inputs and language commands into actionable robot motion space. Unlike existing VLA approaches that merely concatenate robot proprioception (e.g., joint angles) with VL embeddings, this module leverages such robot states to explicitly ground VL representations in physical scale through a learnable "embodiment-anchored" latent space. We trained LoLA on diverse robotic pre-training datasets and conducted extensive evaluations on simulation benchmarks (SIMPLER and LIBERO), as well as two real-world tasks on Franka and Bi-Manual Aloha robots. Results show that LoLA significantly outperforms prior state-of-the-art methods (e.g., pi0), particularly in long-horizon manipulation tasks.

## 개요
장기적인 언어 기반 로봇 조작 작업을 수행하는 능력은 과거 정보를 활용하고 일관된 행동 시퀀스를 생성하는 데 결정적으로 의존합니다. 그러나 이러한 능력은 기존의 Vision-Language-Action (VLA) 모델에서 종종 간과됩니다. 이 문제를 해결하기 위해, 우리는 장기 다중 시점 관찰과 로봇 고유 감각을 통합하여 다단계 추론 및 행동 생성을 가능하게 하는 로봇 조작용 프레임워크인 LoLA (Long Horizon Latent Action Learning)를 제안합니다. 먼저 Vision-Language Models을 사용하여 과거 시퀀스와 다중 시점 관찰로부터 풍부한 맥락적 특징을 인코딩합니다. 또한, 시각적 입력과 언어 명령을 실행 가능한 로봇 동작 공간으로 변환하는 핵심 모듈인 State-Aware Latent Re-representation을 도입합니다. 단순히 로봇 고유 감각(예: 관절 각도)을 VL 임베딩과 연결하는 기존 VLA 접근 방식과 달리, 이 모듈은 학습 가능한 "신체 고정" 잠재 공간을 통해 이러한 로봇 상태를 활용하여 VL 표현을 물리적 규모에 명시적으로 고정시킵니다. 우리는 다양한 로봇 사전 학습 데이터셋에서 LoLA를 훈련하고, 시뮬레이션 벤치마크(SIMPLER 및 LIBERO)와 Franka 및 Bi-Manual Aloha 로봇의 두 가지 실제 작업에서 광범위한 평가를 수행했습니다. 결과는 LoLA가 특히 장기 조작 작업에서 이전 최첨단 방법(예: pi0)을 크게 능가함을 보여줍니다.

## 핵심 내용
장기적인 언어 기반 로봇 조작 작업을 수행하는 능력은 과거 정보를 활용하고 일관된 행동 시퀀스를 생성하는 데 결정적으로 의존합니다. 그러나 이러한 능력은 기존의 Vision-Language-Action (VLA) 모델에서 종종 간과됩니다. 이 문제를 해결하기 위해, 우리는 장기 다중 시점 관찰과 로봇 고유 감각을 통합하여 다단계 추론 및 행동 생성을 가능하게 하는 로봇 조작용 프레임워크인 LoLA (Long Horizon Latent Action Learning)를 제안합니다. 먼저 Vision-Language Models을 사용하여 과거 시퀀스와 다중 시점 관찰로부터 풍부한 맥락적 특징을 인코딩합니다. 또한, 시각적 입력과 언어 명령을 실행 가능한 로봇 동작 공간으로 변환하는 핵심 모듈인 State-Aware Latent Re-representation을 도입합니다. 단순히 로봇 고유 감각(예: 관절 각도)을 VL 임베딩과 연결하는 기존 VLA 접근 방식과 달리, 이 모듈은 학습 가능한 "신체 고정" 잠재 공간을 통해 이러한 로봇 상태를 활용하여 VL 표현을 물리적 규모에 명시적으로 고정시킵니다. 우리는 다양한 로봇 사전 학습 데이터셋에서 LoLA를 훈련하고, 시뮬레이션 벤치마크(SIMPLER 및 LIBERO)와 Franka 및 Bi-Manual Aloha 로봇의 두 가지 실제 작업에서 광범위한 평가를 수행했습니다. 결과는 LoLA가 특히 장기 조작 작업에서 이전 최첨단 방법(예: pi0)을 크게 능가함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2512.20166v1
