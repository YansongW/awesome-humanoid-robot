---
$id: ent_paper_murooka_whole_body_multi_contact_motio_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Whole-body Multi-contact Motion Control for Humanoid Robots Based on Distributed
    Tactile Sensors
  zh: 基于分布式触觉传感器的人形机器人全身多接触运动控制
  ko: 분산 촉각 센서 기반 휴머노이드 로봇의 전신 다중 접촉 동작 제어
summary:
  en: This paper presents a whole-body multi-contact control method that uses distributed
    tactile-sensor feedback to stabilize contacts on intermediate limb areas such
    as knees, elbows, forearms, and thighs, validated in simulation and on the RHP
    Kaleido humanoid.
  zh: 本文提出了一种全身多接触控制方法，利用分布式触觉传感器反馈稳定膝盖、肘部、前臂和大腿等中间肢体区域的接触，并在仿真和RHP Kaleido人形机器人上进行了验证。
  ko: 본 논문은 분산 촉각 센서 피드백을 사용하여 무릎, 팔꿈치, 전완부, 대퇴부와 같은 중간 사지 영역의 접촉을 안정화하는 전신 다중 접촉
    제어 방법을 제시하고, 시뮬레이션과 RHP Kaleido 휴머노이드에서 검증하였다.
domains:
- 07_ai_models_algorithms
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
- multi_contact_control
- whole_body_control
- tactile_sensing
- distributed_tactile_sensors
- humanoid_motion_control
- centroidal_mpc
- model_predictive_control
- contact_polygon_estimation
- rhp_kaleido
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text review needed
    to confirm section-level citations and exact sensor specifications.
sources:
- id: src_001
  type: paper
  title: Whole-body Multi-contact Motion Control for Humanoid Robots Based on Distributed
    Tactile Sensors
  url: https://arxiv.org/abs/2505.19580
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This work addresses robust whole-body multi-contact motion for humanoid robots operating in confined environments, where contacts must be made not only at the hands and feet but also at intermediate limb regions such as the knees, elbows, forearms, and thighs. The authors mount thin, deformable sheet-shaped distributed tactile sensors on the robot's limb surfaces so that contact force can be measured without substantially altering body shape. They extend an earlier multi-contact motion controller, originally designed for extremity contacts, to handle contact at arbitrary intermediate areas. The resulting system stabilizes motion through feedback control that combines force/torque sensors, an inertial measurement unit, and the distributed tactile sensors.

The control pipeline integrates several complementary techniques. Contact wrench and region estimates from the tactile array are used in a centroidal model predictive controller, while the contact polygon vertices are updated online from sensor measurements to avoid over- or underestimating the support region. A damping controller further suppresses oscillations. The authors validate the approach first in MuJoCo dynamics simulations using the JVRC1 virtual humanoid, then on the physical life-sized humanoid RHP Kaleido.

Real-world demonstrations include stepping forward while supporting the body with forearm contact and balancing in a sitting posture using thigh contacts. These experiments show that tactile feedback improves stability against disturbances and environmental errors compared with relying solely on force/torque sensing.

## Key Contributions

- A control method for robust whole-body multi-contact motion that uses distributed tactile sensors mounted directly on robot link surfaces.
- Extension of an existing multi-contact controller to support contact at intermediate limb areas such as knees, elbows, forearms, and thighs.
- Online update of contact polygon vertices from distributed tactile sensor measurements to prevent over/underestimation of contact regions.
- Simulation validation in MuJoCo demonstrating improved stability under disturbances and environmental errors.
- Real-world demonstrations on the life-sized humanoid RHP Kaleido with forearm-support stepping and sitting balance using thigh contacts.

## Relevance to Humanoid Robotics

The paper is directly relevant to humanoid robotics because it enables stable, dynamic whole-body contact with arbitrary limb surfaces. This capability is critical for maneuvering and balancing in cluttered or confined industrial and service environments, where robots may need to brace against walls, squeeze through gaps, or sit and stand in tight spaces. By closing the loop with distributed tactile sensing, the method moves beyond traditional end-effector contact control and makes fuller use of the robot's body for support and interaction.
