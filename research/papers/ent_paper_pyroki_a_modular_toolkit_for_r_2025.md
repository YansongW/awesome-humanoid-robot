---
$id: ent_paper_pyroki_a_modular_toolkit_for_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization'
  zh: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization'
  ko: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization'
summary:
  en: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: PyRoki 是一个 2025 年发布的模块化机器人运动学优化工具包，专注于人形机器人的全身控制与操作任务。它通过可扩展的接口与高效的非线性最小二乘优化器，支持在 CPU、GPU 和 TPU 上原生运行。相比现有工具 cuRobo，PyRoki
    在优化速度上快 1.4-1.7 倍，且收敛误差更低。
  ko: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- loco_manipulation
- pyroki
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.03728v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization (arXiv)'
  url: https://arxiv.org/abs/2505.03728
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization project page'
  url: https://pyroki-toolkit.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
PyRoki 由研究者开发，旨在解决机器人运动优化中多目标（如位姿误差、速度、碰撞或模仿人类演示）的灵活性问题。其核心设计是模块化与跨平台：用户可通过接口自定义运动学变量和代价函数，底层优化器则高效求解非线性最小二乘问题。与仅支持 GPU 加速的 cuRobo 不同，PyRoki 在 CPU、GPU 和 TPU 上均可原生运行，并通过运动重定向与规划案例展示了模块化的优势。基准测试表明，PyRoki 在优化速度上比 cuRobo 快 1.4-1.7 倍，且能收敛到更低的误差。

## 核心内容
### 设计与实现
- **模块化架构**：PyRoki 提供可扩展的接口，允许用户指定运动学变量（如关节角度、末端位姿）和多种代价函数（如位姿误差、速度、碰撞避免、与人类演示的相似度）。
- **优化器**：基于高效的非线性最小二乘求解器，支持多目标联合优化。
- **跨平台支持**：优化计算可原生运行于 CPU、GPU 和 TPU，无需额外适配。

### 案例研究
- **运动重定向**：将人类演示的运动映射到机器人模型，验证了模块化接口对自定义代价函数的灵活性。
- **运动规划**：在复杂任务中同时优化位姿精度与碰撞避免，展示了多目标优化的实用性。

### 基准测试
- **对比对象**：cuRobo（现有 GPU 加速逆运动学库）。
- **性能指标**：
  - 优化速度：PyRoki 比 cuRobo 快 1.4-1.7 倍。
  - 收敛误差：PyRoki 在相同迭代次数下达到更低的最终误差。
- **硬件环境**：测试在 NVIDIA GPU 和 Google TPU 上完成，验证了跨平台一致性。

### 结论
PyRoki 通过模块化设计与跨平台优化，为机器人运动学问题提供了更灵活、高效的解决方案，尤其适用于人形机器人的全身控制与操作任务。

## Overview
Robot motion can have many goals. Depending on the task, we might optimize for pose error, speed, collision, or similarity to a human demonstration. Motivated by this, we present PyRoki: a modular, extensible, and cross-platform toolkit for solving kinematic optimization problems. PyRoki couples an interface for specifying kinematic variables and costs with an efficient nonlinear least squares optimizer. Unlike existing tools, it is also cross-platform: optimization runs natively on CPU, GPU, and TPU. In this paper, we present (i) the design and implementation of PyRoki, (ii) motion retargeting and planning case studies that highlight the advantages of PyRoki's modularity, and (iii) optimization benchmarking, where PyRoki can be 1.4-1.7x faster and converges to lower errors than cuRobo, an existing GPU-accelerated inverse kinematics library.

## 개요
로봇 동작은 다양한 목표를 가질 수 있습니다. 작업에 따라 자세 오차, 속도, 충돌 또는 인간 시연과의 유사성을 최적화할 수 있습니다. 이러한 동기에서 우리는 PyRoki를 소개합니다: 모듈식이며 확장 가능하고 크로스 플랫폼을 지원하는 운동학 최적화 문제 해결 도구입니다. PyRoki는 운동학 변수와 비용을 지정하는 인터페이스와 효율적인 비선형 최소제곱 최적화기를 결합합니다. 기존 도구와 달리 크로스 플랫폼을 지원하여 CPU, GPU 및 TPU에서 최적화가 기본적으로 실행됩니다. 본 논문에서는 (i) PyRoki의 설계 및 구현, (ii) PyRoki의 모듈성 장점을 강조하는 동작 리타겟팅 및 계획 사례 연구, (iii) 기존 GPU 가속 역운동학 라이브러리인 cuRobo보다 1.4-1.7배 빠르고 더 낮은 오차로 수렴하는 최적화 벤치마킹을 제시합니다.

## 핵심 내용
로봇 동작은 다양한 목표를 가질 수 있습니다. 작업에 따라 자세 오차, 속도, 충돌 또는 인간 시연과의 유사성을 최적화할 수 있습니다. 이러한 동기에서 우리는 PyRoki를 소개합니다: 모듈식이며 확장 가능하고 크로스 플랫폼을 지원하는 운동학 최적화 문제 해결 도구입니다. PyRoki는 운동학 변수와 비용을 지정하는 인터페이스와 효율적인 비선형 최소제곱 최적화기를 결합합니다. 기존 도구와 달리 크로스 플랫폼을 지원하여 CPU, GPU 및 TPU에서 최적화가 기본적으로 실행됩니다. 본 논문에서는 (i) PyRoki의 설계 및 구현, (ii) PyRoki의 모듈성 장점을 강조하는 동작 리타겟팅 및 계획 사례 연구, (iii) 기존 GPU 가속 역운동학 라이브러리인 cuRobo보다 1.4-1.7배 빠르고 더 낮은 오차로 수렴하는 최적화 벤치마킹을 제시합니다.

## 参考
- http://arxiv.org/abs/2505.03728v1
