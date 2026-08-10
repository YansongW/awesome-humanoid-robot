---
$id: ent_paper_zhong_flowvla_visual_chain_of_though_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models'
  zh: FlowVLA
  ko: 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models'
summary:
  en: 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models (FlowVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Shanghai Jiao Tong University.'
  zh: FlowVLA 是香港科技大学（广州）与上海交通大学于2025年提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于引入视觉思维链（Visual CoT），强制模型在预测未来帧之前先推理运动动态（光流），从而提升视觉预测的物理合理性与策略学习效率。
  ko: 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models (FlowVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Shanghai Jiao Tong University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- flowvla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.18269v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1051 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2508.18269
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型通常基于下一帧预测范式（$v_t \rightarrow v_{t+1}$）训练内部世界模型，但该范式直接预测未来帧外观，缺乏对底层运动动态的显式推理，导致视觉预测常违反物理规律且策略学习效率低下。FlowVLA 提出视觉思维链（Visual CoT），将推理过程重构为 $v_t \rightarrow f_t \rightarrow v_{t+1}$，其中 $f_t$ 是中间光流预测，天然编码运动信息。通过强制模型先遵循光流编码的运动计划，该方法使动力学预测的预训练目标与动作生成的下游任务自然对齐。实验表明，FlowVLA 在机器人操作基准和真实机器人评估中均生成更连贯、物理合理的视觉预测，并以显著提升的样本效率达到最先进的策略性能。

## 核心内容
### 方法架构
- **核心范式**：提出 Visual Chain of Thought (Visual CoT)，将传统下一帧预测 $v_t \rightarrow v_{t+1}$ 扩展为 $v_t \rightarrow f_t \rightarrow v_{t+1}$，其中 $f_t$ 为中间光流预测。
- **模型设计**：FlowVLA 采用自回归 Transformer 架构，显式实例化该推理过程。光流 $f_t$ 作为运动编码的中间表示，强制模型先推理运动动态再生成未来帧。
- **对齐机制**：通过先遵循光流编码的运动计划，使动力学预测的预训练目标与动作生成的下游任务自然对齐，解决传统范式缺乏显式运动推理的问题。

### 实验设置
- **基准测试**：在多个具有挑战性的机器人操作基准上进行评估，包括仿真环境和真实机器人平台。
- **对比方法**：与现有 VLA 模型（如基于下一帧预测的基线）进行对比，评估视觉预测质量和策略性能。

### 关键结果
- **视觉预测质量**：FlowVLA 生成更连贯、物理合理的视觉预测，避免传统范式中的物理不合理预测。
- **策略性能**：在机器人操作任务上达到最先进的策略性能，样本效率显著提升。
- **效率优势**：通过显式运动推理，减少无效探索，加速策略学习过程。

### 结论
FlowVLA 通过 Visual CoT 范式为 VLA 模型的世界建模提供了更原则性的基础，证明了显式运动推理在提升视觉预测和策略学习方面的有效性。项目页面：https://irpn-lab.github.io/FlowVLA/

## Overview
Many Vision-Language-Action (VLA) models are built upon an internal world model trained via next-frame prediction ``$v_t \rightarrow v_{t+1}$''. However, this paradigm attempts to predict the future frame's appearance directly, without explicitly reasoning about the underlying dynamics. \textbf{This lack of an explicit motion reasoning step} often leads to physically implausible visual forecasts and inefficient policy learning. To address this limitation, we introduce the \textbf{Visual Chain of Thought (Visual CoT)}, a paradigm that compels the model to first reason about \textbf{motion dynamics} before generating the future frame. We instantiate this paradigm by proposing \textbf{FlowVLA}, an autoregressive Transformer that explicitly materializes this reasoning process as ``$v_t \rightarrow f_t \rightarrow v_{t+1}$'', where $f_t$ is an intermediate optical flow prediction that inherently encodes motion. By forcing the model to first follow the motion plan encoded by $f_t$, this process inherently \textbf{aligns the pre-training objective of dynamics prediction with the downstream task of action generation.} We conduct experiments on challenging robotics manipulation benchmarks, as well as real-robot evaluations. Our FlowVLA not only generates \textbf{more coherent and physically plausible visual predictions}, but also achieves state-of-the-art policy performance with \textbf{substantially improved sample efficiency}, pointing toward a more principled foundation for world modeling in VLAs. Project page: https://irpn-lab.github.io/FlowVLA/

## Overview
Many Vision-Language-Action (VLA) models are built upon an internal world model trained via next-frame prediction ``$v_t \rightarrow v_{t+1}$''. However, this paradigm attempts to predict the future frame's appearance directly, without explicitly reasoning about the underlying dynamics. **This lack of an explicit motion reasoning step** often leads to physically implausible visual forecasts and inefficient policy learning. To address this limitation, we introduce the **Visual Chain of Thought (Visual CoT)**, a paradigm that compels the model to first reason about **motion dynamics** before generating the future frame. We instantiate this paradigm by proposing **FlowVLA**, an autoregressive Transformer that explicitly materializes this reasoning process as ``$v_t \rightarrow f_t \rightarrow v_{t+1}$'', where $f_t$ is an intermediate optical flow prediction that inherently encodes motion. By forcing the model to first follow the motion plan encoded by $f_t$, this process inherently **aligns the pre-training objective of dynamics prediction with the downstream task of action generation.** We conduct experiments on challenging robotics manipulation benchmarks, as well as real-robot evaluations. Our FlowVLA not only generates **more coherent and physically plausible visual predictions**, but also achieves state-of-the-art policy performance with **substantially improved sample efficiency**, pointing toward a more principled foundation for world modeling in VLAs. Project page: https://irpn-lab.github.io/FlowVLA/

## Content
Many Vision-Language-Action (VLA) models are built upon an internal world model trained via next-frame prediction ``$v_t \rightarrow v_{t+1}$''. However, this paradigm attempts to predict the future frame's appearance directly, without explicitly reasoning about the underlying dynamics. **This lack of an explicit motion reasoning step** often leads to physically implausible visual forecasts and inefficient policy learning. To address this limitation, we introduce the **Visual Chain of Thought (Visual CoT)**, a paradigm that compels the model to first reason about **motion dynamics** before generating the future frame. We instantiate this paradigm by proposing **FlowVLA**, an autoregressive Transformer that explicitly materializes this reasoning process as ``$v_t \rightarrow f_t \rightarrow v_{t+1}$'', where $f_t$ is an intermediate optical flow prediction that inherently encodes motion. By forcing the model to first follow the motion plan encoded by $f_t$, this process inherently **aligns the pre-training objective of dynamics prediction with the downstream task of action generation.** We conduct experiments on challenging robotics manipulation benchmarks, as well as real-robot evaluations. Our FlowVLA not only generates **more coherent and physically plausible visual predictions**, but also achieves state-of-the-art policy performance with **substantially improved sample efficiency**, pointing toward a more principled foundation for world modeling in VLAs. Project page: https://irpn-lab.github.io/FlowVLA/

## 参考
- http://arxiv.org/abs/2508.18269v3

## 개요
기존의 비전-언어-행동 모델은 일반적으로 다음 프레임 예측 패러다임($v_t \rightarrow v_{t+1}$)을 기반으로 내부 세계 모델을 학습하지만, 이 패러다임은 미래 프레임의 외형을 직접 예측할 뿐, 하위 운동 역학에 대한 명시적 추론이 부족하여 시각적 예측이 물리 법칙을 위반하는 경우가 많고 정책 학습 효율성이 낮습니다. FlowVLA는 시각적 사고 사슬(Visual CoT)을 제안하여 추론 과정을 $v_t \rightarrow f_t \rightarrow v_{t+1}$로 재구성합니다. 여기서 $f_t$는 중간 광학 흐름 예측으로, 운동 정보를 자연스럽게 인코딩합니다. 모델이 먼저 광학 흐름으로 인코딩된 운동 계획을 따르도록 강제함으로써, 이 방법은 역학 예측의 사전 학습 목표와 하위 동작 생성 작업을 자연스럽게 정렬합니다. 실험 결과, FlowVLA는 로봇 조작 벤치마크와 실제 로봇 평가에서 더 일관되고 물리적으로 타당한 시각적 예측을 생성하며, 현저히 향상된 샘플 효율성으로 최첨단 정책 성능에 도달합니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 패러다임**: Visual Chain of Thought (Visual CoT)를 제안하여 기존의 다음 프레임 예측 $v_t \rightarrow v_{t+1}$을 $v_t \rightarrow f_t \rightarrow v_{t+1}$로 확장합니다. 여기서 $f_t$는 중간 광학 흐름 예측입니다.
- **모델 설계**: FlowVLA는 자기회귀 Transformer 아키텍처를 채택하여 이 추론 과정을 명시적으로 구현합니다. 광학 흐름 $f_t$는 운동 인코딩의 중간 표현으로 작용하며, 모델이 미래 프레임을 생성하기 전에 먼저 운동 역학을 추론하도록 강제합니다.
- **정렬 메커니즘**: 먼저 광학 흐름으로 인코딩된 운동 계획을 따르게 함으로써, 역학 예측의 사전 학습 목표와 하위 동작 생성 작업을 자연스럽게 정렬하여 기존 패러다임의 명시적 운동 추론 부재 문제를 해결합니다.

### 실험 설정
- **벤치마크 테스트**: 시뮬레이션 환경과 실제 로봇 플랫폼을 포함한 여러 도전적인 로봇 조작 벤치마크에서 평가를 수행합니다.
- **비교 방법**: 기존 VLA 모델(예: 다음 프레임 예측 기반 기준선)과 비교하여 시각적 예측 품질과 정책 성능을 평가합니다.

### 주요 결과
- **시각적 예측 품질**: FlowVLA는 더 일관되고 물리적으로 타당한 시각적 예측을 생성하여 기존 패러다임의 물리적으로 비합리적인 예측을 방지합니다.
- **정책 성능**: 로봇 조작 작업에서 최첨단 정책 성능에 도달하며 샘플 효율성이 현저히 향상됩니다.
- **효율성 이점**: 명시적 운동 추론을 통해 비효율적인 탐색을 줄이고 정책 학습 과정을 가속화합니다.

### 결론
FlowVLA는 Visual CoT 패러다임을 통해 VLA 모델의 세계 모델링에 더 원칙적인 기반을 제공하며, 명시적 운동 추론이 시각적 예측과 정책 학습 향상에 효과적임을 입증합니다. 프로젝트 페이지: https://irpn-lab.github.io/FlowVLA/
