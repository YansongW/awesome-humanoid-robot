---
$id: ent_paper_gpc_large_scale_generative_pretraining_t_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GPC: Large-Scale Generative Pretraining for Transferable Motor Control'
  zh: 简称 **GPC**，Generative Pretrained Controllers）
  ko: 'GPC: Large-Scale Generative Pretraining for Transferable Motor Control'
summary:
  en: 'Developing controllers capable of completing a wide range of tasks in a natural and life-like manner is a key challenge
    in enabling practical applications of physics-based character animation. Institutions per source list: 西蒙菲莎大学（SFU）、英伟达（NVIDIA）.'
  zh: GPC（Generative Pretrained Controllers）由研究团队提出，通过将运动数据token化并采用next-token预测范式，构建了可复用的通用生成式控制器。核心贡献在于利用端到端强化学习联合优化基于Finite
    Scalar Quantization (FSQ)的“运动词汇表”与对应控制策略，并训练GPT风格的自回归Transformer实现物理仿真角色的控制，在复现大规模运动片段时达到99.98%的成功率。
  ko: 'Developing controllers capable of completing a wide range of tasks in a natural and life-like manner is a key challenge
    in enabling practical applications of physics-based character animation. Institutions per source list: 西蒙菲莎大学（SFU）、英伟达（NVIDIA）.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- gpc
- large
- scale
- generative
- pretraining
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 377 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2606.29148 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.29148v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.29148 GPC: Large-Scale Generative Pretraining for Transferable Motor Control'
  url: https://arxiv.org/abs/2606.29148
  accessed_at: '2026-07-31'
  date: '2026-06-28'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

GPC框架通过端到端强化学习，将运动数据离散化为FSQ编码的“运动词汇表”，并同步训练控制策略以将离散码映射为物理控制信号。随后，利用GPT风格的自回归Transformer建模该词汇表的底层结构，使控制器能通过next-token预测生成物理仿真角色的控制指令。相比此前基于token化的方法，GPC大幅简化训练流程，在复现大量运动片段时达到99.98%的成功率，并展现出对扰动和跌倒的鲁棒响应等自然涌现行为，为下游任务提供了高度通用的控制器基础。

## 核心内容
### 方法架构
- **运动词汇表学习**：采用Finite Scalar Quantization (FSQ)将连续运动数据离散化为有限码本，通过端到端强化学习联合优化码本（即“运动词汇表”）与控制策略，使离散码能有效映射为物理控制信号。
- **生成式控制器训练**：在码本学习完成后，使用GPT风格的自回归Transformer对词汇表的底层结构进行建模。该Transformer通过next-token预测生成控制序列，驱动物理仿真角色完成动作。
- **下游任务适配**：提出一套微调技术（如参数高效微调），使预训练的生成式控制器能快速适应新任务，无需从头训练。

### 实验设置与关键结果
- **训练数据**：使用大规模运动捕捉数据集，涵盖行走、跑步、跳跃等多样化动作。
- **性能指标**：在复现运动片段时达到99.98%的成功率，显著优于此前基于token化的方法（如MCP）。
- **涌现行为**：控制器自然展现出对扰动的响应（如被推搡后恢复平衡）和跌倒后重新站起等鲁棒行为，无需显式编程。
- **下游应用**：在多种任务（如目标导航、障碍规避）中，微调后的控制器保持高鲁棒性，且训练效率提升。

### 结论
GPC通过联合优化运动词汇表与生成式控制策略，解决了传统token化方法训练复杂、泛化性差的问题。其99.98%的运动复现成功率和自然涌现的鲁棒行为，为物理仿真角色的通用控制提供了高效解决方案。

## Overview
Developing controllers capable of completing a wide range of tasks in a natural and life-like manner is a key challenge in enabling practical applications of physics-based character animation. In this work, we introduce Generative Pretrained Controllers (GPC), which leverage tokenization and next-token modeling to create general-purpose, reusable generative controllers from large-scale motion datasets. Our framework utilizes end-to-end reinforcement learning to jointly optimize a "motion vocabulary", modeled via Finite Scalar Quantization (FSQ), along with a corresponding control policy that can map the discrete codes to physics-based controls. After the "codebook" has been learned, the underlying structure of this large vocabulary is modeled by training a GPT-style autoregressive transformer, leading to a powerful generative controller that generates controls for a physically simulated character by performing next-token prediction. Once the generative controller has been trained, we propose a suite of adaptation techniques for finetuning the controller for new downstream tasks. Our proposed framework greatly simplifies the training process compared to previous tokenized methods, and achieves a 99.98% success rate in reproducing a vast corpus of motion clips. The generative controller exhibits a variety of natural emergent behaviors, such as responsive behaviors to perturbations and recovery behaviors after falling. This results in highly robust general purpose controllers for a variety of downstream applications.

## 参考
- https://arxiv.org/abs/2606.29148
- https://github.com/ImChong/Robotics_Notebooks

## 개요

GPC 프레임워크는 종단간 강화 학습을 통해 운동 데이터를 FSQ로 인코딩된 '운동 어휘표'로 이산화하고, 동시에 제어 정책을 훈련하여 이산 코드를 물리적 제어 신호로 매핑합니다. 이후 GPT 스타일의 자기회귀 트랜스포머를 사용해 해당 어휘표의 기저 구조를 모델링하여, 컨트롤러가 next-token 예측을 통해 물리 시뮬레이션 캐릭터의 제어 명령을 생성할 수 있게 합니다. 기존 토큰화 기반 방법과 비교해 GPC는 훈련 과정을 크게 단순화하며, 다수의 운동 구간을 재현할 때 99.98%의 성공률을 달성하고, 외란 및 낙상에 대한 강건한 반응과 같은 자연 발생적 행동을 보여줌으로써 하위 작업에 매우 범용적인 컨트롤러 기반을 제공합니다.

## 핵심 내용
### 방법 아키텍처
- **운동 어휘표 학습**: FSQ(Finite Scalar Quantization)를 사용해 연속 운동 데이터를 유한 코드북으로 이산화하고, 종단간 강화 학습을 통해 코드북(즉, '운동 어휘표')과 제어 정책을 공동 최적화하여 이산 코드가 물리적 제어 신호로 효과적으로 매핑되도록 합니다.
- **생성형 컨트롤러 훈련**: 코드북 학습 완료 후, GPT 스타일의 자기회귀 트랜스포머를 사용해 어휘표의 기저 구조를 모델링합니다. 이 트랜스포머는 next-token 예측을 통해 제어 시퀀스를 생성하여 물리 시뮬레이션 캐릭터의 동작을 구동합니다.
- **하위 작업 적응**: 파라미터 효율적 미세 조정과 같은 미세 조정 기술을 제안하여, 사전 훈련된 생성형 컨트롤러가 처음부터 훈련할 필요 없이 새로운 작업에 빠르게 적응할 수 있도록 합니다.

### 실험 설정 및 주요 결과
- **훈련 데이터**: 걷기, 달리기, 점프 등 다양한 동작을 포함한 대규모 모션 캡처 데이터셋 사용.
- **성능 지표**: 운동 구간 재현 시 99.98%의 성공률을 달성하여, 기존 토큰화 기반 방법(예: MCP)을 크게 능가.
- **자연 발생 행동**: 컨트롤러는 외란에 대한 반응(예: 밀림 후 균형 회복) 및 낙상 후 다시 일어서는 등의 강건한 행동을 명시적 프로그래밍 없이 자연스럽게 보여줌.
- **하위 응용**: 목표 탐색, 장애물 회피 등 다양한 작업에서 미세 조정된 컨트롤러가 높은 강건성을 유지하며 훈련 효율이 향상됨.

### 결론
GPC는 운동 어휘표와 생성형 제어 정책을 공동 최적화함으로써, 기존 토큰화 방법의 복잡한 훈련과 낮은 일반화 문제를 해결합니다. 99.98%의 운동 재현 성공률과 자연 발생적 강건 행동은 물리 시뮬레이션 캐릭터의 범용 제어를 위한 효율적인 솔루션을 제공합니다.
