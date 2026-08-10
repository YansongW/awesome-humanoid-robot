---
$id: ent_paper_unitacvla_unified_tactile_unde_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models'
  zh: 'UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models'
  ko: 'UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models'
summary:
  en: 'arXiv:2606.31723v1 Announce Type: new Abstract: Vision-language-action (VLA) models have achieved strong performance
    in many robotic manipulation tasks, yet remain limited in contact-rich dexterous manipulation. To overcome this limitation,
    recent vision-tactile-language-action (VTLA) methods incorporate tactile sensing into VLA models to provide direct contact
    information. However, they typically treat tactile signals as passive auxiliary inputs, making it difficult to model tactile
    semantics and future physical interactions. To this end, we propose a unified tactile learning framework for contact-rich
    manipulation that models tactile signals as dynamic interaction cues for both contact understanding and prediction. Specifically,
    we construct a unified tactile latent space and jointly model current tactile states and future contact changes through
    tactile chain-of-thought reasoning and coarse-to-fine future tactile prediction, thereby forming a state-aware and dynamics-aware
    tactile prior. Based on this prior, we introduce a tactile-action mixed controller that combines real-time and predicted
    tactile feedback to refine low-frequency action chunks with high-frequency corrections. Real-world experiments on four
    categories of contact-rich tasks, including adjustment, insertion, wiping, and assembly, under both clean and externally
    perturbed settings, show that our method improves success rate, manipulation accuracy, and contact robustness over existing
    methods, demonstrating its effectiveness in dexterous physical interaction.'
  zh: UniTacVLA 是一个统一触觉学习框架，由研究团队提出，用于增强视觉-语言-动作（VLA）模型在接触丰富灵巧操作中的表现。其核心贡献在于将触觉信号建模为动态交互线索，通过触觉链式推理和由粗到细的未来触觉预测，形成状态与动力学感知的触觉先验，并引入触觉-动作混合控制器，显著提升了任务成功率、操作精度和接触鲁棒性。
  ko: 'arXiv:2606.31723v1 Announce Type: new Abstract: Vision-language-action (VLA) models have achieved strong performance
    in many robotic manipulation tasks, yet remain limited in contact-rich dexterous manipulation. To overcome this limitation,
    recent vision-tactile-language-action (VTLA) methods incorporate tactile sensing into VLA models to provide direct contact
    information. However, they typically treat tactile signals as passive auxiliary inputs, making it difficult to model tactile
    semantics and future physical interactions. To this end, we propose a unified tactile learning framework for contact-rich
    manipulation that models tactile signals as dynamic interaction cues for both contact understanding and prediction. Specifically,
    we construct a unified tactile latent space and jointly model current tactile states and future contact changes through
    tactile chain-of-thought reasoning and coarse-to-fine future tactile prediction, thereby forming a state-aware and dynamics-aware
    tactile prior. Based on this prior, we introduce a tactile-action mixed controller that combines real-time and predicted
    tactile feedback to refine low-frequency action chunks with high-frequency corrections. Real-world experiments on four
    categories of contact-rich tasks, including adjustment, insertion, wiping, and assembly, under both clean and externally
    perturbed settings, show that our method improves success rate, manipulation accuracy, and contact robustness over existing
    methods, demonstrating its effectiveness in dexterous physical interaction.'
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
- robotics
- unitacvla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31723v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1008 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'UniTacVLA: Unified Tactile Understanding and Prediction in Vision Language Action Models'
  url: https://arxiv.org/abs/2606.31723
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 模型在接触丰富的灵巧操作中表现有限，而近期 VTLA 方法虽引入触觉传感，却常将触觉信号视为被动辅助输入，难以建模触觉语义和未来物理交互。UniTacVLA 提出统一触觉学习框架，通过构建统一触觉潜在空间，联合建模当前触觉状态与未来接触变化，形成状态与动力学感知的触觉先验。基于此先验，框架引入触觉-动作混合控制器，结合实时与预测触觉反馈，以高频修正优化低频动作块。在调整、插入、擦拭和组装四类接触丰富任务上的真实世界实验表明，该方法在干净和外部扰动环境下均优于现有方法。

## 核心内容
### 方法概述
UniTacVLA 的核心在于将触觉信号从被动辅助输入转变为动态交互线索，用于接触理解与预测。框架包含三个关键组件：
- **统一触觉潜在空间**：构建一个共享的潜在表示空间，用于编码当前触觉状态和未来接触变化。
- **触觉链式推理与由粗到细的未来触觉预测**：通过链式推理逐步推理触觉语义，并采用由粗到细的预测策略，生成未来接触变化的动态先验，从而形成状态感知与动力学感知的触觉先验。
- **触觉-动作混合控制器**：基于上述先验，该控制器融合实时触觉反馈与预测触觉反馈，对低频动作块进行高频修正，提升操作精度与鲁棒性。

### 实验设置
- **任务类别**：调整（adjustment）、插入（insertion）、擦拭（wiping）、组装（assembly），共四类接触丰富任务。
- **环境条件**：在干净环境与外部扰动（如外力干扰）两种设置下进行测试。
- **评估指标**：成功率（success rate）、操作精度（manipulation accuracy）、接触鲁棒性（contact robustness）。

### 关键结果
- 在所有四类任务中，UniTacVLA 的成功率均显著高于现有 VLA 和 VTLA 基线方法。
- 在外部扰动条件下，该方法展现出更强的接触鲁棒性，能有效应对突发干扰。
- 操作精度方面，UniTacVLA 在调整和组装等需要精细接触控制的任务中表现尤为突出。

### 结论
UniTacVLA 通过将触觉信号建模为动态交互线索，并引入预测性触觉反馈与混合控制策略，有效克服了现有 VLA 模型在接触丰富灵巧操作中的局限性。实验证明，该方法在多种任务和扰动条件下均能提升性能，为灵巧物理交互提供了新的解决方案。

## Overview
Vision-language-action (VLA) models have achieved strong performance in many robotic manipulation tasks, yet remain limited in contact-rich dexterous manipulation. To overcome this limitation, recent vision-tactile-language-action (VTLA) methods incorporate tactile sensing into VLA models to provide direct contact information. However, they typically treat tactile signals as passive auxiliary inputs, making it difficult to model tactile semantics and future physical interactions. To this end, we propose a unified tactile learning framework for contact-rich manipulation that models tactile signals as dynamic interaction cues for both contact understanding and prediction. Specifically, we construct a unified tactile latent space and jointly model current tactile states and future contact changes through tactile chain-of-thought reasoning and coarse-to-fine future tactile prediction, thereby forming a state-aware and dynamics-aware tactile prior. Based on this prior, we introduce a tactile-action mixed controller that combines real-time and predicted tactile feedback to refine low-frequency action chunks with high-frequency corrections. Real-world experiments on four categories of contact-rich tasks, including adjustment, insertion, wiping, and assembly, under both clean and externally perturbed settings, show that our method improves success rate, manipulation accuracy, and contact robustness over existing methods, demonstrating its effectiveness in dexterous physical interaction.

## 参考
- http://arxiv.org/abs/2606.31723v1

## 개요
기존 VLA 모델은 접촉이 풍부한 정교한 조작에서 성능이 제한적이며, 최근 VTLA 방법은 촉각 센싱을 도입하지만 종종 촉각 신호를 수동적 보조 입력으로 간주하여 촉각 의미론과 미래 물리적 상호작용을 모델링하기 어렵습니다. UniTacVLA는 통합 촉각 학습 프레임워크를 제안하며, 통합 촉각 잠재 공간을 구축하여 현재 촉각 상태와 미래 접촉 변화를 공동으로 모델링하여 상태 및 역학 인식 촉각 사전 지식을 형성합니다. 이 사전 지식을 기반으로 프레임워크는 촉각-행동 혼합 컨트롤러를 도입하여 실시간 및 예측 촉각 피드백을 결합하고, 고주파수 수정을 통해 저주파수 행동 블록을 최적화합니다. 조정, 삽입, 닦기, 조립의 네 가지 접촉이 풍부한 작업에서의 실제 세계 실험은 이 방법이 깨끗한 환경과 외부 교란 환경 모두에서 기존 방법보다 우수함을 보여줍니다.

## 핵심 내용
### 방법 개요
UniTacVLA의 핵심은 촉각 신호를 수동적 보조 입력에서 동적 상호작용 단서로 전환하여 접촉 이해와 예측에 사용하는 것입니다. 프레임워크는 세 가지 핵심 구성 요소를 포함합니다:
- **통합 촉각 잠재 공간**: 현재 촉각 상태와 미래 접촉 변화를 인코딩하기 위한 공유 잠재 표현 공간을 구축합니다.
- **촉각 체인 추론 및 거친 것에서 세밀한 것으로의 미래 촉각 예측**: 체인 추론을 통해 촉각 의미론을 단계적으로 추론하고, 거친 것에서 세밀한 것으로의 예측 전략을 채택하여 미래 접촉 변화의 동적 사전 지식을 생성함으로써 상태 인식 및 역학 인식 촉각 사전 지식을 형성합니다.
- **촉각-행동 혼합 컨트롤러**: 위 사전 지식을 기반으로 이 컨트롤러는 실시간 촉각 피드백과 예측 촉각 피드백을 융합하여 저주파수 행동 블록을 고주파수로 수정하여 조작 정밀도와 견고성을 향상시킵니다.

### 실험 설정
- **작업 범주**: 조정(adjustment), 삽입(insertion), 닦기(wiping), 조립(assembly)의 네 가지 접촉이 풍부한 작업.
- **환경 조건**: 깨끗한 환경과 외부 교란(예: 외력 간섭)의 두 가지 설정에서 테스트.
- **평가 지표**: 성공률(success rate), 조작 정밀도(manipulation accuracy), 접촉 견고성(contact robustness).

### 주요 결과
- 네 가지 작업 모두에서 UniTacVLA의 성공률은 기존 VLA 및 VTLA 기준 방법보다 현저히 높습니다.
- 외부 교란 조건에서 이 방법은 더 강한 접촉 견고성을 보여주며 갑작스러운 간섭에 효과적으로 대응합니다.
- 조작 정밀도 측면에서 UniTacVLA는 조정 및 조립과 같은 정밀한 접촉 제어가 필요한 작업에서 특히 뛰어난 성능을 보여줍니다.

### 결론
UniTacVLA는 촉각 신호를 동적 상호작용 단서로 모델링하고 예측적 촉각 피드백과 혼합 제어 전략을 도입함으로써 기존 VLA 모델의 접촉이 풍부한 정교한 조작에서의 한계를 효과적으로 극복합니다. 실험은 이 방법이 다양한 작업 및 교란 조건에서 성능을 향상시킬 수 있음을 증명하며, 정교한 물리적 상호작용을 위한 새로운 솔루션을 제공합니다.
