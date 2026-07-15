---
$id: ent_paper_opening_the_sim_to_real_door_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer
  zh: 打开仿真到现实世界的人形像素到动作策略传输之门
  ko: Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer
summary:
  en: 'This work mainly addresses data closed loops: acquisition of human operation and robotic states with camera images/multi-view
    observations, proprioceptive states and joint sequences, teleoperation/exoskeleton data, and joint sequences, then through
    teacher-student knowledge transfer, whole-body Controller/WBC/Mpc, closed-loop error correction/human intervention into
    trainable and reusable whole-body trajectories/action sequences, low-level controller goals. The key is to train the teacher''s
    strategy with privileged information and distill the ability to use only the student''s strategy of deploying observations.'
  zh: 这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过教师-学生知识迁移、全身控制器/WBC/MPC、闭环纠错/人类干预转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
  ko: 这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过教师-学生知识迁移、全身控制器/WBC/MPC、闭环纠错/人类干预转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
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
- manipulation_interface
- mobile_manipulation
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (053). Institution: NVIDIA、UC Berkeley、CMU. Full title: Opening the Sim-to-Real
    Door for Humanoid Pixel-to-Action Policy Transfer. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: 打开仿真到现实世界的人形像素到动作策略传输之门 project page
  url: https://doorman-humanoid.github.io/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过教师-学生知识迁移、全身控制器/WBC/MPC、闭环纠错/人类干预转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。

## 개요
这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过教师-学生知识迁移、全身控制器/WBC/MPC、闭环纠错/人类干预转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。

