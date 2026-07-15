---
$id: ent_benchmark_libero
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: benchmark
names:
  en: LIBERO
  zh: LIBERO
  ko: LIBERO
summary:
  en: A benchmark and dataset for learning library-generalizable robot manipulation skills from short-horizon tabletop tasks
    with procedural object and scene variations.
  zh: 一个用于从短程桌面任务中学习可泛化机器人操作技能的基准与数据集，支持程序化的物体与场景变化。
  ko: 프로시저적 객체 및 장면 변화를 가진 단기 테이블탑 작업에서 라이브러리 일반화 가능한 로봇 조작 기술을 학습하기 위한 벤치마크 및 데이터셋.
domains:
- 09_data_datasets
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- robot_learning
- vla
- tabletop
- benchmark
- dataset
- short_horizon
- generalization
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: high
  notes: Scope confirmed by original NeurIPS 2023 paper and Wang et al. 2026 VLA survey. Body backfilled from entity metadata
    by scripts/backfill_critical_entities.py.
sources:
- id: src_libero_paper
  type: paper
  title: 'LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning'
  url: https://arxiv.org/abs/2304.13470
  date: '2023-04-26'
  accessed_at: '2026-06-22'
- id: src_libero_code
  type: website
  title: LIBERO GitHub Repository
  url: https://github.com/Lifelong-Robot-Learning/LIBERO
  date: '2023-04-26'
  accessed_at: '2026-06-22'
related_entities:
- id: ent_paper_wang_vla_survey_2026
  relationship: cites
  description:
    en: Wang et al. 2026 survey cites LIBERO as a representative short-horizon tabletop VLA benchmark.
    zh: Wang 等人 2026 综述将 LIBERO 引用为代表性短程桌面 VLA 基准。
    ko: Wang et al. 2026 서베이는 LIBERO를 대표적인 단기 테이블탑 VLA 벤치마크로 인용함.
theoretical_depth:
- system
---
## 概述
一个用于从短程桌面任务中学习可泛化机器人操作技能的基准与数据集，支持程序化的物体与场景变化。

## 核心内容
### LIBERO的定义与定位
LIBERO属于 **benchmark** 类型，英文名称为 *LIBERO*。
一个用于从短程桌面任务中学习可泛化机器人操作技能的基准与数据集，支持程序化的物体与场景变化。

### LIBERO的关键信息
以下整理了关于LIBERO的详细说明，供中英文读者参考。

## 抽象

> **生活实例**：它就像一组带随机道具变化的桌面小游戏——每次物体的位置和类型略有不同，用来测试学习者能不能把学到的技能快速迁移到新场景。

> **自然语言逻辑**：LIBERO 是一个面向终身机器人学习的基准与数据集，提供主题化任务套件和程序化变化的桌面场景；它主要用于评估短程操作任务的泛化能力，是研究机器人学习策略迁移与持续学习的重要受控测试平台。

## Overview

LIBERO is a benchmark for lifelong robot learning that provides multiple task suites with shared object sets and procedurally varied scenes. It is frequently used to evaluate generalization in short-horizon tabletop manipulation.

## Key Characteristics

- **Task libraries**: organized into themed task suites (e.g., spatial reasoning, object manipulation).
- **Procedural variation**: object types, positions, and scene configurations are randomized.
- **Short-horizon**: tasks are atomic and completed in a small number of steps.
- **Dual use**: often used both as a training dataset and as an evaluation benchmark.

## Limitations

- Confined to tabletop settings with limited environmental diversity.
- Does not test locomotion, whole-body coordination, or long-horizon composition.

## Relevance to Humanoid Robotics

LIBERO is a useful controlled benchmark for manipulation skill learning, but humanoid applications will require extending similar evaluation to standing, walking, and bimanual whole-body tasks.

## 参考
- [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2304.13470)
- [LIBERO GitHub Repository](https://github.com/Lifelong-Robot-Learning/LIBERO)

LIBERO的相关技术仍在快速发展。从系统科学角度看，它与其他benchmark相互耦合，共同决定了人形机器人的整体性能。深入理解其原理、边界条件与工程约束，是将实验室样机转化为可量产产品的必要环节。

