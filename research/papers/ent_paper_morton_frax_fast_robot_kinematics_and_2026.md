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

## Overview
In robot control, planning, and learning, there is a need for rigid-body dynamics libraries that are highly performant, easy to use, and compatible with CPUs and accelerators. While existing libraries often excel at either low-latency CPU execution or high-throughput GPU workloads, few provide a unified framework that targets multiple architectures without compromising performance or ease-of-use. To address this, we introduce frax, a JAX-based library for robot kinematics and dynamics, providing a high-performance, pure-Python interface across CPU, GPU, and TPU. Via a fully-vectorized approach to robot dynamics, frax enables efficient real-time control and parallelization, while supporting automatic differentiation for optimization-based methods. On CPU, frax achieves low-microsecond computation times suitable for kilohertz control rates, outperforming common libraries in Python and approaching optimized C++ implementations. On GPU, the same code scales to thousands of instances, reaching upwards of 100 million dynamics evaluations per second. We validate performance on a Franka Panda manipulator and a Unitree G1 humanoid, and release frax as an open-source library.

## Content
In robot control, planning, and learning, there is a need for rigid-body dynamics libraries that are highly performant, easy to use, and compatible with CPUs and accelerators. While existing libraries often excel at either low-latency CPU execution or high-throughput GPU workloads, few provide a unified framework that targets multiple architectures without compromising performance or ease-of-use. To address this, we introduce frax, a JAX-based library for robot kinematics and dynamics, providing a high-performance, pure-Python interface across CPU, GPU, and TPU. Via a fully-vectorized approach to robot dynamics, frax enables efficient real-time control and parallelization, while supporting automatic differentiation for optimization-based methods. On CPU, frax achieves low-microsecond computation times suitable for kilohertz control rates, outperforming common libraries in Python and approaching optimized C++ implementations. On GPU, the same code scales to thousands of instances, reaching upwards of 100 million dynamics evaluations per second. We validate performance on a Franka Panda manipulator and a Unitree G1 humanoid, and release frax as an open-source library.

## 개요
로봇 제어, 계획 및 학습 분야에서는 높은 성능, 사용 편의성, CPU 및 가속기 호환성을 갖춘 강체 동역학 라이브러리가 필요합니다. 기존 라이브러리는 종종 저지연 CPU 실행 또는 고처리량 GPU 워크로드 중 하나에 특화되어 있지만, 성능이나 사용 편의성을 저하시키지 않으면서 여러 아키텍처를 지원하는 통합 프레임워크를 제공하는 경우는 드뭅니다. 이를 해결하기 위해, 우리는 JAX 기반의 로봇 기구학 및 동역학 라이브러리인 frax를 소개합니다. frax는 CPU, GPU, TPU에서 고성능 순수 Python 인터페이스를 제공합니다. 완전 벡터화된 로봇 동역학 접근 방식을 통해 frax는 효율적인 실시간 제어 및 병렬화를 가능하게 하며, 최적화 기반 방법을 위한 자동 미분을 지원합니다. CPU에서 frax는 킬로헤르츠 제어 속도에 적합한 마이크로초 단위의 낮은 계산 시간을 달성하여 Python의 일반적인 라이브러리를 능가하고 최적화된 C++ 구현에 근접합니다. GPU에서는 동일한 코드가 수천 개의 인스턴스로 확장되어 초당 1억 회 이상의 동역학 평가를 수행합니다. 우리는 Franka Panda 매니퓰레이터와 Unitree G1 휴머노이드에서 성능을 검증하고, frax를 오픈소스 라이브러리로 공개합니다.

## 핵심 내용
로봇 제어, 계획 및 학습 분야에서는 높은 성능, 사용 편의성, CPU 및 가속기 호환성을 갖춘 강체 동역학 라이브러리가 필요합니다. 기존 라이브러리는 종종 저지연 CPU 실행 또는 고처리량 GPU 워크로드 중 하나에 특화되어 있지만, 성능이나 사용 편의성을 저하시키지 않으면서 여러 아키텍처를 지원하는 통합 프레임워크를 제공하는 경우는 드뭅니다. 이를 해결하기 위해, 우리는 JAX 기반의 로봇 기구학 및 동역학 라이브러리인 frax를 소개합니다. frax는 CPU, GPU, TPU에서 고성능 순수 Python 인터페이스를 제공합니다. 완전 벡터화된 로봇 동역학 접근 방식을 통해 frax는 효율적인 실시간 제어 및 병렬화를 가능하게 하며, 최적화 기반 방법을 위한 자동 미분을 지원합니다. CPU에서 frax는 킬로헤르츠 제어 속도에 적합한 마이크로초 단위의 낮은 계산 시간을 달성하여 Python의 일반적인 라이브러리를 능가하고 최적화된 C++ 구현에 근접합니다. GPU에서는 동일한 코드가 수천 개의 인스턴스로 확장되어 초당 1억 회 이상의 동역학 평가를 수행합니다. 우리는 Franka Panda 매니퓰레이터와 Unitree G1 휴머노이드에서 성능을 검증하고, frax를 오픈소스 라이브러리로 공개합니다.
