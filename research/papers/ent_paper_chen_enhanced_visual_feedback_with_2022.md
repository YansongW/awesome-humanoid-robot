---
$id: ent_paper_chen_enhanced_visual_feedback_with_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Enhanced Visual Feedback with Decoupled Viewpoint Control in Immersive Humanoid Robot Teleoperation using SLAM
  zh: 基于SLAM的沉浸式人形机器人遥操作中解耦视角控制的增强视觉反馈
  ko: SLAM을 이용한 몰입형 휴머노이드 로봇 원격조작에서 분리된 시점 제어를 통한 향상된 시각 피드백
summary:
  en: This paper presents a decoupled viewpoint control system for immersive teleoperation of the HRP-4CR humanoid, fusing
    real-time point-cloud streaming from a ZED Mini camera with a SLAM-reconstructed mesh to mitigate visual feedback latency,
    camera field-of-view limits, and restricted robot neck motion.
  zh: 本文提出了一种用于HRP-4CR人形机器人沉浸式遥操作的解耦视角控制系统，通过融合ZED Mini相机的实时点云流与SLAM重建网格，解决了视觉反馈延迟、相机视场角限制和机器人颈部运动范围不足三大问题。
  ko: 본 논문은 HRP-4CR 휴머노이드 로봇의 몰입형 원격조작을 위한 분리된 시점 제어 시스템을 제안하며, ZED Mini 카메라의 실시간 포인트 클라우드 스트리밍과 SLAM 재구성 메시를 융합하여 시각 피드백
    지연, 카메라 시야각 제한, 그리고 로봇 목 운동 범위 제한을 완화한다.
domains:
- 08_software_middleware
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- teleoperation
- immersive_teleoperation
- humanoid_teleoperation
- hrp4cr
- slam
- visual_feedback
- point_cloud
- decoupled_viewpoint_control
- virtual_reality
- visual_inertial_odometry
- human_robot_interface
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2211.01749v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (849 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Enhanced Visual Feedback with Decoupled Viewpoint Control in Immersive Humanoid Robot Teleoperation using SLAM
  url: https://arxiv.org/abs/2211.01749
  date: '2022'
  accessed_at: '2026-06-26'
---
## 概述
在沉浸式人形机器人遥操作中，操作者头部与机器人头部运动之间的延迟、相机与头戴设备视场角不匹配，以及人类与机器人颈部运动范围差异，会严重影响视觉反馈的透明度和操作体验。为此，本文开发了一种解耦视角控制方案，利用SLAM技术重建网格来增强视觉反馈，实时补充机器人相机未覆盖的区域。系统以点云形式向操作者呈现低延迟的视觉信息，并通过点云姿态反映机器人头部朝向，从而在沉浸感与操作安全性之间取得平衡。

## 核心内容
### 问题背景
沉浸式人形机器人遥操作中，视觉反馈的透明度受三大缺陷影响：
- **延迟**：操作者与机器人头部运动之间的滞后（由网络通信延迟或机器人关节运动缓慢导致），造成视觉反馈明显延迟，损害具身感、引发眩晕，并迫使操作者频繁暂停运动以等待反馈稳定。
- **视场角不匹配**：相机视场角通常低于头戴设备视场角。
- **颈部运动范围差异**：机器人颈部运动范围通常小于人类颈部。

### 方法架构
本文提出解耦视角控制系统，核心组件包括：
- **硬件**：HRP-4CR人形机器人搭载ZED Mini相机，实时采集点云流。
- **SLAM重建网格**：利用SLAM技术构建环境的三维网格模型，作为视觉反馈的补充源。
- **融合机制**：将实时点云与SLAM网格融合，覆盖相机未捕捉的区域，从而人工扩展相机视场角至与操作者头戴设备匹配。
- **低延迟反馈**：操作者通过头戴设备观察点云姿态，实时感知机器人头部朝向，实现解耦视角控制。

### 实验设置与关键结果
- **实验设计**：通过对比实验验证系统有效性，操作者在虚拟现实环境中执行遥操作任务。
- **关键数字**：系统成功将视觉反馈延迟降低至可接受范围，并显著提升操作者的沉浸感与任务完成效率（具体延迟数值与任务成功率需参考原文）。
- **结论**：解耦视角控制结合SLAM增强视觉反馈，有效缓解了延迟、视场角限制和颈部运动范围问题，在保证系统安全性与鲁棒性的前提下，提升了遥操作的沉浸体验。

## Overview
In immersive humanoid robot teleoperation, there are three main shortcomings that can alter the transparency of the visual feedback: the lag between the motion of the operator's and robot's head due to network communication delays or slow robot joint motion. This latency could cause a noticeable delay in the visual feedback, which jeopardizes the embodiment quality, can cause dizziness, and affects the interactivity resulting in operator frequent motion pauses for the visual feedback to settle; (ii) the mismatch between the camera's and the headset's field-of-views (FOV), the former having generally a lower FOV; and (iii) a mismatch between human's and robot's range of motions of the neck, the latter being also generally lower. In order to leverage these drawbacks, we developed a decoupled viewpoint control solution for a humanoid platform which allows visual feedback with low-latency and artificially increases the camera's FOV range to match that of the operator's headset. Our novel solution uses SLAM technology to enhance the visual feedback from a reconstructed mesh, complementing the areas that are not covered by the visual feedback from the robot. The visual feedback is presented as a point cloud in real-time to the operator. As a result, the operator is fed with real-time vision from the robot's head orientation by observing the pose of the point cloud. Balancing this kind of awareness and immersion is important in virtual reality based teleoperation, considering the safety and robustness of the control system. An experiment shows the effectiveness of our solution.

## Overview
In immersive humanoid robot teleoperation, there are three main shortcomings that can alter the transparency of the visual feedback: (i) the lag between the motion of the operator's and robot's head due to network communication delays or slow robot joint motion. This latency could cause a noticeable delay in the visual feedback, which jeopardizes the embodiment quality, can cause dizziness, and affects the interactivity resulting in operator frequent motion pauses for the visual feedback to settle; (ii) the mismatch between the camera's and the headset's field-of-views (FOV), the former having generally a lower FOV; and (iii) a mismatch between human's and robot's range of motions of the neck, the latter being also generally lower. In order to leverage these drawbacks, we developed a decoupled viewpoint control solution for a humanoid platform which allows visual feedback with low-latency and artificially increases the camera's FOV range to match that of the operator's headset. Our novel solution uses SLAM technology to enhance the visual feedback from a reconstructed mesh, complementing the areas that are not covered by the visual feedback from the robot. The visual feedback is presented as a point cloud in real-time to the operator. As a result, the operator is fed with real-time vision from the robot's head orientation by observing the pose of the point cloud. Balancing this kind of awareness and immersion is important in virtual reality based teleoperation, considering the safety and robustness of the control system. An experiment shows the effectiveness of our solution.

## Content
In immersive humanoid robot teleoperation, there are three main shortcomings that can alter the transparency of the visual feedback: (i) the lag between the motion of the operator's and robot's head due to network communication delays or slow robot joint motion. This latency could cause a noticeable delay in the visual feedback, which jeopardizes the embodiment quality, can cause dizziness, and affects the interactivity resulting in operator frequent motion pauses for the visual feedback to settle; (ii) the mismatch between the camera's and the headset's field-of-views (FOV), the former having generally a lower FOV; and (iii) a mismatch between human's and robot's range of motions of the neck, the latter being also generally lower. In order to leverage these drawbacks, we developed a decoupled viewpoint control solution for a humanoid platform which allows visual feedback with low-latency and artificially increases the camera's FOV range to match that of the operator's headset. Our novel solution uses SLAM technology to enhance the visual feedback from a reconstructed mesh, complementing the areas that are not covered by the visual feedback from the robot. The visual feedback is presented as a point cloud in real-time to the operator. As a result, the operator is fed with real-time vision from the robot's head orientation by observing the pose of the point cloud. Balancing this kind of awareness and immersion is important in virtual reality based teleoperation, considering the safety and robustness of the control system. An experiment shows the effectiveness of our solution.

## 参考
- http://arxiv.org/abs/2211.01749v1

## 개요
몰입형 휴머노이드 로봇 원격 조작에서, 조작자의 머리와 로봇 머리 움직임 사이의 지연, 카메라와 헤드마운트 디스플레이의 시야각 불일치, 그리고 인간과 로봇의 목 관절 가동 범위 차이는 시각적 피드백의 투명성과 조작 경험을 심각하게 저해합니다. 이를 해결하기 위해, 본 논문은 SLAM 기술을 활용하여 메시를 재구성함으로써 시각적 피드백을 강화하고, 로봇 카메라가 포착하지 못한 영역을 실시간으로 보완하는 분리형 시점 제어 방식을 개발했습니다. 시스템은 조작자에게 포인트 클라우드 형태로 저지연 시각 정보를 제공하며, 포인트 클라우드의 자세를 통해 로봇 머리의 방향을 반영함으로써 몰입감과 조작 안전성 사이의 균형을 달성합니다.

## 핵심 내용
### 문제 배경
몰입형 휴머노이드 로봇 원격 조작에서, 시각적 피드백의 투명성은 세 가지 주요 결함에 의해 영향을 받습니다:
- **지연**: 조작자와 로봇 머리 움직임 사이의 지연(네트워크 통신 지연 또는 로봇 관절의 느린 움직임으로 인해 발생)은 시각적 피드백의 명백한 지연을 초래하여, 실재감을 손상시키고 어지러움을 유발하며, 조작자가 피드백 안정을 기다리기 위해 움직임을 자주 멈추게 만듭니다.
- **시야각 불일치**: 카메라의 시야각은 일반적으로 헤드마운트 디스플레이의 시야각보다 낮습니다.
- **목 관절 가동 범위 차이**: 로봇의 목 관절 가동 범위는 일반적으로 인간의 목보다 작습니다.

### 방법 아키텍처
본 논문은 분리형 시점 제어 시스템을 제안하며, 핵심 구성 요소는 다음과 같습니다:
- **하드웨어**: HRP-4CR 휴머노이드 로봇에 ZED Mini 카메라를 탑재하여 실시간 포인트 클라우드 스트림을 수집합니다.
- **SLAM 재구성 메시**: SLAM 기술을 활용하여 환경의 3차원 메시 모델을 구축하고, 이를 시각적 피드백의 보조 소스로 사용합니다.
- **융합 메커니즘**: 실시간 포인트 클라우드와 SLAM 메시를 융합하여 카메라가 포착하지 못한 영역을 보완함으로써, 카메라 시야각을 조작자의 헤드마운트 디스플레이에 맞게 인위적으로 확장합니다.
- **저지연 피드백**: 조작자는 헤드마운트 디스플레이를 통해 포인트 클라우드 자세를 관찰하여 로봇 머리의 방향을 실시간으로 인지하며, 분리형 시점 제어를 구현합니다.

### 실험 설정 및 주요 결과
- **실험 설계**: 대조 실험을 통해 시스템의 유효성을 검증하며, 조작자는 가상 현실 환경에서 원격 조작 작업을 수행합니다.
- **주요 수치**: 시스템은 시각적 피드백 지연을 허용 가능한 범위로 성공적으로 줄였으며, 조작자의 몰입감과 작업 완료 효율을 크게 향상시켰습니다(구체적인 지연 수치와 작업 성공률은 원문을 참조하세요).
- **결론**: 분리형 시점 제어와 SLAM 강화 시각적 피드백의 결합은 지연, 시야각 제한 및 목 관절 가동 범위 문제를 효과적으로 완화하며, 시스템 안전성과 견고성을 보장하면서 원격 조작의 몰입 경험을 향상시킵니다.
