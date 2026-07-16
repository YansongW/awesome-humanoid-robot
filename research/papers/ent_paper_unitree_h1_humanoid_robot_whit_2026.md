---
$id: ent_paper_unitree_h1_humanoid_robot_whit_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unitree H1 Humanoid Robot Whitepaper & Specifications
  zh: Unitree H1 Humanoid Robot Whitepaper & Specifications
  ko: Unitree H1 Humanoid Robot Whitepaper & Specifications
summary:
  en: This paper presents a vision-based human action imitation system based on humanoid robots. A forward-facing OAK-Lite
    RGB-D camera mounted approximately 1.2 m in front of the robot is used to capture human motion and reproduce upper-body
    actions in real time. To improve the stability of depth-based keypoints, we employ a cascaded Kalman and weighted moving
    average filter that effectively reduces shake. A warm-start symbolic inverse kinematics solver with velocity-bounded optimization
    enables stable 8-DoF arm control within 12–18 ms. In addition, a finite-state lower-limb gesture recognizer provides intuitive
    locomotion commands, forming a unified full-body imitation framework. Experiments on the Unitree H1 robot demonstrate
    72 ms end-to-end latency, 3.38° joint error, and 95% gesture recogn
  zh: Unitree H1 Humanoid Robot Whitepaper & Specifications is a paper on 硬件设计 for humanoid robotics.
  ko: Unitree H1 Humanoid Robot Whitepaper & Specifications is a paper on 硬件设计 for humanoid robotics.
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- hardware_design
- humanoid
- unitree_h1_humanoid_robot_whit
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: Unitree H1 Humanoid Robot
    Whitepaper & Specifications.'
sources:
- id: src_001
  type: website
  title: Unitree H1 Humanoid Robot Whitepaper & Specifications
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents a vision-based human action imitation system based on humanoid robots. A forward-facing OAK-Lite RGB-D camera mounted approximately 1.2 m in front of the robot is used to capture human motion and reproduce upper-body actions in real time. To improve the stability of depth-based keypoints, we employ a cascaded Kalman and weighted moving average filter that effectively reduces shake. A warm-start symbolic inverse kinematics solver with velocity-bounded optimization enables stable 8-DoF arm control within 12–18 ms. In addition, a finite-state lower-limb gesture recognizer provides intuitive locomotion commands, forming a unified full-body imitation framework. Experiments on the Unitree H1 robot demonstrate 72 ms end-to-end latency, 3.38° joint error, and 95% gesture recognition accuracy, validating the system’s smooth and responsive imitation performance.

## 核心内容
This paper presents a vision-based human action imitation system based on humanoid robots. A forward-facing OAK-Lite RGB-D camera mounted approximately 1.2 m in front of the robot is used to capture human motion and reproduce upper-body actions in real time. To improve the stability of depth-based keypoints, we employ a cascaded Kalman and weighted moving average filter that effectively reduces shake. A warm-start symbolic inverse kinematics solver with velocity-bounded optimization enables stable 8-DoF arm control within 12–18 ms. In addition, a finite-state lower-limb gesture recognizer provides intuitive locomotion commands, forming a unified full-body imitation framework. Experiments on the Unitree H1 robot demonstrate 72 ms end-to-end latency, 3.38° joint error, and 95% gesture recognition accuracy, validating the system’s smooth and responsive imitation performance.

## 参考
- Semantic Scholar search: Unitree H1 Humanoid Robot Whitepaper & Specifications

## Overview
This paper presents a vision-based human action imitation system based on humanoid robots. A forward-facing OAK-Lite RGB-D camera mounted approximately 1.2 m in front of the robot is used to capture human motion and reproduce upper-body actions in real time. To improve the stability of depth-based keypoints, we employ a cascaded Kalman and weighted moving average filter that effectively reduces shake. A warm-start symbolic inverse kinematics solver with velocity-bounded optimization enables stable 8-DoF arm control within 12–18 ms. In addition, a finite-state lower-limb gesture recognizer provides intuitive locomotion commands, forming a unified full-body imitation framework. Experiments on the Unitree H1 robot demonstrate 72 ms end-to-end latency, 3.38° joint error, and 95% gesture recognition accuracy, validating the system’s smooth and responsive imitation performance.

## Content
This paper presents a vision-based human action imitation system based on humanoid robots. A forward-facing OAK-Lite RGB-D camera mounted approximately 1.2 m in front of the robot is used to capture human motion and reproduce upper-body actions in real time. To improve the stability of depth-based keypoints, we employ a cascaded Kalman and weighted moving average filter that effectively reduces shake. A warm-start symbolic inverse kinematics solver with velocity-bounded optimization enables stable 8-DoF arm control within 12–18 ms. In addition, a finite-state lower-limb gesture recognizer provides intuitive locomotion commands, forming a unified full-body imitation framework. Experiments on the Unitree H1 robot demonstrate 72 ms end-to-end latency, 3.38° joint error, and 95% gesture recognition accuracy, validating the system’s smooth and responsive imitation performance.

## 개요
본 논문은 휴머노이드 로봇 기반의 비전 기반 인간 동작 모방 시스템을 제시합니다. 로봇 전방 약 1.2m 지점에 장착된 전방향 OAK-Lite RGB-D 카메라를 사용하여 인간의 움직임을 포착하고 상체 동작을 실시간으로 재현합니다. 깊이 기반 키포인트의 안정성을 향상시키기 위해, 캐스케이드 칼만 필터와 가중 이동 평균 필터를 적용하여 흔들림을 효과적으로 줄였습니다. 속도 제한 최적화를 적용한 웜스타트 기호 역기구학 솔버를 통해 12~18ms 내에 안정적인 8자유도 팔 제어를 구현합니다. 또한, 유한 상태 하체 제스처 인식기를 통해 직관적인 이동 명령을 제공하여 통합된 전신 모방 프레임워크를 구성합니다. Unitree H1 로봇 실험 결과, 종단 간 지연 시간 72ms, 관절 오차 3.38°, 제스처 인식 정확도 95%를 달성하여 시스템의 부드럽고 반응성 높은 모방 성능을 입증했습니다.

## 핵심 내용
본 논문은 휴머노이드 로봇 기반의 비전 기반 인간 동작 모방 시스템을 제시합니다. 로봇 전방 약 1.2m 지점에 장착된 전방향 OAK-Lite RGB-D 카메라를 사용하여 인간의 움직임을 포착하고 상체 동작을 실시간으로 재현합니다. 깊이 기반 키포인트의 안정성을 향상시키기 위해, 캐스케이드 칼만 필터와 가중 이동 평균 필터를 적용하여 흔들림을 효과적으로 줄였습니다. 속도 제한 최적화를 적용한 웜스타트 기호 역기구학 솔버를 통해 12~18ms 내에 안정적인 8자유도 팔 제어를 구현합니다. 또한, 유한 상태 하체 제스처 인식기를 통해 직관적인 이동 명령을 제공하여 통합된 전신 모방 프레임워크를 구성합니다. Unitree H1 로봇 실험 결과, 종단 간 지연 시간 72ms, 관절 오차 3.38°, 제스처 인식 정확도 95%를 달성하여 시스템의 부드럽고 반응성 높은 모방 성능을 입증했습니다.
