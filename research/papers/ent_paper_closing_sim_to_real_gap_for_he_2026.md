---
$id: ent_paper_closing_sim_to_real_gap_for_he_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation
  zh: 带负载的人形机器人不是同一个系统
  ko: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation
summary:
  en: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation is a knowledge node
    related to paper in the humanoid robot value chain.
  zh: Humanoid robots deployed in real-world scenarios often need to carry unknown payloads, which introduce significant mismatch
    and degrade the effectiveness of simulation-to-reality reinforcement learning methods. To address this challenge, we propose
    a two-stage gradient-based system identification framework built on the differentiable simulator MuJoCo XLA. The first
    stage calibrates the nominal robot model using real-world data to reduce intrinsic sim-to-real discrepancies, while the
    second stage further identifies the mass distribution of the unknown payload. By explicitly reducing structured model
    bias prior to policy training, our approach enables zero-shot transfer of reinforcement learning policies to hardware
    under heavy-load conditions. Extensive simulation and real-world experiments
  ko: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation is a knowledge node
    related to paper in the humanoid robot value chain.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- compliance
- contact_rich
- fall_recovery
- load_carrying
- safety
- whole_body_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.15084v1.
sources:
- id: src_001
  type: paper
  title: Closing Sim-to-Real Gap for Heavy-loaded Humanoid Agile Motion Skills via Differentiable Simulation (arXiv)
  url: https://arxiv.org/abs/2603.15084
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 带负载的人形机器人不是同一个系统 project page
  url: https://mwondering.github.io/halo-humanoid/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Humanoid robots deployed in real-world scenarios often need to carry unknown payloads, which introduce significant mismatch and degrade the effectiveness of simulation-to-reality reinforcement learning methods. To address this challenge, we propose a two-stage gradient-based system identification framework built on the differentiable simulator MuJoCo XLA. The first stage calibrates the nominal robot model using real-world data to reduce intrinsic sim-to-real discrepancies, while the second stage further identifies the mass distribution of the unknown payload. By explicitly reducing structured model bias prior to policy training, our approach enables zero-shot transfer of reinforcement learning policies to hardware under heavy-load conditions. Extensive simulation and real-world experiments demonstrate more precise parameter identification, improved motion tracking accuracy, and substantially enhanced agility and robustness compared to existing baselines. Project Page: https://mwondering.github.io/halo-humanoid/

## 核心内容
Humanoid robots deployed in real-world scenarios often need to carry unknown payloads, which introduce significant mismatch and degrade the effectiveness of simulation-to-reality reinforcement learning methods. To address this challenge, we propose a two-stage gradient-based system identification framework built on the differentiable simulator MuJoCo XLA. The first stage calibrates the nominal robot model using real-world data to reduce intrinsic sim-to-real discrepancies, while the second stage further identifies the mass distribution of the unknown payload. By explicitly reducing structured model bias prior to policy training, our approach enables zero-shot transfer of reinforcement learning policies to hardware under heavy-load conditions. Extensive simulation and real-world experiments demonstrate more precise parameter identification, improved motion tracking accuracy, and substantially enhanced agility and robustness compared to existing baselines. Project Page: https://mwondering.github.io/halo-humanoid/

## 参考
- http://arxiv.org/abs/2603.15084v1

