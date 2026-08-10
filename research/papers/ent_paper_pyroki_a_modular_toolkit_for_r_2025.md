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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.03728v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (797 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2505.03728v1

## 개요
PyRoki는 연구자들이 개발한 것으로, 로봇 운동 최적화에서 다중 목표(예: 자세 오차, 속도, 충돌 또는 인간 시연 모방)의 유연성 문제를 해결하기 위해 설계되었습니다. 핵심 설계는 모듈화와 크로스 플랫폼입니다: 사용자는 인터페이스를 통해 운동학 변수와 비용 함수를 사용자 정의할 수 있으며, 기본 최적화기는 비선형 최소제곱 문제를 효율적으로 해결합니다. GPU 가속만 지원하는 cuRobo와 달리, PyRoki는 CPU, GPU 및 TPU에서 기본적으로 실행되며, 운동 재지정 및 계획 사례를 통해 모듈화의 장점을 보여줍니다. 벤치마크 테스트에 따르면 PyRoki는 최적화 속도가 cuRobo보다 1.4-1.7배 빠르며 더 낮은 오차로 수렴할 수 있습니다.

## 핵심 내용
### 설계 및 구현
- **모듈화 아키텍처**: PyRoki는 확장 가능한 인터페이스를 제공하여 사용자가 운동학 변수(예: 관절 각도, 말단 자세)와 다양한 비용 함수(예: 자세 오차, 속도, 충돌 회피, 인간 시연과의 유사성)를 지정할 수 있습니다.
- **최적화기**: 효율적인 비선형 최소제곱 솔버를 기반으로 하며, 다중 목표 공동 최적화를 지원합니다.
- **크로스 플랫폼 지원**: 최적화 계산은 CPU, GPU 및 TPU에서 기본적으로 실행되며 추가 적응이 필요 없습니다.

### 사례 연구
- **운동 재지정**: 인간 시연의 운동을 로봇 모델에 매핑하여 사용자 정의 비용 함수에 대한 모듈화 인터페이스의 유연성을 검증합니다.
- **운동 계획**: 복잡한 작업에서 자세 정밀도와 충돌 회피를 동시에 최적화하여 다중 목표 최적화의 실용성을 보여줍니다.

### 벤치마크 테스트
- **비교 대상**: cuRobo(기존 GPU 가속 역운동학 라이브러리).
- **성능 지표**:
  - 최적화 속도: PyRoki는 cuRobo보다 1.4-1.7배 빠릅니다.
  - 수렴 오차: PyRoki는 동일한 반복 횟수에서 더 낮은 최종 오차에 도달합니다.
- **하드웨어 환경**: 테스트는 NVIDIA GPU 및 Google TPU에서 완료되어 크로스 플랫폼 일관성을 검증했습니다.

### 결론
PyRoki는 모듈화 설계와 크로스 플랫폼 최적화를 통해 로봇 운동학 문제에 더 유연하고 효율적인 솔루션을 제공하며, 특히 휴머노이드 로봇의 전신 제어 및 조작 작업에 적합합니다.
