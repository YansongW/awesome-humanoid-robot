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
  zh: TWIST 是一个面向人形机器人的全身遥操作模仿系统，由研究团队提出。其核心贡献在于通过两阶段教师-学生强化学习与行为克隆（RL+BC）框架，将人体运动捕捉数据重定向至人形机器人，并训练出单一全身控制器，实现实时、协调的全身遥操作，涵盖操作、移动与表达性任务。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.02833v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
TWIST 系统旨在解决当前人形机器人遥操作中缺乏协调全身行为的问题，现有系统通常局限于孤立的移动或操作任务。该系统首先将人体运动捕捉数据重定向至人形机器人以生成参考运动片段，随后结合强化学习与行为克隆（RL+BC）开发出鲁棒、自适应且响应迅速的全身控制器。通过系统分析，研究团队证明了引入特权未来运动帧和真实世界运动捕捉（MoCap）数据可提升跟踪精度。TWIST 使用单一统一神经网络控制器，使人形机器人在真实世界中实现前所未有的多功能协调全身运动技能，包括全身操作、有腿操作、移动和表达性动作。

## 核心内容
### 方法
- **数据重定向**：将人体运动捕捉（MoCap）数据重定向至人形机器人，生成参考运动片段。
- **两阶段训练框架**：采用教师-学生结构，结合强化学习（RL）与行为克隆（BC）。
  - 教师阶段：利用特权信息（如未来运动帧）训练策略。
  - 学生阶段：通过行为克隆模仿教师策略，仅依赖可观测输入。
- **控制器设计**：开发单一统一神经网络控制器，支持全身协调行为。

### 实验设置
- **硬件平台**：真实世界人形机器人。
- **数据来源**：真实世界运动捕捉（MoCap）数据。
- **关键对比**：系统分析特权未来运动帧和 MoCap 数据对跟踪精度的影响。

### 关键数字与结论
- **性能提升**：引入特权未来运动帧和 MoCap 数据显著提高了跟踪精度。
- **技能范围**：TWIST 使机器人能够执行全身操作、有腿操作、移动和表达性动作，使用单一控制器。
- **实时性**：系统支持实时遥操作，实现协调全身行为。
- **项目网站**：https://humanoid-teleop.github.io

## Overview
Teleoperating humanoid robots in a whole-body manner marks a fundamental step toward developing general-purpose robotic intelligence, with human motion providing an ideal interface for controlling all degrees of freedom. Yet, most current humanoid teleoperation systems fall short of enabling coordinated whole-body behavior, typically limiting themselves to isolated locomotion or manipulation tasks. We present the Teleoperated Whole-Body Imitation System (TWIST), a system for humanoid teleoperation through whole-body motion imitation. We first generate reference motion clips by retargeting human motion capture data to the humanoid robot. We then develop a robust, adaptive, and responsive whole-body controller using a combination of reinforcement learning and behavior cloning (RL+BC). Through systematic analysis, we demonstrate how incorporating privileged future motion frames and real-world motion capture (MoCap) data improves tracking accuracy. TWIST enables real-world humanoid robots to achieve unprecedented, versatile, and coordinated whole-body motor skills--spanning whole-body manipulation, legged manipulation, locomotion, and expressive movement--using a single unified neural network controller. Our project website: https://humanoid-teleop.github.io

## 개요
휴머노이드 로봇을 전신 방식으로 원격 조종하는 것은 범용 로봇 지능 개발을 위한 근본적인 단계이며, 인간의 움직임은 모든 자유도를 제어하기 위한 이상적인 인터페이스를 제공합니다. 그러나 현재 대부분의 휴머노이드 원격 조종 시스템은 조화로운 전신 동작을 구현하는 데 한계가 있으며, 일반적으로 개별적인 보행 또는 조작 작업에 국한됩니다. 본 논문에서는 전신 동작 모방을 통한 휴머노이드 원격 조종 시스템인 TWIST(Teleoperated Whole-Body Imitation System)를 제안합니다. 먼저 인간의 모션 캡처 데이터를 휴머노이드 로봇에 리타겟팅하여 참조 동작 클립을 생성합니다. 그런 다음 강화 학습과 행동 복제(RL+BC)를 결합하여 강건하고 적응적이며 반응성이 뛰어난 전신 제어기를 개발합니다. 체계적인 분석을 통해 특권 미래 동작 프레임과 실제 모션 캡처(MoCap) 데이터를 통합함으로써 추적 정확도가 향상됨을 입증합니다. TWIST는 단일 통합 신경망 제어기를 사용하여 실제 휴머노이드 로봇이 전신 조작, 보행 조작, 보행, 표현적 움직임에 이르기까지 전례 없이 다양하고 조화로운 전신 운동 기술을 달성할 수 있게 합니다. 프로젝트 웹사이트: https://humanoid-teleop.github.io

## 핵심 내용
휴머노이드 로봇을 전신 방식으로 원격 조종하는 것은 범용 로봇 지능 개발을 위한 근본적인 단계이며, 인간의 움직임은 모든 자유도를 제어하기 위한 이상적인 인터페이스를 제공합니다. 그러나 현재 대부분의 휴머노이드 원격 조종 시스템은 조화로운 전신 동작을 구현하는 데 한계가 있으며, 일반적으로 개별적인 보행 또는 조작 작업에 국한됩니다. 본 논문에서는 전신 동작 모방을 통한 휴머노이드 원격 조종 시스템인 TWIST(Teleoperated Whole-Body Imitation System)를 제안합니다. 먼저 인간의 모션 캡처 데이터를 휴머노이드 로봇에 리타겟팅하여 참조 동작 클립을 생성합니다. 그런 다음 강화 학습과 행동 복제(RL+BC)를 결합하여 강건하고 적응적이며 반응성이 뛰어난 전신 제어기를 개발합니다. 체계적인 분석을 통해 특권 미래 동작 프레임과 실제 모션 캡처(MoCap) 데이터를 통합함으로써 추적 정확도가 향상됨을 입증합니다. TWIST는 단일 통합 신경망 제어기를 사용하여 실제 휴머노이드 로봇이 전신 조작, 보행 조작, 보행, 표현적 움직임에 이르기까지 전례 없이 다양하고 조화로운 전신 운동 기술을 달성할 수 있게 합니다. 프로젝트 웹사이트: https://humanoid-teleop.github.io

## 参考
- http://arxiv.org/abs/2505.02833v1
