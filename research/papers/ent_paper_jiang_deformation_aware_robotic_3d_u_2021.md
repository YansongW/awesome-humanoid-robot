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
  zh: Tissue deformation in ultrasound (US) imaging leads to geometrical errors when measuring tissues due to the pressure
    exerted by probes. Such deformation has an even larger effect on 3D US volumes as the correct compounding is limited by
    the inconsistent location and geometry. This work proposes a patient-specified stiffness-based method to correct the tissue
    deformations in robotic 3D US acquisitions. To obtain the patient-specified model, robotic palpation is performed at sampling
    positions on the tissue. The contact force, US images and the probe poses of the palpation procedure are recorded
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

## Overview
Tissue deformation in ultrasound (US) imaging leads to geometrical errors when measuring tissues due to the pressure exerted by probes. Such deformation has an even larger effect on 3D US volumes as the correct compounding is limited by the inconsistent location and geometry. This work proposes a patient-specified stiffness-based method to correct the tissue deformations in robotic 3D US acquisitions. To obtain the patient-specified model, robotic palpation is performed at sampling positions on the tissue. The contact force, US images and the probe poses of the palpation procedure are recorded. The contact force and the probe poses are used to estimate the nonlinear tissue stiffness. The images are fed to an optical flow algorithm to compute the pixel displacement. Then the pixel-wise tissue deformation under different forces is characterized by a coupled quadratic regression. To correct the deformation at unseen positions on the trajectory for building 3D volumes, an interpolation is performed based on the stiffness values computed at the sampling positions. With the stiffness and recorded force, the tissue displacement could be corrected. The method was validated on two blood vessel phantoms with different stiffness. The results demonstrate that the method can effectively correct the force-induced deformation and finally generate 3D tissue geometries.

## Content
Tissue deformation in ultrasound (US) imaging leads to geometrical errors when measuring tissues due to the pressure exerted by probes. Such deformation has an even larger effect on 3D US volumes as the correct compounding is limited by the inconsistent location and geometry. This work proposes a patient-specified stiffness-based method to correct the tissue deformations in robotic 3D US acquisitions. To obtain the patient-specified model, robotic palpation is performed at sampling positions on the tissue. The contact force, US images and the probe poses of the palpation procedure are recorded. The contact force and the probe poses are used to estimate the nonlinear tissue stiffness. The images are fed to an optical flow algorithm to compute the pixel displacement. Then the pixel-wise tissue deformation under different forces is characterized by a coupled quadratic regression. To correct the deformation at unseen positions on the trajectory for building 3D volumes, an interpolation is performed based on the stiffness values computed at the sampling positions. With the stiffness and recorded force, the tissue displacement could be corrected. The method was validated on two blood vessel phantoms with different stiffness. The results demonstrate that the method can effectively correct the force-induced deformation and finally generate 3D tissue geometries.

## 개요
초음파(US) 영상에서의 조직 변형은 프로브가 가하는 압력으로 인해 조직을 측정할 때 기하학적 오류를 초래합니다. 이러한 변형은 3D US 볼륨에 훨씬 더 큰 영향을 미치는데, 이는 일관되지 않은 위치와 기하학적 구조로 인해 올바른 합성이 제한되기 때문입니다. 본 연구는 로봇 3D US 획득 과정에서 조직 변형을 보정하기 위해 환자 특화 강성 기반 방법을 제안합니다. 환자 특화 모델을 얻기 위해 조직의 샘플링 위치에서 로봇 촉진(palpation)을 수행합니다. 촉진 과정의 접촉력, US 이미지 및 프로브 자세가 기록됩니다. 접촉력과 프로브 자세는 비선형 조직 강성을 추정하는 데 사용됩니다. 이미지는 광학 흐름(optical flow) 알고리즘에 입력되어 픽셀 변위를 계산합니다. 그런 다음 다양한 힘 하에서의 픽셀 단위 조직 변형은 결합 이차 회귀(coupled quadratic regression)로 특성화됩니다. 3D 볼륨 구축을 위한 궤적 상의 보이지 않는 위치에서 변형을 보정하기 위해 샘플링 위치에서 계산된 강성 값을 기반으로 보간(interpolation)이 수행됩니다. 강성과 기록된 힘을 통해 조직 변위를 보정할 수 있습니다. 이 방법은 서로 다른 강성을 가진 두 개의 혈관 팬텀(phantom)에서 검증되었습니다. 결과는 이 방법이 힘으로 인한 변형을 효과적으로 보정하고 최종적으로 3D 조직 기하학적 구조를 생성할 수 있음을 보여줍니다.

## 핵심 내용
초음파(US) 영상에서의 조직 변형은 프로브가 가하는 압력으로 인해 조직을 측정할 때 기하학적 오류를 초래합니다. 이러한 변형은 3D US 볼륨에 훨씬 더 큰 영향을 미치는데, 이는 일관되지 않은 위치와 기하학적 구조로 인해 올바른 합성이 제한되기 때문입니다. 본 연구는 로봇 3D US 획득 과정에서 조직 변형을 보정하기 위해 환자 특화 강성 기반 방법을 제안합니다. 환자 특화 모델을 얻기 위해 조직의 샘플링 위치에서 로봇 촉진을 수행합니다. 촉진 과정의 접촉력, US 이미지 및 프로브 자세가 기록됩니다. 접촉력과 프로브 자세는 비선형 조직 강성을 추정하는 데 사용됩니다. 이미지는 광학 흐름 알고리즘에 입력되어 픽셀 변위를 계산합니다. 그런 다음 다양한 힘 하에서의 픽셀 단위 조직 변형은 결합 이차 회귀로 특성화됩니다. 3D 볼륨 구축을 위한 궤적 상의 보이지 않는 위치에서 변형을 보정하기 위해 샘플링 위치에서 계산된 강성 값을 기반으로 보간이 수행됩니다. 강성과 기록된 힘을 통해 조직 변위를 보정할 수 있습니다. 이 방법은 서로 다른 강성을 가진 두 개의 혈관 팬텀에서 검증되었습니다. 결과는 이 방법이 힘으로 인한 변형을 효과적으로 보정하고 최종적으로 3D 조직 기하학적 구조를 생성할 수 있음을 보여줍니다.
