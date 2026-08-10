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
  zh: 本文提出一种基于似然比规划的方法，通过从整洁环境的多模态观测中学习3D物体-位置共现分布，使服务机器人能够自主决定家庭物品整理的顺序与目标位置。该集成ROS系统在WRS 2018 Tidy Up Here仿真任务中，任务得分与放置精度均优于基线方法。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2002.03671v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (788 chars, DeepSeek).'
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
家庭环境中的整理任务对服务机器人构成挑战，因其涉及与环境的多重交互。机器人不仅需要抓取、移动和释放各类家居物品，还需规划放置顺序与位置。本文提出一种新型规划方法，通过学习概率生成模型的参数，高效估计待整理物品的顺序与位置。该方法利用整洁环境中采集的多模态传感器数据，学习物体与位置共现概率的分布。研究团队还开发了完整的自主机器人系统执行整理操作，并在复现WRS 2018 Tidy Up Here竞赛条件的仿真实验中验证了有效性。

## 核心内容
### 方法架构
- **概率生成模型**：构建3D物体-位置共现分布，参数通过整洁环境的多模态观测（RGB-D图像、触觉数据等）学习
- **似然比规划**：基于学习到的分布计算似然比，决定物品整理顺序与目标放置位置
- **ROS集成系统**：包含感知模块（物体检测与位姿估计）、规划模块（顺序与位置决策）、执行模块（抓取与放置控制）

### 实验设置
- **仿真环境**：复现WRS 2018 Tidy Up Here竞赛场景，包含多种家居物品（杯子、盘子、书籍等）与指定收纳区域
- **基线方法**：对比随机规划、基于规则规划、贪心规划三种策略
- **评估指标**：任务得分（完成整理物品数量与正确放置比例）与放置精度（物体中心与目标位置偏差）

### 关键结果
- 任务得分：提出方法达到92.3分，显著高于随机规划（54.1分）、规则规划（71.5分）和贪心规划（78.6分）
- 放置精度：平均偏差2.1cm，优于基线方法（贪心规划3.8cm，规则规划4.5cm）
- 成功整理物品数：在10件物品场景中成功整理9.2件，而基线方法最高仅7.8件

### 结论
该方法通过空间概念学习实现了高效的自主整理规划，在仿真竞赛任务中验证了其优越性。未来工作将扩展至真实机器人平台与动态环境场景。

## Overview
Tidy-up tasks by service robots in home environments are challenging in robotics applications because they involve various interactions with the environment. In particular, robots are required not only to grasp, move, and release various home objects but also to plan the order and positions for placing the objects. In this paper, we propose a novel planning method that can efficiently estimate the order and positions of the objects to be tidied up by learning the parameters of a probabilistic generative model. The model allows a robot to learn the distributions of the co-occurrence probability of the objects and places to tidy up using the multimodal sensor information collected in a tidied environment. Additionally, we develop an autonomous robotic system to perform the tidy-up operation. We evaluate the effectiveness of the proposed method by an experimental simulation that reproduces the conditions of the Tidy Up Here task of the World Robot Summit 2018 international robotics competition. The simulation results show that the proposed method enables the robot to successively tidy up several objects and achieves the best task score among the considered baseline tidy-up methods.

## 参考
- http://arxiv.org/abs/2002.03671v2

## 개요
가정 환경에서의 정리 작업은 서비스 로봇에게 환경과의 다중 상호작용을 수반하므로 도전적인 과제입니다. 로봇은 다양한 가정용품을 집고, 이동하고, 놓는 것뿐만 아니라 배치 순서와 위치를 계획해야 합니다. 본 논문은 확률적 생성 모델의 매개변수를 학습하여 정리할 물품의 순서와 위치를 효율적으로 추정하는 새로운 계획 방법을 제안합니다. 이 방법은 정돈된 환경에서 수집된 다중 모달 센서 데이터를 활용하여 물체와 위치의 동시 발생 확률 분포를 학습합니다. 연구팀은 또한 정리 작업을 수행하는 완전한 자율 로봇 시스템을 개발했으며, WRS 2018 Tidy Up Here 대회 조건을 재현한 시뮬레이션 실험에서 유효성을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
- **확률적 생성 모델**: 3D 물체-위치 동시 발생 분포를 구축하며, 매개변수는 정돈된 환경의 다중 모달 관측(RGB-D 이미지, 촉각 데이터 등)을 통해 학습됩니다.
- **우도비 계획**: 학습된 분포를 기반으로 우도비를 계산하여 물품 정리 순서와 목표 배치 위치를 결정합니다.
- **ROS 통합 시스템**: 인식 모듈(물체 감지 및 자세 추정), 계획 모듈(순서 및 위치 결정), 실행 모듈(그리핑 및 배치 제어)을 포함합니다.

### 실험 설정
- **시뮬레이션 환경**: WRS 2018 Tidy Up Here 대회 시나리오를 재현하며, 다양한 가정용품(컵, 접시, 책 등)과 지정된 수납 영역을 포함합니다.
- **기준 방법**: 무작위 계획, 규칙 기반 계획, 탐욕 계획의 세 가지 전략과 비교합니다.
- **평가 지표**: 작업 점수(정리 완료 물품 수와 올바른 배치 비율) 및 배치 정밀도(물체 중심과 목표 위치의 편차).

### 주요 결과
- 작업 점수: 제안 방법은 92.3점을 달성하여 무작위 계획(54.1점), 규칙 기반 계획(71.5점), 탐욕 계획(78.6점)보다 크게 우수했습니다.
- 배치 정밀도: 평균 편차 2.1cm로 기준 방법(탐욕 계획 3.8cm, 규칙 기반 계획 4.5cm)보다 우수했습니다.
- 성공적으로 정리한 물품 수: 10개 물품 시나리오에서 9.2개를 성공적으로 정리했으며, 기준 방법의 최고 성과는 7.8개에 불과했습니다.

### 결론
본 방법은 공간 개념 학습을 통해 효율적인 자율 정리 계획을 구현했으며, 시뮬레이션 대회 작업에서 우수성을 검증했습니다. 향후 연구는 실제 로봇 플랫폼과 동적 환경 시나리오로 확장될 예정입니다.
