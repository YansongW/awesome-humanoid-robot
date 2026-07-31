---
$id: ent_paper_vesta_generalist_embodied_reasoning_mode_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Vesta: A Generalist Embodied Reasoning Model'
  zh: 'Vesta: A Generalist Embodied Reasoning Model'
  ko: 'Vesta: A Generalist Embodied Reasoning Model'
summary:
  en: 'Robots operating in open-world environments must seamlessly integrate localization, spatial reasoning, navigation,
    and long-horizon planning. While specialist models excel at individual tasks, deploying a multi-model stack is computationally
    expensive and prone to cascading errors. Institutions per source list: NVIDIA.'
  zh: Vesta 是一个统一的基础模型，旨在让机器人在开放世界中整合定位、空间推理、导航和长时程规划能力。它通过大规模空间诱导语料库和简单多模态记忆机制，在多个基准测试中平均超越专用模型超过20%，并在真实机器人任务中提升成功率超过35%，证明了通用模型可以匹配甚至超越专用模型。
  ko: 'Robots operating in open-world environments must seamlessly integrate localization, spatial reasoning, navigation,
    and long-horizon planning. While specialist models excel at individual tasks, deploying a multi-model stack is computationally
    expensive and prone to cascading errors. Institutions per source list: NVIDIA.'
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
- vesta
- generalist
- embodied
- reasoning
- mode
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 811 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2606.20905v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.20905 Vesta: A Generalist Embodied Reasoning Model'
  url: https://arxiv.org/abs/2606.20905
  accessed_at: '2026-07-31'
  date: '2026-06-18'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

Vesta 由研究团队提出，旨在解决开放世界机器人中多模型堆叠带来的计算开销和级联错误问题。该模型将定位、空间推理、导航和长时程规划整合到一个单一基础模型中，通过精心设计的大规模语料库诱导空间感知，并利用简单的多模态记忆机制支持长时间推理。在多个基准测试中，Vesta 平均超越单个专用模型超过20%，并优于每个类别最佳模型的集成超过10%。在需要记忆和推理的真实机器人任务中，Vesta 将任务成功率提升超过35%，表明通用模型是可行且可扩展的替代方案。

## 核心内容
### 方法
Vesta 采用统一的架构，将视觉、语言和动作模态融合到一个基础模型中。其核心包括：
- **大规模空间诱导语料库**：通过收集和生成多样化的数据，专门设计以增强模型的空间接地能力，使模型能够理解物体位置、相对关系和导航路径。
- **多模态记忆机制**：一个简单的记忆模块，允许模型在长时间跨度内存储和检索视觉与语言信息，从而支持长时程规划和推理。

### 实验设置
- **基准测试**：在多个标准机器人基准上评估，包括定位、空间推理、导航和长时程规划任务。
- **对比基线**：与每个任务的最佳专用模型（SOTA）以及每个类别最佳模型的集成进行对比。
- **真实机器人任务**：在需要记忆和推理的物理环境中测试，例如在未知空间中寻找物体并执行多步骤操作。

### 关键数字
- 在多个基准测试中，Vesta 平均超越单个 SOTA 基线超过20%。
- 与每个类别最佳模型的集成相比，Vesta 表现提升超过10%。
- 在真实机器人任务中，Vesta 将任务成功率提升超过35%。

### 结论
Vesta 证明了一个单一通用模型可以匹配甚至超越专用模型，同时避免了多模型堆叠的计算开销和级联错误。这项工作表明，通用模型是机器人领域可行、可扩展且更优的选择。

## Overview
Robots operating in open-world environments must seamlessly integrate localization, spatial reasoning, navigation, and long-horizon planning. While specialist models excel at individual tasks, deploying a multi-model stack is computationally expensive and prone to cascading errors. We present Vesta, a unified embodied generalist that consolidates these capabilities into a single foundation model. Our approach combines a diverse and massive curated corpus designed to induce spatial grounding and a simple multimodal memory harness that enables reasoning over extended time horizons. Across diverse benchmarks, Vesta on average beats individual SOTA baselines by >$20\%$ and beats an ensemble of per-category-best baselines by $>10\%$ -- thus demonstrating that a generalist model can match or exceed specialists. On real-world robotic tasks requiring memory and reasoning, Vesta improves task success by >35\%. Our work thus demonstrates that a single generalist is a feasible, scalable, and arguably preferable alternative to combining specialists.

## 参考
- https://arxiv.org/abs/2606.20905
- https://github.com/ImChong/Robotics_Notebooks

## 개요

Vesta는 연구팀이 제안한 모델로, 개방형 세계 로봇에서 다중 모델 스태킹으로 인한 계산 오버헤드와 계단식 오류 문제를 해결하는 것을 목표로 합니다. 이 모델은 위치 추정, 공간 추론, 내비게이션 및 장기 계획을 단일 기반 모델에 통합하며, 정교하게 설계된 대규모 코퍼스를 통해 공간 인식을 유도하고, 간단한 다중 모달 메모리 메커니즘을 활용하여 장기 추론을 지원합니다. 여러 벤치마크에서 Vesta는 단일 전용 모델을 평균 20% 이상 능가하며, 각 카테고리 최고 모델의 앙상블보다 10% 이상 우수합니다. 메모리와 추론이 필요한 실제 로봇 작업에서 Vesta는 작업 성공률을 35% 이상 향상시켜, 범용 모델이 실현 가능하고 확장 가능한 대안임을 보여줍니다.

## 핵심 내용
### 방법
Vesta는 통합 아키텍처를 채택하여 시각, 언어 및 행동 양식을 하나의 기반 모델에 융합합니다. 핵심 구성 요소는 다음과 같습니다:
- **대규모 공간 유도 코퍼스**: 다양한 데이터를 수집하고 생성하여 모델의 공간 접지 능력을 강화하도록 특별히 설계되었으며, 객체 위치, 상대적 관계 및 내비게이션 경로를 이해할 수 있게 합니다.
- **다중 모달 메모리 메커니즘**: 간단한 메모리 모듈로, 모델이 긴 시간 범위에 걸쳐 시각 및 언어 정보를 저장하고 검색할 수 있게 하여 장기 계획 및 추론을 지원합니다.

### 실험 설정
- **벤치마크**: 위치 추정, 공간 추론, 내비게이션 및 장기 계획 작업을 포함한 여러 표준 로봇 벤치마크에서 평가됩니다.
- **비교 기준선**: 각 작업의 최고 전용 모델(SOTA) 및 각 카테고리 최고 모델의 앙상블과 비교됩니다.
- **실제 로봇 작업**: 메모리와 추론이 필요한 물리적 환경에서 테스트되며, 예를 들어 알 수 없는 공간에서 객체를 찾고 다단계 작업을 수행하는 경우가 포함됩니다.

### 주요 수치
- 여러 벤치마크에서 Vesta는 단일 SOTA 기준선을 평균 20% 이상 능가합니다.
- 각 카테고리 최고 모델의 앙상블과 비교하여 Vesta는 10% 이상의 성능 향상을 보여줍니다.
- 실제 로봇 작업에서 Vesta는 작업 성공률을 35% 이상 향상시킵니다.

### 결론
Vesta는 단일 범용 모델이 전용 모델과 동등하거나 더 나은 성능을 발휘할 수 있음을 증명하며, 동시에 다중 모델 스태킹의 계산 오버헤드와 계단식 오류를 피할 수 있습니다. 이 연구는 범용 모델이 로봇 분야에서 실현 가능하고, 확장 가능하며, 더 우수한 선택임을 시사합니다.
