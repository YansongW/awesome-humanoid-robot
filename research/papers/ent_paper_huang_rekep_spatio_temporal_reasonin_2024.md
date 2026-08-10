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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.01652v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (837 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2409.01652v2

## 개요
ReKep은 로봇 조작 작업을 환경의 3D 키포인트 간 수치 제약 함수로 인코딩하여, 기존 제약 표현이 지닌 범용성, 자동 주석, 실시간 최적화 측면의 한계를 해결합니다. 이 방법은 Python 함수를 사용해 키포인트를 비용 값으로 매핑하고, 계층적 최적화 프로세스를 통해 인식-행동 루프에서 엔드 이펙터 포즈 시퀀스를 실시간으로 해석합니다. 수동 주석의 필요성을 없애기 위해 ReKep은 대형 비전 모델과 비전-언어 모델을 결합하여 자연어 명령과 RGB-D 관측에서 제약을 자동 생성합니다. 시스템은 바퀴형 단일 암 플랫폼과 고정 이중 암 플랫폼에서 다단계, 야외, 이중 암 및 반응형 동작의 유효성을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
- **Relational Keypoint Constraints (ReKep)**: 조작 작업을 일련의 3D 키포인트 간 제약으로 표현하며, 각 제약은 Python 함수로 정의되어 환경 키포인트 좌표를 입력으로 받고 수치 비용을 출력합니다.
- **계층적 최적화**: 작업을 다단계 제약 시퀀스로 분해하고, 두 수준의 최적화로 해결합니다. 상위 최적화는 키포인트 궤적을 계획하고, 하위 최적화는 엔드 이펙터 포즈(SE(3) 공간)를 해석하여 실시간 인식-행동 루프를 구현합니다.

### 자동 생성
- **제약 생성**: 대형 비전 모델(예: SAM)을 사용해 3D 키포인트를 추출하고, 비전-언어 모델(예: GPT-4V)을 결합하여 자유 형식 언어 명령과 RGB-D 관측에서 제약 함수를 자동으로 도출합니다.
- **수동 주석 불필요**: 모든 제약은 모델에 의해 자동 생성되며, 작업별 데이터나 환경 모델이 필요하지 않습니다.

### 실험 설정 및 결과
- **플랫폼**: 바퀴형 단일 암 플랫폼(6-DOF 로봇 암 장착) 및 고정 이중 암 플랫폼(두 개의 7-DOF 로봇 암 장착).
- **작업 유형**: 다단계 조작(예: 조립), 야외 조작(예: 미지 물체 파지), 이중 암 협력(예: 협동 운반), 반응형 동작(예: 동적 장애물 회피).
- **주요 성능**: 모든 작업에서 사전 훈련이나 환경 모델 없이 실시간 제어(주파수 ≥ 10 Hz)를 구현하며, 다양한 시나리오에서 견고성을 유지합니다.

### 결론
ReKep은 키포인트 제약의 시각적 표현과 자동 생성을 통해 범용 로봇 조작을 위한 확장 가능한 프레임워크를 제공하며, 작업별 데이터 없이도 다양한 시나리오에서 실시간 조작을 구현합니다.
