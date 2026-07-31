---
$id: ent_paper_robonaldo_accurate_stable_powerful_human_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning'
  zh: 'RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning'
  ko: 'RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum Reinforcement Learning'
summary:
  en: 'Elite humanoid soccer shooting requires whole-body stability, high-impulse whole-body interactions, and accuracy to
    targets. Motion tracking-driven reinforcement learning (RL) provides stability in whole-body movement coordination, but
    a fixed reference makes it hard to adapt to varied ball positions and strike timings; in contrast, task reward-driven
    RL struggles to explore and discover valid kicks from scratch. Institutions per source list: 香港大学、香港中文大学、Archon Robotics.'
  zh: RoboNaldo 是由 OpenDriveLab 等机构提出的三阶段运动引导课程强化学习框架，用于实现人形机器人精准、稳定且高冲击力的足球射门。其核心贡献在于通过单一人类踢球参考逐步优化策略，在仿真中实现自由球射门误差降低 48.6%、射门速度提升
    2.96 倍，并在真实 Unitree G1 机器人上达到 0.73 米（自由球）和 0.86 米（移动球）的平均目标误差，触球后球速达 13.10 m/s。
  ko: 'Elite humanoid soccer shooting requires whole-body stability, high-impulse whole-body interactions, and accuracy to
    targets. Motion tracking-driven reinforcement learning (RL) provides stability in whole-body movement coordination, but
    a fixed reference makes it hard to adapt to varied ball positions and strike timings; in contrast, task reward-driven
    RL struggles to explore and discover valid kicks from scratch. Institutions per source list: 香港大学、香港中文大学、Archon Robotics.'
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
- robonaldo
- accurate
- stable
- powerful
- human
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 755 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2606.11092 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2606.11092v3); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.11092 RoboNaldo: Accurate, Stable and Powerful Humanoid Soccer Shooting via Motion-Guided Curriculum
    Reinforcement Learning'
  url: https://arxiv.org/abs/2606.11092
  accessed_at: '2026-07-31'
  date: '2026-06-09'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

RoboNaldo 针对人形机器人足球射门中全身稳定性、高冲击力交互和精准度三大挑战，提出了一种三阶段课程强化学习框架。该方法以单个人类踢球动作参考作为初始支架，逐步将优化目标从动作模仿转向射门性能。第一阶段学习稳定的全身踢球先验，第二阶段适应随机静止球的自由球场景，第三阶段通过运动指令与踢球触发接口扩展到移动球射门。在仿真中，RoboNaldo 相比基线方法显著提升了射门精度和速度；在真实 Unitree G1 机器人上，结合机载感知实现了 3 米距离的高精度射门，触球后球速达到职业球员开球速度的 59-71%。

## 核心内容
### 方法架构
RoboNaldo 采用三阶段课程强化学习框架，以单一人类踢球参考（human-kick reference）作为初始引导，逐步将优化重心转向射门性能：
- **第一阶段：全身踢球先验学习**：通过运动跟踪（motion tracking）学习稳定的全身动作协调先验，确保机器人能够模仿人类踢球动作。
- **第二阶段：自由球适应**：将策略适应到自由球场景，其中球静止在随机位置，机器人需要调整踢球动作以准确击中目标。
- **第三阶段：移动球射门**：通过运动指令（locomotion-command）和踢球触发（kick-trigger）接口，将策略扩展到移动球射门。训练时，高层启发式规划器（high-level heuristic planner）控制该接口；推理时，可替换为其他高层控制器。

### 实验设置与关键数字
- **仿真实验**：在仿真环境中，RoboNaldo 的自由球射门误差比基线方法低 48.6%，射门速度（shoot velocity）提升 2.96 倍。
- **真实机器人实验**：在 Unitree G1 机器人上，结合机载感知（onboard perception），从 3 米距离射门：
  - 自由球场景：平均目标误差 0.73 米
  - 移动球场景：平均目标误差 0.86 米
  - 触球后球速（post-contact ball velocity）达到 13.10 m/s，相当于职业球员开球速度（reported professional open-play shot speed）的 59-71%。

### 结论
RoboNaldo 通过运动引导的课程强化学习，有效解决了人形机器人高冲击力交互中的稳定性与精度问题，在仿真和真实场景中均显著优于现有方法。其框架设计支持灵活的高层控制器替换，为实际应用提供了可扩展的解决方案。

## Overview
Elite humanoid soccer shooting requires whole-body stability, high-impulse whole-body interactions, and accuracy to targets. Motion tracking-driven reinforcement learning (RL) provides stability in whole-body movement coordination, but a fixed reference makes it hard to adapt to varied ball positions and strike timings; in contrast, task reward-driven RL struggles to explore and discover valid kicks from scratch. We therefore introduce RoboNaldo, a three-stage motion-guided curriculum RL framework for high-impulse humanoid interaction. A single human-kick reference is used as a scaffold and progressively shifts optimization towards shooting performance. The curriculum first learns a stable whole-body kicking prior, then adapts the kick to free-kick settings where the ball is stationary at random positions, and finally extends it to moving-ball shooting through a locomotion-command and kick-trigger interface. A high-level heuristic planner controls this interface during training, while alternative high-level controllers can drive the same low-level policy at inference. In simulation, RoboNaldo demonstrates free-kick shot error 48.6% lower and shoot velocity 2.96x than prior work baselines. In real world on a Unitree G1 with onboard perception, RoboNaldo attains 0.73 m and 0.86 m average target shooting error from 3 m away in free-kick and moving-ball cases, accordingly. And the post-contact ball velocity reaches 13.10 m/s, which is 59-71% of reported professional open-play shot speed. Project page: https://opendrivelab.com/RoboNaldo.

## 参考
- https://arxiv.org/abs/2606.11092
- https://github.com/ImChong/Robotics_Notebooks

## 개요

RoboNaldo는 휴머노이드 로봇 축구 슛에서 전신 안정성, 고충격 상호작용 및 정밀도라는 세 가지 주요 과제를 해결하기 위해 3단계 커리큘럼 강화 학습 프레임워크를 제안합니다. 이 방법은 단일 인간 킥 동작 참조를 초기 지지대로 사용하여 최적화 목표를 점진적으로 동작 모방에서 슛 성능으로 전환합니다. 첫 번째 단계에서는 안정적인 전신 킥 사전 지식을 학습하고, 두 번째 단계에서는 무작위 정지 공에 대한 프리킥 시나리오에 적응하며, 세 번째 단계에서는 운동 명령과 킥 트리거 인터페이스를 통해 이동하는 공 슛으로 확장합니다. 시뮬레이션에서 RoboNaldo는 기준 방법에 비해 슛 정밀도와 속도를 크게 향상시켰으며, 실제 Unitree G1 로봇에서는 탑재 인식을 결합하여 3미터 거리에서 높은 정밀도의 슛을 구현했으며, 공을 맞춘 후 공 속도는 프로 선수의 킥오프 속도의 59-71%에 도달했습니다.

## 핵심 내용
### 방법 아키텍처
RoboNaldo는 3단계 커리큘럼 강화 학습 프레임워크를 채택하며, 단일 인간 킥 참조를 초기 안내로 사용하여 점진적으로 최적화 초점을 슛 성능으로 전환합니다:
- **1단계: 전신 킥 사전 지식 학습**: 모션 트래킹을 통해 안정적인 전신 동작 조정 사전 지식을 학습하여 로봇이 인간의 킥 동작을 모방할 수 있도록 보장합니다.
- **2단계: 프리킥 적응**: 정책을 프리킥 시나리오에 적응시키며, 여기서 공은 무작위 위치에 정지해 있고 로봇은 목표를 정확히 맞추기 위해 킥 동작을 조정해야 합니다.
- **3단계: 이동하는 공 슛**: 운동 명령 및 킥 트리거 인터페이스를 통해 정책을 이동하는 공 슛으로 확장합니다. 훈련 시 고수준 휴리스틱 플래너가 이 인터페이스를 제어하며, 추론 시에는 다른 고수준 컨트롤러로 대체할 수 있습니다.

### 실험 설정 및 주요 수치
- **시뮬레이션 실험**: 시뮬레이션 환경에서 RoboNaldo의 프리킥 슛 오차는 기준 방법보다 48.6% 낮았으며, 슛 속도는 2.96배 향상되었습니다.
- **실제 로봇 실험**: Unitree G1 로봇에서 탑재 인식을 결합하여 3미터 거리에서 슛:
  - 프리킥 시나리오: 평균 목표 오차 0.73미터
  - 이동하는 공 시나리오: 평균 목표 오차 0.86미터
  - 공을 맞춘 후 공 속도는 13.10 m/s에 도달했으며, 이는 프로 선수의 킥오프 속도의 59-71%에 해당합니다.

### 결론
RoboNaldo는 운동 안내 커리큘럼 강화 학습을 통해 휴머노이드 로봇의 고충격 상호작용에서 안정성과 정밀도 문제를 효과적으로 해결했으며, 시뮬레이션과 실제 시나리오 모두에서 기존 방법보다 크게 우수합니다. 이 프레임워크 설계는 유연한 고수준 컨트롤러 교체를 지원하여 실제 응용에 확장 가능한 솔루션을 제공합니다.
