---
$id: ent_paper_gallant_voxel_grid_based_human_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Gallant: Voxel Grid-based Humanoid Locomotion and Local-navigation across 3D
    Constrained Terrains'
  zh: Gallant｜跨3D约束地形的基于体素网格的人形运动和本地导航
  ko: ''
summary:
  en: ''
  zh: Gallant 先从相机图像/多视角观测、本体状态与关节序列、深度/点云/高度图恢复场景、目标或运动表征，再用策略网络和控制模块生成地形/场景表征、导航/到达目标。关键点是把策略网络和控制模块放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
  ko: ''
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
- gallant
- hardware_platform
- real_world
- sensor_suite
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (137). Institution: Shanghai Artificial
    Intelligence Laboratory、The Chinese University of Hong Kong、University of Science
    and Technology of China、University of Tokyo. Full title: Gallant: Voxel Grid-based
    Humanoid Locomotion and Local-navigation across 3D Constrained Terrains.'
sources:
- id: src_001
  type: website
  title: Gallant project page
  url: https://gallantloco.github.io/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


Gallant 先从相机图像/多视角观测、本体状态与关节序列、深度/点云/高度图恢复场景、目标或运动表征，再用策略网络和控制模块生成地形/场景表征、导航/到达目标。关键点是把策略网络和控制模块放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
