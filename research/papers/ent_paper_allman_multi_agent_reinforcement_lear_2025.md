---
$id: ent_paper_allman_multi_agent_reinforcement_lear_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Multi-Agent Reinforcement Learning for Cooperative Warehouse Automation: QMIX
    Value Decomposition for Sparse-Reward Coordination'
  zh: 面向协同仓库自动化的多智能体强化学习：面向稀疏奖励协调的QMIX值分解
  ko: '협력형 창고 자동화를 위한 다중 에이전트 강화학습: 희소 보상 조정을 위한 QMIX 가치 분해'
summary:
  en: This paper compares QMIX, IPPO, and MASAC on warehouse multi-agent reinforcement
    learning tasks using RWARE, MPE, and a custom Unity 3D simulation, demonstrating
    that QMIX's value decomposition outperforms independent learners but requires
    extensive hyperparameter tuning—particularly extended epsilon annealing—to discover
    sparse rewards.
  zh: 该论文在RWARE、MPE和自定义Unity 3D仿真环境中对比了QMIX、IPPO和MASAC在仓库多智能体强化学习任务上的表现，表明QMIX的值分解方法优于独立学习器，但在稀疏奖励场景下需要大量超参数调优，尤其是扩展的epsilon退火策略。
  ko: 본 논문은 RWARE, MPE 및 사용자 정의 Unity 3D 시뮬레이션에서 창고 다중 에이전트 강화학습 작업에 대한 QMIX, IPPO
    및 MASAC을 비교하며, QMIX의 가치 분해가 독립 학습기보다 우수하지만 희소 보상 발견을 위해 광범위한 하이퍼파라미터 튜닝, 특히 확장된
    입실론 어닐링이 필요함을 보여준다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from abstract and provided metadata; requires human review against
    the full arXiv text before final verification.
sources:
- id: src_001
  type: paper
  title: 'Multi-Agent Reinforcement Learning for Cooperative Warehouse Automation:
    QMIX Value Decomposition for Sparse-Reward Coordination'
  url: https://arxiv.org/abs/2512.04463
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## Overview

This paper presents a comparative study of multi-agent reinforcement learning (MARL) algorithms applied to cooperative warehouse robotics. The authors evaluate QMIX, Independent Proximal Policy Optimization (IPPO), and Multi-Agent Soft Actor-Critic (MASAC) across three experimental settings: the Multi-Agent Particle Environment (MPE) as a validation testbed, the Robotic Warehouse (RWARE) benchmark, and a custom Unity 3D simulation developed with Unity ML-Agents. The study focuses on sparse-reward coordination problems where robots must avoid collisions, allocate tasks implicitly, and deliver packages without centralized control.

The main experimental finding is that QMIX's hypernetwork-based value decomposition substantially outperforms independent learning approaches. On RWARE, QMIX achieved a mean return of 3.25 versus 0.38 for an advanced IPPO configuration. However, the authors also report that QMIX requires extensive hyperparameter tuning, especially extended epsilon annealing over 5 million or more steps, to discover rewards in the sparse warehouse tasks. In the Unity ML-Agents environment, the trained agents achieved consistent package delivery after approximately 1 million training steps, demonstrating sim-to-sim transfer feasibility.

The paper is limited to simulation-only evaluation with no physical robot deployment, and experiments are conducted with only 2 to 6 agents. The authors note that the RWARE task structure is simplified relative to real industrial warehouses and that the long training requirements may limit rapid deployment. Despite these limitations, the work provides practical guidance on hyperparameter choices and algorithm selection for MARL warehouse coordination.

## Key Contributions

- Hyperparameter analysis showing that default MARL configurations fail on sparse-reward warehouse tasks and that extended epsilon annealing is critical for QMIX.
- Comparative evaluation of QMIX, IPPO, and MASAC across MPE validation, RWARE benchmark, and a custom Unity 3D simulation at multiple agent scales.
- Unity ML-Agents integration demonstrating sim-to-sim transfer with successful, consistent package delivery after 1M training steps.
- Identification of practical scaling challenges that must be addressed before industrial warehouse deployments of MARL-coordinated robot fleets.

## Relevance to Humanoid Robotics

Although the experiments use wheeled warehouse mobile robots rather than humanoids, the underlying coordination challenges—implicit multi-agent communication, credit assignment, collision avoidance, and task allocation—are directly transferable to fleets of humanoid robots deployed in logistics and warehouse automation. Humanoid platforms operating in human-structured spaces would face analogous sparse-reward coordination problems when learning to hand off items, share aisles, or divide pick-and-place tasks. The paper's findings on the importance of value decomposition and the difficulty of hyperparameter tuning in sparse-reward settings can inform algorithm selection and training design for humanoid robot fleets.
