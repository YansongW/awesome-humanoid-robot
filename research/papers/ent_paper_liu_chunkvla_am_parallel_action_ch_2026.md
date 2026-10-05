---
$id: ent_paper_liu_chunkvla_am_parallel_action_ch_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ChunkVLA-AM: Parallel Action Chunking for Vision-Language-Action Robot Control in Additive Manufacturing'
  zh: 'ChunkVLA-AM: Parallel Action Chunking for Vision-Language-Action Robot Control in Additive Manufacturing'
  ko: 'ChunkVLA-AM: Parallel Action Chunking for Vision-Language-Action Robot Control in Additive Manufacturing'
summary:
  en: Vision-language-action (VLA) models unify visual perception, language understanding, and action generation, offering
    new opportunities for automation in additive manufacturing (AM). However, deployment in AM remains challenging because
    adapting these models to unseen robot embodiments is costly, and performance can degrade under environment changes. In
    this work, we present a framework for ...
  zh: 本文提出一套在增材制造（AM）固定工作单元中部署 OpenVLA-OFT 的框架，将其适配到 FAIRINO FR3 机器人本体。作者构建数据流水线，把单目真实世界演示转换为 OpenVLA 兼容的 TFDS/RLDS 数据集，并在运行时以八步
    7 维动作块进行推理，块间采用开环执行加新观测形成闭环反馈。系统采用云边架构，FR3 客户端经 FastAPI 接口向远程推理服务器流式传输观测；在 42 次实物 A 到 B 物体搬运试验中成功 39 次（92.9%）。
  ko: Vision-language-action (VLA) models unify visual perception, language understanding, and action generation, offering
    new opportunities for automation in additive manufacturing (AM). However, deployment in AM remains challenging because
    adapting these models to unseen robot embodiments is costly, and performance can degrade under environment changes. In
    this work, we present a framework for ...
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
- vision_language_action
- openvla_oft
- additive_manufacturing
- action_chunking
- cloud_edge_inference
- robot_manipulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2610.01856);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.01856 ChunkVLA-AM: Parallel Action Chunking for Vision-Language-Action Robot Control in Additive Manufacturing'
  url: https://arxiv.org/abs/2610.01856
  date: '2026-10-01'
  accessed_at: '2026-10-05'
---

## 概述

该工作面向增材制造场景中 VLA 模型部署的两大障碍：适配未见机器人本体成本高，以及环境变化下性能下降。作者在固定 AM 工作单元内，将 OpenVLA-OFT 部署到 FAIRINO FR3 机器人上，并通过数据流水线把单目真实演示转成 OpenVLA 兼容的 TFDS/RLDS 数据集以支持本体适配。运行时每次推理请求预测一个八步的 7 维动作块，FR3 先开环执行整块动作再采集新观测，从而在块与块之间形成闭环反馈。系统采用云边架构，FR3 客户端通过 FastAPI 接口把观测流式发送到远程推理服务器。在 42 次实物 A 到 B 搬运试验（红蓝目标各半）中成功 39 次，三次失败均发生在最终放置阶段，原因是释放高度控制不足导致物体倾倒；光照扫描还确定了 0-255 尺度下 85-125 的低误差亮度区间，其中 95 处平均空间误差最低。

## 核心内容

### 问题背景
视觉-语言-动作（VLA）模型将视觉感知、语言理解与动作生成统一起来，为增材制造（AM）自动化带来新机会。但在 AM 中部署仍面临困难：把这类模型适配到未见过的机器人本体代价高昂，且环境变化会导致性能退化。

### 方法
- 在固定 AM 工作单元中，将 OpenVLA-OFT 部署到 FAIRINO FR3 机器人上。
- 构建数据流水线，把单目真实世界演示转换为 OpenVLA 兼容的 TFDS/RLDS 数据集，以支持向 FR3 本体的适配。
- 运行时每次推理请求预测一个八步的 7 维动作块（eight-step chunk of 7-D actions）。
- FR3 先以开环方式执行整个动作块，随后再采集新观测，从而在块与块之间提供闭环反馈。
- 系统采用云边架构：FR3 客户端通过 FastAPI 接口把观测流式传输到远程推理服务器。

### 实验设置
- 42 次实物 A 到 B 物体搬运试验，红色与蓝色目标各占一半。
- 进行光照扫描，在 0-255 尺度上评估亮度对误差的影响。

### 关键结果
- 42 次试验中成功 39 次，成功率 92.9%。
- 三次失败全部发生在最终放置阶段，原因是释放高度控制不足导致物体倾倒。
- 光照扫描识别出 0-255 尺度下 85-125 的低误差亮度区间，其中平均空间误差最低出现在 95。

### 结论
该框架验证了在固定 AM 工作单元内将 OpenVLA-OFT 适配到 FAIRINO FR3 的可行性，块间闭环与云边推理架构可支撑实物搬运任务，但最终放置阶段的释放高度控制仍是主要失败来源。

## Overview

Vision-language-action (VLA) models unify visual perception, language understanding, and action generation, offering new opportunities for automation in additive manufacturing (AM). However, deployment in AM remains challenging because adapting these models to unseen robot embodiments is costly, and performance can degrade under environment changes. In this work, we present a framework for deploying OpenVLA-OFT on a FAIRINO FR3 robot in a fixed AM workcell. A data pipeline converts monocular real-world demonstrations into OpenVLA-compatible TFDS/RLDS datasets to support adaptation to the FR3 embodiment. At runtime, each inference request predicts an eight-step chunk of 7-D actions. The FR3 executes each chunk open loop before capturing a new observation, providing closed-loop feedback between chunks. The system uses a cloud-edge architecture in which the FR3 client streams observations to a remote inference server through a FastAPI interface. In 42 physical A-to-B object-transfer trials, evenly split between red and blue targets, the system succeeded in 39 (92.9%). All three failures occurred during final placement, when insufficient release-height control caused the object to topple. An illumination sweep identified a low-error luminance range of 85-125 on a 0-255 scale, with the lowest mean spatial error at 95.

## 参考
- https://arxiv.org/abs/2610.01856
