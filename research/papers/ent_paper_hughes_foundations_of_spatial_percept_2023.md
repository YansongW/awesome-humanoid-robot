---
$id: ent_paper_hughes_foundations_of_spatial_percept_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems'
  zh: 机器人空间感知的基础：层次化表征与实时系统
  ko: '로봇 공간 인식의 기초: 계층적 표상과 실시간 시스템'
summary:
  en: This paper formalizes hierarchical 3D scene graphs as scalable spatial representations and introduces Hydra, an open-source
    real-time system that incrementally builds, maintains, and corrects such scene graphs from visual-inertial data, demonstrated
    in simulation and on real robots.
  zh: 本文将层次化三维场景图形式化为可扩展的空间表征，并提出了Hydra——一个开源实时系统，该系统能从视觉惯性数据中增量式地构建、维护和校正三维场景图，并在仿真和真实机器人上进行了验证。
  ko: 본 논문은 계층적 3D 장면 그래프를 확장 가능한 공간 표상으로 형식화하고, 시각-관성 데이터로부터 3D 장면 그래프를 실시간으로 점진적으로 구축·유지·보정하는 오픈소스 실시간 시스템인 Hydra를 제안하며,
    시뮬레이션과 실제 로봇에서 검증되었다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2305.07154v1.
sources:
- id: src_001
  type: paper
  title: 'Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems'
  url: https://arxiv.org/abs/2305.07154
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- formalism
- method
- system
---
## 概述
3D spatial perception is the problem of building and maintaining an actionable and persistent representation of the environment in real-time using sensor data and prior knowledge. Despite the fast-paced progress in robot perception, most existing methods either build purely geometric maps (as in traditional SLAM) or flat metric-semantic maps that do not scale to large environments or large dictionaries of semantic labels. The first part of this paper is concerned with representations: we show that scalable representations for spatial perception need to be hierarchical in nature. Hierarchical representations are efficient to store, and lead to layered graphs with small treewidth, which enable provably efficient inference. We then introduce an example of hierarchical representation for indoor environments, namely a 3D scene graph, and discuss its structure and properties. The second part of the paper focuses on algorithms to incrementally construct a 3D scene graph as the robot explores the environment. Our algorithms combine 3D geometry, topology (to cluster the places into rooms), and geometric deep learning (e.g., to classify the type of rooms the robot is moving across). The third part of the paper focuses on algorithms to maintain and correct 3D scene graphs during long-term operation. We propose hierarchical descriptors for loop closure detection and describe how to correct a scene graph in response to loop closures, by solving a 3D scene graph optimization problem. We conclude the paper by combining the proposed perception algorithms into Hydra, a real-time spatial perception system that builds a 3D scene graph from visual-inertial data in real-time. We showcase Hydra's performance in photo-realistic simulations and real data collected by a Clearpath Jackal robots and a Unitree A1 robot. We release an open-source implementation of Hydra at https://github.com/MIT-SPARK/Hydra.

## 核心内容
3D spatial perception is the problem of building and maintaining an actionable and persistent representation of the environment in real-time using sensor data and prior knowledge. Despite the fast-paced progress in robot perception, most existing methods either build purely geometric maps (as in traditional SLAM) or flat metric-semantic maps that do not scale to large environments or large dictionaries of semantic labels. The first part of this paper is concerned with representations: we show that scalable representations for spatial perception need to be hierarchical in nature. Hierarchical representations are efficient to store, and lead to layered graphs with small treewidth, which enable provably efficient inference. We then introduce an example of hierarchical representation for indoor environments, namely a 3D scene graph, and discuss its structure and properties. The second part of the paper focuses on algorithms to incrementally construct a 3D scene graph as the robot explores the environment. Our algorithms combine 3D geometry, topology (to cluster the places into rooms), and geometric deep learning (e.g., to classify the type of rooms the robot is moving across). The third part of the paper focuses on algorithms to maintain and correct 3D scene graphs during long-term operation. We propose hierarchical descriptors for loop closure detection and describe how to correct a scene graph in response to loop closures, by solving a 3D scene graph optimization problem. We conclude the paper by combining the proposed perception algorithms into Hydra, a real-time spatial perception system that builds a 3D scene graph from visual-inertial data in real-time. We showcase Hydra's performance in photo-realistic simulations and real data collected by a Clearpath Jackal robots and a Unitree A1 robot. We release an open-source implementation of Hydra at https://github.com/MIT-SPARK/Hydra.

## 参考
- http://arxiv.org/abs/2305.07154v1

## Overview
3D spatial perception is the problem of building and maintaining an actionable and persistent representation of the environment in real-time using sensor data and prior knowledge. Despite the fast-paced progress in robot perception, most existing methods either build purely geometric maps (as in traditional SLAM) or flat metric-semantic maps that do not scale to large environments or large dictionaries of semantic labels. The first part of this paper is concerned with representations: we show that scalable representations for spatial perception need to be hierarchical in nature. Hierarchical representations are efficient to store, and lead to layered graphs with small treewidth, which enable provably efficient inference. We then introduce an example of hierarchical representation for indoor environments, namely a 3D scene graph, and discuss its structure and properties. The second part of the paper focuses on algorithms to incrementally construct a 3D scene graph as the robot explores the environment. Our algorithms combine 3D geometry, topology (to cluster the places into rooms), and geometric deep learning (e.g., to classify the type of rooms the robot is moving across). The third part of the paper focuses on algorithms to maintain and correct 3D scene graphs during long-term operation. We propose hierarchical descriptors for loop closure detection and describe how to correct a scene graph in response to loop closures, by solving a 3D scene graph optimization problem. We conclude the paper by combining the proposed perception algorithms into Hydra, a real-time spatial perception system that builds a 3D scene graph from visual-inertial data in real-time. We showcase Hydra's performance in photo-realistic simulations and real data collected by a Clearpath Jackal robots and a Unitree A1 robot. We release an open-source implementation of Hydra at https://github.com/MIT-SPARK/Hydra.

## Content
3D spatial perception is the problem of building and maintaining an actionable and persistent representation of the environment in real-time using sensor data and prior knowledge. Despite the fast-paced progress in robot perception, most existing methods either build purely geometric maps (as in traditional SLAM) or flat metric-semantic maps that do not scale to large environments or large dictionaries of semantic labels. The first part of this paper is concerned with representations: we show that scalable representations for spatial perception need to be hierarchical in nature. Hierarchical representations are efficient to store, and lead to layered graphs with small treewidth, which enable provably efficient inference. We then introduce an example of hierarchical representation for indoor environments, namely a 3D scene graph, and discuss its structure and properties. The second part of the paper focuses on algorithms to incrementally construct a 3D scene graph as the robot explores the environment. Our algorithms combine 3D geometry, topology (to cluster the places into rooms), and geometric deep learning (e.g., to classify the type of rooms the robot is moving across). The third part of the paper focuses on algorithms to maintain and correct 3D scene graphs during long-term operation. We propose hierarchical descriptors for loop closure detection and describe how to correct a scene graph in response to loop closures, by solving a 3D scene graph optimization problem. We conclude the paper by combining the proposed perception algorithms into Hydra, a real-time spatial perception system that builds a 3D scene graph from visual-inertial data in real-time. We showcase Hydra's performance in photo-realistic simulations and real data collected by a Clearpath Jackal robots and a Unitree A1 robot. We release an open-source implementation of Hydra at https://github.com/MIT-SPARK/Hydra.

## 개요
3D 공간 인식은 센서 데이터와 사전 지식을 활용하여 실시간으로 환경의 실행 가능하고 지속적인 표현을 구축하고 유지하는 문제입니다. 로봇 인식 분야의 빠른 발전에도 불구하고, 대부분의 기존 방법은 순수 기하학적 지도(전통적인 SLAM에서처럼)를 구축하거나, 대규모 환경이나 대규모 의미 레이블 사전에 확장되지 않는 평면적 미터법-의미론적 지도를 구축합니다. 이 논문의 첫 번째 부분은 표현에 관한 것입니다: 우리는 공간 인식을 위한 확장 가능한 표현이 본질적으로 계층적이어야 함을 보여줍니다. 계층적 표현은 저장 효율적이며, 작은 트리 폭을 가진 계층 그래프를 생성하여 증명 가능한 효율적인 추론을 가능하게 합니다. 그런 다음 실내 환경을 위한 계층적 표현의 예, 즉 3D 장면 그래프를 소개하고 그 구조와 속성을 논의합니다. 논문의 두 번째 부분은 로봇이 환경을 탐색하면서 3D 장면 그래프를 점진적으로 구축하는 알고리즘에 초점을 맞춥니다. 우리의 알고리즘은 3D 기하학, 토폴로지(장소를 방으로 클러스터링), 그리고 기하학적 딥러닝(예: 로봇이 이동하는 방의 유형을 분류)을 결합합니다. 논문의 세 번째 부분은 장기 운영 중 3D 장면 그래프를 유지하고 수정하는 알고리즘에 초점을 맞춥니다. 우리는 루프 폐쇄 감지를 위한 계층적 설명자를 제안하고, 3D 장면 그래프 최적화 문제를 해결하여 루프 폐쇄에 대응하여 장면 그래프를 수정하는 방법을 설명합니다. 논문을 마무리하며 제안된 인식 알고리즘을 Hydra에 통합합니다. Hydra는 시각-관성 데이터로부터 실시간으로 3D 장면 그래프를 구축하는 실시간 공간 인식 시스템입니다. 우리는 Hydra의 성능을 사실적인 시뮬레이션과 Clearpath Jackal 로봇 및 Unitree A1 로봇이 수집한 실제 데이터에서 시연합니다. Hydra의 오픈 소스 구현체를 https://github.com/MIT-SPARK/Hydra에서 공개합니다.

## 핵심 내용
3D 공간 인식은 센서 데이터와 사전 지식을 활용하여 실시간으로 환경의 실행 가능하고 지속적인 표현을 구축하고 유지하는 문제입니다. 로봇 인식 분야의 빠른 발전에도 불구하고, 대부분의 기존 방법은 순수 기하학적 지도(전통적인 SLAM에서처럼)를 구축하거나, 대규모 환경이나 대규모 의미 레이블 사전에 확장되지 않는 평면적 미터법-의미론적 지도를 구축합니다. 이 논문의 첫 번째 부분은 표현에 관한 것입니다: 우리는 공간 인식을 위한 확장 가능한 표현이 본질적으로 계층적이어야 함을 보여줍니다. 계층적 표현은 저장 효율적이며, 작은 트리 폭을 가진 계층 그래프를 생성하여 증명 가능한 효율적인 추론을 가능하게 합니다. 그런 다음 실내 환경을 위한 계층적 표현의 예, 즉 3D 장면 그래프를 소개하고 그 구조와 속성을 논의합니다. 논문의 두 번째 부분은 로봇이 환경을 탐색하면서 3D 장면 그래프를 점진적으로 구축하는 알고리즘에 초점을 맞춥니다. 우리의 알고리즘은 3D 기하학, 토폴로지(장소를 방으로 클러스터링), 그리고 기하학적 딥러닝(예: 로봇이 이동하는 방의 유형을 분류)을 결합합니다. 논문의 세 번째 부분은 장기 운영 중 3D 장면 그래프를 유지하고 수정하는 알고리즘에 초점을 맞춥니다. 우리는 루프 폐쇄 감지를 위한 계층적 설명자를 제안하고, 3D 장면 그래프 최적화 문제를 해결하여 루프 폐쇄에 대응하여 장면 그래프를 수정하는 방법을 설명합니다. 논문을 마무리하며 제안된 인식 알고리즘을 Hydra에 통합합니다. Hydra는 시각-관성 데이터로부터 실시간으로 3D 장면 그래프를 구축하는 실시간 공간 인식 시스템입니다. 우리는 Hydra의 성능을 사실적인 시뮬레이션과 Clearpath Jackal 로봇 및 Unitree A1 로봇이 수집한 실제 데이터에서 시연합니다. Hydra의 오픈 소스 구현체를 https://github.com/MIT-SPARK/Hydra에서 공개합니다.
