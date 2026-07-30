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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.18269v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
많은 Vision-Language-Action(VLA) 모델은 다음 프레임 예측 ``$v_t \rightarrow v_{t+1}$''을 통해 훈련된 내부 세계 모델을 기반으로 구축됩니다. 그러나 이 패러다임은 기본 동역학에 대한 명시적 추론 없이 미래 프레임의 외형을 직접 예측하려고 시도합니다. \textbf{명시적 동작 추론 단계의 부재}는 종종 물리적으로 타당하지 않은 시각적 예측과 비효율적인 정책 학습으로 이어집니다. 이러한 한계를 해결하기 위해, 우리는 모델이 미래 프레임을 생성하기 전에 먼저 \textbf{동작 동역학}에 대해 추론하도록 강제하는 패러다임인 \textbf{Visual Chain of Thought(Visual CoT)}를 도입합니다. 우리는 이 추론 과정을 ``$v_t \rightarrow f_t \rightarrow v_{t+1}$''로 명시적으로 구현하는 자기회귀 트랜스포머인 \textbf{FlowVLA}를 제안함으로써 이 패러다임을 구체화합니다. 여기서 $f_t$는 본질적으로 동작을 인코딩하는 중간 광학 흐름 예측입니다. 모델이 $f_t$에 의해 인코딩된 동작 계획을 먼저 따르도록 강제함으로써, 이 과정은 본질적으로 \textbf{동역학 예측의 사전 훈련 목표를 동작 생성의 하위 작업과 정렬시킵니다.} 우리는 까다로운 로봇 조작 벤치마크와 실제 로봇 평가에서 실험을 수행합니다. FlowVLA는 \textbf{더 일관되고 물리적으로 타당한 시각적 예측}을 생성할 뿐만 아니라, \textbf{상당히 향상된 샘플 효율성}으로 최첨단 정책 성능을 달성하여 VLA에서 세계 모델링을 위한 더 원칙적인 기반을 제시합니다. 프로젝트 페이지: https://irpn-lab.github.io/FlowVLA/

## 핵심 내용
많은 Vision-Language-Action(VLA) 모델은 다음 프레임 예측 ``$v_t \rightarrow v_{t+1}$''을 통해 훈련된 내부 세계 모델을 기반으로 구축됩니다. 그러나 이 패러다임은 기본 동역학에 대한 명시적 추론 없이 미래 프레임의 외형을 직접 예측하려고 시도합니다. \textbf{명시적 동작 추론 단계의 부재}는 종종 물리적으로 타당하지 않은 시각적 예측과 비효율적인 정책 학습으로 이어집니다. 이러한 한계를 해결하기 위해, 우리는 모델이 미래 프레임을 생성하기 전에 먼저 \textbf{동작 동역학}에 대해 추론하도록 강제하는 패러다임인 \textbf{Visual Chain of Thought(Visual CoT)}를 도입합니다. 우리는 이 추론 과정을 ``$v_t \rightarrow f_t \rightarrow v_{t+1}$''로 명시적으로 구현하는 자기회귀 트랜스포머인 \textbf{FlowVLA}를 제안함으로써 이 패러다임을 구체화합니다. 여기서 $f_t$는 본질적으로 동작을 인코딩하는 중간 광학 흐름 예측입니다. 모델이 $f_t$에 의해 인코딩된 동작 계획을 먼저 따르도록 강제함으로써, 이 과정은 본질적으로 \textbf{동역학 예측의 사전 훈련 목표를 동작 생성의 하위 작업과 정렬시킵니다.} 우리는 까다로운 로봇 조작 벤치마크와 실제 로봇 평가에서 실험을 수행합니다. FlowVLA는 \textbf{더 일관되고 물리적으로 타당한 시각적 예측}을 생성할 뿐만 아니라, \textbf{상당히 향상된 샘플 효율성}으로 최첨단 정책 성능을 달성하여 VLA에서 세계 모델링을 위한 더 원칙적인 기반을 제시합니다. 프로젝트 페이지: https://irpn-lab.github.io/FlowVLA/

## 参考
- http://arxiv.org/abs/2508.18269v3
