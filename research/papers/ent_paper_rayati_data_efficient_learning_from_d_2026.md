---
$id: ent_paper_rayati_data_efficient_learning_from_d_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Data-Efficient Learning from Demonstration for Humanoid Robots via Feature-Level Perception and Prompt-Based Object
    Detection
  zh: Data-Efficient Learning from Demonstration for Humanoid Robots via Feature-Level Perception and Prompt-Based Object
    Detection
  ko: Data-Efficient Learning from Demonstration for Humanoid Robots via Feature-Level Perception and Prompt-Based Object
    Detection
summary:
  en: Learning from Demonstration (LfD) allows robots to learn new skills from human examples; however, many vision-based
    methods require large datasets and resource-intensive end-to-end training. This paper introduces a data-efficient LfD
    framework for humanoid robots that learns manipulation skills from compact, task-specific features instead of raw images.
    The proposed approach integrates layered ...
  zh: 本文提出一种面向人形机器人的数据高效学习示范（LfD）框架，由 Keyhan Rayati 等人完成。该方法不直接使用原始图像，而是从示范视频中提取紧凑的任务相关特征来学习操作技能，并在 NAO 人形机器人上实现与验证。仿真中仅用
    16 次示范即在抓取放置任务上达到 78% 成功率，用 100 次示范提升至 86%；用 8 次示范在推动任务上达到 71% 成功率。
  ko: Learning from Demonstration (LfD) allows robots to learn new skills from human examples; however, many vision-based
    methods require large datasets and resource-intensive end-to-end training. This paper introduces a data-efficient LfD
    framework for humanoid robots that learns manipulation skills from compact, task-specific features instead of raw images.
    The proposed approach integrates layered ...
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
- learning_from_demonstration
- humanoid_robots
- data_efficient_learning
- object_detection
- motion_features
- nao_robot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.26170);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.26170 Data-Efficient Learning from Demonstration for Humanoid Robots via Feature-Level Perception and
    Prompt-Based Object Detection
  url: https://arxiv.org/abs/2610.26170
  date: '2026-10-19'
  accessed_at: '2026-10-26'
---

## 概述

该研究针对基于视觉的 LfD 方法通常依赖大规模数据集和资源消耗大的端到端训练这一问题，提出了一种数据高效的替代方案：让机器人从紧凑的任务特定特征而非原始图像中学习操作技能。框架融合了分层视觉预处理、基于 Kinect 的人体关节估计、基于提示的目标检测与深度信息，从示范视频中提取人体运动特征和物体的三维位置。这些特征被用于训练一个时序深度学习模型，以预测机器人关节角轨迹并执行。框架在 NAO 人形机器人上实现，在仿真中进行了定量评估，并在实体硬件上进行了演示。仿真结果显示，抓取放置任务仅用 16 次示范即可达到 78% 成功率，使用 100 次示范时提升至 86%；推动任务用 8 次示范达到 71% 成功率，体现了其在数据高效的人形机器人技能获取方面的有效性。

## 核心内容

### 问题背景
Learning from Demonstration（LfD）使机器人能够从人类示例中学习新技能，但许多基于视觉的方法需要大规模数据集，且端到端训练资源开销大，不利于在数据有限条件下快速获取技能。

### 方法
- **特征提取流程**：整合分层视觉预处理、基于 Kinect 的人体关节估计、基于提示的目标检测以及深度信息，从示范视频中提取人体运动特征与物体的三维位置。
- **学习与执行**：以提取到的紧凑任务特定特征为输入，训练时序深度学习模型，预测机器人关节角轨迹供执行使用。
- **核心思路**：不直接使用原始图像，而是依赖任务相关特征，从而降低对数据量和训练资源的需求。

### 实验设置
- 框架在 NAO 人形机器人上实现。
- 在仿真环境中进行定量评估，并在实体硬件上进行演示。

### 关键结果
- 抓取放置任务：仅使用 16 次示范，仿真成功率为 78%；使用 100 次示范时提升至 86%。
- 推动任务：使用 8 次示范，成功率为 71%。

### 结论
结果表明，该框架能够以少量示范实现有效的人形机器人操作技能获取，验证了特征级感知与基于提示的目标检测在数据高效 LfD 中的可行性。

## Overview

Learning from Demonstration (LfD) allows robots to learn new skills from human examples; however, many vision-based methods require large datasets and resource-intensive end-to-end training. This paper introduces a data-efficient LfD framework for humanoid robots that learns manipulation skills from compact, task-specific features instead of raw images. The proposed approach integrates layered visual preprocessing, Kinect-based human joint estimation, prompt-based object detection, and depth information to extract human motion features and three-dimensional object locations from demonstration videos. These features are used to train a temporal deep learning model that predicts robot joint-angle trajectories for execution. The framework is implemented on a NAO humanoid robot, evaluated quantitatively in simulation, and demonstrated on physical hardware. In simulation, the robot achieves a 78% success rate on a pick-and-place task using only 16 demonstrations, which increases to 86% when trained with 100 demonstrations. The framework also achieves a 71% success rate on a pushing task using eight demonstrations, highlighting its effectiveness for data-efficient humanoid skill acquisition.

## 参考
- https://arxiv.org/abs/2610.26170
