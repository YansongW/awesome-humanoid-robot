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
  en: Proposes a patient-specified stiffness-based method to correct force-induced tissue deformation in robotic 3D ultrasound
    by robotic palpation, optical flow, and coupled quadratic regression, validated on two vascular phantoms.
  zh: 提出一种基于患者指定刚度的机器人三维超声组织形变校正方法，通过机器人触诊、光流算法与耦合二次回归估计像素位移，并在两种血管模型上验证可恢复零压缩三维几何。
  ko: 로봇 촉진, 광류 알고리즘 및 결합 2차 회귀를 통해 픽셀 변위를 추정하고 두 가지 혈관 팬텀에서 검증된 환자 지정 강성 기반 변형 보정 방법을 제안한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2107.08411v1.
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
## 概述
Tissue deformation in ultrasound (US) imaging leads to geometrical errors when measuring tissues due to the pressure exerted by probes. Such deformation has an even larger effect on 3D US volumes as the correct compounding is limited by the inconsistent location and geometry. This work proposes a patient-specified stiffness-based method to correct the tissue deformations in robotic 3D US acquisitions. To obtain the patient-specified model, robotic palpation is performed at sampling positions on the tissue. The contact force, US images and the probe poses of the palpation procedure are recorded. The contact force and the probe poses are used to estimate the nonlinear tissue stiffness. The images are fed to an optical flow algorithm to compute the pixel displacement. Then the pixel-wise tissue deformation under different forces is characterized by a coupled quadratic regression. To correct the deformation at unseen positions on the trajectory for building 3D volumes, an interpolation is performed based on the stiffness values computed at the sampling positions. With the stiffness and recorded force, the tissue displacement could be corrected. The method was validated on two blood vessel phantoms with different stiffness. The results demonstrate that the method can effectively correct the force-induced deformation and finally generate 3D tissue geometries

## 核心内容
Tissue deformation in ultrasound (US) imaging leads to geometrical errors when measuring tissues due to the pressure exerted by probes. Such deformation has an even larger effect on 3D US volumes as the correct compounding is limited by the inconsistent location and geometry. This work proposes a patient-specified stiffness-based method to correct the tissue deformations in robotic 3D US acquisitions. To obtain the patient-specified model, robotic palpation is performed at sampling positions on the tissue. The contact force, US images and the probe poses of the palpation procedure are recorded. The contact force and the probe poses are used to estimate the nonlinear tissue stiffness. The images are fed to an optical flow algorithm to compute the pixel displacement. Then the pixel-wise tissue deformation under different forces is characterized by a coupled quadratic regression. To correct the deformation at unseen positions on the trajectory for building 3D volumes, an interpolation is performed based on the stiffness values computed at the sampling positions. With the stiffness and recorded force, the tissue displacement could be corrected. The method was validated on two blood vessel phantoms with different stiffness. The results demonstrate that the method can effectively correct the force-induced deformation and finally generate 3D tissue geometries

## 参考
- http://arxiv.org/abs/2107.08411v1

