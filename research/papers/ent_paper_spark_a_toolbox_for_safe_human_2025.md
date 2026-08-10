---
$id: ent_paper_spark_a_toolbox_for_safe_human_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation'
  zh: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation'
  ko: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation'
summary:
  en: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: SPARK 是一个面向人形机器人安全自主与遥操作的综合工具箱，由智能控制实验室于 2025 年提出。其核心贡献在于提供模块化、可组合的安全控制框架，支持从仿真到真实硬件的快速部署，并兼容 Apple Vision Pro 与 Motion
    Capture System 等外部传感器。该工具箱通过可配置的安全准则与灵敏度级别，帮助用户优化安全与性能的平衡。
  ko: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation is a 2025 work on loco-manipulation and whole-body-control
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
- spark
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.03132v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (944 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation (arXiv)'
  url: https://arxiv.org/abs/2502.03132
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'SPARK: A Toolbox for Safe Humanoid Autonomy and Teleoperation project page'
  url: https://intelligent-control-lab.github.io/spark/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
SPARK（Safe Protective and Assistive Robot Kit）旨在解决人形机器人在复杂环境交互中因物理结构带来的安全风险。它作为一个模块化工具箱，集成了最先进的安全控制算法，允许用户灵活配置安全准则与灵敏度，以在安全与性能之间取得最佳平衡。为加速研究，SPARK 提供了涵盖多种环境、任务与机器人模型的仿真基准，并支持将合成安全控制器快速部署到真实硬件上。在硬件部署方面，SPARK 支持 Apple Vision Pro 或 Motion Capture System 作为外部传感器，同时提供接口以无缝集成其他硬件配置。论文通过仿真实验与 Unitree G1 人形机器人的案例研究展示了 SPARK 的能力，其开源代码已公开。

## 核心内容
### 方法
SPARK 采用模块化与可组合的机器人控制框架，将安全控制算法作为独立组件集成。用户可通过配置安全准则与灵敏度级别，动态调整安全与性能的权衡。该工具箱支持从仿真到真实硬件的无缝迁移，并兼容多种外部传感器（如 Apple Vision Pro 与 Motion Capture System），同时提供通用接口以适配其他硬件。

### 实验设置
- **仿真基准**：在多种环境、任务与机器人模型上对比不同安全方法的表现。
- **硬件部署**：以 Unitree G1 人形机器人作为真实平台，通过 Apple Vision Pro 或 Motion Capture System 提供外部感知输入。
- **案例研究**：结合仿真实验与真实机器人实验，验证 SPARK 在全身控制与移动操作任务中的安全性能。

### 关键数字与结论
- SPARK 通过可配置的安全准则，显著降低了人形机器人在复杂环境中的碰撞风险。
- 在 Unitree G1 上的案例研究显示，SPARK 能够有效平衡安全与任务完成效率。
- 开源代码已发布，便于社区复现与扩展。

### 结论
SPARK 为人形机器人安全研究提供了一个统一、可扩展的工具箱，通过模块化设计、仿真基准与硬件兼容性，加速了安全控制算法的开发与部署。用户可借助 SPARK 显著提升人形系统的安全性，并推动相关研究进展。

## Overview
This paper introduces the Safe Protective and Assistive Robot Kit (SPARK), a comprehensive benchmark designed to ensure safety in humanoid autonomy and teleoperation. Humanoid robots pose significant safety risks due to their physical capabilities of interacting with complex environments. The physical structures of humanoid robots further add complexity to the design of general safety solutions. To facilitate safe deployment of complex robot systems, SPARK can be used as a toolbox that comes with state-of-the-art safe control algorithms in a modular and composable robot control framework. Users can easily configure safety criteria and sensitivity levels to optimize the balance between safety and performance. To accelerate humanoid safety research and development, SPARK provides simulation benchmarks that compare safety approaches in a variety of environments, tasks, and robot models. Furthermore, SPARK allows quick deployment of synthesized safe controllers on real robots. For hardware deployment, SPARK supports Apple Vision Pro (AVP) or a Motion Capture System as external sensors, while offering interfaces for seamless integration with alternative hardware setups at the same time. This paper demonstrates SPARK's capability with both simulation experiments and case studies with a Unitree G1 humanoid robot. Leveraging these advantages of SPARK, users and researchers can significantly improve the safety of their humanoid systems as well as accelerate relevant research. The open source code is available at: https://github.com/intelligent-control-lab/spark.

## 参考
- http://arxiv.org/abs/2502.03132v3

## 개요
SPARK(Safe Protective and Assistive Robot Kit)는 복잡한 환경 상호작용에서 물리적 구조로 인해 발생하는 휴머노이드 로봇의 안전 위험을 해결하기 위해 설계되었습니다. 이는 모듈식 툴킷으로, 최첨단 안전 제어 알고리즘을 통합하여 사용자가 안전 기준과 민감도를 유연하게 구성함으로써 안전과 성능 사이의 최적 균형을 달성할 수 있게 합니다. 연구를 가속화하기 위해 SPARK는 다양한 환경, 작업 및 로봇 모델을 포괄하는 시뮬레이션 벤치마크를 제공하며, 합성 안전 컨트롤러를 실제 하드웨어에 신속하게 배포할 수 있도록 지원합니다. 하드웨어 배포 측면에서 SPARK는 Apple Vision Pro 또는 Motion Capture System을 외부 센서로 지원하며, 다른 하드웨어 구성과의 원활한 통합을 위한 인터페이스도 제공합니다. 논문은 시뮬레이션 실험과 Unitree G1 휴머노이드 로봇 사례 연구를 통해 SPARK의 능력을 입증하며, 오픈소스 코드가 공개되었습니다.

## 핵심 내용
### 방법
SPARK는 모듈식 및 조합 가능한 로봇 제어 프레임워크를 채택하여 안전 제어 알고리즘을 독립적인 구성 요소로 통합합니다. 사용자는 안전 기준과 민감도 수준을 구성하여 안전과 성능 간의 균형을 동적으로 조정할 수 있습니다. 이 툴킷은 시뮬레이션에서 실제 하드웨어로의 원활한 전환을 지원하며, 다양한 외부 센서(예: Apple Vision Pro 및 Motion Capture System)와 호환되고 다른 하드웨어에 적응할 수 있는 범용 인터페이스를 제공합니다.

### 실험 설정
- **시뮬레이션 벤치마크**: 다양한 환경, 작업 및 로봇 모델에서 서로 다른 안전 방법의 성능을 비교합니다.
- **하드웨어 배포**: Unitree G1 휴머노이드 로봇을 실제 플랫폼으로 사용하며, Apple Vision Pro 또는 Motion Capture System을 통해 외부 인식 입력을 제공합니다.
- **사례 연구**: 시뮬레이션 실험과 실제 로봇 실험을 결합하여 전신 제어 및 이동 조작 작업에서 SPARK의 안전 성능을 검증합니다.

### 주요 수치 및 결론
- SPARK는 구성 가능한 안전 기준을 통해 복잡한 환경에서 휴머노이드 로봇의 충돌 위험을 크게 줄입니다.
- Unitree G1에서의 사례 연구는 SPARK가 안전과 작업 완료 효율성을 효과적으로 균형 잡을 수 있음을 보여줍니다.
- 오픈소스 코드가 공개되어 커뮤니티의 재현 및 확장을 용이하게 합니다.

### 결론
SPARK는 휴머노이드 로봇 안전 연구를 위한 통합적이고 확장 가능한 툴킷을 제공하며, 모듈식 설계, 시뮬레이션 벤치마크 및 하드웨어 호환성을 통해 안전 제어 알고리즘의 개발과 배포를 가속화합니다. 사용자는 SPARK를 통해 휴머노이드 시스템의 안전성을 크게 향상시키고 관련 연구 발전을 촉진할 수 있습니다.
