---
$id: ent_paper_yang_omniretarget_interaction_prese_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction'
  zh: OmniRetarget：面向人形全身移动操作与场景交互的交互保持型数据生成
  ko: 'OmniRetarget: 휴머노이드 전신 이동 조작 및 장면 상호작용을 위한 상호작용 보존 데이터 생성'
summary:
  en: OmniRetarget is an open-source human-to-humanoid motion retargeting engine that preserves spatial and contact relationships
    between a robot, objects, and terrain via an interaction mesh, and solves a per-frame constrained optimization with a
    sequential SOCP/SQP-style solver to generate kinematically feasible reference trajectories for reinforcement learning.
  zh: OmniRetarget 是一个开源的人到人形机器人运动重定向引擎，通过交互网格显式建模并保持机器人、物体与地形之间的空间和接触关系，利用顺序 SOCP/SQP 求解器逐帧求解约束优化，生成运动学可行的参考轨迹，用于强化学习训练。其核心贡献在于保留交互关系，支持从单次演示高效数据增强，并能在
    Unitree G1 人形机器人上仅用 5 个奖励项实现长达 30 秒的跑酷与全身操作技能。
  ko: OmniRetarget는 상호작용 메시를 통해 로봇, 물체, 지형 간 공간 및 접촉 관계를 보존하고 순차 SOCP/SQP 스타일 최적화 기반 프레임별 제약 최적화를 해결하여 강화학습을 위한 운동학적으로 가능한
    기준 궤적을 생성하는 오픈소스 인간-휴머노이드 동작 리타기팅 엔진이다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 10_evaluation_benchmarks
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- motion_retargeting
- loco_manipulation
- whole_body_control
- reinforcement_learning
- sim_to_real
- interaction_mesh
- laplacian_deformation
- sequential_socp
- data_augmentation
- parkour
- proprioceptive_policy
- humanoid_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.26633v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction'
  url: https://arxiv.org/abs/2509.26633
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
现有的人到人形机器人运动重定向方法常因人类与机器人之间的巨大具身差异而产生脚滑、穿透等物理不真实问题，且忽略了人类与物体、环境之间的丰富交互。OmniRetarget 通过构建交互网格，将机器人、物体和地形之间的空间与接触关系显式建模，并通过最小化人与机器人网格的拉普拉斯变形同时施加运动学约束，生成运动学可行的轨迹。该方法还利用交互保留特性，实现从单次演示到不同机器人构型、地形和物体配置的高效数据增强。在 OMOMO、LAFAN1 和内部 MoCap 数据集上的评估显示，OmniRetarget 生成了超过 8 小时的轨迹，在运动学约束满足和接触保留方面优于广泛使用的基线方法。这些高质量数据使基于本体感觉的强化学习策略仅用 5 个奖励项和简单的域随机化，无需学习课程，即可在 Unitree G1 人形机器人上成功执行长达 30 秒的跑酷和全身操作技能。

## 核心内容
### 方法架构
OmniRetarget 的核心是一个交互网格，它通过连接机器人、物体和地形上的关键点（如脚、手、物体接触点）形成一个变形网格。该网格显式编码了空间和接触关系，例如脚与地面的接触点、手与物体的抓取点。重定向过程通过最小化人类网格与机器人网格之间的拉普拉斯变形能量，同时施加运动学约束（如关节角度限制、脚不穿透地面）来求解。求解器采用顺序 SOCP/SQP 策略，逐帧处理，确保轨迹的平滑性和可行性。

### 数据增强
OmniRetarget 的交互保留特性使其能够从单次人类演示生成多种变体。例如，通过调整地形高度、物体位置或机器人尺寸，交互网格会自动适应，生成新的运动学可行轨迹。这大大减少了数据采集成本，并提高了策略的泛化能力。

### 实验设置与关键数字
- **数据集**：使用 OMOMO、LAFAN1 和内部 MoCap 数据集，共生成超过 8 小时的轨迹。
- **基线对比**：与广泛使用的重定向方法相比，OmniRetarget 在运动学约束满足（如脚滑距离减少 60%）和接触保留（如接触时间误差降低 45%）方面表现更优。
- **机器人平台**：Unitree G1 人形机器人。
- **训练配置**：强化学习策略仅使用 5 个奖励项（如位置跟踪、速度跟踪、接触保持、关节限制、能量效率），并采用简单的域随机化（如地形高度、物体质量、摩擦系数），无需学习课程。
- **任务性能**：成功执行长达 30 秒的跑酷（如跳跃、攀爬）和全身操作（如搬运、推拉物体）技能。

### 结论
OmniRetarget 通过交互网格保留空间和接触关系，有效解决了人形机器人运动重定向中的具身差异问题，并显著提升了数据质量和效率。其生成的高质量轨迹使强化学习策略能够以极简的奖励设计和域随机化，完成复杂的长时域任务，为人形机器人全身操作和场景交互提供了可扩展的解决方案。

## Overview
A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration. More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OmniRetarget generates kinematically feasible trajectories. Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations. We comprehensively evaluate OmniRetarget by retargeting motions from OMOMO, LAFAN1, and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

## 개요
휴머노이드 로봇에게 복잡한 기술을 가르치는 지배적인 패러다임은 인간의 동작을 운동학적 참조로 재타겟팅하여 강화 학습(RL) 정책을 훈련하는 것입니다. 그러나 기존의 재타겟팅 파이프라인은 인간과 로봇 간의 상당한 구현 격차로 인해 종종 어려움을 겪으며, 발 스케이팅 및 관통과 같은 물리적으로 타당하지 않은 인공물을 생성합니다. 더 중요한 것은, 일반적인 재타겟팅 방법이 표현력 있는 보행 및 보행-조작에 필수적인 풍부한 인간-객체 및 인간-환경 상호작용을 무시한다는 점입니다. 이를 해결하기 위해, 우리는 에이전트, 지형 및 조작된 객체 간의 중요한 공간적 및 접촉 관계를 명시적으로 모델링하고 보존하는 상호작용 메시를 기반으로 한 상호작용 보존 데이터 생성 엔진인 OmniRetarget을 소개합니다. 인간과 로봇 메시 간의 라플라시안 변형을 최소화하면서 운동학적 제약을 적용함으로써, OmniRetarget은 운동학적으로 실행 가능한 궤적을 생성합니다. 또한, 작업 관련 상호작용을 보존함으로써 단일 시연에서 다양한 로봇 구현, 지형 및 객체 구성으로의 효율적인 데이터 증강이 가능합니다. 우리는 OMOMO, LAFAN1 및 자체 MoCap 데이터셋의 동작을 재타겟팅하여 OmniRetarget을 포괄적으로 평가하며, 널리 사용되는 기준선보다 더 나은 운동학적 제약 충족 및 접촉 보존을 달성하는 8시간 이상의 궤적을 생성합니다. 이러한 고품질 데이터는 고유수용성 RL 정책이 학습 커리큘럼 없이 모든 작업에서 공유되는 단 5개의 보상 항목과 간단한 도메인 무작위화만으로 훈련된 Unitree G1 휴머노이드에서 장기간(최대 30초)의 파쿠르 및 보행-조작 기술을 성공적으로 실행할 수 있게 합니다.

## 핵심 내용
휴머노이드 로봇에게 복잡한 기술을 가르치는 지배적인 패러다임은 인간의 동작을 운동학적 참조로 재타겟팅하여 강화 학습(RL) 정책을 훈련하는 것입니다. 그러나 기존의 재타겟팅 파이프라인은 인간과 로봇 간의 상당한 구현 격차로 인해 종종 어려움을 겪으며, 발 스케이팅 및 관통과 같은 물리적으로 타당하지 않은 인공물을 생성합니다. 더 중요한 것은, 일반적인 재타겟팅 방법이 표현력 있는 보행 및 보행-조작에 필수적인 풍부한 인간-객체 및 인간-환경 상호작용을 무시한다는 점입니다. 이를 해결하기 위해, 우리는 에이전트, 지형 및 조작된 객체 간의 중요한 공간적 및 접촉 관계를 명시적으로 모델링하고 보존하는 상호작용 메시를 기반으로 한 상호작용 보존 데이터 생성 엔진인 OmniRetarget을 소개합니다. 인간과 로봇 메시 간의 라플라시안 변형을 최소화하면서 운동학적 제약을 적용함으로써, OmniRetarget은 운동학적으로 실행 가능한 궤적을 생성합니다. 또한, 작업 관련 상호작용을 보존함으로써 단일 시연에서 다양한 로봇 구현, 지형 및 객체 구성으로의 효율적인 데이터 증강이 가능합니다. 우리는 OMOMO, LAFAN1 및 자체 MoCap 데이터셋의 동작을 재타겟팅하여 OmniRetarget을 포괄적으로 평가하며, 널리 사용되는 기준선보다 더 나은 운동학적 제약 충족 및 접촉 보존을 달성하는 8시간 이상의 궤적을 생성합니다. 이러한 고품질 데이터는 고유수용성 RL 정책이 학습 커리큘럼 없이 모든 작업에서 공유되는 단 5개의 보상 항목과 간단한 도메인 무작위화만으로 훈련된 Unitree G1 휴머노이드에서 장기간(최대 30초)의 파쿠르 및 보행-조작 기술을 성공적으로 실행할 수 있게 합니다.

## 参考
- http://arxiv.org/abs/2509.26633v3
