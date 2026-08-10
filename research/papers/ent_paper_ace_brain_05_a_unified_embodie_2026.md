---
$id: ent_paper_ace_brain_05_a_unified_embodie_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ACE-Brain-0.5: A Unified Embodied Foundational Model for Physical Agentic AI'
  zh: 'ACE-Brain-0.5: A Unified Embodied Foundational Model for Physical Agentic AI'
  ko: 'ACE-Brain-0.5: A Unified Embodied Foundational Model for Physical Agentic AI'
summary:
  en: 'arXiv:2607.04426v1 Announce Type: new Abstract: Embodied AI is moving from isolated perception or action modules toward
    physical agents that understand, plan under goals, act through robot bodies, monitor progress, and improve from experience.
    Existing systems address this loop only in parts: end-to-end policies generate actions but often lack spatial reasoning,
    planning, and execution assessment, while robot-agent systems orchestrate tools or specialists but do not learn a shared
    representation. This fragmentation limits general Physical Agentic AI. We present ACE-Brain-0.5, a unified embodied foundation
    model that organizes robot intelligence into five coupled functions: spatial perception, decision making, embodied interaction,
    self-monitoring, and self-improvement. Built on ACE-Brain-0, which established spatial intelligence as a shared scaffold
    across robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a closed-loop foundation model. A single
    8B backbone instantiates the first four functions: grounding objects and affordances, reasoning over 3D and egocentric
    spatial relations, decomposing instructions into subgoals, generating navigation and manipulation actions, and estimating
    progress for verification and recovery. To unify these capabilities without cross-task interference, we introduce SSR+,
    which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector merging. The fifth function, self-improvement,
    is realized by a companion framework that updates external execution state, including task schemas, spatial memory, and
    failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5 improves over ACE-Brain-0 on 14 of 18
    spatial perception and grounding benchmarks, achieves competitive navigation and manipulation performance, and provides
    strong progress estimation in ID and OOD settings. Together, these results mark an early step toward general Physical
    Agentic AI.'
  zh: ACE-Brain-0.5 是一个统一的具身基础模型，由研究团队提出，旨在将机器人智能组织为空间感知、决策、交互、自我监控和自我改进五个耦合功能。它基于 ACE-Brain-0 构建，采用单个 8B 参数骨干网络，并通过 SSR+
    方法实现多任务统一，在 15 个基准测试中展现出显著性能提升。
  ko: 'arXiv:2607.04426v1 Announce Type: new Abstract: Embodied AI is moving from isolated perception or action modules toward
    physical agents that understand, plan under goals, act through robot bodies, monitor progress, and improve from experience.
    Existing systems address this loop only in parts: end-to-end policies generate actions but often lack spatial reasoning,
    planning, and execution assessment, while robot-agent systems orchestrate tools or specialists but do not learn a shared
    representation. This fragmentation limits general Physical Agentic AI. We present ACE-Brain-0.5, a unified embodied foundation
    model that organizes robot intelligence into five coupled functions: spatial perception, decision making, embodied interaction,
    self-monitoring, and self-improvement. Built on ACE-Brain-0, which established spatial intelligence as a shared scaffold
    across robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a closed-loop foundation model. A single
    8B backbone instantiates the first four functions: grounding objects and affordances, reasoning over 3D and egocentric
    spatial relations, decomposing instructions into subgoals, generating navigation and manipulation actions, and estimating
    progress for verification and recovery. To unify these capabilities without cross-task interference, we introduce SSR+,
    which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector merging. The fifth function, self-improvement,
    is realized by a companion framework that updates external execution state, including task schemas, spatial memory, and
    failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5 improves over ACE-Brain-0 on 14 of 18
    spatial perception and grounding benchmarks, achieves competitive navigation and manipulation performance, and provides
    strong progress estimation in ID and OOD settings. Together, these results mark an early step toward general Physical
    Agentic AI.'
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
- ace_brain_05
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04426v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1022 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ACE-Brain-0.5: A Unified Embodied Foundational Model for Physical Agentic AI (arXiv)'
  url: https://arxiv.org/abs/2607.04426
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
ACE-Brain-0.5 将机器人智能整合为五个耦合功能：空间感知、决策、具身交互、自我监控和自我改进。该模型基于 ACE-Brain-0 的空间智能框架，通过单个 8B 参数骨干网络实现前四个功能，包括物体与可供性定位、3D 与自我中心空间关系推理、指令分解为子目标、导航与操作动作生成，以及进度估计用于验证与恢复。为消除跨任务干扰，研究团队引入 SSR+ 方法，在任务向量合并后增加 Reactivate 阶段。第五个功能自我改进通过一个配套框架实现，该框架从 rollout 中更新外部执行状态，包括任务模式、空间记忆和失败恢复案例。在 15 个基准测试中，ACE-Brain-0.5 在 18 个空间感知与定位基准中的 14 个上超越 ACE-Brain-0，在导航与操作任务上表现竞争力，并在分布内和分布外场景中提供强大的进度估计能力。

## 核心内容
### 核心架构
ACE-Brain-0.5 构建于 ACE-Brain-0 之上，后者建立了跨机器人平台的空间智能共享框架。该模型将具身智能组织为五个耦合功能：
- **空间感知**：物体与可供性定位，3D 与自我中心空间关系推理
- **决策**：将指令分解为子目标
- **具身交互**：生成导航与操作动作
- **自我监控**：进度估计用于验证与恢复
- **自我改进**：通过配套框架更新外部执行状态

### 关键技术
- **SSR+ 方法**：在 Scaffold-Specialize-Reconcile 基础上，于任务向量合并后增加 Reactivate 阶段，实现多任务统一且避免跨任务干扰
- **单骨干网络**：单个 8B 参数模型实例化前四个功能
- **自我改进框架**：从 rollout 中更新任务模式、空间记忆和失败恢复案例

### 实验设置与结果
- **基准测试**：在 15 个基准上评估，涵盖空间感知、定位、导航和操作
- **空间感知与定位**：在 18 个基准中的 14 个上超越 ACE-Brain-0
- **导航与操作**：达到竞争力水平
- **进度估计**：在分布内（ID）和分布外（OOD）场景中均表现强劲

### 结论
ACE-Brain-0.5 标志着向通用 Physical Agentic AI 迈出的早期一步，通过统一框架整合了具身智能的关键功能，并展示了在多任务场景下的有效性与泛化能力。

## Overview
Embodied AI is moving from isolated perception or action modules toward physical agents that understand, plan under goals, act through robot bodies, monitor progress, and improve from experience. Existing systems address this loop only in parts: end-to-end policies generate actions but often lack spatial reasoning, planning, and execution assessment, while robot-agent systems orchestrate tools or specialists but do not learn a shared representation. This fragmentation limits general Physical Agentic AI. We present ACE-Brain-0.5, a unified embodied foundation model that organizes robot intelligence into five coupled functions: spatial perception, decision making, embodied interaction, self-monitoring, and self-improvement. Built on ACE-Brain-0, which established spatial intelligence as a shared scaffold across robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a closed-loop foundation model. A single 8B backbone instantiates the first four functions: grounding objects and affordances, reasoning over 3D and egocentric spatial relations, decomposing instructions into subgoals, generating navigation and manipulation actions, and estimating progress for verification and recovery. To unify these capabilities without cross-task interference, we introduce SSR+, which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector merging. The fifth function, self-improvement, is realized by a companion framework that updates external execution state, including task schemas, spatial memory, and failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5 improves over ACE-Brain-0 on 14 of 18 spatial perception and grounding benchmarks, achieves competitive navigation and manipulation performance, and provides strong progress estimation in ID and OOD settings. Together, these results mark an early step toward general Physical Agentic AI.

## 参考
- http://arxiv.org/abs/2607.04426v1

## 개요
ACE-Brain-0.5는 로봇 지능을 다섯 가지 결합 기능으로 통합합니다: 공간 인식, 의사 결정, 구현 상호작용, 자기 모니터링, 자기 개선. 이 모델은 ACE-Brain-0의 공간 지능 프레임워크를 기반으로, 단일 8B 파라미터 백본 네트워크를 통해 처음 네 가지 기능을 구현하며, 객체 및 사용 가능성 위치 파악, 3D 및 자기 중심 공간 관계 추론, 지침을 하위 목표로 분해, 내비게이션 및 조작 동작 생성, 검증 및 복구를 위한 진행률 추정을 포함합니다. 교차 작업 간섭을 제거하기 위해 연구팀은 SSR+ 방법을 도입하여, 작업 벡터 병합 후 Reactivate 단계를 추가합니다. 다섯 번째 기능인 자기 개선은 rollout에서 외부 실행 상태(작업 패턴, 공간 메모리, 실패 복구 사례 포함)를 업데이트하는 보조 프레임워크를 통해 구현됩니다. 15개 벤치마크에서 ACE-Brain-0.5는 18개 공간 인식 및 위치 파악 벤치마크 중 14개에서 ACE-Brain-0을 능가하며, 내비게이션 및 조작 작업에서 경쟁력 있는 성능을 보이고, 분포 내 및 분포 외 시나리오에서 강력한 진행률 추정 능력을 제공합니다.

## 핵심 내용
### 핵심 아키텍처
ACE-Brain-0.5는 로봇 플랫폼 전반에 걸친 공간 지능 공유 프레임워크를 구축한 ACE-Brain-0 위에 구축되었습니다. 이 모델은 구현 지능을 다섯 가지 결합 기능으로 구성합니다:
- **공간 인식**: 객체 및 사용 가능성 위치 파악, 3D 및 자기 중심 공간 관계 추론
- **의사 결정**: 지침을 하위 목표로 분해
- **구현 상호작용**: 내비게이션 및 조작 동작 생성
- **자기 모니터링**: 검증 및 복구를 위한 진행률 추정
- **자기 개선**: 보조 프레임워크를 통한 외부 실행 상태 업데이트

### 핵심 기술
- **SSR+ 방법**: Scaffold-Specialize-Reconcile 기반으로, 작업 벡터 병합 후 Reactivate 단계를 추가하여 다중 작업 통합을 달성하고 교차 작업 간섭을 방지
- **단일 백본 네트워크**: 단일 8B 파라미터 모델이 처음 네 가지 기능을 구현
- **자기 개선 프레임워크**: rollout에서 작업 패턴, 공간 메모리, 실패 복구 사례를 업데이트

### 실험 설정 및 결과
- **벤치마크 테스트**: 15개 벤치마크에서 평가, 공간 인식, 위치 파악, 내비게이션, 조작 포함
- **공간 인식 및 위치 파악**: 18개 벤치마크 중 14개에서 ACE-Brain-0을 능가
- **내비게이션 및 조작**: 경쟁력 있는 수준 달성
- **진행률 추정**: 분포 내(ID) 및 분포 외(OOD) 시나리오 모두에서 강력한 성능

### 결론
ACE-Brain-0.5는 일반적인 Physical Agentic AI를 향한 초기 단계를 나타내며, 통합 프레임워크를 통해 구현 지능의 핵심 기능을 통합하고 다중 작업 시나리오에서의 효과성과 일반화 능력을 입증합니다.
