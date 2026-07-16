---
$id: ent_paper_humanoid_goalkeeper_learning_f_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints'
  zh: Humanoid｜Goalkeeper 从位置条件任务运动约束中学习
  ko: 'Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints'
summary:
  en: 'We present a reinforcement learning framework for autonomous goalkeeping with humanoid robots in real-world scenarios.
    While prior work has demonstrated similar capabilities on quadrupedal platforms, humanoid goalkeeping introduces two critical
    challenges: (1) generating natural, human-like whole-body motions, and (2) covering a wider guarding range with an equivalent
    response time. Unlike existing approaches that rely on separate teleoperation or fixed motion tracking for whole-body
    control, our method learns a single end-to-end RL policy, enabling fully autonomous, highly dynamic, and human-like robot-object
    interactions. To achieve this, we integrate multiple human motion priors conditioned on perceptual inputs into the RL
    training via an adversarial scheme. We demonstrate the effective'
  zh: Humanoid 主要解决数据闭环：用人类视频/动捕轨迹、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配转成可训练、可复用的可执行动作命令。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: Humanoid 主要解决数据闭环：用人类视频/动捕轨迹、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过PPO/RL 策略训练、AMP/运动先验、扩散策略/流匹配转成可训练、可复用的可执行动作命令。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
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
- humanoid
- interaction_planning
- motion_capture
- motion_retargeting
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: Humanoid Goalkeeper: Learning
    from Position Conditioned Task-Motion Constraints.'
sources:
- id: src_001
  type: website
  title: Humanoid project page
  url: https://github.com/InternRobotics/Humanoid-Goalkeeper
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
We present a reinforcement learning framework for autonomous goalkeeping with humanoid robots in real-world scenarios. While prior work has demonstrated similar capabilities on quadrupedal platforms, humanoid goalkeeping introduces two critical challenges: (1) generating natural, human-like whole-body motions, and (2) covering a wider guarding range with an equivalent response time. Unlike existing approaches that rely on separate teleoperation or fixed motion tracking for whole-body control, our method learns a single end-to-end RL policy, enabling fully autonomous, highly dynamic, and human-like robot-object interactions. To achieve this, we integrate multiple human motion priors conditioned on perceptual inputs into the RL training via an adversarial scheme. We demonstrate the effectiveness of our method through real-world experiments, where the humanoid robot successfully performs agile, autonomous, and naturalistic interceptions of fast-moving balls. In addition to goalkeeping, we demonstrate the generalization of our approach through tasks such as ball escaping and grabbing. Our work presents a practical and scalable solution for enabling highly dynamic interactions between robots and moving objects, advancing the field toward more adaptive and lifelike robotic behaviors.

## 核心内容
We present a reinforcement learning framework for autonomous goalkeeping with humanoid robots in real-world scenarios. While prior work has demonstrated similar capabilities on quadrupedal platforms, humanoid goalkeeping introduces two critical challenges: (1) generating natural, human-like whole-body motions, and (2) covering a wider guarding range with an equivalent response time. Unlike existing approaches that rely on separate teleoperation or fixed motion tracking for whole-body control, our method learns a single end-to-end RL policy, enabling fully autonomous, highly dynamic, and human-like robot-object interactions. To achieve this, we integrate multiple human motion priors conditioned on perceptual inputs into the RL training via an adversarial scheme. We demonstrate the effectiveness of our method through real-world experiments, where the humanoid robot successfully performs agile, autonomous, and naturalistic interceptions of fast-moving balls. In addition to goalkeeping, we demonstrate the generalization of our approach through tasks such as ball escaping and grabbing. Our work presents a practical and scalable solution for enabling highly dynamic interactions between robots and moving objects, advancing the field toward more adaptive and lifelike robotic behaviors.

## 参考
- Semantic Scholar search: Humanoid Goalkeeper: Learning from Position Conditioned Task-Motion Constraints

## Overview
We present a reinforcement learning framework for autonomous goalkeeping with humanoid robots in real-world scenarios. While prior work has demonstrated similar capabilities on quadrupedal platforms, humanoid goalkeeping introduces two critical challenges: (1) generating natural, human-like whole-body motions, and (2) covering a wider guarding range with an equivalent response time. Unlike existing approaches that rely on separate teleoperation or fixed motion tracking for whole-body control, our method learns a single end-to-end RL policy, enabling fully autonomous, highly dynamic, and human-like robot-object interactions. To achieve this, we integrate multiple human motion priors conditioned on perceptual inputs into the RL training via an adversarial scheme. We demonstrate the effectiveness of our method through real-world experiments, where the humanoid robot successfully performs agile, autonomous, and naturalistic interceptions of fast-moving balls. In addition to goalkeeping, we demonstrate the generalization of our approach through tasks such as ball escaping and grabbing. Our work presents a practical and scalable solution for enabling highly dynamic interactions between robots and moving objects, advancing the field toward more adaptive and lifelike robotic behaviors.

## Content
We present a reinforcement learning framework for autonomous goalkeeping with humanoid robots in real-world scenarios. While prior work has demonstrated similar capabilities on quadrupedal platforms, humanoid goalkeeping introduces two critical challenges: (1) generating natural, human-like whole-body motions, and (2) covering a wider guarding range with an equivalent response time. Unlike existing approaches that rely on separate teleoperation or fixed motion tracking for whole-body control, our method learns a single end-to-end RL policy, enabling fully autonomous, highly dynamic, and human-like robot-object interactions. To achieve this, we integrate multiple human motion priors conditioned on perceptual inputs into the RL training via an adversarial scheme. We demonstrate the effectiveness of our method through real-world experiments, where the humanoid robot successfully performs agile, autonomous, and naturalistic interceptions of fast-moving balls. In addition to goalkeeping, we demonstrate the generalization of our approach through tasks such as ball escaping and grabbing. Our work presents a practical and scalable solution for enabling highly dynamic interactions between robots and moving objects, advancing the field toward more adaptive and lifelike robotic behaviors.

## 개요
본 논문은 실제 환경에서 휴머노이드 로봇의 자율 골키퍼를 위한 강화 학습 프레임워크를 제시합니다. 이전 연구에서 사족 보행 플랫폼에서 유사한 기능이 입증되었지만, 휴머노이드 골키퍼는 두 가지 중요한 과제를 제기합니다: (1) 자연스럽고 인간과 유사한 전신 동작 생성, (2) 동등한 반응 시간으로 더 넓은 방어 범위를 커버하는 것입니다. 전신 제어를 위해 별도의 원격 조작이나 고정된 동작 추적에 의존하는 기존 접근 방식과 달리, 우리의 방법은 단일 종단 간 강화 학습 정책을 학습하여 완전 자율적이고 고도로 동적이며 인간과 유사한 로봇-객체 상호 작용을 가능하게 합니다. 이를 위해, 우리는 지각 입력에 조건화된 여러 인간 동작 사전 정보를 적대적 방식을 통해 강화 학습 훈련에 통합합니다. 우리는 실제 실험을 통해 휴머노이드 로봇이 빠르게 움직이는 공을 민첩하고 자율적이며 자연스럽게 차단하는 데 성공함으로써 방법의 효과를 입증합니다. 골키퍼 외에도 공 탈출 및 잡기와 같은 작업을 통해 접근 방식의 일반화를 보여줍니다. 우리의 연구는 로봇과 움직이는 객체 간의 고도로 동적인 상호 작용을 가능하게 하는 실용적이고 확장 가능한 솔루션을 제시하며, 더 적응적이고 생생한 로봇 행동을 향한 분야를 발전시킵니다.

## 핵심 내용
본 논문은 실제 환경에서 휴머노이드 로봇의 자율 골키퍼를 위한 강화 학습 프레임워크를 제시합니다. 이전 연구에서 사족 보행 플랫폼에서 유사한 기능이 입증되었지만, 휴머노이드 골키퍼는 두 가지 중요한 과제를 제기합니다: (1) 자연스럽고 인간과 유사한 전신 동작 생성, (2) 동등한 반응 시간으로 더 넓은 방어 범위를 커버하는 것입니다. 전신 제어를 위해 별도의 원격 조작이나 고정된 동작 추적에 의존하는 기존 접근 방식과 달리, 우리의 방법은 단일 종단 간 강화 학습 정책을 학습하여 완전 자율적이고 고도로 동적이며 인간과 유사한 로봇-객체 상호 작용을 가능하게 합니다. 이를 위해, 우리는 지각 입력에 조건화된 여러 인간 동작 사전 정보를 적대적 방식을 통해 강화 학습 훈련에 통합합니다. 우리는 실제 실험을 통해 휴머노이드 로봇이 빠르게 움직이는 공을 민첩하고 자율적이며 자연스럽게 차단하는 데 성공함으로써 방법의 효과를 입증합니다. 골키퍼 외에도 공 탈출 및 잡기와 같은 작업을 통해 접근 방식의 일반화를 보여줍니다. 우리의 연구는 로봇과 움직이는 객체 간의 고도로 동적인 상호 작용을 가능하게 하는 실용적이고 확장 가능한 솔루션을 제시하며, 더 적응적이고 생생한 로봇 행동을 향한 분야를 발전시킵니다.
