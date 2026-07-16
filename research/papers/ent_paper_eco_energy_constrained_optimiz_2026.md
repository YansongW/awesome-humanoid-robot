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
  zh: 'ECO: Energy-Constrained Optimization with Reinforcement Learning for Humanoid Walking is a 2026 work on locomotion
    for humanoid robots, with open-source code available.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06445v1.
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
Achieving stable and energy-efficient locomotion is essential for humanoid robots to operate continuously in real-world applications. Existing MPC and RL approaches often rely on energy-related metrics embedded within a multi-objective optimization framework, which require extensive hyperparameter tuning and often result in suboptimal policies. To address these challenges, we propose ECO (Energy-Constrained Optimization), a constrained RL framework that separates energy-related metrics from rewards, reformulating them as explicit inequality constraints. This method provides a clear and interpretable physical representation of energy costs, enabling more efficient and intuitive hyperparameter tuning for improved energy efficiency. ECO introduces dedicated constraints for energy consumption and reference motion, enforced by the Lagrangian method, to achieve stable, symmetric, and energy-efficient walking for humanoid robots. We evaluated ECO against MPC, standard RL with reward shaping, and four state-of-the-art constrained RL methods. Experiments, including sim-to-sim and sim-to-real transfers on the kid-sized humanoid robot BRUCE, demonstrate that ECO significantly reduces energy consumption compared to baselines while maintaining robust walking performance. These results highlight a substantial advancement in energy-efficient humanoid locomotion. All experimental demonstrations can be found on the project website: https://sites.google.com/view/eco-humanoid.

## 核心内容
Achieving stable and energy-efficient locomotion is essential for humanoid robots to operate continuously in real-world applications. Existing MPC and RL approaches often rely on energy-related metrics embedded within a multi-objective optimization framework, which require extensive hyperparameter tuning and often result in suboptimal policies. To address these challenges, we propose ECO (Energy-Constrained Optimization), a constrained RL framework that separates energy-related metrics from rewards, reformulating them as explicit inequality constraints. This method provides a clear and interpretable physical representation of energy costs, enabling more efficient and intuitive hyperparameter tuning for improved energy efficiency. ECO introduces dedicated constraints for energy consumption and reference motion, enforced by the Lagrangian method, to achieve stable, symmetric, and energy-efficient walking for humanoid robots. We evaluated ECO against MPC, standard RL with reward shaping, and four state-of-the-art constrained RL methods. Experiments, including sim-to-sim and sim-to-real transfers on the kid-sized humanoid robot BRUCE, demonstrate that ECO significantly reduces energy consumption compared to baselines while maintaining robust walking performance. These results highlight a substantial advancement in energy-efficient humanoid locomotion. All experimental demonstrations can be found on the project website: https://sites.google.com/view/eco-humanoid.

## 参考
- http://arxiv.org/abs/2602.06445v1

## Overview
Achieving stable and energy-efficient locomotion is essential for humanoid robots to operate continuously in real-world applications. Existing MPC and RL approaches often rely on energy-related metrics embedded within a multi-objective optimization framework, which require extensive hyperparameter tuning and often result in suboptimal policies. To address these challenges, we propose ECO (Energy-Constrained Optimization), a constrained RL framework that separates energy-related metrics from rewards, reformulating them as explicit inequality constraints. This method provides a clear and interpretable physical representation of energy costs, enabling more efficient and intuitive hyperparameter tuning for improved energy efficiency. ECO introduces dedicated constraints for energy consumption and reference motion, enforced by the Lagrangian method, to achieve stable, symmetric, and energy-efficient walking for humanoid robots. We evaluated ECO against MPC, standard RL with reward shaping, and four state-of-the-art constrained RL methods. Experiments, including sim-to-sim and sim-to-real transfers on the kid-sized humanoid robot BRUCE, demonstrate that ECO significantly reduces energy consumption compared to baselines while maintaining robust walking performance. These results highlight a substantial advancement in energy-efficient humanoid locomotion. All experimental demonstrations can be found on the project website: https://sites.google.com/view/eco-humanoid.

## Content
Achieving stable and energy-efficient locomotion is essential for humanoid robots to operate continuously in real-world applications. Existing MPC and RL approaches often rely on energy-related metrics embedded within a multi-objective optimization framework, which require extensive hyperparameter tuning and often result in suboptimal policies. To address these challenges, we propose ECO (Energy-Constrained Optimization), a constrained RL framework that separates energy-related metrics from rewards, reformulating them as explicit inequality constraints. This method provides a clear and interpretable physical representation of energy costs, enabling more efficient and intuitive hyperparameter tuning for improved energy efficiency. ECO introduces dedicated constraints for energy consumption and reference motion, enforced by the Lagrangian method, to achieve stable, symmetric, and energy-efficient walking for humanoid robots. We evaluated ECO against MPC, standard RL with reward shaping, and four state-of-the-art constrained RL methods. Experiments, including sim-to-sim and sim-to-real transfers on the kid-sized humanoid robot BRUCE, demonstrate that ECO significantly reduces energy consumption compared to baselines while maintaining robust walking performance. These results highlight a substantial advancement in energy-efficient humanoid locomotion. All experimental demonstrations can be found on the project website: https://sites.google.com/view/eco-humanoid.

## 개요
휴머노이드 로봇이 실제 환경에서 지속적으로 작동하려면 안정적이고 에너지 효율적인 보행이 필수적입니다. 기존의 MPC 및 RL 접근법은 다중 목표 최적화 프레임워크 내에 에너지 관련 지표를 포함하는 경우가 많으며, 이는 광범위한 하이퍼파라미터 튜닝이 필요하고 종종 최적이 아닌 정책을 초래합니다. 이러한 문제를 해결하기 위해 우리는 ECO(Energy-Constrained Optimization)를 제안합니다. 이는 에너지 관련 지표를 보상에서 분리하여 명시적 부등식 제약 조건으로 재구성하는 제약 RL 프레임워크입니다. 이 방법은 에너지 비용에 대한 명확하고 해석 가능한 물리적 표현을 제공하여, 에너지 효율성을 개선하기 위한 더 효율적이고 직관적인 하이퍼파라미터 튜닝을 가능하게 합니다. ECO는 에너지 소비 및 참조 동작에 대한 전용 제약 조건을 도입하고, 라그랑주 방법을 통해 이를 강제하여 휴머노이드 로봇의 안정적이고 대칭적이며 에너지 효율적인 보행을 달성합니다. 우리는 ECO를 MPC, 보상 형성을 사용한 표준 RL, 그리고 4가지 최신 제약 RL 방법과 비교 평가했습니다. 어린이 크기 휴머노이드 로봇 BRUCE를 사용한 sim-to-sim 및 sim-to-real 전이 실험을 포함한 실험 결과, ECO가 기준 방법에 비해 에너지 소비를 크게 줄이면서도 강건한 보행 성능을 유지함을 보여줍니다. 이러한 결과는 에너지 효율적인 휴머노이드 보행에서의 중요한 발전을 강조합니다. 모든 실험 데모는 프로젝트 웹사이트에서 확인할 수 있습니다: https://sites.google.com/view/eco-humanoid.

## 핵심 내용
휴머노이드 로봇이 실제 환경에서 지속적으로 작동하려면 안정적이고 에너지 효율적인 보행이 필수적입니다. 기존의 MPC 및 RL 접근법은 다중 목표 최적화 프레임워크 내에 에너지 관련 지표를 포함하는 경우가 많으며, 이는 광범위한 하이퍼파라미터 튜닝이 필요하고 종종 최적이 아닌 정책을 초래합니다. 이러한 문제를 해결하기 위해 우리는 ECO(Energy-Constrained Optimization)를 제안합니다. 이는 에너지 관련 지표를 보상에서 분리하여 명시적 부등식 제약 조건으로 재구성하는 제약 RL 프레임워크입니다. 이 방법은 에너지 비용에 대한 명확하고 해석 가능한 물리적 표현을 제공하여, 에너지 효율성을 개선하기 위한 더 효율적이고 직관적인 하이퍼파라미터 튜닝을 가능하게 합니다. ECO는 에너지 소비 및 참조 동작에 대한 전용 제약 조건을 도입하고, 라그랑주 방법을 통해 이를 강제하여 휴머노이드 로봇의 안정적이고 대칭적이며 에너지 효율적인 보행을 달성합니다. 우리는 ECO를 MPC, 보상 형성을 사용한 표준 RL, 그리고 4가지 최신 제약 RL 방법과 비교 평가했습니다. 어린이 크기 휴머노이드 로봇 BRUCE를 사용한 sim-to-sim 및 sim-to-real 전이 실험을 포함한 실험 결과, ECO가 기준 방법에 비해 에너지 소비를 크게 줄이면서도 강건한 보행 성능을 유지함을 보여줍니다. 이러한 결과는 에너지 효율적인 휴머노이드 보행에서의 중요한 발전을 강조합니다. 모든 실험 데모는 프로젝트 웹사이트에서 확인할 수 있습니다: https://sites.google.com/view/eco-humanoid.
