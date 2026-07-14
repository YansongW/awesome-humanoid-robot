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
  zh: 提出 CE-MRS 方法，通过比较多机器人系统方案与用户提出的反事实方案，生成涵盖任务分配、调度与运动规划的自然语言对比解释，并在搜索救援用户研究中验证。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.08408v1.
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
As the complexity of multi-robot systems grows to incorporate a greater number of robots, more complex tasks, and longer time horizons, the solutions to such problems often become too complex to be fully intelligible to human users. In this work, we introduce an approach for generating natural language explanations that justify the validity of the system's solution to the user, or else aid the user in correcting any errors that led to a suboptimal system solution. Toward this goal, we first contribute a generalizable formalism of contrastive explanations for multi-robot systems, and then introduce a holistic approach to generating contrastive explanations for multi-robot scenarios that selectively incorporates data from multi-robot task allocation, scheduling, and motion-planning to explain system behavior. Through user studies with human operators we demonstrate that our integrated contrastive explanation approach leads to significant improvements in user ability to identify and solve system errors, leading to significant improvements in overall multi-robot team performance.

## 核心内容
As the complexity of multi-robot systems grows to incorporate a greater number of robots, more complex tasks, and longer time horizons, the solutions to such problems often become too complex to be fully intelligible to human users. In this work, we introduce an approach for generating natural language explanations that justify the validity of the system's solution to the user, or else aid the user in correcting any errors that led to a suboptimal system solution. Toward this goal, we first contribute a generalizable formalism of contrastive explanations for multi-robot systems, and then introduce a holistic approach to generating contrastive explanations for multi-robot scenarios that selectively incorporates data from multi-robot task allocation, scheduling, and motion-planning to explain system behavior. Through user studies with human operators we demonstrate that our integrated contrastive explanation approach leads to significant improvements in user ability to identify and solve system errors, leading to significant improvements in overall multi-robot team performance.

## 参考
- http://arxiv.org/abs/2410.08408v1

