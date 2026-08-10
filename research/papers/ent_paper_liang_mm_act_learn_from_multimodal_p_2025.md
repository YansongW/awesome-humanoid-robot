---
$id: ent_paper_liang_mm_act_learn_from_multimodal_p_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MM-ACT: Learn from Multimodal Parallel Generation to Act'
  zh: MM-ACT
  ko: 'MM-ACT: Learn from Multimodal Parallel Generation to Act'
summary:
  en: 'MM-ACT: Learn from Multimodal Parallel Generation to Act (MM-ACT), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai AI Laboratory, Shanghai Jiao Tong University, The University of Hong Kong,
    University of Science and Technology of China, Fudan University, Zhejiang University.'
  zh: MM-ACT 是由上海人工智能实验室、上海交通大学、香港大学、中国科学技术大学、复旦大学和浙江大学联合提出的 2025 年大型视觉-语言-动作模型，专用于机器人操作。其核心贡献在于将文本、图像和动作统一到共享的 token 空间，并通过跨模态并行生成策略提升动作预测效率，在
    LIBERO 仿真任务上达到 96.3% 的成功率。
  ko: 'MM-ACT: Learn from Multimodal Parallel Generation to Act (MM-ACT), is a 2025 large vision-language-action model for
    robotic manipulation, introduced by Shanghai AI Laboratory, Shanghai Jiao Tong University, The University of Hong Kong,
    University of Science and Technology of China, Fudan University, Zhejiang University.'
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
- mm_act
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00975v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (916 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'MM-ACT: Learn from Multimodal Parallel Generation to Act (arXiv)'
  url: https://arxiv.org/abs/2512.00975
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MM-ACT source
  url: https://doi.org/10.48550/arXiv.2512.00975
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
MM-ACT 是一种统一的视觉-语言-动作（VLA）模型，旨在解决通用机器人策略中语义理解与环境交互能力之间的平衡问题。该模型将文本、图像和动作三种模态整合到共享的 token 空间，并分别采用重掩码并行解码策略（用于文本和图像生成）和一步并行解码策略（用于动作生成）以提高效率。通过引入上下文共享多模态学习这一统一训练范式，MM-ACT 从共享上下文中监督三种模态的生成，从而借助跨模态学习增强动作生成能力。实验在 LIBERO 仿真环境、Franka 真实机器人以及 RoboTwin2.0 双机械臂任务上展开，分别评估域内和域外性能，结果显示跨模态学习带来了 9.25% 的额外性能提升。

## 核心内容
### 方法架构
MM-ACT 的核心设计是将文本、图像和动作三种模态统一到共享的 token 空间，形成一个端到端的生成式模型。模型采用两种不同的并行解码策略：
- **重掩码并行解码**：用于文本和图像生成，通过逐步重掩码的方式并行预测多个 token，加速生成过程。
- **一步并行解码**：用于动作生成，直接一步输出完整的动作序列，显著提升推理效率。

### 训练范式
MM-ACT 提出了 **Context-Shared Multimodal Learning**，即从共享的上下文表示中同时监督三种模态的生成。这种统一训练方式使得模型能够利用文本和图像信息辅助动作预测，实现跨模态学习增强。

### 实验设置与结果
实验在三个不同场景下进行，分别测试域内和域外性能：
- **LIBERO 仿真环境**：域内任务，MM-ACT 达到 **96.3%** 的成功率。
- **Franka 真实机器人**：三个真实操作任务，平均成功率为 **72.0%**。
- **RoboTwin2.0**：八个双机械臂任务，域外泛化测试，成功率为 **52.38%**，其中跨模态学习贡献了 **9.25%** 的额外增益。

### 结论
MM-ACT 通过统一的 token 空间和并行解码策略，在保持高效推理的同时，借助跨模态学习显著提升了动作生成的准确性和泛化能力。代码、模型和数据已开源。

## Overview
A generalist robotic policy needs both semantic understanding for task planning and the ability to interact with the environment through predictive capabilities. To tackle this, we present MM-ACT, a unified Vision-Language-Action (VLA) model that integrates text, image, and action in shared token space and performs generation across all three modalities. MM-ACT adopts a re-mask parallel decoding strategy for text and image generation, and employs a one-step parallel decoding strategy for action generation to improve efficiency. We introduce Context-Shared Multimodal Learning, a unified training paradigm that supervises generation in all three modalities from a shared context, enhancing action generation through cross-modal learning. Experiments were conducted on the LIBERO simulation and Franka real-robot setups as well as RoboTwin2.0 to assess in-domain and out-of-domain performances respectively. Our approach achieves a success rate of 96.3% on LIBERO, 72.0% across three tasks of real Franka, and 52.38% across eight bimanual tasks of RoboTwin2.0 with an additional gain of 9.25% from cross-modal learning. We release our codes, models and data at https://github.com/HHYHRHY/MM-ACT.

## 参考
- http://arxiv.org/abs/2512.00975v2

## 개요
MM-ACT는 일반 로봇 정책에서 의미 이해와 환경 상호작용 능력 간의 균형 문제를 해결하기 위해 설계된 통합 비전-언어-행동(VLA) 모델입니다. 이 모델은 텍스트, 이미지, 행동의 세 가지 양식을 공유 토큰 공간에 통합하고, 텍스트 및 이미지 생성을 위한 재마스킹 병렬 디코딩 전략과 행동 생성을 위한 단일 단계 병렬 디코딩 전략을 각각 채택하여 효율성을 높입니다. 컨텍스트 공유 다중 모달 학습이라는 통합 훈련 패러다임을 도입함으로써, MM-ACT는 공유 컨텍스트에서 세 가지 양식의 생성을 감독하여 교차 모달 학습을 통해 행동 생성 능력을 강화합니다. 실험은 LIBERO 시뮬레이션 환경, Franka 실제 로봇, 그리고 RoboTwin2.0 이중 로봇 팔 작업에서 수행되었으며, 도메인 내 및 도메인 외 성능을 각각 평가한 결과 교차 모달 학습이 9.25%의 추가 성능 향상을 가져왔습니다.

## 핵심 내용
### 방법 아키텍처
MM-ACT의 핵심 설계는 텍스트, 이미지, 행동의 세 가지 양식을 공유 토큰 공간에 통합하여 종단 간 생성 모델을 형성하는 것입니다. 모델은 두 가지 서로 다른 병렬 디코딩 전략을 사용합니다:
- **재마스킹 병렬 디코딩**: 텍스트 및 이미지 생성에 사용되며, 점진적 재마스킹 방식으로 여러 토큰을 병렬 예측하여 생성 과정을 가속화합니다.
- **단일 단계 병렬 디코딩**: 행동 생성에 사용되며, 완전한 행동 시퀀스를 한 단계로 직접 출력하여 추론 효율성을 크게 향상시킵니다.

### 훈련 패러다임
MM-ACT는 **컨텍스트 공유 다중 모달 학습(Context-Shared Multimodal Learning)** 을 제안하며, 공유 컨텍스트 표현에서 세 가지 양식의 생성을 동시에 감독합니다. 이러한 통합 훈련 방식은 모델이 텍스트 및 이미지 정보를 활용하여 행동 예측을 보조하고, 교차 모달 학습 강화를 실현할 수 있게 합니다.

### 실험 설정 및 결과
실험은 세 가지 서로 다른 시나리오에서 수행되었으며, 도메인 내 및 도메인 외 성능을 각각 테스트했습니다:
- **LIBERO 시뮬레이션 환경**: 도메인 내 작업, MM-ACT는 **96.3%** 의 성공률을 달성했습니다.
- **Franka 실제 로봇**: 세 가지 실제 조작 작업, 평균 성공률은 **72.0%** 입니다.
- **RoboTwin2.0**: 여덟 가지 이중 로봇 팔 작업, 도메인 외 일반화 테스트, 성공률은 **52.38%** 이며, 교차 모달 학습이 **9.25%** 의 추가 이득을 기여했습니다.

### 결론
MM-ACT는 통합 토큰 공간과 병렬 디코딩 전략을 통해 효율적인 추론을 유지하면서도 교차 모달 학습을 통해 행동 생성의 정확성과 일반화 능력을 크게 향상시켰습니다. 코드, 모델 및 데이터는 오픈소스로 공개되었습니다.
