---
$id: ent_paper_omniretarget_interaction_prese_2026
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
  zh: OmniRetarget 是由研究团队提出的交互保持型数据生成引擎，基于交互网格显式建模智能体、地形与操作对象之间的空间和接触关系。其核心贡献在于通过最小化拉普拉斯变形并施加运动学约束，生成物理可行的轨迹，同时保留任务相关的交互信息，实现从单次演示到不同机器人形态、地形和物体配置的高效数据增强。
  ko: OmniRetarget 先从本体状态与关节序列、人类视频/动捕轨迹、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、ACT/行为克隆模仿学习、IK/动作重定向生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
domains:
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- balance
- behavioral_foundation_model
- locomotion
- motion_tracking
- omniretarget
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: OmniRetarget: Interaction-Preserving
    Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction. [2026-07-29] zh content backfilled from
    English abstract via scripts/sinicize_english_cards.py | WP1 dedup merge 2026-08-06: merged ent_paper_omniretarget_interaction_prese_2026,
    ent_paper_omniretarget_interaction_prese_2026 into this card (rules: same_title_same_year, suffix_reingest). Backup+manifest:
    .staging/cleanup_wp12/. | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (820 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: OmniRetarget project page
  url: https://omniretarget.github.io
  date: '2026'
  accessed_at: '2026-06-26'
- id: src_002
  type: paper
  title: 'OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction'
  url: https://arxiv.org/abs/2509.26633
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
现有的人形机器人技能学习范式通常将人类运动重定向为运动学参考来训练强化学习策略，但受限于人机形态差异，常产生脚滑、穿透等物理不合理的伪影，且忽略了人类与环境、物体之间的丰富交互。OmniRetarget 基于交互网格显式建模并保留智能体、地形与操作对象之间的关键空间和接触关系，通过最小化拉普拉斯变形并施加运动学约束，生成运动学可行的轨迹。该方法还能通过保留任务相关交互实现高效数据增强，从单次演示扩展到不同机器人形态、地形和物体配置。实验在 OMOMO、LAFAN1 及内部 MoCap 数据集上生成超过 8 小时的轨迹，在运动学约束满足和接触保留方面优于广泛使用的基线方法。

## 核心内容
### 方法架构
- **交互网格**：显式建模智能体、地形与操作对象之间的空间和接触关系，保留关键交互信息。
- **拉普拉斯变形最小化**：在人类与机器人网格之间最小化拉普拉斯变形，同时施加运动学约束，生成物理可行的轨迹。
- **数据增强**：通过保留任务相关交互，实现从单次演示到不同机器人形态、地形和物体配置的高效扩展。

### 实验设置
- **数据集**：使用 OMOMO、LAFAN1 及内部 MoCap 数据集进行重定向，生成超过 8 小时的轨迹。
- **基线方法**：与广泛使用的基线方法对比，OmniRetarget 在运动学约束满足和接触保留方面表现更优。
- **机器人平台**：Unitree G1 人形机器人。
- **训练配置**：仅使用 5 个奖励项和简单的域随机化（所有任务共享），无需学习课程。

### 关键结果
- **轨迹质量**：生成的轨迹在运动学约束满足和接触保留方面显著优于基线方法。
- **技能执行**：训练后的本体感知强化学习策略成功执行长达 30 秒的跑酷和移动操作技能。
- **数据效率**：从单次演示即可高效生成适用于不同机器人形态、地形和物体配置的多样化数据。

## Overview
A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration. More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OmniRetarget generates kinematically feasible trajectories. Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations. We comprehensively evaluate OmniRetarget by retargeting motions from OMOMO, LAFAN1, and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

## 参考
- Semantic Scholar search: OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction

## 개요
기존의 휴머노이드 로봇 스킬 학습 패러다임은 일반적으로 인간의 움직임을 운동학적 참조로 재타겟팅하여 강화 학습 정책을 훈련하지만, 인간-로봇 형태 차이로 인해 발 미끄러짐, 관통 등 물리적으로 비합리적인 아티팩트가 자주 발생하며, 인간과 환경 및 객체 간의 풍부한 상호작용을 무시합니다. OmniRetarget은 상호작용 메시를 기반으로 에이전트, 지형 및 조작 객체 간의 핵심 공간 및 접촉 관계를 명시적으로 모델링하고 보존하며, 라플라시안 변형을 최소화하고 운동학적 제약을 적용하여 운동학적으로 실행 가능한 궤적을 생성합니다. 이 방법은 또한 작업 관련 상호작용을 보존하여 효율적인 데이터 증강을 가능하게 하며, 단일 데모에서 다양한 로봇 형태, 지형 및 객체 구성으로 확장합니다. 실험은 OMOMO, LAFAN1 및 내부 MoCap 데이터셋에서 8시간 이상의 궤적을 생성하며, 운동학적 제약 충족 및 접촉 보존 측면에서 널리 사용되는 기준 방법보다 우수합니다.

## 핵심 내용
### 방법 아키텍처
- **상호작용 메시**: 에이전트, 지형 및 조작 객체 간의 공간 및 접촉 관계를 명시적으로 모델링하여 핵심 상호작용 정보를 보존합니다.
- **라플라시안 변형 최소화**: 인간과 로봇 메시 간의 라플라시안 변형을 최소화하면서 운동학적 제약을 적용하여 물리적으로 실행 가능한 궤적을 생성합니다.
- **데이터 증강**: 작업 관련 상호작용을 보존하여 단일 데모에서 다양한 로봇 형태, 지형 및 객체 구성으로 효율적으로 확장합니다.

### 실험 설정
- **데이터셋**: OMOMO, LAFAN1 및 내부 MoCap 데이터셋을 사용하여 재타겟팅하고 8시간 이상의 궤적을 생성합니다.
- **기준 방법**: 널리 사용되는 기준 방법과 비교하여 OmniRetarget은 운동학적 제약 충족 및 접촉 보존 측면에서 더 우수한 성능을 보입니다.
- **로봇 플랫폼**: Unitree G1 휴머노이드 로봇.
- **훈련 구성**: 5개의 보상 항목과 간단한 도메인 무작위화(모든 작업 공유)만 사용하며 학습 커리큘럼은 필요하지 않습니다.

### 핵심 결과
- **궤적 품질**: 생성된 궤적은 운동학적 제약 충족 및 접촉 보존 측면에서 기준 방법보다 현저히 우수합니다.
- **스킬 실행**: 훈련된 본체 감각 강화 학습 정책은 최대 30초 동안의 파쿠르 및 이동 조작 스킬을 성공적으로 실행합니다.
- **데이터 효율성**: 단일 데모에서 다양한 로봇 형태, 지형 및 객체 구성에 적합한 다양한 데이터를 효율적으로 생성할 수 있습니다.
