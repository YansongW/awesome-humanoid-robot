---
$id: ent_paper_taniguchi_autonomous_planning_based_on_s_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Autonomous Planning Based on Spatial Concepts to Tidy Up Home Environments with Service Robots
  zh: 基于空间概念的服务机器人家庭整理自主规划
  ko: 공간 개념에 기반한 서비스 로봇을 이용한 가정 환경 정리 자율 계획
summary:
  en: This paper proposes a likelihood-ratio planning method that learns 3D object-place co-occurrence distributions from
    multimodal observations of a tidied environment, enabling a service robot to decide the order and target positions for
    tidying household objects. The integrated ROS-based system, evaluated on the WRS 2018 Tidy Up Here task in simulation,
    outperformed baseline methods in task score and placement accuracy.
  zh: 本文提出一种基于似然比的规划方法，从整理后环境的多模态观测中学习三维物品-位置共现分布，使服务机器人能够决定家庭物品的整理顺序和目标位置。该基于ROS的集成系统在模拟环境中复现了WRS 2018 Tidy Up Here任务，并在任务得分和放置准确率上优于基线方法。
  ko: 본 논문은 정리된 환경의 다중감각 관측으로부터 3차원 물체-장소 공출현 분포를 학습하는 우도비 계획 방법을 제안하여, 서비스 로봇이 가정 내 물건의 정리 순서와 목표 위치를 결정할 수 있게 한다. ROS 기반
    통합 시스템은 시뮬레이션에서 WRS 2018 Tidy Up Here 과제를 재현하여 평가되었고 기준 방법보다 과제 점수와 배치 정확도에서 우수했다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 02_components
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- spatial_concepts
- tidy_up_planning
- probabilistic_generative_model
- likelihood_ratio_planning
- mobile_manipulation
- service_robot
- home_robotics
- multimodal_learning
- yolov3
- wrs_2018
- ros
- hsr
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2002.03671v2.
sources:
- id: src_001
  type: paper
  title: Autonomous Planning Based on Spatial Concepts to Tidy Up Home Environments with Service Robots
  url: https://arxiv.org/abs/2002.03671
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Tidy-up tasks by service robots in home environments are challenging in robotics applications because they involve various interactions with the environment. In particular, robots are required not only to grasp, move, and release various home objects but also to plan the order and positions for placing the objects. In this paper, we propose a novel planning method that can efficiently estimate the order and positions of the objects to be tidied up by learning the parameters of a probabilistic generative model. The model allows a robot to learn the distributions of the co-occurrence probability of the objects and places to tidy up using the multimodal sensor information collected in a tidied environment. Additionally, we develop an autonomous robotic system to perform the tidy-up operation. We evaluate the effectiveness of the proposed method by an experimental simulation that reproduces the conditions of the Tidy Up Here task of the World Robot Summit 2018 international robotics competition. The simulation results show that the proposed method enables the robot to successively tidy up several objects and achieves the best task score among the considered baseline tidy-up methods.

## 核心内容
Tidy-up tasks by service robots in home environments are challenging in robotics applications because they involve various interactions with the environment. In particular, robots are required not only to grasp, move, and release various home objects but also to plan the order and positions for placing the objects. In this paper, we propose a novel planning method that can efficiently estimate the order and positions of the objects to be tidied up by learning the parameters of a probabilistic generative model. The model allows a robot to learn the distributions of the co-occurrence probability of the objects and places to tidy up using the multimodal sensor information collected in a tidied environment. Additionally, we develop an autonomous robotic system to perform the tidy-up operation. We evaluate the effectiveness of the proposed method by an experimental simulation that reproduces the conditions of the Tidy Up Here task of the World Robot Summit 2018 international robotics competition. The simulation results show that the proposed method enables the robot to successively tidy up several objects and achieves the best task score among the considered baseline tidy-up methods.

## 参考
- http://arxiv.org/abs/2002.03671v2

