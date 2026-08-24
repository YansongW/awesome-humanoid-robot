---
$id: ent_paper_tang_video2doortraversal_push_door_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Video2DoorTraversal: Push Door Traversal via Simulated Door Twins'
  zh: 'Video2DoorTraversal: Push Door Traversal via Simulated Door Twins'
  ko: 'Video2DoorTraversal: Push Door Traversal via Simulated Door Twins'
summary:
  en: Door opening and traversal is a long-horizon loco-manipulation task that requires precise handle interaction and coordinated
    base-arm control. We present Video2DoorTraversal, a single-video real-to-sim-to-real framework for wheel-legged mobile
    manipulators. Given one RGB video of a real door, DoorTwin reconstructs an instance-aligned, articulated, and simulation-ready
    door twin with realistic ...
  zh: Video2DoorTraversal 是一个基于单段真实视频的“真实到仿真再到真实”框架，用于轮腿式移动操作机器人的推门穿越任务。它通过 DoorTwin 重建仿真门孪生体，训练 ArticuACT 双深度策略，在五扇真实门上达到
    96.57% 的平均成功率，并在未见过的相似结构门上实现 80.95% 的零样本成功率。
  ko: Door opening and traversal is a long-horizon loco-manipulation task that requires precise handle interaction and coordinated
    base-arm control. We present Video2DoorTraversal, a single-video real-to-sim-to-real framework for wheel-legged mobile
    manipulators. Given one RGB video of a real door, DoorTwin reconstructs an instance-aligned, articulated, and simulation-ready
    door twin with realistic ...
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
- door_traversal
- real_to_sim_to_real
- wheel_legged_robot
- mobile_manipulation
- policy_learning
- simulation_reconstruction
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-24'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-24). Bibliographic metadata from arXiv API (2608.20251);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.20251 Video2DoorTraversal: Push Door Traversal via Simulated Door Twins'
  url: https://arxiv.org/abs/2608.20251
  date: '2026-08-20'
  accessed_at: '2026-08-24'
---

## 概述

该框架由 Xincheng Tang 等人提出，针对长时程的推门穿越任务，结合了精确的把手交互与基座-手臂协调控制。核心流程包括：从单段 RGB 视频中重建实例对齐、可动且仿真就绪的门孪生体；通过仿真循环代理将门铰链参数转化为参数化技能程序，并迭代优化失败轨迹以生成物理可执行的演示；最后利用这些演示训练 ArticuACT 策略，该策略基于机器人中心相机条件化与交互感知监督，预测基座、手臂和夹爪的协调指令。所有感知与策略推理均在机载完成，系统平均完成整个接近、开门和穿越序列约需 13 秒。

## 核心内容

### 问题背景
推门穿越是一项长时程的移动操作任务，要求机器人精确操作门把手，并协调基座与手臂的运动。现有方法通常依赖预定义的门模型或大量人工演示，难以适应真实环境中门的多样性与物理交互的复杂性。

### 方法
- **DoorTwin 重建**：输入单段真实门的 RGB 视频，重建出实例对齐、具有铰链关节且仿真就绪的门孪生体，包含逼真的几何与外观信息。
- **仿真循环代理**：将恢复的门铰链参数转化为参数化技能程序，并在仿真中迭代执行；对失败的轨迹进行细化，生成物理上可执行的演示数据。
- **ArticuACT 策略**：一种双深度策略网络，使用机器人中心相机条件化输入，并引入交互感知监督，同时预测基座、手臂和夹爪的协调指令。

### 实验设置与关键结果
- 在五扇真实门上测试，平均成功率达到 96.57%。
- 对结构相似但未见过的门进行零样本测试，成功率为 80.95%。
- 整个接近、开门和穿越序列的平均完成时间约为 13 秒。
- 所有感知与策略推理均在机器人机载计算设备上实时运行，无需外部服务器。

### 结论
Video2DoorTraversal 展示了通过仿真门孪生体将单段视频转化为可执行操作策略的有效性，显著提升了轮腿式移动操作机器人在真实推门任务中的泛化能力与成功率。项目页面提供更多细节与演示。

## Overview

Door opening and traversal is a long-horizon loco-manipulation task that requires precise handle interaction and coordinated base-arm control. We present Video2DoorTraversal, a single-video real-to-sim-to-real framework for wheel-legged mobile manipulators. Given one RGB video of a real door, DoorTwin reconstructs an instance-aligned, articulated, and simulation-ready door twin with realistic geometry and appearance. A simulation-in-the-loop agent converts the recovered articulation into a parameterized skill program and iteratively refines failed rollouts to generate physically executable demonstrations. These demonstrations are used to train ArticuACT, a dual-depth policy that predicts coordinated base, arm, and gripper commands using robot-centric camera conditioning and interaction-aware supervision. With all perception and policy inference running onboard, the system achieves a 96.57% average success rate across five real doors and an 80.95% zero-shot success rate on structurally similar unseen doors, while completing the full approach, opening, and traversal sequence in approximately 13s on average. Project Page: https://video2doortraversal.github.io/.

## 参考
- https://arxiv.org/abs/2608.20251
