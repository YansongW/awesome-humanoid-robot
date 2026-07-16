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
  zh: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing is a 2025 work on locomotion for humanoid
    robots.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.12346v1.
sources:
- id: src_001
  type: paper
  title: 'PolygMap: A Perceptive Locomotion Framework for Humanoid Robot Stair Climbing (arXiv)'
  url: https://arxiv.org/abs/2510.12346
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recently, biped robot walking technology has been significantly developed, mainly in the context of a bland walking scheme. To emulate human walking, robots need to step on the positions they see in unknown spaces accurately. In this paper, we present PolyMap, a perception-based locomotion planning framework for humanoid robots to climb stairs. Our core idea is to build a real-time polygonal staircase plane semantic map, followed by a footstep planar using these polygonal plane segments. These plane segmentation and visual odometry are done by multi-sensor fusion(LiDAR, RGB-D camera and IMUs). The proposed framework is deployed on a NVIDIA Orin, which performs 20-30 Hz whole-body motion planning output. Both indoor and outdoor real-scene experiments indicate that our method is efficient and robust for humanoid robot stair climbing.

## 核心内容
Recently, biped robot walking technology has been significantly developed, mainly in the context of a bland walking scheme. To emulate human walking, robots need to step on the positions they see in unknown spaces accurately. In this paper, we present PolyMap, a perception-based locomotion planning framework for humanoid robots to climb stairs. Our core idea is to build a real-time polygonal staircase plane semantic map, followed by a footstep planar using these polygonal plane segments. These plane segmentation and visual odometry are done by multi-sensor fusion(LiDAR, RGB-D camera and IMUs). The proposed framework is deployed on a NVIDIA Orin, which performs 20-30 Hz whole-body motion planning output. Both indoor and outdoor real-scene experiments indicate that our method is efficient and robust for humanoid robot stair climbing.

## 参考
- http://arxiv.org/abs/2510.12346v1

## Overview
Recently, biped robot walking technology has been significantly developed, mainly in the context of a bland walking scheme. To emulate human walking, robots need to step on the positions they see in unknown spaces accurately. In this paper, we present PolyMap, a perception-based locomotion planning framework for humanoid robots to climb stairs. Our core idea is to build a real-time polygonal staircase plane semantic map, followed by a footstep planar using these polygonal plane segments. These plane segmentation and visual odometry are done by multi-sensor fusion (LiDAR, RGB-D camera and IMUs). The proposed framework is deployed on an NVIDIA Orin, which performs 20-30 Hz whole-body motion planning output. Both indoor and outdoor real-scene experiments indicate that our method is efficient and robust for humanoid robot stair climbing.

## Content
Recently, biped robot walking technology has been significantly developed, mainly in the context of a bland walking scheme. To emulate human walking, robots need to step on the positions they see in unknown spaces accurately. In this paper, we present PolyMap, a perception-based locomotion planning framework for humanoid robots to climb stairs. Our core idea is to build a real-time polygonal staircase plane semantic map, followed by a footstep planar using these polygonal plane segments. These plane segmentation and visual odometry are done by multi-sensor fusion (LiDAR, RGB-D camera and IMUs). The proposed framework is deployed on an NVIDIA Orin, which performs 20-30 Hz whole-body motion planning output. Both indoor and outdoor real-scene experiments indicate that our method is efficient and robust for humanoid robot stair climbing.

## 개요
최근 이족 보행 로봇의 보행 기술은 주로 평탄한 보행 방식의 맥락에서 크게 발전해 왔습니다. 인간의 보행을 모방하기 위해 로봇은 미지의 공간에서 자신이 본 위치를 정확히 밟아야 합니다. 본 논문에서는 인간형 로봇이 계단을 오르기 위한 인식 기반 이동 계획 프레임워크인 PolyMap을 제시합니다. 핵심 아이디어는 실시간 다각형 계단 평면 의미 맵을 구축한 후, 이러한 다각형 평면 세그먼트를 사용하여 발판 평면을 생성하는 것입니다. 이러한 평면 분할과 시각적 주행 거리 측정은 다중 센서 융합(LiDAR, RGB-D 카메라 및 IMU)을 통해 수행됩니다. 제안된 프레임워크는 NVIDIA Orin에 배포되어 20-30Hz의 전신 동작 계획 출력을 수행합니다. 실내 및 실외 실제 환경 실험 모두에서 본 방법이 인간형 로봇의 계단 오르기에 효율적이고 강건함을 보여줍니다.

## 핵심 내용
최근 이족 보행 로봇의 보행 기술은 주로 평탄한 보행 방식의 맥락에서 크게 발전해 왔습니다. 인간의 보행을 모방하기 위해 로봇은 미지의 공간에서 자신이 본 위치를 정확히 밟아야 합니다. 본 논문에서는 인간형 로봇이 계단을 오르기 위한 인식 기반 이동 계획 프레임워크인 PolyMap을 제시합니다. 핵심 아이디어는 실시간 다각형 계단 평면 의미 맵을 구축한 후, 이러한 다각형 평면 세그먼트를 사용하여 발판 평면을 생성하는 것입니다. 이러한 평면 분할과 시각적 주행 거리 측정은 다중 센서 융합(LiDAR, RGB-D 카메라 및 IMU)을 통해 수행됩니다. 제안된 프레임워크는 NVIDIA Orin에 배포되어 20-30Hz의 전신 동작 계획 출력을 수행합니다. 실내 및 실외 실제 환경 실험 모두에서 본 방법이 인간형 로봇의 계단 오르기에 효율적이고 강건함을 보여줍니다.
