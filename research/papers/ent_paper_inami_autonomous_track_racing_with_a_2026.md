---
$id: ent_paper_inami_autonomous_track_racing_with_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Autonomous Track Racing with a Commercially Available Humanoid: System Design and Real-World Deployment'
  zh: 'Autonomous Track Racing with a Commercially Available Humanoid: System Design and Real-World Deployment'
  ko: 'Autonomous Track Racing with a Commercially Available Humanoid: System Design and Real-World Deployment'
summary:
  en: Learning-based methods now let humanoids run robustly, and they have begun to compete in athletic events. Yet few reports
    describe a complete autonomous humanoid running system in an actual race, where the robot must follow a lane at a new
    venue, pace itself within hardware limits, and finish without intervention. We report such a system deployed on the Unitree
    G1, a commercially available ...
  zh: 本文报告了一套部署在商用通用人形机器人 Unitree G1 上的完整自主跑步系统，并在 World Humanoid Robot Games 2026 的 100 m、400 m 和 1500 m 项目中实际参赛。系统集成了基于视觉的车道感知、路径跟踪，以及以人类运动先验通过强化学习训练得到的跑步策略。核心工程贡献包括稳定头部相机图像、利用
    IMU 辅助腿部里程计跨越腾空相，以及通过训练中惩罚髋关节俯仰力矩、加装散热板和基于温度的限速与分项配速来应对电机发热。
  ko: Learning-based methods now let humanoids run robustly, and they have begun to compete in athletic events. Yet few reports
    describe a complete autonomous humanoid running system in an actual race, where the robot must follow a lane at a new
    venue, pace itself within hardware limits, and finish without intervention. We report such a system deployed on the Unitree
    G1, a commercially available ...
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
- humanoid_running
- autonomous_racing
- reinforcement_learning
- lane_perception
- thermal_management
- real_world_deployment
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.22445);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.22445 Autonomous Track Racing with a Commercially Available Humanoid: System Design and Real-World Deployment'
  url: https://arxiv.org/abs/2611.22445
  date: '2026-11-17'
  accessed_at: '2026-11-23'
---

## 概述

该工作面向真实赛道中的自主人形跑步任务，要求机器人在陌生场地沿车道行进、在硬件限制内控制配速并全程无人工干预完成比赛。作者在商用通用人形机器人 Unitree G1 上构建了完整系统，融合视觉车道感知、路径跟踪与基于强化学习并引入人类运动先验的跑步策略。为应对人形跑步的固有难点，系统对身体运动引起的头部相机图像抖动进行稳定处理，并用 IMU 辅助的腿部里程计衔接腾空阶段。针对电机发热问题，训练阶段对髋关节俯仰力矩施加惩罚，硬件上加装散热板，运行时采用基于温度的限速与按项目定制的配速策略。机器人最终在 100 m 中位列 74 支队伍第 13 名，400 m 首轮在 44 支队伍中排第 10、半决赛摔倒，1500 m 在 35 支队伍中获第七。作者指出热余量在全部项目中决定了配速，而半决赛摔倒源于一次车道检测错误。

## 核心内容

### 问题背景

基于学习的方法已使人形机器人具备稳健的跑步能力，并开始参与竞技赛事，但关于完整自主人形跑步系统在真实比赛中部署的公开报道仍然很少。真实赛道带来的额外挑战包括：在新场地沿车道行进、在硬件限制内自行控制配速，以及全程无人工干预完成比赛。

### 系统与方法

作者在 Unitree G1 这一商用通用人形机器人上构建并部署了自主跑步系统，参加 World Humanoid Robot Games 2026 的 100 m、400 m 与 1500 m 项目。系统主要包含三部分：

- **视觉车道感知**：用于在新场地中识别并跟随跑道车道。
- **路径跟踪**：依据感知结果控制机器人沿车道行进。
- **跑步策略**：通过强化学习训练，并引入人类运动先验。

针对人形跑步的具体难点，系统采用了两项感知与状态估计上的处理：

- 对身体运动造成的头部相机图像抖动进行稳定化，以支撑车道感知。
- 使用 IMU 辅助的腿部里程计，在腾空阶段之间提供连续的状态估计。

针对电机发热问题，作者从训练、硬件与运行时三个层面处理：

- 训练阶段对髋关节俯仰力矩施加惩罚，以降低发热相关负载。
- 硬件上加装散热板。
- 运行时采用基于温度的限速，并按不同项目设置配速策略。

### 实验结果

- 100 m：在 74 支队伍中位列第 13。
- 400 m：首轮在 44 支队伍中排第 10，半决赛中摔倒。
- 1500 m：在 35 支队伍中位列第七。

### 结论

作者总结称，在此次部署中热余量在每一个项目里都决定了配速；而 400 m 半决赛的摔倒发生在一次车道检测错误之后。

## Overview

Learning-based methods now let humanoids run robustly, and they have begun to compete in athletic events. Yet few reports describe a complete autonomous humanoid running system in an actual race, where the robot must follow a lane at a new venue, pace itself within hardware limits, and finish without intervention. We report such a system deployed on the Unitree G1, a commercially available general-purpose humanoid, in the 100 m, 400 m, and 1500 m events of the World Humanoid Robot Games 2026. The system integrates vision-based lane perception, path tracking, and a running policy trained by reinforcement learning with a human motion prior. To address the challenges of humanoid running, we stabilize head-camera images against body motion and use IMU-assisted leg odometry to bridge flight phases. To manage motor heating, we penalize hip-pitch torque during training, add heat-dissipation plates, and apply temperature-based speed limiting with event-specific pacing. The robot placed 13th of 74 in the 100 m, 10th of 44 in the 400 m first round before falling in the semifinal, and seventh of 35 in the 1500 m. In this deployment, thermal margin set the pace in every event, and the semifinal fall followed a lane-detection error.

## 参考
- https://arxiv.org/abs/2611.22445
