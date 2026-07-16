---
$id: ent_paper_zhang_grounding_actions_in_camera_sp_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy'
  zh: OC-VLA
  ko: 'Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy'
summary:
  en: 'Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy (OC-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Shanghai AI Lab, SenseTime Research, Nanjing University,
    Tsinghua University.'
  zh: 'Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy (OC-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Shanghai AI Lab, SenseTime Research, Nanjing University,
    Tsinghua University.'
  ko: 'Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy (OC-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Shanghai AI Lab, SenseTime Research, Nanjing University,
    Tsinghua University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- oc_vla
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.13103v1.
sources:
- id: src_001
  type: paper
  title: 'Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy (arXiv)'
  url: https://arxiv.org/abs/2508.13103
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OC-VLA source
  url: https://doi.org/10.48550/arXiv.2508.13103
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models frequently encounter challenges in generalizing to real-world environments due to inherent discrepancies between observation and action spaces. Although training data are collected from diverse camera perspectives, the models typically predict end-effector poses within the robot base coordinate frame, resulting in spatial inconsistencies. To mitigate this limitation, we introduce the Observation-Centric VLA (OC-VLA) framework, which grounds action predictions directly in the camera observation space. Leveraging the camera's extrinsic calibration matrix, OC-VLA transforms end-effector poses from the robot base coordinate system into the camera coordinate system, thereby unifying prediction targets across heterogeneous viewpoints. This lightweight, plug-and-play strategy ensures robust alignment between perception and action, substantially improving model resilience to camera viewpoint variations. The proposed approach is readily compatible with existing VLA architectures, requiring no substantial modifications. Comprehensive evaluations on both simulated and real-world robotic manipulation tasks demonstrate that OC-VLA accelerates convergence, enhances task success rates, and improves cross-view generalization. The code will be publicly available.

## 核心内容
Vision-Language-Action (VLA) models frequently encounter challenges in generalizing to real-world environments due to inherent discrepancies between observation and action spaces. Although training data are collected from diverse camera perspectives, the models typically predict end-effector poses within the robot base coordinate frame, resulting in spatial inconsistencies. To mitigate this limitation, we introduce the Observation-Centric VLA (OC-VLA) framework, which grounds action predictions directly in the camera observation space. Leveraging the camera's extrinsic calibration matrix, OC-VLA transforms end-effector poses from the robot base coordinate system into the camera coordinate system, thereby unifying prediction targets across heterogeneous viewpoints. This lightweight, plug-and-play strategy ensures robust alignment between perception and action, substantially improving model resilience to camera viewpoint variations. The proposed approach is readily compatible with existing VLA architectures, requiring no substantial modifications. Comprehensive evaluations on both simulated and real-world robotic manipulation tasks demonstrate that OC-VLA accelerates convergence, enhances task success rates, and improves cross-view generalization. The code will be publicly available.

## 参考
- http://arxiv.org/abs/2508.13103v1

## Overview
Vision-Language-Action (VLA) models frequently encounter challenges in generalizing to real-world environments due to inherent discrepancies between observation and action spaces. Although training data are collected from diverse camera perspectives, the models typically predict end-effector poses within the robot base coordinate frame, resulting in spatial inconsistencies. To mitigate this limitation, we introduce the Observation-Centric VLA (OC-VLA) framework, which grounds action predictions directly in the camera observation space. Leveraging the camera's extrinsic calibration matrix, OC-VLA transforms end-effector poses from the robot base coordinate system into the camera coordinate system, thereby unifying prediction targets across heterogeneous viewpoints. This lightweight, plug-and-play strategy ensures robust alignment between perception and action, substantially improving model resilience to camera viewpoint variations. The proposed approach is readily compatible with existing VLA architectures, requiring no substantial modifications. Comprehensive evaluations on both simulated and real-world robotic manipulation tasks demonstrate that OC-VLA accelerates convergence, enhances task success rates, and improves cross-view generalization. The code will be publicly available.

## Content
Vision-Language-Action (VLA) models frequently encounter challenges in generalizing to real-world environments due to inherent discrepancies between observation and action spaces. Although training data are collected from diverse camera perspectives, the models typically predict end-effector poses within the robot base coordinate frame, resulting in spatial inconsistencies. To mitigate this limitation, we introduce the Observation-Centric VLA (OC-VLA) framework, which grounds action predictions directly in the camera observation space. Leveraging the camera's extrinsic calibration matrix, OC-VLA transforms end-effector poses from the robot base coordinate system into the camera coordinate system, thereby unifying prediction targets across heterogeneous viewpoints. This lightweight, plug-and-play strategy ensures robust alignment between perception and action, substantially improving model resilience to camera viewpoint variations. The proposed approach is readily compatible with existing VLA architectures, requiring no substantial modifications. Comprehensive evaluations on both simulated and real-world robotic manipulation tasks demonstrate that OC-VLA accelerates convergence, enhances task success rates, and improves cross-view generalization. The code will be publicly available.

## 개요
Vision-Language-Action (VLA) 모델은 관찰 공간과 행동 공간 간의 본질적인 차이로 인해 실제 환경에 일반화하는 데 자주 어려움을 겪습니다. 훈련 데이터가 다양한 카메라 시점에서 수집되지만, 모델은 일반적으로 로봇 베이스 좌표계 내에서 엔드 이펙터(end-effector) 자세를 예측하여 공간적 불일치를 초래합니다. 이러한 한계를 완화하기 위해, 우리는 행동 예측을 카메라 관찰 공간에 직접 기반하는 Observation-Centric VLA (OC-VLA) 프레임워크를 소개합니다. 카메라의 외부 캘리브레이션 행렬을 활용하여 OC-VLA는 엔드 이펙터 자세를 로봇 베이스 좌표계에서 카메라 좌표계로 변환함으로써 이질적인 시점 간 예측 대상을 통합합니다. 이 경량의 플러그 앤 플레이(plug-and-play) 전략은 지각과 행동 간의 강력한 정렬을 보장하며, 카메라 시점 변화에 대한 모델의 복원력을 크게 향상시킵니다. 제안된 접근 방식은 기존 VLA 아키텍처와 쉽게 호환되며, 큰 수정이 필요하지 않습니다. 시뮬레이션 및 실제 로봇 조작 작업에 대한 포괄적인 평가는 OC-VLA가 수렴을 가속화하고, 작업 성공률을 높이며, 교차 시점 일반화를 개선함을 보여줍니다. 코드는 공개될 예정입니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 관찰 공간과 행동 공간 간의 본질적인 차이로 인해 실제 환경에 일반화하는 데 자주 어려움을 겪습니다. 훈련 데이터가 다양한 카메라 시점에서 수집되지만, 모델은 일반적으로 로봇 베이스 좌표계 내에서 엔드 이펙터 자세를 예측하여 공간적 불일치를 초래합니다. 이러한 한계를 완화하기 위해, 우리는 행동 예측을 카메라 관찰 공간에 직접 기반하는 Observation-Centric VLA (OC-VLA) 프레임워크를 소개합니다. 카메라의 외부 캘리브레이션 행렬을 활용하여 OC-VLA는 엔드 이펙터 자세를 로봇 베이스 좌표계에서 카메라 좌표계로 변환함으로써 이질적인 시점 간 예측 대상을 통합합니다. 이 경량의 플러그 앤 플레이 전략은 지각과 행동 간의 강력한 정렬을 보장하며, 카메라 시점 변화에 대한 모델의 복원력을 크게 향상시킵니다. 제안된 접근 방식은 기존 VLA 아키텍처와 쉽게 호환되며, 큰 수정이 필요하지 않습니다. 시뮬레이션 및 실제 로봇 조작 작업에 대한 포괄적인 평가는 OC-VLA가 수렴을 가속화하고, 작업 성공률을 높이며, 교차 시점 일반화를 개선함을 보여줍니다. 코드는 공개될 예정입니다.
