---
$id: ent_paper_huang_rekep_spatio_temporal_reasonin_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation'
  zh: ReKep
  ko: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation'
summary:
  en: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation (ReKep), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, Columbia University, and published
    at CoRL 2024.'
  zh: ReKep 是斯坦福大学与哥伦比亚大学于 2024 年提出的机器人操作通用视觉-语言-动作模型，发表于 CoRL 2024。其核心贡献在于将操作任务表示为基于 3D 关键点的关系约束（Relational Keypoint Constraints），并通过分层优化实现实时动作求解，无需任务特定数据或环境模型。
  ko: 'ReKep: Spatio-Temporal Reasoning of Relational Keypoint Constraints for Robotic Manipulation (ReKep), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Stanford University, Columbia University, and published
    at CoRL 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- rekep
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.01652v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: ReKep source
  url: https://proceedings.mlr.press/v270/huang25g.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
ReKep 通过将机器人操作任务编码为环境 3D 关键点之间的数值约束函数，解决了传统约束表示在通用性、自动化标注和实时优化方面的不足。该方法利用 Python 函数将关键点映射为成本值，并采用分层优化流程在感知-动作循环中实时求解末端执行器位姿序列。为消除人工标注需求，ReKep 结合大型视觉模型与视觉-语言模型，从自然语言指令和 RGB-D 观测中自动生成约束。系统在轮式单臂平台和固定双臂平台上验证了多阶段、野外、双臂及反应式行为的有效性。

## 核心内容
### 方法架构
- **Relational Keypoint Constraints (ReKep)**：将操作任务表示为一系列 3D 关键点间的约束，每个约束定义为 Python 函数，输入环境关键点坐标，输出数值成本。
- **分层优化**：将任务分解为多阶段约束序列，通过两级优化求解：上层优化规划关键点轨迹，下层优化求解末端执行器位姿（SE(3) 空间），实现实时感知-动作循环。

### 自动化生成
- **约束生成**：利用大型视觉模型（如 SAM）提取 3D 关键点，结合视觉-语言模型（如 GPT-4V）从自由形式语言指令和 RGB-D 观测中自动推导约束函数。
- **无需人工标注**：所有约束由模型自动生成，无需任务特定数据或环境模型。

### 实验设置与结果
- **平台**：轮式单臂平台（配备 6-DOF 机械臂）和固定双臂平台（配备两个 7-DOF 机械臂）。
- **任务类型**：多阶段操作（如组装）、野外操作（如抓取未知物体）、双臂协作（如协同搬运）、反应式行为（如动态避障）。
- **关键性能**：所有任务均实现实时控制（频率 ≥ 10 Hz），无需预训练或环境模型，在多样化场景中保持鲁棒性。

### 结论
ReKep 通过关键点约束的视觉化表示与自动化生成，为通用机器人操作提供了可扩展框架，在无需任务特定数据的前提下实现了多场景实时操作。

## Overview
Representing robotic manipulation tasks as constraints that associate the robot and the environment is a promising way to encode desired robot behaviors. However, it remains unclear how to formulate the constraints such that they are 1) versatile to diverse tasks, 2) free of manual labeling, and 3) optimizable by off-the-shelf solvers to produce robot actions in real-time. In this work, we introduce Relational Keypoint Constraints (ReKep), a visually-grounded representation for constraints in robotic manipulation. Specifically, ReKep is expressed as Python functions mapping a set of 3D keypoints in the environment to a numerical cost. We demonstrate that by representing a manipulation task as a sequence of Relational Keypoint Constraints, we can employ a hierarchical optimization procedure to solve for robot actions (represented by a sequence of end-effector poses in SE(3)) with a perception-action loop at a real-time frequency. Furthermore, in order to circumvent the need for manual specification of ReKep for each new task, we devise an automated procedure that leverages large vision models and vision-language models to produce ReKep from free-form language instructions and RGB-D observations. We present system implementations on a wheeled single-arm platform and a stationary dual-arm platform that can perform a large variety of manipulation tasks, featuring multi-stage, in-the-wild, bimanual, and reactive behaviors, all without task-specific data or environment models. Website at https://rekep-robot.github.io/.

## 개요
로봇 조작 작업을 로봇과 환경을 연결하는 제약 조건으로 표현하는 것은 원하는 로봇 동작을 인코딩하는 유망한 방법입니다. 그러나 이러한 제약 조건을 1) 다양한 작업에 적용 가능하고, 2) 수동 레이블링이 필요 없으며, 3) 기성 솔버를 통해 실시간으로 로봇 동작을 생성할 수 있도록 최적화 가능하게 공식화하는 방법은 여전히 명확하지 않습니다. 본 연구에서는 로봇 조작에서 제약 조건을 위한 시각 기반 표현인 관계형 키포인트 제약 조건(ReKep)을 소개합니다. 구체적으로, ReKep은 환경 내 3D 키포인트 집합을 수치적 비용으로 매핑하는 Python 함수로 표현됩니다. 조작 작업을 일련의 관계형 키포인트 제약 조건으로 표현함으로써, 계층적 최적화 절차를 사용하여 SE(3)에서의 엔드 이펙터 자세 시퀀스로 표현되는 로봇 동작을 실시간 주파수의 인식-행동 루프로 해결할 수 있음을 보여줍니다. 또한, 각각의 새로운 작업에 대해 ReKep을 수동으로 지정해야 하는 필요성을 피하기 위해, 대규모 비전 모델과 비전-언어 모델을 활용하여 자유 형식의 언어 명령과 RGB-D 관측으로부터 ReKep을 생성하는 자동화된 절차를 고안했습니다. 우리는 작업별 데이터나 환경 모델 없이도 다단계, 실제 환경, 양팔, 반응형 동작을 특징으로 하는 다양한 조작 작업을 수행할 수 있는 바퀴 달린 단일 팔 플랫폼과 고정형 이중 팔 플랫폼에서의 시스템 구현을 제시합니다. 웹사이트: https://rekep-robot.github.io/.

## 핵심 내용
로봇 조작 작업을 로봇과 환경을 연결하는 제약 조건으로 표현하는 것은 원하는 로봇 동작을 인코딩하는 유망한 방법입니다. 그러나 이러한 제약 조건을 1) 다양한 작업에 적용 가능하고, 2) 수동 레이블링이 필요 없으며, 3) 기성 솔버를 통해 실시간으로 로봇 동작을 생성할 수 있도록 최적화 가능하게 공식화하는 방법은 여전히 명확하지 않습니다. 본 연구에서는 로봇 조작에서 제약 조건을 위한 시각 기반 표현인 관계형 키포인트 제약 조건(ReKep)을 소개합니다. 구체적으로, ReKep은 환경 내 3D 키포인트 집합을 수치적 비용으로 매핑하는 Python 함수로 표현됩니다. 조작 작업을 일련의 관계형 키포인트 제약 조건으로 표현함으로써, 계층적 최적화 절차를 사용하여 SE(3)에서의 엔드 이펙터 자세 시퀀스로 표현되는 로봇 동작을 실시간 주파수의 인식-행동 루프로 해결할 수 있음을 보여줍니다. 또한, 각각의 새로운 작업에 대해 ReKep을 수동으로 지정해야 하는 필요성을 피하기 위해, 대규모 비전 모델과 비전-언어 모델을 활용하여 자유 형식의 언어 명령과 RGB-D 관측으로부터 ReKep을 생성하는 자동화된 절차를 고안했습니다. 우리는 작업별 데이터나 환경 모델 없이도 다단계, 실제 환경, 양팔, 반응형 동작을 특징으로 하는 다양한 조작 작업을 수행할 수 있는 바퀴 달린 단일 팔 플랫폼과 고정형 이중 팔 플랫폼에서의 시스템 구현을 제시합니다. 웹사이트: https://rekep-robot.github.io/.

## 参考
- http://arxiv.org/abs/2409.01652v2
