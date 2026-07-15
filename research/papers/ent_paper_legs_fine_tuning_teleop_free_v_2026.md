---
$id: ent_paper_legs_fine_tuning_teleop_free_v_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World'
  zh: LEGS｜微调无TeleopVLA，用于体现高斯泼溅世界中的人形移动操作
  ko: 'LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World'
summary:
  en: The implementation path of LEGS is to first encode language instructions, camera images/multi-view observations, ontology
    states and joint sequences into multimodal representations, and then use ACT/behavior cloning imitation learning, VLA
    multimodal action model, world model/video prediction to predict low-level controller targets, and terrain/scene representations.
    The key point is to let the video/world model provide predictable physical priors, and then the action head turns the
    semantic goal into continuous control.
  zh: LEGS 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、世界模型/视频预测预测低层控制器目标、地形/场景表征。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。
  ko: LEGS 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、世界模型/视频预测预测低层控制器目标、地形/场景表征。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- general_manipulation
- legs
- vision_language_action
- vla
- world_model
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (151). Institution: Stanford University. Full title: LEGS: Fine-Tuning Teleop-Free
    VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World. English name/summary machine-translated from
    Chinese by scripts/backfill_en_translations.py.'
sources:
- id: src_001
  type: website
  title: LEGS project page
  url: https://legsvla.github.io/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## 概述
LEGS 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、世界模型/视频预测预测低层控制器目标、地形/场景表征。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。

## 개요
LEGS 的实现路径是先把语言指令、相机图像/多视角观测、本体状态与关节序列编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、世界模型/视频预测预测低层控制器目标、地形/场景表征。关键点是让视频/世界模型提供可预测的物理先验，再由动作头把语义目标变成连续控制。

