---
$id: ent_paper_landi_admittance_control_parameter_a_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Admittance Control Parameter Adaptation for Physical Human-Robot Interaction
  zh: 物理人机交互中的导纳控制参数自适应
  ko: 물리적 인간-로봇 상호작용을 위한 어드미턴스 제어 매개변수 적응
summary:
  en: Presents an online strategy for detecting deviations from nominal behavior in
    admittance-controlled robots and adapting controller parameters while guaranteeing
    passivity, validated experimentally on a KUKA LWR 4+.
  zh: 提出了一种在线检测导纳控制机器人偏离标称行为的策略，并在保证无源性的同时自适应调整控制器参数，在KUKA LWR 4+上进行了实验验证。
  ko: 어드미턴스 제어 로봇의 명목 동작에서 편차를 온라인으로 검출하고 수동성을 보장하면서 제어기 매개변수를 적응시키는 전략을 제안하며, KUKA
    LWR 4+에서 실험적으로 검증되었다.
domains:
- 02_components
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- admittance_control
- parameter_adaptation
- physical_human_robot_interaction
- passivity
- energy_tank
- kuka_lwr_4plus
- force_control
- online_adaptation
- stability
- pHRI
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text review is needed
    to confirm section-level citations, threshold values, and experimental details.
sources:
- id: src_001
  type: paper
  title: Admittance Control Parameter Adaptation for Physical Human-Robot Interaction
  url: https://arxiv.org/abs/1702.08376
  date: '2017'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper addresses the challenge of maintaining stable and low-effort physical human-robot interaction when an admittance-controlled robot deviates from its expected behavior. The authors observe that rigidifying of the human arm or other unmodeled changes can compromise stability, and that fixed admittance parameters are often too conservative. They therefore propose an online monitoring and adaptation framework that detects behavioral deviations and updates controller parameters while enforcing passivity.

The deviation detector is implemented as a heuristic based on the residual force tracking error, which signals when the actual interaction deviates from the nominal model. Once a deviation is detected, the admittance control parameters—principally inertia and damping—are adapted to restore desirable interaction properties. Passivity is guaranteed throughout adaptation by leveraging an energy-tank formulation, which permits less conservative parameter variations than classical passivity constraints.

Experimental validation is performed on a KUKA LWR 4+ manipulator equipped with an ATI Mini 45 6-axis force/torque sensor. The results illustrate that the proposed method can adapt the controller online to changing interaction conditions while maintaining stability.

## Key Contributions

- Online heuristic for detecting deviations from nominal admittance-controlled behavior based on residual force tracking error.
- Passivity-based parameter adaptation framework that adjusts admittance control inertia and damping online.
- Use of energy tanks to enable less conservative inertia variations than classical passivity conditions allow.
- Experimental validation on a KUKA LWR 4+ with an ATI Mini 45 6-axis force/torque sensor.

## Relevance to Humanoid Robotics

Adaptive admittance control is directly relevant to humanoid robots that must physically collaborate with humans in manufacturing, logistics, or service environments. Humanoids are expected to operate safely alongside people while responding to unpredictable contact forces; passivity-preserving online parameter adaptation provides a principled way to maintain stability without requiring overly conservative fixed gains.

Although the experiments use a single industrial manipulator rather than a full humanoid, the control formalism is limb-agnostic and can be applied to arms or whole-body admittance controllers on humanoid platforms. The energy-tank-based passivity framework is especially valuable for humanoids, where multiple contact points and time-varying environmental stiffness make preset parameters difficult to tune.
