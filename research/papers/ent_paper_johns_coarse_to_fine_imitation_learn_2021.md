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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2105.06411v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (587 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2105.06411v2

## 개요
이 방법은 조작 작업을 대략적인 접근 궤적과 정밀한 상호작용 궤적의 두 단계로 분해합니다. 자기 지도 방식으로 상태 추정기를 훈련하여 엔드 이펙터 카메라를 물체 주위로 자동으로 이동시키며 데이터를 수집합니다. 테스트 시에는 엔드 이펙터가 선형 경로를 따라 추정된 상태로 이동한 후, 원본 시연의 엔드 이펙터 속도를 직접 재생하여 명시적인 정책 학습 없이도 복잡한 상호작용 궤적을 얻습니다. 8가지 일상 작업에 대한 실제 실험에서 이 방법이 단일 시연으로 다양한 기술을 학습하면서도 안정적이고 해석 가능한 제어기를 생성함을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- 모방 학습을 상태 추정 문제로 모델링하며, 상태는 시연에서 물체 상호작용이 시작될 때의 엔드 이펙터 자세(병목 자세)로 정의됩니다.
- 조작 작업은 두 단계로 분해됩니다:
  - 대략적인 접근 궤적: 엔드 이펙터가 초기 위치에서 병목 자세로 이동
  - 정밀한 상호작용 궤적: 병목 자세에서 시연된 엔드 이펙터 속도 재생

### 훈련 메커니즘
- 상태 추정기는 자기 지도 방식으로 훈련됩니다: 엔드 이펙터 카메라를 물체 주위로 자동 이동시켜 다양한 시점의 데이터를 수집
- 상호작용 대상에 대한 사전 지식이 전혀 필요 없음

### 테스트 절차
- 엔드 이펙터가 선형 경로를 따라 추정된 병목 자세로 이동
- 해당 자세에서 원본 시연에 기록된 엔드 이펙터 속도를 직접 재생
- 명시적인 정책 네트워크 학습이 필요 없어 복잡한 상호작용 궤적 획득이 단순화됨

### 실험 설정 및 결과
- 8가지 일상 조작 작업에 대한 실제 실험 수행
- 다양한 기술(예: 잡기, 밀기/당기기, 회전 등)을 성공적으로 학습
- 제어기는 안정성과 해석 가능성을 갖춤
- 핵심 장점: 단일 시연으로 학습 가능하며 대규모 데이터 수집이 필요 없음
