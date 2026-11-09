---
$id: ent_paper_weekly_online_hamilton_jacobi_reachab_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy'
  zh: 'Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy'
  ko: 'Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy'
summary:
  en: Hamilton-Jacobi (HJ) reachability provides certified backward reachable tubes (BRTs) for safety-critical robotic systems,
    but the level-set computation scales exponentially in the state dimension and has historically been performed offline.
    As autonomy stacks (ADAS/AV, humanoid robotics, and vision-language-action models) increasingly rely on black-box, probabilistic
    policies, a deterministic ...
  zh: 本文提出一个基于 CUDA 的 Hamilton-Jacobi-Isaacs 水平集求解器实现，采用 WENO5 + TVD-RK3 + Lax-Friedrichs 格式，可在机器人控制回路内实时运行。作者为 Kevin Weekly
    与 Alexandre M. Bayen，在单块 NVIDIA RTX 4000 Ada 工作站 GPU 上以 FP32 计算 3D Air3D BRT 达 112 Hz、4D 追逃 BRT 达 61 Hz、2D 受风漂移体 BRT 达
    74-147 Hz。该工作为依赖黑箱概率策略的自主系统提供具备形式化保证的确定性安全层。
  ko: Hamilton-Jacobi (HJ) reachability provides certified backward reachable tubes (BRTs) for safety-critical robotic systems,
    but the level-set computation scales exponentially in the state dimension and has historically been performed offline.
    As autonomy stacks (ADAS/AV, humanoid robotics, and vision-language-action models) increasingly rely on black-box, probabilistic
    policies, a deterministic ...
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
- hamilton_jacobi_reachability
- level_set_method
- gpu_solver
- safety_critical_control
- real_time_control
- multi_agent_systems
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.04096);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.04096 Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for
    Safety-Critical Autonomy'
  url: https://arxiv.org/abs/2611.04096
  date: '2026-11-03'
  accessed_at: '2026-11-09'
---

## 概述

Hamilton-Jacobi 可达性分析能为安全关键机器人系统给出经过认证的后向可达管（BRT），但水平集计算随状态维数指数增长，历来只能离线完成。随着 ADAS/AV、人形机器人与视觉-语言-动作模型等自主栈愈发依赖黑箱概率策略，具备形式化保证的确定性安全层成为必要补充。作者将经典的 WENO5 + TVD-RK3 + Lax-Friedrichs 水平集 Hamilton-Jacobi-Isaacs 求解器用 CUDA 实现，覆盖 2D、3D 与 4D 动力学，速度足以嵌入机器人控制回路。在单块 NVIDIA RTX 4000 Ada 工作站 GPU 上以 FP32 运行，3D Air3D BRT 达 112 Hz，4D 追逃 BRT 达 61 Hz，2D 受风漂移体 BRT 达 74-147 Hz，相比同精度的 JAX 参考实现 hj_reachability 快 5.9-17.5 倍。FP64 下与 hj_reachability 在八个基准案例上一致，并复现 Mitchell 的 Air3D BRT 至参考单元数 0.04% 以内。作者还给出多智能体扩展与嵌入式平台验证。

## 核心内容

### 问题背景
Hamilton-Jacobi（HJ）可达性可为安全关键机器人系统提供经过认证的后向可达管（BRT），但其水平集计算随状态维数指数增长，历史上只能离线求解。当前自主栈（ADAS/AV、人形机器人、视觉-语言-动作模型）越来越多地采用黑箱、概率性策略，因此需要一个具备形式化保证的确定性安全层作为补充，并且该安全层必须足够快以进入控制回路。

### 方法
- 采用经典水平集 Hamilton-Jacobi-Isaacs 求解格式：WENO5 空间离散、TVD-RK3 时间积分、Lax-Friedrichs 数值通量。
- 以 CUDA 实现，支持 2D、3D 与 4D 动力学。
- 提供 FP32 与 FP64 两种精度路径。
- 多智能体应用：在内核中加入标签传播扩展，从单次组合 HJ 求解中恢复 K 智能体的捕获盆地 Voronoi 剖分，且与机队规模无关。

### 实验设置与关键结果
- 硬件：单块工作站 GPU（NVIDIA RTX 4000 Ada）；嵌入式平台 NVIDIA Jetson AGX Thor。
- FP32 工作站 GPU 吞吐：
  - 3D Air3D BRT：112 Hz
  - 4D 追逃 BRT：61 Hz
  - 2D 受风漂移体 BRT：74-147 Hz
- 加速比：在匹配精度下比 JAX 参考实现 hj_reachability 快 5.9-17.5 倍；比同一格式的 torch.compile 重实现快 1.7-16 倍。
- FP64 精度验证：在八个基准案例上与 hj_reachability 一致；复现 Mitchell 的 Air3D BRT，单元数与参考相差 0.04% 以内；运行速度快 2.0-4.6 倍。
- 嵌入式平台：NVIDIA Jetson AGX Thor 上 Air3D 达 66 Hz（N=41），2D 漂移体达 54 Hz，比同设备上的 hj_reachability 快 3.8-8.9 倍。
- 多智能体闭环仿真：在六架四旋翼、时变非均匀风场下的野火响应仿真中，标签传播扩展每 tick 耗时 4.0 ms。

### 结论
该 CUDA 求解器使 HJ 可达性分析首次具备进入机器人控制回路的实时性，为黑箱概率策略提供确定性安全层；FP64 下与参考实现一致且更快，并在嵌入式 GPU 与多智能体场景中验证了实用性。

## Overview

Hamilton-Jacobi (HJ) reachability provides certified backward reachable tubes (BRTs) for safety-critical robotic systems, but the level-set computation scales exponentially in the state dimension and has historically been performed offline. As autonomy stacks (ADAS/AV, humanoid robotics, and vision-language-action models) increasingly rely on black-box, probabilistic policies, a deterministic safety layer with formal guarantees is an essential complement. We present a CUDA implementation of the canonical WENO5 + TVD-RK3 + Lax-Friedrichs level-set Hamilton-Jacobi-Isaacs solver for 2D, 3D, and 4D dynamics that is fast enough to run inside a robot's control loop. In 32-bit floating point (FP32) on a single workstation GPU (NVIDIA RTX 4000 Ada), it computes the 3D Air3D BRT at 112 Hz, a 4D pursuit-evasion BRT at 61 Hz, and a 2D wind-affected drifter BRT at 74-147 Hz, 5.9-17.5x faster than the JAX reference hj_reachability at matched precision and 1.7-16x faster than a torch.compile reimplementation of the same scheme. In 64-bit floating point (FP64) it agrees with hj_reachability on eight benchmark cases, reproduces Mitchell's Air3D BRT to within 0.04% of the reference cell count, and runs 2.0-4.6x faster. On an embedded NVIDIA Jetson AGX Thor it computes Air3D at 66 Hz (N=41) and the 2D drifter at 54 Hz, 3.8-8.9x faster than hj_reachability on the same device. As a multi-agent application, an in-kernel label-propagation extension recovers the K-agent capture-basin Voronoi tessellation from a single combined HJ solve, independent of fleet size; it runs at 4.0 ms per tick in a closed-loop wildfire-response simulation of six quadcopters under time-varying, non-uniform wind.

## 参考
- https://arxiv.org/abs/2611.04096
