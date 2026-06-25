---
$id: ent_component_manufacturer_manus
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component_manufacturer
names:
  en: MANUS
  zh: MANUS
  ko: 마누스
summary:
  en: Dutch company specializing in high-precision data gloves for motion capture, virtual
    production, and robot teleoperation.
  zh: 荷兰公司，专注于为动作捕捉、虚拟制作和机器人遥操作提供高精度数据手套。
  ko: 모션 캡처, 가상 제작 및 로봇 원격 조작을 위한 고정밀 데이터 글로브를 전문으로 하는 네덜란드
    기업입니다.
domains:
- 02_components
- 11_applications_markets
layers:
- upstream
- validation_markets
functional_roles:
- organization
- component
tags:
- manus
- data_glove
- hand_tracking
- teleoperation
- motion_capture
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-24'
  confidence: high
  notes: Product lines and integrations are documented on the company's official website.
sources:
- id: src_001
  type: website
  title: MANUS Official Website
  url: https://www.manus-meta.com/
  date: '2026'
  accessed_at: '2026-06-24'
---

# MANUS

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：它原本为电影和游戏做动作捕捉手套，现在这套手套成了机器人遥操作的“遥控器”——人手动一动，机器人手就跟着动。

> **自然语言逻辑**：MANUS 是荷兰公司，专注于高精度数据手套，用于动作捕捉、虚拟制作和机器人遥操作；它能精细记录人手姿态并实时传输给机器人学习框架，为训练灵巧操作策略提供大量人类示范数据。

## Overview

MANUS is a Netherlands-based company that develops data gloves for capturing hand and finger motion. Its products are used in film and game production, biomechanics research, and increasingly in robotics for teleoperation and human-demonstration data collection.

## Key Products

- **Quantum Metagloves**: Sub-millimeter fingertip tracking for high-fidelity capture.
- **Metagloves Pro**: Electromagnetic-field tracking for millimeter-level precision.
- **Metagloves Pro Haptic**: Adds vibrotactile feedback for immersive teleoperation.
- **MANUS Core**: Software for streaming and retargeting hand data to game engines, mocap systems, and robot learning frameworks.

## Relevance to Humanoid Robotics

MANUS gloves are a common peripheral for collecting dexterous manipulation demonstrations. Their integration with NVIDIA Isaac Teleop and Isaac Lab makes them relevant to the data-collection pipeline that feeds learning-based robot policies.
