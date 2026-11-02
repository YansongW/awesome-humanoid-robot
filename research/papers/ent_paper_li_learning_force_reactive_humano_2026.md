---
$id: ent_paper_li_learning_force_reactive_humano_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Force-Reactive Humanoid Loco-Manipulation
  zh: Learning Force-Reactive Humanoid Loco-Manipulation
  ko: Learning Force-Reactive Humanoid Loco-Manipulation
summary:
  en: Many everyday tasks require controlling contact force as well as motion. On a humanoid, this force must often be coordinated
    across both hands and the whole body, and cannot be specified by kinematic trajectories alone. Therefore, we present FLORE,
    a framework for learning force-reactive humanoid loco-manipulation. We collect robot-free demonstrations using two force-sensing
    UMI-style handheld ...
  zh: FLORE 是一个用于学习力反应式人形机器人移动操作（loco-manipulation）的框架，由 Sihang Li、Xiaofeng Guo、Jinkun Cao、Charlie Cheng、Ruihan Yang、Chen
    Feng、Guanya Shi、Haozhi Qi 共同提出。该工作使用两个力感知的 UMI 风格手持夹爪与可穿戴追踪器采集无机器人演示，训练以视觉、本体感知和实测力旋量为输入的力反应扩散策略，并配合带力跟踪的混合柔顺全身控制器执行动作与每手力指令。在三个接触密集任务上，力反应策略的成功率为
    80%，而仅位置策略为 26.7%。
  ko: Many everyday tasks require controlling contact force as well as motion. On a humanoid, this force must often be coordinated
    across both hands and the whole body, and cannot be specified by kinematic trajectories alone. Therefore, we present FLORE,
    a framework for learning force-reactive humanoid loco-manipulation. We collect robot-free demonstrations using two force-sensing
    UMI-style handheld ...
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
- humanoid_loco_manipulation
- force_reactive_policy
- diffusion_policy
- whole_body_control
- compliant_control
- contact_rich_manipulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.35862);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.35862 Learning Force-Reactive Humanoid Loco-Manipulation
  url: https://arxiv.org/abs/2610.35862
  date: '2026-10-26'
  accessed_at: '2026-11-02'
---

## 概述

许多人形机器人的日常任务不仅需要控制运动，还需要控制接触力，且这种力往往要在双手与全身之间协调，无法仅靠运动学轨迹指定。FLORE 针对这一问题提出了一套完整的学习框架：用两个带力传感的 UMI 风格手持夹爪采集手部运动与接触力旋量，用可穿戴追踪器采集身体运动，从而在无需机器人本体的情况下获得演示数据。策略侧采用力反应扩散策略，输入视觉、本体感知与实测力旋量，输出动作以及每只手的力指令；执行侧采用带力跟踪的混合柔顺全身控制器，在保持平衡的同时完成指令。控制器利用真实力/力矩（F/T）传感器测得的力误差积分，使每只手沿指令方向精确跟踪力、在其他方向保持柔顺。仿真中该控制器能在全身运动精度损失很小的情况下跟踪不同大小与方向的手部力指令；在机器人上的三个接触密集任务中，力反应策略成功率为 80%，显著高于同一控制器下仅位置策略的 26.7%。

## 核心内容

### 问题背景

人形机器人的许多日常任务需要同时控制接触力与运动。这类力通常需要在双手与全身之间协调，仅用运动学轨迹无法完整指定。现有方法多聚焦于位置或运动轨迹层面的操作，缺少对接触力的显式建模与执行能力。

### 方法

- **数据采集**：不使用机器人本体，而是通过两个带力传感的 UMI 风格手持夹爪采集手部运动与接触力旋量，并通过可穿戴追踪器采集身体运动，从而获得无机器人的演示数据。
- **力反应扩散策略**：以视觉、本体感知和实测力旋量为输入，预测动作以及每只手的力指令。
- **混合柔顺全身控制器**：带力跟踪能力，在执行动作与力指令的同时维持平衡。控制器对真实力/力矩（F/T）传感器测得的力误差做积分，使每只手沿指令方向精确跟踪力，并在其他方向保持柔顺。

### 实验设置

- 仿真实验：验证控制器对不同大小与方向的手部力指令的跟踪能力，并考察全身运动精度。
- 真机实验：在机器人上开展三个接触密集任务，对比力反应策略与仅位置策略（两者使用相同演示数据训练、由相同控制器执行）。

### 关键结果

- 仿真中，控制器能够跟踪不同大小与方向的手部力指令，全身运动精度损失很小。
- 真机三个接触密集任务中，力反应策略的成功率为 80%，仅位置策略为 26.7%。

### 结论

FLORE 表明，将力感知演示采集、力反应扩散策略与带力跟踪的混合柔顺全身控制器结合，可让人形机器人在保持平衡的同时完成需要协调双手与全身接触力的移动操作任务，效果显著优于仅依赖位置信息的策略。

## Overview

Many everyday tasks require controlling contact force as well as motion. On a humanoid, this force must often be coordinated across both hands and the whole body, and cannot be specified by kinematic trajectories alone. Therefore, we present FLORE, a framework for learning force-reactive humanoid loco-manipulation. We collect robot-free demonstrations using two force-sensing UMI-style handheld grippers for hand motion and contact wrenches, and wearable trackers for body motion. A force-reactive diffusion policy takes vision, proprioception, and measured wrenches as input, then predicts actions and per-hand force commands. A hybrid compliance whole-body controller with force tracking executes these commands while maintaining balance: an integral of the force error measured by real force/torque (F/T) sensors lets each hand track force accurately along the commanded direction and remain compliant along the others. In simulation, the controller tracks per-hand force commands of varied magnitude and direction, with little loss in whole-body motion accuracy. Across three contact-rich tasks on the robot, the force-reactive policy succeeds in 80% of rollouts, compared with 26.7% for a position-only policy trained on the same demonstrations and executed by the same controller. For more details, please visit our website: https://louis-leee.github.io/FLoRe/.

## 参考
- https://arxiv.org/abs/2610.35862
