---
$id: ent_paper_cao_humit_low_latency_whole_body_h_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HuMiT: Low-Latency Whole-Body Humanoid Teleoperation via Compact Reference Tracking'
  zh: 'HuMiT: Low-Latency Whole-Body Humanoid Teleoperation via Compact Reference Tracking'
  ko: 'HuMiT: Low-Latency Whole-Body Humanoid Teleoperation via Compact Reference Tracking'
summary:
  en: Real-time whole-body humanoid teleoperation remains challenging due to the computational latency introduced by optimization-based
    retargeting pipelines and future-frame conditioning. Existing motion tracking policies typically require dense reference
    targets including full joint positions, body-part transformations, and even future frames, which tightly couples the controller
    to expensive ...
  zh: HuMiT 是一套面向人形机器人的全身实时遥操作系统，由 Liu Cao、Botian Xu、Ruoqu Chen 等作者提出。其核心是一个统一跟踪策略，仅需由根高度、根速度与当前帧四个稀疏关键点的 SE(3) 位姿构成的紧凑参考目标，即可达到与依赖完整关节位置、密集身体部位变换乃至未来帧的方法相当的跟踪精度。系统在
    Unitree G1 上验证，从头显推流到策略输出的通信至推理延迟约 20 ms，基于视频的光流延迟中位数为 65 ms。
  ko: Real-time whole-body humanoid teleoperation remains challenging due to the computational latency introduced by optimization-based
    retargeting pipelines and future-frame conditioning. Existing motion tracking policies typically require dense reference
    targets including full joint positions, body-part transformations, and even future frames, which tightly couples the controller
    to expensive ...
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
- humanoid_teleoperation
- whole_body_control
- motion_tracking
- low_latency
- unitree_g1
- loco_manipulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.29903);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.29903 HuMiT: Low-Latency Whole-Body Humanoid Teleoperation via Compact Reference Tracking'
  url: https://arxiv.org/abs/2610.29903
  date: '2026-10-21'
  accessed_at: '2026-10-26'
- id: src_002
  type: website
  title: Project page
  url: https://xiaohu-art.github.io/Track/
  accessed_at: '2026-10-26'
---

## 概述

现有全身人形遥操作受制于基于优化的重定向流程与未来帧条件化所带来的计算延迟，运动跟踪策略通常需要完整关节位置、身体部位变换甚至未来帧等密集参考目标，使控制器与昂贵的上游模块紧密耦合。HuMiT 针对这一问题提出统一跟踪策略，把参考输入压缩为根高度、根速度与当前帧四个稀疏关键点的 SE(3) 位姿，在显著降低输入需求的同时保持有竞争力的跟踪保真度。作者在 Unitree G1 人形机器人上验证系统，测得头显推流到策略输出的通信至推理延迟约 20 ms，不同运动类型下基于视频的光流延迟中位数为 65 ms。系统展现出接住抛来球体这类亚秒级反应能力，以及协调的运动—操作能力。

## 核心内容

### 问题背景

实时全身人形遥操作面临两类主要延迟来源：一是基于优化的重定向管线，二是对未来帧的依赖（future-frame conditioning）。现有运动跟踪策略往往要求密集参考目标，包括完整关节位置、身体部位变换，甚至未来帧，这使控制器与计算代价高昂的上游模块紧密耦合，难以实现低延迟的闭环遥操作。

### 方法

作者提出 HuMiT，其基础是一个统一跟踪策略。该策略的参考输入被压缩为一个紧凑参考目标，仅包含：

- 根高度（root height）
- 根速度（root velocity）
- 当前帧四个稀疏关键点的 SE(3) 位姿

尽管输入远少于常规方法，该策略仍能达到与使用完整关节位置、密集身体部位变换及未来帧等更丰富参考状态的方法相竞争的跟踪保真度。

### 实验设置与关键结果

- 延迟测量：从头显推流到策略输出的通信至推理延迟约为 20 ms；基于视频的光流延迟在不同运动类型下的中位数为 65 ms。
- 硬件验证平台：Unitree G1 人形机器人。
- 能力展示：系统实现了亚秒级（split-second）反应，例如接住抛来的球；同时展示了协调的运动—操作（loco-manipulation）能力。

### 结论

HuMiT 表明，仅依赖紧凑参考目标即可构建低延迟的全身人形遥操作系统，在保持跟踪保真度的同时摆脱对密集参考状态与未来帧的依赖，并在真实人形平台上验证了快速反应与协调运动—操作能力。项目页面为 https://xiaohu-art.github.io/Track/。

## Overview

Real-time whole-body humanoid teleoperation remains challenging due to the computational latency introduced by optimization-based retargeting pipelines and future-frame conditioning. Existing motion tracking policies typically require dense reference targets including full joint positions, body-part transformations, and even future frames, which tightly couples the controller to expensive upstream modules. In this work, we present HuMiT, a whole-body teleoperation system built on a unified tracking policy that requires only a compact reference target, consisting of root height, root velocity, and the SE(3) poses of four sparse keypoints at the current frame, yet achieves competitive tracking fidelity compared to methods relying on more diverse reference states including complete joint positions, dense body-part transformations, and even future frames. Experiments show that our policy achieves a communication-to-inference latency of $\sim$20 ms measured between headset streaming and policy output and a video-based optical flow latency of 65 ms (median) across different motion types. We validate the system on a Unitree G1 humanoid, showcasing split-second reactive responses such as catching a tossed ball, as well as coordinated loco-manipulation capabilities. Project page: https://xiaohu-art.github.io/Track/.

## 参考
- https://arxiv.org/abs/2610.29903
- https://xiaohu-art.github.io/Track/
