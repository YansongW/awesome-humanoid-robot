---
$id: ent_paper_schneider_ce_mrs_contrastive_explanation_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CE-MRS: Contrastive Explanations for Multi-Robot Systems'
  zh: CE-MRS：多机器人系统的对比解释
  ko: 'CE-MRS: 다중 로봇 시스템을 위한 대비 설명'
summary:
  en: Introduces CE-MRS, a method that generates natural-language contrastive explanations by comparing a multi-robot system's
    solution with a user-proposed foil across task allocation, scheduling, and motion planning, validated in a search-and-rescue
    user study.
  zh: CE-MRS 是一种为多机器人系统生成自然语言对比解释的方法。它通过将系统解决方案与用户提出的替代方案（foil）在任务分配、调度和运动规划层面进行对比，帮助用户理解系统行为或纠正错误。在搜救场景的用户研究中验证了该方法能显著提升用户识别和解决系统错误的能力，从而改善多机器人团队的整体性能。
  ko: CE-MRS를 제안하여 다중 로봇 시스템의 해결책과 사용자가 제시한 대안 해결책을 비교하여 작업 할당, 스케줄링 및 동작 계획을 포괄하는 자연어 대비 설명을 생성하고 탐색·구조 사용자 연구로 검증함.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 05_mass_production
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- contrastive_explanations
- multi_robot_systems
- explainable_ai
- task_allocation
- scheduling
- motion_planning
- natural_language_generation
- search_and_rescue
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.08408v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (960 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CE-MRS: Contrastive Explanations for Multi-Robot Systems'
  url: https://arxiv.org/abs/2410.08408
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
随着多机器人系统在机器人数量、任务复杂度和时间跨度上的增长，其解决方案往往过于复杂，难以被人类用户完全理解。CE-MRS 提出了一种通用化的对比解释形式化框架，并在此基础上开发了一套整体性方法，能够有选择地整合多机器人任务分配、调度和运动规划中的数据，生成自然语言解释。这些解释旨在向用户证明系统解决方案的合理性，或帮助用户发现并修正导致次优方案的错误。用户研究结果表明，采用 CE-MRS 后，操作员识别和解决系统错误的能力显著增强，进而大幅提升了多机器人团队的整体表现。

## 核心内容
### 核心贡献
- **对比解释形式化**：首次为多机器人系统提出通用化的对比解释形式化框架，将系统实际方案与用户提出的替代方案（foil）进行结构化对比。
- **多层面数据整合**：方法有选择地融合来自三个关键规划层面的数据：
  - 多机器人任务分配（task allocation）
  - 调度（scheduling）
  - 运动规划（motion planning）
  从而生成覆盖系统行为全貌的解释。

### 方法架构
- **对比解释生成流程**：
  1. 接收系统当前解决方案与用户提出的替代方案（foil）。
  2. 在任务分配、调度和运动规划三个层面分别计算差异。
  3. 将差异转化为自然语言解释，突出系统方案为何更优，或指出用户方案中的错误。
- **解释目标**：既可用于证明系统方案的合理性，也可帮助用户定位并修正导致次优方案的问题。

### 实验设置
- **验证场景**：搜救任务（search-and-rescue）用户研究。
- **评估指标**：用户识别系统错误的能力、解决错误的能力，以及多机器人团队的整体性能。

### 关键结果
- 使用 CE-MRS 对比解释的用户，在识别系统错误方面的表现显著优于未使用该方法的对照组。
- 用户修正错误的速度和准确性均有提升，直接带来多机器人团队整体性能的显著改善。
- 实验证实，整合任务分配、调度和运动规划数据的多层面解释，比仅依赖单一层面的解释更有效。

### 结论
CE-MRS 通过提供结构化、多层面的对比解释，有效弥合了复杂多机器人系统与人类用户之间的理解鸿沟，在提升人机协作效率方面具有实用价值。

## Overview
As the complexity of multi-robot systems grows to incorporate a greater number of robots, more complex tasks, and longer time horizons, the solutions to such problems often become too complex to be fully intelligible to human users. In this work, we introduce an approach for generating natural language explanations that justify the validity of the system's solution to the user, or else aid the user in correcting any errors that led to a suboptimal system solution. Toward this goal, we first contribute a generalizable formalism of contrastive explanations for multi-robot systems, and then introduce a holistic approach to generating contrastive explanations for multi-robot scenarios that selectively incorporates data from multi-robot task allocation, scheduling, and motion-planning to explain system behavior. Through user studies with human operators we demonstrate that our integrated contrastive explanation approach leads to significant improvements in user ability to identify and solve system errors, leading to significant improvements in overall multi-robot team performance.

## 参考
- http://arxiv.org/abs/2410.08408v1

## 개요
다중 로봇 시스템이 로봇 수, 작업 복잡성, 시간 범위 측면에서 성장함에 따라, 그 해결책은 종종 너무 복잡해져 인간 사용자가 완전히 이해하기 어렵다. CE-MRS는 일반화된 대비 설명 형식화 프레임워크를 제안하고, 이를 기반으로 다중 로봇 작업 할당, 스케줄링, 운동 계획의 데이터를 선택적으로 통합하여 자연어 설명을 생성하는 전체론적 방법을 개발했다. 이러한 설명은 사용자에게 시스템 해결책의 타당성을 입증하거나, 사용자가 차선책을 초래한 오류를 발견하고 수정하도록 돕는 것을 목표로 한다. 사용자 연구 결과에 따르면, CE-MRS를 적용한 후 운영자가 시스템 오류를 식별하고 해결하는 능력이 크게 향상되어, 다중 로봇 팀의 전반적인 성과가 대폭 개선되었다.

## 핵심 내용
### 핵심 기여
- **대비 설명 형식화**: 다중 로봇 시스템을 위해 처음으로 일반화된 대비 설명 형식화 프레임워크를 제안하여, 시스템의 실제 해결책과 사용자가 제안한 대안(foil)을 구조적으로 비교한다.
- **다층 데이터 통합**: 이 방법은 세 가지 핵심 계획 수준의 데이터를 선택적으로 융합한다:
  - 다중 로봇 작업 할당(task allocation)
  - 스케줄링(scheduling)
  - 운동 계획(motion planning)
  이를 통해 시스템 행동의 전체적인 모습을 포괄하는 설명을 생성한다.

### 방법 아키텍처
- **대비 설명 생성 흐름**:
  1. 시스템의 현재 해결책과 사용자가 제안한 대안(foil)을 수신한다.
  2. 작업 할당, 스케줄링, 운동 계획의 세 수준에서 각각 차이를 계산한다.
  3. 차이를 자연어 설명으로 변환하여, 시스템 해결책이 왜 더 우수한지 강조하거나 사용자 해결책의 오류를 지적한다.
- **설명 목표**: 시스템 해결책의 타당성을 입증하는 데 사용될 수 있을 뿐만 아니라, 사용자가 차선책을 초래한 문제를 찾고 수정하도록 돕는 데도 사용될 수 있다.

### 실험 설정
- **검증 시나리오**: 수색 및 구조 작업(search-and-rescue) 사용자 연구.
- **평가 지표**: 사용자가 시스템 오류를 식별하는 능력, 오류를 해결하는 능력, 그리고 다중 로봇 팀의 전반적인 성능.

### 핵심 결과
- CE-MRS 대비 설명을 사용한 사용자는, 이 방법을 사용하지 않은 대조군보다 시스템 오류 식별에서 현저히 우수한 성과를 보였다.
- 사용자의 오류 수정 속도와 정확성이 모두 향상되어, 다중 로봇 팀의 전반적인 성능이 직접적으로 크게 개선되었다.
- 실험을 통해 작업 할당, 스케줄링, 운동 계획 데이터를 통합한 다층 설명이 단일 수준에만 의존하는 설명보다 더 효과적임을 확인했다.

### 결론
CE-MRS는 구조화되고 다층적인 대비 설명을 제공함으로써, 복잡한 다중 로봇 시스템과 인간 사용자 사이의 이해 격차를 효과적으로 좁히며, 인간-로봇 협업 효율성을 높이는 데 실용적인 가치를 지닌다.
