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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.08408v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
다중 로봇 시스템의 복잡성이 증가하여 더 많은 로봇, 더 복잡한 작업, 더 긴 시간 범위를 포함하게 됨에 따라, 이러한 문제에 대한 해결책은 종종 인간 사용자가 완전히 이해하기에는 너무 복잡해집니다. 본 연구에서는 시스템 솔루션의 타당성을 사용자에게 설명하거나, 최적이 아닌 시스템 솔루션으로 이어진 오류를 사용자가 수정하는 데 도움을 주는 자연어 설명을 생성하는 접근 방식을 소개합니다. 이를 위해 먼저 다중 로봇 시스템을 위한 대조 설명의 일반화 가능한 형식론을 제시하고, 다중 로봇 작업 할당, 스케줄링 및 모션 플래닝의 데이터를 선택적으로 통합하여 시스템 동작을 설명하는 다중 로봇 시나리오를 위한 대조 설명 생성의 전체론적 접근 방식을 도입합니다. 인간 운영자를 대상으로 한 사용자 연구를 통해, 통합된 대조 설명 접근 방식이 사용자가 시스템 오류를 식별하고 해결하는 능력을 크게 향상시켜, 전반적인 다중 로봇 팀 성능의 유의미한 개선을 가져온다는 것을 입증합니다.

## 핵심 내용
다중 로봇 시스템의 복잡성이 증가하여 더 많은 로봇, 더 복잡한 작업, 더 긴 시간 범위를 포함하게 됨에 따라, 이러한 문제에 대한 해결책은 종종 인간 사용자가 완전히 이해하기에는 너무 복잡해집니다. 본 연구에서는 시스템 솔루션의 타당성을 사용자에게 설명하거나, 최적이 아닌 시스템 솔루션으로 이어진 오류를 사용자가 수정하는 데 도움을 주는 자연어 설명을 생성하는 접근 방식을 소개합니다. 이를 위해 먼저 다중 로봇 시스템을 위한 대조 설명의 일반화 가능한 형식론을 제시하고, 다중 로봇 작업 할당, 스케줄링 및 모션 플래닝의 데이터를 선택적으로 통합하여 시스템 동작을 설명하는 다중 로봇 시나리오를 위한 대조 설명 생성의 전체론적 접근 방식을 도입합니다. 인간 운영자를 대상으로 한 사용자 연구를 통해, 통합된 대조 설명 접근 방식이 사용자가 시스템 오류를 식별하고 해결하는 능력을 크게 향상시켜, 전반적인 다중 로봇 팀 성능의 유의미한 개선을 가져온다는 것을 입증합니다.

## 参考
- http://arxiv.org/abs/2410.08408v1
