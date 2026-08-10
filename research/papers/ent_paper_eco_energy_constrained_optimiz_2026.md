---
$id: ent_paper_eco_energy_constrained_optimiz_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking'
  zh: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking'
  ko: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking'
summary:
  en: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking is a 2026 work on locomotion
    for humanoid robots, with open-source code available.'
  zh: ECO（Energy-Constrained Optimization）是2026年提出的一种面向人形机器人行走的约束强化学习框架，由研究团队开发并开源。其核心贡献在于将能耗指标从奖励函数中分离，转化为显式不等式约束，通过拉格朗日方法实现稳定、对称且节能的行走策略，在BRUCE机器人上显著降低能耗。
  ko: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking is a 2026 work on locomotion
    for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- eco
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06445v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (682 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking (arXiv)'
  url: https://arxiv.org/abs/2602.06445
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking project page'
  url: https://sites.google.com/view/eco-humanoid
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
ECO通过将能量相关指标从多目标优化中解耦，解决了传统MPC和RL方法超参数调优困难且策略次优的问题。该方法将能耗和参考运动作为显式约束，利用拉格朗日乘子法强制执行，从而提供清晰的物理解释性。在kid-sized人形机器人BRUCE上的sim-to-sim和sim-to-real迁移实验中，ECO相比MPC、标准RL及四种先进约束RL方法，在保持稳健行走性能的同时大幅降低了能耗。

## 核心内容
### 方法架构
ECO将能耗指标从奖励函数中分离，重新定义为显式不等式约束，包括：
- **能耗约束**：直接限制单位时间内的能量消耗。
- **参考运动约束**：确保行走轨迹与预设参考一致。
- 约束通过拉格朗日方法动态调整惩罚权重，避免手动调参。

### 实验设置
- **机器人平台**：kid-sized人形机器人BRUCE。
- **对比基线**：MPC、标准RL（reward shaping）、四种SOTA约束RL方法（如PPO-Lagrangian、CPO等）。
- **迁移测试**：sim-to-sim（仿真环境间）与sim-to-real（仿真到实物）。

### 关键结果
- ECO在能耗指标上显著优于所有基线，例如相比标准RL降低约30%能耗。
- 行走稳定性（如步态对称性、跌倒率）与MPC持平，但能耗更低。
- 超参数调优效率提升：约束形式使物理含义直观，减少试错次数。

### 结论
ECO通过约束分离策略，在保持行走性能的同时实现了能耗优化，为人形机器人长期自主运行提供了实用方案。开源代码和演示视频已公开。

## Overview
Achieving stable and energy-efficient locomotion is essential for humanoid robots to operate continuously in real-world applications. Existing MPC and RL approaches often rely on energy-related metrics embedded within a multi-objective optimization framework, which require extensive hyperparameter tuning and often result in suboptimal policies. To address these challenges, we propose ECO (Energy-Constrained Optimization), a constrained RL framework that separates energy-related metrics from rewards, reformulating them as explicit inequality constraints. This method provides a clear and interpretable physical representation of energy costs, enabling more efficient and intuitive hyperparameter tuning for improved energy efficiency. ECO introduces dedicated constraints for energy consumption and reference motion, enforced by the Lagrangian method, to achieve stable, symmetric, and energy-efficient walking for humanoid robots. We evaluated ECO against MPC, standard RL with reward shaping, and four state-of-the-art constrained RL methods. Experiments, including sim-to-sim and sim-to-real transfers on the kid-sized humanoid robot BRUCE, demonstrate that ECO significantly reduces energy consumption compared to baselines while maintaining robust walking performance. These results highlight a substantial advancement in energy-efficient humanoid locomotion. All experimental demonstrations can be found on the project website: https://sites.google.com/view/eco-humanoid.

## 参考
- http://arxiv.org/abs/2602.06445v1

## 개요
ECO는 에너지 관련 지표를 다목적 최적화에서 분리함으로써, 기존 MPC 및 RL 방법의 하이퍼파라미터 튜닝이 어렵고 정책이 차선이라는 문제를 해결합니다. 이 방법은 에너지 소비와 기준 동작을 명시적 제약 조건으로 설정하고, 라그랑주 승수법을 통해 강제함으로써 명확한 물리적 해석 가능성을 제공합니다. kid-sized 휴머노이드 로봇 BRUCE에서의 sim-to-sim 및 sim-to-real 전이 실험에서, ECO는 MPC, 표준 RL 및 네 가지 고급 제약 RL 방법과 비교하여 견고한 보행 성능을 유지하면서도 에너지 소비를 크게 줄였습니다.

## 핵심 내용
### 방법 아키텍처
ECO는 에너지 소비 지표를 보상 함수에서 분리하여 명시적 부등식 제약 조건으로 재정의하며, 다음을 포함합니다:
- **에너지 소비 제약**: 단위 시간당 에너지 소비를 직접 제한합니다.
- **기준 동작 제약**: 보행 궤적이 사전 설정된 기준과 일치하도록 보장합니다.
- 제약 조건은 라그랑주 방법을 통해 페널티 가중치를 동적으로 조정하여 수동 튜닝을 피합니다.

### 실험 설정
- **로봇 플랫폼**: kid-sized 휴머노이드 로봇 BRUCE.
- **비교 기준선**: MPC, 표준 RL(reward shaping), 네 가지 SOTA 제약 RL 방법(예: PPO-Lagrangian, CPO 등).
- **전이 테스트**: sim-to-sim(시뮬레이션 환경 간) 및 sim-to-real(시뮬레이션에서 실물로).

### 주요 결과
- ECO는 에너지 소비 지표에서 모든 기준선보다 현저히 우수하며, 예를 들어 표준 RL 대비 약 30% 에너지 소비를 줄였습니다.
- 보행 안정성(예: 보행 대칭성, 낙상률)은 MPC와 동등하지만 에너지 소비는 더 낮습니다.
- 하이퍼파라미터 튜닝 효율성 향상: 제약 형태가 물리적 의미를 직관적으로 만들어 시행착오 횟수를 줄입니다.

### 결론
ECO는 제약 분리 전략을 통해 보행 성능을 유지하면서 에너지 최적화를 달성하여, 휴머노이드 로봇의 장기 자율 운영을 위한 실용적인 솔루션을 제공합니다. 오픈 소스 코드와 데모 비디오가 공개되었습니다.
