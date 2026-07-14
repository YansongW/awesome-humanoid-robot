---
$id: ent_paper_wholebodyvla_towards_unified_l_2025_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control'
  zh: WholeBodyVLA｜迈向全身移动操作的统一潜在VLA
  ko: 'WholeBodyVLA: Towards Unified Latent VLA for Whole-Body Loco-Manipulation Control'
summary:
  en: ''
  zh: WholeBodyVLA 的实现路径是先把相机图像/多视角观测、遥操作/外骨骼数据编码成多模态表征，再用VLA 多模态动作模型预测全身轨迹/动作序列。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  ko: WholeBodyVLA 的实现路径是先把相机图像/多视角观测、遥操作/外骨骼数据编码成多模态表征，再用VLA 多模态动作模型预测全身轨迹/动作序列。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
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
- vision_guided_control
- visual_perception
- wholebodyvla
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (083). Institution: Fudan University、OpenDriveLab
    & MMLab at The University of Hong Kong. Full title: WholeBodyVLA: Towards Unified
    Latent VLA for Whole-Body Loco-Manipulation Control.'
sources:
- id: src_001
  type: website
  title: WholeBodyVLA project page
  url: https://opendrivelab.com/WholeBodyVLA
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
WholeBodyVLA 的实现路径是先把相机图像/多视角观测、遥操作/外骨骼数据编码成多模态表征，再用VLA 多模态动作模型预测全身轨迹/动作序列。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。

## 개요
WholeBodyVLA 的实现路径是先把相机图像/多视角观测、遥操作/外骨骼数据编码成多模态表征，再用VLA 多模态动作模型预测全身轨迹/动作序列。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
