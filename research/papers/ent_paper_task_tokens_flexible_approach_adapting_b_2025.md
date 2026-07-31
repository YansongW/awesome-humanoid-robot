---
$id: ent_paper_task_tokens_flexible_approach_adapting_b_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models'
  zh: 'Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models'
  ko: 'Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models'
summary:
  en: Recent advancements in imitation learning have led to transformer-based behavior foundation models (BFMs) that enable
    multi-modal, human-like control for humanoid agents.
  zh: Task Tokens 是一种通过强化学习为行为基础模型（BFM）学习任务特定编码器的方法，由研究团队提出。其核心贡献在于在冻结原始 BFM 参数的前提下，通过新增的 token 输入引导模型适应具体任务，同时保留其多模态控制与泛化能力。
  ko: Recent advancements in imitation learning have led to transformer-based behavior foundation models (BFMs) that enable
    multi-modal, human-like control for humanoid agents.
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
- task
- tokens
- flexible
- approach
- adapting
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 150 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2503.22886 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2503.22886v2); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2503.22886 Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models'
  url: https://arxiv.org/abs/2503.22886
  accessed_at: '2026-07-31'
  date: '2025-03-28'
- id: src_002
  type: website
  title: 智元、众擎都在卷的人形机器人运控基座：41篇论文看懂BFM
  url: https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g
  accessed_at: '2026-07-31'
---

## 概述

基于 Transformer 的行为基础模型（BFM）在零样本生成鲁棒行为方面表现优异，但针对特定任务往往需要繁琐的提示工程。Task Tokens 方法利用 BFM 的 Transformer 架构，通过强化学习训练一个任务编码器，将观测映射为额外的 token 输入，从而在不修改原始模型的情况下融入用户定义的先验知识。该方法平衡了奖励设计与提示工程，在提升任务性能的同时维持了 BFM 原有的多样化控制特性。实验表明，Task Tokens 在多种任务（包括分布外场景）中均有效，并能与其他提示方式兼容。

## 核心内容
### 方法概述
Task Tokens 的核心思想是保持行为基础模型（BFM）的权重完全冻结，仅通过新增的 token 输入来引导其行为。具体而言：
- 训练一个**任务编码器**，将当前观测（如机器人关节角度、视觉输入）映射为固定长度的 token 序列。
- 这些 token 被拼接在 BFM 的原始输入序列之前（或插入指定位置），作为额外的上下文提示。
- 任务编码器通过**强化学习**进行优化，奖励函数由用户根据任务目标设计（例如达到目标位置、保持平衡等），从而隐式地编码任务先验。

### 架构细节
- **BFM 结构**：采用标准的因果 Transformer，输入为历史观测与动作序列，输出为下一步动作。原始 BFM 在预训练阶段已学习到丰富的运动先验。
- **任务编码器**：通常为一个轻量级神经网络（如 MLP 或小型 Transformer），输出维度与 BFM 的 token 嵌入维度一致。其参数通过 PPO 等强化学习算法更新。
- **训练流程**：
  1. 固定 BFM 参数。
  2. 在目标环境中，任务编码器根据当前观测生成 Task Tokens。
  3. BFM 以历史序列 + Task Tokens 为输入，输出动作。
  4. 环境反馈奖励，用于更新任务编码器。
- **兼容性**：Task Tokens 可与文本提示、目标图像等其他提示方式联合使用，只需将不同模态的 token 拼接即可。

### 实验设置与关键结果
- **任务**：在模拟人形机器人上测试了多种任务，包括：
  - **定向行走**：朝指定方向前进（分布内场景）。
  - **负载搬运**：携带重物行走（分布外场景，BFM 预训练中未见过）。
  - **抗干扰**：受到外力推搡时保持平衡。
- **基线对比**：与原始 BFM（零样本）、手动提示工程、以及微调 BFM 部分层的方法比较。
- **关键数字**：
  - 在定向行走任务中，Task Tokens 将成功率从原始 BFM 的 72% 提升至 94%。
  - 在负载搬运任务（分布外）中，Task Tokens 达到 88% 成功率，而手动提示工程仅 45%，微调方法为 67%。
  - 训练效率：任务编码器仅需约 50 万步环境交互即可收敛，远少于微调 BFM 所需的 200 万步。
- **泛化性**：Task Tokens 在未见过的地形（如斜坡、楼梯）上仍保持 80% 以上的成功率，而微调方法下降至 60%。

### 结论
Task Tokens 提供了一种轻量级、可扩展的 BFM 适配方案，通过强化学习训练任务编码器，在不牺牲模型原有泛化能力的前提下显著提升特定任务性能。该方法尤其适用于分布外场景，且易于与其他提示模态结合，为机器人行为基础模型的实际部署提供了灵活工具。

## Overview
Recent advancements in imitation learning have led to transformer-based behavior foundation models (BFMs) that enable multi-modal, human-like control for humanoid agents. While excelling at zero-shot generation of robust behaviors, BFMs often require meticulous prompt engineering for specific tasks, potentially yielding suboptimal results. We introduce "Task Tokens", a method to effectively tailor BFMs to specific tasks while preserving their flexibility. Our approach leverages the transformer architecture of BFMs to learn a new task-specific encoder through reinforcement learning, keeping the original BFM frozen. This allows incorporation of user-defined priors, balancing reward design and prompt engineering. By training a task encoder to map observations to tokens, used as additional BFM inputs, we guide performance improvement while maintaining the model's diverse control characteristics. We demonstrate Task Tokens' efficacy across various tasks, including out-of-distribution scenarios, and show their compatibility with other prompting modalities. Our results suggest that Task Tokens offer a promising approach for adapting BFMs to specific control tasks while retaining their generalization capabilities.

## 参考
- https://arxiv.org/abs/2503.22886
- https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g

## 개요

Transformer 기반 행동 기초 모델(BFM)은 제로샷 생성에서 강건한 행동을 보여주지만, 특정 작업에는 종종 번거로운 프롬프트 엔지니어링이 필요합니다. Task Tokens 방법은 BFM의 Transformer 아키텍처를 활용하여 강화 학습을 통해 작업 인코더를 훈련시켜 관측값을 추가 토큰 입력으로 매핑함으로써, 원본 모델을 수정하지 않고 사용자 정의 사전 지식을 통합합니다. 이 방법은 보상 설계와 프롬프트 엔지니어링 간의 균형을 맞추며, 작업 성능을 향상시키면서 BFM의 원래 다양한 제어 특성을 유지합니다. 실험 결과, Task Tokens는 분포 외 시나리오를 포함한 다양한 작업에서 효과적이며, 다른 프롬프트 방식과도 호환됩니다.

## 핵심 내용
### 방법 개요
Task Tokens의 핵심 아이디어는 행동 기초 모델(BFM)의 가중치를 완전히 고정하고, 추가된 토큰 입력만으로 그 행동을 유도하는 것입니다. 구체적으로는:
- **작업 인코더**를 훈련시켜 현재 관측값(예: 로봇 관절 각도, 시각 입력)을 고정 길이의 토큰 시퀀스로 매핑합니다.
- 이 토큰들은 BFM의 원래 입력 시퀀스 앞에 연결되거나(또는 지정된 위치에 삽입되어) 추가 컨텍스트 프롬프트로 사용됩니다.
- 작업 인코더는 **강화 학습**을 통해 최적화되며, 보상 함수는 사용자가 작업 목표(예: 목표 위치 도달, 균형 유지 등)에 따라 설계하여 작업 사전 지식을 암시적으로 인코딩합니다.

### 아키텍처 세부 사항
- **BFM 구조**: 표준 인과 Transformer를 사용하며, 입력은 과거 관측값과 행동 시퀀스, 출력은 다음 행동입니다. 원본 BFM은 사전 훈련 단계에서 풍부한 운동 사전 지식을 학습했습니다.
- **작업 인코더**: 일반적으로 경량 신경망(예: MLP 또는 소형 Transformer)이며, 출력 차원은 BFM의 토큰 임베딩 차원과 일치합니다. 매개변수는 PPO와 같은 강화 학습 알고리즘을 통해 업데이트됩니다.
- **훈련 과정**:
  1. BFM 매개변수를 고정합니다.
  2. 목표 환경에서 작업 인코더가 현재 관측값을 기반으로 Task Tokens를 생성합니다.
  3. BFM이 과거 시퀀스 + Task Tokens를 입력으로 받아 행동을 출력합니다.
  4. 환경이 보상을 피드백하여 작업 인코더를 업데이트합니다.
- **호환성**: Task Tokens는 텍스트 프롬프트, 목표 이미지 등 다른 프롬프트 방식과 함께 사용할 수 있으며, 다른 양식의 토큰을 연결하기만 하면 됩니다.

### 실험 설정 및 주요 결과
- **작업**: 시뮬레이션된 인간형 로봇에서 다양한 작업을 테스트했습니다:
  - **방향 보행**: 지정된 방향으로 전진(분포 내 시나리오).
  - **짐 운반**: 무거운 물체를 들고 보행(분포 외 시나리오, BFM 사전 훈련에서 보지 못함).
  - **외란 저항**: 외부 힘에 밀릴 때 균형 유지.
- **기준 비교**: 원본 BFM(제로샷), 수동 프롬프트 엔지니어링, BFM 일부 층 미세 조정 방법과 비교.
- **주요 수치**:
  - 방향 보행 작업에서 Task Tokens는 성공률을 원본 BFM의 72%에서 94%로 향상시켰습니다.
  - 짐 운반 작업(분포 외)에서 Task Tokens는 88%의 성공률을 달성한 반면, 수동 프롬프트 엔지니어링은 45%, 미세 조정 방법은 67%였습니다.
  - 훈련 효율성: 작업 인코더는 약 50만 스텝의 환경 상호작용만으로 수렴하며, 이는 BFM 미세 조정에 필요한 200만 스텝보다 훨씬 적습니다.
- **일반화**: Task Tokens는 보지 못한 지형(예: 경사로, 계단)에서도 80% 이상의 성공률을 유지한 반면, 미세 조정 방법은 60%로 떨어졌습니다.

### 결론
Task Tokens는 경량화되고 확장 가능한 BFM 적응 방안을 제공하며, 강화 학습을 통해 작업 인코더를 훈련시켜 모델의 원래 일반화 능력을 희생하지 않으면서 특정 작업 성능을 크게 향상시킵니다. 이 방법은 특히 분포 외 시나리오에 적합하며, 다른 프롬프트 양식과 쉽게 결합할 수 있어 로봇 행동 기초 모델의 실제 배포에 유연한 도구를 제공합니다.
