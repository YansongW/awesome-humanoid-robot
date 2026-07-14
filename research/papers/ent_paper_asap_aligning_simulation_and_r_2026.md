---
$id: ent_paper_asap_aligning_simulation_and_r_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills'
  zh: sim-to-real 对齐不是调参数那么简单
  ko: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills'
summary:
  en: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills is a knowledge node
    related to paper in the humanoid robot value chain.'
  zh: Humanoid robots hold the potential for unparalleled versatility in performing human-like, whole-body skills. However,
    achieving agile and coordinated whole-body motions remains a significant challenge due to the dynamics mismatch between
    simulation and the real world. Existing approaches, such as system identification (SysID) and domain randomization (DR)
    methods, often rely on labor-intensive parameter tuning or result in overly conservative policies that sacrifice agility.
    In this paper, we present ASAP (Aligning Simulation and Real-World Physics), a two-stage framework designed to tackle
    the dynamics mismatch and enable agile humanoid whole-body skills. In the first stage, we pre-train motion tracking policies
    in simulation using retargeted human motion data. In the second stage, we dep
  ko: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills is a knowledge node
    related to paper in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- sim_to_real
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.01143v3.
sources:
- id: src_001
  type: paper
  title: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills (arXiv)'
  url: https://arxiv.org/abs/2502.01143
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: sim-to-real 对齐不是调参数那么简单 project page
  url: https://agile.human2humanoid.com
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Humanoid robots hold the potential for unparalleled versatility in performing human-like, whole-body skills. However, achieving agile and coordinated whole-body motions remains a significant challenge due to the dynamics mismatch between simulation and the real world. Existing approaches, such as system identification (SysID) and domain randomization (DR) methods, often rely on labor-intensive parameter tuning or result in overly conservative policies that sacrifice agility. In this paper, we present ASAP (Aligning Simulation and Real-World Physics), a two-stage framework designed to tackle the dynamics mismatch and enable agile humanoid whole-body skills. In the first stage, we pre-train motion tracking policies in simulation using retargeted human motion data. In the second stage, we deploy the policies in the real world and collect real-world data to train a delta (residual) action model that compensates for the dynamics mismatch. Then, ASAP fine-tunes pre-trained policies with the delta action model integrated into the simulator to align effectively with real-world dynamics. We evaluate ASAP across three transfer scenarios: IsaacGym to IsaacSim, IsaacGym to Genesis, and IsaacGym to the real-world Unitree G1 humanoid robot. Our approach significantly improves agility and whole-body coordination across various dynamic motions, reducing tracking error compared to SysID, DR, and delta dynamics learning baselines. ASAP enables highly agile motions that were previously difficult to achieve, demonstrating the potential of delta action learning in bridging simulation and real-world dynamics. These results suggest a promising sim-to-real direction for developing more expressive and agile humanoids.

## 核心内容
Humanoid robots hold the potential for unparalleled versatility in performing human-like, whole-body skills. However, achieving agile and coordinated whole-body motions remains a significant challenge due to the dynamics mismatch between simulation and the real world. Existing approaches, such as system identification (SysID) and domain randomization (DR) methods, often rely on labor-intensive parameter tuning or result in overly conservative policies that sacrifice agility. In this paper, we present ASAP (Aligning Simulation and Real-World Physics), a two-stage framework designed to tackle the dynamics mismatch and enable agile humanoid whole-body skills. In the first stage, we pre-train motion tracking policies in simulation using retargeted human motion data. In the second stage, we deploy the policies in the real world and collect real-world data to train a delta (residual) action model that compensates for the dynamics mismatch. Then, ASAP fine-tunes pre-trained policies with the delta action model integrated into the simulator to align effectively with real-world dynamics. We evaluate ASAP across three transfer scenarios: IsaacGym to IsaacSim, IsaacGym to Genesis, and IsaacGym to the real-world Unitree G1 humanoid robot. Our approach significantly improves agility and whole-body coordination across various dynamic motions, reducing tracking error compared to SysID, DR, and delta dynamics learning baselines. ASAP enables highly agile motions that were previously difficult to achieve, demonstrating the potential of delta action learning in bridging simulation and real-world dynamics. These results suggest a promising sim-to-real direction for developing more expressive and agile humanoids.

## 参考
- http://arxiv.org/abs/2502.01143v3

