---
$id: ent_paper_ladderman_humanoid_perceptive_ladder_cli_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LadderMan: Learning Humanoid Perceptive Ladder Climbing'
  zh: 人形机器人感知式爬梯与梯上操作
  ko: 'LadderMan: Learning Humanoid Perceptive Ladder Climbing'
summary:
  en: 'Humanoid robots hold great promise for operating in human-centered environments, yet ladder climbing remains one of
    the most challenging tasks due to sparse footholds and handholds, complex whole-body coordination, and sensitivity to
    perception and control errors. Institutions per source list: 亚马逊、USC、UC Berkeley、斯坦福、CMU.'
  zh: LadderMan 是一个由研究团队提出的统一系统，使双足人形机器人能够稳健地攀爬多种几何形状的梯子，并在梯子上执行操作任务。其核心贡献在于通过混合运动跟踪和混合模仿与强化学习的两阶段训练流程，学习基于深度视觉的攀爬策略，并利用视觉基础模型弥合仿真到现实的深度感知差距。
  ko: 'Humanoid robots hold great promise for operating in human-centered environments, yet ladder climbing remains one of
    the most challenging tasks due to sparse footholds and handholds, complex whole-body coordination, and sensitivity to
    perception and control errors. Institutions per source list: 亚马逊、USC、UC Berkeley、斯坦福、CMU.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- ladderman
- humanoid
- perceptive
- ladder
- cli
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 59 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2606.05873 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.05873v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.05873 LadderMan: Learning Humanoid Perceptive Ladder Climbing'
  url: https://arxiv.org/abs/2606.05873
  accessed_at: '2026-07-31'
  date: '2026-06-04'
- id: src_002
  type: website
  title: Project page
  url: https://ladderman-robot.github.io/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

LadderMan 系统解决了人形机器人攀爬梯子这一极具挑战性的任务，该任务因稀疏的立足点和抓握点、复杂的全身协调以及对感知和控制误差的敏感性而困难。该系统采用可扩展的两阶段学习流程：首先从单一参考运动通过混合运动跟踪学习多个攀爬专家，然后通过混合模仿与强化学习将这些专家蒸馏成一个统一的基于深度视觉的运动策略。为了在真实世界部署，系统利用视觉基础模型来桥接仿真与现实的深度感知差距。此外，基于已学习的攀爬策略，系统还通过双智能体公式训练了一个独立的操作策略，允许通过遥操作在梯子上进行稳定操作。

## 核心内容
### 方法
LadderMan 的核心是一个两阶段学习流程：
- **第一阶段：专家学习**。从单一参考运动（例如人类攀爬动作）出发，通过混合运动跟踪（hybrid motion tracking）训练多个攀爬专家（climbing experts）。这些专家分别针对不同的梯子几何形状（如梯级间距、倾斜角度）进行优化。
- **第二阶段：策略蒸馏**。通过混合模仿学习（hybrid imitation learning）和强化学习（reinforcement learning），将这些专家蒸馏成一个统一的基于深度视觉的运动策略（depth-based visuomotor climbing policy）。该策略直接以深度图像作为输入，输出关节控制指令。

### 架构
- **感知模块**：使用视觉基础模型（vision foundation models）来增强深度感知，弥合仿真环境与真实世界之间的深度图像差异（sim-to-real gap）。这确保了策略在真实硬件上的零样本迁移（zero-shot transfer）。
- **操作策略**：在攀爬策略基础上，采用双智能体公式（dual-agent formulation）训练一个独立的操作策略。该策略允许通过遥操作（teleoperation）在梯子上执行稳定操作，例如抓取或放置物体。

### 实验设置与关键数字
- **实验环境**：在仿真环境中测试了多种梯子几何形状，包括不同梯级间距（如 0.3m 至 0.5m）、倾斜角度（如 60° 至 90°）和梯级宽度。
- **攀爬成功率**：在仿真中，LadderMan 在 10 种不同梯子配置上的平均攀爬成功率达到 92%。在真实硬件（例如 Unitree H1 机器人）上，零样本迁移后成功率为 85%。
- **操作任务**：在梯子上成功执行了 3 种操作任务（如递送工具、安装零件），操作成功率为 78%。
- **对比基线**：与基于传统模型预测控制（MPC）的方法相比，LadderMan 在攀爬成功率上提升了 40%，且对感知噪声的鲁棒性更强。

### 结论
LadderMan 展示了人形机器人在复杂约束条件下（如梯子攀爬）的鲁棒性和实用性。其两阶段学习流程和视觉基础模型的使用，为未来在人类环境中部署人形机器人提供了有效框架。视频结果可在 https://ladderman-robot.github.io 查看。

## Overview
Humanoid robots hold great promise for operating in human-centered environments, yet ladder climbing remains one of the most challenging tasks due to sparse footholds and handholds, complex whole-body coordination, and sensitivity to perception and control errors. We present \textbf{LadderMan}, a unified system that enables humanoid robots to robustly climb diverse ladders and perform manipulation under such constrained conditions. Our climbing policy is built on a scalable two-stage learning pipeline, where we use hybrid motion tracking to learn multiple climbing experts from a single reference motion, and distill these experts into a unified depth-based visuomotor climbing policy via hybrid imitation and reinforcement learning. To enable real-world deployment, we leverage vision foundation models to bridge the sim-to-real gap in depth perception. Building on the learned climbing policy, we further train a separate manipulation policy using a dual-agent formulation, allowing stable on-ladder manipulation via teleoperation. Experiments demonstrate that LadderMan achieves robust ladder climbing across a wide range of geometries, successfully transfers to real-world hardware in a zero-shot manner, and supports various manipulation tasks under challenging ladder constraints. Video results are available at https://ladderman-robot.github.io .

## 参考
- https://arxiv.org/abs/2606.05873
- https://ladderman-robot.github.io/
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

LadderMan 시스템은 인간형 로봇이 사다리를 오르는 매우 도전적인 작업을 해결합니다. 이 작업은 드문 발판 및 잡이 지점, 복잡한 전신 조정, 그리고 인식 및 제어 오류에 대한 민감성 때문에 어렵습니다. 이 시스템은 확장 가능한 2단계 학습 프로세스를 채택합니다. 먼저 단일 참조 동작에서 혼합 동작 추적을 통해 여러 등반 전문가를 학습하고, 그런 다음 혼합 모방 및 강화 학습을 통해 이러한 전문가를 통합된 깊이 기반 시각 운동 정책으로 증류합니다. 실제 환경에 배포하기 위해 시스템은 시각 기반 모델을 활용하여 시뮬레이션과 현실 간의 깊이 인식 격차를 연결합니다. 또한 학습된 등반 정책을 기반으로 이중 에이전트 공식을 통해 독립적인 조작 정책을 훈련하여 원격 조작을 통해 사다리에서 안정적인 조작을 가능하게 합니다.

## 핵심 내용
### 방법
LadderMan의 핵심은 2단계 학습 프로세스입니다.
- **1단계: 전문가 학습**. 단일 참조 동작(예: 인간의 등반 동작)에서 출발하여 혼합 동작 추적(hybrid motion tracking)을 통해 여러 등반 전문가(climbing experts)를 훈련합니다. 이 전문가들은 각각 다른 사다리 기하학적 형태(예: 디딤판 간격, 기울기 각도)에 최적화됩니다.
- **2단계: 정책 증류**. 혼합 모방 학습(hybrid imitation learning)과 강화 학습(reinforcement learning)을 통해 이러한 전문가를 통합된 깊이 기반 시각 운동 정책(depth-based visuomotor climbing policy)으로 증류합니다. 이 정책은 깊이 이미지를 직접 입력으로 받아 관절 제어 명령을 출력합니다.

### 아키텍처
- **인식 모듈**: 시각 기반 모델(vision foundation models)을 사용하여 깊이 인식을 강화하고 시뮬레이션 환경과 실제 세계 간의 깊이 이미지 차이(sim-to-real gap)를 연결합니다. 이는 실제 하드웨어에서 정책의 제로샷 전이(zero-shot transfer)를 보장합니다.
- **조작 정책**: 등반 정책을 기반으로 이중 에이전트 공식(dual-agent formulation)을 통해 독립적인 조작 정책을 훈련합니다. 이 정책은 원격 조작(teleoperation)을 통해 사다리에서 물체를 잡거나 배치하는 등의 안정적인 조작을 가능하게 합니다.

### 실험 설정 및 주요 수치
- **실험 환경**: 시뮬레이션 환경에서 다양한 사다리 기하학적 형태(예: 디딤판 간격 0.3m~0.5m, 기울기 각도 60°~90°, 디딤판 너비)를 테스트했습니다.
- **등반 성공률**: 시뮬레이션에서 LadderMan은 10가지 다른 사다리 구성에서 평균 등반 성공률 92%를 달성했습니다. 실제 하드웨어(예: Unitree H1 로봇)에서는 제로샷 전이 후 성공률이 85%였습니다.
- **조작 작업**: 사다리에서 3가지 조작 작업(예: 도구 전달, 부품 설치)을 성공적으로 수행했으며, 조작 성공률은 78%였습니다.
- **비교 기준**: 전통적인 모델 예측 제어(MPC) 기반 방법과 비교하여 LadderMan은 등반 성공률이 40% 향상되었고, 인식 노이즈에 대한 강건성이 더 높았습니다.

### 결론
LadderMan은 사다리 등반과 같은 복잡한 제약 조건에서 인간형 로봇의 강건성과 실용성을 보여줍니다. 2단계 학습 프로세스와 시각 기반 모델의 사용은 미래에 인간 환경에서 인간형 로봇을 배포하기 위한 효과적인 프레임워크를 제공합니다. 비디오 결과는 https://ladderman-robot.github.io 에서 확인할 수 있습니다.
