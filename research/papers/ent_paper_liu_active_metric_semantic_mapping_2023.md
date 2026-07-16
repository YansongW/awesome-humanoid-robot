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
  en: This paper presents PAMS, an active metric-semantic mapping framework in which multiple heterogeneous aerial robots
    collaboratively build compact object-level maps and select informative viewpoints to reduce both geometric and semantic
    uncertainties. The approach integrates a real-time metric-semantic SLAM system with empirically characterized uncertainty
    models and is validated through real-world multi-robot experiments.
  zh: 本文提出了PAMS，一种主动度量语义建图框架，使多个异构空中机器人协作构建紧凑的对象级地图，并选择信息丰富的视点以降低几何与语义不确定性。该方法将实时度量语义SLAM与经验表征的不确定性模型相结合，并通过真实多机器人实验验证。
  ko: 본 논문은 다수의 이종 공중 로봇이 협력하여 컴팩트한 객체 수준 지도를 구축하고 기하학적 및 의미론적 불확실성을 모두 줄이도록 정보가 풍부한 관점을 선택하는 능동 메트릭-시맨틱 매핑 프레임워크 PAMS를 제안한다.
    실시간 메트릭-시맨틱 SLAM과 실제 데이터로부터 경험적으로 특성화된 불확실성 모델을 통합하고 실제 다중 로봇 실험으로 검증하였다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2209.08465v4.
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
## 概述
Traditional approaches for active mapping focus on building geometric maps. For most real-world applications, however, actionable information is related to semantically meaningful objects in the environment. We propose an approach to the active metric-semantic mapping problem that enables multiple heterogeneous robots to collaboratively build a map of the environment. The robots actively explore to minimize the uncertainties in both semantic (object classification) and geometric (object modeling) information. We represent the environment using informative but sparse object models, each consisting of a basic shape and a semantic class label, and characterize uncertainties empirically using a large amount of real-world data. Given a prior map, we use this model to select actions for each robot to minimize uncertainties. The performance of our algorithm is demonstrated through multi-robot experiments in diverse real-world environments. The proposed framework is applicable to a wide range of real-world problems, such as precision agriculture, infrastructure inspection, and asset mapping in factories. A demo video can be found at https://youtu.be/S86SgXi54oU.

## 核心内容
Traditional approaches for active mapping focus on building geometric maps. For most real-world applications, however, actionable information is related to semantically meaningful objects in the environment. We propose an approach to the active metric-semantic mapping problem that enables multiple heterogeneous robots to collaboratively build a map of the environment. The robots actively explore to minimize the uncertainties in both semantic (object classification) and geometric (object modeling) information. We represent the environment using informative but sparse object models, each consisting of a basic shape and a semantic class label, and characterize uncertainties empirically using a large amount of real-world data. Given a prior map, we use this model to select actions for each robot to minimize uncertainties. The performance of our algorithm is demonstrated through multi-robot experiments in diverse real-world environments. The proposed framework is applicable to a wide range of real-world problems, such as precision agriculture, infrastructure inspection, and asset mapping in factories. A demo video can be found at https://youtu.be/S86SgXi54oU.

## 参考
- http://arxiv.org/abs/2209.08465v4

## Overview
Traditional approaches for active mapping focus on building geometric maps. For most real-world applications, however, actionable information is related to semantically meaningful objects in the environment. We propose an approach to the active metric-semantic mapping problem that enables multiple heterogeneous robots to collaboratively build a map of the environment. The robots actively explore to minimize the uncertainties in both semantic (object classification) and geometric (object modeling) information. We represent the environment using informative but sparse object models, each consisting of a basic shape and a semantic class label, and characterize uncertainties empirically using a large amount of real-world data. Given a prior map, we use this model to select actions for each robot to minimize uncertainties. The performance of our algorithm is demonstrated through multi-robot experiments in diverse real-world environments. The proposed framework is applicable to a wide range of real-world problems, such as precision agriculture, infrastructure inspection, and asset mapping in factories. A demo video can be found at https://youtu.be/S86SgXi54oU.

## Content
Traditional approaches for active mapping focus on building geometric maps. For most real-world applications, however, actionable information is related to semantically meaningful objects in the environment. We propose an approach to the active metric-semantic mapping problem that enables multiple heterogeneous robots to collaboratively build a map of the environment. The robots actively explore to minimize the uncertainties in both semantic (object classification) and geometric (object modeling) information. We represent the environment using informative but sparse object models, each consisting of a basic shape and a semantic class label, and characterize uncertainties empirically using a large amount of real-world data. Given a prior map, we use this model to select actions for each robot to minimize uncertainties. The performance of our algorithm is demonstrated through multi-robot experiments in diverse real-world environments. The proposed framework is applicable to a wide range of real-world problems, such as precision agriculture, infrastructure inspection, and asset mapping in factories. A demo video can be found at https://youtu.be/S86SgXi54oU.

## 개요
전통적인 능동 매핑 접근법은 기하학적 지도 구축에 중점을 둡니다. 그러나 대부분의 실제 응용에서 실행 가능한 정보는 환경 내 의미론적으로 의미 있는 객체와 관련됩니다. 우리는 다수의 이종 로봇이 협력하여 환경 지도를 구축할 수 있도록 하는 능동적 메트릭-의미론 매핑 문제에 대한 접근법을 제안합니다. 로봇은 의미론적(객체 분류) 및 기하학적(객체 모델링) 정보의 불확실성을 최소화하기 위해 능동적으로 탐색합니다. 우리는 환경을 기본 형태와 의미론적 클래스 레이블로 구성된 정보성 있지만 희소한 객체 모델로 표현하고, 대량의 실제 데이터를 사용하여 경험적으로 불확실성을 특성화합니다. 사전 지도가 주어지면 이 모델을 사용하여 각 로봇의 행동을 선택하여 불확실성을 최소화합니다. 우리 알고리즘의 성능은 다양한 실제 환경에서의 다중 로봇 실험을 통해 입증됩니다. 제안된 프레임워크는 정밀 농업, 인프라 검사, 공장 내 자산 매핑과 같은 다양한 실제 문제에 적용 가능합니다. 데모 비디오는 https://youtu.be/S86SgXi54oU에서 확인할 수 있습니다.

## 핵심 내용
전통적인 능동 매핑 접근법은 기하학적 지도 구축에 중점을 둡니다. 그러나 대부분의 실제 응용에서 실행 가능한 정보는 환경 내 의미론적으로 의미 있는 객체와 관련됩니다. 우리는 다수의 이종 로봇이 협력하여 환경 지도를 구축할 수 있도록 하는 능동적 메트릭-의미론 매핑 문제에 대한 접근법을 제안합니다. 로봇은 의미론적(객체 분류) 및 기하학적(객체 모델링) 정보의 불확실성을 최소화하기 위해 능동적으로 탐색합니다. 우리는 환경을 기본 형태와 의미론적 클래스 레이블로 구성된 정보성 있지만 희소한 객체 모델로 표현하고, 대량의 실제 데이터를 사용하여 경험적으로 불확실성을 특성화합니다. 사전 지도가 주어지면 이 모델을 사용하여 각 로봇의 행동을 선택하여 불확실성을 최소화합니다. 우리 알고리즘의 성능은 다양한 실제 환경에서의 다중 로봇 실험을 통해 입증됩니다. 제안된 프레임워크는 정밀 농업, 인프라 검사, 공장 내 자산 매핑과 같은 다양한 실제 문제에 적용 가능합니다. 데모 비디오는 https://youtu.be/S86SgXi54oU에서 확인할 수 있습니다.
