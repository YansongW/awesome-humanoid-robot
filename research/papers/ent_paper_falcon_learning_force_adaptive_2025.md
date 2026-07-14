---
$id: ent_paper_falcon_learning_force_adaptive_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation'
  zh: FALCON｜学习力自适应人形移动操作
  ko: 'FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation'
summary:
  en: ''
  zh: FALCON 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过全身控制器/WBC/MPC转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、末端执行器/腕手目标。关键点是把全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
  ko: FALCON 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过全身控制器/WBC/MPC转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、末端执行器/腕手目标。关键点是把全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
domains:
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- falcon
- manipulation_interface
- mobile_manipulation
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (036). Institution: Carnegie Mellon University.
    Full title: FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation.'
sources:
- id: src_001
  type: website
  title: FALCON project page
  url: https://lecar-lab.github.io/falcon-humanoid
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
FALCON 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过全身控制器/WBC/MPC转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、末端执行器/腕手目标。关键点是把全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。

## 개요
FALCON 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过全身控制器/WBC/MPC转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、末端执行器/腕手目标。关键点是把全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
