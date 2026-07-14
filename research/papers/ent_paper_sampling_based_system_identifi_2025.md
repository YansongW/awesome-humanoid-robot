---
$id: ent_paper_sampling_based_system_identifi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning
  zh: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning
  ko: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning
summary:
  en: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning is a 2025 work on sim-to-real
    for humanoid robots.
  zh: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning is a 2025 work on sim-to-real
    for humanoid robots.
  ko: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning is a 2025 work on sim-to-real
    for humanoid robots.
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
- sampling_based_system_identifi
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.14266v1.
sources:
- id: src_001
  type: paper
  title: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning (arXiv)
  url: https://arxiv.org/abs/2505.14266
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Sim-to-real discrepancies hinder learning-based policies from achieving high-precision tasks in the real world. While Domain Randomization (DR) is commonly used to bridge this gap, it often relies on heuristics and can lead to overly conservative policies with degrading performance when not properly tuned. System Identification (Sys-ID) offers a targeted approach, but standard techniques rely on differentiable dynamics and/or direct torque measurement, assumptions that rarely hold for contact-rich legged systems. To this end, we present SPI-Active (Sampling-based Parameter Identification with Active Exploration), a two-stage framework that estimates physical parameters of legged robots to minimize the sim-to-real gap. SPI-Active robustly identifies key physical parameters through massive parallel sampling, minimizing state prediction errors between simulated and real-world trajectories. To further improve the informativeness of collected data, we introduce an active exploration strategy that maximizes the Fisher Information of the collected real-world trajectories via optimizing the input commands of an exploration policy. This targeted exploration leads to accurate identification and better generalization across diverse tasks. Experiments demonstrate that SPI-Active enables precise sim-to-real transfer of learned policies to the real world, outperforming baselines by 42-63% in various locomotion tasks.

## 核心内容
Sim-to-real discrepancies hinder learning-based policies from achieving high-precision tasks in the real world. While Domain Randomization (DR) is commonly used to bridge this gap, it often relies on heuristics and can lead to overly conservative policies with degrading performance when not properly tuned. System Identification (Sys-ID) offers a targeted approach, but standard techniques rely on differentiable dynamics and/or direct torque measurement, assumptions that rarely hold for contact-rich legged systems. To this end, we present SPI-Active (Sampling-based Parameter Identification with Active Exploration), a two-stage framework that estimates physical parameters of legged robots to minimize the sim-to-real gap. SPI-Active robustly identifies key physical parameters through massive parallel sampling, minimizing state prediction errors between simulated and real-world trajectories. To further improve the informativeness of collected data, we introduce an active exploration strategy that maximizes the Fisher Information of the collected real-world trajectories via optimizing the input commands of an exploration policy. This targeted exploration leads to accurate identification and better generalization across diverse tasks. Experiments demonstrate that SPI-Active enables precise sim-to-real transfer of learned policies to the real world, outperforming baselines by 42-63% in various locomotion tasks.

## 参考
- http://arxiv.org/abs/2505.14266v1

