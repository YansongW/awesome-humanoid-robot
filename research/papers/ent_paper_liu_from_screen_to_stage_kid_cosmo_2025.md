---
$id: ent_paper_liu_from_screen_to_stage_kid_cosmo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From Screen to Stage: Kid Cosmo, A Life-Like, Torque-Controlled Humanoid for
    Entertainment Robotics'
  zh: 从银幕到舞台：Kid Cosmo——一款用于娱乐机器人的力控逼真类人机器人
  ko: '스크린에서 무대로: Kid Cosmo, 엔터테인먼트 로봇을 위한 생동감 있는 토크 제어 휴머노이드'
summary:
  en: This paper presents Kid Cosmo, a 1.45 m, 25 kg, 28-DoF torque-controlled child-sized
    humanoid developed for entertainment performances, combining proprioceptive actuation,
    compliant character shells, and a model-based locomotion stack with whole-body
    control.
  zh: 本文介绍了 Kid Cosmo，一款身高 1.45 米、重 25 千克、具有 28 自由度的力控儿童尺寸人形机器人，面向娱乐表演，结合了本体感知驱动、柔顺的角色外壳以及基于模型的全身控制运动栈。
  ko: 본 논문은 엔터테인먼트 공연을 위해 개발된 1.45m, 25kg, 28자유도 토크 제어 아동 크기 휴머노이드인 Kid Cosmo를 제시하며,
    본체감각 액추에이터, 순응형 캐릭터 셸, 및 전신 제어 기반 모델 기반 보행 스택을 결합한다.
domains:
- 06_design_engineering
- 11_applications_markets
- 02_components
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
tags:
- kid_cosmo
- entertainment_robotics
- torque_control
- whole_body_control
- humanoid_locomotion
- character_embodiment
- proprioceptive_actuators
- compliant_shells
- lip_footstep_planning
- inverse_kinematics
- quadratic_programming
- finite_state_machine
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the provided paper metadata and abstract; requires human
    review against the full arXiv text before full verification.
sources:
- id: src_001
  type: paper
  title: 'From Screen to Stage: Kid Cosmo, A Life-Like, Torque-Controlled Humanoid
    for Entertainment Robotics'
  url: https://arxiv.org/abs/2508.11884
  date: '2025'
  accessed_at: '2026-06-28'
theoretical_depth:
- system
---

## Overview

Kid Cosmo is a child-sized humanoid robot developed as a research and performance platform for entertainment robotics. Standing 1.45 m tall, weighing 25 kg, and equipped with 28 degrees of freedom, the robot is designed to emulate the appearance and mannerisms of its namesake character from Netflix's The Electric State while performing dynamic, torque-controlled locomotion. Its drivetrain relies primarily on proprioceptive actuators, including Panda Bear Plus and Koala Bear Muscle Build units, and it incorporates character-faithful compliant shells to absorb impacts during motion.

The system architecture combines a model-based locomotion stack with whole-body motion generation. The lower-body controller uses Linear Inverted Pendulum (LIP) footstep planning, an implicit hierarchical whole-body controller formulated as a quadratic program (QP), and damped-least-squares inverse kinematics to coordinate upper- and lower-body motion. A finite-state-machine-based upper-body motion manager triggers pre-recorded gestures during operation. The paper also discusses packaging trade-offs, such as a 3:1 planetary gearbox added to the knee joint to address thermal limits and the omission of ankle roll to reduce distal mass.

Following public showcases during the film's press tour, the authors report initial findings on stability during simultaneous upper- and lower-body movement and on disturbance rejection while standing and walking. The work is positioned as a demonstration that performance-oriented humanoids can integrate character embodiment with functional dynamic locomotion.

## Key Contributions

- Use of compliance in aesthetic shells to mitigate impact during dynamic movements.
- Novel internal packaging and hip joint configuration to conform to character aesthetics.
- Demonstration of torque-controlled walking with simultaneous upper body gestures.
- Validation of disturbance rejection during standing and walking.
- Integration of a life-like character embodiment with real-world dynamic locomotion.

## Relevance to Humanoid Robotics

Kid Cosmo is directly relevant to humanoid robotics because it packages torque-controlled walking, whole-body control, and proprioceptive actuation into a deployable, character-faithful entertainment platform. The design choices—such as compliant shells, distal mass reduction, and thermal-management trade-offs—illustrate how functional locomotion requirements interact with aesthetic and packaging constraints in real-world humanoid systems. The paper also provides a practical example of transitioning laboratory humanoid mobility toward mass-audience public performances.
