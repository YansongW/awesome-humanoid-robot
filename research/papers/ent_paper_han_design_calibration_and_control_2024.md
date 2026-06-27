---
$id: ent_paper_han_design_calibration_and_control_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Design, Calibration, and Control of Compliant Force-sensing Gripping Pads for
    Humanoid Robots
  zh: 面向人形机器人的柔顺力传感夹持垫设计、标定与控制
  ko: 휴머노이드 로봇을 위한 순응형 힘 감지 그리핑 패드의 설계, 보정 및 제어
summary:
  en: This 2024 paper presents low-cost, lightweight compliant gripping pads that
    measure normal gripping force and center of pressure, together with a calibration
    procedure and a hybrid force-alignment-position controller using limit-surface
    theory for slippage avoidance, demonstrated on a NAO humanoid robot manipulating
    box-like objects.
  zh: 该2024年论文提出了一种低成本、轻量化的柔顺力传感夹持垫，可测量法向夹持力与压力中心，并开发了标定方法以及基于极限面理论防止打滑的混成力-对准-位置控制器，在NAO人形机器人抓取箱形物体上进行了验证。
  ko: 이 2024년 논문은 저렴하고 가벼운 순응형 힘 감지 그리핑 패드를 제안하며, 법선 방향 그리핑 힘과 압력 중심을 측정하고 비선형 보정
    절차와 극한 표면 이론을 활용한 미끄러짐 방지 하이브리드 힘-정렬-위치 제어기를 개발하여 NAO 휴머노이드 로봇의 상자형 물체 조작에서 입증하였다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- force_sensing
- gripping_pad
- end_effector
- nao
- dual_arm_manipulation
- compliant_mechanism
- load_cell
- center_of_pressure
- limit_surface
- slippage_avoidance
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from metadata and abstract; requires human review against the
    full arXiv text before verification.
sources:
- id: src_001
  type: paper
  title: Design, Calibration, and Control of Compliant Force-sensing Gripping Pads
    for Humanoid Robots
  url: https://arxiv.org/abs/2405.20969
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper introduces a pair of low-cost, lightweight, and compliant force-sensing gripping pads intended for dual-arm manipulation of rigid box-like objects by smaller-sized humanoid robots. Each pad integrates 1-D load cells, a PLA 3-D printed support structure, a frictional rubber pad, and a stacked wave disk spring to measure normal gripping force and center of pressure (CoP). A dedicated calibration method based on nonlinear optimization is developed to improve CoP measurement accuracy, reportedly reducing error to approximately 1 mm.

The authors propose a hybrid force-alignment-position control framework in which gripping force, gripper orientation, and position are regulated through decoupled control loops. Limit surface theory is adopted as a contact-friction modeling tool to determine the minimum gripping forces required to avoid slippage during task-space manipulation. The electronics consist of a SparkFun HX711 ADC, an RF-Nano MCU with an NRF24L01 wireless module, an Arduino Mega receiver, and a ROS-based processing module. The complete system is evaluated on a NAO humanoid robot in horizontal sliding, vertical manipulation, and lifting experiments.

## Key Contributions

- Design of 35 g, sub-$45 compliant force-sensing gripping pads measuring normal force and center of pressure.
- Nonlinear calibration method that reduces CoP measurement error to approximately 1 mm.
- Hybrid force-alignment-position control framework with decoupled force, orientation, and position loops.
- Limit-surface-based gripping force regulation for slippage avoidance during task-space manipulation.
- Experimental validation on a NAO humanoid robot performing horizontal, vertical, and lifting tasks.

## Relevance to Humanoid Robotics

The work is directly relevant to humanoid manipulation because it addresses a recurring hardware gap for smaller humanoid platforms: affordable, lightweight end-effector force sensing. By integrating compliant sensing pads with a model-based force controller, the paper enables more reliable dual-arm manipulation of everyday rigid objects without requiring expensive multi-axis force/torque sensors. The demonstration on the NAO robot provides a concrete reference for low-cost force-controlled grasping in humanoid systems.
