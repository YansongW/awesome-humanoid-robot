---
$id: ent_paper_omnidp_beyond_fov_large_worksp_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniDP: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception'
  zh: OmniDP｜具有全方位3D感知的超视场大工作空间人形操控
  ko: 'OmniDP: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception'
summary:
  en: The deployment of humanoid robots for dexterous manipulation in unstructured environments remains challenging due to
    perceptual limitations that constrain the effective workspace. In scenarios where physical constraints prevent the robot
    from repositioning itself, maintaining omnidirectional awareness becomes far more critical than color or semantic information.While
    recent advances in visuomotor policy learning have improved manipulation capabilities, conventional RGB-D solutions suffer
    from narrow fields of view (FOV) and self-occlusion, requiring frequent base movements that introduce motion uncertainty
    and safety risks. Existing approaches to expanding perception, including active vision systems and third-view cameras,
    introduce mechanical complexity, calibration dependencies, and late
  zh: OmniDP 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过策略网络和控制模块转成可训练、可复用的可执行动作命令。关键点是把策略网络和控制模块放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
  ko: OmniDP 主要解决数据闭环：用相机图像/多视角观测、本体状态与关节序列、遥操作/外骨骼数据采集人类操作和机器人状态，再通过策略网络和控制模块转成可训练、可复用的可执行动作命令。关键点是把策略网络和控制模块放在同一条训练/部署链路里，减少高层目标到低层动作之间的断点。
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
- omnidp
- scene_understanding
- vision_guided_control
- visual_perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: OmniDP: Beyond-FOV Large-Workspace
    Humanoid Manipulation with Omnidirectional 3D Perception.'
sources:
- id: src_001
  type: website
  title: 'OmniDP: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception'
  url: ''
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
The deployment of humanoid robots for dexterous manipulation in unstructured environments remains challenging due to perceptual limitations that constrain the effective workspace. In scenarios where physical constraints prevent the robot from repositioning itself, maintaining omnidirectional awareness becomes far more critical than color or semantic information.While recent advances in visuomotor policy learning have improved manipulation capabilities, conventional RGB-D solutions suffer from narrow fields of view (FOV) and self-occlusion, requiring frequent base movements that introduce motion uncertainty and safety risks. Existing approaches to expanding perception, including active vision systems and third-view cameras, introduce mechanical complexity, calibration dependencies, and latency that hinder reliable real-time performance. In this work, We propose OmniDP, an end-to-end LiDAR-driven 3D visuomotor policy that enables robust manipulation in large workspaces. Our method processes panoramic point clouds through a Time-Aware Attention Pooling mechanism, efficiently encoding sparse 3D data while capturing temporal dependencies. This 360{\deg} perception allows the robot to interact with objects across wide areas without frequent repositioning. To support policy learning, we develop a whole-body teleoperation system for efficient data collection on full-body coordination. Extensive experiments in simulation and real-world environments show that OmniDP achieves robust performance in large-workspace and cluttered scenarios, outperforming baselines that rely on egocentric depth cameras.

## 核心内容
The deployment of humanoid robots for dexterous manipulation in unstructured environments remains challenging due to perceptual limitations that constrain the effective workspace. In scenarios where physical constraints prevent the robot from repositioning itself, maintaining omnidirectional awareness becomes far more critical than color or semantic information.While recent advances in visuomotor policy learning have improved manipulation capabilities, conventional RGB-D solutions suffer from narrow fields of view (FOV) and self-occlusion, requiring frequent base movements that introduce motion uncertainty and safety risks. Existing approaches to expanding perception, including active vision systems and third-view cameras, introduce mechanical complexity, calibration dependencies, and latency that hinder reliable real-time performance. In this work, We propose OmniDP, an end-to-end LiDAR-driven 3D visuomotor policy that enables robust manipulation in large workspaces. Our method processes panoramic point clouds through a Time-Aware Attention Pooling mechanism, efficiently encoding sparse 3D data while capturing temporal dependencies. This 360{\deg} perception allows the robot to interact with objects across wide areas without frequent repositioning. To support policy learning, we develop a whole-body teleoperation system for efficient data collection on full-body coordination. Extensive experiments in simulation and real-world environments show that OmniDP achieves robust performance in large-workspace and cluttered scenarios, outperforming baselines that rely on egocentric depth cameras.

## 参考
- Semantic Scholar search: OmniDP: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception

