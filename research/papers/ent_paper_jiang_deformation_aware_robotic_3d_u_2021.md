---
$id: ent_paper_jiang_deformation_aware_robotic_3d_u_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Deformation-Aware Robotic 3D Ultrasound
  zh: 变形感知机器人三维超声
  ko: 변형 인식 로봇 3D 초음파
summary:
  en: Proposes a patient-specified stiffness-based method to correct force-induced
    tissue deformation in robotic 3D ultrasound by robotic palpation, optical flow,
    and coupled quadratic regression, validated on two vascular phantoms.
  zh: 提出一种基于患者指定刚度的机器人三维超声组织形变校正方法，通过机器人触诊、光流算法与耦合二次回归估计像素位移，并在两种血管模型上验证可恢复零压缩三维几何。
  ko: 로봇 촉진, 광류 알고리즘 및 결합 2차 회귀를 통해 픽셀 변위를 추정하고 두 가지 혈관 팬텀에서 검증된 환자 지정 강성 기반 변형 보정
    방법을 제안한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- robotic_ultrasound
- tissue_deformation_correction
- patient_specified_stiffness
- force_controlled_palpation
- optical_flow
- 3d_ultrasound_compounding
- compliant_robotic_manipulation
- vascular_phantom
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv preprint/full text; requires human review before
    verification.
sources:
- id: src_001
  type: paper
  title: Deformation-Aware Robotic 3D Ultrasound
  url: https://arxiv.org/abs/2107.08411
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper presents a stiffness-based deformation-correction framework for robotic 3D ultrasound acquisition. The method first performs robotic palpation at a set of tissue-sampling positions, recording synchronized contact force, probe pose, and 2D B-mode ultrasound images. Contact force and probe displacement are used to estimate local nonlinear tissue stiffness, while optical flow extracts pixel displacement between images acquired under different forces. A coupled quadratic regression then relates pixel displacement to pixel position, contact force, and dynamic tissue stiffness. Finally, stiffness values at sparse sampling points are interpolated so the optimized regression can be propagated to unseen positions along a scanning trajectory, yielding a corrected, zero-compression 3D volume. The approach is validated on two blood-vessel phantoms of markedly different stiffness.

## Key Contributions

- Patient-specific nonlinear tissue stiffness estimation using robotic palpation with recorded force, pose, and ultrasound images.
- A coupled quadratic regression model that relates pixel displacement to pixel position, contact force, and dynamic tissue stiffness.
- Fast propagation of the optimized deformation regression to unseen positions and to other tissues by substituting local stiffness values.
- Experimental validation on stiff and soft vascular phantoms demonstrating recovery of zero-compression 3D geometries.

## Relevance to Humanoid Robotics

Although the paper targets medical ultrasound, its core robotic capabilities are directly transferable to humanoid systems. The work demonstrates compliant, force-controlled surface interaction, automated data acquisition, sensor fusion from force/torque and vision streams, and model adaptation across spatially varying material properties. These are the same skills required for humanoid robots performing delicate inspection, assembly, or clinical assistance tasks.
