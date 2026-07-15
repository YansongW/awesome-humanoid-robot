---
$id: ent_paper_learning_human_to_humanoid_rea_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation
  zh: 学习人对人的实时全身远程操作
  ko: Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation
summary:
  en: 'This work mainly addresses the data closed loop: using camera images/multi-view observations, ontology state and joint
    sequences, human videos/motion capture trajectories to collect human operations and robot states, and then converting
    them into trainable and reusable whole-body trajectory/action sequences and low-level controller targets through IK/action
    redirection. The key point is to put IK/action redirection in the same training/deployment chain to reduce the breakpoints
    between high-level goals and low-level actions.'
  zh: 这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、人类视频/动捕轨迹采集人类操作和机器人状态，再通过IK/动作重定向转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把IK/动作重定向放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
  ko: 这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、人类视频/动捕轨迹采集人类操作和机器人状态，再通过IK/动作重定向转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把IK/动作重定向放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
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
- balance
- behavioral_foundation_model
- locomotion
- motion_tracking
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (029). Institution: Carnegie Mellon University. Full title: Learning Human-to-Humanoid
    Real-Time Whole-Body Teleoperation. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: 学习人对人的实时全身远程操作 project page
  url: https://human2humanoid.com
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、人类视频/动捕轨迹采集人类操作和机器人状态，再通过IK/动作重定向转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把IK/动作重定向放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。

## 개요
这篇工作主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、人类视频/动捕轨迹采集人类操作和机器人状态，再通过IK/动作重定向转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是把IK/动作重定向放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。

