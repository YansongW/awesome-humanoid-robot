---
$id: ent_paper_allman_multi_agent_reinforcement_lear_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Multi-Agent Reinforcement Learning for Cooperative Warehouse Automation: QMIX Value Decomposition for Sparse-Reward
    Coordination'
  zh: 面向协同仓库自动化的多智能体强化学习：面向稀疏奖励协调的QMIX值分解
  ko: '협력형 창고 자동화를 위한 다중 에이전트 강화학습: 희소 보상 조정을 위한 QMIX 가치 분해'
summary:
  en: This paper compares QMIX, IPPO, and MASAC on warehouse multi-agent reinforcement learning tasks using RWARE, MPE, and
    a custom Unity 3D simulation, demonstrating that QMIX's value decomposition outperforms independent learners but requires
    extensive hyperparameter tuning—particularly extended epsilon annealing—to discover sparse rewards.
  zh: 该论文在RWARE、MPE和自定义Unity 3D仿真环境中对比了QMIX、IPPO和MASAC在仓库多智能体强化学习任务上的表现，表明QMIX的值分解方法优于独立学习器，但在稀疏奖励场景下需要大量超参数调优，尤其是扩展的epsilon退火策略。
  ko: 본 논문은 RWARE, MPE 및 사용자 정의 Unity 3D 시뮬레이션에서 창고 다중 에이전트 강화학습 작업에 대한 QMIX, IPPO 및 MASAC을 비교하며, QMIX의 가치 분해가 독립 학습기보다 우수하지만
    희소 보상 발견을 위해 광범위한 하이퍼파라미터 튜닝, 특히 확장된 입실론 어닐링이 필요함을 보여준다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- marl
- qmix
- ippo
- masac
- warehouse_automation
- multi_agent_coordination
- reinforcement_learning
- sim_to_sim_transfer
- rware
- mpe
- unity_ml_agents
- sparse_rewards
- value_decomposition
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.04463v2.
sources:
- id: src_001
  type: paper
  title: 'Multi-Agent Reinforcement Learning for Cooperative Warehouse Automation: QMIX Value Decomposition for Sparse-Reward
    Coordination'
  url: https://arxiv.org/abs/2512.04463
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
We present a comparative study of multi-agent reinforcement learning (MARL) algorithms for cooperative warehouse robotics. We evaluate QMIX and IPPO on the Robotic Warehouse (RWARE) environment and a custom Unity 3D simulation. Our experiments reveal that QMIX's value decomposition significantly outperforms independent learning approaches (achieving 3.25 mean return vs. 0.38 for advanced IPPO), but requires extensive hyperparameter tuning -- particularly extended epsilon annealing (5M+ steps) for sparse reward discovery. We demonstrate successful deployment in Unity ML-Agents, achieving consistent package delivery after 1M training steps. While MARL shows promise for small-scale deployments (2-4 robots), significant scaling challenges remain. Code and analyses: https://pallman14.github.io/MARL-QMIX-Warehouse-Robots/

## 核心内容
We present a comparative study of multi-agent reinforcement learning (MARL) algorithms for cooperative warehouse robotics. We evaluate QMIX and IPPO on the Robotic Warehouse (RWARE) environment and a custom Unity 3D simulation. Our experiments reveal that QMIX's value decomposition significantly outperforms independent learning approaches (achieving 3.25 mean return vs. 0.38 for advanced IPPO), but requires extensive hyperparameter tuning -- particularly extended epsilon annealing (5M+ steps) for sparse reward discovery. We demonstrate successful deployment in Unity ML-Agents, achieving consistent package delivery after 1M training steps. While MARL shows promise for small-scale deployments (2-4 robots), significant scaling challenges remain. Code and analyses: https://pallman14.github.io/MARL-QMIX-Warehouse-Robots/

## 参考
- http://arxiv.org/abs/2512.04463v2

