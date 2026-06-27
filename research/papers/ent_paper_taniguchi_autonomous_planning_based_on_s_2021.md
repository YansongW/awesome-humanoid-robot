---
$id: ent_paper_taniguchi_autonomous_planning_based_on_s_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Autonomous Planning Based on Spatial Concepts to Tidy Up Home Environments with
    Service Robots
  zh: 基于空间概念的服务机器人家庭整理自主规划
  ko: 공간 개념에 기반한 서비스 로봇을 이용한 가정 환경 정리 자율 계획
summary:
  en: This paper proposes a likelihood-ratio planning method that learns 3D object-place
    co-occurrence distributions from multimodal observations of a tidied environment,
    enabling a service robot to decide the order and target positions for tidying
    household objects. The integrated ROS-based system, evaluated on the WRS 2018
    Tidy Up Here task in simulation, outperformed baseline methods in task score and
    placement accuracy.
  zh: 本文提出一种基于似然比的规划方法，从整理后环境的多模态观测中学习三维物品-位置共现分布，使服务机器人能够决定家庭物品的整理顺序和目标位置。该基于ROS的集成系统在模拟环境中复现了WRS
    2018 Tidy Up Here任务，并在任务得分和放置准确率上优于基线方法。
  ko: 본 논문은 정리된 환경의 다중감각 관측으로부터 3차원 물체-장소 공출현 분포를 학습하는 우도비 계획 방법을 제안하여, 서비스 로봇이 가정
    내 물건의 정리 순서와 목표 위치를 결정할 수 있게 한다. ROS 기반 통합 시스템은 시뮬레이션에서 WRS 2018 Tidy Up Here
    과제를 재현하여 평가되었고 기준 방법보다 과제 점수와 배치 정확도에서 우수했다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; full-text verification,
    DOI resolution, and human review are still required.
sources:
- id: src_001
  type: paper
  title: Autonomous Planning Based on Spatial Concepts to Tidy Up Home Environments
    with Service Robots
  url: https://arxiv.org/abs/2002.03671
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper addresses autonomous tidy-up planning for service robots in home environments, where a robot must both manipulate objects and decide the order and final placement of multiple scattered items. The authors formulate the problem as learning the spatial concepts of a tidied environment from multimodal sensor observations, including 3D positions, camera images, and place-name words. A probabilistic generative model captures the co-occurrence distributions of objects and places, allowing the robot to infer where each object belongs. From this learned model, a likelihood-ratio objective selects the next object to tidy and its target position by prioritizing objects whose tidied location is most clearly defined.

The planning method is integrated into a complete autonomous robotic system running ROS Kinetic. The system combines RGB-D perception, SLAM (Hector SLAM/AMCL/RTAB-Map), occupancy mapping (Octomap), YOLOv3 object detection, and MoveIt! manipulation planning, together with speech interaction. Experiments are conducted in Gazebo simulation using a Toyota Human Support Robot, reproducing the conditions of the World Robot Summit 2018 Tidy Up Here task.

Evaluation compares the proposed method against baseline tidy-up strategies. Results show that the likelihood-ratio planner enables the robot to tidy several objects successively and achieves the best task score among the considered baselines, with higher placement accuracy.

## Key Contributions

- Novel likelihood-ratio planning objective that selects the next object and its target position by maximizing the clarity of the learned object-place association.
- Probabilistic generative model for spatial concept formation in 3D space, learned from object positions, images, and place-name words.
- Integrated autonomous service-robot system combining ROS, RGB-D perception, SLAM, manipulation planning, object detection, and speech interaction.
- Simulation evaluation on the WRS 2018 Tidy Up Here task showing higher task scores and accuracy than baseline methods.

## Relevance to Humanoid Robotics

Although the experiments use the Toyota Human Support Robot, the core capabilities developed—autonomous perception of cluttered home scenes, semantic spatial-concept learning, task-and-motion planning for manipulation, and human-robot interaction—are directly transferable to general-purpose humanoid service robots. Tidy-up is a representative domestic application that requires the full stack of perception, reasoning, and dexterous manipulation needed for mass-market humanoid deployment. The paper therefore contributes both an AI planning method and an integrated system architecture relevant to humanoid domestic robotics.
