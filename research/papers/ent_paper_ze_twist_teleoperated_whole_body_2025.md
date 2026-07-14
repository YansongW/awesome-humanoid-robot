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

