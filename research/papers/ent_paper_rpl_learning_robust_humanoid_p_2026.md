---
$id: ent_paper_rpl_learning_robust_humanoid_p_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RPL: Learning Robust Humanoid Perceptive Locomotion on Challenging Terrains'
  zh: RPL｜在具有挑战性的地形上学习鲁棒的人形感知运动
  ko: 'RPL: Learning Robust Humanoid Perceptive Locomotion on Challenging Terrains'
summary:
  en: ''
  zh: RPL 先从相机图像/多视角观测、本体状态与关节序列、深度/点云/高度图恢复场景、目标或运动表征，再用下视深度相机和 U-Net 高度图重建、教师-学生知识迁移、世界模型/视频预测生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把地形重建、步态相位和全身姿态放进同一个控制回路，而不是把感知和运控拆成松散串联。
  ko: RPL 先从相机图像/多视角观测、本体状态与关节序列、深度/点云/高度图恢复场景、目标或运动表征，再用下视深度相机和 U-Net 高度图重建、教师-学生知识迁移、世界模型/视频预测生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把地形重建、步态相位和全身姿态放进同一个控制回路，而不是把感知和运控拆成松散串联。
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
- rpl
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (044). Institution: Carnegie Mellon University、Stanford
    University、UC Berkeley. Full title: RPL: Learning Robust Humanoid Perceptive Locomotion
    on Challenging Terrains.'
sources:
- id: src_001
  type: website
  title: RPL project page
  url: https://rpl-humanoid.github.io/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
RPL 先从相机图像/多视角观测、本体状态与关节序列、深度/点云/高度图恢复场景、目标或运动表征，再用下视深度相机和 U-Net 高度图重建、教师-学生知识迁移、世界模型/视频预测生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把地形重建、步态相位和全身姿态放进同一个控制回路，而不是把感知和运控拆成松散串联。

## 개요
RPL 先从相机图像/多视角观测、本体状态与关节序列、深度/点云/高度图恢复场景、目标或运动表征，再用下视深度相机和 U-Net 高度图重建、教师-学生知识迁移、世界模型/视频预测生成全身轨迹/动作序列、低层控制器目标、地形/场景表征。关键点是把地形重建、步态相位和全身姿态放进同一个控制回路，而不是把感知和运控拆成松散串联。
