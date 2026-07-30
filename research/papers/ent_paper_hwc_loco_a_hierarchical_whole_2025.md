---
$id: ent_paper_hwc_loco_a_hierarchical_whole_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion'
  zh: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion'
  ko: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion'
summary:
  en: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion is a 2025 work on locomotion for
    humanoid robots.'
  zh: HWC-Loco 是 2025 年提出的一种面向人形机器人行走任务的鲁棒全身控制算法。该工作通过将策略学习重构为鲁棒优化问题，并引入分层策略动态平衡目标追踪与安全恢复，显著提升了机器人在训练与部署环境差异下的鲁棒性。实验表明，HWC-Loco
    在多种地形、机器人结构和行走任务中均优于现有模型。
  ko: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion is a 2025 work on locomotion for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- hwc_loco
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.00923v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2503.00923
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'HWC-Loco: A Hierarchical Whole-Body Control Approach to Robust Humanoid Locomotion project page'
  url: https://simonlinsx.github.io/HWC_Loco/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
HWC-Loco 的核心创新在于将人形机器人的行走控制建模为鲁棒优化问题，使策略能够显式学习从安全关键场景中恢复。为解决过度保守行为影响任务完成的问题，该方法设计了一种分层策略，该策略依据人类行为规范与动力学约束，动态协调目标追踪与安全恢复之间的权衡。通过在仿真与真实环境中的广泛对比，HWC-Loco 在多种地形、不同机器人结构及行走任务上均展现出优于现有模型的性能。

## 核心内容
### 方法
HWC-Loco 采用分层全身控制框架，将策略学习转化为鲁棒优化问题。上层策略负责根据人类行为规范与动力学约束，动态权衡目标追踪与安全恢复；下层策略则执行具体的全身控制动作，确保机器人从安全关键场景中恢复。

### 实验设置
- **对比模型**：与多种 state-of-the-art 人形机器人控制模型进行对比。
- **测试环境**：涵盖仿真环境与真实世界场景。
- **评估维度**：包括不同地形（如平坦地面、斜坡、障碍物）、不同机器人结构以及多种行走任务（如前进、转向、避障）。

### 关键结果
- HWC-Loco 在仿真与真实环境中均表现出更强的鲁棒性，尤其在训练与部署环境存在差异时。
- 相比对比模型，HWC-Loco 在复杂地形上的行走成功率显著提升，且任务完成效率更高。
- 分层策略有效避免了过度保守行为，使机器人能够在保证安全的同时高效完成任务。

### 结论
HWC-Loco 通过鲁棒优化与分层策略的结合，为人形机器人在复杂环境中的鲁棒行走提供了一种有效解决方案。其性能在多种场景下均优于现有方法，展示了在真实世界部署中的潜力。

## Overview
Humanoid robots, capable of assuming human roles in various workplaces, have become essential to embodied intelligence. However, as robots with complex physical structures, learning a control model that can operate robustly across diverse environments remains inherently challenging, particularly under the discrepancies between training and deployment environments. In this study, we propose HWC-Loco, a robust whole-body control algorithm tailored for humanoid locomotion tasks. By reformulating policy learning as a robust optimization problem, HWC-Loco explicitly learns to recover from safety-critical scenarios. While prioritizing safety guarantees, overly conservative behavior can compromise the robot's ability to complete the given tasks. To tackle this challenge, HWC-Loco leverages a hierarchical policy for robust control. This policy can dynamically resolve the trade-off between goal-tracking and safety recovery, guided by human behavior norms and dynamic constraints. To evaluate the performance of HWC-Loco, we conduct extensive comparisons against state-of-the-art humanoid control models, demonstrating HWC-Loco's superior performance across diverse terrains, robot structures, and locomotion tasks under both simulated and real-world environments.

## 개요
휴머노이드 로봇은 다양한 작업 현장에서 인간의 역할을 대체할 수 있는 능력을 갖추며, 구현된 지능(embodied intelligence)의 핵심 요소가 되었습니다. 그러나 복잡한 물리적 구조를 가진 로봇이 다양한 환경에서 강건하게 작동할 수 있는 제어 모델을 학습하는 것은, 특히 훈련 환경과 배포 환경 간의 차이가 존재할 때 본질적으로 어려운 과제입니다. 본 연구에서는 휴머노이드 보행 작업에 특화된 강건한 전신 제어 알고리즘인 HWC-Loco를 제안합니다. 정책 학습을 강건 최적화 문제로 재구성함으로써, HWC-Loco는 안전이 중요한 시나리오에서 회복하는 방법을 명시적으로 학습합니다. 안전 보장을 우선시하는 과정에서 지나치게 보수적인 행동은 로봇이 주어진 작업을 완료하는 능력을 저하시킬 수 있습니다. 이 문제를 해결하기 위해 HWC-Loco는 계층적 정책을 활용한 강건 제어를 도입합니다. 이 정책은 인간 행동 규범과 동적 제약 조건에 따라 목표 추적과 안전 회복 간의 균형을 동적으로 조정할 수 있습니다. HWC-Loco의 성능을 평가하기 위해 최신 휴머노이드 제어 모델과의 광범위한 비교를 수행하였으며, 시뮬레이션 및 실제 환경 모두에서 다양한 지형, 로봇 구조 및 보행 작업에서 HWC-Loco의 우수한 성능을 입증했습니다.

## 핵심 내용
휴머노이드 로봇은 다양한 작업 현장에서 인간의 역할을 대체할 수 있는 능력을 갖추며, 구현된 지능의 핵심 요소가 되었습니다. 그러나 복잡한 물리적 구조를 가진 로봇이 다양한 환경에서 강건하게 작동할 수 있는 제어 모델을 학습하는 것은, 특히 훈련 환경과 배포 환경 간의 차이가 존재할 때 본질적으로 어려운 과제입니다. 본 연구에서는 휴머노이드 보행 작업에 특화된 강건한 전신 제어 알고리즘인 HWC-Loco를 제안합니다. 정책 학습을 강건 최적화 문제로 재구성함으로써, HWC-Loco는 안전이 중요한 시나리오에서 회복하는 방법을 명시적으로 학습합니다. 안전 보장을 우선시하는 과정에서 지나치게 보수적인 행동은 로봇이 주어진 작업을 완료하는 능력을 저하시킬 수 있습니다. 이 문제를 해결하기 위해 HWC-Loco는 계층적 정책을 활용한 강건 제어를 도입합니다. 이 정책은 인간 행동 규범과 동적 제약 조건에 따라 목표 추적과 안전 회복 간의 균형을 동적으로 조정할 수 있습니다. HWC-Loco의 성능을 평가하기 위해 최신 휴머노이드 제어 모델과의 광범위한 비교를 수행하였으며, 시뮬레이션 및 실제 환경 모두에서 다양한 지형, 로봇 구조 및 보행 작업에서 HWC-Loco의 우수한 성능을 입증했습니다.

## 参考
- http://arxiv.org/abs/2503.00923v3
