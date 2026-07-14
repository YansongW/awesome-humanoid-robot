---
$id: ent_paper_humanoidgen_data_generation_fo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning'
  zh: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning'
  ko: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning'
summary:
  en: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning is a 2025 work on simulation benchmark
    for humanoid robots.'
  zh: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning is a 2025 work on simulation benchmark
    for humanoid robots.'
  ko: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning is a 2025 work on simulation benchmark
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
- humanoid
- humanoidgen
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.00833v2.
sources:
- id: src_001
  type: paper
  title: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning (arXiv)'
  url: https://arxiv.org/abs/2507.00833
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning project page'
  url: https://openhumanoidgen.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
For robotic manipulation, existing robotics datasets and simulation benchmarks predominantly cater to robot-arm platforms. However, for humanoid robots equipped with dual arms and dexterous hands, simulation tasks and high-quality demonstrations are notably lacking. Bimanual dexterous manipulation is inherently more complex, as it requires coordinated arm movements and hand operations, making autonomous data collection challenging. This paper presents HumanoidGen, an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints. Specifically, we provide spatial annotations for both assets and dexterous hands based on the atomic operations, and perform an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes. To further improve planning ability, we employ a variant of Monte Carlo tree search to enhance LLM reasoning for long-horizon tasks and insufficient annotation. In experiments, we create a novel benchmark with augmented scenarios to evaluate the quality of the collected data. The results show that the performance of the 2D and 3D diffusion policies can scale with the generated dataset. Project page is https://openhumanoidgen.github.io.

## 核心内容
For robotic manipulation, existing robotics datasets and simulation benchmarks predominantly cater to robot-arm platforms. However, for humanoid robots equipped with dual arms and dexterous hands, simulation tasks and high-quality demonstrations are notably lacking. Bimanual dexterous manipulation is inherently more complex, as it requires coordinated arm movements and hand operations, making autonomous data collection challenging. This paper presents HumanoidGen, an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints. Specifically, we provide spatial annotations for both assets and dexterous hands based on the atomic operations, and perform an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes. To further improve planning ability, we employ a variant of Monte Carlo tree search to enhance LLM reasoning for long-horizon tasks and insufficient annotation. In experiments, we create a novel benchmark with augmented scenarios to evaluate the quality of the collected data. The results show that the performance of the 2D and 3D diffusion policies can scale with the generated dataset. Project page is https://openhumanoidgen.github.io.

## 参考
- http://arxiv.org/abs/2507.00833v2

