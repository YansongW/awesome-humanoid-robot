---
$id: ent_robot_system_figure_02
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Figure 02
  zh: Figure 02
  ko: 피규어 02
summary:
  en: Humanoid robot developed by Figure AI for logistics and manufacturing, featuring onboard
    vision-language models and 16-degree-of-freedom hands.
  zh: Figure AI 为物流和制造业开发的人形机器人，配备 onboard 视觉语言模型和 16 自由度手部。
  ko: Figure AI가 물류 및 제조업용으로 개발한 휴인oid 로봇으로, 온보드 비전-언어 모델과 16자유도
    손을 갖추고 있습니다.
domains:
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- validation_markets
functional_roles:
- system
- knowledge
tags:
- figure
- figure_02
- humanoid
- robot_system
- vla
- manipulation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-24'
  confidence: medium
  notes: Specifications and partnership announcements sourced from company communications
    and press coverage; sustained operational data is limited.
sources:
- id: src_001
  type: website
  title: Figure AI Official Website
  url: https://www.figure.ai/
  date: '2026'
  accessed_at: '2026-06-24'
- id: src_002
  type: website
  title: Built In — What Is Figure AI Building?
  url: https://builtin.com/articles/figure-ai
  date: '2024'
  accessed_at: '2026-06-24'
---

# Figure 02

## 抽象

> **生活实例**：它就像仓库里一位既能看懂货架标签、又能用双手分拣包裹的 AI 助手——眼睛看懂，脑子理解，双手执行。

> **自然语言逻辑**：Figure 02 是 Figure AI 开发的第二代通用人形机器人，面向仓储和制造场景；它集成了 onboard 视觉-语言模型和 16 自由度的灵巧手，使机器人能够理解自然语言指令并执行精细抓取与搬运任务。

## Overview

Figure 02 is the second-generation humanoid robot from Figure AI. It is designed for warehouse and factory tasks, with improvements in compute, battery capacity, and hand dexterity over the earlier Figure 01 prototype. The robot integrates six onboard RGB cameras and an onboard vision-language model for perception and task reasoning.

## Key Characteristics

- **Hands**: 16 degrees of freedom with tactile sensing for dexterous manipulation.
- **Cameras**: Six onboard RGB cameras for visual perception.
- **Battery**: 2.25 kWh torso-integrated battery pack, reported to support approximately five to ten hours of operation depending on duty cycle.
- **AI**: Onboard vision-language model for task understanding and planning.

## Relevance to Humanoid Robotics

Figure 02 represents the current state of startup-developed humanoids targeting commercial deployment. Its emphasis on AI-driven task execution and industrial partnerships makes it a useful case study for the path from prototype to operational robot.
