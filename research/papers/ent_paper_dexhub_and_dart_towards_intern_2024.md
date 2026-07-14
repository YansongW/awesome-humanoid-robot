---
$id: ent_paper_dexhub_and_dart_towards_intern_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexHub and DART: Towards Internet-Scale Robot Data Collection'
  zh: 'DexHub and DART: Towards Internet-Scale Robot Data Collection'
  ko: 'DexHub and DART: Towards Internet-Scale Robot Data Collection'
summary:
  en: 'DexHub and DART: Towards Internet-Scale Robot Data Collection is a 2024 work on manipulation for humanoid robots.'
  zh: 'DexHub and DART: Towards Internet-Scale Robot Data Collection is a 2024 work on manipulation for humanoid robots.'
  ko: 'DexHub and DART: Towards Internet-Scale Robot Data Collection is a 2024 work on manipulation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dexhub_and_dart
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.02214v1.
sources:
- id: src_001
  type: paper
  title: 'DexHub and DART: Towards Internet-Scale Robot Data Collection (arXiv)'
  url: https://arxiv.org/abs/2411.02214
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'DexHub and DART: Towards Internet-Scale Robot Data Collection project page'
  url: https://dexhub.ai/project
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
The quest to build a generalist robotic system is impeded by the scarcity of diverse and high-quality data. While real-world data collection effort exist, requirements for robot hardware, physical environment setups, and frequent resets significantly impede the scalability needed for modern learning frameworks. We introduce DART, a teleoperation platform designed for crowdsourcing that reimagines robotic data collection by leveraging cloud-based simulation and augmented reality (AR) to address many limitations of prior data collection efforts. Our user studies highlight that DART enables higher data collection throughput and lower physical fatigue compared to real-world teleoperation. We also demonstrate that policies trained using DART-collected datasets successfully transfer to reality and are robust to unseen visual disturbances. All data collected through DART is automatically stored in our cloud-hosted database, DexHub, which will be made publicly available upon curation, paving the path for DexHub to become an ever-growing data hub for robot learning. Videos are available at: https://dexhub.ai/project

## 核心内容
The quest to build a generalist robotic system is impeded by the scarcity of diverse and high-quality data. While real-world data collection effort exist, requirements for robot hardware, physical environment setups, and frequent resets significantly impede the scalability needed for modern learning frameworks. We introduce DART, a teleoperation platform designed for crowdsourcing that reimagines robotic data collection by leveraging cloud-based simulation and augmented reality (AR) to address many limitations of prior data collection efforts. Our user studies highlight that DART enables higher data collection throughput and lower physical fatigue compared to real-world teleoperation. We also demonstrate that policies trained using DART-collected datasets successfully transfer to reality and are robust to unseen visual disturbances. All data collected through DART is automatically stored in our cloud-hosted database, DexHub, which will be made publicly available upon curation, paving the path for DexHub to become an ever-growing data hub for robot learning. Videos are available at: https://dexhub.ai/project

## 参考
- http://arxiv.org/abs/2411.02214v1

