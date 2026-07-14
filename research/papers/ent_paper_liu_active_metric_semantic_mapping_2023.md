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

