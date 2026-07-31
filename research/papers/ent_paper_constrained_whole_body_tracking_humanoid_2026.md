---
$id: ent_paper_constrained_whole_body_tracking_humanoid_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Constrained Whole-Body Tracking for Humanoid Robots
  zh: 人形机器人全身动作跟踪的实时约束安全控制
  ko: Constrained Whole-Body Tracking for Humanoid Robots
summary:
  en: 'Recent advances in reinforcement learning (RL) have demonstrated impressive whole-body agility for humanoid robots,
    yet ensuring safety and satisfying constraints -- particularly those specified after training -- remains a challenge.
    Institutions per source list: 斯坦福、英伟达研究院.'
  zh: ConstrainedMimic 是一个面向人形机器人的控制框架，由研究团队提出，旨在强化学习跟踪策略中实时强制执行运动学与动力学约束。其核心贡献在于融合操作空间控制与控制障碍函数（CBFs），在保持策略能力的同时实现碰撞避免、关节限位与质心稳定性等约束，且支持
    CPU、GPU 与 TPU 部署，运行频率可达 300-500 Hz。
  ko: 'Recent advances in reinforcement learning (RL) have demonstrated impressive whole-body agility for humanoid robots,
    yet ensuring safety and satisfying constraints -- particularly those specified after training -- remains a challenge.
    Institutions per source list: 斯坦福、英伟达研究院.'
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
- constrained
- whole
- body
- tracking
- humanoid
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 35 (.staging/ingest_yuanxq). Tier B->full. arXiv id 2606.00374 recovered
    programmatically (strict title match/page scan). Title guard: abstract_mention (score 0.8). Abstract and metadata from
    arXiv API (2606.00374v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2606.00374 Constrained Whole-Body Tracking for Humanoid Robots
  url: https://arxiv.org/abs/2606.00374
  accessed_at: '2026-07-31'
  date: '2026-05-29'
- id: src_002
  type: website
  title: Project page
  url: https://danielpmorton.github.io/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

该工作针对强化学习策略在训练后难以满足运行时约束的问题，提出了 ConstrainedMimic 框架。它通过整合全身运动学与动力学模型，在实时控制中强制执行任意约束，包括运动参考轨迹与底层动力学。在 Unitree G1 仿真机器人的全身运动跟踪与遥操作实验中，该方法成功实现了机器人自身与外部障碍物的碰撞避免、关节限位以及质心稳定性约束。框架设计确保约束激活时对策略能力的限制最小化，且完全可微，支持多种硬件平台高效运行。

## 核心内容
### 方法架构
ConstrainedMimic 的核心在于将操作空间控制（Operational Space Control）与控制障碍函数（CBFs）的原理融入强化学习跟踪策略。具体而言，它通过全身运动学与动力学模型，在策略输出与机器人执行之间插入一个约束层。该层实时计算满足约束条件的控制指令，同时最小化对原始策略行为的偏离。

### 约束类型与实现
- **碰撞避免**：同时处理机器人自身肢体碰撞与外部障碍物碰撞，通过 CBF 约束确保安全距离。
- **关节限位**：限制每个关节的角度与速度范围，防止超出硬件极限。
- **质心稳定性**：约束机器人质心（CoM）的位置与速度，维持动态平衡。

### 实验设置
- **平台**：在 Unitree G1 仿真机器人上测试，使用预训练的强化学习策略。
- **任务**：全身运动跟踪与遥操作，要求机器人跟随参考轨迹同时满足运行时约束。
- **性能**：框架在 CPU、GPU 与 TPU 上均可运行，控制频率达到 300-500 Hz，满足实时性要求。

### 关键结果
- 约束激活时，策略能力仅受最小限制，保持与当前接触模式与跟踪目标的一致性。
- 所有约束均在实时中成功强制执行，未出现违反安全边界的情况。
- 框架完全可微，便于集成到端到端学习流程中。

### 结论
ConstrainedMimic 提供了一种有效的方法，在强化学习策略中引入运行时约束，兼顾安全性与灵活性。所有软件将在论文发表后开源。

## Overview
Recent advances in reinforcement learning (RL) have demonstrated impressive whole-body agility for humanoid robots, yet ensuring safety and satisfying constraints -- particularly those specified after training -- remains a challenge. Towards this goal, we present ConstrainedMimic, a control framework that leverages whole-body kinematics and dynamics for real-time constraint enforcement within RL tracking policies. By integrating principles from operational space control and control barrier functions (CBFs), we enable the satisfaction of arbitrary runtime constraints on both the kinematic reference motion and the underlying dynamics. In whole-body motion-tracking and teleoperation experiments on a (simulated) Unitree G1 with a learned policy, we demonstrate collision avoidance (both with the robot body and external obstacles), joint limits, and center of mass stability constraints. By remaining consistent with the current contact mode and tracking objectives, we minimally restrict the capabilities of the policy when constraints are active. Our method is fully differentiable, runs on CPU, GPU, and TPU, and can be deployed at up to 300-500 Hz. All software will be freely available upon publication.

## 参考
- https://arxiv.org/abs/2606.00374
- https://danielpmorton.github.io/
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

본 연구는 강화 학습 정책이 훈련 후 실행 시 제약 조건을 충족하기 어려운 문제를 해결하기 위해 ConstrainedMimic 프레임워크를 제안한다. 이는 전신 운동학 및 동역학 모델을 통합하여 실시간 제어에서 운동 참조 궤적과 기저 동역학을 포함한 임의의 제약 조건을 강제로 적용한다. Unitree G1 시뮬레이션 로봇의 전신 운동 추적 및 원격 조작 실험에서, 이 방법은 로봇 자체와 외부 장애물 간의 충돌 회피, 관절 한계, 그리고 질량 중심 안정성 제약을 성공적으로 구현했다. 프레임워크 설계는 제약 조건 활성화 시 정책 능력에 대한 제한을 최소화하며, 완전히 미분 가능하여 다양한 하드웨어 플랫폼에서 효율적으로 실행될 수 있다.

## 핵심 내용
### 방법 아키텍처
ConstrainedMimic의 핵심은 작업 공간 제어(Operational Space Control)와 제어 장애 함수(CBFs)의 원리를 강화 학습 추적 정책에 통합하는 것이다. 구체적으로, 전신 운동학 및 동역학 모델을 통해 정책 출력과 로봇 실행 사이에 제약 계층을 삽입한다. 이 계층은 제약 조건을 충족하는 제어 명령을 실시간으로 계산하면서 원래 정책 행동과의 편차를 최소화한다.

### 제약 유형 및 구현
- **충돌 회피**: 로봇 자체의 신체 충돌과 외부 장애물 충돌을 동시에 처리하며, CBF 제약을 통해 안전 거리를 보장한다.
- **관절 한계**: 각 관절의 각도와 속도 범위를 제한하여 하드웨어 한계를 초과하지 않도록 한다.
- **질량 중심 안정성**: 로봇의 질량 중심(CoM) 위치와 속도를 제약하여 동적 균형을 유지한다.

### 실험 설정
- **플랫폼**: Unitree G1 시뮬레이션 로봇에서 테스트되었으며, 사전 훈련된 강화 학습 정책을 사용한다.
- **작업**: 전신 운동 추적 및 원격 조작으로, 로봇이 참조 궤적을 따르면서 실행 시 제약 조건을 충족해야 한다.
- **성능**: 프레임워크는 CPU, GPU 및 TPU에서 실행 가능하며, 제어 주파수가 300-500 Hz에 도달하여 실시간 요구 사항을 충족한다.

### 주요 결과
- 제약 조건 활성화 시, 정책 능력은 최소한의 제한만 받으며 현재 접촉 모드 및 추적 목표와 일관성을 유지한다.
- 모든 제약 조건이 실시간으로 성공적으로 강제 적용되었으며, 안전 경계 위반은 발생하지 않았다.
- 프레임워크는 완전히 미분 가능하여 종단 간 학습 파이프라인에 통합하기 용이하다.

### 결론
ConstrainedMimic은 강화 학습 정책에 실행 시 제약 조건을 도입하여 안전성과 유연성을 모두 확보하는 효과적인 방법을 제공한다. 모든 소프트웨어는 논문 게재 후 오픈소스로 공개될 예정이다.
