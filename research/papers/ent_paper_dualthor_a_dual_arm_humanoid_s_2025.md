---
$id: ent_paper_dualthor_a_dual_arm_humanoid_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning'
  zh: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning'
  ko: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning'
summary:
  en: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning is a 2025 work on simulation benchmark
    for humanoid robots.'
  zh: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning is a 2025 work on simulation benchmark
    for humanoid robots.'
  ko: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning is a 2025 work on simulation benchmark
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- dualthor
- humanoid
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.16012v2.
sources:
- id: src_001
  type: paper
  title: 'DualTHOR: A Dual-Arm Humanoid Simulation Platform for Contingency-Aware Planning (arXiv)'
  url: https://arxiv.org/abs/2506.16012
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Developing embodied agents capable of performing complex interactive tasks in real-world scenarios remains a fundamental challenge in embodied AI. Although recent advances in simulation platforms have greatly enhanced task diversity to train embodied Vision Language Models (VLMs), most platforms rely on simplified robot morphologies and bypass the stochastic nature of low-level execution, which limits their transferability to real-world robots. To address these issues, we present a physics-based simulation platform DualTHOR for complex dual-arm humanoid robots, built upon an extended version of AI2-THOR. Our simulator includes real-world robot assets, a task suite for dual-arm collaboration, and inverse kinematics solvers for humanoid robots. We also introduce a contingency mechanism that incorporates potential failures through physics-based low-level execution, bridging the gap to real-world scenarios. Our simulator enables a more comprehensive evaluation of the robustness and generalization of VLMs in household environments. Extensive evaluations reveal that current VLMs struggle with dual-arm coordination and exhibit limited robustness in realistic environments with contingencies, highlighting the importance of using our simulator to develop more capable VLMs for embodied tasks. The code is available at https://github.com/ds199895/DualTHOR.git.

## 核心内容
Developing embodied agents capable of performing complex interactive tasks in real-world scenarios remains a fundamental challenge in embodied AI. Although recent advances in simulation platforms have greatly enhanced task diversity to train embodied Vision Language Models (VLMs), most platforms rely on simplified robot morphologies and bypass the stochastic nature of low-level execution, which limits their transferability to real-world robots. To address these issues, we present a physics-based simulation platform DualTHOR for complex dual-arm humanoid robots, built upon an extended version of AI2-THOR. Our simulator includes real-world robot assets, a task suite for dual-arm collaboration, and inverse kinematics solvers for humanoid robots. We also introduce a contingency mechanism that incorporates potential failures through physics-based low-level execution, bridging the gap to real-world scenarios. Our simulator enables a more comprehensive evaluation of the robustness and generalization of VLMs in household environments. Extensive evaluations reveal that current VLMs struggle with dual-arm coordination and exhibit limited robustness in realistic environments with contingencies, highlighting the importance of using our simulator to develop more capable VLMs for embodied tasks. The code is available at https://github.com/ds199895/DualTHOR.git.

## 参考
- http://arxiv.org/abs/2506.16012v2

