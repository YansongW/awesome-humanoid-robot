---
$id: ent_paper_johns_coarse_to_fine_imitation_learn_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration'
  zh: 从粗到精的模仿学习：单演示下的机器人操作
  ko: 'Coarse-to-Fine 모방 학습: 단일 시연으로부터의 로봇 조작'
summary:
  en: Johns (2021) proposes a visual imitation-learning method that learns a novel manipulation task from a single human demonstration
    by estimating the end-effector's bottleneck pose and replaying the demonstration's end-effector velocities from that pose.
  zh: Johns (2021) 提出一种视觉模仿学习方法，通过估计末端执行器在物体交互开始时的瓶颈位姿，并重放该位姿下的末端执行器速度，实现从单次人类演示中学习新型机器人操作任务。该方法将模仿学习建模为状态估计问题，无需预先了解交互对象。
  ko: Johns(2021)은 엔드이펙터의 병목 자세를 추정하고 해당 자세부터 시연의 엔드이펙터 속도를 재생함으로써 단일 인간 시연으로부터 새로운 조작 작업을 학습하는 시각적 모방 학습 방법을 제안한다.
domains:
- 07_ai_models_algorithms
- 04_assembly_integration_testing
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- imitation_learning
- single_demonstration_learning
- visual_imitation
- bottleneck_pose_estimation
- end_effector_velocity_replay
- self_supervised_learning
- manipulation
- sawyer_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2105.06411v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration'
  url: https://arxiv.org/abs/2105.06411
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该方法将操作任务分解为粗放接近轨迹和精细交互轨迹两个阶段。通过自监督方式训练状态估计器，自动移动末端执行器相机围绕物体采集数据。测试时，末端执行器沿线性路径移动到估计状态，然后直接重放原始演示的末端执行器速度，从而获得复杂交互轨迹而无需显式学习策略。在8种日常任务上的真实世界实验表明，该方法能从单次演示中学习多样化技能，同时产生稳定且可解释的控制器。

## 核心内容
### 方法架构
- 将模仿学习建模为状态估计问题，状态定义为演示中物体交互开始时的末端执行器位姿（bottleneck pose）
- 操作任务分解为两个阶段：
  - 粗放接近轨迹：末端执行器从初始位置移动到瓶颈位姿
  - 精细交互轨迹：从瓶颈位姿开始重放演示的末端执行器速度

### 训练机制
- 状态估计器通过自监督方式训练：自动移动末端执行器相机围绕物体采集不同视角数据
- 无需任何关于交互对象的先验知识

### 测试流程
- 末端执行器沿线性路径移动到估计的瓶颈位姿
- 从该位姿开始直接重放原始演示记录的末端执行器速度
- 无需显式学习策略网络，简化了复杂交互轨迹的获取

### 实验设置与结果
- 在8种日常操作任务上进行真实世界实验
- 成功学习多样化技能（如抓取、推拉、旋转等）
- 控制器具有稳定性和可解释性
- 关键优势：单次演示即可学习，无需大量数据收集

## Overview
We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the point where object interaction begins, as observed from the demonstration. By then modelling a manipulation task as a coarse, approach trajectory followed by a fine, interaction trajectory, this state estimator can be trained in a self-supervised manner, by automatically moving the end-effector's camera around the object. At test time, the end-effector moves to the estimated state through a linear path, at which point the original demonstration's end-effector velocities are simply replayed. This enables convenient acquisition of a complex interaction trajectory, without actually needing to explicitly learn a policy. Real-world experiments on 8 everyday tasks show that our method can learn a diverse range of skills from a single human demonstration, whilst also yielding a stable and interpretable controller.

## 개요
우리는 단일 인간 시연으로부터 새로운 로봇 조작 작업을 학습할 수 있는 간단한 시각적 모방 학습 방법을 소개합니다. 이 방법은 상호작용 대상 객체에 대한 사전 지식 없이도 작동합니다. 우리의 방법은 모방 학습을 상태 추정 문제로 모델링하며, 상태는 시연에서 관찰된 객체 상호작용이 시작되는 지점의 엔드 이펙터(end-effector) 자세로 정의됩니다. 조작 작업을 대략적인 접근 궤적과 세밀한 상호작용 궤적으로 모델링함으로써, 이 상태 추정기는 엔드 이펙터의 카메라를 객체 주위로 자동 이동시켜 자기 지도 방식으로 훈련될 수 있습니다. 테스트 시에는 엔드 이펙터가 선형 경로를 통해 추정된 상태로 이동하며, 그 시점에서 원래 시연의 엔드 이펙터 속도가 단순히 재생됩니다. 이를 통해 명시적으로 정책을 학습할 필요 없이 복잡한 상호작용 궤적을 편리하게 획득할 수 있습니다. 8가지 일상 작업에 대한 실제 실험 결과, 우리의 방법은 단일 인간 시연으로부터 다양한 기술을 학습할 수 있을 뿐만 아니라 안정적이고 해석 가능한 제어기를 제공함을 보여줍니다.

## 핵심 내용
우리는 단일 인간 시연으로부터 새로운 로봇 조작 작업을 학습할 수 있는 간단한 시각적 모방 학습 방법을 소개합니다. 이 방법은 상호작용 대상 객체에 대한 사전 지식 없이도 작동합니다. 우리의 방법은 모방 학습을 상태 추정 문제로 모델링하며, 상태는 시연에서 관찰된 객체 상호작용이 시작되는 지점의 엔드 이펙터 자세로 정의됩니다. 조작 작업을 대략적인 접근 궤적과 세밀한 상호작용 궤적으로 모델링함으로써, 이 상태 추정기는 엔드 이펙터의 카메라를 객체 주위로 자동 이동시켜 자기 지도 방식으로 훈련될 수 있습니다. 테스트 시에는 엔드 이펙터가 선형 경로를 통해 추정된 상태로 이동하며, 그 시점에서 원래 시연의 엔드 이펙터 속도가 단순히 재생됩니다. 이를 통해 명시적으로 정책을 학습할 필요 없이 복잡한 상호작용 궤적을 편리하게 획득할 수 있습니다. 8가지 일상 작업에 대한 실제 실험 결과, 우리의 방법은 단일 인간 시연으로부터 다양한 기술을 학습할 수 있을 뿐만 아니라 안정적이고 해석 가능한 제어기를 제공함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2105.06411v2
