---
$id: ent_paper_humanoid_parkour_learning_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Parkour Learning
  zh: Humanoid Parkour Learning
  ko: Humanoid Parkour Learning
summary:
  en: Humanoid Parkour Learning is a 2024 work on locomotion for humanoid robots.
  zh: Parkour is a grand challenge for legged locomotion, even for quadruped robots, requiring active perception and various
    maneuvers to overcome multiple challenging obstacles. Existing methods for humanoid locomotion either optimize a trajectory
    for a single parkour track or train a reinforcement learning policy only to walk with a significant amount of motion references.
    In this work, we propose a framework for learning an end-to-end vision-based whole-body-control parkour policy for humanoid
    robots that overcomes multiple parkour skills without any motion prior. Using the parkour policy, the hu
  ko: Humanoid Parkour Learning is a 2024 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humanoid_parkour_learning
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.10759v2.
sources:
- id: src_001
  type: paper
  title: Humanoid Parkour Learning (arXiv)
  url: https://arxiv.org/abs/2406.10759
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Humanoid Parkour Learning project page
  url: https://humanoid4parkour.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---

## 概述
Parkour is a grand challenge for legged locomotion, even for quadruped robots, requiring active perception and various maneuvers to overcome multiple challenging obstacles. Existing methods for humanoid locomotion either optimize a trajectory for a single parkour track or train a reinforcement learning policy only to walk with a significant amount of motion references. In this work, we propose a framework for learning an end-to-end vision-based whole-body-control parkour policy for humanoid robots that overcomes multiple parkour skills without any motion prior. Using the parkour policy, the humanoid robot can jump on a 0.42m platform, leap over hurdles, 0.8m gaps, and much more. It can also run at 1.8m/s in the wild and walk robustly on different terrains. We test our policy in indoor and outdoor environments to demonstrate that it can autonomously select parkour skills while following the rotation command of the joystick. We override the arm actions and show that this framework can easily transfer to humanoid mobile manipulation tasks. Videos can be found at https://humanoid4parkour.github.io

## 核心内容
Parkour is a grand challenge for legged locomotion, even for quadruped robots, requiring active perception and various maneuvers to overcome multiple challenging obstacles. Existing methods for humanoid locomotion either optimize a trajectory for a single parkour track or train a reinforcement learning policy only to walk with a significant amount of motion references. In this work, we propose a framework for learning an end-to-end vision-based whole-body-control parkour policy for humanoid robots that overcomes multiple parkour skills without any motion prior. Using the parkour policy, the humanoid robot can jump on a 0.42m platform, leap over hurdles, 0.8m gaps, and much more. It can also run at 1.8m/s in the wild and walk robustly on different terrains. We test our policy in indoor and outdoor environments to demonstrate that it can autonomously select parkour skills while following the rotation command of the joystick. We override the arm actions and show that this framework can easily transfer to humanoid mobile manipulation tasks. Videos can be found at https://humanoid4parkour.github.io

## 参考
- http://arxiv.org/abs/2406.10759v2

## Overview
Parkour is a grand challenge for legged locomotion, even for quadruped robots, requiring active perception and various maneuvers to overcome multiple challenging obstacles. Existing methods for humanoid locomotion either optimize a trajectory for a single parkour track or train a reinforcement learning policy only to walk with a significant amount of motion references. In this work, we propose a framework for learning an end-to-end vision-based whole-body-control parkour policy for humanoid robots that overcomes multiple parkour skills without any motion prior. Using the parkour policy, the humanoid robot can jump on a 0.42m platform, leap over hurdles, 0.8m gaps, and much more. It can also run at 1.8m/s in the wild and walk robustly on different terrains. We test our policy in indoor and outdoor environments to demonstrate that it can autonomously select parkour skills while following the rotation command of the joystick. We override the arm actions and show that this framework can easily transfer to humanoid mobile manipulation tasks. Videos can be found at https://humanoid4parkour.github.io

## Content
Parkour is a grand challenge for legged locomotion, even for quadruped robots, requiring active perception and various maneuvers to overcome multiple challenging obstacles. Existing methods for humanoid locomotion either optimize a trajectory for a single parkour track or train a reinforcement learning policy only to walk with a significant amount of motion references. In this work, we propose a framework for learning an end-to-end vision-based whole-body-control parkour policy for humanoid robots that overcomes multiple parkour skills without any motion prior. Using the parkour policy, the humanoid robot can jump on a 0.42m platform, leap over hurdles, 0.8m gaps, and much more. It can also run at 1.8m/s in the wild and walk robustly on different terrains. We test our policy in indoor and outdoor environments to demonstrate that it can autonomously select parkour skills while following the rotation command of the joystick. We override the arm actions and show that this framework can easily transfer to humanoid mobile manipulation tasks. Videos can be found at https://humanoid4parkour.github.io

## 개요
파쿠르는 보행 로봇, 특히 사족 로봇에게도 큰 도전 과제로, 능동적인 인식과 다양한 기동을 통해 여러 장애물을 극복해야 합니다. 기존의 인간형 로봇 보행 방법은 단일 파쿠르 트랙에 대한 궤적을 최적화하거나, 상당한 양의 동작 참조를 사용하여 보행만을 위한 강화 학습 정책을 훈련합니다. 본 연구에서는 사전 동작 없이도 여러 파쿠르 기술을 극복할 수 있는, 인간형 로봇을 위한 엔드투엔드(end-to-end) 비전 기반 전신 제어 파쿠르 정책 학습 프레임워크를 제안합니다. 이 파쿠르 정책을 통해 인간형 로봇은 0.42m 높이의 플랫폼에 점프하고, 허들, 0.8m 간격의 갭 등을 뛰어넘을 수 있습니다. 또한 야외에서 1.8m/s 속도로 달리고, 다양한 지형에서 견고하게 보행할 수 있습니다. 우리는 실내 및 실외 환경에서 정책을 테스트하여 조이스틱의 회전 명령을 따르면서 자율적으로 파쿠르 기술을 선택할 수 있음을 입증했습니다. 팔 동작을 오버라이드(override)하여 이 프레임워크가 인간형 로봇의 이동 조작 작업에 쉽게 전이될 수 있음을 보여줍니다. 비디오는 https://humanoid4parkour.github.io 에서 확인할 수 있습니다.

## 핵심 내용
파쿠르는 보행 로봇, 특히 사족 로봇에게도 큰 도전 과제로, 능동적인 인식과 다양한 기동을 통해 여러 장애물을 극복해야 합니다. 기존의 인간형 로봇 보행 방법은 단일 파쿠르 트랙에 대한 궤적을 최적화하거나, 상당한 양의 동작 참조를 사용하여 보행만을 위한 강화 학습 정책을 훈련합니다. 본 연구에서는 사전 동작 없이도 여러 파쿠르 기술을 극복할 수 있는, 인간형 로봇을 위한 엔드투엔드(end-to-end) 비전 기반 전신 제어 파쿠르 정책 학습 프레임워크를 제안합니다. 이 파쿠르 정책을 통해 인간형 로봇은 0.42m 높이의 플랫폼에 점프하고, 허들, 0.8m 간격의 갭 등을 뛰어넘을 수 있습니다. 또한 야외에서 1.8m/s 속도로 달리고, 다양한 지형에서 견고하게 보행할 수 있습니다. 우리는 실내 및 실외 환경에서 정책을 테스트하여 조이스틱의 회전 명령을 따르면서 자율적으로 파쿠르 기술을 선택할 수 있음을 입증했습니다. 팔 동작을 오버라이드(override)하여 이 프레임워크가 인간형 로봇의 이동 조작 작업에 쉽게 전이될 수 있음을 보여줍니다. 비디오는 https://humanoid4parkour.github.io 에서 확인할 수 있습니다.
