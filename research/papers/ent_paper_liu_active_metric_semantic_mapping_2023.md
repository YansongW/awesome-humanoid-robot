---
$id: ent_paper_liu_active_metric_semantic_mapping_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Active Metric-Semantic Mapping by Multiple Aerial Robots
  zh: 多空中机器人主动度量语义建图
  ko: 다중 공중 로봇을 위한 능동 메트릭-시맨틱 매핑
summary:
  en: This paper presents PAMS, an active metric-semantic mapping framework in which
    multiple heterogeneous aerial robots collaboratively build compact object-level
    maps and select informative viewpoints to reduce both geometric and semantic uncertainties.
    The approach integrates a real-time metric-semantic SLAM system with empirically
    characterized uncertainty models and is validated through real-world multi-robot
    experiments.
  zh: 本文提出了PAMS，一种主动度量语义建图框架，使多个异构空中机器人协作构建紧凑的对象级地图，并选择信息丰富的视点以降低几何与语义不确定性。该方法将实时度量语义SLAM与经验表征的不确定性模型相结合，并通过真实多机器人实验验证。
  ko: 본 논문은 다수의 이종 공중 로봇이 협력하여 컴팩트한 객체 수준 지도를 구축하고 기하학적 및 의미론적 불확실성을 모두 줄이도록 정보가 풍부한
    관점을 선택하는 능동 메트릭-시맨틱 매핑 프레임워크 PAMS를 제안한다. 실시간 메트릭-시맨틱 SLAM과 실제 데이터로부터 경험적으로 특성화된
    불확실성 모델을 통합하고 실제 다중 로봇 실험으로 검증하였다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- intelligence
- knowledge
tags:
- active_perception
- metric_semantic_mapping
- multi_robot_mapping
- semantic_slam
- object_level_mapping
- information_theoretic_planning
- uncertainty_quantification
- aerial_robots
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied paper metadata; requires human review against
    the full PDF before verification.
sources:
- id: src_001
  type: paper
  title: Active Metric-Semantic Mapping by Multiple Aerial Robots
  url: https://arxiv.org/abs/2209.08465
  date: '2023'
  accessed_at: '2026-06-27'
  doi: 10.1109/ICRA48891.2023.10161564
theoretical_depth:
- method
---

## Overview

The paper addresses active metric-semantic mapping, where robots must simultaneously acquire geometric structure and semantic labels for objects in an environment rather than building purely geometric maps. It proposes a collaborative framework called PAMS that dispatches multiple heterogeneous aerial robots to explore a scene and reduce uncertainty in both object shape estimates and object class predictions. The environment is represented compactly by sparse object models—primarily cuboids, cylinders, and planes—each associated with a semantic class label, which keeps storage requirements low while retaining actionable information.

A real-time metric-semantic SLAM backend is implemented with customized cuboid and cylinder factors within a GTSAM factor graph, enabling joint inference over robot poses and object states. To guide exploration, the authors derive empirical uncertainty models from a large corpus of real-world observations; these models predict how semantic classification error and geometric estimation error vary with viewpoint and sensor configuration. The resulting information-theoretic planner selects actions for each robot that maximize the expected reduction in combined semantic and geometric uncertainty.

The complete autonomy stack is evaluated in real-world multi-robot experiments across outdoor and semi-structured environments. Results show that the proposed PAMS planner outperforms a heuristic baseline that simply visits each prior object location, producing more accurate object models with fewer observations. The authors also demonstrate that heterogeneous robot teams can improve mapping speed and accuracy while maintaining the compact object-level map representation.

## Key Contributions

- A real-time metric-semantic SLAM algorithm using sparse, storage-efficient object models with customized cuboid and cylinder factors in a factor graph, supporting multi-robot collaboration.
- An active metric-semantic mapping algorithm (PAMS) that uses empirical uncertainty characterizations learned from real-world data to select informative robot actions.
- Integration with a complete autonomy stack and real-world multi-robot experiments demonstrating improved object-model accuracy over a heuristic baseline.
- Demonstration that heterogeneous multi-robot teams improve mapping accuracy and speed while maintaining a compact map representation.

## Relevance to Humanoid Robotics

Although the experiments are conducted with aerial robots, the core technical contributions—real-time metric-semantic SLAM, object-level scene representations, and data-driven active perception for uncertainty reduction—are directly transferable to humanoid robotics. Humanoid platforms operating in factories, warehouses, or unstructured outdoor settings must similarly build semantic maps of objects and infrastructure while planning viewpoints that improve classification and shape estimates.

The compact object-model representation and the information-theoretic planning principle can help humanoid robots decide where to stand or how to orient their head-mounted sensors to reduce uncertainty before manipulation or navigation tasks. Therefore, the paper is most relevant to the ai_models_algorithms domain as a methodological reference for semantic mapping and active perception in general mobile robotics, including humanoid applications.
