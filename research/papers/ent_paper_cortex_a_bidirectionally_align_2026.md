---
$id: ent_paper_cortex_a_bidirectionally_align_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation'
  zh: 'Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation'
  ko: 'Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation'
summary:
  en: 'arXiv:2607.05377v1 Announce Type: new Abstract: While recent Vision-Language-Action (VLA) models show promise toward
    generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on
    current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning
    semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework
    with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level
    VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles,
    such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This
    enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data.
    We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better
    handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts
    to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex''s efficacy,
    e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex''s generalist VLM
    enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply
    combining with a fine-tuned VLA-a capability infeasible through VLA fine-tuning alone.'
  zh: 'arXiv:2607.05377v1 Announce Type: new Abstract: While recent Vision-Language-Action (VLA) models show promise toward
    generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on
    current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning
    semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework
    with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level
    VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles,
    such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This
    enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data.
    We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better
    handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts
    to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex''s efficacy,
    e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex''s generalist VLM
    enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply
    combining with a fine-tuned VLA-a capability infeasible through VLA fine-tuning alone.'
  ko: 'arXiv:2607.05377v1 Announce Type: new Abstract: While recent Vision-Language-Action (VLA) models show promise toward
    generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on
    current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning
    semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework
    with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level
    VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles,
    such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This
    enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data.
    We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better
    handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts
    to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex''s efficacy,
    e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex''s generalist VLM
    enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply
    combining with a fine-tuned VLA-a capability infeasible through VLA fine-tuning alone.'
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
- cortex
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.05377v1.
sources:
- id: src_001
  type: paper
  title: 'Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.05377
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles, such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data. We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy, e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply combining with a fine-tuned VLA-a capability infeasible through VLA fine-tuning alone.

## 核心内容
While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles, such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data. We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy, e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply combining with a fine-tuned VLA-a capability infeasible through VLA fine-tuning alone.

## 参考
- http://arxiv.org/abs/2607.05377v1

## Overview
While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature—relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles, such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data. We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy, e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply combining with a fine-tuned VLA—a capability infeasible through VLA fine-tuning alone.

## Content
While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature—relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles, such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data. We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy, e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply combining with a fine-tuned VLA—a capability infeasible through VLA fine-tuning alone.

## 개요
최근 Vision-Language-Action(VLA) 모델은 범용 조작 정책에 대한 가능성을 보여주지만, 마르코프 특성(현재 관찰에만 의존)으로 인해 장기적 과제에서 어려움을 겪습니다. 계층적 이중 시스템 방법은 이를 해결하지만, 고수준 계획 의미론과 저수준 실행 운동학 사이의 격차로 인해 어려움을 겪습니다. 우리는 Cortex를 소개합니다. 이는 고수준 VLM에서 저수준 VLA로 실행 가능하고 다루기 쉬운 하위 작업 계획을 전달하는 맞춤형 계획 인터페이스를 갖춘 양방향 정렬된 임베디드 에이전트 프레임워크입니다. 구체적으로, 조작 하위 작업을 32개의 표준 기술 프리미티브로 표준화하고, 대표 객체 속성 및 개선된 궤적 도달 가능성과 같은 다루기 쉬운 원칙을 데이터 생성 파이프라인에 주입합니다. 이를 통해 4,000시간 이상의 오픈소스 비디오 데이터를 자동으로 주석 처리하고 30시간의 시뮬레이션 데이터를 생성할 수 있습니다. 또한, 하위 작업 전환 중 계획 모호성을 더 잘 처리하기 위해 프레임워크를 미세 조정하기 위한 훈련 데이터를 구성하는 이벤트 균형 샘플링 전략을 고안하며, 추론 중 작업 컨텍스트에서 기술 제약까지 신중하게 설계된 하네스 엔지니어링으로 강화됩니다. 개방 루프 VLM 및 폐쇄 루프 시스템 평가 모두 Cortex의 효능을 입증합니다. 예를 들어, Libero-long에서 3.1%, RoboTwin에서 4.1%의 성능 향상을 보여줍니다. 특히, Cortex의 범용 VLM은 미세 조정된 VLA와 단순히 결합하여 다단계 화학 실험과 같은 보지 못한 실제 장기적 과제를 제로샷으로 완료할 수 있게 합니다. 이는 VLA 미세 조정만으로는 불가능한 능력입니다.

## 핵심 내용
최근 Vision-Language-Action(VLA) 모델은 범용 조작 정책에 대한 가능성을 보여주지만, 마르코프 특성(현재 관찰에만 의존)으로 인해 장기적 과제에서 어려움을 겪습니다. 계층적 이중 시스템 방법은 이를 해결하지만, 고수준 계획 의미론과 저수준 실행 운동학 사이의 격차로 인해 어려움을 겪습니다. 우리는 Cortex를 소개합니다. 이는 고수준 VLM에서 저수준 VLA로 실행 가능하고 다루기 쉬운 하위 작업 계획을 전달하는 맞춤형 계획 인터페이스를 갖춘 양방향 정렬된 임베디드 에이전트 프레임워크입니다. 구체적으로, 조작 하위 작업을 32개의 표준 기술 프리미티브로 표준화하고, 대표 객체 속성 및 개선된 궤적 도달 가능성과 같은 다루기 쉬운 원칙을 데이터 생성 파이프라인에 주입합니다. 이를 통해 4,000시간 이상의 오픈소스 비디오 데이터를 자동으로 주석 처리하고 30시간의 시뮬레이션 데이터를 생성할 수 있습니다. 또한, 하위 작업 전환 중 계획 모호성을 더 잘 처리하기 위해 프레임워크를 미세 조정하기 위한 훈련 데이터를 구성하는 이벤트 균형 샘플링 전략을 고안하며, 추론 중 작업 컨텍스트에서 기술 제약까지 신중하게 설계된 하네스 엔지니어링으로 강화됩니다. 개방 루프 VLM 및 폐쇄 루프 시스템 평가 모두 Cortex의 효능을 입증합니다. 예를 들어, Libero-long에서 3.1%, RoboTwin에서 4.1%의 성능 향상을 보여줍니다. 특히, Cortex의 범용 VLM은 미세 조정된 VLA와 단순히 결합하여 다단계 화학 실험과 같은 보지 못한 실제 장기적 과제를 제로샷으로 완료할 수 있게 합니다. 이는 VLA 미세 조정만으로는 불가능한 능력입니다.
