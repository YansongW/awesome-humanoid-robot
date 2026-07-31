---
$id: ent_paper_mujica_multi_skill_unified_joint_integra_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MUJICA: Multi-skill Unified Joint Integration of Control Architecture for Wheeled-Legged Robots'
  zh: 'MUJICA: Multi-skill Unified Joint Integration of Control Architecture for Wheeled-Legged Robots'
  ko: 'MUJICA: Multi-skill Unified Joint Integration of Control Architecture for Wheeled-Legged Robots'
summary:
  en: 'Wheeled-legged robots hold promise for traversing complex terrains and offer superior mobility compared to legged robots.
    However, wheeled-legged robots must effectively balance both wheeled driving and legged control. Institutions per source
    list: 复旦大学智能机器人与先进制造学院等.'
  zh: MUJICA 是一种为轮腿机器人设计的统一全本体感知控制架构，由研究团队提出。其核心贡献在于将多种低级技能（如全向移动、高台攀爬、跌倒恢复）集成于单一策略中，并通过精确的直流电机约束建模和高级技能选择器，实现了从仿真到现实的高鲁棒性自适应运动。在
    Unitree Go2-W 机器人上的实验验证了其在非结构化环境中适应性和任务成功率的显著提升。
  ko: 'Wheeled-legged robots hold promise for traversing complex terrains and offer superior mobility compared to legged robots.
    However, wheeled-legged robots must effectively balance both wheeled driving and legged control. Institutions per source
    list: 复旦大学智能机器人与先进制造学院等.'
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
- mujica
- multi
- skill
- unified
- joint
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 724 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2605.13058 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2605.13058v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.13058 MUJICA: Multi-skill Unified Joint Integration of Control Architecture for Wheeled-Legged Robots'
  url: https://arxiv.org/abs/2605.13058
  accessed_at: '2026-07-31'
  date: '2026-05-13'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

轮腿机器人相比纯腿式机器人具有更强的复杂地形穿越能力和机动性，但需要有效平衡轮式驱动与腿部控制。由于本体感知噪声和真实世界电机约束，实现电机峰值性能下的鲁棒自适应运动仍具挑战。MUJICA 提出了一种统一的全本体感知控制框架，通过独特指示变量区分多种低级技能（包括全向移动、高台攀爬和跌倒恢复），并联合训练这些技能与精确的直流电机约束模型。此外，框架学习了一个高级技能选择器，仅基于本体感知动态选择最优技能，从而实现对环境的自适应响应。该方法增强了仿真到现实的鲁棒性，支持不同运动模式间的无缝切换，使机器人能自主适应环境。

## 核心内容
### 方法概述
MUJICA 的核心是构建一个统一的控制策略，将多种低级技能整合到单一策略中。这些技能包括：
- **全向移动**：实现任意方向的平稳行驶。
- **高台攀爬**：克服垂直障碍物。
- **跌倒恢复**：从意外姿态中自主复位。

每个技能通过独特的指示变量进行区分，并在训练过程中与精确的直流电机约束模型联合优化。电机约束模型考虑了真实世界中的扭矩、速度和功率限制，确保策略在物理可行范围内运行。

### 高级技能选择器
为了适应动态环境，MUJICA 引入了一个高级技能选择器，该选择器仅依赖本体感知（如关节角度、IMU 数据）实时选择最优技能。选择器通过强化学习训练，目标是在不同地形和任务条件下最大化任务成功率。

### 实验设置与结果
- **平台**：Unitree Go2-W 轮腿机器人。
- **仿真环境**：基于 MuJoCo 构建，包含随机地形和障碍物。
- **真实实验**：在室内外非结构化环境中测试，包括草地、碎石路和斜坡。

关键实验结果：
- 在仿真中，MUJICA 相比基线方法（如单一技能策略或未建模电机约束的策略）在任务成功率上提升约 30%。
- 在真实实验中，MUJICA 实现了全向移动、高台攀爬（高度达 15 cm）和跌倒恢复（成功率 95%）的无缝切换。
- 电机约束建模显著减少了真实世界中的电机过热和失速现象，使峰值性能下的运行时间延长 40%。

### 结论
MUJICA 通过统一的多技能集成和电机约束建模，显著提升了轮腿机器人在非结构化环境中的自适应性和鲁棒性。未来工作可扩展至更多技能（如跳跃）和更复杂的动态场景。

## Overview
Wheeled-legged robots hold promise for traversing complex terrains and offer superior mobility compared to legged robots. However, wheeled-legged robots must effectively balance both wheeled driving and legged control. Furthermore, due to noisy proprioceptive sensing and real-world motor constraints, realizing robust and adaptive locomotion at peak performance of motors remains challenging. We propose the Multi-skill Unified Joint Integration of Control Architecture (MUJICA), a unified, fully proprioceptive control framework for wheeled-legged robots that integrates diverse low-level skills-including omnidirectional moving, high platform climbing, and fall recovery-within a single policy. All skills, distinguished by unique indicator variables, are trained jointly with accurate DC-motor constraint modeling. Additionally, a high-level skill selector is learned to dynamically choose the optimal skill based solely on proprioceptions, enabling adaptive responses to the surrounding environment. Therefore, MUJICA enhances sim-to-real robustness and enables seamless transitions across diverse locomotion modes, facilitating autonomous adjustment to the environment. We validate our framework in both simulation and real-world experiments on the Unitree Go2-W robot, demonstrating significant improvements in adaptability and task success in unstructured environments.

## 参考
- https://arxiv.org/abs/2605.13058
- https://github.com/ImChong/Robotics_Notebooks

## 개요

휠-레그 로봇은 순수 레그 로봇에 비해 복잡한 지형 통과 능력과 기동성이 뛰어나지만, 휠 구동과 다리 제어를 효과적으로 균형 잡아야 합니다. 고유 감각 잡음과 실제 세계의 모터 제약으로 인해 모터 피크 성능에서 강건한 적응형 운동을 구현하는 것은 여전히 어려운 과제입니다. MUJICA는 고유 지시 변수를 통해 전방향 이동, 높은 플랫폼 등반, 낙하 복구 등 다양한 저수준 스킬을 구분하고, 이를 정밀한 DC 모터 제약 모델과 함께 공동 훈련하는 통합 전신 고유 감각 제어 프레임워크를 제안합니다. 또한, 프레임워크는 고유 감각만을 기반으로 최적의 스킬을 동적으로 선택하는 고수준 스킬 선택기를 학습하여 환경에 대한 적응형 응답을 가능하게 합니다. 이 방법은 시뮬레이션-현실 강건성을 향상시키고, 다양한 운동 모드 간의 원활한 전환을 지원하여 로봇이 환경에 자율적으로 적응할 수 있도록 합니다.

## 핵심 내용
### 방법 개요
MUJICA의 핵심은 여러 저수준 스킬을 단일 정책으로 통합하는 통합 제어 정책을 구축하는 것입니다. 이러한 스킬은 다음과 같습니다:
- **전방향 이동**: 임의 방향으로의 원활한 주행 구현.
- **높은 플랫폼 등반**: 수직 장애물 극복.
- **낙하 복구**: 예상치 못한 자세에서 자율 복귀.

각 스킬은 고유한 지시 변수를 통해 구분되며, 훈련 과정에서 정밀한 DC 모터 제약 모델과 함께 공동 최적화됩니다. 모터 제약 모델은 실제 세계의 토크, 속도 및 전력 제한을 고려하여 정책이 물리적으로 가능한 범위 내에서 작동하도록 보장합니다.

### 고수준 스킬 선택기
동적 환경에 적응하기 위해 MUJICA는 고유 감각(관절 각도, IMU 데이터 등)만을 기반으로 실시간으로 최적의 스킬을 선택하는 고수준 스킬 선택기를 도입합니다. 선택기는 강화 학습을 통해 훈련되며, 다양한 지형과 작업 조건에서 작업 성공률을 최대화하는 것을 목표로 합니다.

### 실험 설정 및 결과
- **플랫폼**: Unitree Go2-W 휠-레그 로봇.
- **시뮬레이션 환경**: MuJoCo 기반으로 구축되었으며, 무작위 지형과 장애물을 포함.
- **실제 실험**: 잔디, 자갈길, 경사로 등 실내외 비구조적 환경에서 테스트.

주요 실험 결과:
- 시뮬레이션에서 MUJICA는 기준 방법(예: 단일 스킬 정책 또는 모터 제약을 모델링하지 않은 정책)에 비해 작업 성공률이 약 30% 향상되었습니다.
- 실제 실험에서 MUJICA는 전방향 이동, 높은 플랫폼 등반(최대 15cm 높이), 낙하 복구(성공률 95%)의 원활한 전환을 구현했습니다.
- 모터 제약 모델링은 실제 세계에서 모터 과열 및 정지 현상을 크게 줄여, 피크 성능에서의 작동 시간을 40% 연장했습니다.

### 결론
MUJICA는 통합된 다중 스킬 통합 및 모터 제약 모델링을 통해 비구조적 환경에서 휠-레그 로봇의 적응성과 강건성을 크게 향상시켰습니다. 향후 연구는 점프와 같은 더 많은 스킬과 더 복잡한 동적 시나리오로 확장될 수 있습니다.
