---
$id: ent_paper_wang_a_soft_continuum_robot_with_se_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Soft Continuum Robot with Self-Controllable Variable Curvature
  zh: 具有自可控变曲率的软连续体机器人
  ko: 자기 제어 가능한 가변 곡률을 가진 소프트 연속체 로봇
summary:
  en: This paper presents SCoReS, a pneumatic soft continuum robot that embeds a motor-controlled,
    granular-jamming growing spine to achieve continuous, segment-level curvature
    and stiffness variation without external forces or discrete locking mechanisms.
  zh: 本文提出SCoReS，一种嵌入电机控制的颗粒阻塞生长脊柱的气动软连续体机器人，可在无需外力或离散锁定机构的情况下实现分段层面连续的曲率与刚度变化。
  ko: 본 논문은 외력이나 이산식 잠금 장치 없이 세그먼트 단위에서 연속적인 곡률과 강성 변화를 실현하는 모터 제어 입자 잠금 성장 척추를 내장한
    공압식 소프트 연속체 로봇 SCoReS를 제안한다.
domains:
- 02_components
- 06_design_engineering
layers:
- upstream
- midstream
functional_roles:
- knowledge
- system
tags:
- soft_continuum_robot
- variable_curvature
- continuous_stiffness_regulation
- granular_jamming
- growing_spine
- stiffness_control
- compliant_actuation
- fruit_grasping
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from arXiv preprint full text; requires human review before
    full verification.
sources:
- id: src_001
  type: paper
  title: A Soft Continuum Robot with Self-Controllable Variable Curvature
  url: https://arxiv.org/abs/2401.01739
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

SCoReS (Soft Continuum Robot with Self-controllable variable curvature) is a pneumatic soft continuum robot that embeds a motor-driven, variable-stiffness growing spine inside its body. The spine is filled with glass-bubble granules and uses micro-particle granular jamming to switch between flexible and rigid states, while a stepper-motor-based length-control unit adjusts how much of the spine is inserted into the robot. By combining pneumatic chamber pressurization with a selectively jammed region, the robot can produce a range of bending profiles using the same control inputs.

The authors detail the mechanical design and fabrication process, including the use of DragonSkin 10 silicone, embedded Kevlar constraint strings, and a TPU-coated ripstop fabric airtight chamber. Stiffness is modeled with Euler-Bernoulli beam theory as a cantilever beam, and the overall bending behavior is simulated with finite-element analysis (FEA) in Abaqus using a Neo-Hookean material model. Experiments compare bending angles and end-effector positions across spine lengths from 0 cm to 30 cm and pressures from 50 kPa to 250 kPa.

A real-world demonstration mounts a gripper on the robot and shows how different spine lengths create distinct bending profiles and end-effector paths, suggesting utility in confined or cluttered environments.

## Key Contributions

- Novel SCoReS design that achieves continuous, segment-level variable curvature and stiffness without external forces or discrete locking mechanisms.
- Development of a growing spine with automatic length control and micro-particle granular jamming using glass-bubble granules.
- Beam-theory-based stiffness modeling of the jammed growing spine as a cantilever beam, validated through experiments.
- FEA simulation of the integrated soft continuum robot using a Neo-Hookean DragonSkin 10 model in Abaqus, compared against experimental bending profiles.
- Experimental characterization of bending angles, end-effector positions, and length-control accuracy across multiple configurations.
- Real-world demonstration with a gripper showing configurable bending profiles in constrained spaces.

## Relevance to Humanoid Robotics

Although SCoReS is a continuum manipulator rather than a biped, the technologies it develops are directly relevant to humanoid robotics. Compliant, continuously variable-stiffness actuation and jamming-based reconfigurable bodies can improve humanoid arms, spines, and end effectors that must operate safely and adaptively in unstructured or confined industrial settings. The ability to modulate curvature and stiffness with a single, self-contained mechanism also informs the design of compact, lightweight, and intrinsically safe humanoid components.
