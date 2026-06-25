---
$id: ent_component_manus_metaglove
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: MANUS Metagloves
  zh: MANUS Metagloves 数据手套
  ko: MANUS Metagloves
summary:
  en: A family of high-precision data gloves for hand tracking, motion capture, and robot
    teleoperation, using electromagnetic, quantum, or inertial tracking technologies.
  zh: 一系列用于手部追踪、动作捕捉和机器人遥操作的高精度数据手套，采用电磁、量子或惯性追踪技术。
  ko: 전자기, 양자 또는 관성 추적 기술을 사용하여 손 추적, 모션 캡처 및 로봇 원격 조작을 위한 고정밀 데이터 글로브 제품군.
domains:
- 02_components
- 11_applications_markets
layers:
- upstream
- validation_markets
functional_roles:
- component
- knowledge
tags:
- manus
- data_glove
- hand_tracking
- teleoperation
- motion_capture
- haptic_feedback
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: Product family overview; specific models include Quantum Metagloves, Metagloves Pro,
    and Metagloves Pro Haptic.
sources:
- id: src_001
  type: website
  title: MANUS Official Website
  url: https://www.manus-meta.com/
  date: '2026'
  accessed_at: '2026-06-22'
- id: src_002
  type: paper
  title: 'RUKA: Rethinking the Design of Humanoid Hands with Learning'
  url: https://arxiv.org/abs/2504.13165
  date: '2025'
  accessed_at: '2026-06-22'
---

## Overview

MANUS Metagloves are professional data gloves developed by MANUS (Netherlands) for capturing high-fidelity hand and finger motion. They are used in motion capture, virtual production, biomechanics research, and increasingly in robotics for teleoperation and human-hand dataset collection. Different product lines use different tracking technologies: Quantum Metagloves use sub-millimeter fingertip tracking sensors; Metagloves Pro use electromagnetic-field (EMF) tracking for millimeter-level precision; and Metagloves Pro Haptic add vibrotactile feedback.

The gloves track up to 25 degrees of freedom of the hand and stream data through MANUS Core software to game engines, mocap systems, and robot learning frameworks. They are officially integrated with NVIDIA Isaac Teleop and Isaac Lab, making them a common choice for collecting human demonstration data for dexterous robot policies.

## Key Characteristics

- Up to 25 hand degrees of freedom tracked
- Electromagnetic, quantum, or inertial sensing options
- MANUS Core software for streaming and retargeting
- Compatibility with NVIDIA Isaac Teleop / Isaac Lab
- Optional haptic feedback variants
- Wireless operation with swappable batteries

## Relevance to Humanoid Robotics

MANUS gloves are a key data-collection and teleoperation peripheral for training humanoid manipulation policies. They enable precise capture of human hand pose and motion, which can be retargeted to robot hands such as LEAP, Allegro, or Dex3-1. Their adoption in robot learning pipelines highlights the importance of high-quality human demonstration data for scaling dexterous manipulation.
