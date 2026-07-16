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
  zh: 'arXiv:2607.04426v1 Announce Type: new Abstract: Embodied AI is moving from isolated perception or action modules toward
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04426v1.
sources:
- id: src_001
  type: paper
  title: 'ACE-Brain-0.5: A Unified Embodied Foundational Model for Physical Agentic AI (arXiv)'
  url: https://arxiv.org/abs/2607.04426
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Embodied AI is moving from isolated perception or action modules toward physical agents that understand, plan under goals, act through robot bodies, monitor progress, and improve from experience. Existing systems address this loop only in parts: end-to-end policies generate actions but often lack spatial reasoning, planning, and execution assessment, while robot-agent systems orchestrate tools or specialists but do not learn a shared representation. This fragmentation limits general Physical Agentic AI. We present ACE-Brain-0.5, a unified embodied foundation model that organizes robot intelligence into five coupled functions: spatial perception, decision making, embodied interaction, self-monitoring, and self-improvement. Built on ACE-Brain-0, which established spatial intelligence as a shared scaffold across robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a closed-loop foundation model. A single 8B backbone instantiates the first four functions: grounding objects and affordances, reasoning over 3D and egocentric spatial relations, decomposing instructions into subgoals, generating navigation and manipulation actions, and estimating progress for verification and recovery. To unify these capabilities without cross-task interference, we introduce SSR+, which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector merging. The fifth function, self-improvement, is realized by a companion framework that updates external execution state, including task schemas, spatial memory, and failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5 improves over ACE-Brain-0 on 14 of 18 spatial perception and grounding benchmarks, achieves competitive navigation and manipulation performance, and provides strong progress estimation in ID and OOD settings. Together, these results mark an early step toward general Physical Agentic AI.

## 核心内容
Embodied AI is moving from isolated perception or action modules toward physical agents that understand, plan under goals, act through robot bodies, monitor progress, and improve from experience. Existing systems address this loop only in parts: end-to-end policies generate actions but often lack spatial reasoning, planning, and execution assessment, while robot-agent systems orchestrate tools or specialists but do not learn a shared representation. This fragmentation limits general Physical Agentic AI. We present ACE-Brain-0.5, a unified embodied foundation model that organizes robot intelligence into five coupled functions: spatial perception, decision making, embodied interaction, self-monitoring, and self-improvement. Built on ACE-Brain-0, which established spatial intelligence as a shared scaffold across robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a closed-loop foundation model. A single 8B backbone instantiates the first four functions: grounding objects and affordances, reasoning over 3D and egocentric spatial relations, decomposing instructions into subgoals, generating navigation and manipulation actions, and estimating progress for verification and recovery. To unify these capabilities without cross-task interference, we introduce SSR+, which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector merging. The fifth function, self-improvement, is realized by a companion framework that updates external execution state, including task schemas, spatial memory, and failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5 improves over ACE-Brain-0 on 14 of 18 spatial perception and grounding benchmarks, achieves competitive navigation and manipulation performance, and provides strong progress estimation in ID and OOD settings. Together, these results mark an early step toward general Physical Agentic AI.

## 参考
- http://arxiv.org/abs/2607.04426v1

## Overview
Embodied AI is moving from isolated perception or action modules toward physical agents that understand, plan under goals, act through robot bodies, monitor progress, and improve from experience. Existing systems address this loop only in parts: end-to-end policies generate actions but often lack spatial reasoning, planning, and execution assessment, while robot-agent systems orchestrate tools or specialists but do not learn a shared representation. This fragmentation limits general Physical Agentic AI. We present ACE-Brain-0.5, a unified embodied foundation model that organizes robot intelligence into five coupled functions: spatial perception, decision making, embodied interaction, self-monitoring, and self-improvement. Built on ACE-Brain-0, which established spatial intelligence as a shared scaffold across robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a closed-loop foundation model. A single 8B backbone instantiates the first four functions: grounding objects and affordances, reasoning over 3D and egocentric spatial relations, decomposing instructions into subgoals, generating navigation and manipulation actions, and estimating progress for verification and recovery. To unify these capabilities without cross-task interference, we introduce SSR+, which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector merging. The fifth function, self-improvement, is realized by a companion framework that updates external execution state, including task schemas, spatial memory, and failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5 improves over ACE-Brain-0 on 14 of 18 spatial perception and grounding benchmarks, achieves competitive navigation and manipulation performance, and provides strong progress estimation in ID and OOD settings. Together, these results mark an early step toward general Physical Agentic AI.

## Content
Embodied AI is moving from isolated perception or action modules toward physical agents that understand, plan under goals, act through robot bodies, monitor progress, and improve from experience. Existing systems address this loop only in parts: end-to-end policies generate actions but often lack spatial reasoning, planning, and execution assessment, while robot-agent systems orchestrate tools or specialists but do not learn a shared representation. This fragmentation limits general Physical Agentic AI. We present ACE-Brain-0.5, a unified embodied foundation model that organizes robot intelligence into five coupled functions: spatial perception, decision making, embodied interaction, self-monitoring, and self-improvement. Built on ACE-Brain-0, which established spatial intelligence as a shared scaffold across robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a closed-loop foundation model. A single 8B backbone instantiates the first four functions: grounding objects and affordances, reasoning over 3D and egocentric spatial relations, decomposing instructions into subgoals, generating navigation and manipulation actions, and estimating progress for verification and recovery. To unify these capabilities without cross-task interference, we introduce SSR+, which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector merging. The fifth function, self-improvement, is realized by a companion framework that updates external execution state, including task schemas, spatial memory, and failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5 improves over ACE-Brain-0 on 14 of 18 spatial perception and grounding benchmarks, achieves competitive navigation and manipulation performance, and provides strong progress estimation in ID and OOD settings. Together, these results mark an early step toward general Physical Agentic AI.

## 개요
Embodied AI는 고립된 인식 또는 행동 모듈에서 물리적 에이전트로 진화하고 있습니다. 이 에이전트는 이해하고, 목표에 따라 계획하며, 로봇 신체를 통해 행동하고, 진행 상황을 모니터링하며, 경험을 통해 개선합니다. 기존 시스템은 이 순환 과정의 일부만을 다룹니다. 종단 간 정책은 행동을 생성하지만 공간 추론, 계획 및 실행 평가가 부족한 경우가 많고, 로봇-에이전트 시스템은 도구나 전문가를 조정하지만 공유 표현을 학습하지 못합니다. 이러한 단편화는 일반적인 물리적 에이전트 AI를 제한합니다. 우리는 ACE-Brain-0.5를 제시합니다. 이는 로봇 지능을 다섯 가지 결합된 기능(공간 인식, 의사 결정, 구현된 상호작용, 자기 모니터링, 자기 개선)으로 구성하는 통합된 구현 기반 모델입니다. ACE-Brain-0(로봇 플랫폼 전반에 걸쳐 공유된 스캐폴드로 공간 지능을 확립)을 기반으로 구축된 ACE-Brain-0.5는 이해 중심 모델을 폐루프 기반 모델로 확장합니다. 단일 8B 백본은 처음 네 가지 기능을 구현합니다: 객체와 어포던스 접지, 3D 및 자기 중심 공간 관계 추론, 명령을 하위 목표로 분해, 탐색 및 조작 행동 생성, 검증 및 복구를 위한 진행 상황 추정. 이러한 기능을 교차 작업 간섭 없이 통합하기 위해 우리는 SSR+를 도입합니다. 이는 작업 벡터 병합 후 Reactivate 단계로 Scaffold-Specialize-Reconcile을 확장합니다. 다섯 번째 기능인 자기 개선은 롤아웃에서 작업 스키마, 공간 메모리, 실패 복구 사례를 포함한 외부 실행 상태를 업데이트하는 동반 프레임워크에 의해 실현됩니다. 15개의 벤치마크에서 ACE-Brain-0.5는 18개의 공간 인식 및 접지 벤치마크 중 14개에서 ACE-Brain-0보다 개선되었으며, 경쟁력 있는 탐색 및 조작 성능을 달성하고, ID 및 OOD 설정에서 강력한 진행 상황 추정을 제공합니다. 이러한 결과는 함께 일반적인 물리적 에이전트 AI를 향한 초기 단계를 나타냅니다.

## 핵심 내용
Embodied AI는 고립된 인식 또는 행동 모듈에서 물리적 에이전트로 진화하고 있습니다. 이 에이전트는 이해하고, 목표에 따라 계획하며, 로봇 신체를 통해 행동하고, 진행 상황을 모니터링하며, 경험을 통해 개선합니다. 기존 시스템은 이 순환 과정의 일부만을 다룹니다. 종단 간 정책은 행동을 생성하지만 공간 추론, 계획 및 실행 평가가 부족한 경우가 많고, 로봇-에이전트 시스템은 도구나 전문가를 조정하지만 공유 표현을 학습하지 못합니다. 이러한 단편화는 일반적인 물리적 에이전트 AI를 제한합니다. 우리는 ACE-Brain-0.5를 제시합니다. 이는 로봇 지능을 다섯 가지 결합된 기능(공간 인식, 의사 결정, 구현된 상호작용, 자기 모니터링, 자기 개선)으로 구성하는 통합된 구현 기반 모델입니다. ACE-Brain-0(로봇 플랫폼 전반에 걸쳐 공유된 스캐폴드로 공간 지능을 확립)을 기반으로 구축된 ACE-Brain-0.5는 이해 중심 모델을 폐루프 기반 모델로 확장합니다. 단일 8B 백본은 처음 네 가지 기능을 구현합니다: 객체와 어포던스 접지, 3D 및 자기 중심 공간 관계 추론, 명령을 하위 목표로 분해, 탐색 및 조작 행동 생성, 검증 및 복구를 위한 진행 상황 추정. 이러한 기능을 교차 작업 간섭 없이 통합하기 위해 우리는 SSR+를 도입합니다. 이는 작업 벡터 병합 후 Reactivate 단계로 Scaffold-Specialize-Reconcile을 확장합니다. 다섯 번째 기능인 자기 개선은 롤아웃에서 작업 스키마, 공간 메모리, 실패 복구 사례를 포함한 외부 실행 상태를 업데이트하는 동반 프레임워크에 의해 실현됩니다. 15개의 벤치마크에서 ACE-Brain-0.5는 18개의 공간 인식 및 접지 벤치마크 중 14개에서 ACE-Brain-0보다 개선되었으며, 경쟁력 있는 탐색 및 조작 성능을 달성하고, ID 및 OOD 설정에서 강력한 진행 상황 추정을 제공합니다. 이러한 결과는 함께 일반적인 물리적 에이전트 AI를 향한 초기 단계를 나타냅니다.
