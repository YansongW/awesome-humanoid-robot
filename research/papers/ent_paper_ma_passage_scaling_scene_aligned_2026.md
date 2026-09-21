---
$id: ent_paper_ma_passage_scaling_scene_aligned_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PASSAGE: Scaling Scene-Aligned Motion Learning for Perceptive Humanoid Traversal in Cluttered Environments'
  zh: 'PASSAGE: Scaling Scene-Aligned Motion Learning for Perceptive Humanoid Traversal in Cluttered Environments'
  ko: 'PASSAGE: Scaling Scene-Aligned Motion Learning for Perceptive Humanoid Traversal in Cluttered Environments'
summary:
  en: Humanoid robots can step over, squeeze past, and duck under obstacles, but learning to select and coordinate these behaviors
    from onboard perception remains challenging. Many existing approaches rely on task-specific reinforcement-learning objectives
    or curated motion libraries, making broad behavioral coverage costly. We present PASSAGE, a perception-conditioned planner--tracker
    framework for ...
  zh: PASSAGE 是一个面向人形机器人穿越杂乱环境的感知条件化规划器—跟踪器框架，由 Yuxuan Ma、Zicheng Zeng、Chunlin Peng 等研究者提出。它利用 VR 与惯性动捕采集 1,500 个杂乱场景中 100
    小时场景对齐人体运动数据，通过条件流匹配规划器与感知全身跟踪器协同工作，无需技能标注或障碍专用策略即可组合多种穿越行为。将数据从 6 小时扩展至 100 小时后，留出场景上的平均无接触成功率由 48.1% 提升至 68.9%，最终模型达
    70.3%。
  ko: Humanoid robots can step over, squeeze past, and duck under obstacles, but learning to select and coordinate these behaviors
    from onboard perception remains challenging. Many existing approaches rely on task-specific reinforcement-learning objectives
    or curated motion libraries, making broad behavioral coverage costly. We present PASSAGE, a perception-conditioned planner--tracker
    framework for ...
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- humanoid_traversal
- perception_conditioned_planning
- whole_body_tracking
- flow_matching
- motion_capture
- onboard_perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.18732);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.18732 PASSAGE: Scaling Scene-Aligned Motion Learning for Perceptive Humanoid Traversal in Cluttered Environments'
  url: https://arxiv.org/abs/2609.18732
  date: '2026-09-16'
  accessed_at: '2026-09-21'
---

## 概述

人形机器人具备跨过、侧身挤过、低头钻过障碍的能力，但如何从机载感知中自主选择并协调这些行为仍是难题。现有方法多依赖任务专用强化学习目标或人工整理的运动库，导致行为覆盖范围扩展成本高昂。为此，作者提出 PASSAGE：一个感知条件化的规划器—跟踪器框架，用条件流匹配规划器根据运动历史、局部目标点与机器人中心多层高程图生成短时域参考轨迹，再由感知全身跟踪器以 50 Hz 结合几何反馈执行。系统引入实时分块以增强块间一致性，并在冻结跟踪器的前提下对规划器做强化学习后训练以提升闭环性能。仿真消融验证了各阶段贡献，数据规模扩展带来显著成功率提升，且整套系统可完全机载运行。

## 核心内容

### 问题背景
人形机器人需要跨越、侧身通过、低头钻过等多样化穿越行为，但从机载感知出发学习如何选择与协调这些行为仍具挑战。已有方法通常依赖任务专用的强化学习目标或精心整理的运动库，使得行为覆盖面的扩展代价高昂。

### 方法
- **数据采集**：使用虚拟现实与惯性动捕，在 1,500 个杂乱场景中采集 100 小时场景对齐的人体运动数据。
- **框架结构**：PASSAGE 为感知条件化的规划器—跟踪器框架。
  - 条件流匹配规划器：以运动历史、局部目标点、机器人中心多层高程图为输入，生成短时域参考。
  - 感知全身跟踪器：以 50 Hz 执行参考，并引入几何反馈。
- **一致性机制**：采用实时分块（real-time chunking）促进块间一致性。
- **后训练**：在冻结跟踪器的条件下，对规划器进行强化学习后训练，进一步改善闭环性能。
- **无需标注**：不需要技能标注或障碍专用策略，单一规划器—跟踪器组合即可在未见几何结构上选择并组合穿越行为。

### 实验设置与关键结果
- 仿真中进行组件消融，量化各阶段贡献。
- 在三个独立训练种子下，将采集数据从 6 小时扩展至 100 小时，留出场景上的平均无接触成功率从 48.1% 提升至 68.9%；经场景增强验证的最终模型达到 70.3%。
- 全机载系统集成第一视角 3D LiDAR 感知、在线占据建图、6.25 Hz 规划与 50 Hz 控制，运行于 Jetson AGX Orin。
- 在 50 个未见过的物理布局上测试，无需预建地图或机外计算即可完成穿越。

### 结论
PASSAGE 通过感知条件化的规划器—跟踪器设计与大规模场景对齐运动数据，实现了无需技能标注和障碍专用策略的人形机器人穿越行为选择与组合，并验证了数据规模扩展与全机载部署的可行性。

## Overview

Humanoid robots can step over, squeeze past, and duck under obstacles, but learning to select and coordinate these behaviors from onboard perception remains challenging. Many existing approaches rely on task-specific reinforcement-learning objectives or curated motion libraries, making broad behavioral coverage costly. We present PASSAGE, a perception-conditioned planner--tracker framework for humanoid traversal. Using virtual reality and inertial motion capture, we collect 100 h of scene-aligned human motion across 1,500 cluttered scenes. A conditional flow-matching planner generates short-horizon references from motion history, a local destination, and a robot-centric multi-layer elevation map, while a perceptive whole-body tracker executes them at 50 Hz with geometric feedback. Real-time chunking promotes inter-chunk consistency, and planner-side RL post-training under the frozen tracker further improves closed-loop performance. Without skill annotations or obstacle-specific policies, one planner--tracker pair selects and composes traversal behaviors across unseen geometries. In simulation, component ablations quantify the contribution of each stage. Across three independent training seeds, scaling captured data from 6 to 100 h increases mean contact-free success from 48.1% to 68.9% on held-out scenes, while the final model with validated scene augmentation reaches 70.3%. The fully onboard system integrates egocentric 3D LiDAR perception, online occupancy mapping, 6.25 Hz planning, and 50 Hz control on a Jetson AGX Orin; tests across 50 unseen physical layouts demonstrate traversal without prebuilt maps or offboard computation.

## 参考
- https://arxiv.org/abs/2609.18732
