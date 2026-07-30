---
$id: ent_paper_softvtbench_a_safety_aware_vis_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SoftVTBench: A Safety-Aware Visuo-Tactile Benchmark for Physically Constrained Robotic Manipulation of Deformable Objects'
  zh: 'SoftVTBench: A Safety-Aware Visuo-Tactile Benchmark for Physically Constrained Robotic Manipulation of Deformable Objects'
  ko: 'SoftVTBench: A Safety-Aware Visuo-Tactile Benchmark for Physically Constrained Robotic Manipulation of Deformable Objects'
summary:
  en: 'arXiv:2607.04234v1 Announce Type: new Abstract: Deformable object manipulation poses challenges beyond task completion:
    successful execution must also maintain safe physical interaction, holding the object stably without slip or drop while
    avoiding excessive deformation. However, existing manipulation benchmarks are predominantly success-oriented and rarely
    evaluate whether a policy remains physically safe throughout execution. We present SoftVTBench, a safety-aware visuo-tactile
    benchmark for physically constrained deformable object manipulation. Built in Isaac Sim with finite-element-simulated
    deformable objects, SoftVTBench provides multi-view RGB observations, RGB tactile sensing with marker motion, proprioception,
    and language instructions, and defines four matched task suites over object type (deformable vs. rigid) and variation
    axis (object vs. spatial). It separately reports Goal Success and Safety Success; the latter additionally requires no
    drop and peak deformation below a calibrated object-specific threshold, measured from policy-hidden privileged Finite
    Element Method (FEM) states. We implement pi0.5-based baselines under this protocol. Experiments show that success-only
    evaluation substantially overstates policy performance, as a large fraction of goal-completing rollouts still violate
    physical safety. Furthermore, incorporating tactile sensing improves Safety Success (e.g., from 21.4% to 35.6% on object-centric
    deformable tasks) and reduces object deformation during execution, while maintaining comparable Goal Success. SoftVTBench
    provides a reproducible benchmark for studying visuo-tactile deformable manipulation under physical interaction constraints.'
  zh: SoftVTBench 是一个面向物理约束下可变形物体操作的安全感知视觉-触觉基准，由研究团队基于 Isaac Sim 构建。它通过有限元模拟的可变形物体，提供多视角 RGB 观测、RGB 触觉传感（含标记运动）、本体感知和语言指令，并分别报告任务成功率和安全成功率。实验表明，仅关注任务成功率会高估策略性能，而引入触觉传感可显著提升安全成功率（例如在物体中心可变形任务中从
    21.4% 提升至 35.6%）。
  ko: 'arXiv:2607.04234v1 Announce Type: new Abstract: Deformable object manipulation poses challenges beyond task completion:
    successful execution must also maintain safe physical interaction, holding the object stably without slip or drop while
    avoiding excessive deformation. However, existing manipulation benchmarks are predominantly success-oriented and rarely
    evaluate whether a policy remains physically safe throughout execution. We present SoftVTBench, a safety-aware visuo-tactile
    benchmark for physically constrained deformable object manipulation. Built in Isaac Sim with finite-element-simulated
    deformable objects, SoftVTBench provides multi-view RGB observations, RGB tactile sensing with marker motion, proprioception,
    and language instructions, and defines four matched task suites over object type (deformable vs. rigid) and variation
    axis (object vs. spatial). It separately reports Goal Success and Safety Success; the latter additionally requires no
    drop and peak deformation below a calibrated object-specific threshold, measured from policy-hidden privileged Finite
    Element Method (FEM) states. We implement pi0.5-based baselines under this protocol. Experiments show that success-only
    evaluation substantially overstates policy performance, as a large fraction of goal-completing rollouts still violate
    physical safety. Furthermore, incorporating tactile sensing improves Safety Success (e.g., from 21.4% to 35.6% on object-centric
    deformable tasks) and reduces object deformation during execution, while maintaining comparable Goal Success. SoftVTBench
    provides a reproducible benchmark for studying visuo-tactile deformable manipulation under physical interaction constraints.'
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
- robotics
- softvtbench
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04234v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'SoftVTBench: A Safety-Aware Visuo-Tactile Benchmark for Physically Constrained Robotic Manipulation of Deformable
    Objects (arXiv)'
  url: https://arxiv.org/abs/2607.04234
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
SoftVTBench 旨在解决现有操作基准主要面向任务完成而忽视物理安全的问题。该基准在 Isaac Sim 中利用有限元方法模拟可变形物体，提供多视角 RGB 图像、RGB 触觉传感（含标记运动）、本体感知和语言指令，并定义了四组匹配任务套件（按物体类型和变化轴划分）。它分别报告目标成功率和安全成功率，其中安全成功率额外要求无掉落且峰值变形低于校准后的物体特定阈值（基于策略隐藏的特权有限元状态测量）。基于 pi0.5 的基线实验表明，仅评估任务成功率会严重高估策略性能，因为大量完成目标的 rollout 仍违反物理安全。此外，融合触觉传感在保持目标成功率的同时，能提升安全成功率并减少执行中的物体变形。

## 核心内容
### 核心问题
可变形物体操作不仅需要完成任务，还必须确保物理交互安全：稳定持握物体（无滑落或掉落），同时避免过度变形。现有基准大多以任务成功为导向，很少评估策略在执行过程中是否保持物理安全。

### SoftVTBench 设计
- **仿真环境**：基于 Isaac Sim 构建，使用有限元方法模拟可变形物体。
- **观测模态**：多视角 RGB 观测、RGB 触觉传感（含标记运动）、本体感知、语言指令。
- **任务套件**：按物体类型（可变形 vs. 刚性）和变化轴（物体 vs. 空间）定义四组匹配任务。
- **评估指标**：
  - **Goal Success**：任务完成成功率。
  - **Safety Success**：在任务完成基础上，额外要求无掉落且峰值变形低于校准后的物体特定阈值（基于策略隐藏的特权有限元状态测量）。

### 实验设置与基线
- **基线模型**：基于 pi0.5 实现。
- **实验协议**：分别报告 Goal Success 和 Safety Success。

### 关键结果
- **仅任务成功率的误导性**：大量完成目标的 rollout 仍违反物理安全，说明仅评估 Goal Success 会严重高估策略性能。
- **触觉传感的贡献**：
  - 在物体中心可变形任务中，Safety Success 从 21.4% 提升至 35.6%。
  - 执行过程中物体变形显著减少。
  - Goal Success 保持可比水平。

### 结论
SoftVTBench 提供了一个可复现的基准，用于研究物理交互约束下的视觉-触觉可变形物体操作，强调了安全评估的必要性和触觉传感的价值。

## Overview
Deformable object manipulation poses challenges beyond task completion: successful execution must also maintain safe physical interaction, holding the object stably without slip or drop while avoiding excessive deformation. However, existing manipulation benchmarks are predominantly success-oriented and rarely evaluate whether a policy remains physically safe throughout execution. We present SoftVTBench, a safety-aware visuo-tactile benchmark for physically constrained deformable object manipulation. Built in Isaac Sim with finite-element-simulated deformable objects, SoftVTBench provides multi-view RGB observations, RGB tactile sensing with marker motion, proprioception, and language instructions, and defines four matched task suites over object type (deformable vs. rigid) and variation axis (object vs. spatial). It separately reports Goal Success and Safety Success; the latter additionally requires no drop and peak deformation below a calibrated object-specific threshold, measured from policy-hidden privileged Finite Element Method (FEM) states. We implement pi0.5-based baselines under this protocol. Experiments show that success-only evaluation substantially overstates policy performance, as a large fraction of goal-completing rollouts still violate physical safety. Furthermore, incorporating tactile sensing improves Safety Success (e.g., from 21.4% to 35.6% on object-centric deformable tasks) and reduces object deformation during execution, while maintaining comparable Goal Success. SoftVTBench provides a reproducible benchmark for studying visuo-tactile deformable manipulation under physical interaction constraints.

## 개요
변형 가능한 객체 조작은 작업 완료 이상의 도전 과제를 제시합니다. 성공적인 실행은 미끄러짐이나 낙하 없이 객체를 안정적으로 잡고 과도한 변형을 피하면서 안전한 물리적 상호작용을 유지해야 합니다. 그러나 기존 조작 벤치마크는 주로 성공 지향적이며, 정책이 실행 전반에 걸쳐 물리적으로 안전한지 평가하는 경우는 드뭅니다. 본 논문에서는 물리적 제약이 있는 변형 가능한 객체 조작을 위한 안전 인식 시각-촉각 벤치마크인 SoftVTBench를 제시합니다. Isaac Sim에서 유한 요소 시뮬레이션된 변형 가능한 객체로 구축된 SoftVTBench는 다중 시점 RGB 관찰, 마커 움직임을 포함한 RGB 촉각 센싱, 고유 수용감각, 언어 명령을 제공하며, 객체 유형(변형 가능 vs. 강체) 및 변동 축(객체 vs. 공간)에 따라 네 가지 일치하는 작업 모음을 정의합니다. 목표 성공과 안전 성공을 별도로 보고하며, 후자는 낙하가 없고 정책에 숨겨진 특권 유한 요소법(FEM) 상태에서 측정된 보정된 객체별 임계값 미만의 최대 변형을 추가로 요구합니다. 이 프로토콜 하에 pi0.5 기반 기준선을 구현합니다. 실험 결과, 성공만 평가하는 방식은 정책 성능을 상당히 과장하며, 목표를 완료한 롤아웃의 상당 부분이 여전히 물리적 안전을 위반하는 것으로 나타났습니다. 또한, 촉각 센싱을 통합하면 안전 성공이 향상되고(예: 객체 중심 변형 가능 작업에서 21.4%에서 35.6%로), 실행 중 객체 변형이 감소하며, 목표 성공은 유사한 수준을 유지합니다. SoftVTBench는 물리적 상호작용 제약 하에서 시각-촉각 변형 가능 조작을 연구하기 위한 재현 가능한 벤치마크를 제공합니다.

## 핵심 내용
변형 가능한 객체 조작은 작업 완료 이상의 도전 과제를 제시합니다. 성공적인 실행은 미끄러짐이나 낙하 없이 객체를 안정적으로 잡고 과도한 변형을 피하면서 안전한 물리적 상호작용을 유지해야 합니다. 그러나 기존 조작 벤치마크는 주로 성공 지향적이며, 정책이 실행 전반에 걸쳐 물리적으로 안전한지 평가하는 경우는 드뭅니다. 본 논문에서는 물리적 제약이 있는 변형 가능한 객체 조작을 위한 안전 인식 시각-촉각 벤치마크인 SoftVTBench를 제시합니다. Isaac Sim에서 유한 요소 시뮬레이션된 변형 가능한 객체로 구축된 SoftVTBench는 다중 시점 RGB 관찰, 마커 움직임을 포함한 RGB 촉각 센싱, 고유 수용감각, 언어 명령을 제공하며, 객체 유형(변형 가능 vs. 강체) 및 변동 축(객체 vs. 공간)에 따라 네 가지 일치하는 작업 모음을 정의합니다. 목표 성공과 안전 성공을 별도로 보고하며, 후자는 낙하가 없고 정책에 숨겨진 특권 유한 요소법(FEM) 상태에서 측정된 보정된 객체별 임계값 미만의 최대 변형을 추가로 요구합니다. 이 프로토콜 하에 pi0.5 기반 기준선을 구현합니다. 실험 결과, 성공만 평가하는 방식은 정책 성능을 상당히 과장하며, 목표를 완료한 롤아웃의 상당 부분이 여전히 물리적 안전을 위반하는 것으로 나타났습니다. 또한, 촉각 센싱을 통합하면 안전 성공이 향상되고(예: 객체 중심 변형 가능 작업에서 21.4%에서 35.6%로), 실행 중 객체 변형이 감소하며, 목표 성공은 유사한 수준을 유지합니다. SoftVTBench는 물리적 상호작용 제약 하에서 시각-촉각 변형 가능 조작을 연구하기 위한 재현 가능한 벤치마크를 제공합니다.

## 参考
- http://arxiv.org/abs/2607.04234v1
