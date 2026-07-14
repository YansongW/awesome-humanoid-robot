---
$id: ent_paper_twist2_scalable_portable_and_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System'
  zh: TWIST2｜可扩展、便携式、整体的人形数据收集系统
  ko: 'TWIST2: Scalable, Portable, and Holistic Humanoid Data Collection System'
summary:
  en: ''
  zh: TWIST2 的实现路径是先把相机图像/多视角观测、人类视频/动捕轨迹、遥操作/外骨骼数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、全身控制器/WBC/MPC预测全身轨迹/动作序列、低层控制器目标。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  ko: TWIST2 的实现路径是先把相机图像/多视角观测、人类视频/动捕轨迹、遥操作/外骨骼数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、全身控制器/WBC/MPC预测全身轨迹/动作序列、低层控制器目标。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
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
- twist2
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (020). Institution: Stanford University、UC
    Berkeley、CMU. Full title: TWIST2: Scalable, Portable, and Holistic Humanoid Data
    Collection System.'
sources:
- id: src_001
  type: website
  title: TWIST2 project page
  url: https://twist-data.github.io
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
TWIST2 的实现路径是先把相机图像/多视角观测、人类视频/动捕轨迹、遥操作/外骨骼数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、全身控制器/WBC/MPC预测全身轨迹/动作序列、低层控制器目标。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。

## 개요
TWIST2 的实现路径是先把相机图像/多视角观测、人类视频/动捕轨迹、遥操作/外骨骼数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、全身控制器/WBC/MPC预测全身轨迹/动作序列、低层控制器目标。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
