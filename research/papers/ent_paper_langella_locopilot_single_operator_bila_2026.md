---
$id: ent_paper_langella_locopilot_single_operator_bila_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LocoPilot: Single-Operator Bilateral Teleoperation for Loco-Manipulation Policy Learning'
  zh: 'LocoPilot: Single-Operator Bilateral Teleoperation for Loco-Manipulation Policy Learning'
  ko: 'LocoPilot: Single-Operator Bilateral Teleoperation for Loco-Manipulation Policy Learning'
summary:
  en: Learning loco-manipulation policies requires demonstrations that capture coordinated base and arm motion on the target
    embodiment. Robot-free interfaces allow demonstrations to be collected independently of the target robot, increasing flexibility
    but without directly capturing platform-specific commands, proprioception, and body-mounted observations. On-robot teleoperation
    allows to capture ...
  zh: LocoPilot 是面向腿足式机器人 loco-manipulation 策略学习的单操作员双边遥操作与数据采集框架，由 Antonio Langella 等来自 IIT-DLSLab 的研究者实现于一台 12-DoF Unitree
    Go2 四足机器人上，该机器人搭载 6-DoF AgileX Piper L 机械臂、Intel RealSense D435 腕部相机与 D405 头部相机。系统以第二台 6-DoF Piper L 作为主端机械臂，配合两个手持控制器同时控制底盘、身体姿态、机械臂与夹爪，并在无专用力/力矩传感器条件下估计从端交互力，经无源性约束的触觉通道反馈给操作员。其核心贡献在于统一了机器人闭环的腿足数据采集、无需动作捕捉设备的力反馈，以及遥操作与策略部署共享的同一
    11D 动作接口。
  ko: Learning loco-manipulation policies requires demonstrations that capture coordinated base and arm motion on the target
    embodiment. Robot-free interfaces allow demonstrations to be collected independently of the target robot, increasing flexibility
    but without directly capturing platform-specific commands, proprioception, and body-mounted observations. On-robot teleoperation
    allows to capture ...
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
- bilateral_teleoperation
- loco_manipulation
- legged_robots
- data_collection
- haptic_feedback
- policy_learning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.27998);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.27998 LocoPilot: Single-Operator Bilateral Teleoperation for Loco-Manipulation Policy Learning'
  url: https://arxiv.org/abs/2610.27998
  date: '2026-10-20'
  accessed_at: '2026-10-26'
---

## 概述

LocoPilot 针对的是 loco-manipulation 策略学习中演示数据难以同时覆盖底盘与手臂协同运动的问题：无机器人接口虽灵活，却无法直接记录平台相关指令、本体感知与机体安装观测；而机器人端遥操作能采集这些信号，但需要能并发指挥整个系统的接口。为此作者构建了单操作员双边遥操作与数据采集框架，硬件为 12-DoF Unitree Go2 四足平台，搭载 6-DoF AgileX Piper L 机械臂、Intel RealSense D435 腕部相机与 D405 头部相机，并以第二台 6-DoF Piper L 作为主端、两个手持控制器实现底盘、身体姿态、机械臂与夹爪的同步控制。系统在没有专用力/力矩传感器的情况下估计从端机械臂交互力，并通过无源性约束的触觉通道呈现给操作员。ROS 2 流水线同步记录多模态观测，并输出遥操作与策略部署共用的统一 11D 动作。作者在多个 loco-manipulation 任务上评估该接口，并通过在抓放演示上微调 MolmoAct2、在实体机器人上部署且不做动作重定向或额外逆运动学，验证了从采集到部署的完整流程。

## 核心内容

### 问题背景

学习 loco-manipulation 策略需要能在目标本体上同时体现底盘与手臂协同运动的演示数据。现有两条路径各有局限：无机器人接口可在与目标机器人无关的条件下采集演示，灵活性更高，但无法直接捕获平台相关指令、本体感知与机体安装观测；机器人端遥操作能够直接记录这些信号，但要求接口具备并发指挥整个系统的能力。

### 方法

作者提出 LocoPilot，一个单操作员双边遥操作与数据采集框架，其硬件构成如下：

- 从端平台：12-DoF Unitree Go2 四足机器人，搭载 6-DoF AgileX Piper L 机械臂、Intel RealSense D435 腕部相机与 Intel RealSense D405 头部相机。
- 主端设备：第二台 6-DoF Piper L 机械臂作为主端，另配两个手持控制器，用于同时控制底盘、身体姿态、机械臂与夹爪。
- 力反馈：从端机械臂的交互力在没有专用力/力矩传感器的条件下被估计，并通过无源性约束的触觉通道呈现给操作员。
- 数据流水线：基于 ROS 2 的流水线同步记录多模态观测，并输出遥操作与策略部署共享的统一 11D 动作。

与已有工作相比，LocoPilot 的特点在于将机器人闭环的腿足数据采集、无需动作捕捉仪器的力反馈，以及部署阶段沿用同一动作接口这三者统一在同一框架内。

### 实验设置与关键结果

作者在多个 loco-manipulation 任务上对该接口进行了评估，并通过在抓放（pick-and-place）演示上微调 MolmoAct2、随后在实体机器人上部署，验证了从采集到部署的完整流程；部署过程不做动作重定向，也不额外引入逆运动学。代码已开源于 https://github.com/iit-DLSLab/LocoPilot。

### 结论

LocoPilot 以单操作员双边遥操作的方式，在真实腿足平台上同时采集底盘与手臂协同的演示数据，并提供与部署一致的动作接口，配合无力/力矩传感器条件下的触觉反馈，构成了从数据采集到策略部署的完整闭环。

## Overview

Learning loco-manipulation policies requires demonstrations that capture coordinated base and arm motion on the target embodiment. Robot-free interfaces allow demonstrations to be collected independently of the target robot, increasing flexibility but without directly capturing platform-specific commands, proprioception, and body-mounted observations. On-robot teleoperation allows to capture these signals directly, but requires an interface capable of commanding the complete system concurrently. This paper presents LocoPilot, a single-operator bilateral teleoperation and data-collection framework implemented on a 12-DoF Unitree Go2 quadruped equipped with a 6-DoF AgileX Piper L manipulator, an Intel RealSense D435 wrist camera, and an Intel RealSense D405 head camera. A second 6-DoF Piper L arm, used as the leader and two handheld controllers provide simultaneous control of the base, body posture, manipulator, and gripper. The follower arm interaction forces are estimated without a dedicated force/torque sensor and rendered to the operator through a passivity-constrained haptic channel. A ROS~2 pipeline records synchronized multimodal observations together with a unified 11D action shared by teleoperation and policy deployment. Compared to prior work, LocoPilot uniquely unifies robot-in-the-loop legged data collection, force feedback without motion-capture instrumentation, and the same action interface at deployment. We evaluate the interface across multiple loco-manipulation tasks and validate the complete collection-to-deployment pipeline by fine-tuning MolmoAct2 \cite{MOLMO} on pick-and-place demonstrations and deploying on the physical robot without action retargeting or additional inverse kinematics. Code available at: https://github.com/iit-DLSLab/LocoPilot

## 参考
- https://arxiv.org/abs/2610.27998
