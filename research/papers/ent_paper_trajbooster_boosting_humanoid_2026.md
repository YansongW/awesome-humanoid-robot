---
$id: ent_paper_trajbooster_boosting_humanoid_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning'
  zh: TrajBooster｜通过以轨迹为中心的学习促进人形全身操作
  ko: 'TrajBooster: Boosting Humanoid Whole-Body Manipulation via Trajectory-Centric Learning'
summary:
  en: The implementation path of TrajBooster is to first encode camera images/multi-view observations, ontology states and
    joint sequences, teleoperation/exoskeleton data into multimodal representations, and then use ACT/behavioral cloning imitation
    learning, VLA multimodal action model, IK/action redirection to predict whole-body trajectories/action sequences, and
    end effector/wrist targets. The key point is to preserve the semantic understanding of VLM while adding robot states and
    action heads to avoid staying only at language planning.
  zh: TrajBooster 的实现路径是先把相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、IK/动作重定向预测全身轨迹/动作序列、末端执行器/腕手目标。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  ko: TrajBooster 的实现路径是先把相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、IK/动作重定向预测全身轨迹/动作序列、末端执行器/腕手目标。关键点是保留
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
- trajbooster
- vision_guided_control
- visual_perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (080). Institution: Limited Teleoperation Data. Full title: TrajBooster: Boosting
    Humanoid Whole-Body Manipulation via Trajectory-Centric Learning. English name/summary machine-translated from Chinese
    by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: TrajBooster project page
  url: https://jiachengliu3.github.io/TrajBooster
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
TrajBooster 的实现路径是先把相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、IK/动作重定向预测全身轨迹/动作序列、末端执行器/腕手目标。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。

## 개요
TrajBooster 的实现路径是先把相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、IK/动作重定向预测全身轨迹/动作序列、末端执行器/腕手目标。关键点是保留 VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。

