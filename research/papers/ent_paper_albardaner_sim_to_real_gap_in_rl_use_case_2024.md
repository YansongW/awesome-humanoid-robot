---
$id: ent_paper_albardaner_sim_to_real_gap_in_rl_use_case_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Sim-to-Real gap in RL: Use Case with TIAGo and Isaac Sim/Gym'
  zh: 强化学习中的仿真到现实差距：基于 TIAGo 与 Isaac Sim/Gym 的实例研究
  ko: 'RL의 시뮬레이션-현실 간격: TIAGo 및 Isaac Sim/Gym 활용 사례'
summary:
  en: This 2024 arXiv paper trains reinforcement-learning policies for the TIAGo mobile manipulator in Nvidia Isaac Gym and
    Isaac Sim, then quantifies joint-response differences and accumulated errors against the real robot to demonstrate sim-to-real
    transfer.
  zh: 这篇2024年的arXiv论文针对TIAGo移动操作臂，在Nvidia Isaac Gym和Isaac Sim两个仿真器中训练强化学习策略，并通过量化关节响应差异和累积误差，验证了从仿真到真实机器人的迁移效果。
  ko: 이 2024년 arXiv 논문은 Nvidia Isaac Gym과 Isaac Sim에서 TIAGo 이동 조작 로봇용 강화학습 정책을 학습한 후, 실제 로봇과의 관절 응답 차이 및 누적 오차를 정량화하여 시뮬레이션-현실
    전이를 입증한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- reinforcement_learning
- isaac_gym
- isaac_sim
- tiago
- mobile_manipulation
- physics_simulation
- control_architecture
- collision_avoidance
- ros
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.07091v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (660 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Sim-to-Real gap in RL: Use Case with TIAGo and Isaac Sim/Gym'
  url: https://arxiv.org/abs/2403.07091
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该研究聚焦于机器人操作任务中的仿真到现实迁移问题，以TIAGo移动操作臂为平台，对比了Nvidia开发的Isaac Gym和Isaac Sim两种先进仿真环境。论文详细讨论了控制架构设计，特别强调在仿真和真实环境中实现无碰撞运动。实验结果显示，强化学习训练的模型在仿真和真实场景中执行了相似的动作，成功实现了仿真到现实的迁移。

## 核心内容
### 研究背景与目标
- 针对TIAGo移动操作臂，探索强化学习策略从仿真到真实环境的迁移方法
- 对比两种Nvidia仿真器：Isaac Gym（侧重快速训练）和Isaac Sim（侧重高保真渲染与物理）

### 方法架构
- 采用强化学习训练策略，在仿真环境中学习无碰撞运动控制
- 控制架构设计兼顾仿真与真实环境的差异，包括关节响应特性与动力学参数

### 实验设置
- 训练环境：Isaac Gym用于策略快速迭代，Isaac Sim用于高保真验证
- 真实机器人：TIAGo移动操作臂，配备完整传感器与执行器
- 评估指标：关节响应差异、累积误差、运动轨迹一致性

### 关键结果
- 成功实现仿真到真实迁移，RL模型在仿真与真实环境中执行相似运动
- 量化了关节响应差异与累积误差，为后续迁移优化提供基准
- 验证了Isaac Gym与Isaac Sim在TIAGo平台上的有效性

### 结论
- 证明了基于Nvidia仿真器的强化学习策略可有效迁移至真实TIAGo机器人
- 为移动操作臂的仿真到现实迁移提供了可复现的评估框架与定量分析

## Overview
This paper explores policy-learning approaches in the context of sim-to-real transfer for robotic manipulation using a TIAGo mobile manipulator, focusing on two state-of-art simulators, Isaac Gym and Isaac Sim, both developed by Nvidia. Control architectures are discussed, with a particular emphasis on achieving collision-less movement in both simulation and the real environment. Presented results demonstrate successful sim-to-real transfer, showcasing similar movements executed by an RL-trained model in both simulated and real setups.

## Overview
This paper explores policy-learning approaches in the context of sim-to-real transfer for robotic manipulation using a TIAGo mobile manipulator, focusing on two state-of-the-art simulators, Isaac Gym and Isaac Sim, both developed by Nvidia. Control architectures are discussed, with a particular emphasis on achieving collision-less movement in both simulation and the real environment. Presented results demonstrate successful sim-to-real transfer, showcasing similar movements executed by an RL-trained model in both simulated and real setups.

## Content
This paper explores policy-learning approaches in the context of sim-to-real transfer for robotic manipulation using a TIAGo mobile manipulator, focusing on two state-of-the-art simulators, Isaac Gym and Isaac Sim, both developed by Nvidia. Control architectures are discussed, with a particular emphasis on achieving collision-less movement in both simulation and the real environment. Presented results demonstrate successful sim-to-real transfer, showcasing similar movements executed by an RL-trained model in both simulated and real setups.

## 参考
- http://arxiv.org/abs/2403.07091v2

## 개요
이 연구는 로봇 조작 작업에서의 시뮬레이션-실제 전이 문제에 초점을 맞추며, TIAGo 모바일 매니퓰레이터 플랫폼을 기반으로 Nvidia가 개발한 Isaac Gym과 Isaac Sim 두 가지 고급 시뮬레이션 환경을 비교합니다. 논문은 제어 아키텍처 설계를 자세히 논의하며, 특히 시뮬레이션 및 실제 환경에서의 충돌 없는 운동 구현을 강조합니다. 실험 결과, 강화 학습으로 훈련된 모델이 시뮬레이션 및 실제 시나리오에서 유사한 동작을 수행하여 시뮬레이션-실제 전이를 성공적으로 달성했습니다.

## 핵심 내용
### 연구 배경 및 목표
- TIAGo 모바일 매니퓰레이터를 대상으로 강화 학습 정책의 시뮬레이션-실제 환경 전이 방법 탐구
- 두 가지 Nvidia 시뮬레이터 비교: Isaac Gym(빠른 훈련 중심) 및 Isaac Sim(고충실도 렌더링 및 물리 중심)

### 방법 아키텍처
- 강화 학습을 사용하여 정책을 훈련하고, 시뮬레이션 환경에서 충돌 없는 운동 제어 학습
- 제어 아키텍처 설계는 관절 응답 특성 및 동역학 매개변수를 포함한 시뮬레이션과 실제 환경 간의 차이를 고려

### 실험 설정
- 훈련 환경: Isaac Gym은 정책의 빠른 반복에 사용되고, Isaac Sim은 고충실도 검증에 사용
- 실제 로봇: TIAGo 모바일 매니퓰레이터, 완전한 센서 및 액추에이터 장착
- 평가 지표: 관절 응답 차이, 누적 오차, 운동 궤적 일관성

### 주요 결과
- 시뮬레이션-실제 전이 성공, RL 모델이 시뮬레이션 및 실제 환경에서 유사한 동작 수행
- 관절 응답 차이 및 누적 오차를 정량화하여 후속 전이 최적화를 위한 기준 제공
- TIAGo 플랫폼에서 Isaac Gym과 Isaac Sim의 유효성 검증

### 결론
- Nvidia 시뮬레이터 기반 강화 학습 정책이 실제 TIAGo 로봇으로 효과적으로 전이될 수 있음을 입증
- 모바일 매니퓰레이터의 시뮬레이션-실제 전이를 위한 재현 가능한 평가 프레임워크 및 정량적 분석 제공
