---
$id: ent_method_hierarchical_qp_wbc
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Hierarchical QP Whole-Body Control
  zh: 分层二次规划全身控制
  ko: 계층적 QP 전신 제어
summary:
  en: A whole-body control method that stacks multiple tasks by priority and solves them as a cascade of quadratic programs, ensuring higher-priority tasks are fulfilled before lower-priority ones.
  zh: 一种按优先级堆叠多个任务并通过级联二次规划求解的全身控制方法，确保高优先级任务优先满足。
  ko: 여러 작업을 우선순위에 따라 쌓아 올리고 연속된 이차 계획법으로 풀어 높은 우선순위 작업을 먼저 만족시키는 전신 제어 방법이다.
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- intelligence
- knowledge
tags:
- whole_body_control
- hierarchical_qp
- stack_of_tasks
- quadratic_programming
- humanoid_robot
theoretical_depth:
- method
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Based on de Lasa et al. 2010, Herzog et al. 2016, and Kim et al. 2019.
sources:
- id: src_001
  type: paper
  title: 'Hierarchical QP whole-body control: from theory to practice'
  url: https://arxiv.org/abs/1910.13329
  date: '2019'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_formalism_inverse_dynamics_qp
  relationship: formalizes
  description:
    en: Hierarchical QP WBC instantiates the inverse-dynamics QP formulation.
    zh: 分层 QP WBC 实例化了逆动力学 QP 形式化。
    ko: 계층적 QP WBC는 역동역학 QP 공식화를 구현한다.
- id: ent_operator_task_jacobian
  relationship: uses
  description:
    en: Each task in the hierarchy is expressed through its task Jacobian.
    zh: 层级中的每个任务都通过其任务 Jacobian 表达。
    ko: 계층의 각 작업은 작업 Jacobian을 통해 표현된다.
---

## 抽象

> **生活实例**：想象一位杂技演员同时要保持平衡、伸手抓杆、还要对观众微笑。她的身体得先保证不倒（最高优先级），再完成抓杆，最后才是表情。Hierarchical QP WBC 就像这位演员的大脑——它把“平衡”“抓杆”“微笑”排成优先级，先求解最重要的任务，再在不破坏高优先级任务的前提下处理下一个。
>
> **自然语言逻辑**：人形机器人有多个同时发生的目标（如保持重心、跟踪 footsteps、操作物体）。把这些目标按优先级排序后，QP WBC 用二次规划逐层求解：每一层都在满足更高层约束的剩余自由度里优化自己的目标。

## Overview

Hierarchical QP Whole-Body Control (WBC) is a control framework for floating-base robots such as humanoids. It represents each desired task (e.g., center-of-mass tracking, foot placement, upper-body posture) as a task space objective and solves them in strict priority order. Higher-priority tasks are treated as hard constraints for lower-priority tasks, which prevents important behaviors such as balance from being sacrificed for secondary objectives.

## Key Characteristics

- Tasks are stacked by priority using a stack-of-tasks formulation.
- Each priority level is solved as a quadratic program (QP).
- The solution of higher-priority QPs constrains the feasible set of lower-priority QPs.
- Commonly used with inverse-dynamics formulations to compute joint torques directly.

## Relevance to Humanoid Robotics

Humanoid robots must simultaneously balance, locomote, and manipulate. Hierarchical QP WBC provides a principled way to coordinate these objectives while respecting physical limits such as torque and joint limits.
