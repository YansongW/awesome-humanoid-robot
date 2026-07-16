---
$id: ent_paper_he_learning_getting_up_policies_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Getting-Up Policies for Real-World Humanoid Robots
  zh: 面向现实世界人形机器人的起身策略学习
  ko: 실제 세계 휴머노이드 로봇을 위한 일어서기 정책 학습
summary:
  en: Introduces HUMANUP, a two-stage reinforcement-learning framework that learns getting-up controllers for humanoid robots,
    enabling a Unitree G1 to recover from supine and prone lying poses on flat, deformable, slippery, and sloped terrains.
  zh: 提出 HUMANUP，一个两阶段强化学习框架，用于学习人形机器人的起身控制器，使 Unitree G1 能够在平地、可变形地面、湿滑地面和斜坡上从仰卧和俯卧姿势恢复站立。
  ko: 휴머노이드 로봇을 위한 일어서기 컨트롤러를 학습하는 두 단계 강화학습 프레임워크인 HUMANUP을 소개하며, Unitree G1이 평지, 가변형 지면, 미끄러운 지면 및 경사면에서 엎드린 자세와 누운 자세에서
    복귀할 수 있도록 함.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- reinforcement_learning
- sim_to_real
- fall_recovery
- whole_body_control
- unitree_g1
- isaac_gym
- domain_randomization
- contact_rich_motion
- humanoid_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.12152v2.
sources:
- id: src_001
  type: paper
  title: Learning Getting-Up Policies for Real-World Humanoid Robots
  url: https://arxiv.org/abs/2502.12152
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
related_entities:
- id: ent_robot_system_unitree_g1
  relationship: evaluates_on
  description:
    en: Real-world experiments are conducted on a Unitree G1 humanoid robot.
    zh: 在 Unitree G1 人形机器人上进行真实世界实验。
    ko: Unitree G1 휴머노이드 로봇에서 실제 세계 실험을 수행함.
- id: ent_oem_unitree_robotics
  relationship: uses
  description:
    en: Uses the Unitree G1 robot platform developed by Unitree Robotics.
    zh: 使用宇树科技开发的 Unitree G1 机器人平台。
    ko: Unitree Robotics가 개발한 Unitree G1 로봇 플랫폼을 사용함.
---
## 概述
Automatic fall recovery is a crucial prerequisite before humanoid robots can be reliably deployed. Hand-designing controllers for getting up is difficult because of the varied configurations a humanoid can end up in after a fall and the challenging terrains humanoid robots are expected to operate on. This paper develops a learning framework to produce controllers that enable humanoid robots to get up from varying configurations on varying terrains. Unlike previous successful applications of learning to humanoid locomotion, the getting-up task involves complex contact patterns (which necessitates accurately modeling of the collision geometry) and sparser rewards. We address these challenges through a two-phase approach that induces a curriculum. The first stage focuses on discovering a good getting-up trajectory under minimal constraints on smoothness or speed / torque limits. The second stage then refines the discovered motions into deployable (i.e. smooth and slow) motions that are robust to variations in initial configuration and terrains. We find these innovations enable a real-world G1 humanoid robot to get up from two main situations that we considered: a) lying face up and b) lying face down, both tested on flat, deformable, slippery surfaces and slopes (e.g., sloppy grass and snowfield). This is one of the first successful demonstrations of learned getting-up policies for human-sized humanoid robots in the real world.

## 核心内容
Automatic fall recovery is a crucial prerequisite before humanoid robots can be reliably deployed. Hand-designing controllers for getting up is difficult because of the varied configurations a humanoid can end up in after a fall and the challenging terrains humanoid robots are expected to operate on. This paper develops a learning framework to produce controllers that enable humanoid robots to get up from varying configurations on varying terrains. Unlike previous successful applications of learning to humanoid locomotion, the getting-up task involves complex contact patterns (which necessitates accurately modeling of the collision geometry) and sparser rewards. We address these challenges through a two-phase approach that induces a curriculum. The first stage focuses on discovering a good getting-up trajectory under minimal constraints on smoothness or speed / torque limits. The second stage then refines the discovered motions into deployable (i.e. smooth and slow) motions that are robust to variations in initial configuration and terrains. We find these innovations enable a real-world G1 humanoid robot to get up from two main situations that we considered: a) lying face up and b) lying face down, both tested on flat, deformable, slippery surfaces and slopes (e.g., sloppy grass and snowfield). This is one of the first successful demonstrations of learned getting-up policies for human-sized humanoid robots in the real world.

## 参考
- http://arxiv.org/abs/2502.12152v2

## Overview
Automatic fall recovery is a crucial prerequisite before humanoid robots can be reliably deployed. Hand-designing controllers for getting up is difficult because of the varied configurations a humanoid can end up in after a fall and the challenging terrains humanoid robots are expected to operate on. This paper develops a learning framework to produce controllers that enable humanoid robots to get up from varying configurations on varying terrains. Unlike previous successful applications of learning to humanoid locomotion, the getting-up task involves complex contact patterns (which necessitates accurately modeling of the collision geometry) and sparser rewards. We address these challenges through a two-phase approach that induces a curriculum. The first stage focuses on discovering a good getting-up trajectory under minimal constraints on smoothness or speed / torque limits. The second stage then refines the discovered motions into deployable (i.e. smooth and slow) motions that are robust to variations in initial configuration and terrains. We find these innovations enable a real-world G1 humanoid robot to get up from two main situations that we considered: a) lying face up and b) lying face down, both tested on flat, deformable, slippery surfaces and slopes (e.g., sloppy grass and snowfield). This is one of the first successful demonstrations of learned getting-up policies for human-sized humanoid robots in the real world.

## Content
Automatic fall recovery is a crucial prerequisite before humanoid robots can be reliably deployed. Hand-designing controllers for getting up is difficult because of the varied configurations a humanoid can end up in after a fall and the challenging terrains humanoid robots are expected to operate on. This paper develops a learning framework to produce controllers that enable humanoid robots to get up from varying configurations on varying terrains. Unlike previous successful applications of learning to humanoid locomotion, the getting-up task involves complex contact patterns (which necessitates accurately modeling of the collision geometry) and sparser rewards. We address these challenges through a two-phase approach that induces a curriculum. The first stage focuses on discovering a good getting-up trajectory under minimal constraints on smoothness or speed / torque limits. The second stage then refines the discovered motions into deployable (i.e. smooth and slow) motions that are robust to variations in initial configuration and terrains. We find these innovations enable a real-world G1 humanoid robot to get up from two main situations that we considered: a) lying face up and b) lying face down, both tested on flat, deformable, slippery surfaces and slopes (e.g., sloppy grass and snowfield). This is one of the first successful demonstrations of learned getting-up policies for human-sized humanoid robots in the real world.

## 개요
휴머노이드 로봇이 안정적으로 배치되기 전에 자동 낙상 회복은 필수적인 선행 조건입니다. 낙상 후 휴머노이드가 취할 수 있는 다양한 자세와 휴머노이드 로봇이 작동해야 하는 까다로운 지형 때문에, 일어서기를 위한 제어기를 수동으로 설계하는 것은 어렵습니다. 본 논문은 다양한 지형에서 다양한 자세로부터 휴머노이드 로봇이 일어설 수 있도록 하는 제어기를 생성하는 학습 프레임워크를 개발합니다. 휴머노이드 보행에 대한 이전의 성공적인 학습 적용 사례와 달리, 일어서기 작업은 복잡한 접촉 패턴(충돌 형상의 정확한 모델링이 필요함)과 더 희박한 보상을 수반합니다. 우리는 커리큘럼을 유도하는 2단계 접근 방식을 통해 이러한 문제를 해결합니다. 첫 번째 단계는 매끄러움 또는 속도/토크 제한에 대한 최소한의 제약 하에 좋은 일어서기 궤적을 발견하는 데 초점을 맞춥니다. 두 번째 단계는 발견된 동작을 초기 자세와 지형의 변화에 강건한 배치 가능한(즉, 매끄럽고 느린) 동작으로 정제합니다. 이러한 혁신을 통해 실제 G1 휴머노이드 로봇이 고려한 두 가지 주요 상황, 즉 a) 얼굴을 위로 하고 누운 경우와 b) 얼굴을 아래로 하고 누운 경우에서 일어설 수 있음을 확인했습니다. 두 경우 모두 평평한 표면, 변형 가능한 표면, 미끄러운 표면 및 경사면(예: 미끄러운 잔디와 설원)에서 테스트되었습니다. 이는 실제 세계에서 인간 크기의 휴머노이드 로봇을 위한 학습된 일어서기 정책의 최초의 성공적인 시연 중 하나입니다.

## 핵심 내용
휴머노이드 로봇이 안정적으로 배치되기 전에 자동 낙상 회복은 필수적인 선행 조건입니다. 낙상 후 휴머노이드가 취할 수 있는 다양한 자세와 휴머노이드 로봇이 작동해야 하는 까다로운 지형 때문에, 일어서기를 위한 제어기를 수동으로 설계하는 것은 어렵습니다. 본 논문은 다양한 지형에서 다양한 자세로부터 휴머노이드 로봇이 일어설 수 있도록 하는 제어기를 생성하는 학습 프레임워크를 개발합니다. 휴머노이드 보행에 대한 이전의 성공적인 학습 적용 사례와 달리, 일어서기 작업은 복잡한 접촉 패턴(충돌 형상의 정확한 모델링이 필요함)과 더 희박한 보상을 수반합니다. 우리는 커리큘럼을 유도하는 2단계 접근 방식을 통해 이러한 문제를 해결합니다. 첫 번째 단계는 매끄러움 또는 속도/토크 제한에 대한 최소한의 제약 하에 좋은 일어서기 궤적을 발견하는 데 초점을 맞춥니다. 두 번째 단계는 발견된 동작을 초기 자세와 지형의 변화에 강건한 배치 가능한(즉, 매끄럽고 느린) 동작으로 정제합니다. 이러한 혁신을 통해 실제 G1 휴머노이드 로봇이 고려한 두 가지 주요 상황, 즉 a) 얼굴을 위로 하고 누운 경우와 b) 얼굴을 아래로 하고 누운 경우에서 일어설 수 있음을 확인했습니다. 두 경우 모두 평평한 표면, 변형 가능한 표면, 미끄러운 표면 및 경사면(예: 미끄러운 잔디와 설원)에서 테스트되었습니다. 이는 실제 세계에서 인간 크기의 휴머노이드 로봇을 위한 학습된 일어서기 정책의 최초의 성공적인 시연 중 하나입니다.
