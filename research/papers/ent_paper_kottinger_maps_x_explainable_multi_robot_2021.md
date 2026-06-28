---
$id: ent_paper_kottinger_maps_x_explainable_multi_robot_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MAPS-X: Explainable Multi-Robot Motion Planning via Segmentation'
  zh: MAPS-X：基于轨迹分段的可解释多机器人运动规划
  ko: 'MAPS-X: 세분화를 통한 설명 가능한 다중 로봇 동작 계획'
summary:
  en: MAPS-X introduces meta-algorithms that integrate disjoint trajectory segmentation
    into centralized sampling-based tree planners to generate multi-robot motion plans
    that are visually explainable and bounded by a user-defined number of segments.
  zh: MAPS-X 将不相交轨迹分段集成到集中式基于采样的树规划器中，生成受用户指定段数约束、可视觉验证的多机器人运动规划。
  ko: MAPS-X는 중앙 집중식 샘플링 기반 트리 플래너에 분리된 궤적 세분화를 통합하여 사용자가 정의한 세그먼트 수 범위 내에서 시각적으로
    설명 가능한 다중 로봇 동작 계획을 생성한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- multi_robot_motion_planning
- explainable_ai
- trajectory_segmentation
- sampling_based_planning
- motion_planning
- safety_critical_systems
- probabilistic_completeness
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from abstract and supplied metadata; requires human review against
    full paper before verification.
sources:
- id: src_001
  type: paper
  title: 'MAPS-X: Explainable Multi-Robot Motion Planning via Segmentation'
  url: https://arxiv.org/abs/2010.16106
  date: '2021'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Multi-robot motion planning (MMP) traditionally computes collision-free trajectories for multiple robots acting simultaneously in a shared environment. While such plans can be proven correct algorithmically, safety-critical applications often require human supervisors to visually verify that the plan is collision-free. This paper proposes an explanation framework for MMP based on segmenting the plan into a short sequence of images, each representing a time segment in which the robot trajectories are spatially disjoint. The authors observe that standard optimality objectives, such as makespan, can conflict with the goal of producing short, understandable explanations.

To resolve this tension, the authors introduce MAPS-X and Lazy MAPS-X, meta-algorithms that wrap existing centralized sampling-based tree planners. MAPS-X enforces a user-specified bound on the number of segments during tree growth, while Lazy MAPS-X first finds a solution and then prunes it if it violates the segment bound. Both variants are shown to preserve the probabilistic completeness of the underlying planner. The methods are evaluated empirically across several simulated environments and agent dynamics.

## Key Contributions

- Formalization of explainable MMP using segment-disjoint trajectories in continuous space.
- MAPS-X meta-algorithm that enforces a segmentation bound during tree growth.
- Lazy MAPS-X variant that prunes solutions violating the segmentation bound.
- Proof that both variants preserve probabilistic completeness of the base planner.
- Extensive empirical evaluation across multiple environments and agent dynamics.

## Relevance to Humanoid Robotics

Although MAPS-X is framed generally for multi-robot systems, its focus on explainable, collision-free motion planning is directly relevant to humanoid deployment in shared industrial or service workspaces. Humanoid robots operating near humans must not only plan safe trajectories but also make those plans interpretable to human supervisors and collaborators. The segment-based visualization approach in this work provides a mechanism for human verification of complex multi-agent motions, supporting safer integration of humanoid systems into safety-critical applications.
