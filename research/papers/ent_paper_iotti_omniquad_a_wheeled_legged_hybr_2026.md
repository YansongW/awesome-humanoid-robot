---
$id: ent_paper_iotti_omniquad_a_wheeled_legged_hybr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniQuad: a Wheeled-Legged Hybrid Robot with Omnidirectional Wheels'
  zh: 'OmniQuad: a Wheeled-Legged Hybrid Robot with Omnidirectional Wheels'
  ko: 'OmniQuad: a Wheeled-Legged Hybrid Robot with Omnidirectional Wheels'
summary:
  en: Combining wheeled and legged locomotion within a single robotic platform offers the potential to harness the advantages
    of both systems. The development of such hybrid systems remains an active area of research. While legged robots exhibit
    remarkable adaptability for traversing uneven and rugged terrains, their relatively low speed limits their practicality
    in indoor environments. Conversely, ...
  zh: OmniQuad 是一种将 mecanum 轮与腿式运动结合的新型轮腿混合机器人，由 Francesco Iotti、Alok Ranjan、Franco Angelini 和 Manolo Garabini 提出。其核心贡献在于设计了集成
    mecanum 轮的定制轮足，并基于 EM-Act 执行器完成整机装配与配套控制方案，从而实现全向移动能力。作者通过室内与室外环境中的实验评估了该机器人的性能。
  ko: Combining wheeled and legged locomotion within a single robotic platform offers the potential to harness the advantages
    of both systems. The development of such hybrid systems remains an active area of research. While legged robots exhibit
    remarkable adaptability for traversing uneven and rugged terrains, their relatively low speed limits their practicality
    in indoor environments. Conversely, ...
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
- wheeled_legged_robot
- mecanum_wheels
- omnidirectional_mobility
- hybrid_locomotion
- robot_design
- em_act_actuators
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.38502);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.38502 OmniQuad: a Wheeled-Legged Hybrid Robot with Omnidirectional Wheels'
  url: https://arxiv.org/abs/2610.38502
  date: '2026-10-28'
  accessed_at: '2026-11-02'
---

## 概述

该研究针对腿式机器人在室内环境中速度偏低、轮式机器人难以跨越台阶等障碍的互补性局限，提出轮腿混合平台 OmniQuad。作者首先设计了一种内置 mecanum 轮的定制轮足，使机器人具备全向移动能力，从而在狭窄空间中灵活运动，并能在执行任务时保持朝向不变。整机由这些轮足与 EM-Act 执行器组装而成，研究团队还为其开发了相应的控制方案。最后，作者在室内和室外两种环境中开展实验，对 OmniQuad 的性能进行了评估。

## 核心内容

### 问题背景

轮式与腿式运动各有优势：腿式机器人在崎岖不平地形上适应性强，但速度相对较低，在室内场景中的实用性受限；轮式机器人在平坦表面上效率更高，却在台阶等障碍面前表现不佳。将两者结合于同一平台，有望同时利用两类系统的长处，但此类混合系统的研制仍是活跃的研究方向。

### 方法

- **轮足设计**：作者首先设计了一种定制的轮足，将 mecanum 轮集成其中。mecanum 轮提供全向移动能力，使机器人能够在狭窄空间中敏捷运动，并在执行任务过程中保持一致的朝向，从而提升机动性。
- **整机装配**：机器人由上述轮足与 EM-Act 执行器组合装配而成。
- **控制方案**：作者进一步描述了为 OmniQuad 开发的控制方案，用于对其运动进行调控。

### 实验设置

作者在室内和室外两种环境中开展了实验试验，以评估 OmniQuad 的性能。

### 结论

OmniQuad 通过 mecanum 轮与腿式运动的结合，兼顾了全向机动性与地形适应性的潜力；摘要层面给出的验证方式为室内外实验评估，未报告具体量化结果。

## Overview

Combining wheeled and legged locomotion within a single robotic platform offers the potential to harness the advantages of both systems. The development of such hybrid systems remains an active area of research. While legged robots exhibit remarkable adaptability for traversing uneven and rugged terrains, their relatively low speed limits their practicality in indoor environments. Conversely, wheeled robots demonstrate higher efficiency on flat surfaces but often encounter difficulties when navigating obstacles such as steps. This paper introduces OmniQuad, a novel hybrid robot that integrates mecanum wheels with legged locomotion to exploit the benefits of both modalities. Mecanum wheels provide omnidirectional mobility, enhancing the robot's manoeuvrability by enabling agile movement in confined spaces and the ability to maintain a consistent orientation during task execution. In this work, we first present the design of a custom wheeled-foot featuring mecanum wheels. Subsequently, we describe the complete robot assembly, comprising these wheeled feet and EM-Act actuators. Finally, we detail the control scheme developed to govern the OmniQuad and evaluate its performance through experimental trials conducted in both indoor and outdoor environments.

## 参考
- https://arxiv.org/abs/2610.38502
