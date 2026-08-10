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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04234v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1054 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.04234v1

## 개요
SoftVTBench는 기존 조작 벤치마크가 주로 작업 완료에 초점을 맞추고 물리적 안전을 간과하는 문제를 해결하기 위해 설계되었습니다. 이 벤치마크는 Isaac Sim에서 유한 요소 방법을 사용하여 변형 가능한 물체를 시뮬레이션하며, 다중 시점 RGB 이미지, RGB 촉각 센싱(마커 움직임 포함), 고유 수용 감각, 언어 명령을 제공하고, 네 가지 매칭 작업 세트(물체 유형 및 변화 축에 따라 구분)를 정의합니다. 목표 성공률과 안전 성공률을 각각 보고하며, 안전 성공률은 추가로 낙하 없음 및 보정된 물체별 임계값(정책에 숨겨진 특권 유한 요소 상태 측정 기반) 미만의 최대 변형을 요구합니다. pi0.5 기반의 기준 실험은 작업 성공률만 평가하면 정책 성능을 심각하게 과대평가할 수 있음을 보여줍니다. 목표를 달성한 많은 롤아웃이 여전히 물리적 안전을 위반하기 때문입니다. 또한, 촉각 센싱을 통합하면 목표 성공률을 유지하면서 안전 성공률을 향상시키고 실행 중 물체 변형을 줄일 수 있습니다.

## 핵심 내용
### 핵심 문제
변형 가능한 물체 조작은 작업 완료뿐만 아니라 물리적 상호작용의 안전도 보장해야 합니다: 물체를 안정적으로 잡고(미끄러짐 또는 낙하 없음) 과도한 변형을 피해야 합니다. 기존 벤치마크는 대부분 작업 성공에 초점을 맞추며, 정책이 실행 중 물리적 안전을 유지하는지 평가하는 경우는 드뭅니다.

### SoftVTBench 설계
- **시뮬레이션 환경**: Isaac Sim 기반으로 구축되었으며, 유한 요소 방법을 사용하여 변형 가능한 물체를 시뮬레이션합니다.
- **관측 모달리티**: 다중 시점 RGB 관측, RGB 촉각 센싱(마커 움직임 포함), 고유 수용 감각, 언어 명령.
- **작업 세트**: 물체 유형(변형 가능 vs. 강체) 및 변화 축(물체 vs. 공간)에 따라 네 가지 매칭 작업을 정의합니다.
- **평가 지표**:
  - **Goal Success**: 작업 완료 성공률.
  - **Safety Success**: 작업 완료를 기반으로, 추가로 낙하 없음 및 보정된 물체별 임계값(정책에 숨겨진 특권 유한 요소 상태 측정 기반) 미만의 최대 변형을 요구합니다.

### 실험 설정 및 기준
- **기준 모델**: pi0.5 기반으로 구현되었습니다.
- **실험 프로토콜**: Goal Success와 Safety Success를 각각 보고합니다.

### 핵심 결과
- **작업 성공률만의 오해 소지**: 목표를 달성한 많은 롤아웃이 여전히 물리적 안전을 위반하므로, Goal Success만 평가하면 정책 성능을 심각하게 과대평가할 수 있습니다.
- **촉각 센싱의 기여**:
  - 물체 중심 변형 작업에서 Safety Success가 21.4%에서 35.6%로 향상되었습니다.
  - 실행 중 물체 변형이 크게 감소했습니다.
  - Goal Success는 비교 가능한 수준을 유지했습니다.

### 결론
SoftVTBench는 물리적 상호작용 제약 하에서의 시각-촉각 변형 가능한 물체 조작을 연구하기 위한 재현 가능한 벤치마크를 제공하며, 안전 평가의 필요성과 촉각 센싱의 가치를 강조합니다.
