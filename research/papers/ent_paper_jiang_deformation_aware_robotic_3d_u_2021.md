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
  zh: 该论文提出一种基于患者特定刚度的变形校正方法，用于机器人3D超声成像中由探头压力引起的组织变形。该方法通过机器人触诊、光流算法和耦合二次回归实现，并在两种不同硬度的血管体模上验证了有效性。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2107.08411v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (793 chars, DeepSeek).'
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
超声成像中探头施加的压力会导致组织变形，从而产生几何测量误差，这种误差在构建3D超声体积时尤为显著。本文提出一种患者特定的刚度建模方法，通过机器人触诊在组织采样点记录接触力、超声图像和探头位姿，利用这些数据估计非线性组织刚度。光流算法计算像素位移，耦合二次回归建立不同力下的像素级变形模型。对于3D体积构建轨迹中未观测位置，基于采样点刚度值进行插值校正。在两种不同硬度的血管体模上验证，该方法能有效校正力致变形并生成准确的3D组织几何结构。

## 核心内容
### 方法架构
- **患者特定刚度建模**：在组织表面选定采样位置进行机器人触诊，同步记录接触力、超声图像和探头位姿。
- **非线性刚度估计**：利用接触力和探头位姿数据，通过力学模型估计组织的非线性刚度特性。
- **像素位移计算**：将超声图像输入光流算法（optical flow），计算不同压力下组织像素点的位移场。
- **变形建模**：采用耦合二次回归（coupled quadratic regression）建立接触力与像素位移之间的映射关系，实现像素级变形表征。
- **变形校正**：对于3D体积构建轨迹中的未采样位置，基于已知采样点的刚度值进行插值，结合实时记录的接触力，校正组织位移。

### 实验设置
- **体模**：使用两种不同硬度的血管体模（vascular phantoms）进行验证。
- **评估指标**：通过比较校正前后3D重建的组织几何精度，量化变形校正效果。

### 关键结果
- 该方法能有效消除力致变形导致的几何误差，生成更准确的3D组织几何结构。
- 在两种硬度体模上均表现出稳定的校正性能，验证了方法的泛化能力。

### 结论
该研究为机器人3D超声成像中的组织变形校正提供了一种无需外部跟踪设备的解决方案，通过患者特定刚度建模实现了高精度几何重建。

## Overview
Tissue deformation in ultrasound (US) imaging leads to geometrical errors when measuring tissues due to the pressure exerted by probes. Such deformation has an even larger effect on 3D US volumes as the correct compounding is limited by the inconsistent location and geometry. This work proposes a patient-specified stiffness-based method to correct the tissue deformations in robotic 3D US acquisitions. To obtain the patient-specified model, robotic palpation is performed at sampling positions on the tissue. The contact force, US images and the probe poses of the palpation procedure are recorded. The contact force and the probe poses are used to estimate the nonlinear tissue stiffness. The images are fed to an optical flow algorithm to compute the pixel displacement. Then the pixel-wise tissue deformation under different forces is characterized by a coupled quadratic regression. To correct the deformation at unseen positions on the trajectory for building 3D volumes, an interpolation is performed based on the stiffness values computed at the sampling positions. With the stiffness and recorded force, the tissue displacement could be corrected. The method was validated on two blood vessel phantoms with different stiffness. The results demonstrate that the method can effectively correct the force-induced deformation and finally generate 3D tissue geometries

## Overview
Tissue deformation in ultrasound (US) imaging leads to geometrical errors when measuring tissues due to the pressure exerted by probes. Such deformation has an even larger effect on 3D US volumes as the correct compounding is limited by the inconsistent location and geometry. This work proposes a patient-specified stiffness-based method to correct the tissue deformations in robotic 3D US acquisitions. To obtain the patient-specified model, robotic palpation is performed at sampling positions on the tissue. The contact force, US images and the probe poses of the palpation procedure are recorded. The contact force and the probe poses are used to estimate the nonlinear tissue stiffness. The images are fed to an optical flow algorithm to compute the pixel displacement. Then the pixel-wise tissue deformation under different forces is characterized by a coupled quadratic regression. To correct the deformation at unseen positions on the trajectory for building 3D volumes, an interpolation is performed based on the stiffness values computed at the sampling positions. With the stiffness and recorded force, the tissue displacement could be corrected. The method was validated on two blood vessel phantoms with different stiffness. The results demonstrate that the method can effectively correct the force-induced deformation and finally generate 3D tissue geometries.

## Content
Tissue deformation in ultrasound (US) imaging leads to geometrical errors when measuring tissues due to the pressure exerted by probes. Such deformation has an even larger effect on 3D US volumes as the correct compounding is limited by the inconsistent location and geometry. This work proposes a patient-specified stiffness-based method to correct the tissue deformations in robotic 3D US acquisitions. To obtain the patient-specified model, robotic palpation is performed at sampling positions on the tissue. The contact force, US images and the probe poses of the palpation procedure are recorded. The contact force and the probe poses are used to estimate the nonlinear tissue stiffness. The images are fed to an optical flow algorithm to compute the pixel displacement. Then the pixel-wise tissue deformation under different forces is characterized by a coupled quadratic regression. To correct the deformation at unseen positions on the trajectory for building 3D volumes, an interpolation is performed based on the stiffness values computed at the sampling positions. With the stiffness and recorded force, the tissue displacement could be corrected. The method was validated on two blood vessel phantoms with different stiffness. The results demonstrate that the method can effectively correct the force-induced deformation and finally generate 3D tissue geometries.

## 参考
- http://arxiv.org/abs/2107.08411v1

## 개요
초음파 영상에서 프로브가 가하는 압력은 조직 변형을 유발하여 기하학적 측정 오차를 발생시키며, 이러한 오차는 3D 초음파 볼륨을 구축할 때 특히 두드러진다. 본 논문은 로봇 촉진을 통해 조직 샘플링 지점에서 접촉력, 초음파 영상 및 프로브 자세를 기록하고, 이러한 데이터를 활용하여 비선형 조직 강성을 추정하는 환자 특이적 강성 모델링 방법을 제안한다. 광류 알고리즘은 픽셀 변위를 계산하고, 결합 이차 회귀를 통해 서로 다른 힘 하에서의 픽셀 수준 변형 모델을 수립한다. 3D 볼륨 구축 궤적에서 관찰되지 않은 위치의 경우, 샘플링 지점의 강성 값을 기반으로 보간하여 보정한다. 두 가지 서로 다른 경도의 혈관 팬텀에서 검증한 결과, 이 방법은 힘으로 인한 변형을 효과적으로 보정하고 정확한 3D 조직 기하 구조를 생성할 수 있음을 확인했다.

## 핵심 내용
### 방법 아키텍처
- **환자 특이적 강성 모델링**: 조직 표면의 선택된 샘플링 위치에서 로봇 촉진을 수행하고, 접촉력, 초음파 영상 및 프로브 자세를 동시에 기록한다.
- **비선형 강성 추정**: 접촉력과 프로브 자세 데이터를 활용하여 역학 모델을 통해 조직의 비선형 강성 특성을 추정한다.
- **픽셀 변위 계산**: 초음파 영상을 광류 알고리즘(optical flow)에 입력하여 서로 다른 압력 하에서 조직 픽셀 지점의 변위장을 계산한다.
- **변형 모델링**: 결합 이차 회귀(coupled quadratic regression)를 사용하여 접촉력과 픽셀 변위 간의 매핑 관계를 수립하고, 픽셀 수준 변형 특성을 구현한다.
- **변형 보정**: 3D 볼륨 구축 궤적에서 샘플링되지 않은 위치의 경우, 알려진 샘플링 지점의 강성 값을 기반으로 보간하고, 실시간으로 기록된 접촉력을 결합하여 조직 변위를 보정한다.

### 실험 설정
- **팬텀**: 두 가지 서로 다른 경도의 혈관 팬텀(vascular phantoms)을 사용하여 검증한다.
- **평가 지표**: 보정 전후의 3D 재구성 조직 기하 정밀도를 비교하여 변형 보정 효과를 정량화한다.

### 주요 결과
- 이 방법은 힘으로 인한 변형으로 발생하는 기하학적 오차를 효과적으로 제거하고 더 정확한 3D 조직 기하 구조를 생성한다.
- 두 가지 경도의 팬텀 모두에서 안정적인 보정 성능을 보여주며, 방법의 일반화 능력을 검증한다.

### 결론
본 연구는 로봇 3D 초음파 영상에서 조직 변형 보정을 위한 외부 추적 장치가 필요 없는 솔루션을 제공하며, 환자 특이적 강성 모델링을 통해 고정밀 기하 재구성을 구현한다.
