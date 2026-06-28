---
$id: ent_paper_morton_frax_fast_robot_kinematics_and_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'frax: Fast Robot Kinematics and Dynamics in JAX'
  zh: frax：基于 JAX 的快速机器人运动学与动力学库
  ko: 'frax: JAX 기반의 고속 로봇 운동학 및 동역학 라이브러리'
summary:
  en: frax is a pure-Python JAX library for fully-vectorized robot kinematics and
    dynamics that runs on CPU, GPU, and TPU, achieving low-microsecond CPU latency
    and over 100 million dynamics evaluations per second on GPU.
  zh: frax 是一个纯 Python 的 JAX 库，用于在 CPU、GPU 和 TPU 上实现完全向量化的机器人运动学与动力学计算，在 CPU 上达到微秒级延迟，在
    GPU 上每秒可完成超过一亿次动力学评估。
  ko: frax는 CPU, GPU, TPU에서 동작하는 완전히 벡터화된 로봇 운동학 및 동역학을 위한 순수 Python JAX 라이브러리로, CPU에서는
    마이크로초 단위 지연을, GPU에서는 초당 1억 번 이상의 동역학 평가를 달성한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
- tool_equipment
tags:
- jax
- robot_dynamics
- rigid_body_dynamics
- kinematics
- automatic_differentiation
- gpu_acceleration
- vectorized_computation
- unitree_g1
- franka_panda
- real_time_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text verification
    and human review required before promotion to verified.
sources:
- id: src_001
  type: paper
  title: 'frax: Fast Robot Kinematics and Dynamics in JAX'
  url: https://arxiv.org/abs/2604.04310
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

frax is a pure-Python library for robot kinematics and dynamics built on JAX. It targets a unified execution backend across CPU, GPU, and TPU through a fully-vectorized formulation of rigid-body dynamics. The implementation uses an ancestor-mask tree representation to expose fine-grained parallelism and to support just-in-time compilation and automatic differentiation.

The library is positioned for robot control, planning, and learning workflows that require both low-latency single-instance evaluation and high-throughput batch evaluation. The authors report CPU compute times in the low-microsecond range, suitable for kilohertz control loops, while the same code scales to thousands of parallel instances on GPU.

frax is released as open-source software and is validated on two representative systems: a Franka Panda manipulator and a Unitree G1 humanoid.

## Key Contributions

- Pure-Python JAX library for robot kinematics and dynamics on CPU, GPU, and TPU.
- Fully-vectorized rigid-body dynamics algorithms using an ancestor mask for fine-grained parallelism and fast automatic differentiation.
- Low-microsecond CPU controller compute and over 100 million dynamics evaluations per second on GPU for thousands of parallel instances.
- Validation on Franka Panda and Unitree G1 robots with tuned spherized collision models and open-source release.

## Relevance to Humanoid Robotics

frax is directly relevant to humanoid robotics because it is explicitly validated on the Unitree G1, a high-degree-of-freedom humanoid platform. The library supports inverse kinematics and inverse dynamics controllers at low latency, which are core building blocks for humanoid balance, locomotion, and manipulation.

Because frax runs on accelerators and supports automatic differentiation, it is also useful for optimization-based and learning-based humanoid control pipelines that require batched dynamics rollouts or gradient-based policy training.
