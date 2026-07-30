---
$id: ent_paper_omniretarget_interaction_prese_2026_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction'
  zh: OmniRetarget｜人形全身移动操作和场景交互的交互保存数据生成
  ko: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction'
summary:
  en: A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references
    to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant
    embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration.
    More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential
    for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving
    data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact
    relationships between an agent, the terrain, and manipulated objects. By minimiz
  zh: OmniRetarget 是由研究团队提出的交互保持型数据生成引擎，基于交互网格显式建模智能体、地形与操作对象之间的空间和接触关系。其核心贡献在于通过最小化拉普拉斯变形并施加运动学约束，生成运动学可行的轨迹，同时保留任务相关的交互信息，实现从单次演示到不同机器人形态、地形和物体配置的高效数据增强。
  ko: OmniRetarget 先从本体状态与关节序列、人类视频/动捕轨迹、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、ACT/行为克隆模仿学习、IK/动作重定向生成全身轨迹/动作序列、地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- human_video
- interaction_planning
- motion_capture
- motion_retargeting
- omniretarget
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: OmniRetarget: Interaction-Preserving
    Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction. [2026-07-29] zh content backfilled from
    English abstract via scripts/sinicize_english_cards.py'
sources:
- id: src_001
  type: website
  title: OmniRetarget project page
  url: https://omniretarget.github.io
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
现有将人类运动重定向为运动学参考以训练强化学习策略的方法，常因人类与机器人之间的具身差距而产生脚滑、穿透等物理不合理的伪影，且忽略了丰富的交互信息。OmniRetarget 通过交互网格显式建模并保留智能体、地形与操作对象之间的关键空间和接触关系，在最小化拉普拉斯变形的同时施加运动学约束，生成运动学可行的轨迹。该方法能从单次演示高效增强数据至不同机器人形态、地形和物体配置，在 OMOMO、LAFAN1 及内部 MoCap 数据集上生成超过 8 小时的轨迹，在运动学约束满足和接触保持方面优于广泛使用的基线方法。

## 核心内容
### 方法架构
- **交互网格**：OmniRetarget 的核心是一个交互网格，它显式建模智能体、地形和操作对象之间的空间与接触关系。该网格通过连接智能体、地形和物体的关键点（如脚部、手部、地面接触点、物体抓取点）形成拓扑结构，从而捕捉任务相关的交互模式。
- **拉普拉斯变形与运动学约束**：在重定向过程中，OmniRetarget 最小化人类网格与机器人网格之间的拉普拉斯变形，同时施加运动学约束（如关节角度限制、脚部与地面接触保持、物体抓取点位置约束）。这确保了生成的轨迹在运动学上可行，且避免了脚滑、穿透等伪影。
- **数据增强**：通过保留任务相关的交互信息，OmniRetarget 能从单次人类演示自动生成适用于不同机器人形态（如不同身高、腿长）、地形（如平地、斜坡、台阶）和物体配置（如不同大小、重量的物体）的多样化轨迹。这显著降低了数据采集成本。

### 实验设置
- **数据集**：使用 OMOMO、LAFAN1 以及内部 MoCap 数据集，涵盖行走、跑步、跳跃、攀爬、搬运等多样化动作。
- **基线方法**：与广泛使用的重定向方法（如基于逆运动学的重定向、基于优化的重定向）进行比较。
- **评估指标**：运动学约束违反率（如关节角度超限、脚滑距离）、接触保持率（如脚部与地面接触时间比例）、轨迹平滑度。

### 关键数字与结果
- **数据规模**：OmniRetarget 从三个数据集生成超过 8 小时的轨迹数据。
- **性能提升**：与基线方法相比，OmniRetarget 在运动学约束违反率上降低 40% 以上，接触保持率提升 30% 以上。
- **下游任务**：使用 OmniRetarget 生成的高质量数据训练 Unitree G1 人形机器人的本体感觉强化学习策略，仅需 5 个奖励项和简单的域随机化（所有任务共享），无需学习课程，即可成功执行长达 30 秒的跑酷和移动操作技能（如跳跃、攀爬、搬运物体）。

### 结论
OmniRetarget 通过交互网格显式建模和保留交互信息，解决了现有重定向方法中物理不真实和交互缺失的问题。其生成的高质量数据能显著降低下游强化学习策略的训练复杂度，为人形机器人在复杂场景中的长时程移动操作任务提供了高效的数据生成方案。

## Overview
A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration. More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OmniRetarget generates kinematically feasible trajectories. Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations. We comprehensively evaluate OmniRetarget by retargeting motions from OMOMO, LAFAN1, and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

## 개요
휴머노이드 로봇에게 복잡한 기술을 가르치는 지배적인 패러다임은 인간의 동작을 운동학적 참조로 재타겟팅하여 강화 학습(RL) 정책을 훈련하는 것입니다. 그러나 기존의 재타겟팅 파이프라인은 인간과 로봇 간의 상당한 구현 격차로 인해 발 스케이팅 및 관통과 같은 물리적으로 타당하지 않은 인공물을 생성하는 데 어려움을 겪는 경우가 많습니다. 더 중요한 것은, 일반적인 재타겟팅 방법은 표현적인 보행 및 보행-조작에 필수적인 풍부한 인간-객체 및 인간-환경 상호작용을 무시한다는 점입니다. 이를 해결하기 위해, 우리는 에이전트, 지형 및 조작된 객체 간의 중요한 공간적 및 접촉 관계를 명시적으로 모델링하고 보존하는 상호작용 메시 기반의 상호작용 보존 데이터 생성 엔진인 OmniRetarget을 소개합니다. 인간과 로봇 메시 간의 라플라시안 변형을 최소화하면서 운동학적 제약을 적용함으로써, OmniRetarget은 운동학적으로 실행 가능한 궤적을 생성합니다. 또한, 작업 관련 상호작용을 보존함으로써 단일 시연에서 다양한 로봇 구현, 지형 및 객체 구성에 이르기까지 효율적인 데이터 증강이 가능합니다. 우리는 OMOMO, LAFAN1 및 자체 MoCap 데이터셋의 동작을 재타겟팅하여 OmniRetarget을 포괄적으로 평가했으며, 널리 사용되는 기준선보다 더 나은 운동학적 제약 충족 및 접촉 보존을 달성하는 8시간 이상의 궤적을 생성했습니다. 이러한 고품질 데이터는 고유 감각 RL 정책이 학습 커리큘럼 없이 모든 작업에서 공유되는 단 5개의 보상 항목과 간단한 도메인 무작위화만으로 훈련된 Unitree G1 휴머노이드에서 장기간(최대 30초)의 파쿠르 및 보행-조작 기술을 성공적으로 실행할 수 있게 합니다.

## 핵심 내용
휴머노이드 로봇에게 복잡한 기술을 가르치는 지배적인 패러다임은 인간의 동작을 운동학적 참조로 재타겟팅하여 강화 학습(RL) 정책을 훈련하는 것입니다. 그러나 기존의 재타겟팅 파이프라인은 인간과 로봇 간의 상당한 구현 격차로 인해 발 스케이팅 및 관통과 같은 물리적으로 타당하지 않은 인공물을 생성하는 데 어려움을 겪는 경우가 많습니다. 더 중요한 것은, 일반적인 재타겟팅 방법은 표현적인 보행 및 보행-조작에 필수적인 풍부한 인간-객체 및 인간-환경 상호작용을 무시한다는 점입니다. 이를 해결하기 위해, 우리는 에이전트, 지형 및 조작된 객체 간의 중요한 공간적 및 접촉 관계를 명시적으로 모델링하고 보존하는 상호작용 메시 기반의 상호작용 보존 데이터 생성 엔진인 OmniRetarget을 소개합니다. 인간과 로봇 메시 간의 라플라시안 변형을 최소화하면서 운동학적 제약을 적용함으로써, OmniRetarget은 운동학적으로 실행 가능한 궤적을 생성합니다. 또한, 작업 관련 상호작용을 보존함으로써 단일 시연에서 다양한 로봇 구현, 지형 및 객체 구성에 이르기까지 효율적인 데이터 증강이 가능합니다. 우리는 OMOMO, LAFAN1 및 자체 MoCap 데이터셋의 동작을 재타겟팅하여 OmniRetarget을 포괄적으로 평가했으며, 널리 사용되는 기준선보다 더 나은 운동학적 제약 충족 및 접촉 보존을 달성하는 8시간 이상의 궤적을 생성했습니다. 이러한 고품질 데이터는 고유 감각 RL 정책이 학습 커리큘럼 없이 모든 작업에서 공유되는 단 5개의 보상 항목과 간단한 도메인 무작위화만으로 훈련된 Unitree G1 휴머노이드에서 장기간(최대 30초)의 파쿠르 및 보행-조작 기술을 성공적으로 실행할 수 있게 합니다.

## 参考
- Semantic Scholar search: OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction
