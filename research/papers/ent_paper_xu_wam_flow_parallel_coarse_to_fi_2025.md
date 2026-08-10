---
$id: ent_paper_xu_wam_flow_parallel_coarse_to_fi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving'
  zh: WAM-Flow
  ko: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving'
summary:
  en: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving (WAM-Flow), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Fudan University, Yinwang Intelligent
    Technology Co., Ltd..'
  zh: WAM-Flow 是复旦大学与引望智能技术有限公司于 2025 年提出的大型视觉-语言-动作模型，用于机器人操控。其核心贡献在于将自车轨迹规划转化为离散流匹配问题，通过完全并行的双向去噪实现从粗到细的规划，并支持可调节的计算-精度权衡。
  ko: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving (WAM-Flow), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Fudan University, Yinwang Intelligent
    Technology Co., Ltd..'
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
- vision_language_action
- vla
- wam_flow
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.06112v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (710 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2512.06112
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: WAM-Flow source
  url: https://doi.org/10.48550/arXiv.2512.06112
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
WAM-Flow 摒弃了传统的自回归解码方式，采用离散流匹配在结构化 token 空间中进行并行双向去噪，从而实现从粗到细的轨迹优化。该方法包含三个关键组件：一个通过三元组边缘学习保持标量几何结构的度量对齐数值分词器、一个几何感知的流目标函数，以及一个结合安全、自车进度和舒适度奖励的模拟器引导 GRPO 对齐。通过多阶段适配，WAM-Flow 将预训练的自回归骨干网络 Janus-1.5B 从因果解码转换为非因果流模型，并通过持续的多模态预训练增强道路场景理解能力。

## 核心内容
### 方法架构
- **离散流匹配**：将轨迹规划建模为在结构化 token 空间上的离散流匹配过程，实现完全并行的双向去噪。
- **度量对齐数值分词器**：通过三元组边缘学习保留标量几何结构，确保数值表示的准确性。
- **几何感知流目标**：设计专门的目标函数以感知轨迹的几何特性。
- **模拟器引导 GRPO 对齐**：整合安全、自车进度和舒适度奖励，同时保持并行生成能力。

### 多阶段适配
- 将预训练的自回归骨干网络 Janus-1.5B 从因果解码转换为非因果流模型。
- 通过持续的多模态预训练增强道路场景理解能力。

### 实验设置与结果
- **基准测试**：在 NAVSIM v1 基准上进行评估。
- **关键性能指标**：
  - 1 步推理达到 89.1 PDMS。
  - 5 步推理达到 90.3 PDMS。
- **对比基线**：在闭环性能上优于自回归和基于扩散的 VLA 基线模型。

### 结论
离散流匹配被证明是端到端自动驾驶中一种有前景的新范式，代码将很快公开。

## Overview
We introduce WAM-Flow, a vision-language-action (VLA) model that casts ego-trajectory planning as discrete flow matching over a structured token space. In contrast to autoregressive decoders, WAM-Flow performs fully parallel, bidirectional denoising, enabling coarse-to-fine refinement with a tunable compute-accuracy trade-off. Specifically, the approach combines a metric-aligned numerical tokenizer that preserves scalar geometry via triplet-margin learning, a geometry-aware flow objective and a simulator-guided GRPO alignment that integrates safety, ego progress, and comfort rewards while retaining parallel generation. A multi-stage adaptation converts a pre-trained auto-regressive backbone (Janus-1.5B) from causal decoding to non-causal flow model and strengthens road-scene competence through continued multimodal pretraining. Thanks to the inherent nature of consistency model training and parallel decoding inference, WAM-Flow achieves superior closed-loop performance against autoregressive and diffusion-based VLA baselines, with 1-step inference attaining 89.1 PDMS and 5-step inference reaching 90.3 PDMS on NAVSIM v1 benchmark. These results establish discrete flow matching as a new promising paradigm for end-to-end autonomous driving. The code will be publicly available soon.

## 参考
- http://arxiv.org/abs/2512.06112v2

## 개요
WAM-Flow는 전통적인 자기회귀 디코딩 방식을 버리고, 구조화된 토큰 공간에서 이산 흐름 매칭을 통해 병렬 양방향 디노이징을 수행하여, 조대한 것에서 세밀한 것으로의 궤적 최적화를 실현합니다. 이 방법은 세 가지 핵심 구성 요소를 포함합니다: 삼중항 엣지 학습을 통해 스칼라 기하 구조를 유지하는 메트릭 정렬 수치 토크나이저, 기하 인식 흐름 목적 함수, 그리고 안전, 자차 진행도 및 편안함 보상을 결합한 시뮬레이터 유도 GRPO 정렬입니다. 다단계 적응을 통해 WAM-Flow는 사전 훈련된 자기회귀 백본 네트워크 Janus-1.5B를 인과 디코딩에서 비인과 흐름 모델로 변환하고, 지속적인 다중 모달 사전 훈련을 통해 도로 장면 이해 능력을 강화합니다.

## 핵심 내용
### 방법 아키텍처
- **이산 흐름 매칭**: 궤적 계획을 구조화된 토큰 공간에서의 이산 흐름 매칭 과정으로 모델링하여 완전히 병렬적인 양방향 디노이징을 실현합니다.
- **메트릭 정렬 수치 토크나이저**: 삼중항 엣지 학습을 통해 스칼라 기하 구조를 보존하여 수치 표현의 정확성을 보장합니다.
- **기하 인식 흐름 목적 함수**: 궤적의 기하 특성을 인식하도록 설계된 전용 목적 함수를 구성합니다.
- **시뮬레이터 유도 GRPO 정렬**: 안전, 자차 진행도 및 편안함 보상을 통합하면서 병렬 생성 능력을 유지합니다.

### 다단계 적응
- 사전 훈련된 자기회귀 백본 네트워크 Janus-1.5B를 인과 디코딩에서 비인과 흐름 모델로 변환합니다.
- 지속적인 다중 모달 사전 훈련을 통해 도로 장면 이해 능력을 강화합니다.

### 실험 설정 및 결과
- **벤치마크**: NAVSIM v1 벤치마크에서 평가를 수행합니다.
- **주요 성능 지표**:
  - 1단계 추론에서 89.1 PDMS 달성.
  - 5단계 추론에서 90.3 PDMS 달성.
- **비교 기준선**: 폐루프 성능에서 자기회귀 및 확산 기반 VLA 기준 모델보다 우수합니다.

### 결론
이산 흐름 매칭은 엔드투엔드 자율주행에서 유망한 새로운 패러다임으로 입증되었으며, 코드는 곧 공개될 예정입니다.
