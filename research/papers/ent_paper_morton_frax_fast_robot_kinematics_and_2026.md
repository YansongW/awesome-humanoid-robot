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
  en: frax is a pure-Python JAX library for fully-vectorized robot kinematics and dynamics that runs on CPU, GPU, and TPU,
    achieving low-microsecond CPU latency and over 100 million dynamics evaluations per second on GPU.
  zh: frax 是一个纯 Python 的 JAX 库，用于在 CPU、GPU 和 TPU 上实现完全向量化的机器人运动学与动力学计算，在 CPU 上达到微秒级延迟，在 GPU 上每秒可完成超过一亿次动力学评估。
  ko: frax는 CPU, GPU, TPU에서 동작하는 완전히 벡터화된 로봇 운동학 및 동역학을 위한 순수 Python JAX 라이브러리로, CPU에서는 마이크로초 단위 지연을, GPU에서는 초당 1억 번 이상의 동역학
    평가를 달성한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.04310v2.
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
## 概述
In robot control, planning, and learning, there is a need for rigid-body dynamics libraries that are highly performant, easy to use, and compatible with CPUs and accelerators. While existing libraries often excel at either low-latency CPU execution or high-throughput GPU workloads, few provide a unified framework that targets multiple architectures without compromising performance or ease-of-use. To address this, we introduce frax, a JAX-based library for robot kinematics and dynamics, providing a high-performance, pure-Python interface across CPU, GPU, and TPU. Via a fully-vectorized approach to robot dynamics, frax enables efficient real-time control and parallelization, while supporting automatic differentiation for optimization-based methods. On CPU, frax achieves low-microsecond computation times suitable for kilohertz control rates, outperforming common libraries in Python and approaching optimized C++ implementations. On GPU, the same code scales to thousands of instances, reaching upwards of 100 million dynamics evaluations per second. We validate performance on a Franka Panda manipulator and a Unitree G1 humanoid, and release frax as an open-source library.

## 核心内容
In robot control, planning, and learning, there is a need for rigid-body dynamics libraries that are highly performant, easy to use, and compatible with CPUs and accelerators. While existing libraries often excel at either low-latency CPU execution or high-throughput GPU workloads, few provide a unified framework that targets multiple architectures without compromising performance or ease-of-use. To address this, we introduce frax, a JAX-based library for robot kinematics and dynamics, providing a high-performance, pure-Python interface across CPU, GPU, and TPU. Via a fully-vectorized approach to robot dynamics, frax enables efficient real-time control and parallelization, while supporting automatic differentiation for optimization-based methods. On CPU, frax achieves low-microsecond computation times suitable for kilohertz control rates, outperforming common libraries in Python and approaching optimized C++ implementations. On GPU, the same code scales to thousands of instances, reaching upwards of 100 million dynamics evaluations per second. We validate performance on a Franka Panda manipulator and a Unitree G1 humanoid, and release frax as an open-source library.

## 参考
- http://arxiv.org/abs/2604.04310v2

