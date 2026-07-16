---
$id: ent_paper_ze_twist_teleoperated_whole_body_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TWIST: Teleoperated Whole-Body Imitation System'
  zh: TWIST：遥操作全身模仿系统
  ko: 'TWIST: 원격조작 전신 모방 시스템'
summary:
  en: TWIST retargets human motion capture data to humanoid robots and trains a single whole-body controller through a two-stage
    teacher-student RL+BC framework, enabling real-time, coordinated whole-body teleoperation across manipulation, locomotion,
    and expressive tasks.
  zh: TWIST 将人体动作捕捉数据重定向到人形机器人，并通过两阶段教师-学生 RL+BC 框架训练单一全身控制器，实现跨操作、移动和表现性任务的实时协调全身遥操作。
  ko: TWIST는 human motion capture 데이터를 휴머노이드 로봇에 리타겟팅하고 2단계 교사-학생 RL+BC 프레임워크로 단일 전신 컨트롤러를 학습하여 조작, 보행, 표현적 동작에 걸친 실시간 조화로운
    전신 원격조작을 가능하게 한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- whole_body_teleoperation
- imitation_learning
- reinforcement_learning
- behavior_cloning
- teacher_student_distillation
- motion_retargeting
- sim_to_real
- humanoid_control
- unitree_g1
- booster_t1
- mocap
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.02833v1.
sources:
- id: src_001
  type: paper
  title: 'TWIST: Teleoperated Whole-Body Imitation System'
  url: https://arxiv.org/abs/2505.02833
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Teleoperating humanoid robots in a whole-body manner marks a fundamental step toward developing general-purpose robotic intelligence, with human motion providing an ideal interface for controlling all degrees of freedom. Yet, most current humanoid teleoperation systems fall short of enabling coordinated whole-body behavior, typically limiting themselves to isolated locomotion or manipulation tasks. We present the Teleoperated Whole-Body Imitation System (TWIST), a system for humanoid teleoperation through whole-body motion imitation. We first generate reference motion clips by retargeting human motion capture data to the humanoid robot. We then develop a robust, adaptive, and responsive whole-body controller using a combination of reinforcement learning and behavior cloning (RL+BC). Through systematic analysis, we demonstrate how incorporating privileged future motion frames and real-world motion capture (MoCap) data improves tracking accuracy. TWIST enables real-world humanoid robots to achieve unprecedented, versatile, and coordinated whole-body motor skills--spanning whole-body manipulation, legged manipulation, locomotion, and expressive movement--using a single unified neural network controller. Our project website: https://humanoid-teleop.github.io

## 核心内容
Teleoperating humanoid robots in a whole-body manner marks a fundamental step toward developing general-purpose robotic intelligence, with human motion providing an ideal interface for controlling all degrees of freedom. Yet, most current humanoid teleoperation systems fall short of enabling coordinated whole-body behavior, typically limiting themselves to isolated locomotion or manipulation tasks. We present the Teleoperated Whole-Body Imitation System (TWIST), a system for humanoid teleoperation through whole-body motion imitation. We first generate reference motion clips by retargeting human motion capture data to the humanoid robot. We then develop a robust, adaptive, and responsive whole-body controller using a combination of reinforcement learning and behavior cloning (RL+BC). Through systematic analysis, we demonstrate how incorporating privileged future motion frames and real-world motion capture (MoCap) data improves tracking accuracy. TWIST enables real-world humanoid robots to achieve unprecedented, versatile, and coordinated whole-body motor skills--spanning whole-body manipulation, legged manipulation, locomotion, and expressive movement--using a single unified neural network controller. Our project website: https://humanoid-teleop.github.io

## 参考
- http://arxiv.org/abs/2505.02833v1

## Overview
Teleoperating humanoid robots in a whole-body manner marks a fundamental step toward developing general-purpose robotic intelligence, with human motion providing an ideal interface for controlling all degrees of freedom. Yet, most current humanoid teleoperation systems fall short of enabling coordinated whole-body behavior, typically limiting themselves to isolated locomotion or manipulation tasks. We present the Teleoperated Whole-Body Imitation System (TWIST), a system for humanoid teleoperation through whole-body motion imitation. We first generate reference motion clips by retargeting human motion capture data to the humanoid robot. We then develop a robust, adaptive, and responsive whole-body controller using a combination of reinforcement learning and behavior cloning (RL+BC). Through systematic analysis, we demonstrate how incorporating privileged future motion frames and real-world motion capture (MoCap) data improves tracking accuracy. TWIST enables real-world humanoid robots to achieve unprecedented, versatile, and coordinated whole-body motor skills--spanning whole-body manipulation, legged manipulation, locomotion, and expressive movement--using a single unified neural network controller. Our project website: https://humanoid-teleop.github.io

## Content
Teleoperating humanoid robots in a whole-body manner marks a fundamental step toward developing general-purpose robotic intelligence, with human motion providing an ideal interface for controlling all degrees of freedom. Yet, most current humanoid teleoperation systems fall short of enabling coordinated whole-body behavior, typically limiting themselves to isolated locomotion or manipulation tasks. We present the Teleoperated Whole-Body Imitation System (TWIST), a system for humanoid teleoperation through whole-body motion imitation. We first generate reference motion clips by retargeting human motion capture data to the humanoid robot. We then develop a robust, adaptive, and responsive whole-body controller using a combination of reinforcement learning and behavior cloning (RL+BC). Through systematic analysis, we demonstrate how incorporating privileged future motion frames and real-world motion capture (MoCap) data improves tracking accuracy. TWIST enables real-world humanoid robots to achieve unprecedented, versatile, and coordinated whole-body motor skills--spanning whole-body manipulation, legged manipulation, locomotion, and expressive movement--using a single unified neural network controller. Our project website: https://humanoid-teleop.github.io

## 개요
휴머노이드 로봇을 전신 방식으로 원격 조종하는 것은 범용 로봇 지능 개발을 위한 근본적인 단계이며, 인간의 움직임은 모든 자유도를 제어하기 위한 이상적인 인터페이스를 제공합니다. 그러나 현재 대부분의 휴머노이드 원격 조종 시스템은 조화로운 전신 동작을 구현하는 데 한계가 있으며, 일반적으로 개별적인 보행 또는 조작 작업에 국한됩니다. 본 논문에서는 전신 동작 모방을 통한 휴머노이드 원격 조종 시스템인 TWIST(Teleoperated Whole-Body Imitation System)를 제안합니다. 먼저 인간의 모션 캡처 데이터를 휴머노이드 로봇에 리타겟팅하여 참조 동작 클립을 생성합니다. 그런 다음 강화 학습과 행동 복제(RL+BC)를 결합하여 강건하고 적응적이며 반응성이 뛰어난 전신 제어기를 개발합니다. 체계적인 분석을 통해 특권 미래 동작 프레임과 실제 모션 캡처(MoCap) 데이터를 통합함으로써 추적 정확도가 향상됨을 입증합니다. TWIST는 단일 통합 신경망 제어기를 사용하여 실제 휴머노이드 로봇이 전신 조작, 보행 조작, 보행, 표현적 움직임에 이르기까지 전례 없이 다양하고 조화로운 전신 운동 기술을 달성할 수 있게 합니다. 프로젝트 웹사이트: https://humanoid-teleop.github.io

## 핵심 내용
휴머노이드 로봇을 전신 방식으로 원격 조종하는 것은 범용 로봇 지능 개발을 위한 근본적인 단계이며, 인간의 움직임은 모든 자유도를 제어하기 위한 이상적인 인터페이스를 제공합니다. 그러나 현재 대부분의 휴머노이드 원격 조종 시스템은 조화로운 전신 동작을 구현하는 데 한계가 있으며, 일반적으로 개별적인 보행 또는 조작 작업에 국한됩니다. 본 논문에서는 전신 동작 모방을 통한 휴머노이드 원격 조종 시스템인 TWIST(Teleoperated Whole-Body Imitation System)를 제안합니다. 먼저 인간의 모션 캡처 데이터를 휴머노이드 로봇에 리타겟팅하여 참조 동작 클립을 생성합니다. 그런 다음 강화 학습과 행동 복제(RL+BC)를 결합하여 강건하고 적응적이며 반응성이 뛰어난 전신 제어기를 개발합니다. 체계적인 분석을 통해 특권 미래 동작 프레임과 실제 모션 캡처(MoCap) 데이터를 통합함으로써 추적 정확도가 향상됨을 입증합니다. TWIST는 단일 통합 신경망 제어기를 사용하여 실제 휴머노이드 로봇이 전신 조작, 보행 조작, 보행, 표현적 움직임에 이르기까지 전례 없이 다양하고 조화로운 전신 운동 기술을 달성할 수 있게 합니다. 프로젝트 웹사이트: https://humanoid-teleop.github.io
