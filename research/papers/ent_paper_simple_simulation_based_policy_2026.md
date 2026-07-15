---
$id: ent_paper_simple_simulation_based_policy_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation'
  zh: SIMPLE｜基于仿真的人形移动操作策略学习和评估
  ko: 'SIMPLE: Simulation-Based Policy Learning and Evaluation for Humanoid Loco-manipulation'
summary:
  en: The implementation path of SIMPLE is to first encode camera images/multi-view observations, ontology state and joint
    sequences, teleoperation/exoskeleton data into multimodal representations, and then use VLA multimodal action model and
    world model/video prediction to predict the whole-body trajectory/action sequence. The key point is to let the video/world
    model provide predictable physical priors, and then the action head turns the semantic goal into continuous control.
  zh: SIMPLE 的实现路径是先把相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据编码成多模态表征，再用VLA 多模态动作模型、世界模型/视频预测预测全身轨迹/动作序列。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。
  ko: SIMPLE 的实现路径是先把相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据编码成多模态表征，再用VLA 多模态动作模型、世界模型/视频预测预测全身轨迹/动作序列。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。
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
- simple
- vision_guided_control
- visual_perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (075). Institution: . Full title: SIMPLE: Simulation-Based Policy Learning and
    Evaluation for Humanoid Loco-manipulation. English name/summary machine-translated from Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: SIMPLE project page
  url: https://psi-lab.ai/SIMPLE
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
SIMPLE 的实现路径是先把相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据编码成多模态表征，再用VLA 多模态动作模型、世界模型/视频预测预测全身轨迹/动作序列。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。

## 개요
SIMPLE 的实现路径是先把相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据编码成多模态表征，再用VLA 多模态动作模型、世界模型/视频预测预测全身轨迹/动作序列。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。

