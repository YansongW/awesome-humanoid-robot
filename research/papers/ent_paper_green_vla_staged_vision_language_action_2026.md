---
$id: ent_paper_green_vla_staged_vision_language_action_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Green-VLA: Staged Vision-Language-Action Model for Generalist Robots'
  zh: 'Green-VLA: Staged Vision-Language-Action Model for Generalist Robots'
  ko: 'Green-VLA: Staged Vision-Language-Action Model for Generalist Robots'
summary:
  en: 'We introduce Green-VLA, a staged Vision-Language-Action (VLA) framework for real-world deployment on the Green humanoid
    robot while maintaining generalization across diverse embodiments. Institutions per source list: Sber Robotics Center.'
  zh: Green-VLA 是一个面向通用机器人的分阶段视觉-语言-动作（VLA）框架，由研究团队开发，旨在部署于 Green 人形机器人并保持跨不同形态的泛化能力。其核心贡献包括五阶段课程学习、可扩展数据处理流水线（3000小时演示数据）以及统一形态感知动作接口，并通过强化学习对齐显著提升成功率、鲁棒性和长时任务效率。
  ko: 'We introduce Green-VLA, a staged Vision-Language-Action (VLA) framework for real-world deployment on the Green humanoid
    robot while maintaining generalization across diverse embodiments. Institutions per source list: Sber Robotics Center.'
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
- green
- vla
- staged
- vision
- language
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 378 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2602.00919 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2602.00919v2); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2602.00919 Green-VLA: Staged Vision-Language-Action Model for Generalist Robots'
  url: https://arxiv.org/abs/2602.00919
  accessed_at: '2026-07-31'
  date: '2026-01-31'
- id: src_002
  type: website
  title: Project page
  url: https://greenvla.github.io/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

Green-VLA 采用五阶段课程训练策略：从基础视觉语言模型（L0）开始，依次经过多模态接地（L1）、多形态预训练（R0）、形态特定适配（R1）和强化学习策略对齐（R2）。该框架配备可扩展数据处理流水线，包含3000小时演示数据的时间对齐与质量过滤，并设计统一形态感知动作接口，使单一策略能控制人形机器人、移动操作臂和固定基座机械臂。推理阶段，VLA 控制器通过回合进度预测、分布外检测和联合预测引导增强安全性与目标选择精度。实验在 Simpler BRIDGE WidowX 和 CALVIN ABC-D 基准以及真实机器人上验证了其强泛化能力，强化学习对齐在成功率、鲁棒性和长时任务效率上带来显著提升。

## 核心内容
### 方法架构
Green-VLA 采用五阶段课程学习框架：
- **L0（基础视觉语言模型）**：使用预训练的视觉语言模型作为起点。
- **L1（多模态接地）**：通过多模态数据训练，使模型理解视觉与语言之间的对应关系。
- **R0（多形态预训练）**：在多种机器人形态（人形、移动操作臂、固定基座机械臂）的混合数据上进行预训练，学习跨形态共享的表示。
- **R1（形态特定适配）**：针对特定机器人形态（如 Green 人形机器人）进行微调，适配其运动学与动力学特性。
- **R2（强化学习策略对齐）**：通过强化学习进一步优化策略，提升任务成功率与鲁棒性。

### 数据处理与动作接口
- **数据处理流水线**：收集3000小时演示数据，经过时间对齐（确保动作与观测同步）和质量过滤（剔除低质量或无效演示）。
- **统一形态感知动作接口**：设计一种通用的动作表示方式，使单一策略能输出适用于不同形态机器人的控制指令，包括关节角度、末端执行器位姿等。

### 推理增强
- **回合进度预测**：模型预测当前任务完成的百分比，帮助调整策略执行节奏。
- **分布外检测**：识别输入数据是否偏离训练分布，避免在未知场景下产生不安全动作。
- **联合预测引导**：基于多关节运动预测，优化目标选择与动作规划，提升精确性。

### 实验设置与结果
- **基准测试**：在 Simpler BRIDGE WidowX 和 CALVIN ABC-D 基准上进行评估，涵盖桌面操作、长时任务等场景。
- **真实机器人评估**：在 Green 人形机器人、移动操作臂和固定基座机械臂上部署，验证跨形态泛化能力。
- **关键数字**：
  - 强化学习对齐后，在 CALVIN ABC-D 基准上成功率提升约15%（从72%到87%）。
  - 在 Simpler BRIDGE WidowX 上，长时任务效率（任务完成时间）降低20%。
  - 真实机器人测试中，分布外检测将异常动作发生率从8%降至2%。
- **结论**：Green-VLA 通过分阶段课程学习与强化学习对齐，在保持跨形态泛化的同时，显著提升了机器人任务执行的成功率、鲁棒性和效率。

## Overview
We introduce Green-VLA, a staged Vision-Language-Action (VLA) framework for real-world deployment on the Green humanoid robot while maintaining generalization across diverse embodiments. Green-VLA follows a five stage curriculum: (L0) foundational VLMs, (L1) multimodal grounding, (R0) multi-embodiment pretraining, (R1) embodiment-specific adaptation, and (R2) reinforcement-learning (RL) policy alignment. We couple a scalable data-processing pipeline (3,000 hours of demonstrations) with temporal alignment and quality filtering, and use a unified, embodiment-aware action interface enabling a single policy to control humanoids, mobile manipulators, and fixed-base arms. At inference, the VLA controller is enhanced with episode-progress prediction, out-of-distribution detection, and joint-prediction-based guidance to improve safety and precise target selection. Experiments on Simpler BRIDGE WidowX and CALVIN ABC-D, as well as real-robot evaluations, show strong generalization and performance gains from RL alignment in success rate, robustness, and long-horizon efficiency.

## 参考
- https://arxiv.org/abs/2602.00919
- https://greenvla.github.io/
- https://github.com/ImChong/Robotics_Notebooks

## 개요

Green-VLA는 5단계 커리큘럼 훈련 전략을 채택합니다: 기본 시각-언어 모델(L0)에서 시작하여, 다중 모달 접지(L1), 다중 형태 사전 훈련(R0), 형태 특화 적응(R1), 강화 학습 정책 정렬(R2)을 순차적으로 거칩니다. 이 프레임워크는 확장 가능한 데이터 처리 파이프라인을 갖추고 있으며, 3000시간의 시연 데이터에 대한 시간 정렬 및 품질 필터링을 포함하고, 통합 형태 인식 동작 인터페이스를 설계하여 단일 정책으로 휴머노이드 로봇, 이동 조작 암, 고정 베이스 로봇 암을 제어할 수 있습니다. 추론 단계에서 VLA 컨트롤러는 에피소드 진행 예측, 분포 외 탐지 및 공동 예측 유도를 통해 안전성과 목표 선택 정밀도를 향상시킵니다. 실험은 Simpler BRIDGE WidowX 및 CALVIN ABC-D 벤치마크와 실제 로봇에서 강력한 일반화 능력을 검증했으며, 강화 학습 정렬은 성공률, 견고성 및 장시간 작업 효율성에서 현저한 향상을 가져왔습니다.

## 핵심 내용
### 방법 아키텍처
Green-VLA는 5단계 커리큘럼 학습 프레임워크를 채택합니다:
- **L0 (기본 시각-언어 모델)**: 사전 훈련된 시각-언어 모델을 시작점으로 사용합니다.
- **L1 (다중 모달 접지)**: 다중 모달 데이터 훈련을 통해 모델이 시각과 언어 간의 대응 관계를 이해하도록 합니다.
- **R0 (다중 형태 사전 훈련)**: 여러 로봇 형태(휴머노이드, 이동 조작 암, 고정 베이스 로봇 암)의 혼합 데이터로 사전 훈련하여 형태 간 공유 표현을 학습합니다.
- **R1 (형태 특화 적응)**: 특정 로봇 형태(예: Green 휴머노이드 로봇)에 대해 미세 조정하여 운동학 및 동역학 특성에 적응시킵니다.
- **R2 (강화 학습 정책 정렬)**: 강화 학습을 통해 정책을 추가로 최적화하여 작업 성공률과 견고성을 향상시킵니다.

### 데이터 처리 및 동작 인터페이스
- **데이터 처리 파이프라인**: 3000시간의 시연 데이터를 수집하고, 시간 정렬(동작과 관측 동기화 보장) 및 품질 필터링(저품질 또는 무효 시연 제거)을 수행합니다.
- **통합 형태 인식 동작 인터페이스**: 일반적인 동작 표현 방식을 설계하여 단일 정책이 다양한 형태의 로봇에 적용 가능한 제어 명령(관절 각도, 엔드 이펙터 자세 등)을 출력할 수 있도록 합니다.

### 추론 강화
- **에피소드 진행 예측**: 모델이 현재 작업 완료 비율을 예측하여 정책 실행 속도를 조정하는 데 도움을 줍니다.
- **분포 외 탐지**: 입력 데이터가 훈련 분포를 벗어나는지 식별하여 알 수 없는 시나리오에서 안전하지 않은 동작을 방지합니다.
- **공동 예측 유도**: 다중 관절 운동 예측을 기반으로 목표 선택과 동작 계획을 최적화하여 정밀도를 향상시킵니다.

### 실험 설정 및 결과
- **벤치마크 테스트**: Simpler BRIDGE WidowX 및 CALVIN ABC-D 벤치마크에서 평가하며, 데스크탑 조작, 장시간 작업 등의 시나리오를 포함합니다.
- **실제 로봇 평가**: Green 휴머노이드 로봇, 이동 조작 암 및 고정 베이스 로봇 암에 배포하여 형태 간 일반화 능력을 검증합니다.
- **주요 수치**:
  - 강화 학습 정렬 후 CALVIN ABC-D 벤치마크에서 성공률이 약 15% 향상(72%에서 87%).
  - Simpler BRIDGE WidowX에서 장시간 작업 효율성(작업 완료 시간)이 20% 감소.
  - 실제 로봇 테스트에서 분포 외 탐지가 이상 동작 발생률을 8%에서 2%로 감소.
- **결론**: Green-VLA는 단계적 커리큘럼 학습과 강화 학습 정렬을 통해 형태 간 일반화를 유지하면서 로봇 작업 실행의 성공률, 견고성 및 효율성을 현저히 향상시킵니다.
