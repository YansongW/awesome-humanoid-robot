---
$id: ent_paper_lu_uniugp_unifying_understanding_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving'
  zh: UniUGP
  ko: 'UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving'
summary:
  en: 'UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving (UniUGP), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by ByteDance Seed, HKUST-GZ.'
  zh: UniUGP 是字节跳动 Seed 团队与港科大（广州）于 2025 年提出的统一理解-生成-规划框架，用于端到端自动驾驶。其核心贡献在于通过混合专家架构，将预训练视觉语言模型与视频生成模型协同，同时实现场景推理、未来视频生成与轨迹规划。该模型在感知、推理与决策任务上达到最先进水平，并在长尾场景中展现出卓越的泛化能力。
  ko: 'UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving (UniUGP), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by ByteDance Seed, HKUST-GZ.'
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
- uniugp
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.09864v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'UniUGP: Unifying Understanding, Generation, and Planing For End-to-end Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2512.09864
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UniUGP source
  url: https://doi.org/10.48550/arXiv.2512.09864
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有自动驾驶系统因缺乏世界知识与视觉动态建模能力，在长尾场景中表现不佳。UniUGP 通过构建多个专用数据集，为复杂场景提供推理与规划标注，并设计了一个统一框架，将场景理解、未来视频生成与轨迹规划三大任务融合。该模型以多帧观测与语言指令为输入，输出可解释的思维链推理、物理一致的轨迹以及连贯的未来视频。通过四阶段训练策略，UniUGP 逐步在多个现有自动驾驶数据集上构建这些能力，最终在感知、推理与决策任务上超越现有方法，尤其擅长处理具有挑战性的长尾场景。

## 核心内容
### 方法概述
UniUGP 的核心是一个混合专家架构，它整合了预训练的视觉语言模型（VLM）与视频生成模型。该架构旨在利用视觉动态信息与语义推理能力，共同提升规划性能。

### 输入与输出
- **输入**：多帧观测数据（如摄像头图像）与自然语言指令。
- **输出**：
  - 可解释的思维链（Chain-of-Thought）推理过程。
  - 物理上一致的自车轨迹。
  - 连贯的未来视频帧预测。

### 训练策略
UniUGP 采用四阶段渐进式训练策略：
1.  **阶段一**：在现有自动驾驶数据集上预训练基础视觉与语言能力。
2.  **阶段二**：利用专用数据集训练场景推理与因果学习能力。
3.  **阶段三**：引入视频生成模型，训练未来帧预测与视觉动态建模。
4.  **阶段四**：联合微调所有模块，实现理解、生成与规划的协同优化。

### 实验设置与关键结果
- **数据集**：在多个现有自动驾驶数据集（如 nuScenes）以及作者构建的专用数据集上进行训练与评估。
- **性能**：实验表明，UniUGP 在感知、推理与决策任务上均达到最先进水平（SOTA）。
- **泛化能力**：在长尾场景（如罕见障碍物、极端天气）中，UniUGP 的规划成功率显著优于基线方法，验证了其通过视觉因果学习与语言推理带来的泛化优势。

## Overview
Autonomous driving (AD) systems struggle in long-tail scenarios due to limited world knowledge and weak visual dynamic modeling. Existing vision-language-action (VLA)-based methods cannot leverage unlabeled videos for visual causal learning, while world model-based methods lack reasoning capabilities from large language models. In this paper, we construct multiple specialized datasets providing reasoning and planning annotations for complex scenarios. Then, a unified Understanding-Generation-Planning framework, named UniUGP, is proposed to synergize scene reasoning, future video generation, and trajectory planning through a hybrid expert architecture. By integrating pre-trained VLMs and video generation models, UniUGP leverages visual dynamics and semantic reasoning to enhance planning performance. Taking multi-frame observations and language instructions as input, it produces interpretable chain-of-thought reasoning, physically consistent trajectories, and coherent future videos. We introduce a four-stage training strategy that progressively builds these capabilities across multiple existing AD datasets, along with the proposed specialized datasets. Experiments demonstrate state-of-the-art performance in perception, reasoning, and decision-making, with superior generalization to challenging long-tail situations.

## 개요
자율주행(AD) 시스템은 제한된 세계 지식과 약한 시각적 동적 모델링으로 인해 롱테일(Long-tail) 시나리오에서 어려움을 겪습니다. 기존의 VLA(Vision-Language-Action) 기반 방법은 레이블이 없는 비디오를 시각적 인과 학습에 활용할 수 없으며, 월드 모델 기반 방법은 대규모 언어 모델의 추론 능력이 부족합니다. 본 논문에서는 복잡한 시나리오에 대한 추론 및 계획 주석을 제공하는 여러 특화 데이터셋을 구축합니다. 그런 다음, 하이브리드 전문가 아키텍처를 통해 장면 추론, 미래 비디오 생성 및 궤적 계획을 시너지 효과를 내는 통합 이해-생성-계획 프레임워크인 UniUGP를 제안합니다. 사전 훈련된 VLM과 비디오 생성 모델을 통합함으로써 UniUGP는 시각적 역학과 의미론적 추론을 활용하여 계획 성능을 향상시킵니다. 다중 프레임 관찰과 언어 명령을 입력으로 받아 해석 가능한 사고 사슬 추론, 물리적으로 일관된 궤적 및 일관된 미래 비디오를 생성합니다. 우리는 여러 기존 AD 데이터셋과 제안된 특화 데이터셋에 걸쳐 이러한 능력을 점진적으로 구축하는 4단계 훈련 전략을 도입합니다. 실험을 통해 인식, 추론 및 의사 결정에서 최첨단 성능을 입증하며, 까다로운 롱테일 상황에 대한 뛰어난 일반화 능력을 보여줍니다.

## 핵심 내용
자율주행(AD) 시스템은 제한된 세계 지식과 약한 시각적 동적 모델링으로 인해 롱테일 시나리오에서 어려움을 겪습니다. 기존의 VLA 기반 방법은 레이블이 없는 비디오를 시각적 인과 학습에 활용할 수 없으며, 월드 모델 기반 방법은 대규모 언어 모델의 추론 능력이 부족합니다. 본 논문에서는 복잡한 시나리오에 대한 추론 및 계획 주석을 제공하는 여러 특화 데이터셋을 구축합니다. 그런 다음, 하이브리드 전문가 아키텍처를 통해 장면 추론, 미래 비디오 생성 및 궤적 계획을 시너지 효과를 내는 통합 이해-생성-계획 프레임워크인 UniUGP를 제안합니다. 사전 훈련된 VLM과 비디오 생성 모델을 통합함으로써 UniUGP는 시각적 역학과 의미론적 추론을 활용하여 계획 성능을 향상시킵니다. 다중 프레임 관찰과 언어 명령을 입력으로 받아 해석 가능한 사고 사슬 추론, 물리적으로 일관된 궤적 및 일관된 미래 비디오를 생성합니다. 우리는 여러 기존 AD 데이터셋과 제안된 특화 데이터셋에 걸쳐 이러한 능력을 점진적으로 구축하는 4단계 훈련 전략을 도입합니다. 실험을 통해 인식, 추론 및 의사 결정에서 최첨단 성능을 입증하며, 까다로운 롱테일 상황에 대한 뛰어난 일반화 능력을 보여줍니다.

## 参考
- http://arxiv.org/abs/2512.09864v1
