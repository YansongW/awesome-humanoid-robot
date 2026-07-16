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
  zh: 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models (FlowVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by HKUST(GZ), Shanghai Jiao Tong University.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.18269v3.
sources:
- id: src_001
  type: paper
  title: 'FlowVLA: Visual Chain of Thought-based Motion Reasoning for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2508.18269
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Many Vision-Language-Action (VLA) models are built upon an internal world model trained via next-frame prediction ``$v_t \rightarrow v_{t+1}$''. However, this paradigm attempts to predict the future frame's appearance directly, without explicitly reasoning about the underlying dynamics. \textbf{This lack of an explicit motion reasoning step} often leads to physically implausible visual forecasts and inefficient policy learning. To address this limitation, we introduce the \textbf{Visual Chain of Thought (Visual CoT)}, a paradigm that compels the model to first reason about \textbf{motion dynamics} before generating the future frame. We instantiate this paradigm by proposing \textbf{FlowVLA}, an autoregressive Transformer that explicitly materializes this reasoning process as ``$v_t \rightarrow f_t \rightarrow v_{t+1}$'', where $f_t$ is an intermediate optical flow prediction that inherently encodes motion. By forcing the model to first follow the motion plan encoded by $f_t$, this process inherently \textbf{aligns the pre-training objective of dynamics prediction with the downstream task of action generation.} We conduct experiments on challenging robotics manipulation benchmarks, as well as real-robot evaluations. Our FlowVLA not only generates \textbf{more coherent and physically plausible visual predictions}, but also achieves state-of-the-art policy performance with \textbf{substantially improved sample efficiency}, pointing toward a more principled foundation for world modeling in VLAs. Project page: https://irpn-lab.github.io/FlowVLA/

## 核心内容
Many Vision-Language-Action (VLA) models are built upon an internal world model trained via next-frame prediction ``$v_t \rightarrow v_{t+1}$''. However, this paradigm attempts to predict the future frame's appearance directly, without explicitly reasoning about the underlying dynamics. \textbf{This lack of an explicit motion reasoning step} often leads to physically implausible visual forecasts and inefficient policy learning. To address this limitation, we introduce the \textbf{Visual Chain of Thought (Visual CoT)}, a paradigm that compels the model to first reason about \textbf{motion dynamics} before generating the future frame. We instantiate this paradigm by proposing \textbf{FlowVLA}, an autoregressive Transformer that explicitly materializes this reasoning process as ``$v_t \rightarrow f_t \rightarrow v_{t+1}$'', where $f_t$ is an intermediate optical flow prediction that inherently encodes motion. By forcing the model to first follow the motion plan encoded by $f_t$, this process inherently \textbf{aligns the pre-training objective of dynamics prediction with the downstream task of action generation.} We conduct experiments on challenging robotics manipulation benchmarks, as well as real-robot evaluations. Our FlowVLA not only generates \textbf{more coherent and physically plausible visual predictions}, but also achieves state-of-the-art policy performance with \textbf{substantially improved sample efficiency}, pointing toward a more principled foundation for world modeling in VLAs. Project page: https://irpn-lab.github.io/FlowVLA/

## 参考
- http://arxiv.org/abs/2508.18269v3

## Overview
Many Vision-Language-Action (VLA) models are built upon an internal world model trained via next-frame prediction ``$v_t \rightarrow v_{t+1}$''. However, this paradigm attempts to predict the future frame's appearance directly, without explicitly reasoning about the underlying dynamics. **This lack of an explicit motion reasoning step** often leads to physically implausible visual forecasts and inefficient policy learning. To address this limitation, we introduce the **Visual Chain of Thought (Visual CoT)**, a paradigm that compels the model to first reason about **motion dynamics** before generating the future frame. We instantiate this paradigm by proposing **FlowVLA**, an autoregressive Transformer that explicitly materializes this reasoning process as ``$v_t \rightarrow f_t \rightarrow v_{t+1}$'', where $f_t$ is an intermediate optical flow prediction that inherently encodes motion. By forcing the model to first follow the motion plan encoded by $f_t$, this process inherently **aligns the pre-training objective of dynamics prediction with the downstream task of action generation.** We conduct experiments on challenging robotics manipulation benchmarks, as well as real-robot evaluations. Our FlowVLA not only generates **more coherent and physically plausible visual predictions**, but also achieves state-of-the-art policy performance with **substantially improved sample efficiency**, pointing toward a more principled foundation for world modeling in VLAs. Project page: https://irpn-lab.github.io/FlowVLA/

## Content
Many Vision-Language-Action (VLA) models are built upon an internal world model trained via next-frame prediction ``$v_t \rightarrow v_{t+1}$''. However, this paradigm attempts to predict the future frame's appearance directly, without explicitly reasoning about the underlying dynamics. **This lack of an explicit motion reasoning step** often leads to physically implausible visual forecasts and inefficient policy learning. To address this limitation, we introduce the **Visual Chain of Thought (Visual CoT)**, a paradigm that compels the model to first reason about **motion dynamics** before generating the future frame. We instantiate this paradigm by proposing **FlowVLA**, an autoregressive Transformer that explicitly materializes this reasoning process as ``$v_t \rightarrow f_t \rightarrow v_{t+1}$'', where $f_t$ is an intermediate optical flow prediction that inherently encodes motion. By forcing the model to first follow the motion plan encoded by $f_t$, this process inherently **aligns the pre-training objective of dynamics prediction with the downstream task of action generation.** We conduct experiments on challenging robotics manipulation benchmarks, as well as real-robot evaluations. Our FlowVLA not only generates **more coherent and physically plausible visual predictions**, but also achieves state-of-the-art policy performance with **substantially improved sample efficiency**, pointing toward a more principled foundation for world modeling in VLAs. Project page: https://irpn-lab.github.io/FlowVLA/

## 개요
많은 Vision-Language-Action(VLA) 모델은 다음 프레임 예측 ``$v_t \rightarrow v_{t+1}$''을 통해 훈련된 내부 세계 모델을 기반으로 구축됩니다. 그러나 이 패러다임은 기본 동역학에 대한 명시적 추론 없이 미래 프레임의 외형을 직접 예측하려고 시도합니다. \textbf{명시적 동작 추론 단계의 부재}는 종종 물리적으로 타당하지 않은 시각적 예측과 비효율적인 정책 학습으로 이어집니다. 이러한 한계를 해결하기 위해, 우리는 모델이 미래 프레임을 생성하기 전에 먼저 \textbf{동작 동역학}에 대해 추론하도록 강제하는 패러다임인 \textbf{Visual Chain of Thought(Visual CoT)}를 도입합니다. 우리는 이 추론 과정을 ``$v_t \rightarrow f_t \rightarrow v_{t+1}$''로 명시적으로 구현하는 자기회귀 트랜스포머인 \textbf{FlowVLA}를 제안함으로써 이 패러다임을 구체화합니다. 여기서 $f_t$는 본질적으로 동작을 인코딩하는 중간 광학 흐름 예측입니다. 모델이 $f_t$에 의해 인코딩된 동작 계획을 먼저 따르도록 강제함으로써, 이 과정은 본질적으로 \textbf{동역학 예측의 사전 훈련 목표를 동작 생성의 하위 작업과 정렬시킵니다.} 우리는 까다로운 로봇 조작 벤치마크와 실제 로봇 평가에서 실험을 수행합니다. FlowVLA는 \textbf{더 일관되고 물리적으로 타당한 시각적 예측}을 생성할 뿐만 아니라, \textbf{상당히 향상된 샘플 효율성}으로 최첨단 정책 성능을 달성하여 VLA에서 세계 모델링을 위한 더 원칙적인 기반을 제시합니다. 프로젝트 페이지: https://irpn-lab.github.io/FlowVLA/

## 핵심 내용
많은 Vision-Language-Action(VLA) 모델은 다음 프레임 예측 ``$v_t \rightarrow v_{t+1}$''을 통해 훈련된 내부 세계 모델을 기반으로 구축됩니다. 그러나 이 패러다임은 기본 동역학에 대한 명시적 추론 없이 미래 프레임의 외형을 직접 예측하려고 시도합니다. \textbf{명시적 동작 추론 단계의 부재}는 종종 물리적으로 타당하지 않은 시각적 예측과 비효율적인 정책 학습으로 이어집니다. 이러한 한계를 해결하기 위해, 우리는 모델이 미래 프레임을 생성하기 전에 먼저 \textbf{동작 동역학}에 대해 추론하도록 강제하는 패러다임인 \textbf{Visual Chain of Thought(Visual CoT)}를 도입합니다. 우리는 이 추론 과정을 ``$v_t \rightarrow f_t \rightarrow v_{t+1}$''로 명시적으로 구현하는 자기회귀 트랜스포머인 \textbf{FlowVLA}를 제안함으로써 이 패러다임을 구체화합니다. 여기서 $f_t$는 본질적으로 동작을 인코딩하는 중간 광학 흐름 예측입니다. 모델이 $f_t$에 의해 인코딩된 동작 계획을 먼저 따르도록 강제함으로써, 이 과정은 본질적으로 \textbf{동역학 예측의 사전 훈련 목표를 동작 생성의 하위 작업과 정렬시킵니다.} 우리는 까다로운 로봇 조작 벤치마크와 실제 로봇 평가에서 실험을 수행합니다. FlowVLA는 \textbf{더 일관되고 물리적으로 타당한 시각적 예측}을 생성할 뿐만 아니라, \textbf{상당히 향상된 샘플 효율성}으로 최첨단 정책 성능을 달성하여 VLA에서 세계 모델링을 위한 더 원칙적인 기반을 제시합니다. 프로젝트 페이지: https://irpn-lab.github.io/FlowVLA/
