---
$id: ent_paper_hughes_foundations_of_spatial_percept_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Foundations of Spatial Perception for Robotics: Hierarchical Representations
    and Real-time Systems'
  zh: 机器人空间感知的基础：层次化表征与实时系统
  ko: '로봇 공간 인식의 기초: 계층적 표상과 실시간 시스템'
summary:
  en: This paper formalizes hierarchical 3D scene graphs as scalable spatial representations
    and introduces Hydra, an open-source real-time system that incrementally builds,
    maintains, and corrects such scene graphs from visual-inertial data, demonstrated
    in simulation and on real robots.
  zh: 本文将层次化三维场景图形式化为可扩展的空间表征，并提出了Hydra——一个开源实时系统，该系统能从视觉惯性数据中增量式地构建、维护和校正三维场景图，并在仿真和真实机器人上进行了验证。
  ko: 본 논문은 계층적 3D 장면 그래프를 확장 가능한 공간 표상으로 형식화하고, 시각-관성 데이터로부터 3D 장면 그래프를 실시간으로 점진적으로
    구축·유지·보정하는 오픈소스 실시간 시스템인 Hydra를 제안하며, 시뮬레이션과 실제 로봇에서 검증되었다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- spatial_perception
- 3d_scene_graph
- hydra
- slam
- metric_semantic_mapping
- hierarchical_mapping
- loop_closure
- visual_inertial
- real_time_perception
- indoor_navigation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the paper PDF and metadata; human review is required before
    marking fully verified.; approved by autonomous review workflow.
sources:
- id: src_001
  type: paper
  title: 'Foundations of Spatial Perception for Robotics: Hierarchical Representations
    and Real-time Systems'
  url: https://arxiv.org/abs/2305.07154
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- formalism
- method
- system
---

## Overview

The paper defines 3D spatial perception as the task of building and maintaining an actionable, persistent representation of the environment in real time from sensor data and prior knowledge. It argues that purely geometric maps and flat metric-semantic maps do not scale to large environments or large semantic vocabularies, and that scalable representations must be hierarchical. The authors formalize hierarchical graphs, prove that their treewidth is bounded by the complexity of individual layers rather than the overall graph size, and instantiate these ideas as a 3D scene graph for indoor environments with layers for geometry, objects, places, rooms, and buildings.

The second and third parts present incremental algorithms to construct and correct 3D scene graphs. Construction combines metric-semantic mesh reconstruction, Generalized Voronoi Diagram-based extraction of a sparse graph of places, topological room clustering via persistent homology, and neural-tree room classification. Maintenance relies on learned hierarchical descriptors for loop-closure detection and a 3D scene graph optimization algorithm that uses embedded deformation graphs to consistently correct all layers, including the 3D mesh, objects, places, and the robot trajectory.

The algorithms are integrated into Hydra, an open-source, highly parallelized perception system that processes visual-inertial data at sensor, sub-second, and map-scale rates. Hydra is evaluated on simulated Matterport3D and uHumans2 data and on the real-world Simmons dataset collected with a Clearpath Jackal and a Unitree A1, including an onboard real-time demonstration on the Unitree A1 with an NVIDIA Xavier NX.

## Key Contributions

- Formal foundations showing that hierarchical representations compress symbolic and geometric information and yield layered graphs with small treewidth for efficient inference.
- Real-time incremental algorithms to build a multi-layer 3D scene graph (mesh, objects, places, rooms, building) from visual-inertial data.
- Hierarchical loop-closure detection using learned descriptors and the first 3D scene graph optimization algorithm for consistent correction across layers.
- Hydra, an open-source real-time spatial perception system demonstrated in photo-realistic simulation and on real Clearpath Jackal and Unitree A1 robots.

## Relevance to Humanoid Robotics

Mass-produced humanoid robots need low-memory, actionable spatial representations that support scalable mapping, loop closure, and task execution in large indoor environments. Hydra provides a real-time hierarchical 3D scene graph that organizes geometry, objects, places, and rooms, which can serve as a semantic map for navigation, manipulation planning, and natural-language instruction grounding. The learned hierarchical descriptors and multi-layer optimization also offer a path toward robust long-term autonomy for humanoids. However, the paper focuses on static indoor environments and evaluates on wheeled and quadruped robots, so direct deployment on humanoid platforms would require extensions for dynamic scenes, uneven terrain, and whole-body perception.
