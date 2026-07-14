---
$id: ent_paper_gait_adaptive_perceptive_human_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Gait-Adaptive Perceptive Humanoid Locomotion with Real-Time Under-Base Terrain
    Reconstruction
  zh: 具有实时基础地形重建的步态自适应感知人形运动
  ko: Gait-Adaptive Perceptive Humanoid Locomotion with Real-Time Under-Base Terrain
    Reconstruction
summary:
  en: ''
  zh: 这篇工作先从相机图像/多视角观测、本体状态与关节序列、深度/点云/高度图恢复场景、目标或运动表征，再用下视深度相机和 U-Net 高度图重建、步态相位/频率调节、教师-学生知识迁移生成关节位置/力矩命令、地形/场景表征。关键点是把地形重建、步态相位和全身姿态放进同一个控制回路，而不是把感知和运控拆成松散串联。
  ko: 这篇工作先从相机图像/多视角观测、本体状态与关节序列、深度/点云/高度图恢复场景、目标或运动表征，再用下视深度相机和 U-Net 高度图重建、步态相位/频率调节、教师-学生知识迁移生成关节位置/力矩命令、地形/场景表征。关键点是把地形重建、步态相位和全身姿态放进同一个控制回路，而不是把感知和运控拆成松散串联。
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
  notes: 'Imported from WeChat curated list (142). Institution: . Full title: Gait-Adaptive
    Perceptive Humanoid Locomotion with Real-Time Under-Base Terrain Reconstruction.'
sources:
- id: src_001
  type: website
  title: 具有实时基础地形重建的步态自适应感知人形运动 project page
  url: https://ga-phl.github.io/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
这篇工作先从相机图像/多视角观测、本体状态与关节序列、深度/点云/高度图恢复场景、目标或运动表征，再用下视深度相机和 U-Net 高度图重建、步态相位/频率调节、教师-学生知识迁移生成关节位置/力矩命令、地形/场景表征。关键点是把地形重建、步态相位和全身姿态放进同一个控制回路，而不是把感知和运控拆成松散串联。

## 개요
这篇工作先从相机图像/多视角观测、本体状态与关节序列、深度/点云/高度图恢复场景、目标或运动表征，再用下视深度相机和 U-Net 高度图重建、步态相位/频率调节、教师-学生知识迁移生成关节位置/力矩命令、地形/场景表征。关键点是把地形重建、步态相位和全身姿态放进同一个控制回路，而不是把感知和运控拆成松散串联。
