---
$id: ent_paper_falcon_learning_force_adaptive_2025_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation'
  zh: FALCON｜学习力自适应人形移动操作
  ko: 'FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation'
summary:
  en: 'Falcon primarily addresses data closed-loop: capturing human operations and robot states with ontology states and joint
    sequences, human video/dynamic capture trajectories, teleoperation/exoskeleton data, and data capture, then through the
    whole body controller/WBC/Mpc into a trainable and reusable joint position/Torque Command, End-effector/wrist-hand target.
    The key is to put the Full-body Controller/WBC/MPC in the same training/deployment link, reducing the discontinuity between
    high-level goals and low-level actions.'
  zh: FALCON 主要解决数据闭环：用本体状态与关节序列、人类视频/动捕轨迹、遥操作/外骨骼数据采集人类操作和机器人状态，再通过全身控制器/WBC/MPC转成可训练、可复用的关节位置/力矩命令、末端执行器/腕手目标。关键点是把全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
  ko: FALCON 主要解决数据闭环：用本体状态与关节序列、人类视频/动捕轨迹、遥操作/外骨骼数据采集人类操作和机器人状态，再通过全身控制器/WBC/MPC转成可训练、可复用的关节位置/力矩命令、末端执行器/腕手目标。关键点是把全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- falcon
- human_video
- interaction_planning
- motion_capture
- motion_retargeting
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (109). Institution: Carnegie Mellon University. Full title: FALCON: Learning Force-Adaptive
    Humanoid Loco-Manipulation. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
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
FALCON 主要解决数据闭环：用本体状态与关节序列、人类视频/动捕轨迹、遥操作/外骨骼数据采集人类操作和机器人状态，再通过全身控制器/WBC/MPC转成可训练、可复用的关节位置/力矩命令、末端执行器/腕手目标。关键点是把全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。

## 개요
FALCON 主要解决数据闭环：用本体状态与关节序列、人类视频/动捕轨迹、遥操作/外骨骼数据采集人类操作和机器人状态，再通过全身控制器/WBC/MPC转成可训练、可复用的关节位置/力矩命令、末端执行器/腕手目标。关键点是把全身控制器/WBC/MPC放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。

