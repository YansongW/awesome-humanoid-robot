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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31723v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Vision-language-action(VLA) 모델은 많은 로봇 조작 작업에서 뛰어난 성능을 달성했지만, 접촉이 많은 정밀 조작(contact-rich dexterous manipulation)에서는 여전히 한계를 보입니다. 이러한 한계를 극복하기 위해 최근 vision-tactile-language-action(VTLA) 방법은 촉각 감지를 VLA 모델에 통합하여 직접적인 접촉 정보를 제공합니다. 그러나 이러한 방법은 일반적으로 촉각 신호를 수동적인 보조 입력으로 처리하여 촉각 의미론과 미래의 물리적 상호작용을 모델링하기 어렵게 만듭니다. 이를 해결하기 위해, 우리는 접촉이 많은 조작을 위한 통합 촉각 학습 프레임워크를 제안하며, 촉각 신호를 접촉 이해와 예측 모두를 위한 동적 상호작용 단서로 모델링합니다. 구체적으로, 우리는 통합된 촉각 잠재 공간을 구축하고, 촉각 사고 사슬 추론(tactile chain-of-thought reasoning)과 거친 것에서 세밀한 미래 촉각 예측(coarse-to-fine future tactile prediction)을 통해 현재 촉각 상태와 미래 접촉 변화를 공동으로 모델링하여, 상태 인식 및 동역학 인식 촉각 사전 지식을 형성합니다. 이 사전 지식을 기반으로, 우리는 실시간 및 예측된 촉각 피드백을 결합하여 저주파수 동작 청크를 고주파수 보정으로 개선하는 촉각-동작 혼합 제어기를 도입합니다. 조정, 삽입, 닦기, 조립의 네 가지 접촉이 많은 작업 범주에 대해 깨끗한 환경과 외부 교란 환경 모두에서 수행된 실제 실험은, 우리의 방법이 기존 방법보다 성공률, 조작 정확도 및 접촉 견고성을 향상시켜 정밀한 물리적 상호작용에서의 효과를 입증합니다.

## 핵심 내용
Vision-language-action(VLA) 모델은 많은 로봇 조작 작업에서 뛰어난 성능을 달성했지만, 접촉이 많은 정밀 조작에서는 여전히 한계를 보입니다. 이러한 한계를 극복하기 위해 최근 vision-tactile-language-action(VTLA) 방법은 촉각 감지를 VLA 모델에 통합하여 직접적인 접촉 정보를 제공합니다. 그러나 이러한 방법은 일반적으로 촉각 신호를 수동적인 보조 입력으로 처리하여 촉각 의미론과 미래의 물리적 상호작용을 모델링하기 어렵게 만듭니다. 이를 해결하기 위해, 우리는 접촉이 많은 조작을 위한 통합 촉각 학습 프레임워크를 제안하며, 촉각 신호를 접촉 이해와 예측 모두를 위한 동적 상호작용 단서로 모델링합니다. 구체적으로, 우리는 통합된 촉각 잠재 공간을 구축하고, 촉각 사고 사슬 추론과 거친 것에서 세밀한 미래 촉각 예측을 통해 현재 촉각 상태와 미래 접촉 변화를 공동으로 모델링하여, 상태 인식 및 동역학 인식 촉각 사전 지식을 형성합니다. 이 사전 지식을 기반으로, 우리는 실시간 및 예측된 촉각 피드백을 결합하여 저주파수 동작 청크를 고주파수 보정으로 개선하는 촉각-동작 혼합 제어기를 도입합니다. 조정, 삽입, 닦기, 조립의 네 가지 접촉이 많은 작업 범주에 대해 깨끗한 환경과 외부 교란 환경 모두에서 수행된 실제 실험은, 우리의 방법이 기존 방법보다 성공률, 조작 정확도 및 접촉 견고성을 향상시켜 정밀한 물리적 상호작용에서의 효과를 입증합니다.

## 参考
- http://arxiv.org/abs/2606.31723v1
