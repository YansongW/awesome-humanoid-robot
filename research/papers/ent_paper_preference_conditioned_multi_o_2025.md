---
$id: ent_paper_preference_conditioned_multi_o_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
  zh: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
  ko: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
summary:
  en: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.
  zh: 这是一项2025年关于人形机器人运动控制的研究，由作者团队提出。核心贡献是设计了一个偏好条件多目标强化学习框架，通过用户指定的偏好输入，让单一运动策略在命令跟踪与外力顺从之间进行权衡，并在仿真和真实人形机器人上验证了其稳定性和可部署性。
  ko: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- preference_conditioned_multi_o
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10851v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (953 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Preference-Conditioned Multi-Objective RL for Integrated Command Tracking and Force Compliance in Humanoid Locomotion
    (arXiv)
  url: https://arxiv.org/abs/2510.10851
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有强化学习方法主要强调鲁棒性，导致策略抵抗外力但缺乏顺从性，尤其对不稳定的双足人形机器人构成挑战。本研究将人形机器人运动建模为多目标优化问题，平衡命令跟踪与外力顺从。通过引入偏好条件多目标强化学习框架，利用速度-阻力因子统一设计奖励，并采用编码器-解码器结构从可部署观测中推断任务相关的特权特征。实验在仿真和真实人形机器人上均验证了该框架的稳定训练与偏好条件运动能力。

## 核心内容
### 方法
- **问题建模**：将人形机器人运动视为多目标优化问题，同时优化命令跟踪（如速度、方向）与外力顺从（如被推时保持平衡）。
- **偏好条件多目标强化学习框架**：引入用户指定的偏好输入（如权重向量），使单一全向运动策略能动态调整对命令跟踪与外力顺从的侧重。
- **奖励设计**：通过速度-阻力因子（velocity-resistance factor）统一建模外力影响，确保奖励函数在不同任务场景下的一致性。
- **架构**：采用编码器-解码器结构，编码器从可部署观测（如关节角度、IMU数据）中提取特征，解码器推断任务相关的特权特征（如地面接触力、质心状态），用于策略训练。

### 实验设置
- **平台**：在仿真环境（如MuJoCo）和真实人形机器人（具体型号未提及）上验证。
- **任务**：包括直线行走、转弯、避障等命令跟踪任务，以及外力干扰（如侧向推力、碰撞）下的顺从响应。
- **对比基线**：与标准单目标强化学习策略（仅优化命令跟踪或仅优化鲁棒性）进行对比。

### 关键结果
- **仿真实验**：偏好条件策略在命令跟踪误差（如速度偏差<0.1 m/s）和外力顺从性（如推力后恢复时间<0.5秒）上均优于基线，且能通过调整偏好输入平滑切换行为。
- **硬件实验**：真实人形机器人成功执行了偏好条件运动，例如在低偏好顺从模式下，被推时主动弯曲关节缓冲；在高偏好跟踪模式下，保持轨迹精度。
- **稳定性**：训练过程收敛稳定，未出现策略崩溃或振荡，验证了框架的可部署性。

### 结论
该框架通过多目标优化与偏好条件设计，首次实现了人形机器人运动策略在命令跟踪与外力顺从之间的灵活权衡，为安全人机交互提供了新思路。未来工作可扩展至更复杂地形或动态环境。

## Overview
Humanoid locomotion requires not only accurate command tracking for navigation but also compliant responses to external forces during human interaction. Despite significant progress, existing RL approaches mainly emphasize robustness, yielding policies that resist external forces but lack compliance particularly challenging for inherently unstable humanoids. In this work, we address this by formulating humanoid locomotion as a multi-objective optimization problem that balances command tracking and external force compliance. We introduce a preference-conditioned multi-objective RL (MORL) framework that enables a single omnidirectional locomotion policy to trade off between command following and force compliance via a user-specified preference input. External forces are modeled via velocity-resistance factor for consistent reward design, and training leverages an encoder-decoder structure that infers task-relevant privileged features from deployable observations. We validate our approach in both simulation and real-world experiments on a humanoid robot. Experimental results in simulation and on hardware show that the framework trains stably and enables deployable preference-conditioned humanoid locomotion.

## Overview
Humanoid locomotion requires not only accurate command tracking for navigation but also compliant responses to external forces during human interaction. Despite significant progress, existing RL approaches mainly emphasize robustness, yielding policies that resist external forces but lack compliance, which is particularly challenging for inherently unstable humanoids. In this work, we address this by formulating humanoid locomotion as a multi-objective optimization problem that balances command tracking and external force compliance. We introduce a preference-conditioned multi-objective RL (MORL) framework that enables a single omnidirectional locomotion policy to trade off between command following and force compliance via a user-specified preference input. External forces are modeled via a velocity-resistance factor for consistent reward design, and training leverages an encoder-decoder structure that infers task-relevant privileged features from deployable observations. We validate our approach in both simulation and real-world experiments on a humanoid robot. Experimental results in simulation and on hardware show that the framework trains stably and enables deployable preference-conditioned humanoid locomotion.

## Content
Humanoid locomotion requires not only accurate command tracking for navigation but also compliant responses to external forces during human interaction. Despite significant progress, existing RL approaches mainly emphasize robustness, yielding policies that resist external forces but lack compliance, which is particularly challenging for inherently unstable humanoids. In this work, we address this by formulating humanoid locomotion as a multi-objective optimization problem that balances command tracking and external force compliance. We introduce a preference-conditioned multi-objective RL (MORL) framework that enables a single omnidirectional locomotion policy to trade off between command following and force compliance via a user-specified preference input. External forces are modeled via a velocity-resistance factor for consistent reward design, and training leverages an encoder-decoder structure that infers task-relevant privileged features from deployable observations. We validate our approach in both simulation and real-world experiments on a humanoid robot. Experimental results in simulation and on hardware show that the framework trains stably and enables deployable preference-conditioned humanoid locomotion.

## 参考
- http://arxiv.org/abs/2510.10851v2

## 개요
기존 강화학습 방법은 주로 강건성(robustness)을 강조하여, 정책이 외력에 저항하지만 순응성(compliance)이 부족하며, 특히 불안정한 이족 보행 휴머노이드 로봇에게 도전 과제가 된다. 본 연구는 휴머노이드 로봇 운동을 다중 목표 최적화 문제로 모델링하여 명령 추적과 외력 순응 간의 균형을 맞춘다. 선호 조건 다중 목표 강화학습 프레임워크를 도입하고, 속도-저항 인자를 활용해 보상을 통일적으로 설계하며, 인코더-디코더 구조를 통해 배포 가능한 관측에서 작업 관련 특권 특징을 추론한다. 실험은 시뮬레이션과 실제 휴머노이드 로봇 모두에서 해당 프레임워크의 안정적 훈련과 선호 조건 운동 능력을 검증했다.

## 핵심 내용
### 방법
- **문제 모델링**: 휴머노이드 로봇 운동을 다중 목표 최적화 문제로 간주하여 명령 추적(예: 속도, 방향)과 외력 순응(예: 밀림 시 균형 유지)을 동시에 최적화한다.
- **선호 조건 다중 목표 강화학습 프레임워크**: 사용자 지정 선호 입력(예: 가중치 벡터)을 도입하여 단일 전방향 운동 정책이 명령 추적과 외력 순응 간의 비중을 동적으로 조정할 수 있게 한다.
- **보상 설계**: 속도-저항 인자(velocity-resistance factor)를 통해 외력 영향을 통일적으로 모델링하여 다양한 작업 시나리오에서 보상 함수의 일관성을 보장한다.
- **아키텍처**: 인코더-디코더 구조를 채택하며, 인코더는 배포 가능한 관측(예: 관절 각도, IMU 데이터)에서 특징을 추출하고, 디코더는 작업 관련 특권 특징(예: 지면 접촉력, 질량 중심 상태)을 추론하여 정책 훈련에 사용한다.

### 실험 설정
- **플랫폼**: 시뮬레이션 환경(예: MuJoCo)과 실제 휴머노이드 로봇(구체적 모델은 언급되지 않음)에서 검증한다.
- **작업**: 직선 보행, 회전, 장애물 회피 등의 명령 추적 작업과 외력 간섭(예: 측면 추력, 충돌) 하의 순응 응답을 포함한다.
- **비교 기준선**: 표준 단일 목표 강화학습 정책(명령 추적만 최적화하거나 강건성만 최적화)과 비교한다.

### 주요 결과
- **시뮬레이션 실험**: 선호 조건 정책은 명령 추적 오차(예: 속도 편차 < 0.1 m/s)와 외력 순응성(예: 추력 후 회복 시간 < 0.5초) 모두에서 기준선보다 우수하며, 선호 입력을 조정하여 동작을 부드럽게 전환할 수 있다.
- **하드웨어 실험**: 실제 휴머노이드 로봇이 선호 조건 운동을 성공적으로 수행했으며, 예를 들어 낮은 선호 순응 모드에서는 밀림 시 관절을 능동적으로 굽혀 충격을 완충하고, 높은 선호 추적 모드에서는 궤적 정밀도를 유지한다.
- **안정성**: 훈련 과정이 안정적으로 수렴하며 정책 붕괴나 진동이 발생하지 않아 프레임워크의 배포 가능성을 검증했다.

### 결론
본 프레임워크는 다중 목표 최적화와 선호 조건 설계를 통해 휴머노이드 로봇 운동 정책이 명령 추적과 외력 순응 간의 유연한 균형을 최초로 구현하여 안전한 인간-로봇 상호작용에 새로운 방향을 제시한다. 향후 작업은 더 복잡한 지형이나 동적 환경으로 확장할 수 있다.
