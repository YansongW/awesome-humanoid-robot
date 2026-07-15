---
$id: ent_benchmark_humanoidbench
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: benchmark
names:
  en: HumanoidBench
  zh: HumanoidBench
  ko: HumanoidBench
summary:
  en: A simulated benchmark for whole-body humanoid locomotion and manipulation based on the Unitree H1 robot, providing over
    40 tasks for controlled comparison of VLA and control algorithms.
  zh: 一个基于 Unitree H1 机器人的全身人形运动与操作仿真基准，提供 40 余项任务用于 VLA 与控制算法的受控比较。
  ko: Unitree H1 로봇을 기반으로 한 전신 휨로봇 로코모션 및 조작 시뮬레이션 벤치마크로, VLA 및 제어 알고리즘의 통제된 비교를 위해 40개 이상의 작업을 제공함.
domains:
- 07_ai_models_algorithms
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- manipulation
- simulation
- benchmark
- vla
- whole_body_control
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: high
  notes: Paper and code repository retrieved from arXiv and GitHub; scope confirmed by Wang et al. 2026 VLA survey. Body backfilled
    from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_humanoidbench_paper
  type: paper
  title: 'HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation'
  url: https://arxiv.org/abs/2403.10506
  date: '2024-03-15'
  accessed_at: '2026-06-22'
- id: src_humanoidbench_code
  type: website
  title: HumanoidBench GitHub Repository
  url: https://github.com/carlosferrazza/humanoid-bench
  date: '2024-03-15'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_paper_wang_vla_survey_2026
  relationship: cites
  description:
    en: Wang et al. 2026 survey discusses HumanoidBench as a simulation benchmark for whole-body VLA.
    zh: Wang 等人 2026 综述将 HumanoidBench 作为全身 VLA 仿真基准进行讨论。
    ko: Wang et al. 2026 서베이는 HumanoidBench를 전신 VLA 시뮬레이션 벤치마크로 논의함.
theoretical_depth:
- system
---
## 概述
一个基于 Unitree H1 机器人的全身人形运动与操作仿真基准，提供 40 余项任务用于 VLA 与控制算法的受控比较。

## 核心内容
### HumanoidBench的定义与定位
HumanoidBench属于 **benchmark** 类型，英文名称为 *HumanoidBench*。
一个基于 Unitree H1 机器人的全身人形运动与操作仿真基准，提供 40 余项任务用于 VLA 与控制算法的受控比较。

### HumanoidBench的关键信息
以下整理了关于HumanoidBench的详细说明，供中英文读者参考。

## 抽象

> **生活实例**：它就像为一个标准虚拟运动员设置的综合性障碍赛——既要跑步、跳跃，又要弯腰搬东西、伸手够物，用来比较不同“大脑”控制下的全身表现。

> **自然语言逻辑**：HumanoidBench 是基于 Unitree H1 形态构建的仿真基准，包含 40 多项全身运动与操作任务；它为人形机器人 VLA 和控制算法提供统一的受控比较环境，帮助研究者在投入真实硬件前验证和筛选策略。

## Overview

HumanoidBench provides a standardized simulation environment for evaluating algorithms that control a full humanoid body. It is built around the Unitree H1 morphology and includes tasks that require locomotion, manipulation, or both.

## Key Characteristics

- **Whole-body tasks**: evaluates policies that must coordinate legs, torso, arms, and hands.
- **Task diversity**: over 40 tasks spanning locomotion, reaching, object manipulation, and loco-manipulation.
- **Controlled comparison**: same robot model and environment parameters make cross-algorithm comparisons meaningful.
- **Sim-to-real relevance**: tasks are designed to isolate capabilities that matter for real humanoid deployment.

## Limitations

- It is simulation-only; real-world transfer remains an open challenge.
- The action space and morphology are tied to Unitree H1, limiting direct generalization to other humanoids.

## Relevance to Humanoid Robotics

HumanoidBench is one of the few benchmarks that explicitly targets whole-body humanoid control. It is a key tool for developing and comparing VLA policies before expensive hardware deployment.

## 参考
- [HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation](https://arxiv.org/abs/2403.10506)
- [HumanoidBench GitHub Repository](https://github.com/carlosferrazza/humanoid-bench)

HumanoidBench的相关技术仍在快速发展。从系统科学角度看，它与其他benchmark相互耦合，共同决定了人形机器人的整体性能。深入理解其原理、边界条件与工程约束，是将实验室样机转化为可量产产品的必要环节。

