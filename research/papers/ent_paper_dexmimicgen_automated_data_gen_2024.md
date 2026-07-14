---
$id: ent_paper_dexmimicgen_automated_data_gen_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning'
  zh: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning'
  ko: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning'
summary:
  en: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning is a 2024 work on
    simulation benchmark for humanoid robots.'
  zh: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning is a 2024 work on
    simulation benchmark for humanoid robots.'
  ko: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning is a 2024 work on
    simulation benchmark for humanoid robots.'
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
- dexmimicgen
- humanoid
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.24185v2.
sources:
- id: src_001
  type: paper
  title: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning (arXiv)'
  url: https://arxiv.org/abs/2410.24185
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning project page'
  url: https://dexmimicgen.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning from human demonstrations is an effective means to teach robots manipulation skills. But data acquisition is a major bottleneck in applying this paradigm more broadly, due to the amount of cost and human effort involved. There has been significant interest in imitation learning for bimanual dexterous robots, like humanoids. Unfortunately, data collection is even more challenging here due to the challenges of simultaneously controlling multiple arms and multi-fingered hands. Automated data generation in simulation is a compelling, scalable alternative to fuel this need for data. To this end, we introduce DexMimicGen, a large-scale automated data generation system that synthesizes trajectories from a handful of human demonstrations for humanoid robots with dexterous hands. We present a collection of simulation environments in the setting of bimanual dexterous manipulation, spanning a range of manipulation behaviors and different requirements for coordination among the two arms. We generate 21K demos across these tasks from just 60 source human demos and study the effect of several data generation and policy learning decisions on agent performance. Finally, we present a real-to-sim-to-real pipeline and deploy it on a real-world humanoid can sorting task. Generated datasets, simulation environments and additional results are at https://dexmimicgen.github.io/

## 核心内容
Imitation learning from human demonstrations is an effective means to teach robots manipulation skills. But data acquisition is a major bottleneck in applying this paradigm more broadly, due to the amount of cost and human effort involved. There has been significant interest in imitation learning for bimanual dexterous robots, like humanoids. Unfortunately, data collection is even more challenging here due to the challenges of simultaneously controlling multiple arms and multi-fingered hands. Automated data generation in simulation is a compelling, scalable alternative to fuel this need for data. To this end, we introduce DexMimicGen, a large-scale automated data generation system that synthesizes trajectories from a handful of human demonstrations for humanoid robots with dexterous hands. We present a collection of simulation environments in the setting of bimanual dexterous manipulation, spanning a range of manipulation behaviors and different requirements for coordination among the two arms. We generate 21K demos across these tasks from just 60 source human demos and study the effect of several data generation and policy learning decisions on agent performance. Finally, we present a real-to-sim-to-real pipeline and deploy it on a real-world humanoid can sorting task. Generated datasets, simulation environments and additional results are at https://dexmimicgen.github.io/

## 参考
- http://arxiv.org/abs/2410.24185v2

