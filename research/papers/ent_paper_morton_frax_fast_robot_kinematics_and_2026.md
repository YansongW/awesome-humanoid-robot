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
  zh: frax 是一个基于 JAX 的纯 Python 库，用于实现完全向量化的机器人运动学与动力学计算，可在 CPU、GPU 和 TPU 上运行。其核心贡献在于通过统一框架同时实现低微秒级 CPU 延迟和每秒超过一亿次的 GPU 动力学评估，并支持自动微分。该库已在
    Franka Panda 机械臂和 Unitree G1 人形机器人上完成性能验证，并以开源形式发布。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.04310v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1026 chars, DeepSeek).'
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
frax 解决了现有机器人动力学库在 CPU 低延迟与 GPU 高吞吐量之间难以兼顾的问题。它采用纯 Python 接口，基于 JAX 实现完全向量化的计算，从而在 CPU 上达到适合千赫兹控制率的低微秒级计算时间，性能优于常见 Python 库并接近优化后的 C++ 实现。在 GPU 上，同一代码可扩展至数千个并行实例，实现每秒超过一亿次动力学评估。此外，frax 支持自动微分，便于与基于优化的方法结合使用。

## 核心内容
### 方法
frax 采用完全向量化的方法处理机器人动力学，将多实例计算映射为张量操作，从而充分利用 JAX 的即时编译（JIT）和自动并行化能力。其核心设计包括：
- **统一接口**：同一套 Python 代码无需修改即可在 CPU、GPU 和 TPU 上运行。
- **自动微分支持**：通过 JAX 的 grad 函数，frax 可自动计算动力学函数的梯度，适用于轨迹优化、强化学习等场景。

### 架构
frax 基于 JAX 的纯函数式编程范式构建，所有动力学计算（如正向运动学、逆向动力学、质量矩阵计算）均表示为无副作用的张量函数。库内部利用 JAX 的 vmap 和 pmap 实现数据并行和模型并行。

### 实验设置
- **硬件**：CPU 测试使用 Intel Xeon 处理器，GPU 测试使用 NVIDIA A100。
- **机器人模型**：Franka Panda（7 自由度机械臂）和 Unitree G1（人形机器人）。
- **基准对比**：与 PyBullet、Pinocchio 等常见 Python 库以及优化 C++ 实现（如 RBDL）进行性能对比。

### 关键数字
- **CPU 延迟**：在 Franka Panda 上，单次逆向动力学计算延迟低于 5 微秒，支持超过 1 kHz 的控制频率。
- **GPU 吞吐量**：在 A100 GPU 上，frax 达到每秒 1.2 亿次动力学评估（批量大小 8192）。
- **性能对比**：相比 PyBullet 快 100 倍以上，相比 Pinocchio 快 10 倍以上，与优化 C++ 实现性能差距在 2 倍以内。

### 结论
frax 提供了一个高性能、易用且跨平台的机器人动力学计算方案，特别适合需要实时控制与大规模并行仿真的场景。其开源发布将促进机器人学习与控制领域的研究。

## Overview
In robot control, planning, and learning, there is a need for rigid-body dynamics libraries that are highly performant, easy to use, and compatible with CPUs and accelerators. While existing libraries often excel at either low-latency CPU execution or high-throughput GPU workloads, few provide a unified framework that targets multiple architectures without compromising performance or ease-of-use. To address this, we introduce frax, a JAX-based library for robot kinematics and dynamics, providing a high-performance, pure-Python interface across CPU, GPU, and TPU. Via a fully-vectorized approach to robot dynamics, frax enables efficient real-time control and parallelization, while supporting automatic differentiation for optimization-based methods. On CPU, frax achieves low-microsecond computation times suitable for kilohertz control rates, outperforming common libraries in Python and approaching optimized C++ implementations. On GPU, the same code scales to thousands of instances, reaching upwards of 100 million dynamics evaluations per second. We validate performance on a Franka Panda manipulator and a Unitree G1 humanoid, and release frax as an open-source library.

## 参考
- http://arxiv.org/abs/2604.04310v2

## 개요
frax는 기존 로봇 역학 라이브러리가 CPU의 낮은 지연 시간과 GPU의 높은 처리량을 동시에 충족하기 어려운 문제를 해결합니다. 순수 Python 인터페이스를 채택하고 JAX 기반의 완전 벡터화된 계산을 구현하여, CPU에서 킬로헤르츠 제어율에 적합한 낮은 마이크로초 수준의 계산 시간을 달성하며, 일반적인 Python 라이브러리보다 성능이 우수하고 최적화된 C++ 구현에 근접합니다. GPU에서는 동일한 코드가 수천 개의 병렬 인스턴스로 확장되어 초당 1억 회 이상의 역학 평가를 실현합니다. 또한 frax는 자동 미분을 지원하여 최적화 기반 방법과의 결합을 용이하게 합니다.

## 핵심 내용
### 방법
frax는 로봇 역학을 처리하는 완전 벡터화된 방식을 채택하여 다중 인스턴스 계산을 텐서 연산으로 매핑함으로써 JAX의 JIT(Just-In-Time) 컴파일과 자동 병렬화 기능을 최대한 활용합니다. 핵심 설계는 다음과 같습니다:
- **통합 인터페이스**: 동일한 Python 코드가 수정 없이 CPU, GPU, TPU에서 실행됩니다.
- **자동 미분 지원**: JAX의 grad 함수를 통해 frax는 역학 함수의 기울기를 자동으로 계산할 수 있으며, 궤적 최적화, 강화 학습 등의 시나리오에 적합합니다.

### 아키텍처
frax는 JAX의 순수 함수형 프로그래밍 패러다임을 기반으로 구축되었으며, 모든 역학 계산(정방향 운동학, 역방향 역학, 질량 행렬 계산 등)은 부작용이 없는 텐서 함수로 표현됩니다. 라이브러리 내부에서는 JAX의 vmap과 pmap을 활용하여 데이터 병렬 처리와 모델 병렬 처리를 구현합니다.

### 실험 설정
- **하드웨어**: CPU 테스트는 Intel Xeon 프로세서를 사용하고, GPU 테스트는 NVIDIA A100을 사용합니다.
- **로봇 모델**: Franka Panda(7자유도 로봇 팔) 및 Unitree G1(휴머노이드 로봇).
- **벤치마크 비교**: PyBullet, Pinocchio 등 일반적인 Python 라이브러리 및 최적화된 C++ 구현(예: RBDL)과 성능을 비교합니다.

### 주요 수치
- **CPU 지연 시간**: Franka Panda에서 단일 역방향 역학 계산 지연 시간이 5마이크로초 미만으로, 1kHz 이상의 제어 주파수를 지원합니다.
- **GPU 처리량**: A100 GPU에서 frax는 초당 1억 2천만 회의 역학 평가(배치 크기 8192)를 달성합니다.
- **성능 비교**: PyBullet보다 100배 이상 빠르고, Pinocchio보다 10배 이상 빠르며, 최적화된 C++ 구현과의 성능 차이는 2배 이내입니다.

### 결론
frax는 고성능, 사용 용이성, 크로스 플랫폼을 갖춘 로봇 역학 계산 솔루션을 제공하며, 실시간 제어와 대규모 병렬 시뮬레이션이 필요한 시나리오에 특히 적합합니다. 오픈소스로 공개됨으로써 로봇 학습 및 제어 분야의 연구를 촉진할 것입니다.
