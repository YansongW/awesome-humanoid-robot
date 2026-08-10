---
$id: ent_paper_polygmap_a_perceptive_locomoti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing'
  zh: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing'
  ko: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing'
summary:
  en: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing is a 2025 work on locomotion for humanoid
    robots.'
  zh: PolygMap 是一个面向人形机器人爬楼梯的感知运动规划框架，由研究团队于 2025 年提出。其核心贡献在于通过多传感器融合（LiDAR、RGB-D 相机与 IMU）实时构建多边形楼梯平面语义地图，并基于此生成足部落脚点，最终在
    NVIDIA Orin 上实现 20-30 Hz 的全身运动规划输出。
  ko: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing is a 2025 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- polygmap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.12346v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (644 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing (arXiv)'
  url: https://arxiv.org/abs/2510.12346
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该框架旨在解决人形机器人在未知空间中精确模仿人类步态的问题，特别是楼梯攀爬场景。PolygMap 的核心思路是首先利用多传感器融合（LiDAR、RGB-D 相机与 IMU）进行平面分割与视觉里程计，实时构建多边形楼梯平面语义地图。随后，基于这些多边形平面段规划足部落脚点，从而生成全身运动规划。整个框架部署在 NVIDIA Orin 上，能够以 20-30 Hz 的频率输出规划结果。室内外真实场景实验均验证了该方法在楼梯攀爬任务中的高效性与鲁棒性。

## 核心内容
### 方法概述
PolygMap 提出了一种基于感知的运动规划框架，其核心流程包括：
- **实时多边形楼梯平面语义地图构建**：通过多传感器融合（LiDAR、RGB-D 相机与 IMU）实现平面分割与视觉里程计，生成楼梯的语义地图。
- **足部落脚点规划**：利用上述多边形平面段，为机器人规划精确的足部落脚位置，以模拟人类在未知空间中的步态。

### 实验设置
- **硬件部署**：框架运行于 NVIDIA Orin 计算平台。
- **规划频率**：全身运动规划输出频率为 20-30 Hz。
- **实验场景**：涵盖室内与室外真实环境，验证方法的通用性。

### 关键结果与结论
- **效率与鲁棒性**：室内外实验均表明，PolygMap 在人形机器人楼梯攀爬任务中表现出高效性与鲁棒性。
- **核心贡献**：通过实时语义地图与多传感器融合，解决了未知空间中精确步态规划的关键挑战。

## Overview
Recently, biped robot walking technology has been significantly developed, mainly in the context of a bland walking scheme. To emulate human walking, robots need to step on the positions they see in unknown spaces accurately. In this paper, we present PolyMap, a perception-based locomotion planning framework for humanoid robots to climb stairs. Our core idea is to build a real-time polygonal staircase plane semantic map, followed by a footstep planar using these polygonal plane segments. These plane segmentation and visual odometry are done by multi-sensor fusion(LiDAR, RGB-D camera and IMUs). The proposed framework is deployed on a NVIDIA Orin, which performs 20-30 Hz whole-body motion planning output. Both indoor and outdoor real-scene experiments indicate that our method is efficient and robust for humanoid robot stair climbing.

## Overview
Recently, biped robot walking technology has been significantly developed, mainly in the context of a bland walking scheme. To emulate human walking, robots need to step on the positions they see in unknown spaces accurately. In this paper, we present PolyMap, a perception-based locomotion planning framework for humanoid robots to climb stairs. Our core idea is to build a real-time polygonal staircase plane semantic map, followed by a footstep planar using these polygonal plane segments. These plane segmentation and visual odometry are done by multi-sensor fusion (LiDAR, RGB-D camera and IMUs). The proposed framework is deployed on an NVIDIA Orin, which performs 20-30 Hz whole-body motion planning output. Both indoor and outdoor real-scene experiments indicate that our method is efficient and robust for humanoid robot stair climbing.

## Content
Recently, biped robot walking technology has been significantly developed, mainly in the context of a bland walking scheme. To emulate human walking, robots need to step on the positions they see in unknown spaces accurately. In this paper, we present PolyMap, a perception-based locomotion planning framework for humanoid robots to climb stairs. Our core idea is to build a real-time polygonal staircase plane semantic map, followed by a footstep planar using these polygonal plane segments. These plane segmentation and visual odometry are done by multi-sensor fusion (LiDAR, RGB-D camera and IMUs). The proposed framework is deployed on an NVIDIA Orin, which performs 20-30 Hz whole-body motion planning output. Both indoor and outdoor real-scene experiments indicate that our method is efficient and robust for humanoid robot stair climbing.

## 参考
- http://arxiv.org/abs/2510.12346v1

## 개요
이 프레임워크는 인간형 로봇이 미지의 공간에서 인간의 보행을 정밀하게 모방하는 문제, 특히 계단 오르기 시나리오를 해결하기 위해 설계되었습니다. PolygMap의 핵심 아이디어는 먼저 다중 센서 융합(LiDAR, RGB-D 카메라 및 IMU)을 활용하여 평면 분할과 시각적 주행 거리 측정을 수행하고, 실시간으로 다각형 계단 평면 의미론적 지도를 구축하는 것입니다. 이후, 이러한 다각형 평면 세그먼트를 기반으로 발 착지점을 계획하여 전신 운동 계획을 생성합니다. 전체 프레임워크는 NVIDIA Orin에 배포되어 20-30 Hz의 주파수로 계획 결과를 출력할 수 있습니다. 실내외 실제 환경 실험 모두 이 방법이 계단 오르기 작업에서 효율성과 견고성을 검증했습니다.

## 핵심 내용
### 방법 개요
PolygMap은 인식 기반 운동 계획 프레임워크를 제안하며, 핵심 프로세스는 다음과 같습니다:
- **실시간 다각형 계단 평면 의미론적 지도 구축**: 다중 센서 융합(LiDAR, RGB-D 카메라 및 IMU)을 통해 평면 분할과 시각적 주행 거리 측정을 구현하여 계단의 의미론적 지도를 생성합니다.
- **발 착지점 계획**: 위의 다각형 평면 세그먼트를 활용하여 로봇의 정밀한 발 착지 위치를 계획함으로써 미지의 공간에서 인간의 보행을 모방합니다.

### 실험 설정
- **하드웨어 배포**: 프레임워크는 NVIDIA Orin 컴퓨팅 플랫폼에서 실행됩니다.
- **계획 주파수**: 전신 운동 계획 출력 주파수는 20-30 Hz입니다.
- **실험 시나리오**: 실내 및 실외 실제 환경을 모두 포함하여 방법의 일반성을 검증합니다.

### 주요 결과 및 결론
- **효율성 및 견고성**: 실내외 실험 모두 PolygMap이 인간형 로봇의 계단 오르기 작업에서 효율성과 견고성을 보여줍니다.
- **핵심 기여**: 실시간 의미론적 지도와 다중 센서 융합을 통해 미지의 공간에서 정밀한 보행 계획의 핵심 과제를 해결합니다.
