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

## Overview
Tidy-up tasks by service robots in home environments are challenging in robotics applications because they involve various interactions with the environment. In particular, robots are required not only to grasp, move, and release various home objects but also to plan the order and positions for placing the objects. In this paper, we propose a novel planning method that can efficiently estimate the order and positions of the objects to be tidied up by learning the parameters of a probabilistic generative model. The model allows a robot to learn the distributions of the co-occurrence probability of the objects and places to tidy up using the multimodal sensor information collected in a tidied environment. Additionally, we develop an autonomous robotic system to perform the tidy-up operation. We evaluate the effectiveness of the proposed method by an experimental simulation that reproduces the conditions of the Tidy Up Here task of the World Robot Summit 2018 international robotics competition. The simulation results show that the proposed method enables the robot to successively tidy up several objects and achieves the best task score among the considered baseline tidy-up methods.

## Content
Tidy-up tasks by service robots in home environments are challenging in robotics applications because they involve various interactions with the environment. In particular, robots are required not only to grasp, move, and release various home objects but also to plan the order and positions for placing the objects. In this paper, we propose a novel planning method that can efficiently estimate the order and positions of the objects to be tidied up by learning the parameters of a probabilistic generative model. The model allows a robot to learn the distributions of the co-occurrence probability of the objects and places to tidy up using the multimodal sensor information collected in a tidied environment. Additionally, we develop an autonomous robotic system to perform the tidy-up operation. We evaluate the effectiveness of the proposed method by an experimental simulation that reproduces the conditions of the Tidy Up Here task of the World Robot Summit 2018 international robotics competition. The simulation results show that the proposed method enables the robot to successively tidy up several objects and achieves the best task score among the considered baseline tidy-up methods.

## 개요
가정 환경에서 서비스 로봇의 정리 작업은 환경과의 다양한 상호작용을 포함하기 때문에 로봇 공학 응용 분야에서 도전적인 과제입니다. 특히 로봇은 다양한 가정용 물체를 잡고, 이동하고, 놓는 것뿐만 아니라 물체를 배치할 순서와 위치를 계획해야 합니다. 본 논문에서는 확률적 생성 모델의 매개변수를 학습하여 정리할 물체의 순서와 위치를 효율적으로 추정할 수 있는 새로운 계획 방법을 제안합니다. 이 모델은 로봇이 정리된 환경에서 수집된 다중 모달 센서 정보를 사용하여 물체와 정리할 장소의 동시 발생 확률 분포를 학습할 수 있게 합니다. 또한 정리 작업을 수행하기 위한 자율 로봇 시스템을 개발합니다. 제안된 방법의 효과를 World Robot Summit 2018 국제 로봇 경진대회의 Tidy Up Here 과제 조건을 재현한 실험 시뮬레이션을 통해 평가합니다. 시뮬레이션 결과는 제안된 방법이 로봇이 여러 물체를 연속적으로 정리할 수 있게 하며, 고려된 기준 정리 방법 중 최고의 작업 점수를 달성함을 보여줍니다.

## 핵심 내용
가정 환경에서 서비스 로봇의 정리 작업은 환경과의 다양한 상호작용을 포함하기 때문에 로봇 공학 응용 분야에서 도전적인 과제입니다. 특히 로봇은 다양한 가정용 물체를 잡고, 이동하고, 놓는 것뿐만 아니라 물체를 배치할 순서와 위치를 계획해야 합니다. 본 논문에서는 확률적 생성 모델의 매개변수를 학습하여 정리할 물체의 순서와 위치를 효율적으로 추정할 수 있는 새로운 계획 방법을 제안합니다. 이 모델은 로봇이 정리된 환경에서 수집된 다중 모달 센서 정보를 사용하여 물체와 정리할 장소의 동시 발생 확률 분포를 학습할 수 있게 합니다. 또한 정리 작업을 수행하기 위한 자율 로봇 시스템을 개발합니다. 제안된 방법의 효과를 World Robot Summit 2018 국제 로봇 경진대회의 Tidy Up Here 과제 조건을 재현한 실험 시뮬레이션을 통해 평가합니다. 시뮬레이션 결과는 제안된 방법이 로봇이 여러 물체를 연속적으로 정리할 수 있게 하며, 고려된 기준 정리 방법 중 최고의 작업 점수를 달성함을 보여줍니다.
