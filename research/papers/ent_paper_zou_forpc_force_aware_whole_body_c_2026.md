---
$id: ent_paper_zou_forpc_force_aware_whole_body_c_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ForPC: Force-Aware Whole-Body Control for Precise Humanoid Cart Pushing'
  zh: 'ForPC: Force-Aware Whole-Body Control for Precise Humanoid Cart Pushing'
  ko: 'ForPC: Force-Aware Whole-Body Control for Precise Humanoid Cart Pushing'
summary:
  en: Humanoid robots are expected to take over strenuous material handling in manufacturing, logistics, and healthcare, where
    operating existing wheeled carts would let them move heavy loads without modifying the workplace. However, humanoid cart
    pushing remains challenging because the bimanual grasp closes a force-coupled loop in which the contact wrenches that
    drive the cart also disturb the robot's ...
  zh: ForPC 是一个面向人形机器人推车任务的力量感知全身控制框架，由 ZhenYu Zou、Xing Liu 等作者提出。该方法通过两阶段强化学习实现：先训练运动先验以提供平衡支撑，再结合从机载观测推断的力量隐变量与状态隐变量，由残差策略协调手臂、腰部与腿部动作及基座速度指令。仿真实验表明，相比仅运动控制基线（Loco-only），ForPC
    将推车速度 RMSE 最多降低 68.2%，在多弯道路线上的横向跟踪 RMSE 最多降低 74.2%，并零样本迁移至实体 Unitree G1，在无负载专项调整的情况下以 0.5 m/s 推动载重达 30 kg 的推车。
  ko: Humanoid robots are expected to take over strenuous material handling in manufacturing, logistics, and healthcare, where
    operating existing wheeled carts would let them move heavy loads without modifying the workplace. However, humanoid cart
    pushing remains challenging because the bimanual grasp closes a force-coupled loop in which the contact wrenches that
    drive the cart also disturb the robot's ...
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
- humanoid_robot
- whole_body_control
- reinforcement_learning
- sim_to_real_transfer
- loco_manipulation
- force_aware_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.08664);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.08664 ForPC: Force-Aware Whole-Body Control for Precise Humanoid Cart Pushing'
  url: https://arxiv.org/abs/2611.08664
  date: '2026-11-05'
  accessed_at: '2026-11-09'
- id: src_002
  type: website
  title: Project page
  url: https://roboforpc.github.io/
  accessed_at: '2026-11-09'
---

## 概述

人形机器人有望在制造、物流与医疗场景中接管繁重的物料搬运任务，而直接操作现有轮式推车无需改造工作环境，是颇具吸引力的方案。但双臂抓握会形成力耦合闭环：驱动推车的接触力同时扰动机器人平衡，且负载变化会改变耦合动力学，使推车控制颇具挑战。为此，作者提出 ForPC 力量感知全身控制框架，通过两阶段强化学习调节推车速度。第一阶段在不同手部负载与上肢姿态下训练运动先验以提供平衡支撑；第二阶段从机载观测中推断力量隐变量与状态隐变量（无需外部力传感器），并输入残差策略，协调受限的手臂、腰部与腿部调整及基座速度指令。多目标奖励对双臂内力对抗、抓握滑移与执行器饱和进行惩罚，使策略无需人类示教即可按需施加接触力。仿真实验显示该方法显著优于仅运动控制基线，且仅经仿真训练即可零样本迁移到实体 Unitree G1，推动载重 30 kg 的推车以 0.5 m/s 行进。

## 核心内容

### 问题背景

在制造、物流与医疗等场景中，人形机器人被期望接管繁重的物料搬运工作。若机器人能直接操作现场已有的轮式推车，就可在不改造工作环境的前提下搬运重物。然而人形机器人推车面临的核心困难在于：双臂抓握推车会闭合一个力耦合回路，驱动推车的接触力同时会干扰机器人自身平衡；同时负载变化会改变这一耦合动力学，使控制问题更加复杂。

### 方法

作者提出 ForPC，一个力量感知的全身控制框架，通过两阶段强化学习实现对推车速度的调节：

- **第一阶段：运动先验训练。** 在不同手部负载与上肢姿态条件下训练运动先验，为机器人提供平衡支撑能力。
- **第二阶段：残差策略学习。** 从机载观测中推断力量隐变量与状态隐变量，无需外部力传感器；两者输入残差策略，由该策略协调受限的手臂、腰部与腿部调整，并结合基座速度指令。
- **多目标奖励设计。** 奖励中对双臂内力对抗、抓握滑移与执行器饱和施加惩罚，促使策略按需施加接触力，且不依赖人类示教数据。

### 实验设置

实验包含 sim-to-sim 对比实验与实机迁移测试。对比基线为仅运动控制的方法（Loco-only）。实机平台为 Unitree G1 人形机器人，策略仅在仿真中训练，未进行真实世界训练或微调。

### 关键结果

- 在 sim-to-sim 实验中，ForPC 相对 Loco-only 基线将推车速度 RMSE 最多降低 68.2%。
- 在多弯道路线上，横向跟踪 RMSE 最多降低 74.2%。
- 仅经仿真训练的策略零样本迁移至实体 Unitree G1，在无负载专项调整的情况下，以 0.5 m/s 推动载重达 30 kg 的推车。

### 结论

结果表明，力量感知的全身控制策略可有效应对双臂推车中的力耦合与平衡干扰问题，并具备从仿真到实机的迁移能力。作者认为，这预示着人形机器人未来有望在日常生活场景中替代人类完成高效的物料搬运任务。

## Overview

Humanoid robots are expected to take over strenuous material handling in manufacturing, logistics, and healthcare, where operating existing wheeled carts would let them move heavy loads without modifying the workplace. However, humanoid cart pushing remains challenging because the bimanual grasp closes a force-coupled loop in which the contact wrenches that drive the cart also disturb the robot's balance, and payload changes alter the coupled dynamics. We propose ForPC, a force-aware whole-body control framework that regulates cart velocity through two-stage reinforcement learning. A locomotion prior is first trained under varied hand loads and upper-body postures to provide balance support. A force latent and a state latent are then inferred from onboard observations, without external force sensors, and fed to a residual policy that coordinates bounded arm, waist, and leg adjustments with base-velocity commands. Multi-objective rewards penalize bimanual internal opposition, grasp slip, and actuator saturation, encouraging the policy to apply contact force on demand without human demonstrations. Sim-to-sim experiments show that ForPC reduces cart-velocity RMSE by up to 68.2% relative to a locomotion-only baseline (Loco-only) and cross-track RMSE by up to 74.2% on the multi-bend route. Trained solely in simulation, the policy also transfers to a physical Unitree G1 without real-world training or fine-tuning and, with no payload-specific adjustment, pushes a cart carrying up to 30 kg at 0.5 m/s. These results suggest that humanoid robots could eventually replace humans for efficient material handling in daily life.

## 参考
- https://arxiv.org/abs/2611.08664
- https://roboforpc.github.io/
