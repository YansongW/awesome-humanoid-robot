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
  en: "arXiv:2607.04426v1 Announce Type: new \nAbstract: Embodied AI is moving from\
    \ isolated perception or action modules toward physical agents that understand,\
    \ plan under goals, act through robot bodies, monitor progress, and improve from\
    \ experience. Existing systems address this loop only in parts: end-to-end policies\
    \ generate actions but often lack spatial reasoning, planning, and execution assessment,\
    \ while robot-agent systems orchestrate tools or specialists but do not learn\
    \ a shared representation. This fragmentation limits general Physical Agentic\
    \ AI. We present ACE-Brain-0.5, a unified embodied foundation model that organizes\
    \ robot intelligence into five coupled functions: spatial perception, decision\
    \ making, embodied interaction, self-monitoring, and self-improvement. Built on\
    \ ACE-Brain-0, which established spatial intelligence as a shared scaffold across\
    \ robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a\
    \ closed-loop foundation model. A single 8B backbone instantiates the first four\
    \ functions: grounding objects and affordances, reasoning over 3D and egocentric\
    \ spatial relations, decomposing instructions into subgoals, generating navigation\
    \ and manipulation actions, and estimating progress for verification and recovery.\
    \ To unify these capabilities without cross-task interference, we introduce SSR+,\
    \ which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector\
    \ merging. The fifth function, self-improvement, is realized by a companion framework\
    \ that updates external execution state, including task schemas, spatial memory,\
    \ and failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5\
    \ improves over ACE-Brain-0 on 14 of 18 spatial perception and grounding benchmarks,\
    \ achieves competitive navigation and manipulation performance, and provides strong\
    \ progress estimation in ID and OOD settings. Together, these results mark an\
    \ early step toward general Physical Agentic AI."
  zh: "arXiv:2607.04426v1 Announce Type: new \nAbstract: Embodied AI is moving from\
    \ isolated perception or action modules toward physical agents that understand,\
    \ plan under goals, act through robot bodies, monitor progress, and improve from\
    \ experience. Existing systems address this loop only in parts: end-to-end policies\
    \ generate actions but often lack spatial reasoning, planning, and execution assessment,\
    \ while robot-agent systems orchestrate tools or specialists but do not learn\
    \ a shared representation. This fragmentation limits general Physical Agentic\
    \ AI. We present ACE-Brain-0.5, a unified embodied foundation model that organizes\
    \ robot intelligence into five coupled functions: spatial perception, decision\
    \ making, embodied interaction, self-monitoring, and self-improvement. Built on\
    \ ACE-Brain-0, which established spatial intelligence as a shared scaffold across\
    \ robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a\
    \ closed-loop foundation model. A single 8B backbone instantiates the first four\
    \ functions: grounding objects and affordances, reasoning over 3D and egocentric\
    \ spatial relations, decomposing instructions into subgoals, generating navigation\
    \ and manipulation actions, and estimating progress for verification and recovery.\
    \ To unify these capabilities without cross-task interference, we introduce SSR+,\
    \ which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector\
    \ merging. The fifth function, self-improvement, is realized by a companion framework\
    \ that updates external execution state, including task schemas, spatial memory,\
    \ and failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5\
    \ improves over ACE-Brain-0 on 14 of 18 spatial perception and grounding benchmarks,\
    \ achieves competitive navigation and manipulation performance, and provides strong\
    \ progress estimation in ID and OOD settings. Together, these results mark an\
    \ early step toward general Physical Agentic AI."
  ko: "arXiv:2607.04426v1 Announce Type: new \nAbstract: Embodied AI is moving from\
    \ isolated perception or action modules toward physical agents that understand,\
    \ plan under goals, act through robot bodies, monitor progress, and improve from\
    \ experience. Existing systems address this loop only in parts: end-to-end policies\
    \ generate actions but often lack spatial reasoning, planning, and execution assessment,\
    \ while robot-agent systems orchestrate tools or specialists but do not learn\
    \ a shared representation. This fragmentation limits general Physical Agentic\
    \ AI. We present ACE-Brain-0.5, a unified embodied foundation model that organizes\
    \ robot intelligence into five coupled functions: spatial perception, decision\
    \ making, embodied interaction, self-monitoring, and self-improvement. Built on\
    \ ACE-Brain-0, which established spatial intelligence as a shared scaffold across\
    \ robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a\
    \ closed-loop foundation model. A single 8B backbone instantiates the first four\
    \ functions: grounding objects and affordances, reasoning over 3D and egocentric\
    \ spatial relations, decomposing instructions into subgoals, generating navigation\
    \ and manipulation actions, and estimating progress for verification and recovery.\
    \ To unify these capabilities without cross-task interference, we introduce SSR+,\
    \ which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector\
    \ merging. The fifth function, self-improvement, is realized by a companion framework\
    \ that updates external execution state, including task schemas, spatial memory,\
    \ and failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5\
    \ improves over ACE-Brain-0 on 14 of 18 spatial perception and grounding benchmarks,\
    \ achieves competitive navigation and manipulation performance, and provides strong\
    \ progress estimation in ID and OOD settings. Together, these results mark an\
    \ early step toward general Physical Agentic AI."
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
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'ACE-Brain-0.5: A Unified Embodied Foundational Model for Physical Agentic
    AI (arXiv)'
  url: https://arxiv.org/abs/2607.04426
  date: '2026'
  accessed_at: '2026-07-08'
---

## 概述
arXiv:2607.04426v1 Announce Type: new 
Abstract: Embodied AI is moving from isolated perception or action modules toward physical agents that understand, plan under goals, act through robot bodies, monitor progress, and improve from experience. Existing systems address this loop only in parts: end-to-end policies generate actions but often lack spatial reasoning, planning, and execution assessment, while robot-agent systems orchestrate tools or specialists but do not learn a shared representation. This fragmentation limits general Physical Agentic AI. We present ACE-Brain-0.5, a unified embodied foundation model that organizes robot intelligence into five coupled functions: spatial perception, decision making, embodied interaction, self-monitoring, and self-improvement. Built on ACE-Brain-0, which established spatial intelligence as a shared scaffold across robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a closed-loop foundation model. A single 8B backbone instantiates the first four functions: grounding objects and affordances, reasoning over 3D and egocentric spatial relations, decomposing instructions into subgoals, generating navigation and manipulation actions, and estimating progress for verification and recovery. To unify these capabilities without cross-task interference, we introduce SSR+, which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector merging. The fifth function, self-improvement, is realized by a companion framework that updates external execution state, including task schemas, spatial memory, and failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5 improves over ACE-Brain-0 on 14 of 18 spatial perception and grounding benchmarks, achieves competitive navigation and manipulation performance, and provides strong progress estimation in ID and OOD settings. Together, these results mark an early step toward general Physical Agentic AI.

## Overview
arXiv:2607.04426v1 Announce Type: new 
Abstract: Embodied AI is moving from isolated perception or action modules toward physical agents that understand, plan under goals, act through robot bodies, monitor progress, and improve from experience. Existing systems address this loop only in parts: end-to-end policies generate actions but often lack spatial reasoning, planning, and execution assessment, while robot-agent systems orchestrate tools or specialists but do not learn a shared representation. This fragmentation limits general Physical Agentic AI. We present ACE-Brain-0.5, a unified embodied foundation model that organizes robot intelligence into five coupled functions: spatial perception, decision making, embodied interaction, self-monitoring, and self-improvement. Built on ACE-Brain-0, which established spatial intelligence as a shared scaffold across robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a closed-loop foundation model. A single 8B backbone instantiates the first four functions: grounding objects and affordances, reasoning over 3D and egocentric spatial relations, decomposing instructions into subgoals, generating navigation and manipulation actions, and estimating progress for verification and recovery. To unify these capabilities without cross-task interference, we introduce SSR+, which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector merging. The fifth function, self-improvement, is realized by a companion framework that updates external execution state, including task schemas, spatial memory, and failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5 improves over ACE-Brain-0 on 14 of 18 spatial perception and grounding benchmarks, achieves competitive navigation and manipulation performance, and provides strong progress estimation in ID and OOD settings. Together, these results mark an early step toward general Physical Agentic AI.

## 개요
arXiv:2607.04426v1 Announce Type: new 
Abstract: Embodied AI is moving from isolated perception or action modules toward physical agents that understand, plan under goals, act through robot bodies, monitor progress, and improve from experience. Existing systems address this loop only in parts: end-to-end policies generate actions but often lack spatial reasoning, planning, and execution assessment, while robot-agent systems orchestrate tools or specialists but do not learn a shared representation. This fragmentation limits general Physical Agentic AI. We present ACE-Brain-0.5, a unified embodied foundation model that organizes robot intelligence into five coupled functions: spatial perception, decision making, embodied interaction, self-monitoring, and self-improvement. Built on ACE-Brain-0, which established spatial intelligence as a shared scaffold across robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a closed-loop foundation model. A single 8B backbone instantiates the first four functions: grounding objects and affordances, reasoning over 3D and egocentric spatial relations, decomposing instructions into subgoals, generating navigation and manipulation actions, and estimating progress for verification and recovery. To unify these capabilities without cross-task interference, we introduce SSR+, which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector merging. The fifth function, self-improvement, is realized by a companion framework that updates external execution state, including task schemas, spatial memory, and failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5 improves over ACE-Brain-0 on 14 of 18 spatial perception and grounding benchmarks, achieves competitive navigation and manipulation performance, and provides strong progress estimation in ID and OOD settings. Together, these results mark an early step toward general Physical Agentic AI.
