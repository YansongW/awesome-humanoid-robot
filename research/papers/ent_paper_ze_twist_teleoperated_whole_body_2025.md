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
  en: TWIST retargets human motion capture data to humanoid robots and trains a single
    whole-body controller through a two-stage teacher-student RL+BC framework, enabling
    real-time, coordinated whole-body teleoperation across manipulation, locomotion,
    and expressive tasks.
  zh: TWIST 将人体动作捕捉数据重定向到人形机器人，并通过两阶段教师-学生 RL+BC 框架训练单一全身控制器，实现跨操作、移动和表现性任务的实时协调全身遥操作。
  ko: TWIST는 human motion capture 데이터를 휴머노이드 로봇에 리타겟팅하고 2단계 교사-학생 RL+BC 프레임워크로 단일
    전신 컨트롤러를 학습하여 조작, 보행, 표현적 동작에 걸친 실시간 조화로운 전신 원격조작을 가능하게 한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the arXiv full text; requires human review before promotion
    to verified.
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

## Overview

TWIST formulates whole-body humanoid teleoperation as a real-time motion retargeting and tracking problem. It first converts human motion capture data into humanoid-compatible reference motions through offline and online retargeters, then trains a single neural-network whole-body controller to track those references while maintaining balance. The controller is trained in large-scale simulation using a two-stage teacher-student approach that combines reinforcement learning with behavior cloning, and is deployed zero-shot on real hardware.

## Key Contributions

- Two-stage teacher-student RL+BC training: a privileged teacher observes future motion frames for smooth planning, and a single-frame student is distilled via RL plus KL-regularized behavior cloning.
- Mixing a small in-house online MoCap dataset (150 clips, ~0.5 hours) with large offline datasets (AMASS and OMOMO, ~15,000 clips) to close the offline-to-online retargeting gap.
- Joint optimization of 3D joint positions and orientations in the online retargeter for smoother real-time reference motions.
- Training with large end-effector perturbations to improve stability and force exertion in contact-rich tasks.
- Real-world deployment on Unitree G1 and sim-to-sim transfer to Booster T1 using a single unified neural network controller.

## Relevance to Humanoid Robotics

TWIST is directly relevant to humanoid robotics because it advances real-time, coordinated whole-body control of physical humanoid robots through learning-based teleoperation. By unifying locomotion, manipulation, and expressive motions under one controller, it provides a practical pipeline for acquiring diverse whole-body skills on humanoid hardware.
