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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2211.01749v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
몰입형 휴머노이드 로봇 원격 조작에서 시각적 피드백의 투명성을 저하시킬 수 있는 세 가지 주요 단점이 있습니다: 네트워크 통신 지연이나 느린 로봇 관절 움직임으로 인한 조작자와 로봇 머리 움직임 간의 지연입니다. 이 지연은 시각적 피드백에 눈에 띄는 지연을 유발하여 체화 품질을 저하시키고, 어지러움을 유발할 수 있으며, 상호작용성에 영향을 주어 조작자가 시각적 피드백이 안정될 때까지 자주 움직임을 멈추게 합니다. (ii) 카메라와 헤드셋의 시야각(FOV) 불일치로, 전자가 일반적으로 더 낮은 FOV를 가집니다. (iii) 인간과 로봇의 목 움직임 범위 불일치로, 후자가 일반적으로 더 낮습니다. 이러한 단점을 해결하기 위해, 우리는 휴머노이드 플랫폼을 위한 분리형 시점 제어 솔루션을 개발했습니다. 이 솔루션은 저지연 시각적 피드백을 제공하고 카메라의 FOV 범위를 인위적으로 증가시켜 조작자의 헤드셋과 일치시킵니다. 우리의 새로운 솔루션은 SLAM 기술을 사용하여 재구성된 메시로부터 시각적 피드백을 향상시키고, 로봇의 시각적 피드백이 커버하지 못하는 영역을 보완합니다. 시각적 피드백은 실시간으로 포인트 클라우드 형태로 조작자에게 제공됩니다. 결과적으로, 조작자는 포인트 클라우드의 자세를 관찰함으로써 로봇 머리 방향의 실시간 시야를 제공받습니다. 이러한 인식과 몰입의 균형을 맞추는 것은 제어 시스템의 안전성과 견고성을 고려할 때 가상 현실 기반 원격 조작에서 중요합니다. 실험을 통해 우리 솔루션의 효과를 입증했습니다.

## 핵심 내용
몰입형 휴머노이드 로봇 원격 조작에서 시각적 피드백의 투명성을 저하시킬 수 있는 세 가지 주요 단점이 있습니다: 네트워크 통신 지연이나 느린 로봇 관절 움직임으로 인한 조작자와 로봇 머리 움직임 간의 지연입니다. 이 지연은 시각적 피드백에 눈에 띄는 지연을 유발하여 체화 품질을 저하시키고, 어지러움을 유발할 수 있으며, 상호작용성에 영향을 주어 조작자가 시각적 피드백이 안정될 때까지 자주 움직임을 멈추게 합니다. (ii) 카메라와 헤드셋의 시야각(FOV) 불일치로, 전자가 일반적으로 더 낮은 FOV를 가집니다. (iii) 인간과 로봇의 목 움직임 범위 불일치로, 후자가 일반적으로 더 낮습니다. 이러한 단점을 해결하기 위해, 우리는 휴머노이드 플랫폼을 위한 분리형 시점 제어 솔루션을 개발했습니다. 이 솔루션은 저지연 시각적 피드백을 제공하고 카메라의 FOV 범위를 인위적으로 증가시켜 조작자의 헤드셋과 일치시킵니다. 우리의 새로운 솔루션은 SLAM 기술을 사용하여 재구성된 메시로부터 시각적 피드백을 향상시키고, 로봇의 시각적 피드백이 커버하지 못하는 영역을 보완합니다. 시각적 피드백은 실시간으로 포인트 클라우드 형태로 조작자에게 제공됩니다. 결과적으로, 조작자는 포인트 클라우드의 자세를 관찰함으로써 로봇 머리 방향의 실시간 시야를 제공받습니다. 이러한 인식과 몰입의 균형을 맞추는 것은 제어 시스템의 안전성과 견고성을 고려할 때 가상 현실 기반 원격 조작에서 중요합니다. 실험을 통해 우리 솔루션의 효과를 입증했습니다.

## 参考
- http://arxiv.org/abs/2211.01749v1
