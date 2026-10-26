---
$id: ent_paper_marew_fast_motion_retargeting_pipeli_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Fast Motion Retargeting Pipeline for Scalable Humanoid Robot Learning
  zh: Fast Motion Retargeting Pipeline for Scalable Humanoid Robot Learning
  ko: Fast Motion Retargeting Pipeline for Scalable Humanoid Robot Learning
summary:
  en: While large-scale human motion capture datasets provide a rich source of demonstrations for humanoid robot learning,
    retargeting the diverse motions to different humanoid robots remains a nontrivial challenge. Existing kinodynamic trajectory
    optimization pipelines are computationally expensive and often require manual adjustments per motion. We present FRDV
    (Fast Retargeting with Dynamics ...
  zh: FRDV（Fast Retargeting with Dynamics Validation）是由 Daniel Marew、Sangjun Park、Nisal Perera、Donghyun Kim 提出的可扩展人形机器人运动重定向框架，由快速约束运动学重定向与动力学验证两部分组成。其运动学阶段结合自定义
    Sequential Quadratic Programming 求解器、Real-Time Iteration 与并行分块处理，最高可达每秒 9,156 帧，相比 GMR 与 ProtoMotions 约快至 136 倍。对于需要进一步验证的运动，该框架使用接触隐式
    iLQR 控制器在完整刚体动力学下检验重定向参考，识别动力学不可行动作并改善脚部漂浮、脚部打滑等接触相关伪影。
  ko: While large-scale human motion capture datasets provide a rich source of demonstrations for humanoid robot learning,
    retargeting the diverse motions to different humanoid robots remains a nontrivial challenge. Existing kinodynamic trajectory
    optimization pipelines are computationally expensive and often require manual adjustments per motion. We present FRDV
    (Fast Retargeting with Dynamics ...
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
- motion_retargeting
- humanoid_robot
- sequential_quadratic_programming
- ilqr
- sim_to_real
- motion_tracking
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.28470);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.28470 Fast Motion Retargeting Pipeline for Scalable Humanoid Robot Learning
  url: https://arxiv.org/abs/2610.28470
  date: '2026-10-20'
  accessed_at: '2026-10-26'
---

## 概述

大规模人体运动捕捉数据集为人形机器人学习提供了丰富的示范来源，但将多样运动重定向到不同人形机器人仍具挑战，现有运动学-动力学轨迹优化流程计算代价高且常需逐运动人工调整。为此，作者提出 FRDV，一个由快速约束运动学重定向和额外动力学验证流程构成的可扩展框架。其运动学阶段集成自定义 Sequential Quadratic Programming 求解器、Real-Time Iteration 与并行分块处理，最高达到每秒 9,156 帧，相比 GMR 和 ProtoMotions 约快至 136 倍，并在优化中引入机器人特定约束以减少地面穿透与自碰撞等常见重定向伪影。对于需要额外验证的运动，框架采用接触隐式 iLQR 控制器在完整刚体动力学下测试重定向参考，从而识别动力学不可行的运动并改善脚部漂浮、脚部打滑等接触相关伪影。作者通过使用多种先进流程训练运动跟踪强化学习策略来评估重定向质量，比较其跟踪保真度与成功率，并在 Unitree G1 人形机器人上展示了仿真到现实的迁移。

## 核心内容

### 问题背景
大规模人体运动捕捉数据集可为人形机器人学习提供丰富的示范，但把多样运动重定向到不同人形机器人并非易事。现有基于运动学-动力学的轨迹优化流程计算开销大，且往往需要针对每个运动进行人工调整。

### 方法
作者提出 FRDV（Fast Retargeting with Dynamics Validation），一个可扩展框架，包含两个阶段：

- **快速约束运动学重定向**：集成自定义 Sequential Quadratic Programming 求解器、Real-Time Iteration 以及并行分块处理；在优化中纳入机器人特定约束，以减少地面穿透、自碰撞等常见重定向伪影。
- **动力学验证**：对需要额外验证的运动，使用接触隐式 iLQR 控制器在完整刚体动力学下测试重定向后的参考，识别动力学上不可行的运动，并改善脚部漂浮、脚部打滑等接触相关伪影。

### 实验设置与关键结果
- 运动学阶段最高达到每秒 9,156 帧，相比 GMR 与 ProtoMotions 约快至 136 倍。
- 通过使用多种先进流程训练运动跟踪强化学习策略来评估重定向质量，并比较跟踪保真度与成功率。
- 在 Unitree G1 人形机器人上展示了仿真到现实的迁移。

### 结论
FRDV 通过快速约束运动学重定向与动力学验证相结合，在显著提升重定向速度的同时减少常见伪影，并支持运动跟踪策略训练与实机迁移。视频与代码见 https://daroslab.github.io/frdv/。

## Overview

While large-scale human motion capture datasets provide a rich source of demonstrations for humanoid robot learning, retargeting the diverse motions to different humanoid robots remains a nontrivial challenge. Existing kinodynamic trajectory optimization pipelines are computationally expensive and often require manual adjustments per motion. We present FRDV (Fast Retargeting with Dynamics Validation), a scalable framework consisting of rapid constrained kinematic retargeting and an additional dynamics validation pipeline. Its kinematic stage integrates a custom Sequential Quadratic Programming solver, Real-Time Iteration, and parallel chunk-based processing, achieving up to 9,156 frames per second, approximately up to 136 times faster than GMR and ProtoMotions, while robot-specific constraints are incorporated into the optimization to reduce common retargeting artifacts, such as ground penetration and self-collision. For motions requiring additional verification, a contact implicit iLQR controller is utilized to test the retargeted reference under full rigid body dynamics. This dynamics-based validation identifies dynamically infeasible motions and refines contact-related artifacts such as foot floating and foot skating. We evaluate retargeting quality by training motion tracking reinforcement learning policies using several state-of-the-art pipelines and comparing their tracking fidelity and success rates. Furthermore, sim-to-real transfer is demonstrated on a Unitree G1 humanoid. Videos and code are available at: https://daroslab.github.io/frdv/.

## 参考
- https://arxiv.org/abs/2610.28470
