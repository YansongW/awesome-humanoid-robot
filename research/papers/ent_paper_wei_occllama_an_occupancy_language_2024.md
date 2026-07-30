---
$id: ent_paper_wei_occllama_an_occupancy_language_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving'
  zh: OccLLaMA
  ko: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving'
summary:
  en: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving (OccLLaMA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Academy for Engineering & Technology, Fudan University, Institute for AI
    Industry Research, Tsinghua University.'
  zh: OccLLaMA 是复旦大学工程与应用技术研究院与清华大学智能产业研究院于 2024 年联合提出的大型视觉-语言-动作生成世界模型。其核心贡献在于将语义占用作为通用视觉表征，通过自回归模型统一视觉、语言与动作模态，并在 4D 占用预测、运动规划与视觉问答等多项自动驾驶任务中取得竞争性表现。
  ko: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving (OccLLaMA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Academy for Engineering & Technology, Fudan University, Institute for AI
    Industry Research, Tsinghua University.'
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
- occllama
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.03272v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2409.03272
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OccLLaMA source
  url: https://doi.org/10.48550/arXiv.2409.03272
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
现有基于多模态大语言模型的自动驾驶方法通常直接从感知映射到动作，忽略了世界动态以及动作与世界状态之间的关联。受人类世界模型启发，OccLLaMA 提出以语义占用作为通用视觉表征，构建了一个视觉-语言-动作统一的生成式世界模型。该模型通过引入类似 VQVAE 的场景分词器高效离散化并重建语义占用场景，同时构建了包含视觉、语言与动作的统一多模态词表。在此基础上，OccLLaMA 增强 LLaMA 模型，使其能够在统一词表上进行下一 token/场景预测，从而完成多项自动驾驶任务。

## 核心内容
### 方法架构
OccLLaMA 的核心创新在于将语义占用作为连接视觉、语言与动作的通用表征，并采用自回归生成范式统一处理多模态信息。具体包括以下关键组件：

- **场景分词器（Scene Tokenizer）**：设计了一种类似 VQVAE 的结构，专门针对语义占用场景的稀疏性与类别不平衡问题，实现高效的离散化编码与重建。
- **统一多模态词表**：将视觉占用 token、语言 token 与动作 token 整合到同一个词表中，使模型能够以统一的序列形式处理多模态输入与输出。
- **增强的 LLaMA 骨干**：在 LLaMA 基础上进行改进，使其能够基于统一词表执行下一 token 预测（用于语言与动作）以及下一场景预测（用于 4D 占用），从而同时支持多种任务。

### 实验设置与关键结果
- **任务覆盖**：在 4D 占用预测、运动规划与视觉问答三个典型自动驾驶任务上进行评估。
- **性能表现**：OccLLaMA 在所有任务上均取得具有竞争力的结果，验证了其作为自动驾驶基础模型的潜力。具体数值需参考原文实验表格。
- **对比基线**：与现有基于 MLLM 的方法相比，OccLLaMA 通过显式建模世界动态（占用预测）提升了动作规划与场景理解的连贯性。

### 结论
OccLLaMA 首次将语义占用引入生成式世界模型框架，通过统一视觉-语言-动作模态的自回归建模，为自动驾驶提供了一种新的基础模型范式。其成功表明，显式建模世界动态有助于提升多任务联合学习的效果，未来可进一步扩展至更复杂的驾驶场景与交互任务。

## Overview
The rise of multi-modal large language models(MLLMs) has spurred their applications in autonomous driving. Recent MLLM-based methods perform action by learning a direct mapping from perception to action, neglecting the dynamics of the world and the relations between action and world dynamics. In contrast, human beings possess world model that enables them to simulate the future states based on 3D internal visual representation and plan actions accordingly. To this end, we propose OccLLaMA, an occupancy-language-action generative world model, which uses semantic occupancy as a general visual representation and unifies vision-language-action(VLA) modalities through an autoregressive model. Specifically, we introduce a novel VQVAE-like scene tokenizer to efficiently discretize and reconstruct semantic occupancy scenes, considering its sparsity and classes imbalance. Then, we build a unified multi-modal vocabulary for vision, language and action. Furthermore, we enhance LLM, specifically LLaMA, to perform the next token/scene prediction on the unified vocabulary to complete multiple tasks in autonomous driving. Extensive experiments demonstrate that OccLLaMA achieves competitive performance across multiple tasks, including 4D occupancy forecasting, motion planning, and visual question answering, showcasing its potential as a foundation model in autonomous driving.

## Overview
The rise of multi-modal large language models (MLLMs) has spurred their applications in autonomous driving. Recent MLLM-based methods perform action by learning a direct mapping from perception to action, neglecting the dynamics of the world and the relations between action and world dynamics. In contrast, human beings possess world model that enables them to simulate the future states based on 3D internal visual representation and plan actions accordingly. To this end, we propose OccLLaMA, an occupancy-language-action generative world model, which uses semantic occupancy as a general visual representation and unifies vision-language-action (VLA) modalities through an autoregressive model. Specifically, we introduce a novel VQVAE-like scene tokenizer to efficiently discretize and reconstruct semantic occupancy scenes, considering its sparsity and classes imbalance. Then, we build a unified multi-modal vocabulary for vision, language and action. Furthermore, we enhance LLM, specifically LLaMA, to perform the next token/scene prediction on the unified vocabulary to complete multiple tasks in autonomous driving. Extensive experiments demonstrate that OccLLaMA achieves competitive performance across multiple tasks, including 4D occupancy forecasting, motion planning, and visual question answering, showcasing its potential as a foundation model in autonomous driving.

## Content
The rise of multi-modal large language models (MLLMs) has spurred their applications in autonomous driving. Recent MLLM-based methods perform action by learning a direct mapping from perception to action, neglecting the dynamics of the world and the relations between action and world dynamics. In contrast, human beings possess world model that enables them to simulate the future states based on 3D internal visual representation and plan actions accordingly. To this end, we propose OccLLaMA, an occupancy-language-action generative world model, which uses semantic occupancy as a general visual representation and unifies vision-language-action (VLA) modalities through an autoregressive model. Specifically, we introduce a novel VQVAE-like scene tokenizer to efficiently discretize and reconstruct semantic occupancy scenes, considering its sparsity and classes imbalance. Then, we build a unified multi-modal vocabulary for vision, language and action. Furthermore, we enhance LLM, specifically LLaMA, to perform the next token/scene prediction on the unified vocabulary to complete multiple tasks in autonomous driving. Extensive experiments demonstrate that OccLLaMA achieves competitive performance across multiple tasks, including 4D occupancy forecasting, motion planning, and visual question answering, showcasing its potential as a foundation model in autonomous driving.

## 개요
멀티모달 대규모 언어 모델(MLLM)의 부상은 자율주행 분야에서의 응용을 촉진했습니다. 최근 MLLM 기반 방법은 인식에서 행동으로의 직접적인 매핑을 학습하여 행동을 수행하지만, 세계의 역학과 행동과 세계 역학 간의 관계를 무시합니다. 반면, 인간은 3D 내부 시각적 표현을 기반으로 미래 상태를 시뮬레이션하고 그에 따라 행동을 계획할 수 있는 세계 모델을 보유하고 있습니다. 이를 위해 우리는 OccLLaMA를 제안합니다. 이는 점유-언어-행동 생성 세계 모델로, 의미적 점유를 일반적인 시각적 표현으로 사용하고 자기회귀 모델을 통해 시각-언어-행동(VLA) 모달리티를 통합합니다. 구체적으로, 우리는 희소성과 클래스 불균형을 고려하여 의미적 점유 장면을 효율적으로 이산화하고 재구성하는 새로운 VQVAE 유사 장면 토크나이저를 도입합니다. 그런 다음, 시각, 언어 및 행동을 위한 통합 멀티모달 어휘를 구축합니다. 또한, LLM, 특히 LLaMA를 개선하여 통합 어휘에 대한 다음 토큰/장면 예측을 수행함으로써 자율주행에서 여러 작업을 완료합니다. 광범위한 실험을 통해 OccLLaMA가 4D 점유 예측, 모션 계획 및 시각 질문 응답을 포함한 여러 작업에서 경쟁력 있는 성능을 달성하여 자율주행의 기초 모델로서의 잠재력을 입증합니다.

## 핵심 내용
멀티모달 대규모 언어 모델(MLLM)의 부상은 자율주행 분야에서의 응용을 촉진했습니다. 최근 MLLM 기반 방법은 인식에서 행동으로의 직접적인 매핑을 학습하여 행동을 수행하지만, 세계의 역학과 행동과 세계 역학 간의 관계를 무시합니다. 반면, 인간은 3D 내부 시각적 표현을 기반으로 미래 상태를 시뮬레이션하고 그에 따라 행동을 계획할 수 있는 세계 모델을 보유하고 있습니다. 이를 위해 우리는 OccLLaMA를 제안합니다. 이는 점유-언어-행동 생성 세계 모델로, 의미적 점유를 일반적인 시각적 표현으로 사용하고 자기회귀 모델을 통해 시각-언어-행동(VLA) 모달리티를 통합합니다. 구체적으로, 우리는 희소성과 클래스 불균형을 고려하여 의미적 점유 장면을 효율적으로 이산화하고 재구성하는 새로운 VQVAE 유사 장면 토크나이저를 도입합니다. 그런 다음, 시각, 언어 및 행동을 위한 통합 멀티모달 어휘를 구축합니다. 또한, LLM, 특히 LLaMA를 개선하여 통합 어휘에 대한 다음 토큰/장면 예측을 수행함으로써 자율주행에서 여러 작업을 완료합니다. 광범위한 실험을 통해 OccLLaMA가 4D 점유 예측, 모션 계획 및 시각 질문 응답을 포함한 여러 작업에서 경쟁력 있는 성능을 달성하여 자율주행의 기초 모델로서의 잠재력을 입증합니다.

## 参考
- http://arxiv.org/abs/2409.03272v1
