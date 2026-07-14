---
$id: ent_paper_viral_visual_sim_to_real_at_sc_2025_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation'
  zh: VIRAL｜大规模视觉模拟现实世界，用于人形移动操作
  ko: 'VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation'
summary:
  en: ''
  zh: VIRAL 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过教师-学生知识迁移、ACT/行为克隆模仿学习、分层技能/专家策略转成可训练、可复用的可执行动作命令。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
  ko: VIRAL 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过教师-学生知识迁移、ACT/行为克隆模仿学习、分层技能/专家策略转成可训练、可复用的可执行动作命令。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- scene_understanding
- viral
- vision_guided_control
- visual_perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (081). Institution: NVIDIA、CMU、UC Berkeley.
    Full title: VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation.'
sources:
- id: src_001
  type: website
  title: VIRAL project page
  url: https://viral-humanoid.github.io
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
VIRAL 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过教师-学生知识迁移、ACT/行为克隆模仿学习、分层技能/专家策略转成可训练、可复用的可执行动作命令。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。

## 개요
VIRAL 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过教师-学生知识迁移、ACT/行为克隆模仿学习、分层技能/专家策略转成可训练、可复用的可执行动作命令。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
