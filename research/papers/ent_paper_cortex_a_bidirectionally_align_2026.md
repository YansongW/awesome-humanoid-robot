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
  zh: Cortex 是一个双向对齐的具身智能体框架，旨在解决长时程操作任务中高层规划与低层执行之间的语义鸿沟。该框架由研究团队提出，核心贡献在于通过 32 种规范技能原语和可执行性注入的数据生成管线，实现了从 VLM 到 VLA 的可执行子任务规划传递，并在
    Libero-long 和 RoboTwin 基准上分别取得 3.1% 和 4.1% 的性能提升。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.05377v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (797 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.05377
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Cortex 框架通过双向对齐机制弥合了高层规划语义与低层执行运动学之间的差距。它将操作子任务标准化为 32 种规范技能原语，并在数据生成管线中注入可执行性原理，如代表性物体属性和改进的轨迹可达性。该框架能够自动标注超过 4000 小时的开源视频数据，并生成 30 小时的仿真数据。通过事件平衡采样策略和推理时的任务上下文约束工程，Cortex 有效处理了子任务转换中的规划歧义问题。

## 核心内容
### 方法架构
Cortex 采用层次化双系统架构，核心是一个自定义规划接口，负责将高层 VLM 的规划语义转化为低层 VLA 可执行的子任务计划。具体而言：
- **技能原语标准化**：将操作子任务归纳为 32 种规范技能原语，覆盖常见操作类型。
- **可执行性注入**：在数据生成管线中引入代表性物体属性和改进的轨迹可达性等原则，确保生成的子任务计划在运动学上可行。
- **数据生成**：实现自动标注超过 4000 小时的开源视频数据，并生成 30 小时的仿真数据用于训练。

### 训练与推理策略
- **事件平衡采样**：设计专门的采样策略构建训练数据，重点处理子任务转换时的规划歧义问题。
- **推理时约束工程**：从任务上下文中提取技能约束，通过精心设计的约束机制增强推理阶段的规划稳定性。

### 实验设置与结果
- **基准测试**：在 Libero-long 和 RoboTwin 两个长时程操作基准上进行评估。
- **性能对比**：Cortex 在 Libero-long 上超越 monolithic 基线 3.1%，在 RoboTwin 上超越 4.1%。
- **零样本泛化**：Cortex 的通用 VLM 与微调后的 VLA 结合，能够零样本完成未见过的真实世界长时程任务，例如多阶段化学实验——这一能力仅通过 VLA 微调无法实现。

## Overview
While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature-relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles, such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data. We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy, e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply combining with a fine-tuned VLA-a capability infeasible through VLA fine-tuning alone.

## Overview
While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature—relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles, such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data. We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy, e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply combining with a fine-tuned VLA—a capability infeasible through VLA fine-tuning alone.

## Content
While recent Vision-Language-Action (VLA) models show promise toward generalist manipulation policies, they struggle with long-horizon tasks due to their Markovian nature—relying solely on current observations. Hierarchical dual-system methods address this but suffer from a gap between high-level planning semantics and low-level execution kinematics. We introduce Cortex, a bidirectionally aligned embodied agent framework with a customized planning interface that conveys executable and tractable subtask plans from high-level VLM to low-level VLA. Specifically, we standardize manipulation subtasks into 32 canonical skill primitives and inject tractability principles, such as representative object attributes and improved trajectory reachability, into the data generation pipeline. This enables automatic annotation of over 4k hours of open-source video data and generation of 30 hours of simulation data. We further devise an event-balanced sampling strategy to construct training data for fine-tuning the framework to better handle planning ambiguity during subtask transitions, enhanced by carefully designed harness engineering from task contexts to skill constraints during inference. Both open-loop VLM and closed-loop system evaluations demonstrate Cortex's efficacy, e.g., it outperforms monolithic baselines by 3.1% on Libero-long and 4.1% on RoboTwin. Notably, Cortex's generalist VLM enables zero-shot completion of unseen real-world long-horizon tasks, such as multi-stage chemistry experiments, by simply combining with a fine-tuned VLA—a capability infeasible through VLA fine-tuning alone.

## 参考
- http://arxiv.org/abs/2607.05377v1

## 개요
Cortex 프레임워크는 양방향 정렬 메커니즘을 통해 고수준 계획 의미론과 저수준 실행 운동학 사이의 격차를 해소합니다. 조작 하위 작업을 32가지 표준 스킬 원시 유형으로 표준화하고, 데이터 생성 파이프라인에 대표 객체 속성 및 개선된 궤적 도달 가능성과 같은 실행 가능성 원칙을 주입합니다. 이 프레임워크는 4000시간 이상의 오픈소스 비디오 데이터를 자동으로 주석 처리하고 30시간의 시뮬레이션 데이터를 생성할 수 있습니다. 이벤트 균형 샘플링 전략과 추론 시 작업 컨텍스트 제약 엔지니어링을 통해 Cortex는 하위 작업 전환에서의 계획 모호성 문제를 효과적으로 처리합니다.

## 핵심 내용
### 방법 아키텍처
Cortex는 계층적 이중 시스템 아키텍처를 채택하며, 핵심은 고수준 VLM의 계획 의미론을 저수준 VLA가 실행 가능한 하위 작업 계획으로 변환하는 맞춤형 계획 인터페이스입니다. 구체적으로:
- **스킬 원시 유형 표준화**: 조작 하위 작업을 32가지 표준 스킬 원시 유형으로 귀납하여 일반적인 조작 유형을 포괄합니다.
- **실행 가능성 주입**: 데이터 생성 파이프라인에 대표 객체 속성 및 개선된 궤적 도달 가능성과 같은 원칙을 도입하여 생성된 하위 작업 계획이 운동학적으로 실행 가능하도록 보장합니다.
- **데이터 생성**: 4000시간 이상의 오픈소스 비디오 데이터를 자동으로 주석 처리하고, 훈련을 위한 30시간의 시뮬레이션 데이터를 생성합니다.

### 훈련 및 추론 전략
- **이벤트 균형 샘플링**: 훈련 데이터 구축을 위한 전용 샘플링 전략을 설계하여 하위 작업 전환 시의 계획 모호성 문제를 중점적으로 처리합니다.
- **추론 시 제약 엔지니어링**: 작업 컨텍스트에서 스킬 제약을 추출하고, 정교하게 설계된 제약 메커니즘을 통해 추론 단계의 계획 안정성을 강화합니다.

### 실험 설정 및 결과
- **벤치마크 테스트**: Libero-long 및 RoboTwin 두 가지 장기 조작 벤치마크에서 평가를 수행합니다.
- **성능 비교**: Cortex는 Libero-long에서 monolithic 기준선을 3.1% 초과하고, RoboTwin에서 4.1% 초과합니다.
- **제로샷 일반화**: Cortex의 범용 VLM과 미세 조정된 VLA의 결합은 다단계 화학 실험과 같은 보지 못한 실제 세계 장기 작업을 제로샷으로 완료할 수 있습니다 — 이 능력은 VLA 미세 조정만으로는 달성할 수 없습니다.
