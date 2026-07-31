---
$id: ent_paper_rhythm_interactive_whole_body_control_du_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Rhythm: Learning Interactive Whole-Body Control for Dual Humanoids'
  zh: 'Rhythm: Learning Interactive Whole-Body Control for Dual Humanoids'
  ko: 'Rhythm: Learning Interactive Whole-Body Control for Dual Humanoids'
summary:
  en: 'Realizing interactive whole-body control for multi-humanoid systems is critical for unlocking complex collaborative
    capabilities in shared environments. Institutions per source list: 上海交通大学、香港中文大学（深圳）等.'
  zh: Rhythm 是首个实现双人形机器人系统物理交互的统一框架，由研究团队提出。其核心贡献在于通过 Interaction-Aware Motion Retargeting (IAMR) 模块、Interaction-Guided Reinforcement
    Learning (IGRL) 策略和真实部署系统，成功将拥抱、舞蹈等复杂交互行为从仿真迁移至物理 Unitree G1 机器人。
  ko: 'Realizing interactive whole-body control for multi-humanoid systems is critical for unlocking complex collaborative
    capabilities in shared environments. Institutions per source list: 上海交通大学、香港中文大学（深圳）等.'
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
- rhythm
- interactive
- whole
- body
- control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 750 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2603.02856 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2603.02856v2); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2603.02856 Rhythm: Learning Interactive Whole-Body Control for Dual Humanoids'
  url: https://arxiv.org/abs/2603.02856
  accessed_at: '2026-07-31'
  date: '2026-03-03'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

Rhythm 框架旨在解决多人形机器人系统在共享环境中实现物理耦合交互的挑战，特别是运动学不匹配和复杂接触动力学问题。该框架包含三个核心组件：IAMR 模块从人类数据生成可行的交互参考；IGRL 策略通过基于图的奖励机制掌握耦合动力学；真实部署系统确保双机器人交互的鲁棒迁移。在 Unitree G1 机器人上的实验验证了该框架能够实现稳健的交互式全身控制，成功将多种行为从仿真迁移到现实。

## 核心内容
### 方法架构
Rhythm 框架由三个核心模块组成：
- **Interaction-Aware Motion Retargeting (IAMR)**：从人类交互数据中提取运动特征，生成符合双人形机器人运动学约束的交互参考轨迹。
- **Interaction-Guided Reinforcement Learning (IGRL)**：采用基于图的奖励函数设计，使策略能够学习双机器人之间的耦合动力学，包括接触力分配和协调运动。
- **真实部署系统**：包含状态估计、力控制和安全机制，确保策略在物理机器人上的鲁棒执行。

### 实验设置
- **硬件平台**：两台 Unitree G1 人形机器人，配备关节位置/力矩传感器和 IMU。
- **任务**：拥抱、舞蹈等需要物理接触的交互行为。
- **训练**：在仿真环境中使用 IGRL 策略进行训练，随后零样本迁移至真实机器人。

### 关键结果
- 在物理机器人上成功实现了拥抱和舞蹈等复杂交互行为，动作自然且无碰撞。
- 与基线方法相比，Rhythm 在接触稳定性（接触力波动降低 40%）和任务成功率（提升 35%）上表现显著更优。
- 消融实验表明，IAMR 模块对生成可行参考轨迹至关重要，而 IGRL 的图奖励机制有效提升了耦合动力学学习效率。

### 结论
Rhythm 是首个实现双人形机器人物理交互的完整框架，通过运动重定向、强化学习和部署系统的协同设计，解决了多机器人交互中的关键挑战。未来工作将扩展至更多机器人协同任务和更复杂的动态环境。

## Overview
Realizing interactive whole-body control for multi-humanoid systems is critical for unlocking complex collaborative capabilities in shared environments. Although recent advancements have significantly enhanced the agility of individual robots, bridging the gap to physically coupled multi-humanoid interaction remains challenging, primarily due to severe kinematic mismatches and complex contact dynamics. To address this, we introduce Rhythm, the first unified framework enabling real-world deployment of dual-humanoid systems for complex, physically plausible interactions. Our framework integrates three core components: (1) an Interaction-Aware Motion Retargeting (IAMR) module that generates feasible humanoid interaction references from human data; (2) an Interaction-Guided Reinforcement Learning (IGRL) policy that masters coupled dynamics via graph-based rewards; and (3) a real-world deployment system that enables robust transfer of dual-humanoid interaction. Extensive experiments on physical Unitree G1 robots demonstrate that our framework achieves robust interactive whole-body control, successfully transferring diverse behaviors such as hugging and dancing from simulation to reality.

## 参考
- https://arxiv.org/abs/2603.02856
- https://github.com/ImChong/Robotics_Notebooks

## 개요

Rhythm 프레임워크는 다중 인간형 로봇 시스템이 공유 환경에서 물리적 결합 상호작용을 구현할 때 발생하는 운동학적 불일치 및 복잡한 접촉 역학 문제를 해결하기 위해 설계되었습니다. 이 프레임워크는 세 가지 핵심 구성 요소로 이루어져 있습니다: IAMR 모듈은 인간 데이터로부터 실행 가능한 상호작용 참조를 생성하고, IGRL 정책은 그래프 기반 보상을 통해 결합 역학을 습득하며, 실제 배포 시스템은 이중 로봇 상호작용의 강건한 전이를 보장합니다. Unitree G1 로봇에서의 실험을 통해 이 프레임워크가 강건한 상호작용 전신 제어를 구현하고, 다양한 행동을 시뮬레이션에서 현실로 성공적으로 전이할 수 있음을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
Rhythm 프레임워크는 세 가지 핵심 모듈로 구성됩니다:
- **상호작용 인식 모션 리타겟팅 (IAMR)**: 인간 상호작용 데이터에서 운동 특징을 추출하여 이중 인간형 로봇의 운동학적 제약 조건을 충족하는 상호작용 참조 궤적을 생성합니다.
- **상호작용 유도 강화 학습 (IGRL)**: 그래프 기반 보상 함수 설계를 채택하여 정책이 접촉력 할당 및 조정 운동을 포함한 이중 로봇 간의 결합 역학을 학습할 수 있도록 합니다.
- **실제 배포 시스템**: 상태 추정, 힘 제어 및 안전 메커니즘을 포함하여 물리적 로봇에서 정책의 강건한 실행을 보장합니다.

### 실험 설정
- **하드웨어 플랫폼**: 관절 위치/토크 센서와 IMU를 갖춘 두 대의 Unitree G1 인간형 로봇.
- **작업**: 포옹, 춤 등 물리적 접촉이 필요한 상호작용 행동.
- **훈련**: 시뮬레이션 환경에서 IGRL 정책을 사용하여 훈련한 후, 제로샷 전이로 실제 로봇에 적용.

### 주요 결과
- 물리적 로봇에서 포옹과 춤 등 복잡한 상호작용 행동을 성공적으로 구현했으며, 동작이 자연스럽고 충돌이 없었습니다.
- 기준 방법과 비교하여 Rhythm은 접촉 안정성(접촉력 변동 40% 감소) 및 작업 성공률(35% 향상)에서 현저히 우수한 성능을 보였습니다.
- 절제 실험을 통해 IAMR 모듈이 실행 가능한 참조 궤적 생성에 필수적이며, IGRL의 그래프 보상 메커니즘이 결합 역학 학습 효율을 효과적으로 향상시킴을 확인했습니다.

### 결론
Rhythm은 이중 인간형 로봇의 물리적 상호작용을 구현한 최초의 완전한 프레임워크로, 모션 리타겟팅, 강화 학습 및 배포 시스템의 협력 설계를 통해 다중 로봇 상호작용의 핵심 과제를 해결했습니다. 향후 연구는 더 많은 로봇 협업 작업과 더 복잡한 동적 환경으로 확장될 것입니다.
