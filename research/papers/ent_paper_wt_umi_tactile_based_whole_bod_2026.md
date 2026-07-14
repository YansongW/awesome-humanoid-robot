---
$id: ent_paper_wt_umi_tactile_based_whole_bod_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware
    Planning'
  zh: WT-UMI｜通过力监督接触感知规划进行基于触觉的全身操作
  ko: 'WT-UMI: Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware
    Planning'
summary:
  en: ''
  zh: WT-UMI 主要解决数据闭环：用相机图像/多视角观测、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配转成可训练、可复用的全身轨迹/动作序列、末端执行器/腕手目标、动作
    chunk/token。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
  ko: WT-UMI 主要解决数据闭环：用相机图像/多视角观测、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配转成可训练、可复用的全身轨迹/动作序列、末端执行器/腕手目标、动作
    chunk/token。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 09_data_datasets
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- data_collection
- dataset
- human_demonstration
- teleoperation
- wt_umi
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (134). Institution: . Full title: WT-UMI:
    Tactile-based Whole-Body Manipulation via Force-Supervised Contact-Aware Planning.'
sources:
- id: src_001
  type: website
  title: WT-UMI project page
  url: https://wt-umi.github.io/WTUMI/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## 概述
WT-UMI 主要解决数据闭环：用相机图像/多视角观测、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配转成可训练、可复用的全身轨迹/动作序列、末端执行器/腕手目标、动作 chunk/token。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。

## 개요
WT-UMI 主要解决数据闭环：用相机图像/多视角观测、遥操作/外骨骼数据、接触力/触觉信号采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配转成可训练、可复用的全身轨迹/动作序列、末端执行器/腕手目标、动作 chunk/token。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
