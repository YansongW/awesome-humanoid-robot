---
$id: ent_paper_open_television_teleoperation_2024_2
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Open-TeleVision: Teleoperation with Immersive Active Visual Feedback'
  zh: 学习人对人的实时全身远程操作。
  ko: 'Open-TeleVision: Teleoperation with Immersive Active Visual Feedback'
summary:
  en: 'This work mainly addresses data closed loops: acquisition of human operation and robot states with camera images/multi-view
    observations, proprioceptive states and joint sequences, teleoperation/exoskeleton data, and joint sequences, then through
    Act/behavior clone imitation learning, diffusion strategy/flow matching, MM-DiT/Transformer action head to trainable,
    reusable joint position/torque commands, whole body trajectory/action sequence, end-effector/wrist-hand target. The key
    point is to treat action generation as a conditional generation problem, and use diffusion or flow matching to sample
    executable trajectories in multimodal action distributions.'
  zh: 这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配、MM-DiT/Transformer 动作头转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、末端执行器/腕手目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: 这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配、MM-DiT/Transformer 动作头转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、末端执行器/腕手目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
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
- deployment
- hardware_platform
- real_world
- sensor_suite
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (144). Institution: UC San Diego1、MIT2、San Diego、and GR- operator are at San Diego
    (approximately miles away). j: interactions with humans. Full title: Open-TeleVision: Teleoperation with Immersive Active
    Visual Feedback. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: 学习人对人的实时全身远程操作。 project page
  url: https://robot-tv.github.io/
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配、MM-DiT/Transformer 动作头转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、末端执行器/腕手目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

## 개요
这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配、MM-DiT/Transformer 动作头转成可训练、可复用的关节位置/力矩命令、全身轨迹/动作序列、末端执行器/腕手目标。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

