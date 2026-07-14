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
  en: MAPS-X introduces meta-algorithms that integrate disjoint trajectory segmentation into centralized sampling-based tree
    planners to generate multi-robot motion plans that are visually explainable and bounded by a user-defined number of segments.
  zh: MAPS-X 将不相交轨迹分段集成到集中式基于采样的树规划器中，生成受用户指定段数约束、可视觉验证的多机器人运动规划。
  ko: MAPS-X는 중앙 집중식 샘플링 기반 트리 플래너에 분리된 궤적 세분화를 통합하여 사용자가 정의한 세그먼트 수 범위 내에서 시각적으로 설명 가능한 다중 로봇 동작 계획을 생성한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2010.16106v3.
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
## 概述
Traditional multi-robot motion planning (MMP) focuses on computing trajectories for multiple robots acting in an environment, such that the robots do not collide when the trajectories are taken simultaneously. In safety-critical applications, a human supervisor may want to verify that the plan is indeed collision-free. In this work, we propose a notion of explanation for a plan of MMP, based on visualization of the plan as a short sequence of images representing time segments, where in each time segment the trajectories of the agents are disjoint, clearly illustrating the safety of the plan. We show that standard notions of optimality (e.g., makespan) may create conflict with short explanations. Thus, we propose meta-algorithms, namely multi-agent plan segmenting-X (MAPS-X) and its lazy variant, that can be plugged on existing centralized sampling-based tree planners X to produce plans with good explanations using a desirable number of images. We demonstrate the efficacy of this explanation-planning scheme and extensively evaluate the performance of MAPS-X.

## 核心内容
Traditional multi-robot motion planning (MMP) focuses on computing trajectories for multiple robots acting in an environment, such that the robots do not collide when the trajectories are taken simultaneously. In safety-critical applications, a human supervisor may want to verify that the plan is indeed collision-free. In this work, we propose a notion of explanation for a plan of MMP, based on visualization of the plan as a short sequence of images representing time segments, where in each time segment the trajectories of the agents are disjoint, clearly illustrating the safety of the plan. We show that standard notions of optimality (e.g., makespan) may create conflict with short explanations. Thus, we propose meta-algorithms, namely multi-agent plan segmenting-X (MAPS-X) and its lazy variant, that can be plugged on existing centralized sampling-based tree planners X to produce plans with good explanations using a desirable number of images. We demonstrate the efficacy of this explanation-planning scheme and extensively evaluate the performance of MAPS-X.

## 参考
- http://arxiv.org/abs/2010.16106v3

