---
$id: ent_paper_demohlm_from_one_demonstration_2025_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation'
  zh: DemoHLM｜从单一示范到通用人形移动操作
  ko: 'DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation'
summary:
  en: ''
  zh: DemoHLM 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、全身控制器/WBC/MPC、闭环纠错/人类干预转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作
    chunk 或闭环执行降低时序抖动。
  ko: DemoHLM 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、全身控制器/WBC/MPC、闭环纠错/人类干预转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作
    chunk 或闭环执行降低时序抖动。
domains:
- 02_components
- 06_design_engineering
layers:
- upstream
- midstream
functional_roles:
- knowledge
- component
tags:
- demohlm
- deployment
- hardware_platform
- real_world
- sensor_suite
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (136). Institution: Peking University.
    Full title: DemoHLM: From One Demonstration to Generalizable Humanoid Loco-Manipulation.'
sources:
- id: src_001
  type: website
  title: DemoHLM project page
  url: https://beingbeyond.github.io/DemoHLM/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
DemoHLM 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、全身控制器/WBC/MPC、闭环纠错/人类干预转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作 chunk 或闭环执行降低时序抖动。

## 개요
DemoHLM 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、全身控制器/WBC/MPC、闭环纠错/人类干预转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、低层控制器目标。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作 chunk 或闭环执行降低时序抖动。
