---
$id: ent_paper_colan_constrained_motion_planning_fo_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Constrained Motion Planning for a Robotic Endoscope Holder based on Hierarchical
    Quadratic Programming
  zh: 基于分层二次规划的机器人内窥镜支架约束运动规划
  ko: 계층적 이차 계획법을 기반으로 한 로봇 내시경 홀더의 구속 운동 계획
summary:
  en: Proposes an online hierarchical quadratic programming framework for visual servoing
    control of a surgical endoscope, prioritizing remote-center-of-motion constraints
    while tracking visual features as a secondary task.
  zh: 提出了一种用于手术内窥镜视觉伺服控制的在线分层二次规划框架，将远程运动中心约束作为高优先级任务，视觉特征跟踪作为次要任务。
  ko: 수술용 내시경의 비주얼 서보 제어를 위한 온라인 계층적 이차 계획 프레임워크를 제안하며, 원격 운동 중심 제약을 높은 우선순위 작업으로
    하고 시각적 특징 추적을 보조 작업으로 수행한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- hierarchical_quadratic_programming
- null_space_task_prioritization
- visual_servoing
- remote_center_of_motion
- constrained_motion_planning
- surgical_robotics
- real_time_optimization
- whole_body_control_transferable
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    full text before verification.
sources:
- id: src_001
  type: paper
  title: Constrained Motion Planning for a Robotic Endoscope Holder based on Hierarchical
    Quadratic Programming
  url: https://arxiv.org/abs/2406.09982
  date: '2023'
  accessed_at: '2026-06-27'
  doi: 10.1109/ICCRE57112.2023.10155579
theoretical_depth:
- method
---

## Overview

Minimally invasive surgery imposes strict kinematic constraints on robotic endoscope holders because the instrument must pivot around a fixed trocar insertion point without damaging surrounding tissue. This paper addresses that challenge by casting endoscope positioning and visual tracking as a hierarchy of quadratic programs solved online. The remote-center-of-motion (RCM) constraint is enforced at the highest priority, while visual servoing is relegated to the null space of the RCM task so that tracking motions cannot violate the insertion constraint.

The authors implement the framework on a 6-DOF Denso VS050 manipulator equipped with a rigid endoscope, a Ximea MQ022CG camera, and an Optitrack motion-capture system for ground-truth pose feedback. The hierarchical QP is solved in real time, reportedly averaging 372 μs per optimization step and keeping maximum RCM deviation near 0.4 mm. Joint limits are handled via slack variables integrated into the QP formulation.

The reported experiments validate both RCM preservation and autonomous visual-feature tracking on phantom tissue, demonstrating that the prioritized structure can satisfy safety-critical constraints while still enabling useful visual task execution.

## Key Contributions

- Formulation of the RCM constraint as a prioritized QP task with joint-limit handling through slack variables.
- HQP-based null-space visual servoing that leaves the high-priority RCM constraint undisturbed.
- Real-time implementation with average QP solving times of 372 μs.
- Experimental validation on a 6-DOF Denso VS050 manipulator with maximum RCM deviation of approximately 0.4 mm.

## Relevance to Humanoid Robotics

Although the work targets surgical endoscope holders, its hierarchical QP and null-space task-prioritization techniques are directly transferable to humanoid whole-body control. Humanoids must simultaneously enforce multiple hard constraints—balance, joint limits, self-collision avoidance, and manipulation task goals—in real time, exactly the setting for which HQP was designed.

The paper therefore serves as a reference implementation of prioritized whole-body control methods that can be reused or extended in humanoid platforms, particularly where high-priority safety constraints must take precedence over lower-priority operational tasks without manual weight tuning.
