---
$id: ent_paper_harithas_brace_adapting_whole_body_refe_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BRACE: Adapting Whole-Body References for Force and Terrain Aware Humanoid Motion Tracking'
  zh: 'BRACE: Adapting Whole-Body References for Force and Terrain Aware Humanoid Motion Tracking'
  ko: 'BRACE: Adapting Whole-Body References for Force and Terrain Aware Humanoid Motion Tracking'
summary:
  en: 'Whole-body tracking has become the interface through which operators drive humanoid robots, yet the references it consumes
    are recorded on level ground and carrying nothing, so the tracker is aware of neither the forces the robot must exchange
    with objects nor the terrain it must stand on. Existing controllers address one side of this gap: force-capable policies
    command an end-effector force but ...'
  zh: BRACE 是一种面向人形机器人的全身运动跟踪器，由 Sudarshan Harithas、Chen Yu、Juan Borbon、Shubhankar Mondal、Winston Zha、Srinath Sridhar、Dingqi
    Zhang、Jiuguang Wang 共同提出。它把地形贴合与手部力旋量变换折入所跟踪的参考轨迹中，使机器人能在斜坡地形上跟随平地参考、同时施加并补偿指令手部力。方法通过 DAgger 将分别负责施力与补偿的两个教师蒸馏为单一 flow-matching
    学生策略，仅依赖本体感知运行，并在 Unitree-G1 上完成仿真与真机实验。
  ko: 'Whole-body tracking has become the interface through which operators drive humanoid robots, yet the references it consumes
    are recorded on level ground and carrying nothing, so the tracker is aware of neither the forces the robot must exchange
    with objects nor the terrain it must stand on. Existing controllers address one side of this gap: force-capable policies
    command an end-effector force but ...'
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
- humanoid_motion_tracking
- whole_body_control
- force_aware_control
- terrain_adaptation
- teacher_student_distillation
- sim_to_real
- end
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.07052);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.07052 BRACE: Adapting Whole-Body References for Force and Terrain Aware Humanoid Motion Tracking'
  url: https://arxiv.org/abs/2610.07052
  date: '2026-10-05'
  accessed_at: '2026-10-12'
---

## 概述

现有全身跟踪器所消费的参考动作多在平地、空载条件下录制，因此既不了解机器人需要与物体交换的力，也不了解所站立的地形。已有控制器只解决其中一面：具备施力能力的策略只给末端执行器力指令而不规定全身姿态，地形自适应跟踪器则把负载当作需要抑制的扰动而非可指令的力旋量。BRACE 的做法是不让跟踪器被动吸收负载与坡度，而是把两者一并折入参考：地形贴合把落脚点与根位姿抬升到局部表面，力旋量变换则解出产生目标力所需的手部位移，以及随之产生的质心与压力中心偏移，并受教师特定的手臂用力上限约束。施力与补偿两个教师经 DAgger 蒸馏为一个 flow-matching 学生策略，仅凭本体感知运行，无需高度图或实测力旋量，因此远程操作者只需提供平地轨迹，机器人在机即可解算坡度与负载。作者在 Unitree-G1 上开展了大量实验，验证 BRACE 在仿真与真机中施加力、补偿力以及应对多样地形的能力。

## 核心内容

### 问题背景
全身跟踪已成为操作者驱动机器人的人机接口，但其参考轨迹通常在平地录制且不携带任何负载。这带来两个盲区：跟踪器既不知道机器人需要与物体交换多大的力，也不知道脚下地形如何。现有控制器各解决一半问题——具备施力能力的策略可以指令末端执行器力，却不规定全身姿态；地形自适应跟踪器则把负载视为需要抑制的扰动，而不是可以指令的力旋量。

### 方法
BRACE 的核心思路是把负载与坡度都折入跟踪器所跟随的参考，而不是留给跟踪器自行吸收：

- **地形贴合**：将落脚点与根位姿抬升到局部表面，使平地参考在斜坡上仍然可用。
- **力旋量变换**：解算为产生目标手部力所需的手部位移，以及该位移同时引起的质心与压力中心偏移，并受教师特定的手臂用力上限约束。
- **教师蒸馏**：分别训练施力教师与补偿教师，再通过 DAgger 蒸馏为单一 flow-matching 学生策略。
- **仅本体感知部署**：学生策略不依赖高度图，也不依赖实测力旋量，因此远程操作者（即使在异地）只需提供平地轨迹，坡度与负载由机器人在机解算。

### 实验设置
作者在 Unitree-G1 人形机器人上开展了大量实验，覆盖仿真与真机两类场景。

### 关键结果
实验展示了 BRACE 具备三方面能力：施加指令手部力、补偿负载，以及在多样地形上完成运动跟踪。

### 结论
通过把地形贴合与力旋量变换统一折入参考轨迹，并用 DAgger 将施力与补偿两个教师蒸馏为单一仅靠本体感知的 flow-matching 学生策略，BRACE 让操作者只需提供平地、空载的参考动作，机器人即可在斜坡上跟随该参考并同时施加与补偿手部力。

## Overview

Whole-body tracking has become the interface through which operators drive humanoid robots, yet the references it consumes are recorded on level ground and carrying nothing, so the tracker is aware of neither the forces the robot must exchange with objects nor the terrain it must stand on. Existing controllers address one side of this gap: force-capable policies command an end-effector force but prescribe no whole-body pose, while terrain-adaptive trackers treat loads as disturbances to reject rather than wrenches to command. We present BRACE, a whole-body tracker that exerts and compensates commanded hand forces from diverse poses while following a flat-ground reference on sloped terrain. Rather than leaving the tracker to absorb the load and the slope, BRACE folds both into the reference it follows: terrain conformance lifts footholds and root onto the local surface, and a wrench transformation resolves the hand displacement that produces a force jointly with the center-of-mass and center- of-pressure shifts it induces, bounded by teacher-specific arm-effort limits. Separate exertion and compensation teachers are distilled by DAgger into one flow-matching student that runs on proprioception alone, without a height map or measured wrench, so a teleoperator (even in remote locations) can supply a flat- ground trajectory and the robot resolves slope and load onboard. We extensive experiments on the Unitree-G1 to demonstrate the ability of BRACE to exert, compensate force and handle diverse terrain in simulation and real robot experiments.

## 参考
- https://arxiv.org/abs/2610.07052
