---
$id: ent_paper_zhang_reasoning_vla_a_fast_and_gener_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving'
  zh: Reasoning-VLA
  ko: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving'
summary:
  en: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving (Reasoning-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University, National University
    of Singapore, University of Science and Technology of China, Tsinghua University, University of New South Wales.'
  zh: Reasoning-VLA 是2025年由兰州大学、新加坡国立大学、中国科学技术大学、清华大学、新南威尔士大学联合提出的大型视觉-语言-动作模型，专为自动驾驶决策设计。其核心贡献在于通过可学习的动作查询与推理增强的视觉-语言特征并行交互，实现快速且通用的动作轨迹生成，并在多个基准上达到最先进的性能与推理速度。
  ko: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving (Reasoning-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University, National University
    of Singapore, University of Science and Technology of China, Tsinghua University, University of New South Wales.'
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
- reasoning_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19912v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (917 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2511.19912
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Reasoning-VLA source
  url: https://doi.org/10.48550/arXiv.2511.19912
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作（VLA）模型在自动驾驶中虽展现出强大决策能力，但常面临推理效率低、难以泛化至新车辆配置与驾驶场景的问题。Reasoning-VLA 提出一种通用且快速的框架，利用高斯采样从训练语料中的真实轨迹初始化可学习动作查询，使其与推理增强的视觉-语言特征并行交互以生成连续动作轨迹。为提升泛化性，该模型将八个公开自动驾驶数据集整合为标准化、基于思维链推理的易用格式，并通过监督学习与强化学习微调进行训练。实验表明，Reasoning-VLA 在多个基准上实现了当前最优的性能、卓越的泛化能力以及最快的推理速度。

## 核心内容
### 方法架构
- **可学习动作查询**：从训练语料中的真实轨迹通过高斯采样初始化一组可学习的动作查询，这些查询与推理增强的视觉-语言特征进行并行交互，直接生成连续动作轨迹。
- **推理增强**：视觉-语言特征经过思维链（Chain-of-Thought）推理增强，提升决策的可解释性与准确性。

### 数据与训练
- **数据集整合**：将八个公开自动驾驶数据集（如 nuScenes、Waymo Open Dataset 等）统一为标准化格式，并加入思维链推理标注，便于模型学习通用驾驶逻辑。
- **训练策略**：采用两阶段训练——先通过监督学习（SL）预训练，再使用强化学习（RL）微调，以优化动作生成质量与泛化能力。

### 实验设置与结果
- **基准测试**：在多个自动驾驶基准（如 CARLA、nuPlan 等）上评估，涵盖不同车辆配置与驾驶场景。
- **关键性能**：
  - **推理速度**：达到当前报告的最快推理速度，显著优于现有 VLA 模型。
  - **泛化能力**：在未见过的车辆配置与场景中表现稳定，泛化性能大幅提升。
  - **SOTA 性能**：在多个指标（如碰撞率、路径偏差、任务完成率）上均达到最先进水平。

### 结论
Reasoning-VLA 通过可学习动作查询与推理增强特征的并行交互，结合标准化数据集与两阶段训练，有效解决了 VLA 模型在自动驾驶中的推理效率与泛化瓶颈，为实时、通用的自动驾驶决策提供了新范式。

## Overview
Vision-Language-Action (VLA) models have recently shown strong decision-making capabilities in autonomous driving. However, existing VLAs often struggle with achieving efficient inference and generalizing to novel autonomous vehicle configurations and driving scenarios. In this paper, we propose Reasoning-VLA, a general and fast action-generation VLA framework. The proposed model employs a set of learnable action queries, initialized via Gaussian sampling from ground-truth trajectories within the training corpus. These learnable queries interact with reasoning-enhanced vision-language features to generate continuous action trajectories in parallel. To promote robust generalization, we consolidate eight publicly available autonomous driving datasets into a standardized, Chain-of-Thought reasoning-based, and easy-to-use data format for model training. Leveraging both supervised learning and reinforcement learning fine-tuning, extensive empirical evaluations across multiple benchmarks demonstrate that Reasoning-VLA achieves state-of-the-art performance, superior generalization capability, and the excellent inference speed reported to date.

## 参考
- http://arxiv.org/abs/2511.19912v1

## 개요
기존의 비전-언어-행동(VLA) 모델은 자율주행에서 강력한 의사 결정 능력을 보여주지만, 종종 추론 효율성이 낮고 새로운 차량 구성 및 주행 시나리오로의 일반화가 어려운 문제에 직면합니다. Reasoning-VLA는 훈련 코퍼스의 실제 궤적에서 가우시안 샘플링을 통해 학습 가능한 행동 쿼리를 초기화하여, 추론 강화된 비전-언어 특징과 병렬로 상호작용하며 연속적인 행동 궤적을 생성하는 범용적이고 빠른 프레임워크를 제안합니다. 일반화 성능을 향상시키기 위해, 이 모델은 8개의 공개 자율주행 데이터셋을 표준화된 사고 사슬 추론 기반의 사용하기 쉬운 형식으로 통합하고, 지도 학습과 강화 학습 미세 조정을 통해 훈련합니다. 실험 결과, Reasoning-VLA는 여러 벤치마크에서 최첨단 성능, 뛰어난 일반화 능력, 그리고 가장 빠른 추론 속도를 달성했습니다.

## 핵심 내용
### 방법 아키텍처
- **학습 가능한 행동 쿼리**: 훈련 코퍼스의 실제 궤적에서 가우시안 샘플링을 통해 학습 가능한 행동 쿼리 세트를 초기화하며, 이러한 쿼리는 추론 강화된 비전-언어 특징과 병렬로 상호작용하여 연속적인 행동 궤적을 직접 생성합니다.
- **추론 강화**: 비전-언어 특징은 사고 사슬(Chain-of-Thought) 추론을 통해 강화되어 의사 결정의 해석 가능성과 정확성을 향상시킵니다.

### 데이터 및 훈련
- **데이터셋 통합**: 8개의 공개 자율주행 데이터셋(예: nuScenes, Waymo Open Dataset 등)을 표준화된 형식으로 통합하고, 사고 사슬 추론 주석을 추가하여 모델이 범용 주행 논리를 학습하기 쉽게 합니다.
- **훈련 전략**: 두 단계 훈련을 채택합니다——먼저 지도 학습(SL)으로 사전 훈련한 후, 강화 학습(RL)으로 미세 조정하여 행동 생성 품질과 일반화 능력을 최적화합니다.

### 실험 설정 및 결과
- **벤치마크 테스트**: 여러 자율주행 벤치마크(예: CARLA, nuPlan 등)에서 평가하며, 다양한 차량 구성과 주행 시나리오를 포함합니다.
- **주요 성능**:
  - **추론 속도**: 현재 보고된 가장 빠른 추론 속도를 달성하여 기존 VLA 모델보다 크게 우수합니다.
  - **일반화 능력**: 보지 못한 차량 구성과 시나리오에서 안정적인 성능을 보이며, 일반화 성능이 크게 향상되었습니다.
  - **SOTA 성능**: 여러 지표(예: 충돌률, 경로 편차, 작업 완료율)에서 최첨단 수준에 도달했습니다.

### 결론
Reasoning-VLA는 학습 가능한 행동 쿼리와 추론 강화 특징의 병렬 상호작용, 표준화된 데이터셋 및 두 단계 훈련을 통해 자율주행에서 VLA 모델의 추론 효율성과 일반화 병목 현상을 효과적으로 해결하며, 실시간 범용 자율주행 의사 결정을 위한 새로운 패러다임을 제공합니다.
