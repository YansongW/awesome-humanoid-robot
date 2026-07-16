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
  zh: OmniRetarget 先从本体状态与关节序列、人类视频/动捕轨迹、接触力/触觉信号恢复场景、目标或运动表征，再用PPO/RL 策略训练、ACT/行为克隆模仿学习、IK/动作重定向生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把任务拆成可路由的技能或专家策略，再用高层模块在执行中选择和组合。
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
    Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction.'
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
A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration. More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OmniRetarget generates kinematically feasible trajectories. Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations. We comprehensively evaluate OmniRetarget by retargeting motions from OMOMO, LAFAN1, and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

## 核心内容
A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration. More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OmniRetarget generates kinematically feasible trajectories. Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations. We comprehensively evaluate OmniRetarget by retargeting motions from OMOMO, LAFAN1, and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

## 参考
- Semantic Scholar search: OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction

## Overview
A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration. More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OmniRetarget generates kinematically feasible trajectories. Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations. We comprehensively evaluate OmniRetarget by retargeting motions from OMOMO, LAFAN1, and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

## Content
A dominant paradigm for teaching humanoid robots complex skills is to retarget human motions as kinematic references to train reinforcement learning (RL) policies. However, existing retargeting pipelines often struggle with the significant embodiment gap between humans and robots, producing physically implausible artifacts like foot-skating and penetration. More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation. To address this, we introduce OmniRetarget, an interaction-preserving data generation engine based on an interaction mesh that explicitly models and preserves the crucial spatial and contact relationships between an agent, the terrain, and manipulated objects. By minimizing the Laplacian deformation between the human and robot meshes while enforcing kinematic constraints, OmniRetarget generates kinematically feasible trajectories. Moreover, preserving task-relevant interactions enables efficient data augmentation, from a single demonstration to different robot embodiments, terrains, and object configurations. We comprehensively evaluate OmniRetarget by retargeting motions from OMOMO, LAFAN1, and our in-house MoCap datasets, generating over 8-hour trajectories that achieve better kinematic constraint satisfaction and contact preservation than widely used baselines. Such high-quality data enables proprioceptive RL policies to successfully execute long-horizon (up to 30 seconds) parkour and loco-manipulation skills on a Unitree G1 humanoid, trained with only 5 reward terms and simple domain randomization shared by all tasks, without any learning curriculum.

## 개요
휴머노이드 로봇에게 복잡한 기술을 가르치는 지배적인 패러다임은 인간의 동작을 운동학적 참조로 재타겟팅하여 강화 학습(RL) 정책을 훈련하는 것입니다. 그러나 기존의 재타겟팅 파이프라인은 인간과 로봇 사이의 상당한 구현 격차로 인해 종종 어려움을 겪으며, 발 스케이팅 및 관통과 같은 물리적으로 타당하지 않은 인공물을 생성합니다. 더 중요하게는, 일반적인 재타겟팅 방법은 표현적인 보행 및 보행-조작에 필수적인 풍부한 인간-객체 및 인간-환경 상호작용을 무시합니다. 이를 해결하기 위해, 우리는 에이전트, 지형 및 조작된 객체 간의 중요한 공간적 및 접촉 관계를 명시적으로 모델링하고 보존하는 상호작용 메시를 기반으로 한 상호작용 보존 데이터 생성 엔진인 OmniRetarget을 소개합니다. 인간과 로봇 메시 간의 라플라시안 변형을 최소화하면서 운동학적 제약을 적용함으로써, OmniRetarget은 운동학적으로 실행 가능한 궤적을 생성합니다. 또한, 작업 관련 상호작용을 보존함으로써 단일 데모에서 다양한 로봇 구현, 지형 및 객체 구성으로의 효율적인 데이터 증강이 가능합니다. 우리는 OMOMO, LAFAN1 및 자체 MoCap 데이터셋의 동작을 재타겟팅하여 OmniRetarget을 포괄적으로 평가하며, 널리 사용되는 기준선보다 더 나은 운동학적 제약 충족 및 접촉 보존을 달성하는 8시간 이상의 궤적을 생성합니다. 이러한 고품질 데이터는 고유수용성 RL 정책이 Unitree G1 휴머노이드에서 장기간(최대 30초)의 파쿠르 및 보행-조작 기술을 성공적으로 실행할 수 있게 하며, 모든 작업에서 공유되는 단 5개의 보상 항목과 간단한 도메인 무작위화로 훈련되며 학습 커리큘럼이 없습니다.

## 핵심 내용
휴머노이드 로봇에게 복잡한 기술을 가르치는 지배적인 패러다임은 인간의 동작을 운동학적 참조로 재타겟팅하여 강화 학습(RL) 정책을 훈련하는 것입니다. 그러나 기존의 재타겟팅 파이프라인은 인간과 로봇 사이의 상당한 구현 격차로 인해 종종 어려움을 겪으며, 발 스케이팅 및 관통과 같은 물리적으로 타당하지 않은 인공물을 생성합니다. 더 중요하게는, 일반적인 재타겟팅 방법은 표현적인 보행 및 보행-조작에 필수적인 풍부한 인간-객체 및 인간-환경 상호작용을 무시합니다. 이를 해결하기 위해, 우리는 에이전트, 지형 및 조작된 객체 간의 중요한 공간적 및 접촉 관계를 명시적으로 모델링하고 보존하는 상호작용 메시를 기반으로 한 상호작용 보존 데이터 생성 엔진인 OmniRetarget을 소개합니다. 인간과 로봇 메시 간의 라플라시안 변형을 최소화하면서 운동학적 제약을 적용함으로써, OmniRetarget은 운동학적으로 실행 가능한 궤적을 생성합니다. 또한, 작업 관련 상호작용을 보존함으로써 단일 데모에서 다양한 로봇 구현, 지형 및 객체 구성으로의 효율적인 데이터 증강이 가능합니다. 우리는 OMOMO, LAFAN1 및 자체 MoCap 데이터셋의 동작을 재타겟팅하여 OmniRetarget을 포괄적으로 평가하며, 널리 사용되는 기준선보다 더 나은 운동학적 제약 충족 및 접촉 보존을 달성하는 8시간 이상의 궤적을 생성합니다. 이러한 고품질 데이터는 고유수용성 RL 정책이 Unitree G1 휴머노이드에서 장기간(최대 30초)의 파쿠르 및 보행-조작 기술을 성공적으로 실행할 수 있게 하며, 모든 작업에서 공유되는 단 5개의 보상 항목과 간단한 도메인 무작위화로 훈련되며 학습 커리큘럼이 없습니다.
